# 独立站 V8 备份 · 2026-11-06 19:35 CST

## 结论

- 版本：V8 · 欧美 SEO + 站点修复 + 转化归因
- 站点主仓：`/Users/zuo/kalistorik-site`
- 分支：`master`
- 本地 commit：`f651a5d feat: 强化欧美 SEO 与站点修复`
- 部署状态：**未 push、未部署**；线上仍是 V7
- 备份方式：完整站点快照 + 数据报告 + 三方终检；只新增，不删除历史

## 本轮内容

- 新增欧洲落地页：`/en/furniture-sourcing-europe/`
- 新增美国落地页：`/en/furniture-sourcing-usa/`
- 新增 4 篇博客：验厂、MOQ、比利时首单、美国首单
- sitemap：18 → 25 URL
- 六语言首页补欧美双入口、FAQ 可见文本、欧美标题
- 修复六语言首页强制切英文、表单成功判断、GA 归因字段
- 补 hreflang、Organization `areaServed`（12 个欧盟国家 + 美国）
- 补 `llms.txt` / `llms-full.txt` / OKF 的欧美定位与博客索引
- 文案去 AI 化；路西法 7 条内容小修全部落实

## 验收

- Headless Chrome：120/120 PASS，0 FAIL
- sitemap：25/25 可映射，0 重复
- 页面：25/25 单 H1，canonical 自指，title/description 合规
- JSON-LD：全部可解析
- 三方：玛门技术终检 5/5 PASS；路西法内容审查完成并修复；米迦勒终审通过

## 线上待办

1. `git push origin master` 触发 Cloudflare Pages
2. GSC 重提 sitemap，欧美两页 + 4 篇新文 Request Indexing
3. IndexNow ping Bing / Yandex
4. 线上 25 URL 200、canonical、hreflang、FAQ schema 复核
5. 7 天 / 28 天看 GSC 与 GA4

## 文件说明

- 根目录：完整站点文件（排除 `.git`、`node_modules`、`.wrangler`、`.DS_Store`；`tools/.venv` 为本地虚拟环境，不纳入 Git）
- `reports/`：SEO 方案、最终检查、三方终检、120 项浏览器日志
- `data/`：GA4/GSC 对比、调研、CSV、社媒数据快照
- `manifest.json`：版本、commit、文件数、大小、验收摘要
- `SHA256SUMS`：报告与关键文件的 SHA-256
