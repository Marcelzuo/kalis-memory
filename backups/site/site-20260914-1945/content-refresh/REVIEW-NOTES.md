# REVIEW NOTES — 2026-09-14 内容审查（路西法）

范围：仅今天修改的 content-refresh 文案源（4 篇 EN 源稿 + homepage.json + secondary.json + 4 篇博客）。未读/未改 first-post、旧 FAQ、旧 contact、旧 footer。未碰任何 .html/.css/.js，未 commit。

## 一、发现的 AI 味问题（原稿共性）

1. **破折号三连 + 排比工整**：hook3_body、why_body、freight_block3_text 全是"三个名词短语。长句——长句。"的机械节奏，六语言逐字镜像翻译，痕迹重。
2. **强行升华式收尾**：why_body 结尾 "one vetted floor at a time"、picks_closing "One answer that runs through all of them" 这类包装句，删掉信息量为零。
3. **过度对仗**：quality_closing "That order is not an accident — it is the whole point" 属于典型 AI 金句腔，改为直白说法。
4. **长句偏多**：西/葡/意语版照搬英文长句结构，未做本地化断句（已按短句优先重写）。
5. **hiw_closing "Ready when you are."** 空洞套话，删。
6. **产品红线**：post-mid-production-qc 原稿出现 timber/lumber/solid wood/kiln 内容 → 违反品牌红线（不做实木），已改为 fabric/leather/foam/hardware/frame material，删除 kiln drying 整条建议。

## 二、合规检查结果

- 价格/百分比/尺寸/工厂名/CIF：✅ 无（扫描命中的 "cif" 是 specifica/especificación 子串，误报）
- 人物脸/手/身体：✅ 无（文案不涉及）
- 文末强引导 DM：✅ 无（博客结尾保持内链 + 自然收束，无 "DM us" 类）
- 模糊数字口径：✅ 保留 "two decades"、"100+" 级表述，未新增具体数字
- 键名结构：✅ 未改任何 key，未新增 key，未新增品牌说法

## 三、改动摘要

### review-homepage.json（10 keys × 6 语言）
hook1_body / hook2_body / hook3_body / why_subtext / why_body / why_proof / hiw_step1_desc / hiw_step2_desc / hiw_closing / testimonial3_text
- why_body：删 "Factories do not fail loudly. They fail politely" 对仗开头与升华结尾，第三段缩为一句
- why_proof："Bad pieces do not leave the factory"（绝对化承诺）→ "Problems get caught at the factory, not at your warehouse"
- testimonial3_text：修 "First sourcing partner I never wanted to fly to China" 逻辑不通 → "First partner I never felt like flying to China to double-check"
- hiw_closing：删 "Ready when you are."

### review-secondary.json（9 keys × 6 语言）
picks_meta_desc / picks_hero_sub / picks_closing / factories_subtitle / factories_block2_text / factories_closing / quality_closing / freight_block3_text / freight_closing
- picks_hero_sub：原文把三个板块说明硬塞一句，拆成三个短句
- 各语版同步断句，西/葡语去英式长从句

### review-blog/（4 篇全部重写，EN）
- post-local-value.md：结构保留，长短句节奏重排，删排比堆叠
- post-mid-production-qc.md：**实木内容全部替换**（产品红线），其余节奏重排
- post-on-the-ground-partner.md："a stain match" → "a colour match"（避免木工暗示），节奏重排
- post-q4-shipping-window.md：删 "in late September" 时效锚点（文案会过时），节奏重排
- frontmatter（title/meta_description/slug）未动

## 四、给玛门回填的注意点

1. **回填目标**：review-*.json 里的 key 与线上 i18n JSON 的 key 一一对应，直接按 key 覆盖值即可；没列出的 key = 审查通过，不要动。
2. **why_body 段落数变了**（原 3 段 → 现 3 段但第三段只剩一句），如果模板按 `\n\n` 分段渲染没问题；若有按段数写死的样式需检查。
3. **博客 4 篇用 review-blog/ 下的版本整体替换** source/ 下同名文件（frontmatter 未改，slug 不变，不会动路由）。
4. testimonial3_text 六语言都改了，别只回填英文。
5. 我未 commit、未部署，回填后走正常 git 流程（commit 归你，英文 conventional commits）。
