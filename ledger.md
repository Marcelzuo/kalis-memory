# Ledger

## 2026-06-27 — 路西法审查 (5 项) 报告

**结论：🟡 通过，3 项必修**

### 1. 痛点覆盖（A-F）✓ 完整无重复
- 6 类痛点 A/B/C/D/E/F 在 EN 文案全部命中（每类 9-17 条）
- 6 USP 全部对应：1/3/6 月回访 / MOQ 灵活 / QC 双留证 / 到岸全包价 / EU 法规预警 / DM 5 分钟
- Testimonials 用 Carlos García / Lena Hofmann / João Silva（符合痛点文档 §五指定）
- 无业务文案重复（仅 nav_how=how_title 等 nav/section 标签语义重合，可保留）

### 2. fr/de/es 翻译质量 ✓ 良好
- 用词口语化、无生僻词（sourcer/sourcen 是行业法语/德语常见用法，正确）
- 数字/地名（Porto, Berlin, Madrid, Rotterdam, 100+, 40%）保留
- **⚠ 但发现 1 个真错**：`pain_1_label` 三语都错——MOQ 的行业缩写应该是 MOQ/МОQ（全世界通用），现译成 QMC(法) / MBM(德) / PMO(西)，**应是 MOQ**（或意 MOQ/西 MOQ/法 MOQ/德 MOQ），3 处错误必改

### 3. data-i18n 完整性 ✓
- index.html: 46 处 data-i18n（HTML）+ 91 处脚本内部键（hero_slogan_1/2/3 经 JS 注入、pain 段由 JS 生成）
- picks.html: 12 处 data-i18n + 3 处 data-nav 全对齐
- **⚠ 5 语种各缺 6 键**：`cta_text` / `proof_text` / `stat_factories` / `stat_years` / `stat_clients` / `stat_rates`（EN 有，其他 5 语种均无，会 fallback 英文，严重度中）

### 4. MODAL_CONTENT 多语切换
- ✓ **picks.html**：内联 modal JS 用 `t.hook1_body/cta`、`t.picks_first_order_title`、`t.hook3_title/body`、`t.picks_what_next`、`t.picks_what_looks_like`，6 语种全支持
- ⚠ **index.html 内联 modal JS**：hook1.title、hook2.title/cta、hook3.cta **写死英文**，未走 `__LANGS__` 翻译键 → 切语言后 modal 仍显示英文
- /assets/picks-modal.js 外链版本也是写死英文（但 index.html 没引用它，picks.html 也没引用 → 死代码）

### 5. picks.html lang-switcher ✓ 工作
- `#lang-btn` 触发下拉、`#lang-dropdown` 6 按钮 → setLang()
- setLang 同时刷新 `data-i18n`/`data-nav`、更新按钮 active 态、改 `document.documentElement.lang`、写 `localStorage('kalis-lang')`
- 初始化读 localStorage，无值保持 EN

