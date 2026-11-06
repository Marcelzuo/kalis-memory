# KALIS TORIK 网站设计系统

版本：1.1  
状态：商业与视觉原则已确认；整页 A/B 方向稿被老板否决；只允许在线上现有结构上做局部装修，尚未上线  
更新：2026-11-06  
适用：`kalistorik.com` 六语言站点  
维护：米迦勒、玛门、路西法共用；老板拥有最终决定权

## 1. 一句话定位

**KALIS TORIK 是面向海外买家的中国家具采购服务商：客户可以带着自己的工厂来，也可以从找厂开始。**

网站不是家具商城，不是工厂官网，也不是品牌经销商页面。它先证明“我们会做事”，再展示“我们能供什么货”。

## 2. 商业前提

| 项目 | 规则 |
|---|---|
| 客户 | 海外中小买家、进口商、设计/工程采购方；需求常常不明确 |
| 服务 | 找厂、比价、打样协调、跟单、验货、拼柜、单证与异常处理 |
| 产品 | 床、沙发、桌、椅、沙发床等；只展示能力，不做完整 SKU 目录 |
| 成交 | 邮件多轮沟通，按客户需求发图册和方案 |
| 市场 | 所有市场都接；欧美是投放和 SEO 重点，但公开页面不写地域限制 |
| 内部参考 | 欧洲:美国约 7:3，不写进网站 |

## 3. 第一性原理

1. 每张图必须大气、精美、第一眼抓人；平庸图直接不用。
2. Hero 一句话读完；每个 section 只讲一件事。
3. 每个 section 必须回答一个买家问题，或推动下一步；回答不了就删。
4. 不做纯装饰图、空话、堆图标、堆卡片。
5. 先让客户记住“你能做什么”，再让他翻产品。
6. 页面要丰富，但丰富来自摄影、材质、色块和版式，不来自更多按钮。
7. 以线上现有结构为唯一底稿，只做局部装修；未经老板逐项确认，禁止整页重排或一次性重做。

## 4. 信息架构

### 首页顺序（长期目标，不是一次性重排指令）

> 当前 baseline 是线上站 `f651a5d` 的现有结构。以下顺序用于后续逐段优化，不得据此一次性重做首页。

1. **Hero**：亮色背景 + 强产品/材质图；主标语 + `Email your brief`。
2. **服务总览**：六项服务，同等权重，不排序。
3. **Start where you are**：已有工厂 / 有产品想法 / 多家供应商待协调，三个入口同等重要。
4. **What we source**：现有产品图做分区、拼贴或横向滚动，定期换顺序。
5. **How it moves**：从需求、找厂、打样、订单、验货、拼柜到单证的流程。
6. **Typical project scenarios**：三类典型场景，讲问题、处理方式、结果，不写真实客户。
7. **Why KALIS TORIK**：三条差异化，不写空泛自夸。
8. **Markets & email**：不写地域限制；显示邮箱、`Copy email`、`Open email app` 和“第一封邮件写什么”。
9. **Journal**：保留 SEO 文章入口，不占首屏主叙事。

### 保留页面

- `What We Do`：服务流程与工作方式。
- `Products`：品类能力展示，不做完整目录。
- `Journal`：现有博客，继续做搜索与 AI 可发现性。
- `Contact`：首页锚点或简短联系区，不新增复杂表单。

## 5. 服务与差异化

六项服务同等重要：Supplier search & comparison、Sampling coordination、Order follow-up、Quality inspection、Consolidation & shipping coordination、Documents & issue handling。

三类客户起点同等重要：`I already have a factory`、`I have a product idea`、`I have several suppliers to coordinate`。

只反复讲三条差异：

1. **You can keep your factory, or use ours.**
2. **One brief, many suppliers.**
3. **We work to your brief, not a fixed catalog.**

## 6. 文案规则

- 主标语：`Furniture sourcing, inspection and consolidation — one team, many factories.`
- 主 CTA：`Email your brief`；次 CTA 只能是弱化的 `See how we work`。
- 一句只做一件事；正文尽量不超过两行。
- 用买家听得懂的供应链词：sourcing、sampling、QC、inspection、consolidation、documents。
- 不写具体数字、MOQ、交期、价格、港口时效、服务国家数量或回复时限。
- 可用模糊但有底气的表达，如“more than two decades”。
- 不写“buyers in Europe and US”“only for Europe/US”等限制性句子。
- 去 AI 化：删 `elevate`、`seamless`、`curated`、`comprehensive`、`tailored solutions`、`in today's fast-paced world` 一类空话。
- 不伪造可核验的公司名、客户名、数字、认证或项目事实。

## 7. 视觉系统

### 方向

**Bright Product Editorial**：明亮、舒适、编辑式、产品导向。不是暗色奢华，不是黑白画廊，也不是五颜六色的促销页。

### 色彩

- 基础：暖白 `#FFF9F0`、墨黑 `#111111`、石色 `#D8D1C6`。
- 亮色章节每次只用 1–2 个：亮黄 `#FFD866`、天蓝 `#9DD9F3`、珊瑚 `#FF927D`、鼠尾草绿 `#B7D6A8`、淡紫 `#C9B8E8`。
- 产品图放亮色块上，文字用墨黑；金色 `#C9A96E` 退出 UI。

### 字体与版式

