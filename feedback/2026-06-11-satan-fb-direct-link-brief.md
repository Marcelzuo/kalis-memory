# 撒旦派活 v2 — 2026-06-11 FB 入口改直链主页

**派活人**: 撒旦（地狱三人组统筹）
**触发**: 老板 17:27 反馈「我们从网站上的入口进去，并不是直接进入了 Facebook 的账号，而是进入了一个类似二级页面的东西，这个存在是完全没有意义的。我要求是所有的网站 Facebook 入口都是能直接链接到我的 Facebook 账号里去的。这才是个有意义的动作」
**根因**: 6/5 v14.5 部署时，4 社媒 nav 设计是直链主页（IG `1980zuo` / WA `+8613602222361` / FB `facebook.com/kalistorik`），但 6/10 你部署 v2 时把 FB nav 改回 `/social-fb`（站内中间页），违反了老板"直接到账号"的意图
**KALIS FB 主页 URL**: `https://www.facebook.com/kalistorik`（已 curl 200 验证：title="kalis torik | Guangzhou" · description="CHINESE FURNITURE SOURCING"）

---

## 老板原话（再读一遍）

> 「所有的网站 Facebook 入口都是能直接链接到我的 Facebook 账号里去的。这才是个有意义的动作」

**所有 FB 入口** = 主页 nav + 中间页内部 + 其他页里的 FB 链接，全部直链 `https://www.facebook.com/kalistorik`

---

## 必须执行（6 处替换，0 风险）

撒旦已在 `~/.openclaw/workspace/`（撒旦的源）改完 6 处，请你**同步在 `kalis/dist/` 改同样的 6 处 + wrangler 部署**：

### 1. `kalis/dist/index.html` line 623
```diff
- <a href="/social-fb" target="_blank" rel="noopener" aria-label="Facebook" class="nav-social-icon nav-social-fb" data-i18n-aria="social_fb_aria">
+ <a href="https://www.facebook.com/kalistorik" target="_blank" rel="noopener" aria-label="Facebook" class="nav-social-icon nav-social-fb" data-i18n-aria="social_fb_aria">
```

### 2. `kalis/dist/social-fb.html` line 293（mobile-only IG 占位，顺便修）
```diff
- <a href="https://instagram.com/" class="social-icon mobile-only" aria-label="Instagram" target="_blank" rel="noopener" style="display:none">
+ <a href="https://instagram.com/1980zuo" class="social-icon mobile-only" aria-label="Instagram" target="_blank" rel="noopener" style="display:none">
```

### 3. `kalis/dist/social-fb.html` line 341（CTA "Message on Facebook"）
```diff
- <a href="https://www.facebook.com/messages/" class="btn-gold" target="_blank" rel="noopener" data-i18n="cta_follow">Message on Facebook</a>
+ <a href="https://www.facebook.com/kalistorik" class="btn-gold" target="_blank" rel="noopener" data-i18n="cta_follow">Message on Facebook</a>
```

### 4. `kalis/dist/social-wa.html` line 330（社交图标区 FB）
```diff
- <a href="https://facebook.com/" class="social-icon" aria-label="Facebook" target="_blank" rel="noopener">
+ <a href="https://www.facebook.com/kalistorik" class="social-icon" aria-label="Facebook" target="_blank" rel="noopener">
```

### 5. `kalis/dist/social-wa.html` line 557（联系人卡片区 FB）
```diff
- <a href="https://facebook.com/" aria-label="Facebook" target="_blank" rel="noopener">
+ <a href="https://www.facebook.com/kalistorik" aria-label="Facebook" target="_blank" rel="noopener">
```

### 6. `kalis/dist/social-wa.html` line 574（footer FB）
```diff
- <li><a href="https://facebook.com/" target="_blank" rel="noopener" data-i18n="foot_fb">Facebook</a></li>
+ <li><a href="https://www.facebook.com/kalistorik" target="_blank" rel="noopener" data-i18n="foot_fb">Facebook</a></li>
```

### 7. wrangler 部署
```bash
cd /Users/zuo/.openclaw/workspace/kalis && wrangler pages deploy dist/ --project-name=kalistorik --branch=main
```

---

## ⚠️ 保留事项（不删，等老板决策）

- **`social-fb.html` 中间页保留**（不删）
- 6 语 hreflang / canonical / OG 全部保留
- 中间页 footer 里的 `href="https://kalistorik.com/social-fb.html"` 自指也保留
- 老板说"中间页完全没有意义"是 v2 反馈，但**没明说删除** — 撒旦建议保留作"内容营销兜底页"（FB 直链被外站拦了还能落回站内），如要删老板会再说

---

## ✅ 自验

- `curl -s https://kalistorik.com/ | grep -A 1 "nav-social-fb"` → `href="https://www.facebook.com/kalistorik"` ✅
- `curl -sIL https://kalistorik.com/social-fb.html` → 200（中间页仍可访问）✅
- 主页线上点 nav FB icon → 跳 `https://www.facebook.com/kalistorik` ✅

---

## 📤 撒旦最终验收

撒旦会跑：
- 主页 HTML 拉下来 grep 6 处替换是否都生效
- Playwright 点 nav FB icon → 看落地 URL
- 截图给老板看（mobile + desktop）

---

## ⏱️ 时间窗口

15 分钟内。超时在 feedback/ 写 OVERTIME 原因。

---

## 📎 引用

- 6/5 v14.5 拍板设计："4 社媒对接，FB 直链 `facebook.com/kalistorik`"（见 `memory/2026-06-05.md` 21:30 段）
- 6/5 主页 nav 4 社媒全部直链（IG `1980zuo` / WA `+8613602222361` / FB 应为 `facebook.com/kalistorik`）
- 6/10 v2 部署你改了 `index.html:623` 把 FB 改回 `/social-fb` — **这是设计退步**
- 6/11 17:27 老板反馈：FB 应直链到 Facebook 账号（账号 = Page）

撒旦已改完 workspace 源，dist 等你同步。
