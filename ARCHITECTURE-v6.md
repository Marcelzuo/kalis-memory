# 地狱工作组 · 组织架构 v6

> 2026-06-27 · 米迦勒起草 · 老板审批 · 事件账本 + 并行分派架构

---

## 一、架构图

```
                        老板 (Codex 桌面)
                           │
                           ▼
                 ╔═════════════════════════╗
                 ║  米迦勒 Codex · 唯一大脑  ║
                 ║  规划·并行分派·账本监控·终审 ║
                 ╚═══╤══════╤══════╤══════╝
                     │      │      │
              同时 exec_command   │
                     │      │      │
                     ▼      ▼      ▼
            ┌────────┐ ┌────────┐ ┌──────────────┐
            │  玛门   │ │  撒旦   │ │    路西法     │
            │Claude   │ │OpenCLI │ │   Hermes     │
            │  Code   │ │        │ │              │
            ├─────────┤ ├────────┤ ├──────────────┤
            │ HTML/CSS│ │ 浏览器 │ │ 代码审查(初审)│
            │  JS开发 │ │ 页面截图│ │ 视觉验收(初审)│
            │ 找图采图│ │ GUI操作│ │ 知识库管理    │
            │ 素材生成│ │ 连通测试│ │ 规则维护归档  │
            │ 文件操作│ │ 数据抓取│ │ 备份          │
            │ 单元测试│ │ 表单填写│ │ 第二意见      │
            └────┬────┘ └────┬───┘ └──────┬───────┘
                 │           │            │
                 └───────────┼────────────┘
                             │
                    所有互动写入
                             │
                             ▼
              ┌──────────────────────────┐
              │     ledger.jsonl         │
              │  事件账本（唯一真相源）    │
              └──────────┬───────────────┘
                         │
                    tail -f 实时
                         │
                         ▼
                    米迦勒（全貌可视）
```

---

## 二、核心变革：v5 → v6

| v5 | v6 |
|----|----|
| 串行分派：玛门 → 等 → 路西法 → 等 → 撒旦 | **并行分派**：三者同时 exec_command |
| 信息通过我中转 | **事件账本 ledger.jsonl** 旁路直通 |
| 兄弟之间不互知 | 兄弟之间的互动全写账本，我随时可见 |
| 瓶颈在我 | 我只做决策和终审，不做转发 |
| 子 agent 方案（曾讨论） | **放弃**。纯扁平，0 额外层级 |

---

## 三、事件账本协议

### 路径

```
~/.openclaw/workspace/coordination/ledger.jsonl
```

### 格式

每条一行 JSON：

```json
{"from":"mammon","to":"lucifer","event":"done","file":"index.html","ts":"2026-06-27T14:30:00"}
{"from":"lucifer","to":"mammon","event":"ack","eta":"2min","ts":"2026-06-27T14:30:05"}
{"from":"lucifer","to":"mammon","event":"review_done","result":"pass","issues":0,"ts":"2026-06-27T14:32:10"}
{"from":"satan","to":"michael","event":"screenshot_done","url":"https://...","ts":"2026-06-27T14:35:00"}
```

### 事件类型

| event | 含义 | 必填字段 |
|-------|------|---------|
| `task_start` | 接到任务开始执行 | from, to, task |
| `done` | 完成任务 | from, to, file/result |
| `ack` | 确认收到任务 | from, to, eta |
| `review_done` | 审查完成 | from, to, result, issues |
| `blocked` | 卡死/受阻 | from, to, reason |
| `timeout` | 超时自动记录 | from, reason |
| `screenshot_done` | 截图完成 | from, to, url |

### 监控方式

```bash
# 我随时执行，看全貌
tail -f ~/.openclaw/workspace/coordination/ledger.jsonl

# 检查谁超过 10 分钟没动静
# （按 ts 字段判断）
```

---

## 四、并行分派协议

### 分派方式

所有兄弟在同一个 tool call 轮次同时发出：

```bash
# 同时执行，不串行等
exec_command → claude -p "玛门任务..." &
exec_command → opencli browser ... &
exec_command → hermes -c ... -z "路西法任务..." &
```

### 分派规则

- 任务不依赖 → 同时派
- 任务有依赖 → 在派单指令中写明"等 X done 事件后再动手"
- 每个兄弟的派单指令最后必须加：`完成后写入 ledger.jsonl: {"from":"<名字>","event":"done",...}`

### 我的工作模式

```
轮次 1：同时派三人 → 各自后台跑
轮次 2：tail -f ledger.jsonl → 看谁完成了 → 收集产物
轮次 3：终审 → 部署 → 汇报老板
```

我不再"等玛门完派路西法"，而是"先全派出去，看谁先回来收谁的"。

---

## 五、超时与自愈（v5 三层保留，增强）

| 监控方式 | v5 | v6 |
|----------|----|----|
| 怎么知道兄弟卡死 | 10 分钟无响应 → 手动查询 | **ledger.jsonl 最后 ts > 10 分钟 = 自动发现** |
| 怎么知道路西法没审 | 10 分钟不等了 | **账本上 mammon→done 后 10 分钟内无 lucifer→ack = 卡死** |
| 自愈三层 | 自助 → 互助 → 留痕 | **同左，但第一层从账本自动触发，不需手动查** |

---

## 六、各角色职责（不变）

与 v5 完全相同。变的只是：
- 分派方式：串行 → 并行
- 可见性：经我中转 → 账本旁路

---

## 七、品牌与设计参数（不变）

- 品牌层级：金线 #C9A96E > KALIS > TORIK
- 色盘：#000 / #FFF / #C9A96E / #888
- 字体：Montserrat（标题/数字 weight 200）、Inter（正文 300）
- 图片：免版权（Unsplash/Pexels）、禁外国人脸、脱敏

---

## 八、部署（不变）

- 路径：`/Users/zuo/kalistorik-site/`
- 命令：`npx wrangler pages deploy . --project-name=kalistorik --branch=master`
- 验证：curl HTTP 200 → 撒旦截图 → 路西法视觉比对 → 我终审

---

## 九、常用命令速查

```bash
# 分派玛门
claude -p "你是玛门。任务：[...]。完成后写 ledger: {\"from\":\"mammon\",\"event\":\"done\",\"file\":\"...\",\"ts\":\"$(date -u +%Y-%m-%dT%H:%M:%S)\"}"

# 分派路西法
hermes -c <session> -z "你是路西法。审查：[...]。完成后写 ledger"

# 分派撒旦
opencli browser <action> <target>

# 监控账本
tail -f ~/.openclaw/workspace/coordination/ledger.jsonl

# 部署
cd /Users/zuo/kalistorik-site && npx wrangler pages deploy . --project-name=kalistorik --branch=master
```

---

**v6 终版。扁平化。并行化。全透明。即日生效。**
