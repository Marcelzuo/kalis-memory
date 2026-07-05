# KALIS TORIK · 网站与社媒状态审计 V2
**2026-07-04 · 米迦勒 · 多源信息收集总结归档**

---

## 一、独立网站 kalistorik.com

### 1.1 基础状态

| 项目 | 状态 |
|------|------|
| HTTP | ✅ 200 |
| 托管 | Cloudflare Pages (HKG edge) |
| 源码版本 | v6.2 (kalistorik-site-v6.2) |
| 部署频率 | 25 次 / 近 3 天 |
| 页面大小 | ~279KB |

### 1.2 SEO 评分

| 检查项 | 状态 | 详情 |
|--------|:--:|------|
| Title | ✅ | KALIS TORIK - Chinese Furniture Sourcing Partner |
| Meta Description | ✅ | 100+ vetted factories, Beds, sofas, tables... |
| OG / Twitter Card | ✅ | 完整（title/image/description/locale/site_name） |
| Canonical | ✅ | https://kalistorik.com/?lang=en |
| hreflang | ✅ | en/fr/de/it/es/pt + x-default(en) |
| Structured Data | ✅ | 3 个 JSON-LD 块 |
| robots.txt | ✅ | search=yes, ai-train=no, use=reference |
| Sitemap | ✅ | 12 URLs (6 语首页 + picks/factories/freight/quality/wa/privacy) |
| Indexability | ✅ | robots: index,follow |
| Missing pages | ⚠️ | /products 和 /about 在 HTML 中存在但未纳入 sitemap |

### 1.3 安全与性能

| 检查项 | 状态 | 详情 |
|--------|:--:|------|
| SSL/TLS | ✅ | TLS 1.3 / AES-256-GCM |
| SSL 有效期 | ✅ | 至 2026-09-21（79 天） |
| X-Content-Type-Options | ✅ | nosniff |
| Referrer-Policy | ✅ | strict-origin-when-cross-origin |
| HSTS | ❌ | **缺失** — 建议添加 |
| X-Frame-Options | ❌ | **缺失** — 防点击劫持 |
| Content-Security-Policy | ❌ | **缺失** — 防 XSS |
| PageSpeed | ⏳ | API 今日配额耗尽，待重试 |
| CF 内置分析 | ⏳ | 需进 CF Dashboard 查看 |

### 1.4 页面结构

| 元素 | 数量 | 备注 |
|------|:--:|------|
| section | 9 | 语义化良好 |
| article | 6 | |
| img | 3 | 可能偏少，产品页应有更多图片 |
| link (a) | 24 | |
| 结构化数据 | 3 | JSON-LD |

### 1.5 多语言

| 语言 | 首页 | sitemap |
|------|:--:|:--:|
| en (默认) | ✅ | ✅ |
| fr | ✅ | ✅ |
| de | ✅ | ✅ |
| it | ✅ | ✅ |
| es | ✅ | ✅ |
| pt | ✅ | ✅ |

---

## 二、可用分析渠道总览

### 已用渠道（本次审计）

| 渠道 | 工具 | 数据类型 | 本次状态 |
|------|------|------|:--:|
| HTTP 状态检查 | curl | 在线/响应码/headers | ✅ |
| SEO Meta 检查 | curl + grep | title/description/OG/hreflang | ✅ |
| robots.txt + sitemap | curl | 爬虫规则 + URL 列表 | ✅ |
| SSL/TLS | openssl | 证书/协议/加密套件 | ✅ |
| 安全 headers | curl | HSTS/CSP/X-Frame/CORS | ✅ |
| 部署历史 | wrangler CLI | 频率/版本/时间线 | ✅ |

### 待接入渠道

| 渠道 | 工具/入口 | 数据类型 | 接入难度 |
|------|------|------|:--:|
| **Google Analytics** | GA Dashboard / API | 流量/来源/跳出率/用户画像 | 🟡 需老板登录 |
| **Google Search Console** | GSC Dashboard | 搜索词/展示/点击/CTR/索引状态 | 🟡 需老板登录 |
| **Cloudflare Web Analytics** | CF Dashboard | PV/UV/带宽/国家分布（CF 免费内置）| 🟢 无需额外设置 |
| **PageSpeed Insights** | 公开 API | 性能/Core Web Vitals | 🟢 公开（今日配额耗尽） |
| **GTmetrix** | 公开 | 瀑布图/性能分级 | 🟢 公开 |
| **结构化数据验证** | schema.org validator | JSON-LD 正确性 | 🟢 公开 |
| **移动端可用性** | Google Mobile-Friendly Test | 触摸目标/字号/视口 | 🟢 公开 |
| **Ahrefs/Semrush** | 付费/免费版 | 外链/关键词/竞争分析 | 🔴 付费 |

### 社媒分析渠道（当前盲区）

| 渠道 | 入口 | 数据类型 | 接入难度 |
|------|------|------|:--:|
| **Instagram Insights** | IG App | 粉丝/触达/互动/画像 | 🟡 需专业账号 |
| **LinkedIn Analytics** | LI Dashboard | 帖文表现/访客/行业分布 | 🟡 需老板登录 |
| **Facebook Page Insights** | FB Dashboard | 粉丝/触达/互动/视频表现 | 🟡 需老板登录 |
| **Meta Business Suite** | 统一后台 | IG+FB 跨平台数据 | 🟡 需绑定 |

---

## 三、社媒三平台

| 平台 | 账号 | 自动采集 |
|------|------|:--:|
| IG | @kalistorik | ❌ 撒旦超时 / AI 搜索找不到新号 |
| LI | kalistorik 个人号 | ❌ 同上 |
| FB | Page kalistorik | ❌ 同上 |

