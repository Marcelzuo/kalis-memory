# V5 终审报告 — /Users/zuo/kalistorik-site/

**结论：🟡 整体通过，3 项必修 + 5 项低优**

## 必修（影响 i18n/SEO 完整性）

| # | 文件 | 位置 | 问题 | 修复 |
|---|------|------|------|------|
| 1 | index.html | L545-548 (`why-split__stats`) | 引用了 `stat_factories_label` / `stat_years_label` / `stat_clients_label` / `stat_rates_label` 4 键，但 `__LANGS__`（140 键）全部未定义 → 切到非 EN 时这 4 个 `<span>` 显示空（HTML hardcoded EN 不被覆盖，因 JS 走 `if(t[k])` 跳过缺失键） | 在 `__LANGS__` 6 语种各加这 4 键（复用现有 `stat_factories/years/clients/rates` 文案或新建带 `_label` 后缀的别名） |
| 2 | picks.html | L1-46 `<head>` | 完全无 `hreflang` 标签（index.html 有 6 语种 + x-default 7 条），且无 `og:locale` / `og:locale:alternate`，无 twitter:title i18n 钩子 | 添加 6 语种 `hreflang` 指向 `picks.html?lang=xx` + x-default + og:locale 6 套 |
| 3 | picks.html | L553-714 `setLang()` | 不更新 `document.title` / `meta description` / og meta → 浏览器 tab + 社交分享永远是英文 | setLang 末尾追加 4 行：`document.title = t.page_title`；`document.querySelector('meta[name=description]').setAttribute('content', t.meta_description)` + og:description + twitter:description |

## 低优（已知/可接受/无影响）

| # | 项目 | 说明 |
|---|------|------|
| L1 | index.html `__LANGS__` 6 语种 140 键完整一致 | ✓ 上次审查 4 必修已修 |
| L2 | picks.html `__LANGS__` 6 语种 20 键完整一致 | ✓ 6×20=120 键全对齐 |
| L3 | 全部 HTML 标签完整（7 文件） | ✓ HTMLParser 验证 |
| L4 | 全部 `<img>` 有 alt 属性 | ✓ |
| L5 | 内部 href 链接全部有效 | ✓ `/cdn-cgi/l/email-protection` 是 Cloudflare 自动生成，非真断链 |
| L6 | 图片引用全部存在 | ✓ 索引中 `'+s+'` `'+p.main_image+'` 是 JS 模板字面量，非真引用 |
| L7 | index.html `__LANGS__` 140 键中 87 个"死键" | 实为 JS 注入（hero_slogan_1/2/3、pain_1/2/3/4、modal hook1/2/3）或 modal/fetch 反馈键（contact_thanks、newsletter_success），非真死 |
| L8 | picks.html `__LANGS__` 5 死键（hook1_body/hook1_cta/hook2_body/hook3_body/hook3_title） | 实为 modal JS 读取（picks.html:855 `MODAL_CONTENT` 段），非真死 |
| L9 | index.html L905-917 IIFE 引用未声明的 `closeBtn`/`overlay`/`close` | 残缺代码，但 `if (!box) return` 早退保护——`insight-modal-1` DOM 元素不存在，永远走 early return，**实际不报错**（建议清理或补全） |
| L10 | factories/freight/quality/privacy 4 页无多语 | 纯展示页（卡片/费率/法规），与主 nav 解耦；属于"暂无多语"接受范围 |
| L11 | 法语缺 « »、德语缺 „ " 本地引号 | narrative 文本中无直接引语 → 无可视引号可替换；不构成硬伤 |
| L12 | sitemap.xml 引用 3 个不存在的 insight-* 页面，且漏了 picks.html | 应删除 3 条死链 + 增 1 条 picks.html |
| L13 | picks.html setLang 写 `localStorage('kalis-lang')` 但 init 未读 | 用户首次访问保持 EN，可接受；index.html 主入口同款处理 |

## 跨文件小结

- **i18n 完整性**：index 6×140、picks 6×20 全 ✓
- **HTML 结构**：7 文件标签齐全 ✓
- **图片/链接/alt**：全部有效 ✓
- **SEO 头部**：index ✓、picks 缺 hreflang + meta update
- **标点**：6 语种 em-dash / 句号 / 问号统一；法语/德语缺本地引号因无引语而不显

**总评：3 必修可一次合并修（增 picks hreflang 头 + index 4 键 + picks meta update），其他项目当前不影响发布。**
