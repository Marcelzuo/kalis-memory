# Task Report — 2026-06-11 FB 入口改直链

## 任务
所有 FB 入口直链 `https://www.facebook.com/kalistorik`，不经过站内中间页，一劳永逸

## 执行者
天使长 Michael (Codex)

## 变更文件
- `kalis/dist/index.html` L623 — nav FB icon：`/social-fb` → `https://www.facebook.com/kalistorik`
- `kalis/dist/social-ig.html` L299/325/531 — 3 处 FB 链接直链化
- `kalis/dist/social-wa.html` L330/557/574 — 3 处 FB 占位（`facebook.com/`）→ `facebook.com/kalistorik`
- `kalis/dist/_redirects` — `/social-fb` `/social-fb.html` `/facebook.html` 全 301 → Facebook

## 方案
- **直链**：所有站内 FB 链接直接指向 `https://www.facebook.com/kalistorik`
- **兜底**：`_redirects` 捕获所有旧路径（`/social-fb` `/social-fb.html` `/facebook.html`）301 到 Facebook
- **中间页**：`social-fb.html` 文件保留但不再被访问（`_redirects` 拦截）

## 验证结果（7/7 通过）
| # | 端点 | 预期 | 结果 |
|---|------|------|------|
| 1 | 主页 nav FB icon | `facebook.com/kalistorik` | ✅ |
| 2 | `/social-fb` | 301 → Facebook | ✅ |
| 3 | `/social-fb.html` | 301 → Facebook | ✅ |
| 4 | `/facebook.html` | 301 → Facebook | ✅ |
| 5 | social-ig 页面 | 3 处 FB 直链 | ✅ |
| 6 | social-wa 页面 | 3 处 FB 直链 | ✅ |
| 7 | Facebook 主页 | 200 | ✅ |

## 审核结论
- **逻辑正确性** ✅：所有旧路径有兜底，不死链
- **架构合规** ✅：CF Pages _redirects 标准做法
- **安全性** ✅：外部链接带 `target="_blank" rel="noopener"`
- **需求覆盖** ✅：一劳永逸，无中间页
- **代码风格** ✅：与现有代码一致

## 撒旦验收
Playwright 点 nav FB → 截图验证落地 `facebook.com/kalistorik`
