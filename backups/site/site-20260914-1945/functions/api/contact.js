/**
 * Cloudflare Pages Function
 * POST /api/contact
 *
 * 接收 Kalistorik contact 表单提交，通过 Zoho SMTP 转发邮件到 hello@kalistorik.com。
 *
 * 环境变量（需米迦勒在 Cloudflare Pages 项目设置里配置）：
 *   ZOHO_SMTP_PASSWORD  - Zoho SMTP 专用密码（不是登录密码）
 *   ZOHO_SMTP_USER      - （可选）发件账户，默认 hello@kalistorik.com
 *
 * 依赖：nodemailer（需在仓库根目录 package.json 中声明并部署时安装）
 */

import nodemailer from 'nodemailer';

// --- 简单 HTML 转义，防 XSS 注入到邮件正文 ---
function escapeHtml(str) {
  if (str === undefined || str === null) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// --- 简单必填校验 ---
function validate(fields) {
  const errors = [];
  if (!fields.name || fields.name.trim().length < 1) errors.push('name');
  if (!fields.email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(fields.email)) errors.push('email');
  if (!fields.message || fields.message.trim().length < 1) errors.push('message');
  return errors;
}

export async function onRequestPost(context) {
  const { request } = context;

  // CORS 预检（如果以后改成 fetch 直接发，要 preflight）
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      status: 204,
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      },
    });
  }

  try {
    // 1. 解析 form-urlencoded
    const contentType = request.headers.get('content-type') || '';
    let raw = {};
    if (contentType.includes('application/x-www-form-urlencoded')) {
      const text = await request.text();
      const params = new URLSearchParams(text);
      for (const [k, v] of params.entries()) raw[k] = v;
    } else if (contentType.includes('application/json')) {
      raw = await request.json();
    } else {
      return jsonResponse({ success: false, error: 'Unsupported Content-Type' }, 415);
    }

    const fields = {
      name: (raw.name || '').trim(),
      company: (raw.company || '').trim(),
      email: (raw.email || '').trim(),
      whatsapp: (raw.whatsapp || '').trim(),
      product: (raw.product || '').trim(),
      message: (raw.message || '').trim(),
      lang: (raw.lang || 'en').trim(),
    };

    // 2. 校验
    const missing = validate(fields);
    if (missing.length > 0) {
      return jsonResponse(
        { success: false, error: `Missing or invalid fields: ${missing.join(', ')}` },
        400
      );
    }

    // 3. 邮件账户（SMTP 密码走环境变量）
    const smtpUser = context.env.ZOHO_SMTP_USER || 'hello@kalistorik.com';
    const smtpPass = context.env.ZOHO_SMTP_PASSWORD;

    if (!smtpPass) {
      // 没配密码 = 配置错误，立刻返回，不暴露内部细节
      console.error('ZOHO_SMTP_PASSWORD is not set in CF Pages env');
      return jsonResponse(
        { success: false, error: 'Mail server is not configured. Please contact the site admin.' },
        500
      );
    }

    // 4. 构造 nodemailer transport（Zoho SSL 465）
    const transporter = nodemailer.createTransport({
      host: 'smtp.zoho.com',
      port: 465,
      secure: true, // SSL
      auth: {
        user: smtpUser,
        pass: smtpPass,
      },
    });

    // 5. 邮件正文（HTML + 纯文本双版本）
    const safe = {
      name: escapeHtml(fields.name),
      company: escapeHtml(fields.company),
      email: escapeHtml(fields.email),
      whatsapp: escapeHtml(fields.whatsapp),
      product: escapeHtml(fields.product),
      message: escapeHtml(fields.message).replace(/\n/g, '<br>'),
      lang: escapeHtml(fields.lang),
      submittedAt: escapeHtml(new Date().toISOString()),
    };

    const subject = `[Kalistorik Contact] ${safe.name} — ${safe.product || 'general'}`;

    const textBody = `
New contact form submission
---------------------------
Name:      ${fields.name}
Company:   ${fields.company || '-'}
Email:     ${fields.email}
WhatsApp:  ${fields.whatsapp || '-'}
Product:   ${fields.product || '-'}
Language:  ${fields.lang}
Submitted: ${new Date().toISOString()}

Message:
${fields.message}
`.trim();

    const htmlBody = `
<!doctype html>
<html>
  <body style="font-family: -apple-system, system-ui, sans-serif; color:#222; line-height:1.5;">
    <h2 style="color:#C8102E; margin-bottom:0;">New Contact Form Submission</h2>
    <p style="color:#888; margin-top:4px;">Received ${safe.submittedAt}</p>
    <table cellpadding="6" style="border-collapse:collapse;">
      <tr><td><b>Name</b></td><td>${safe.name}</td></tr>
      <tr><td><b>Company</b></td><td>${safe.company || '-'}</td></tr>
      <tr><td><b>Email</b></td><td><a href="mailto:${safe.email}">${safe.email}</a></td></tr>
      <tr><td><b>WhatsApp</b></td><td>${safe.whatsapp || '-'}</td></tr>
      <tr><td><b>Product</b></td><td>${safe.product || '-'}</td></tr>
      <tr><td><b>Language</b></td><td>${safe.lang}</td></tr>
    </table>
    <h3>Message</h3>
    <div style="white-space:pre-wrap; padding:12px; background:#f6f6f6; border-left:3px solid #C8102E;">
${safe.message}
    </div>
  </body>
</html>`.trim();

    // 6. 发件人 = SMTP 账户；Reply-To = 填表人，方便直接回
    const mailOptions = {
      from: `"Kalistorik Site" <${smtpUser}>`,
      to: 'hello@kalistorik.com',
      replyTo: fields.email,
      subject,
      text: textBody,
      html: htmlBody,
    };

    await transporter.sendMail(mailOptions);

    return jsonResponse({ success: true }, 200);
  } catch (err) {
    console.error('Contact form error:', err);
    return jsonResponse(
      { success: false, error: 'Failed to send message. Please try again later.' },
      500
    );
  }
}

// 其它方法直接 405
export async function onRequest(context) {
  if (context.request.method === 'POST' || context.request.method === 'OPTIONS') {
    return onRequestPost(context);
  }
  return jsonResponse({ success: false, error: 'Method Not Allowed' }, 405, {
    Allow: 'POST, OPTIONS',
  });
}

function jsonResponse(payload, status = 200, extraHeaders = {}) {
  return new Response(JSON.stringify(payload), {
    status,
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*',
      ...extraHeaders,
    },
  });
}