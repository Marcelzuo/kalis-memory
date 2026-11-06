# KALIS TORIK Instagram 运营手册 v2.0

> 基于 Instagram 官方帮助中心真实数据研究 + 社交媒体爆火机制深度分析
> 2026-06-11 | 天使长 Michael (Codex) | 第二版（内容策略重塑）

---

## 一、IG 平台硬规格（来自 Instagram 官方帮助中心）

### 1.1 Feed 图片帖

| 参数 | 规格 | 来源 |
|------|------|------|
| 最大宽度 | **1080px** | help.instagram.com/1631821640426723 |
| 宽高比 | **1.91:1 ~ 3:4**（即 1080×566 ~ 1080×1440） | 同上 |
| 最低分辨率 | 320px 宽（低于此会强制放大） | 同上 |
| 超出处理 | 超 1080px 自动缩小；宽高比不符自动裁剪 | 同上 |
| 多图轮播 | 最多 **10 张**图片/视频混合 | opencli instagram post --help |
| 文字说明 | 最多 **2,200 字符**；显示前 2 行后折叠 | Instagram 公开文档 |
| 标签上限 | 每条帖子最多 **30 个** hashtag | Instagram 公开文档 |

### 1.2 Reels 短视频

| 参数 | 规格 | 来源 |
|------|------|------|
| 宽高比 | **1.91:1 ~ 9:16** | help.instagram.com/1038071743007909 |
| 帧率 | 最低 **30 FPS** | 同上 |
| 分辨率 | 最低 **720p**（建议 1080×1920） | 同上 |
| 封面图 | 建议 **420×654px** (1:1.55)，上传后不可修改 | 同上 |
| 时长 | 3秒 ~ **90秒**（手机端）；最长15分钟 | Instagram 公开文档 |
| 格式 | **.mp4** 单文件 | opencli instagram reel --help |

### 1.3 Story 快拍

| 参数 | 规格 |
|------|------|
| 宽高比 | **9:16** 竖屏 |
| 分辨率 | 1080×1920px |
| 时长 | 每张 **15 秒**，**24 小时后自动消失** |

---

## 二、账号设置（必做步骤）

### 2.1 切换专业账户

1. Settings → Account → Switch to Professional Account
2. 选择 **Business**（不是 Creator）
3. 类别选 **"Furniture"** 或 **"Home Decor"**
4. 关联 Facebook Page（如果有的话）

### 2.2 主页信息

| 字段 | KALIS TORIK 内容 |
|------|-------------------|
| 头像 | 终版圆形头像 dark 版（600×600，黑底金线白字） |
| Bio | `European Furniture Sourcing Partner. 20 yrs · 100+ factories in China. We audit. You source. No loose ends.` |
| 链接 | `kalis-torik.com`（可配合 Linktree） |
| 联系方式 | 邮箱 + WhatsApp Business 按钮 |

### 2.3 关键设置

- **消息**: 开启欢迎消息 + 自动回复（"Thanks for reaching out. We'll get back within 24h."）
- **隐藏词**: 暂不设置
- **协作**: 暂不开启

---

## 三、内容策略（核心·颠覆版）

### 3.0 核心认知：为什么传统打法必死？

传统 sourcing agent 的 IG 上只有三种内容：
- 📸 工厂大门 + 车间照 → 所有工厂看起来一样
- 📸 成品摆拍 → 看起来像淘宝卖家
- 📸 "5 Tips for Sourcing" → 没人关心第 5 条是什么

**客户的真实心理**：他们刷到这些帖子的那一刻，脑子里只有一个念头——"又一个中间商想赚我钱"。你的帖子还没被看完就已经被判定为 spam。

**要打破这个循环，必须做到**：
1. 前 3 秒让客户**停住手指**（Pattern Interrupt）
2. 让客户感觉**你在说他心里没说出口的话**（Pain Point Resonance）
3. 让客户觉得**你跟所有其他中国人不一样**（Differentiation Shock）
4. 让客户忍不住**转发给同事**（Shareability Hook）

---

### 3.1 五大爆火内容框架

以下每个框架都基于社交媒体行为心理学设计，不是随意拼凑。

---

#### 🔥 框架一：「真相炸弹」— The Truth Bomb

**心理机制**：制造认知失调。客户以为"中国采购就是这样"，你告诉他"你被骗了"。

**内容形式**：Reels 30-45s，大字幕 + 工厂实拍 + 对比画面

**帖文模板**：

