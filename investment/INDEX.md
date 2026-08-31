# 投资 INDEX（唯一入口）

> 用法：先看触发词，跳到精确文件；文件里找不到再回本表。不多读不少读。
> 每日收盘复盘后同步清理本表：删除失效链接，只保留终版。

## 最快路径

| 要找什么 | 文件 |
|:--|:--|
| 今天/当前持仓、触发价、盯盘、资金分配 | `strategies/active/current-watchlist.md` |
| 操作规则/止损止盈/换股/仓位/持仓周期/过周末 | `strategies/stock/rules-operation.md` |
| 个股规则/选股/多条件交集/盈亏比≥2 | `strategies/stock/rules-stock.md` |
| 大盘规则/仓位分级/大盘走弱 | `strategies/market/china-policy-hotspot.md` |
| 规则迭代/复盘教训/今天学到什么 | `strategies/stock/lessons-log.md` |
| 留存/归档/清理/每日整理 | `RETENTION.md` |
| 今日午间复盘/上午对账/午后预测 | `analysis/2026-08-28-midday-review.md` |
| 今日盘前决议/三情景/买不买/什么价买 | `analysis/2026-08-31-preopen.md` |
| 今日收盘复盘/四兄弟比对/终审 | `analysis/2026-08-31-close-review.md` |
| 明日候选/四人独立选股/综合三只 | `analysis/2026-08-31-four-screens.md` |
| 2026-08-28 终版推荐（排名/资金/买点/大盘区间/赔率/事件） | `analysis/2026-08-28-final-recommendation.md` |
| 中国市场特点/政策市/热点市 | `strategies/market/china-policy-hotspot.md` |
| ETF 长期组合与收益测算 | `strategies/etf/2026-08-25-etf-strategy.md` |
| 美股/AI 泡沫终审结论 | `analysis/2026-08-25-us-ai-bubble.md` |
| 个股/指数查询快照 | `data/quotes/`、`data/market/` |
| 外部研究素材 | `data/research/` |
| 国外机构/投行对 A股+房地产 2025–2026 观点汇总 | `data/research/2026-08-30-foreign-institutions-china-outlook.md` |
| 投资数据源总表 | `data/research/sources.md` |
| 查询/搜索台账 | `data/ledger/` |
| 今日最终决策/空仓观察期/资金分配结论 | `discussions/2026-08-27-decisions.md` |
| 午间复盘/上午对账/午后预测/冲高回落/不追高 | `analysis/2026-08-28-midday-review.md` |

## 触发词

| 触发词 | 文件 |
|:--|:--|
| 止损/止盈/换股/仓位/操作/每日重筛/持股时长/过周末/候选池失效线/剔除/期望值/交易台账/样本量/单笔风险封顶/仓位公式/压力测试 | `strategies/stock/rules-operation.md` |
| 选股/个股/多条件交集/技术硬门槛/盈亏比≥2/入场三问/期望值门槛/ATR/量比/RSI/回测 | `strategies/stock/rules-stock.md` |
| 大盘/仓位分级/大盘走弱/生命线/涨停潮 | `strategies/market/china-policy-hotspot.md` |
| 教训/复盘/T+1/不接飞刀/规则迭代/和胜放量 | `strategies/stock/lessons-log.md` |
| 留存/归档/清理/过期数据/每日整理 | `RETENTION.md` |
| 当前核心3只+候补3只/中天/工业富联/招金/唯万/泰凌微/和胜 | `strategies/active/current-watchlist.md` |
| 三只排名/资金分配/买多少股/什么价进/赔率/来源分层/事件日历/大盘指数预测 | `analysis/2026-08-28-final-recommendation.md` |
| 今日收盘复盘/四兄弟比对/终审/招金富联中天 | `analysis/2026-08-28-close-review.md` |
| ETF/定投/5年/10年收益 | `strategies/etf/2026-08-25-etf-strategy.md` |
| 美股/AI 泡沫/经济危机/看空 | `analysis/2026-08-25-us-ai-bubble.md` |
| 历史数据/原始行情/个股查询记录 | `data/quotes/`、`data/market/` |
| Grantham/格兰瑟姆/AI capex/论坛情绪 | `data/research/` |
| 国外投行/外资观点/海外 A股展望/海外房地产展望 | `data/research/2026-08-30-foreign-institutions-china-outlook.md` |
| 数据源/权威网站/基金官网/来源分层 | `data/research/sources.md` |
| 今日最终决策/空仓观察期/资金分配结论 | `discussions/2026-08-27-decisions.md` |
| 午间复盘/上午对账/午后预测/冲高回落/不追高 | `analysis/2026-08-28-midday-review.md` |
| 旧方案/已否决/历史版本 | `archive/` |

## 铁律

1. 每次查个股/指数行情 → 必须落盘到 `data/quotes/YYYY/MM/YYYY-MM-DD/` 或 `data/market/YYYY/MM/YYYY-MM-DD/`。
2. 新结论 → 先写对应文件，再更新本表；旧版移 `archive/`，不保留重复版本。
3. 当前状态只放 `strategies/active/`；`data/` 只存原始快照；`strategies/` 只存规则；`discussions/` 只存决策过程。
4. 每日收盘后：清理冗余、剔除否决项、只留终版，并同步本表。
