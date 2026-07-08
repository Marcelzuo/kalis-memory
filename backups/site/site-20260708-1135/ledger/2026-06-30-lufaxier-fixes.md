# 路西法审查补修 · 2026-06-30

## 修复清单

### 1. 删除真死代码 — index.html
- **变更**: 删除 `__imgCache__` + `__loadImg__` 函数体（L857–L868，12 行）
- **原因**: 0 个调用点，代码从未被使用
- **验证**: `grep -c '__loadImg__\|__imgCache__'` → 0

### 2. 清理 stat_*_label 重复 — index.html
- **变更**: 从 `__LANGS__` 每个语种删除 4 个死键 `stat_factories`/`stat_years`/`stat_clients`/`stat_rates`
- **原因**: 这 4 键无 `data-i18n` 引用，仅在 `__LANGS__` 中定义却从未被消费；真正使用的是 `stat_*_label` 变体
- **数量**: 6 语种 × 4 键 = 24 个死键移除
- **验证**: Python 脚本逐语种确认 clean

### 3. picks.html hreflang 语义修正 — picks.html
- **变更**: 7 个 `<link rel="alternate" hreflang="...">` 的 href 从 `/xx.html` 改为 `/picks.html`
- **原因**: 旧值全指向首页各语种版本，不符合 self-referential 规范；子目录无 picks.html，统一指向当前页 URL

### 4. 补 twitter:card — factories.html / freight.html / quality.html
- **变更**: 三页各补 `<meta name="twitter:card" content="summary_large_image" />`
- **原因**: picks.html 和 index.html 已有，三子页遗漏

### 5. i18n XSS 防护 — index.html
- **变更**: `el.innerHTML=t[k]` → `el.innerHTML=__esc__(t[k])`（L876）
- **原因**: 翻译文本未经 HTML 转义直接注入 innerHTML，存在 XSS 风险

## 受影响的文件
- `index.html` — 修复 1/2/5（删 12 行死代码 + 移除 24 死键 + 1 行 __esc__ 包裹）
- `picks.html` — 修复 3（7 行 href 修正）
- `factories.html` — 修复 4（+1 行 meta）
- `freight.html` — 修复 4（+1 行 meta）
- `quality.html` — 修复 4（+1 行 meta）