> 三平台实时数据 = **当前盲区**。建议老板手动截三平台主页屏 → 我归档。

---

## 四、内容作战状态 (W1)

| 日期 | 应发 | 实发 | 缺口 |
|------|:--:|:--:|:--:|
| 周三 7/1 | LI #3 | ✅ | — |
| 周四 7/2 | IG Reels #1 + Story #2 | ❌ | 2 |
| 周五 7/3 | IG Carousel #4 + Reels #6 | ❌ | 2 |
| 周六 7/4（今天） | FB Page #7 + 群组 #8 + IG Story #9 | ⬜ | 3 |
| 周日 7/5 | IG Carousel #10 + WA 简报 | ⬜ | 2 |
| **合计** | **10** | **1** | **9** |

### 安全建议（本次审计发现）

| 发现 | 优先级 | 建议 |
|------|:--:|------|
| 缺少 HSTS header | 🔴 高 | 加 `Strict-Transport-Security` |
| 缺少 CSP | 🟡 中 | 加 Content-Security-Policy |
| 缺少 X-Frame-Options | 🟡 中 | 防点击劫持 |
| /products /about 未入 sitemap | 🟡 中 | 补入 |
| 仅 3 张 img | 🟡 低 | 产品页加实物图 |
| 社媒数据盲区 | 🔴 高 | 老板截图 → 我归档 |

---

> V2 审计完成：2026-07-04 · 米迦勒
> 下次审计：部署后或老板指令

---

## 五、社媒实时数据 (2026-07-04 20:30 更新)

| 平台 | 账号 | 粉丝 | 关注 | 帖子 | 方法 |
|------|------|:--:|:--:|:--:|------|
| **Instagram** | @kalistorik | 0 | 0 | **4** | curl OG meta ✅ |
| **Facebook** | Page kalistorik | ? | — | ? | curl OG meta（粉丝未暴露）|
| **LinkedIn** | 个人号 kalistorik | ? | — | ? | ❌ 登录墙 |

### IG 趋势
- 7/1：0 Followers / 0 Following / **2 Posts**
- 7/4：0 Followers / 0 Following / **4 Posts**（+2）

### 缺口
- FB 粉丝数、帖子数需手动查看
- LI 全盲

---

## 六、Google Analytics 数据 (2026-07-04)

### 用户概览

| 时间范围 | 用户数 | 变化 |
|:--|:--:|:--:|
| 过去 30 天 | 34 | +6.3% |
| 过去 7 天 | 5 | +28.6% |
| 过去 1 天 | 1 | +75.0% |
| 实时在线 | 1 (Hong Kong) | — |

### 流量来源

| 渠道 | 会话数 | 占比 |
|------|:--:|:--:|
| Organic Social | 13 | — |
| Direct | 11 | 73.8% |

### 页面浏览分布

| 页面 | 浏览 | 变化 |
|------|:--:|:--:|
| KALIS TORIK · Chinese Furniture Sourcing (首页 EN) | 111 | +25.0% |
| KALIS TORIK Picks | 4 | +50.0% |
| KALIS TORIK - Sourcing Partner | 2 | +71.4% |
| DE 首页 | 3 | — |
| FR 首页 | 3 | — |
| Quality Control | 0 | 100% |
| Freight | 0 | 100% |

### 访客地理

| 国家 | 用户 | 占比 |
|------|:--:|:--:|
| Hong Kong | 4 | 42.9% |
| China | 1 | 0.0% |
| Japan | 1 | — |
| United States | 1 | — |

### 关键事件

| 事件 | 次数 | 变化 |
|------|:--:|:--:|
| page_view | 124 | +25.7% |
| user_engagement | 108 | +10.0% |
| scroll | 42 | +7.7% |
| session_start | 24 | +42.9% |
| click | 14 | +7.7% |
| wa_redirect | 4 | +20.0% |
| first_visit | 2 | +60.0% |

---

## 七、LinkedIn 数据 (2026-07-04)

### 账号：Max Zuo | Founder & Sourcing Director at KALIS TORIK

| 指标 | 数值 |
|------|:--:|
| 档案浏览量 | 0 |
| 动态展示量 (近 7 天) | 118 |
| 搜索分析 | 2 |
| 关注者 | 0 |

### 最近帖子

| 帖子 | 展示 | 回应 | 评论 |
|------|:--:|:--:|:--:|
| "wholesaler vs direct sourcing" | 57 | 2 | 3 |
| "5 things buyers said this week" | 42 | — | — |

---

## 八、三平台汇总 (2026-07-04)

| 平台 | 粉丝 | 帖子 | 展示/浏览 | 趋势 |
|------|:--:|:--:|:--:|:--:|
| **IG** @kalistorik | 0 | 4 | — | 7/1 → 7/4: +2 帖 |
| **LI** Max Zuo | 0 | ≥4 | 118/7天 | 展示增长中 |
| **FB** kalistorik | ? | ? | — | 需手动查看 |
| **网站** kalistorik.com | — | — | 34 UV/30天 | HK 为主 |

### 分析

- **网站流量极低** (34 UV/30天, ≈1/天)，主要来自 HK + Direct/Organic Social
- **LI 是唯一有展示数据的平台** (118/7天)，但 0 档案浏览 = 无人点进主页
- **IG 0 粉丝 4 帖** — 内容在发但零触达
- **核心问题**：三平台 + 网站全无欧洲访客（目标市场完全未触达）

