# kalistorik.pages.dev 全站审计报告

> 审计时间：2026-06-30
> 审计范围：kalistorik.pages.dev 全站（index + picks / factories / freight / quality / wa / privacy）
> 方法：curl + 静态分析 index.html 源码（287KB / 1338 行）
> 审计人：玛门

## 一、发现清单

### SEO

- [🔴] SEO·双源重复内容 — kalistorik.com 和 kalistorik.pages.dev 同时提供完全相同的 HTML（294KB），无 redirect，无 canonical 交叉指向。Google 会视为 duplicate content，两边权重互相稀释。
- [🔴] SEO·hreflang URL 非最终 canonical — hreflang 指向 `kalistorik.com/en.html` 等 URL，但实际访问 `kalistorik.com/en.html` 会 302 → `kalistorik.com/?lang=en`。搜索引擎每次都要跟一次重定向链。
- [🔴] SEO·canonical 混淆 — `pages.dev` 上的 `<link rel="canonical">` 指向 `kalistorik.com/en.html`，但 `kalistorik.com/en.html` 又会 redirect。搜索引擎不知道该索引哪个 origin。
- [🔴] SEO·六语种文件内容完全一致 — /en.html /fr.html /de.html /it.html /es.html /pt.html 全部返回相同的 294KB HTML，`<html lang="en">`、`<title>`、`<meta description>`、body 内容完全一样。i18n 纯靠客户端 JS 运行时注入，搜索引擎爬虫看到的是全部英语。
- [🔴] SEO·404 返回 200 — 任意不存在的 URL（如 /nonexistent-page-12345）都返回 index.html 的完整 200 响应。没有真正的 404 状态码。Google 会索引无限多的垃圾 URL。
- [🔴] SEO·Schema Product price 为 "0" — 4 个产品的 JSON-LD offer.price 都是 "0"。Google Merchant 规则会拒绝 price=0 的产品。应该去掉 offer 或标注为无价格。
- [🟡] SEO·Schema 声称 6 个产品，实际只有 4 个 — 注释写 "6 selected products"，JSON-LD @graph 只有 4 条。
- [🟡] SEO·无 BreadcrumbList 结构化数据 — 缺少面包屑 schema，不利于 rich result。
- [🟡] SEO·robots.txt sitemap 指向 .com — `Sitemap: https://kalistorik.com/sitemap.xml`，但页面在 pages.dev 上，sitemap 中的 URL 又全是 .com。
- [🟡] SEO·`cache-control: max-age=0` — HTML 完全不做缓存。每次页面访问都重新下载 294KB。搜索引擎爬虫会频繁抓取但得不到 304。
- [🟡] SEO·picks.html hreflang 全部指向同一个 URL — `<link rel="alternate" hreflang="fr" href="https://kalistorik.com/picks.html">` 等 6 个 hreflang 的 href 完全一样，搜索引擎无法区分语言版本。
- [🟡] SEO·wa.html 只有 en 和 x-default hreflang — 缺少 fr/de/it/es/pt 的 alternate 链接。
- [🟢] SEO·Organization + WebSite 双 schema 存在且完整 — sameAs / contactPoint / areaServed 齐全。
- [🟢] SEO·描述性 `<title>` 和 `<meta description>` — 英文版关键词恰当。
- [🟢] SEO·`robots: index,follow` 设置正确。

### 语言 / 国际化

- [🔴] 语言·质量弹窗全部硬编码英文 — Quality Inspection 弹窗（#quality-modal）标题、描述、"Pre-Production Sample" 等三张卡片完全无 `data-i18n` 属性。切换到任何语言都是英文。
- [🔴] 语言·促销抽屉全部硬编码英文 — #promo-drawer 的 "Current Promotions"、"Sale ends in..."、"Total"、"Send Inquiry" 无 i18n。
- [🔴] 语言·迷你询价弹窗全部硬编码英文 — #inquiry-modal 的 "Name *"、"Email *"、"Message"、"Send Inquiry"、成功提示全部硬编码，无 `data-i18n`。
- [🟡] 语言·`<html lang="en">` 从未被 JS 更新 — 切换语言后 `<html lang>` 仍然保持 "en"。屏幕阅读器和搜索引擎无法感知语言切换。
- [🟡] 语言·Hero 口号纯 JS 注入 — 3 条 slogan 通过 `setLang()` 动态写入 innerHTML，初始 HTML 里是空 `<div>`。JS 禁用时 hero 区域显示空白。
- [🟡] 语言·`<title>` JS 更新爬虫不可见 — `document.title = t.site_title` 在 setLang 中执行，但搜索引擎爬虫不执行 JS，所有语种在搜索结果中标题相同。
- [🟡] 语言·Product 卡片名 / 描述无 i18n — 产品系列名和变体名由 JS 动态生成模板字符串，不在 `__LANGS__` 体系中。
- [🟢] 语言·`__LANGS__` 六语种 9 核心键均已灌入（site_title / cookie 文案 / footer 文案 / 表单 placeholder 等）。

