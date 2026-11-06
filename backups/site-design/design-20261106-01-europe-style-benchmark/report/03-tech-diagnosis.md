# KALIS TORIK 首页“太素”技术定位（只读静态分析，未改文件）

## 一、太素的技术原因（≤8 条）
1. 首屏纯黑无图：`en/index.html:524-540` hero 只有 Logo+三行轮换文案+一个 CTA；`.hero{background:var(--color-black)}`(:108) 纯色，`.hero::before` 金色径向渐变仅 `rgba(201,169,110,.06)`(:109) 肉眼不可见。benchmark 里 moooi/carl-hansen 首屏是图/视频，本站 `videos=[]`。
2. 全页仅 4 张实景图：pick 卡 `hook1/2/3.jpg`(:548/552/556) + `why-hero.jpg`(:586)。metrics `counts.images=23` 其余全是 `__PRODS__`(:948) JS 渲染的产品缩略图，不构成视觉丰富。
3. 全页只有两个底色交替：`.section` 白 / `.section-alt{background:var(--color-linen)}`(:123) 米白；Testimonials/How/FAQ/Regions/Contact/Newsletter 全是纯文字平铺，无材质、无景深。
4. 字号层级平：正文 Inter 300(:69)、标题 Montserrat 300(:70)，H1 实测仅 13.6px 灰字，所有 H2 都 36px，无视觉焦点。
5. 产品卡发空：`.product-card-img` 米色底 + `img{object-fit:contain;padding:1.25rem}`(:162-163)，每张产品浮在米色盒大留白，密度低。
6. 装饰全凭 1px 金线：`.how-step-num` 金圈(:148)、`.pick-card` 金边 `rgba(201,169,110,.18)`(:271)，丰富感只剩发丝描边。
7. 唯一动效是纯文字淡入淡出 `.hero-slogan-item`(:114)，无图/无视频 → 首屏“静”。
8. 金是唯一点缀色 `--color-gold:#C9A96E`(:53)，但 brand.md 规定金仅特种工艺不能加码 → 缺第二层材质补空。

## 二、可选改动分档
- **A 纯 CSS/局部 HTML（低风险）**：加粗 `.hero::before` 渐变+暗角；放大 `.section-title` 字号对比；正文引入深灰 `#2D2D2D`（brand.md 已列）替代 #888；压缩 `.section{padding:6rem}`(:122) 留白；产品卡改 `object-fit:cover` 减内边距；加 hover/滚动淡入微交互。
- **B 需新增图片资产**：首屏加一张工厂/材质特写背景图（无人物，守人物禁令）配暗蒙层+preload；Why/Testimonials 各加 1-2 张五金/皮料/布料纹理图（brand.md“可围绕”清单）。
- **C 重构（暂不建议）**：首屏轮播/视频、视差分区、杂志式网格重排、把 6 语言 string-replace 镜像换成组件系统。

## 三、最易被改版弄坏的点（≤4）
1. 多语言镜像：`generate.py` 从根 index.html 纯字符串替换(:9-13)且强制 `setLang('{lang}')`(:25)——新增 HTML/CSS 必须 6 语言同构，新增 `data-i18n` 键必须六语字典齐全，否则文案空白。
2. 图片路径：镜像页带 `<base href="/">`(:5)，新加 `background-image:url(...)` 须用 `/images/...` 绝对路径，否则 en/fr 下 404。
3. 首屏 LCP：现在首屏无图 LCP 快；若用内联 CSS 背景图而非 `<img>` 无法 preload，LCP 回退，须加 `<link rel=preload as=image>` 或 `<picture>`。
4. 移动端：`.hero{height:100vh;min-height:700px}`(:108) 加背景图须保暗蒙层（对比度≥4.5:1）；`.why-split` 768px 折叠单列(:143)；产品图 `loading=lazy` 无宽高(:1109) 有 CLS 隐患。

## 四、最小改动 3 步
1. 只动 CSS：强化首屏 `.hero::before` 渐变+暗角、放大 `.section-title`、压缩 section 留白（零资产）。
2. 产品网格提质：`object-fit:cover`+减 padding 让产品填满卡片；同时加一张首屏背景图（webp+preload），单点收益最大。
3. 中段补 1-2 张材质图到 Why/Testimonials，打破纯文字长页。

注：`assets/geo.css` 未被首页引用（grep 0 次）且变量不同（`--gold:#b08d57`），判断为旧/落地页样式，本次改版可忽略。
