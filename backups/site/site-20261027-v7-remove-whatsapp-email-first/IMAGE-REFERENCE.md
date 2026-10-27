# 图片参考 — 权威路径与方法

> 2026-06-23 | 撒旦整理。图片出问题先看本文，不要到处试。

## 一、目录结构

```
images/
├── beds/           # 23 产品,  350 图
├── sofas/          # 22 产品,  842 图
├── sofa-beds/      # 52 产品, 1911 图
├── tables/         # 25 产品,   84 图
├── chairs/         #  9 产品,   84 图
└── factories/      #  3 图 (factories.html 引用)
assets/
└── factories-modal/ # 3 webp (index.html why-section modal)
```

**规则：**
- 主图命名：`{产品系列}/{前缀}-{系列号}01.webp`（如 `1600G/WS-16001.webp`）
- 细节图命名：同一目录下 `{前缀}-{系列号}02.webp` 起递增
- 产品系列名含 `#` 的（如 `12302#`），目录名用 `-` 替代 `#`（如 `12302-/`）
- 图片格式：统一 `.webp`

## 二、图片引用方式

### index.html — 产品数据（唯一权威源）
```
var __PRODS__ = { "beds": [{ "series": "1600G", "main_image": "images/beds/1600G/WS-16001.webp", "detail_images": ["images/beds/1600G/WS-16002.webp", ...] }] }
```
- 131 产品，3271 引用
- 所有路径相对于站点根目录
- `data-details` 使用 `encodeURIComponent(JSON.stringify(...))` 编码，读取时 `decodeURIComponent` 解码

### factories.html — 工厂图
```
src="/images/factories/bed-workshop.jpg"
```
- 3 张工厂车间图，直接 `<img>` 引用

### assets/ — 弹窗图
```
src="assets/factories-modal/bed.webp"
```
- why-section V4 modal 的 3 张工厂展示图

## 三、部署与验证

### 部署方式
- Git push master → GitHub Actions → `wrangler pages deploy . --project-name=kalistorik --branch=master`
- 部署整个仓库目录到 Cloudflare Pages
- 自定义域名：`kalistorik.com` → CF Pages（DNS 橙色代理）

### 验证步骤（按顺序）
1. `git ls-files images/ | wc -l` → 应为 3274
2. `curl -sI "https://kalistorik.com/images/beds/1600G/WS-16001.webp"` → 200
3. 抽样：每类产品取首/中/尾各 1 主图 + 2 细节图 → 全 200
4. `diff <(curl -sL "https://kalistorik.com/") index.html` → 一致
5. 浏览器硬刷新（Cmd+Shift+R）后点开产品 → 细节缩略图应全部显示

### 图片出问题排查顺序
1. **本地文件** → `git ls-files images/` 确认未被误删
2. **git 状态** → 确认未提交的图片已 push
3. **线上可达** → `curl -sI` 逐个查 HTTP 状态码
4. **CDN 缓存** → 加 `Cache-Control: no-cache`（已有 `_headers`）
5. **浏览器缓存** → 硬刷新 Cmd+Shift+R

## 四、红线

- ❌ `images/` 目录结构不可随意改动
- ❌ 产品系列目录名与 `__PRODS__` 路径必须一致
- ❌ 不要用 `%23` 编码 `#`（CF Pages 不解码）→ 用 `-` 替代
- ❌ 不要改 `assets/` 和 `images/` 之外的图片引用方式
- ❌ 不要动 `.github/workflows/deploy.yml` 的部署命令

## 五、当前数据

| 类别 | 产品数 | 图片数 |
|---|---|---|
| beds | 23 | 350 |
| sofas | 22 | 842 |
| sofa-beds | 52 | 1911 |
| tables | 25 | 84 |
| chairs | 9 | 84 |
| factories | — | 3 |
| assets | — | 3 |
| **合计** | **131** | **3277** |