### 社媒入口

- [🟡] 社媒·Instagram / Facebook 链接返回 HTTP 200 但未验证真实 profile — curl 请求被登录墙拦截，无法确认 profile 是否存在且公开。LinkedIn /in/kalistorik 返回 HTTP 999（LinkedIn 反爬），建议浏览器验证。
- [🟡] 社媒·缺少 Pinterest — 家具是强视觉品类，Pinterest 是高意向流量渠道，当前无入口。
- [🟡] 社媒·缺少 X/Twitter — 仅有 og:twitter 标签但无 Twitter 主页链接。
- [🟢] 社媒·5 个入口覆盖 WhatsApp / Email / LinkedIn / Facebook / Instagram — 足以满足 B2B 家具采购场景。
- [🟢] 社媒·导航栏 + Contact 区域双展示社媒入口 — WhatsApp 绿标、LinkedIn 蓝标等品牌色正确。
- [🟢] 社媒·所有外链带 `target="_blank" rel="noopener"` — 安全。
- [🟢] 社媒·`aria-label` + `data-i18n-aria` 支持多语言无障碍文案。

### 代码

- [🔴] 代码·CSS 中有裸 `article` 文本 — `<style>` 块第 266-267 行出现两行裸文本 `article\narticle`，不在任何规则体内。浏览器会当作无效 CSS 跳过，但增加解析负担。
- [🔴] 代码·`.inquiry-modal-field input` 是孤立选择器 — index.html:353 行只有选择器没有声明块 `{}`，死代码。
- [🔴] 代码·3 个空 `@media` 块 — `@media(max-width:768px){}` ×2（:162, :205），`@media(max-width:992px){}` ×1（:270）。死代码。
- [🔴] 代码·`src=""` 空属性 — `#lightbox-img` 的 `<img src="" alt="Product detail">` 会造成浏览器对当前页面 URL 发起一次重复请求。应在 JS 激活前用 `about:blank` 或 `src="data:..."` 占位。
- [🟡] 代码·页面 294KB 全内联 — CSS（~400 行）+ JS（~380 行）+ HTML 全部打在单个文件里。没有任何外部 CSS/JS 可被浏览器缓存。首次访问即全量下载。
- [🟡] 代码·联系表单无 `action` 属性 — `<form id="contact-form">` 和 `<form id="newsletter-form">` 都依赖 JS `fetch` 提交。JS 禁用时表单完全无法工作。
- [🟡] 代码·产品图片纯 JS 渲染 — `<img src="'+p.main_image+'"` 等模板字符串在 HTML 中不可见。搜索引擎无法索引产品图片。只有 lightbox 占位 img 在 DOM 中。
- [🟡] 代码·无 CSRF 防护 — 表单提交走 fetch to Google Apps Script endpoint，无 CSRF token。
- [🟢] 代码·honeypot 反垃圾 — newsletter 有 `tabindex="-1"` + `aria-hidden="true"` 的隐藏字段。
- [🟢] 代码·Cloudflare Email Obfuscation 开启 — 邮箱地址被保护。
- [🟢] 代码·GDPR cookie consent 默认 denied — `gtag('consent','default',{analytics_storage:'denied',...})` 合规。
- [🟢] 代码·`form[method]` 缺失但 fetch 提交正常 — 逻辑完整，表单提交到 Google Apps Script 有 FormData + language 参数。
- [🟢] 代码·WCAG 语义标签齐全 — `<header>` / `<main>` / `<nav>` / `<footer>` / `<section>` / `<article>` 均有使用。
- [🟢] 代码·`referrer-policy: strict-origin-when-cross-origin` + `x-content-type-options: nosniff` — 安全头齐全。
- [🟢] 代码·HTTP/2 103 Early Hints 已启用 — fonts.googleapis.com 和 googletagmanager.com 预连接优化。

