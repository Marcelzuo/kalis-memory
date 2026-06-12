# 📋 派活米迦勒：修复 kalistorik.com Facebook 入口

**来自**：撒旦（统筹+验收）
**触发**：老板 2026-06-11 17:08 下任务"测试网站里所有的 Facebook 入口是否代码正确，以及连接畅通，有问题不用问我，直接及时修复"
**状态**：撒旦已暂停，等米迦勒做完

---

## 🎯 任务清单（4 项必做 + 1 项顺手）

### 1. `kalis/dist/social-fb.html` 替换为完整 HTML
- **当前**：`kalis/dist/social-fb.html` = **85 字节占位文件**（6/10 部署时的占位）
- **改成**：用本地完整源 `/Users/zuo/.openclaw/workspace/social-fb.html`（17KB）覆盖
- **命令**：
  ```bash
  cp /Users/zuo/.openclaw/workspace/social-fb.html /Users/zuo/.openclaw/workspace/kalis/dist/social-fb.html
  ```

### 2. 主页 FB nav 启用
- **文件**：`kalis/dist/index.html` line 623 附近
- **当前**（关闭态）：
  ```html
  <a href="#" target="_blank" rel="noopener" aria-label="Facebook" class="nav-social-icon nav-social-fb nav-social-disabled" data-i18n-aria="social_fb_aria" title="Coming Soon" onclick="return false;">
  ```
- **改成**（启用态）：
  ```html
  <a href="/social-fb.html" target="_blank" rel="noopener" aria-label="Facebook" class="nav-social-icon nav-social-fb" data-i18n-aria="social_fb_aria">
  ```
- **参考**：`/Users/zuo/.openclaw/workspace/index.html` line 623

### 3. 同步修复 IG/WA 子页（顺便修）
- `kalis/dist/social-ig.html`、`kalis/dist/social-wa.html` 同为 85 字节占位
- 主页 nav IG/WA icon 同为"Coming Soon" 关闭态
- 完整源：`/Users/zuo/.openclaw/workspace/social-{ig,wa}.html`
- 同样用本地源覆盖 + 主页 nav 启用

### 4. 重新部署 Pages
```bash
cd /Users/zuo/.openclaw/workspace/kalis && wrangler pages deploy dist/ --project-name=kalistorik
```

---

## ✅ 自验清单（你做完顺手验一下）

- `curl -sI https://kalistorik.com/social-fb.html` → 200
- `curl -sI https://kalistorik.com/social-ig.html` → 200
- `curl -sI https://kalistorik.com/social-wa.html` → 200
- 主页 nav FB/IG/WA icon 不再有 `onclick="return false"` 或 "Coming Soon"
- 主页所有 `href="/social-fb.html"` 真实可达

---

## 📤 验收

做完跟我说一声（共享仓库 `memory/shared/` 或喊老板）。撒旦会跑最终验收：

- grep `<link rel="alternate" hreflang` 在 social-fb/ig/wa.html 各 7 个（6 语 + x-default）
- curl 6 语 + 默认 共 7 个 URL 全 200
- curl 旧地址 `/facebook.html` `/instagram.html` `/whatsapp.html` 全 301 → 新地址
- 主页 `<a href="/social-fb.html" ...>` 至少 1 处（已确认本地有 1 处）
- MD5 三验：本地 dist 源 = Pages 线上 = wrangler 上传包

---

## ⏱️ 时间窗口

建议 30 分钟内。超时在 `memory/feedback/feedback_to_michael_fb_fix_DONE.md` 写原因。

---

## 📎 老板原话

> "你告诉我让他做什么就行了。"
