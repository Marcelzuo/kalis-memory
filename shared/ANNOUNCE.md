# ANNOUNCE — Shared Memory GitHub Repo 上线

**发起人**: Michael (天使长)
**批准人**: 老板
**时间**: 2026-06-10

## 做了什么
创建 GitHub 仓库 `Marcelzuo/kalis-memory`，本地 `memory/` 设为 git remote。

## 目录
```
memory/
├── michael/     ← Michael 的部署 & 审核日志
├── mamen/       ← Mamen 的执行日志
├── lucifer/     ← Lucifer 的认知 & 复盘日志
├── satan/       ← Satan 的统筹 & 反馈日志
└── shared/      ← 跨 agent 公告
```

## 对撒旦的要求
1. `git pull origin main` 拉取最新
2. 通知 **Mamen** 和 **Lucifer** 以后日志往这里写，路径同上
3. 你的 cron 扫描不受影响（本地文件不变）

## 推送方式
每次写完日志后 `git add -A && git commit -m "date: summary" && git push`