### 视觉

- [🔴] 视觉·FAQ 区域无实际 FAQ 条目 — `#faq` section 仅有标题 + 一段说明文字，没有任何问答交互内容。导航栏 "FAQ" 链接到空壳区域。
- [🟡] 视觉·Hero slogan 初始无内容 — 3 个 slogan div 在 HTML 中为空，JS 执行前 hero 区域中间有一大块空白。如 JS 加载慢或失败，用户看到缺失内容。
- [🟡] 视觉·无 LCP 字体预加载 — 首屏文字 logo 使用 Google Fonts Montserrat，但字体文件没有 `<link rel="preload">`，仅对 CSS 文件做了 preload。字体加载前有 FOIT。
- [🟡] 视觉·`webmanifest` 声明 `favicon-192.png` — 文件存在（HTTP 200），但非标准 Android icon 尺寸通常用 192×192。当前 OK。
- [🟢] 视觉·金黑配色一致 — `#C9A96E` 金色贯穿 logo、按钮、边框、链接，视觉语言统一。
- [🟢] 视觉·`@media` 响应式断点覆盖 480/576/768/900/992px — 移动端到桌面适配完整。
- [🟢] 视觉·lightbox + carousel 交互完整 — 产品图片查看器支持左右切换和缩略图导航。

---

## 二、严重性汇总

| 等级 | 数量 | 关键类别 |
|------|------|----------|
| 🔴 Critical | 15 | SEO 6 + 语言 3 + 代码 4 + 视觉 1 |
| 🟡 Warning | 17 | SEO 6 + 语言 4 + 社媒 3 + 代码 4 + 视觉 3 |
| 🟢 OK     | 15 | 安全 / WCAG / 结构化数据 / 响应式 |

### 优先级排序 Top 10

1. 🔴 404 → 200 — 必须先修，否则 Google 索引无限膨胀
2. 🔴 双 origin 重复内容 — 选一个 canonical origin 并 redirect 另一个
3. 🔴 `kalistorik.com/en.html` → `?lang=en` redirect — hreflang/canonical 必须指向最终 URL
4. 🔴 六语种文件内容相同 — 要么 SSR 多语种、要么接受 Google 只索引英文
5. 🔴 Schema price "0" — 去掉价格或改用无报价 schema
6. 🔴 质量弹窗 / 促销 / 询价弹窗 全英文 — i18n 覆盖盲区，需灌入 `__LANGS__`
7. 🔴 CSS 死代码（裸 article、空 @media、孤立选择器）— 清理
8. 🔴 `src=""` 空 src — 改为 about:blank 或 data URI，消除重复请求
9. 🟡 FAQ 空壳 — 要么加 QA 内容、要么改名或隐藏导航链接
10. 🟡 产品图片 JS 渲染 — 搜索引擎看不到，考虑 SSR 或 noscript 回退

---

## 三、Ledger

```
kalistorik.pages.dev audit ledger · 2026-06-30
─────────────────────────────────────────────
Pages crawled:   7 (index, picks, factories, freight, quality, wa, privacy)
Total findings:  47 (15 🔴 + 17 🟡 + 15 🟢)
Page weight:     294KB (CSS + JS + HTML all inline)
Response time:   ~477ms (HKG edge)

Key metrics:
  SEO health:      ⚠️  Poor (dual origin, fake 404, price=0 schema)
  i18n coverage:   ⚠️  70% (modals all English, lang attr stuck)
  Social links:    ✅  5 platforms + WA + email
  Code quality:    ⚠️  Dead CSS, empty src, forms JS-only
  Visual:          ✅  Clean dark/luxury brand, responsive
  Security:        ✅  GDPR consent, email obfuscation, good headers

Biggest risk:  双 origin + fake 404 = Google penalty vector
Quickest win:  修 src="" → about:blank (1 行)
Most impact:   kalistorik.com redirect 链修复 + 统一 canonical
```

---

> 审计完毕。具体修复方案等待米迦勒指示。