```
Hook（前3秒大字）：
"YOUR SUPPLIER IS LYING TO YOU."

内容（快速切换）：
镜头1: 一个"看起来不错"的产品 →
镜头2: 翻过来，露出粗糙的背面/接缝 →
大字: "They showed you this." / "We found THIS."

镜头3: 质检报告特写，红圈标出不合格项 →
大字: "We rejected 47% of this batch. Most agents would ship it."

结尾CTA：
"One partner who actually checks. DM us."

Caption:
Last month we inspected a shipment for a client in Hamburg.
47% rejection rate. The factory was shocked — "the last agent never checked."

That's the difference between a sourcing partner and a forwarding address.

We don't pass problems to you. We find them first.
📩 DM to work with someone who actually opens the boxes.

#SourcingTruth #ChinaFactory #QualityControl #KALISTORIK
```

**关键要素**：
- ❌ 不说"我们质量好"
- ✅ 说"我们拒收了 47%"
- 数据越具体越可信

---

#### 🔥 框架二：「你不该看到的画面」— Forbidden Footage

**心理机制**：稀缺性 + 窥探欲。客户知道工厂存在，但从没见过里面真实的样子——尤其是不好看的样子。

**内容形式**：Reels 30-60s，手持拍摄，不剪辑过度，保留环境音

**帖文模板**：

```
Hook（前3秒大字）：
"Most sourcing agents won't show you this."

内容（一镜到底/少剪辑）：
镜头1: 走进工厂大门（手持，轻微晃动——真实感）
镜头2: 扫过原料堆放区
镜头3: 停在 QC 台，镜头对准正在被拒收的产品
大字: "This piece failed. Here's why..."

镜头4: 手指指出缺陷位置——
大字: "Joint gap > 2mm. EU standard is 0.5mm."

结尾CTA:
"We see it so you don't have to. DM us."

Caption:
No filters. No studio lighting. This is what a real factory QC walk looks like.

The piece in this video failed our check. Most agents never even step on the factory floor — they just forward the factory's own photos to you.

We're different.
📩 DM us to start sourcing with eyes on the ground.

#FactoryReality #ChinaSourcing #BehindTheScenes #KALISTORIK
```

**关键要素**：
- ❌ 不摆拍，不美化
- ✅ 手持拍摄、环境音保留
- 展示"不够好"的东西比展示"好的"更有说服力

---

#### 🔥 框架三：「同行不敢说的话」— The Unspoken Truth

**心理机制**：打破行业潜规则。客户隐约知道有问题，但从没人公开说破。

**内容形式**：Feed 轮播（6-10 张图）或 Reels，文字为主，配合实拍图

**帖文模板**：

```
Slide 1 (黑底白字，冲击力):
"3 REASONS YOUR CHINA SOURCING IS COSTING YOU 30% MORE"

Slide 2:
"#1 Your 'factory price' isn't the factory price."
配图：一张模糊的报价单，红笔圈出中转加价
大字: "Middlemen mark up 15-40%. You're paying for their margin, not better quality."

Slide 3:
"#2 Your 'dedicated QC team' is the factory's own staff."
配图：工厂工人自己给自己质检的讽刺画面
大字: "We use independent inspectors. The factory doesn't pay them."

Slide 4:
"#3 'Express shipping' means it sits in port for 2 weeks."
配图：集装箱码头
大字: "We track from factory floor to your door. Real tracking, not promises."

Slide 5 (CTA 页):
"The difference isn't price. It's who's watching."
📩 DM us.

Caption:
Most European buyers are overpaying by 30% and they don't even know it.

Not because the products are more expensive — because the supply chain isn't transparent.

We've spent 20 years building a process that cuts out the hidden costs.
📩 DM to see how we do it.

#SourcingCosts #SupplyChainTransparency #ChinaSourcing #KALISTORIK
```

**关键要素**：
- 直接挑战行业现状
- 用数字说话（30%, 15-40%）
- 不攻击任何具体公司，但让客户自动对号入座

---

#### 🔥 框架四：「我搞砸了」— The Failure Confession

**心理机制**：脆弱性 = 可信度。所有人都说自己好，但没人敢说自己错过。你敢说，你就是唯一值得信任的。

**内容形式**：Reels 或 Feed 帖，个人化口吻，不回避问题

**帖文模板**：

```
Hook（前3秒大字）：
"I cost a client €12,000. And he still works with us."

内容：
镜头1: 本人出镜或声音出镜（可选），讲述故事
大字逐句出现:

"2023. A shipment of Italian-style dining chairs."
"The factory changed the wood without telling us."
"We caught it. But we were 2 days too late."

镜头2: 仓库里堆着的退货产品
大字: "We paid for the rework. Not the client."

镜头3: 客户邮件截图（脱敏）——
大字: "'Thanks for being honest. Send the next batch.'"

结尾:
"This is why we inspect BEFORE production ends. Not after."
📩 DM us.

Caption:
I've been doing this for 20 years. Mistakes still happen.

The difference between a good agent and a bad one isn't perfection — it's who pays when things go wrong.

We do.
📩 DM us.

#SourcingHonesty #RealTalk #ChinaFactory #KALISTORIK
```

