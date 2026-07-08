# 备份规则

## 大备份（老板说"大备份"）
- 收集规则文件
- commit + push `Marcelzuo/kalis-memory`
- 其他人只读

## 小备份
- 触发: 部署后 / 距上次 >24h
- 路径: `~/.codex/backups/`，保留最近 10 个
- 路西法自己管: `~/.hermes/backups/`

## 共用备份库红线
- `Marcelzuo/kalis-memory` 内任何文件/目录，**删除前必须经老板同意**
- 仅允许：新增（commit+push）、更新配置（agents/）、只读查询
- 禁止：删文件、删目录、改历史

## 检查点
大事前写 `~/.codex/state/checkpoint.json`:
```json
{
  "last_action": "描述当前操作",
  "pending_tasks": ["待办列表"],
  "timestamp": "ISO时间"
}
```
Codex 重启后自动读，提示"上次停在 X，继续？"
