# 资料通道库（分类版）

> 米迦勒维护 · 玛门/路西法/米迦勒三兄弟共用。找素材/数据/搜索前先查本表定位通道，禁止乱试。
> 更新时间：2026-09-03。✅=实测可用；⚠️=待验证/需条件。

## 0. 总规则（写死）

1. 先判内网/外网：Clash 端口 7890/7891/7897 探测，规则见 `ops/web-search.md`。
2. 简单/机械任务用 Flash 模型；深度/创作/严谨任务用 Pro 模型（见 `ops/team.md`）。
3. 同一源失败 1 次即换；2 个不同源都失败 → 报米迦勒，不再空转、不 sleep 重试。

## 1. 图片素材

### 国内（优先）
- 百度图片 / 花瓣网 / 站酷 / 图虫 / 小红书 / 抖音
- 红线：出现外国面孔必须换中国人；出现国外品牌 logo 必须剔除或替换。

### 海外（仅补充）
- ✅ Pexels CDN 直链（⚠️ 搜索页 curl 直接 403，禁用）：
  - `https://images.pexels.com/photos/{photo_id}/pexels-photo-{photo_id}.jpeg?auto=compress&cs=tinysrgb&w=1600`
  - 需要照片 ID：用 `opencli browser` 打开搜索页提取，或查下方已知 ID。
  - 已知可用 ID（货轮/港口/堆场，2026-09-03 验证）：34492032 / 32508222 / 36771191 / 35459333 / 32399136 / 36269623。
- ⚠️ Unsplash / Pixabay：curl 可能被反爬，需走 `opencli browser`，待验证。

## 2. 视频素材
- ⚠️ Pexels Videos / Pixabay Videos：待验证（建议走 opencli browser 或视频 CDN 直链）。
- 自有素材：`~/kalis-video/`、`~/Desktop/家具/`。

## 3. 音乐（无版权）
- ✅ 本地库 `~/kalis-video/audio/`：
  - `ambient_electronic` · `industrial_cinematic` · `industrial_dark_ambient` · `minimal_techno` · `music` · `sad_piano_heartbreaking` · `sea_whisper_electronic`
- ✅ 国内 CC0 通道：
  - 耳聆网 `https://www.ear0.com/`：CC0 声音/背景音乐，作者 `kingphosphor` 有 30s/35s/40s 背景音乐系列
  - 淘声网 `https://www.tosound.com/`：聚合耳聆网/Freesound/Looperman，可搜“音乐：平静/氛围/极简”，按 `X-Requested-With: XMLHttpRequest` 抓 `/search/word-<词>/page-1`
  - 耳聆网预览直链：`https://down.ear0.com:3321/index/preview?soundid=<ID>&type=mp3&audio=sound.mp3`
- ⚠️ Pixabay Music / YouTube Audio Library：待验证下载通道；海外 CC0 备选 Openverse API。

## 4. AI 生图
- ✅ DashScope 通义万相 `wanx2.0-t2i-turbo`（100张/天）：POST → 轮询 task_id → 下载。
- 竖版白名单最高 720×1280；需要 ≥1440 用 1.5× 上采样。
- Prompt 必须指定 Chinese/Asian 面孔（不指定默认出外国脸，违反品牌红线）。

## 5. 搜索
- 国内：搜狗 `curl -sL --max-time 10 -A "Mozilla/5.0" "https://www.sogou.com/web?query=<URL编码>"`；百度备选；必应 RSS `https://www.bing.com/search?q=<词>&format=rss`。
- 海外（开 Clash）：Google / DuckDuckGo / Bing 国际。
- 禁止：`claude` 的 WebSearch/WebFetch；未开 Clash 访问外网。

## 6. A 股行情
- 实时报价：`opencli eastmoney quote <代码> -f json`
- 资金榜：`opencli eastmoney money-flow --limit 100 -f json`
- 板块：`opencli eastmoney sectors -f json`
- 日 K：新浪 `quotes.sina.cn/cn/api/jsonp_v2.php/...getKLineData?symbol=<sz|sh+代码>&scale=240&ma=no&datalen=120`
- 禁：东财 `push2his.eastmoney.com` K线接口（已断）。

## 7. 社媒数据 / 后台
- Chrome 登录态 AppleScript：GA4 / LinkedIn / Facebook / Instagram 后台数据。
- 细节见 `kalistorik/social/rules.md` 数据采集 SOP。

## 8. 浏览器通道（绕过 curl 反爬）
- ✅ `opencli browser <session> open <url>` + `state` / `eval` / `network`：真 Chrome 渲染，用于被反爬页面的 ID/数据提取。
- 备选：in-app Browser / chrome control。
