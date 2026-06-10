# 撒旦反馈 — 2026-06-10 默认域 404

**发现时间**: 2026-06-10 14:43
**反馈人**: 撒旦（地狱三人组统筹）
**触发任务**: 老板 14:38「测试所有 WA 入口」中顺带 curl 检查部署地址

## 现象

| 域名 | 状态 |
|------|------|
| `https://kalistorik.com/`（主域） | ✅ 200 |
| `https://www.kalistorik.com/`（WWW）| ✅ 200（SSL 签发中）|
| `https://master.kalistorik.pages.dev/`（master 分支）| ✅ 200 |
| **`https://kalistorik.pages.dev/`（项目默认域）**| ❌ **404** |

## 推测原因

`wrangler pages deploy` 把构建推到了 `master` 分支名（即 preview deployment），未提升为 production。项目根域（无分支后缀）应该指向 production deployment，当前为空。

## 建议修复

```bash
# 方案 1：把当前 master 分支提升为 production
wrangler pages deployment promote --project-name=kalistorik

# 方案 2：重新部署到 main 分支（看你的默认分支名）
wrangler pages deploy ~/.openclaw/workspace/kalis/dist/ --project-name=kalistorik --branch=main
```

## 优先级

- **中等**：不影响用户访问（主域 `kalistorik.com` 正常）
- **影响**：
  - 品牌一致性（默认域 404 不专业）
  - SEO 索引（搜索引擎可能抓 `*.pages.dev`）
  - 分享链接（`pages.dev` 域比 `kalistorik.com` 弱）

## 验收

修复后请发 ping 给我，我用 curl 验证默认域 200。修复完在 `memory/2026-06-10-michael.md` 追加一段「反馈闭环」即可，我会自动巡检到。

## 边界

撒旦没有 Cloudflare 账号（按 A11 账号用完即弃），无法替你修。**修的执行必须由你完成**，撒旦负责验收。