- 主字体 Montserrat，正文 Inter。
- H1/H2 建立清晰层级，不再全站同字号、全大写、全居中。
- 大标题、短标签、产品抠图、色块和大数字做杂志式组合。
- 每两个文字区至少出现一个视觉块：产品图、色块、流程图或授权场景图。
- 产品展示可自动轮播或横向滚动；每两周换顺序，支持手动切换和暂停。
- 动效只做慢速淡入、横向滑动和图片切换；不做滚动劫持。

### 图片

1. 现有产品图全部可用，通过裁切、组合、色块和重复排列做丰富度。
2. 背景图优先国内免费商用图库或有授权的现成摄影，要求电影画报级质量。
3. 不用海外客户容易认出的同款图库图；授权必须可查。
4. 禁止人物、手、脸、品牌标识、工厂名称和可识别工厂信息。
5. AI 只做抽象背景、纹理、色块；不生成假产品、假工厂、假项目现场。
6. 不用暗黄、深蓝、黑压压的“奢华感”；要亮、透、舒适。

### Logo 红线

- 冠线 `#888` 在 KALIS 上方：36×1px，间距 28px。
- KALIS：`#000`，Montserrat Light 300，字距为字号 34%。
- TORIK：`#888`，ExtraLight 200，字号为 KALIS 的 25%，字距为字号 112%。
- 禁止金线分隔、旧 SVG/PNG、KT 或 KALIS·TORIK 简写、阴影。
- favicon 不动。

## 8. 转化路径

- 全站主入口只保留一个邮箱：`hello@kalistorik.com`。
- 当前已有邮件卡、页尾表单、产品弹窗表单三套入口；下一步是收拢，不是增加第四套。
- 邮件按钮提供 `Copy email` 和带主题的 `Open email app`。
- 按钮下写清第一封邮件应包含：品类、数量、目的港、预计时间、当前阶段。
- 产品弹窗主按钮改为 `Email about this item`；表单只作为邮件客户端打不开时的备选。
- 首页 Hero、服务区之后、页尾各放一次 `Email your brief`。
- LinkedIn、Facebook、Instagram 统一指向 `https://kalistorik.com/en/#contact` 并带 UTM；文案同时写邮箱。
- 跟踪 `email_click`、`social_outbound`、`contact_scroll`，按平台拆分来源。

## 9. Google SEO 与 AI 可发现性

- 公开站点保持六语言：EN / FR / DE / IT / ES / PT。
- Google SEO 优先英语页面中的欧洲、美国采购意图；其他市场保留，不删除、不设限。
- 每页一个 H1；title、description、canonical、hreflang、OG、JSON-LD 完整。
- 继续维护 sitemap、`llms.txt`、`llms-full.txt`、OKF。
- 内容围绕真实服务问题：找厂、验货、拼柜、单证、首单、EUDR、MOQ 风险。
- 不写假地点、假案例、假统计、doorway page，不做关键词堆砌。
- AI 搜索优化以“可引用的事实、清楚的服务定义、问答结构、稳定链接”为主，不以堆文章为主。
- 新增或改写文案必须通过去 AI 化检查；六语内容同步更新。

## 10. 明确不做

- 材料页、Spec Sheet、Swatch Request、国际寄样、选品清单。
- 多步骤询盘、复杂表单、For Trade 独立页。
- 购物车、价格、在线下单、支付。
- 工厂实景、工厂名、客户名、可核验的假案例、假数字。
- 人物、手、脸；AI 生成的假产品/假工厂/假项目。
- 金色 UI、暗色奢华风、全站同字号、滚动劫持。

## 11. 三批实施（2026-11-06 修正）

1. **首页视觉重构**：亮色 Hero、服务前置、撤金、产品图色块/拼贴/滚动、服务总览、Start where you are、How it moves、邮件 CTA。
2. **服务内容与典型场景**：`What We Do`、三类 Typical project scenarios、产品分类展示逻辑、导航与六语同步。
3. **流量到邮件**：社媒 UTM、邮件主题模板、Copy email、What to include、统一 CTA、GA4 事件与按平台复盘。

执行方式已改为局部装修：每次只改一个点，验收后再进入下一个点；禁止把三批内容合成一次整页改版。

## 12. 验收清单

- 首屏 3 秒内看懂“做什么、为谁做、下一步做什么”。
- 六语言内容一致，无空白键、无英文串语。
- 所有 CTA 指向同一邮件路径，无第四套表单。
- 移动端不溢出，图片不变形，LCP 不明显回退。
- 一个 H1；canonical、hreflang、sitemap、JSON-LD 全部通过。
- Logo 冠线为 `#888`，UI 无金色。
- 无人物、手、脸、工厂名、客户名、可核验假数据。
- 图片授权可查，文件体积合理。
- 三方独立检查通过后才允许部署；部署前必须备份。

## 13. 变更流程

1. 先改 `DECISION-LOG.md`，写清日期、决策、影响。
2. 再改本文件；版本号按语义递增。
3. 先核对线上当前结构和 commit，以它为底稿。
4. 小任务分派，一项验收后再派下一项；卡住先停，检查通路后重派。
5. 每次只做一个局部改动，禁止整页替换、一次性大改和并行大任务。
6. 方案定稿后，在 `backups/site-design/` 冻结一轮证据，不改历史。
7. 上线前在 `backups/site/` 建整站快照，再部署。
