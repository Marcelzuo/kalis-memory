# 玛门终检 · 只读复核（重跑）

目标：direction-a / direction-b · index.html + style.css
方法：静态解析（Python html.parser + 正则）+ Chrome headless CDP（360/390/768/1024/1440 实测）

| # | 检查项 | A | B |
|---|---|---|---|
| 1 | H1 数量/层级 | PASS（H1×1，层级 1→2→3 无跳级） | PASS（H1×1，层级 1→2→3 无跳级） |
| 2 | 图片加载/alt | PASS（7 图全部存在且 alt 非空；CSS 背景图均存在） | PASS（9 图全部存在且 alt 非空） |
| 3 | 链接与锚点 | PASS（#锚点全部命中；外链 target=_blank + rel=noopener） | PASS（同上） |
| 4 | Copy email 点击反馈 | PASS（type=button、data-copy、clipboard 写回 + fallback、role=status aria-live） | PASS（同上） |
| 5 | console/pageerror | PASS（无 JS 异常、无 console error） | PASS（无 JS 异常、无 console error） |
| 6 | 360/390/768/1024/1440 无横向溢出 | PASS（各宽度 docSW==innerWidth，A 产品轨为容器内 overflow-x:auto 不计） | PASS（各宽度 docSW==innerWidth） |
| 7 | Logo 冠线 #888 / KALIS·TORIK 比例 / 无金色 | PASS（冠线 #888888；TORIK=25% KALIS、KALIS ls 34%、TORIK ls 112%；无 #C9A96E/金线） | PASS（同上；why 区背景为 --sky #9dd9f3） |
| 8 | 重复 id / 标签闭合 / button type | PASS（id 唯一；标签闭合无错配无未闭；按钮均 type=button） | PASS（同上） |
| 9 | CTA 仅 mailto 或页内锚点 | PASS（所有 CTA 均为 mailto 或 #锚点） | PASS（同上） |

结论：9 项全 PASS，无 FAIL。
（附：B 编号已 KT→REF 无残留；A/B 文案、A/B 页头字号、B why 天空蓝均已到位。）

DONE
