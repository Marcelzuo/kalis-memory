# 路西法 SEO+i18n 审计 · kalistorik.pages.dev

**时间**: 2026-06-30T07:01:38+00:00
**范围**: kalistorik.pages.dev (源 kalistorik-site/ + curl 实时验证)
**结论**: SEO+i18n+元数据审计 kalistorik.pages.dev(磁盘源 kalistorik-site/) — 30 条问题:🔴4 🟡16 🟢10

## 实时验证结果

```
  deployment_url: https://kalistorik.pages.dev/  HTTP 200
  robots_txt: 200 OK,内容正确
  sitemap_xml: 200 OK,content-type=application/xml
  en.html_redirect: 301 → /?lang=en
  favicon_192: 200 但返回 HTML(SPA fallback,content-type=text/html)
  en_slash_path: 200 但内容是 236B 重定向壳而非 index.html
  langs_complete: 6 语言 × 140 keys 全对齐
```

## 关键文件

- kalistorik-site/index.html (287KB,1338 行,含 inline CSS+JS+__LANGS__+3 JSON-LD)
- kalistorik-site/picks.html (53KB,hreflang 全指同 URL)
- kalistorik-site/factories/freight/quality/wa/privacy.html (5 子页缺 JSON-LD+twitter tags)
- kalistorik-site/site.webmanifest (引用 /favicon-192.png 但文件缺失)
- kalistorik-site/_redirects (只映射 /xx.html,无 /xx/ 子目录)
- kalistorik-site/sitemap.xml (x-default 滥用 7 处)
- kalistorik-site/_headers (缺安全头)

## 阻断项 (🔴4)

- hreflang/picks.html:6 语言全指同 URL,Google 忽略
- hreflang/en+fr+de+it+es+pt.html 壳:无 hreflang,canonical 格式不一致
- Favicon/192:manifest 声明但磁盘无此文件,SPA fallback 返回 HTML,PWA 装不上
- 域名统一:pages.dev 部署但 SEO 信号全指 kalistorik.com(38 处)

## 完整 30 条问题清单

详见审计报告输出(JSON: /tmp/audit_findings.json)
- 🔴 4
- 🟡 16
- 🟢 10