### 必修清单
| # | 文件 | 行/键 | 问题 | 修复 |
|---|------|------|------|------|
| 1 | index.html `__LANGS__` | `pain_1_label` fr/de/es | QMC/MBM/PMO 全错 | 全部改 MOQ |
| 2 | index.html `__LANGS__` | cta_text / proof_text / stat_factories/years/clients/rates fr/de/it/es/pt | 5 语种缺 6 键 | 补全 30 处翻译 |
| 3 | index.html 内联 modal JS (script #8, ~L284278) | hook1.title / hook2.title / hook2.cta / hook3.cta | 写死英文不切语言 | 改成 `t.story1_hook1` / `t.picks_first_order_title` / `t.picks_what_looks_like` / `t.picks_what_next`，对齐 picks.html |
| 4 | /assets/picks-modal.js | MODAL_CONTENT 段 | 写死英文 + 死代码（无页面引用） | 删除整个文件或对齐 index 内联版本 |

---

## 2026-06-27 — picks.html 故事文案替换 + index.html how_step3_desc fallback 修复

**picks.html** (7 处):

| # | 行 | 区块 | 变更 |
|---|-----|------|------|
| 1 | 572 | hook3__sub | "A buyer in Porto reached out. Not after the first order — after the third. When cutting corners started, the pattern was clear." |
| 2 | 586 | hook1__title | "More factories refused than most agents ever visit." |
| 3 | 587 | hook1__sub | "KALIS TORIK works for studios, retailers, and brands who choose quality over volume. Most of the week: walking away from the wrong ones." |
| 4 | 591 | hook1__counter span | "Factories in the network · new partners added every year" |
| 5 | 593 | hook1__ps | "PS. One factory offered 40% commission. The call was never returned." |
| 6 | 612 | hook2__sub | "30-piece trials for Berlin studios. 200-bed runs for Madrid retailers. Every size has a path. Start where you are. The rest gets figured out, step by step." |
| 7 | ~855 | MODAL_CONTENT hook1 title | "More factories refused than most agents ever visit." (与 hook1__title 同步) |

**index.html** (1 处):

| # | 行 | 区块 | 变更 |
|---|-----|------|------|
| 1 | 563 | how_step3_desc fallback | "Photos and video of your order. You approve before the balance is due." (与 __LANGS__.en.how_step3_desc 一致) |

## 2026-06-27 — en 语言键值检查

| Key | Value |
|-----|-------|
| hero_slogan_3 | 100+ factories. Every one tested with real orders. |
| why_text | The hard part is not finding a factory. It is finding one that stays honest. |
| how_step2_title | Factory Match & Quote |

来源：`index.html:881` `__LANGS__.en` 对象。

## 2026-06-27 — picks.html 六语 i18n 支持

**文件**: `picks.html`
**译文来源**: `/tmp/translations.json`（20 键，6 语种）

### 新增内容

| 区块 | 说明 |
|------|------|
| CSS (L100–L106) | `.lang-switch` / `.lang-btn` / `.lang-dropdown` 样式，适配 brandbar 的 `mix-blend-mode` |
| `<script>` (L553–L715) | `__LANGS__` 对象（en/fr/de/it/es/pt，每语种 20 键）+ `setLang()` 函数 |
| Nav (L727–L737) | 语言下拉切换器（`.lang-switch` > `#lang-btn` + `#lang-dropdown`） |
| IIFE 末尾 (L1128–L1150) | Lang 事件绑定 + `localStorage('kalis-lang')` 初始化 |

### data-i18n 属性（12 处）

| 元素 | 键 | 位置 |
|------|-----|------|
| `.hook3__title span:nth-child(1)` | `picks_first_two` | L753 |
| `.hook3__title span:nth-child(3)` | `picks_third_didnt` | L753 |
| `.hook3__sub` | `story1_intro` | L754 |
| `.hook3__cta` | `picks_what_next` | L755 |
| `.hook1__title` | `story1_hook1` | L768 |
| `.hook1__sub` | `story1_body` | L769 |
| `.hook1__counter span` | `story1_stats` | L773 |
| `.hook1__ps` | `story1_ps` | L775 |
| `.hook2__note` | `picks_note_buyers` | L792 |
| `.hook2__title` | `picks_first_order_title` | L793 |
| `.hook2__sub` | `story2_body` | L794 |
| `.hook2__cta` | `picks_what_looks_like` | L795 |

### data-nav 属性（3 处）

| 元素 | 键 |
|------|-----|
| Nav "how it works" | `nav_how` |
| Nav "factories" | `nav_factories` |
| Nav "contact" | `nav_contact` |

### Modal JS 更新

`openModal()` 改为读取 `__curLang__`，hook1/hook2/hook3 的 modal title/body/cta 全部走翻译键：
- hook1: `story1_hook1` / `hook1_body` / `hook1_cta`
- hook2: `picks_first_order_title` / `hook2_body` / `picks_what_looks_like`
- hook3: `hook3_title` / `hook3_body` / `picks_what_next`

### 未改动

- CSS 布局 / 结构 / 动画
- `.hook3__eyebrow` 保留原文（含专有名词 "Porto, 2019"）
- `.hook1__counter strong` 数字计数逻辑
- WhatsApp/Email 链接文案（非翻译目标）

## 2026-06-27 — index.html L510 pick-card__title 文案修正

`index.html:510`
**Before:** `Twenty years on the ground. One person, start to finish.`
**After:** `More than 20 years on the ground. Full service, start to finish.`

## 2026-06-27 · 玛门 · 路西法审出 4 问题修复

### 变更文件
- `index.html` — __LANGS__ 补键 + pain_1_label 修正 + modal JS 去硬编码
- `assets/picks-modal.js` — **删除**（死代码，无页面引用）

### 明细

| # | 问题 | 修复 |
|---|------|------|
| 1 | pain_1_label fr=QMC/de=MBM/es=PMO/it=QMO/pt=QME | 全部改为工业标准 MOQ |
| 2 | __LANGS__ fr/de/it/es/pt 缺 cta_text/proof_text/stat_factories/stat_years/stat_clients/stat_rates | proof_text 从 /tmp/translations.json 补入；其余 5 键自行翻译补入 |
| 3 | hook1_title/hook2_title/hook2_cta/hook3_cta 缺所有语言（含 en） | en 从原代码英文默认值提取；5 语种自行翻译；modal JS 改为 `t.KEY \|\| "fallback"` |
| 4 | index.html modal JS hook1.title/hook2.title/hook2.cta/hook3.cta 死英文 | 改为从 `t.hook1_title` / `t.hook2_title` / `t.hook2_cta` / `t.hook3_cta` 读取，保留英文 fallback |
| 5 | picks-modal.js 死代码 | 删除 91 行 |

### 每语种新增 10 键
cta_text, proof_text, stat_factories, stat_years, stat_clients, stat_rates, hook1_title, hook2_title, hook2_cta, hook3_cta

---

## 2026-06-27 — 路西法 V5 终审报告

**范围**: /Users/zuo/kalistorik-site/ 全部 7 个 HTML + sitemap.xml  
**结论**: 🟡 整体通过, **3 项必修 + 13 项低优/可接受**

### 必修清单

| # | 文件 | 位置 | 问题 | 修复 |
|---|------|------|------|------|
| 1 | index.html | L545-548 (why-split__stats) | 引用 4 键 (`stat_factories_label` / `stat_years_label` / `stat_clients_label` / `stat_rates_label`) 在 `__LANGS__` 140 键中全部未定义 → 切非 EN 时 4 个 span 显示空 | __LANGS__ 6 语种各增 4 键 |
| 2 | picks.html | L1-46 head | 完全无 hreflang (6 语种 + x-default 缺失) + 无 og:locale:alternate | 增 7 条 link rel=alternate hreflang |
| 3 | picks.html | setLang() L689-714 | 不更新 document.title / meta description / og / twitter → tab 永远英文 | 末尾追加 4 行 setAttribute |

### 低优/可接受 (摘要)

- index.html __LANGS__ 6×140 键 / picks.html 6×20 键 ✓
- 7 HTML 文件标签完整 / alt 全有 / 内部链接有效
- "死键" 87+5 个实为 JS 注入 (hero_slogan/pain/modal) 和 modal feedback, 非真死
- L905-917 IIFE 残缺 (closeBtn/overlay/close 未声明) 但 `if(!box) return` 早退保护, 不报错
- factories/freight/quality/privacy 无多语 (设计接受)
- 法语/德语 narrative 无本地引号 (因无引语不可见)
- sitemap.xml 引用 3 个不存在的 insight-* + 漏 picks.html
- picks.html init 未读 localStorage (与 index 一致, 保持 EN)

### 跨维度小结

| 维度 | 状态 |
|------|------|
| __LANGS__ 6 语种键数一致性 | ✓ index 140×6 / picks 20×6 |
| data-i18n 拼写 | ✓ (picks 多 5 modal 死键但实际用) |
| HTML 标签闭合 | ✓ 7 文件 |
| 图片引用 + alt | ✓ |
| href 内部链接 | ✓ |
| hreflang | ⚠ index ✓ / picks 缺 |
| meta description i18n | ⚠ index 缺翻译键 / picks 不更新 |
| 标点统一 | ✓ em-dash/句号/问号, 百分号德语正字 |
| favicon 链 | ✓ 4 文件 (ico+svg+16/32/180) |

**总评**: 3 必修可一次合并修 (增 picks hreflang + 4 个 stat_*_label 键 + picks meta update), 其他项当前不影响发布。

---

## 2026-06-27 · 玛门 · V5 终审 3 必修修复

### 变更文件

| 文件 | 变更行数 | 说明 |
|------|---------|------|
| `index.html` | 1 行 (L865 内联 JSON) | `__LANGS__` 6 语种各增 4 键 |
| `picks.html` | +21 行 | hreflang ×7 + og:locale ×6 + `__LANGS__` 2 键 ×6 + setLang title/meta 逻辑 |

### 明细

**Fix 1 — index.html 补 `stat_*_label` 4 键**

`__LANGS__` 每语种增 4 键，插在 `stat_rates` 之后：

| Key | en | fr | de | it | es | pt |
|-----|----|----|----|----|----|----|
| `stat_factories_label` | Factories | Usines | Fabriken | Fabbriche | Fábricas | Fábricas |
| `stat_years_label` | Years | Ans | Jahre | Anni | Años | Anos |
| `stat_clients_label` | EU Clients | Clients UE | EU-Kunden | Clienti UE | Clientes UE | Clientes UE |
| `stat_rates_label` | Rates | Tarifs | Preise | Tariffe | Tarifas | Tarifas |

**Fix 2 — picks.html 增 hreflang + og:locale**

- 7 条 `<link rel="alternate" hreflang="...">`（en/fr/de/it/es/pt + x-default），指向 `picks.html?lang=XX`
- 6 条 `<meta property="og:locale">`（en_US + 5 条 alternate）
- 参照 index.html 格式，插在 canonical 后、og:image 后

**Fix 3 — picks.html setLang() 更新 title + meta description**

- `__LANGS__` 每语种增 `picks_title` / `picks_desc` 2 键
- setLang 末尾追加：`document.title = t.picks_title || __LANGS__.en.picks_title` + `meta[name="description"]` setAttribute
