# 撒旦派活 — 2026-06-11 修复 Facebook 入口

**派活人**: 撒旦（地狱三人组统筹）
**触发**: 老板 17:00「测试网站里所有的 Facebook 入口是否代码正确，以及连接畅通，有问题不用问我，直接及时修复，最后给我结果就行」
**状态**: 撒旦已暂停，等米迦勒做完

---

## 撒旦已挖到的问题（线上 Pages 部署层 = 米迦勒领地）

| # | 文件 | 当前 | 应改为 |
|---|------|------|--------|
| 1 | `kalis/dist/social-fb.html` | **85 字节占位** | 本地完整源 17KB |
| 2 | `kalis/dist/social-ig.html` | **85 字节占位** | 本地完整源 |
| 3 | `kalis/dist/social-wa.html` | **85 字节占位** | 本地完整源 |
| 4 | `kalis/dist/index.html` line 623 附近 | FB/IG/WA nav `onclick="return false;"` "Coming Soon" | 启用态，链接到 `/social-{fb,ig,wa}.html` |

**测试证据**：
- `curl -I https://kalistorik.com/social-fb.html` → 301 → `/404` ❌
- `curl -I https://kalistorik.com/social-fb` → 200 ✅（说明文件存在但 .html 后缀处理不对）
- DNS 切到 Cloudflare Pages（172.67.209.104 / 104.21.45.40），生产走 Pages

---

## 必须修复（4 项）

### 1. social-fb.html 完整源覆盖
```bash
cp /Users/zuo/.openclaw/workspace/social-fb.html /Users/zuo/.openclaw/workspace/kalis/dist/social-fb.html
```

### 2. social-ig.html + social-wa.html 同样覆盖
```bash
cp /Users/zuo/.openclaw/workspace/social-ig.html /Users/zuo/.openclaw/workspace/kalis/dist/social-ig.html
cp /Users/zuo/.openclaw/workspace/social-wa.html /Users/zuo/.openclaw/workspace/kalis/dist/social-wa.html
```

### 3. 主页 nav 启用 FB/IG/WA
- 文件：`/Users/zuo/.openclaw/workspace/kalis/dist/index.html`
- 找 `onclick="return false"` 和 `title="Coming Soon"` 的 nav social icon
- 删 `onclick="return false"` + `nav-social-disabled` class + 改 `href="#"` → `href="/social-{fb,ig,wa}.html"`
- 参考本地源：`/Users/zuo/.openclaw/workspace/index.html` line 623 区域

### 4. 重新部署 Pages
```bash
cd /Users/zuo/.openclaw/workspace/kalis && wrangler pages deploy dist/ --project-name=kalistorik
```

---

## ✅ 你做完顺手验（避免来回）

- `curl -sI https://kalistorik.com/social-fb.html` → 200
- `curl -sI https://kalistorik.com/social-ig.html` → 200
- `curl -sI https://kalistorik.com/social-wa.html` → 200
- 主页 nav FB/IG/WA icon 不再有 `onclick="return false"` 或 "Coming Soon"
- 主页所有 `href="/social-fb.html"` 真实可达

---

## 📤 撒旦最终验收（米迦勒做完通知我）

撒旦会跑：
- grep `<link rel="alternate" hreflang` 在 social-fb/ig/wa.html 各 7 个（6 语 + x-default）
- curl 6 语 + 默认 共 7 个 URL 全 200
- curl 旧地址 `/facebook.html` `/instagram.html` `/whatsapp.html` 全 301 → 新地址
- 主页 `<a href="/social-fb.html"` 至少 1 处
- MD5 三验：本地 dist 源 = Pages 线上 = wrangler 上传包

---

## ⏱️ 时间窗口

30 分钟内。超时在 feedback/ 写 `2026-06-11-fb-entry-fix-OVERTIME.md` 原因。

---

## 老板原话

> "你告诉我让他做什么就行了。"
