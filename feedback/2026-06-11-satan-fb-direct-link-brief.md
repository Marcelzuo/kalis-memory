# 撒旦派活 — 2026-06-11 FB 入口改直链（方案自定）

**派活人**: 撒旦
**触发**: 老板 17:27 反馈：从网站 FB 入口点进去不是直接到 Facebook 账号，而是站内中间页（social-fb.html），「这个存在是完全没有意义的」「所有 FB 入口都要直链到 Facebook 账号」
**老板 17:35 追加**: 解决方案你定，不要折中，要一劳永逸

---

## 问题

`kalistorik.com` 站内的 Facebook 入口（主页 nav 等）点了之后不是直链到 `https://www.facebook.com/kalistorik`（KALIS FB 主页），而是先落到站内 `social-fb.html` 中间页。

KALIS FB 主页：`https://www.facebook.com/kalistorik`（已验证 200，title="kalis torik | Guangzhou"）

## 你来做

请你自己设计方案修。一劳永逸，不要折中。完成后撒旦验收（Playwright 点 nav FB 落地 + 截图）。

具体细节（哪些文件、哪些行）你自己看 dist/ 决定，**不要保留任何形式的中间页**。

## 撒旦已改的部分（workspace 源，不是 dist）

仅供参考，dist 在你那边，自己处理：
- `workspace/index.html:623` nav FB：`/social-fb.html` → `https://www.facebook.com/kalistorik`
- `workspace/social-fb.html:293` mobile IG 占位 → `https://instagram.com/1980zuo`
- `workspace/social-fb.html:341` CTA → `https://www.facebook.com/kalistorik`
- `workspace/social-wa.html:330/557/574` 3 处 FB 占位 → `https://www.facebook.com/kalistorik`

## 验收标准

- 主页线上点 nav FB icon → 直接跳 `https://www.facebook.com/kalistorik`（**不落任何站内页**）
- 所有站内 FB 链接 → `https://www.facebook.com/kalistorik`
- 老链接 `/social-fb` `/social-fb.html` `/facebook.html` 兜底到位（不死链）
- wrangler 部署到 main 分支

## 时间

30 分钟内。做完通知撒旦。
