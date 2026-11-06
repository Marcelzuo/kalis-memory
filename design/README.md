# 共享设计法典

本目录是三兄弟共用的网站设计真源，不是备份附件。

## 三层结构

| 层 | 路径 | 作用 | 可否修改 |
|---|---|---|---|
| 规则层 | `design/kalistorik/website/` | 当前有效的设计规则与决策 | 可版本化更新 |
| 方案层 | `backups/site-design/` | 每轮调研、方案、证据快照 | 冻结，不改历史 |
| 部署层 | `backups/site/` | 可回滚的整站代码快照 | 冻结，不改历史 |

## 使用规则

- 修改网站视觉、文案、信息架构、图片或转化路径前，先读 `DESIGN-SYSTEM.md` 和 `DECISION-LOG.md`。
- 老板的最新明确指示 > 本设计系统 > 单轮方案 > 个人审美。冲突时记录到决策日志，不口头覆盖。
- 设计规则变更用 `docs:` 提交；整站部署快照仍按 `site-YYYYMMDD-HHMM-<版本>-<描述>` 命名。
- 方案轮次按 `design-YYYYMMDD-NN-<描述>` 命名；`NN` 是当天第几轮，不塞进站点版本号。
- 每次部署前备份；未备份不上线，未三方检查不部署。

## 当前入口

- 设计系统：`kalistorik/website/DESIGN-SYSTEM.md`
- 决策记录：`kalistorik/website/DECISION-LOG.md`
- 首轮方案备份：`../backups/site-design/design-20261106-01-europe-style-benchmark/`