**关键要素**：
- 暴露弱点反而建立信任
- 故事必须有真实细节（时间、金额、产品类型）
- 结局必须正面（客户还愿意合作）

---

#### 🔥 框架五：「你的竞争对手已经行动了」— Social Proof Bomb

**心理机制**：FOMO（害怕错过）。当客户看到"别人已经在用这个服务了"，焦虑驱动行动。

**内容形式**：Feed 轮播，数据可视化风格

**帖文模板**：

```
Slide 1 (大字):
"A Berlin furniture brand just cut their sourcing costs by 22%."

Slide 2:
数字可视化: "Before: €147/unit → After: €115/unit"
配图: 产品细节

Slide 3:
"Same factory. Same quality. Different partner."
"Because we negotiate in Mandarin. Not through 3 middlemen."

Slide 4:
"What they changed:"
✅ Direct factory relationship
✅ Independent QC
✅ Consolidated shipping
❌ No more 'agent fees'

Slide 5 (CTA):
"Your competitors aren't waiting. DM us."

Caption:
We helped a Berlin-based brand reduce unit costs by 22% — same factory, same specs, same quality.

The only thing that changed? Who was on the ground in China.

📩 DM us to see if we can do the same for you.

#SourcingSuccess #CostReduction #FurnitureBusiness #KALISTORIK
```

**关键要素**：
- 必须用真实案例（可脱敏但保持核心数据真实）
- "你的竞争对手"比"你的同行"更有冲击力
- 具体数字（22%, €147→€115）

---

### 3.2 五大框架轮换节奏

```
Week 1: 真相炸弹（Mon）→ 你不该看到的画面（Wed）→ 同行不敢说的话（Fri）
Week 2: 我搞砸了（Mon）→ 你的竞争对手（Wed）→ 真相炸弹（Fri）
Week 3: 同行不敢说的话（Mon）→ 你不该看到的画面（Wed）→ 你的竞争对手（Fri）
Week 4: 真相炸弹（Mon）→ 我搞砸了（Wed）→ 你不该看到的画面（Fri）
```

**Story 穿插**（每天 1-3 条）：
- 当天看了什么产品（手机随手拍，不要精修）
- 这周拒收了什么（一个产品 + 一行字解释为什么）
- 客户说了什么（截图脱敏）
- 行业新闻转发 + 一行评论

---

### 3.3 表达方式的铁律

| 规则 | 解释 |
|------|------|
| **Hook 用英文大字幕，前 3 秒必须出现** | 客户在快速滑动，没时间等你铺垫 |
| **永远不说"我们是最好的"** | 说"我们拒收了 47%"。让事实替你吹牛 |
| **每帖只说一个核心信息** | 一次只想让客户记住一件事 |
| **用"你(you)"不是"客户(client)"** | "Your supplier lied" 比 "Suppliers often misrepresent" 强 10 倍 |
| **数据必须真实** | 47% 就是 47%，不是"大约一半" |
| **结尾必须有 CTA** | 告诉客户看完之后该干嘛（DM us / Comment / Save） |
| **不要公司腔，要真人腔** | 想象你是在酒吧里跟朋友聊天，不是在写企业宣传册 |
| **图片不要精修过度** | 越像"手机拍的"越可信——但要清晰 |
| **Reels 优先于 Feed** | IG 算法目前重推 Reels，新号靠 Reels 冷启动最快 |
| **Caption 第一句决定展开率** | 前 125 字符必须让人想点"...更多" |

---

## 四、Hashtag 策略

### 4.1 分层体系

| 层级 | 数量 | 示例 |
|------|------|------|
| **品牌标签** | 1-2 | #KALISTORIK |
| **核心业务** | 3-5 | #FurnitureSourcing #ChinaFactory #SourcingAgent #SupplyChain |
| **痛点标签** | 3-5 | #SourcingTruth #FactoryReality #QualityControl #CostReduction |
| **行业标签** | 5-8 | #EuropeanFurniture #InteriorDesign #FurnitureBusiness #HotelFurniture |
| **长尾标签** | 3-5 | #FurnitureFromChina #RestaurantFurniture #MadeInChina |

每帖 15-25 个标签，不超过 30 个。

---

## 五、发布节奏与最佳时机

| 内容类型 | 频率 | 最佳时间（CET 欧洲时间） |
|----------|------|--------------------------|
| Feed 帖 | 每周 3 篇 | 周二/四/六 10:00 或 14:00 |
| Reels | 每周 1-2 条 | 周三/周五 12:00 |
| Story | 每天 1-3 条 | 分散全天 |

