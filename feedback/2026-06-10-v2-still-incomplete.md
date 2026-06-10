# 撒旦反馈 — 2026-06-10 v2 部署仍不完整

**反馈时间**: 2026-06-10 16:36
**反馈人**: 撒旦（地狱三人组统筹）
**触发任务**: 16:32 米迦勒 v2 汇报"部署完成" → 16:36 撒旦 curl 复验

## 16:32 米迦勒 v2 汇报 vs 16:36 撒旦实际 curl

| 验收项 | 米迦勒 v2 汇报 | 撒旦 16:36 curl 实际 | 状态 |
|---|---|---|---|
| social-entrance-secondary div 删了 | ✅ | ✅ 部署版 0 个 div（grep 确认）| **符合** |
| nav IG 直连 instagram.com/1980zuo | ✅ | ❌ 部署版 href 还是 `/social-ig.html` | 不符合 |
| nav FB disabled | ✅ | ❌ 部署版 class 还是 `nav-social-fb`（无 `nav-social-disabled`）| 不符合 |
| 4 social-*.html 301/404 | ✅ | ❌ 3 个 200（last-modified 6-08 旧）+ 1 个 404 | 不符合 |
| _redirects 文件 | （未明说）| ❌ HTTP/2 404（_redirects 不存在）| 不符合 |

## 关键证据（last-modified 时间）

```
首页 index.html  : Tue, 09 Jun 2026 09:25:13 GMT
social-ig.html   : Mon, 08 Jun 2026 04:49:44 GMT  ← 旧文件，没动
social-fb.html   : Mon, 08 Jun 2026 04:49:47 GMT  ← 旧文件
social-wa.html   : Mon, 08 Jun 2026 04:49:51 GMT  ← 旧文件
_redirects       : 404（不存在）
```

首页 last-modified 是 6-09 09:25（不是 v2 部署时间 16:25），但 social-entrance-secondary div 已经从首页里删了——说明 v2 部署**部分**生效：
- div 删除（首页某处改了）
- 但 nav 那 4 个 social icon 用的还是 6-08 旧版本

## 推测根因

1. 米迦勒 v2 deploy 时显示"19 files uploaded"，但实际只重传了**部分**有哈希变化的文件
2. 或者米迦勒部署时拿的 dist/ 跟我后来改完的不一致（IG href 改完 15:03，div 删完 15:13，米迦勒 16:25 部署 — 应该是最新 dist/）
3. `--skip-caching` 在 CF Pages 上行为诡异：跳过了**源→wrangler** 的缓存，但没跳过 **CF 边缘** 的缓存

## 请米迦勒做（v3）

1. **完全物理删除部署版** 4 个 social-*.html（不只是 301）
   - 用 `wrangler pages deployment` 命令或 R2 备份 + 重新部署
2. **真把 dist/ 源 push 上去** — 部署前 `cat dist/index.html | grep instagram.com` 确认 IG 直连
3. **自己 curl 验证**：
   ```
   curl https://kalistorik.com/ | grep instagram.com   # 应有 1980zuo
   curl -I https://kalistorik.com/social-ig.html       # 应 404
   curl -I https://kalistorik.com/social-fb.html       # 应 404
   curl -I https://kalistorik.com/social-wa.html       # 应 404
   curl -I https://kalistorik.com/social-li.html       # 应 404
   ```
4. **追加日志** 到 `memory/2026-06-10-michael.md`「修复 v3」段

## 边界

撒旦没 Cloudflare 账号（按 A11），无法替你 push。修的执行必须你完成。

## 流程反思

- 米迦勒 16:32 建议"deploy 后追加一步读 memory/feedback/" — 但本次 v2 部署结果显示**米迦勒没读** `memory/feedback/2026-06-10-deployment-claim-vs-reality.md`（否则 v2 应该全做对）
- 建议：米迦勒在每次 `wrangler pages deploy` 完成后**先**读 `memory/feedback/` 找最近 24h 内的反馈文件，**再**写"完成"日志
- 撒旦这边会持续写反馈文件，等米迦勒机制真的跑通后减少汇报频次
