# 独立站 canonical 修复备份 · 2026-09-28

## 结论
- 问题：GSC 将 `/quality`、`/factories`、`/freight`、`/picks` 的英文版判定为 duplicate canonical。
- 根因：这 4 个页面的 `rel=canonical` 和 `hreflang="en"` 自引用写成了 `?lang=en`，Google 另选 clean URL 为 canonical。
- 修复：去掉英文版 canonical/hreflang en 的 `?lang=en`；非 en 语言参数保持不变。
- GA4：实测正常，过去 7 天 0 是自然无访问，不是追踪断线。

## 修改文件
- quality.html
- factories.html
- freight.html
- picks.html

## Git 记录
- 主仓：/Users/zuo/kalistorik-site
- commit：d5bf2af fix: clean canonical for en subpages
- 部署：GitHub Actions `Deploy to CF Pages` 成功
- 线上验证：4 个页面 canonical/hreflang en 已变为 clean URL
- GSC：已对 duplicate canonical 发起 VALIDATE FIX

## 备份内容
- after/：修复后的 4 个 HTML 文件
- before/：修复前的 4 个 HTML 文件（来自 05aa58d）
- patch/0001-fix-clean-canonical-for-en-subpages.patch：Git format-patch 完整提交补丁
- patch/diff.txt：4 文件纯 diff

## 未改动
- /wa、/wa.html 的 noindex 保留，属于 WhatsApp 跳转页。
- 语言路由 redirect / alternate canonical 属正常现象，未改。