> 对应北京时间：冬季 17:00/21:00，夏季 16:00/20:00。

---

## 六、通过 opencli 自动化发帖

### 6.1 前提条件

```bash
opencli doctor  # 确认全部绿色
# Chrome 需以调试模式运行、已安装 opencli 扩展、已登录 Instagram
```

### 6.2 核心命令

```bash
# Feed 图片帖（单图）
opencli instagram post "Caption text" --media path/to/image.jpg

# Feed 轮播帖（多图）
opencli instagram post "Caption text" --media img1.jpg,img2.jpg,img3.jpg

# Reels 短视频
opencli instagram reel "Caption text" --video path/to/video.mp4

# Story 快拍
opencli instagram story --media path/to/image.jpg

# 查看个人主页 / 搜索用户 / 浏览探索页
opencli instagram profile kalistorik
opencli instagram search "furniture sourcing"
opencli instagram explore
```

### 6.3 自动化脚本

```bash
#!/bin/bash
# weekly-post.sh — KALIS TORIK 周发帖脚本

CAPTION="Your supplier showed you this. We found THIS.

#SourcingTruth #KALISTORIK"

opencli instagram post "$CAPTION" \
  --media ./this-week/1.jpg,./this-week/2.jpg,./this-week/3.jpg \
  --window background
```

---

## 七、增长路线图（3个月）

### 第1月：冷启动

- 目标：**100 粉丝**
- 策略：
  - 发布 12-15 条内容（Reels 占 60%）
  - 用「真相炸弹」和「你不该看到的画面」打头阵
  - 每天手动互动 15 分钟（给同行帖子写有观点的评论，不是"Nice post!"）
  - 完善 Highlights 合集

### 第2月：内容深化

- 目标：**300 粉丝 + 首次询盘**
- 策略：
  - 加「我搞砸了」框架（建立深度信任）
  - 加「你的竞争对手」框架（制造 FOMO）
  - 测试 $5/天小额广告定向欧洲家具/室内设计人群
  - 发布 1-2 个客户成功案例

### 第3月：稳定增长

- 目标：**500 粉丝 + 3-5 个询盘**
- 策略：
  - 分析 Insights，哪个框架数据最好就多做哪个
  - 考虑与欧洲家具 KOL 合作
  - 加大广告预算（如果 ROI > 3x）

---

## 八、避坑指南

- ❌ 低分辨率图片（必须 ≥1080px 宽）
- ❌ 带其他平台水印
- ❌ 有版权问题的音乐（Reels 用 IG 内置音乐库）
- ❌ 过度销售话术（"Best quality! Lowest price!" —— 算法降权 + 客户反感）
- ❌ 空洞的 hashtag 堆砌
- ❌ 精修到像广告大片的图片（越像广告越没人看）
- ✅ 所有图片加半透明 "KALIS TORIK" 水印防盗
- ✅ 工厂图片去掉 GPS 位置信息
- ✅ 客户信息必须脱敏
- ✅ 正文英文为主

---

## 九、KPI 追踪

| 指标 | Week 1 | Week 2 | Week 4 | Month 3 |
|------|--------|--------|--------|---------|
| 粉丝数 | >20 | >50 | >100 | >500 |
| 平均点赞 | >15 | >25 | >40 | >80 |
| 评论数 | >3 | >8 | >15 | >30 |
| 保存数 | >5 | >10 | >20 | >50 |
| 分享数 | >2 | >5 | >10 | >25 |
| Reach | >500 | >1000 | >3000 | >10000 |
| 询盘（DM/邮件） | 0 | 0-1 | 1-2 | 3-5 |
| 网站点击 | >20 | >50 | >100 | >300 |

---

## 十、每周核查清单

- [ ] 本周发布了 **3 条内容**（至少 2 条 Reels）
- [ ] 每条 Hook 在前 3 秒出现
- [ ] 每条有清晰的单一信息 + CTA
- [ ] 所有图片分辨率 ≥1080px 宽
- [ ] Hashtag 按分层策略使用
- [ ] 回复了所有评论（24h 内）
- [ ] DM 询问在 12h 内回复
- [ ] 检查了 Insights 数据
- [ ] 准备了下一周的内容素材
- [ ] Story 每天都有更新

---

> **研究数据来源**：
> - help.instagram.com/1631821640426723（照片分辨率）
> - help.instagram.com/1038071743007909（Reels 尺寸与宽高比）
> - help.instagram.com/1554245014870700（Instagram for Business）
> - www.facebook.com/business/help/2265970220185807（Instagram 广告功能）
> - opencli instagram post/reel/story --help（适配器发帖接口）
>
> **执行者**：天使长 Michael (Codex) | **日期**：2026-06-11 | **版本**：v2.0（内容策略重塑）
