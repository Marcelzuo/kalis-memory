# Task — favicon 同步 + 记忆库迁移

**派单人**：Michael（经老板授权）
**时间**：2026-06-12
**状态**：待执行

## 执行顺序

### 1. favicon 方案 A 先动
- 拷 nginx 端 7 个 favicon 文件到 `kalistorik-site/dist/`
- 拷 `workspace/index.html`（带 `?v=20260612` 的 icon 引用）到 `dist/`
- commit: `favicon: nginx 同步 Pages dist/`
- push → 通知 Michael 验 + deploy

### 2. 记忆库迁移随后
- `git mv` 老路径 → 新路径（daily/{person}/ + topics/{topic}/）
- 跑 `find memory/ -type f | sort` → 存 `shared/MIGRATION-VERIFY.md`
- 写 `README.md` + `topics/INDEX.md`
- commit: `🚚 migrate: memory structure v2`
- push

### 3. 时间
- 14:00 不是硬死线，做完就行

## 通信协议更新（老板授权）

以后 Michael ↔ Satan 任务派发走共享仓库 `shared/tasks/`。openclaw agent 仅用于 3 字 ping。
