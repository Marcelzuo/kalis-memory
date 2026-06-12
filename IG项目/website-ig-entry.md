# 独立网站 IG 入口 — 线上最新配置（2026-06-12）

## IG 账号
`https://www.instagram.com/1980zuo/`

## 入口位置（index.html）

### 1. 导航栏社交图标（L620）
```html
<a href="https://www.instagram.com/1980zuo/" target="_blank" rel="noopener"
   aria-label="Instagram" class="nav-social-icon nav-social-ig"
   data-i18n-aria="social_ig_aria">
```

### 2. Contact 区社交卡片（L958）
```html
<a href="https://www.instagram.com/1980zuo/" target="_blank" rel="noopener"
   class="social-card social-ig">
```

### 3. CSS 品牌色（L233-234）
```css
.social-ig .social-card-cta{color:#E4405F;border-color:#E4405F}
.social-ig:hover .social-card-cta{background:#E4405F;color:#fff}
```

### 4. 多语言标签
- `social_ig_aria`: "Instagram"（所有语言共用）

## IG 专属着陆页

- URL: `https://kalistorik.com/social-ig.html`（nginx 服务器）
- 独立 SEO 页面，含完整 OG/Twitter Card、hreflang 7 语
- 带 "Open Instagram" CTA 按钮引导到 `instagram.com/1980zuo/`
- 完整快照: `website-social-ig-2026-06-12.html`

## 部署位置
- **Nginx 服务器**: `/www/wwwroot/kalistorik.com/social-ig.html`
- **源文件**: `~/kalistorik-site/`（build → dist_lang → deploy.sh）
- **CF Pages**: 同步部署（wrangler --branch=main）

## 最后更新
2026-06-11 22:39 — 撒旦修复 4 个社媒入口 bug，含 IG 链接修正
