# KALIS TORIK — 部署操作手册（已验证方法）

> 天使长 Michael 整理 | 2026-06-12

## 部署网站到 Cloudflare Pages

```bash
cd ~/kalistorik-site
wrangler pages deploy dist/ --project-name kalistorik --branch master
```

部署完成后 `kalistorik.com` 自动生效（DNS 已指向 Pages，无需额外操作）。

## DNS 管理（Cloudflare Dashboard API）

Token 的 `wrangler` OAuth 没有 `dns:write`，**唯一可用路径**：通过 `opencli browser` + Cloudflare Dashboard 内部 API。

```bash
# 1. 打开 DNS 管理页（首次认证用）
opencli browser cf open "https://dash.cloudflare.com/bd85d282f224fc36aac152d7f72cfb2d/kalistorik.com/dns"

# 2. 列出 A 记录
opencli browser cf eval "
(async () => {
  const resp = await fetch('/api/v4/zones/0aaed943cf228188f24edf16ee1a83e8/dns_records?type=A');
  const data = await resp.json();
  return JSON.stringify(data.result.map(r => ({id: r.id, name: r.name, content: r.content})));
})()
"

# 3. 删除记录
opencli browser cf eval "
(async () => {
  const resp = await fetch('/api/v4/zones/0aaed943cf228188f24edf16ee1a83e8/dns_records/RECORD_ID', {method:'DELETE'});
  return await resp.json();
})()
"

# 4. 创建 CNAME（proxied）
opencli browser cf eval "
(async () => {
  const resp = await fetch('/api/v4/zones/0aaed943cf228188f24edf16ee1a83e8/dns_records', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({type:'CNAME', name:'kalistorik.com', content:'kalistorik.pages.dev', proxied:true})
  });
  return await resp.json();
})()
"
```

## 关键信息

| 项目 | 值 |
|------|-----|
| Cloudflare Account ID | `bd85d282f224fc36aac152d7f72cfb2d` |
| Zone ID | `0aaed943cf228188f24edf16ee1a83e8` |
| Pages 项目名 | `kalistorik` |
| Pages 域名 | `kalistorik.pages.dev` |
| 自定义域名 | `kalistorik.com` (CNAME → `kalistorik.pages.dev`, proxied) |
| GitHub | `https://github.com/Marcelzuo/kalistorik-site.git` |
| Google Analytics | `G-YRPEYWWLM1` |
| WhatsApp | `+8613602222361` |

## 注意事项

- `wrangler` OAuth token 无 `dns:write` 权限，DNS 操作**必须走浏览器 Dashboard API**
- `dist/` 目录在 `.gitignore` 中，仅用于部署，不提交 Git
- 旧 SCP nginx 部署路径已作废，以后只走 Cloudflare Pages
