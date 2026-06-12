# Task Report — 2026-06-11 FB 入口修复

## 任务
修复独立站 Facebook 入口：social 子页占位 → 完整页、主页 nav 启用、部署到生产

## 执行者
天使长 Michael (Codex)

## 变更文件
- `kalis/dist/social-fb.html` (覆盖：85B → 70KB)
- `kalis/dist/social-ig.html` (覆盖：85B → 60KB)
- `kalis/dist/social-wa.html` (覆盖：85B → 86KB)
- `kalis/dist/index.html` (L623 FB nav：启用，删 `onclick="return false"` + `Coming Soon` + `nav-social-disabled`，改 `href="#"` → `href="/social-fb"`)
- `kalis/dist/_redirects` (删除 social-*.html → /404 规则，新增旧地址 301：`/facebook.html → /social-fb` 等 3 条)

## 方案
1. 用完整源文件覆盖 3 个 social-*.html 占位（85 字节 → 完整多语言页）
2. 修复 index.html L623 FB nav icon，启用链接到 `/social-fb`（CF Pages clean URL）
3. 重写 `_redirects`：旧地址 `/facebook.html`、`/instagram.html`、`/whatsapp.html` 301 → 新地址
4. 部署到 CF Pages **main 分支**（Production），之前误部署到 master/Preview

## 踩坑
- **wrangler 分支问题**：默认部署到 `master` 分支（Preview），而生产域名 `kalistorik.com` 绑定 `main` 分支（Production）。需显式 `--branch=main`
- **clean URL**：CF Pages 默认去 `.html` 后缀，nav 链接需用 `/social-fb` 而非 `/social-fb.html`

## 验证结果（9/9 通过）
| # | 端点 | 预期 | 结果 |
|---|------|------|------|
| 1 | `/social-fb` | 200 | ✅ |
| 2 | `/social-ig` | 200 | ✅ |
| 3 | `/social-wa` | 200 | ✅ |
| 4 | `/social-fb?lang=fr` | 200 | ✅ |
| 5 | `/facebook.html` | 301 → `/social-fb` | ✅ |
| 6 | `/instagram.html` | 301 → `/social-ig` | ✅ |
| 7 | `/whatsapp.html` | 301 → `/social-wa` | ✅ |
| 8 | `/` (主页) | 200 | ✅ |
| 9 | 主页 FB nav `href="/social-fb"` | 存在 | ✅ |

## 审核结论
- **逻辑正确性** ✅：边界条件覆盖，空值无影响
- **架构合规** ✅：符合项目 CF Pages 部署规范
- **安全性** ✅：无敏感信息变更
- **需求覆盖** ✅：4 项修复全部完成
- **代码风格** ✅：与现有代码一致

**撒旦可继续验收**：hreflang 7×3=21、多语言 7URL×3=21、旧地址 301×3、主页 FB 入口 ≥1、MD5 三验。
