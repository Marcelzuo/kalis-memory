# Google Looker Studio 数据看板 — 配置指南

> GA4 属性: `G-YRPEYWWLM1` (kalistorik.com)
> 免费工具，无需付费。以下为手动创建步骤。

## 前置条件

- Google 账号（与 GA4 属性关联的账号）
- 浏览器登录

## 创建步骤

### 1. 新建报告

1. 打开 [lookerstudio.google.com](https://lookerstudio.google.com)
2. 点击 **Create** → **Report**
3. 选择国家 + 勾选条款 → 继续

### 2. 添加数据源

1. 弹窗中选择 **Google Analytics** 连接器
2. 在右侧面板找到 GA4 属性 **G-YRPEYWWLM1** (显示名为 kalistorik.com 或 KALIS TORIK)
3. 点击 **Add** 确认字段列表
4. 点击 **Add to report** 完成数据源绑定

### 3. 关键指标卡片 (Scorecards)

从工具栏添加 **Scorecard** 组件，逐一配置：

| 指标卡片 | 指标 (Metric) | 建议名称 |
|----------|-------------|---------|
| UV (独立访客) | `Total users` | Visitors |
| 会话数 | `Sessions` | Sessions |
| 转化事件 | `Event count` + 筛选 `event_name = form_submit` | Conversions |
| 国家分布 | 新建 Table，维度 `Country`，指标 `Total users` | Countries |
| 来源/媒介 | Table，维度 `Session source / medium`，指标 `Sessions` | Traffic Sources |

### 4. 添加趋势图 (Time Series)

1. 工具栏 → **Time series chart**
2. 维度: `Date`
3. 指标: `Total users`, `Sessions`
4. 日期范围: 默认 30 天

### 5. 添加地理图 (Optional)

1. 工具栏 → **Geo chart**
2. 维度: `Country`
3. 指标: `Total users`

### 6. 样式调整

- 主题: 右上角 **Theme and layout** → 选一个深色/浅色主题
- 页面标题: 双击顶部 → `KALIS TORIK Analytics`
- 右上角 **Share** → 设置查看权限（Anyone with link can view）

### 7. 保存 & 分享

- 文件自动保存到 Google Drive
- **Share** → **Get report link** → 复制嵌入 URL
- 可选嵌入: **File** → **Embed report** → 获取 `<iframe>` 代码

## 建议的看板布局

```
┌────────────────────────────────────────────┐
│  KALIS TORIK Analytics         (date range) │
├──────────┬──────────┬──────────┬───────────┤
│ Visitors │ Sessions │ Conv     │ Bounce    │
│  (UV)    │          │ (form)   │  Rate     │
├──────────┴──────────┴──────────┴───────────┤
│         Users + Sessions trend             │
│         (30-day time series)                │
├──────────────────────┬─────────────────────┤
│   Countries (table)  │  Traffic Sources     │
│                      │  (table)            │
└──────────────────────┴─────────────────────┘
```

## 故障排查

- **找不到 GA4 属性**: 确认当前 Google 账号有该 GA4 属性的 Read & Analyze 权限
- **数据为空**: 新创建的 GA4 属性需 24-48 小时才有数据
- **指标报错**: 检查指标名称是否与 GA4 字段名完全一致
