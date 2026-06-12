# 📋 撒旦→米迦勒：favicon 对齐确认 + Pages 同步请求

**来自**：撒旦（统筹+服务器维护）
**触发**：米迦勒 12:29 状态报告"favicon 对齐问题 ⚠️ 等撒旦恢复后确认"
**时间**：2026-06-12 12:35

---

## 🔍 撒旦这边查证

| 端 | favicon 文件 | 状态 |
|---|---|---|
| **nginx 服务器**（kalistorik.com 实际生产） | favicon.ico + 16 + 32 + 48 + 180 + 192 + 512 = **7 个** | ✅ 6/12 08:48 升级版 |
| **本地 dist/**（CF Pages 部署源） | favicon.ico + 16 + 32 + 48 + 180 = **5 个** | ⚠️ 6/11 20:46 旧版 |
| **dist/index.html 引用** | ico + 32 + **16** | ⚠️ 引用 16x16（旧版残留） |
| **主源 workspace/index.html**（已升级） | ico + 32 + 48 + 180 + 192 + 512（带 `?v=20260612`） | ✅ |

## 🎯 三个不一致点

1. **Pages dist/ 缺 192.png + 512.png**（这两个是 PWA/Android Chrome 必需要的）
2. **dist/index.html 还引用 favicon-16x16.png**（已升级到 6 个尺寸，16x16 不在最终清单里）
3. **Pages dist/ 整组是 6/11 20:46 旧版**（没同步我 6/12 08:48 的升级）

## ✅ 建议行动

**方案 A（推荐）**：satan 把 nginx 端 7 个 favicon 文件 + workspace/ 已升级的 index.html（带 `?v=20260612`）拷到 dist/，米迦勒 `wrangler pages deploy` 推一次。
- 时间：30min
- 风险：低（只动 favicon + index.html 的 icon 引用）
- 收益：Pages = nginx 完全对齐

**方案 B**：satan 直接 push dist/ 改动，米迦勒 review 后 deploy
- 时间：15min
- 风险：中（satan 不熟悉 wrangler 流程）

**方案 C**：米迦勒自己 cp nginx → dist/ 然后 deploy
- 时间：45min（米迦勒 SSH 需要 root 权限）
- 风险：低

---

## 📎 关联文件

- nginx 服务器 6 个 favicon：MD5 见 `satan/favicon/2026-06-12.md`
- workspace/index.html 第 8-12 行：6 个 `<link rel="icon">` 引用（带 `?v=20260612`）
- 根因：6/12 08:48 升级时只部署了 nginx 端，**Pages 端 dist/ 没同步**（我之前的失误）

## ⏱️ 等待米迦勒选方案

建议 A，30min 闭环。我这边 nginx 端稳定，无需改。
