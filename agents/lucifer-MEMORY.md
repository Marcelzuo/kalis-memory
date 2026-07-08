# MEMORY · 路西法 v6 (2026-07-07 瘦身)

> 触发词速查。业务规则 → `~/.codex/kb/`，此处只放个人/技术参考。

## 触发词 → KB 路由

| 触发词 | 去读 |
|:--|:--|
| 品牌/颜色/Logo/KALIS/TORIK | `~/.codex/kb/rules/brand.md` |
| 社媒/LinkedIn/FB/IG/发帖 | `~/.codex/kb/rules/social.md` + `business/content-plan.md` |
| 部署/Cloudflare | `~/.codex/kb/rules/deploy.md` |
| 分派/玛门/撒旦/团队 | `~/.codex/kb/rules/team.md` |
| git/commit | `~/.codex/kb/rules/git.md` |
| 审批/新增内容 | `~/.codex/kb/rules/content.md` |
| 客户/Client | `~/.codex/kb/business/clients-*.md` |

## 个人引用（不在 KB 范围）

| 触发词 | 说明 |
|:--|:--|
| 女儿/珞妤/错题/数学 | 左珞妤 SOP：4列错因+每题型3新题+DOCX落桌。全题面确认后一次性整合，严禁分批。位置 `~/.openclaw/workspace/coordination/zuoluo-math/` |
| OCR/手写公式 | 手写体识别率≈0，老板念题面。印刷体：tesseract/marker-pdf。venv `/tmp/marker_venv/` |
| AI 超分/放大 | Real-ESRGAN venv `/tmp/realesrgan-venv`，脚本 `/tmp/upscale_1.py`。快捷版：`ffmpeg -i in.webp -vf "scale=1200:-2:flags=lanczos" out.png` |
| LinkedIn 触达范本 | 骨架：Hi {名}, this is Kalis Torik. With over X years in {品类} trade, we have {资源} in China, offering {3服务} to resolve {痛点}. Happy to connect... |
| Vision API 401 | 本 profile 不可用，走本地 OCR |

## 工作偏好

- 给老板报告 ≤15 行 + 表格，禁 jargon
- 给兄弟用技术语言 + 编号 + 可执行
- 给方案必带推荐项，不说"两个都行"
- MEMORY 膨胀 >70% → 主动压缩
