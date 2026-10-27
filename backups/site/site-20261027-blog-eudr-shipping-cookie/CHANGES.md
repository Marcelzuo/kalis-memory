# Site Backup 2026-10-27

Source repo: `Marcelzuo/kalistorik-site`
Source commit: `7898d45`

## Scope
This snapshot contains the full site code/config except `images/` (unchanged, see `backups/site/site-20260914-2224/images`), `.git`, `.wrangler`, and `node_modules`.

## Changes since last full backup (20260914-2224)
- feat: add GA4 consent mode and link click tracking (`4f0a9d7`)
- feat: add EUDR and shipping blog posts (`cbddd4e`)
- feat: add cookie banner to service pages (`7898d45`)

## New pages
- `blog/post-eudr-wooden-furniture.html`
- `blog/post-shipping-furniture-china-to-europe.html`

## Updated files
- `blog/index.html`
- `sitemap.xml`
- `factories.html`
- `quality.html`
- `freight.html`
- `picks.html`

## Verification
- Local Chrome headless: homepage, blog index, 2 new posts, 4 service pages all HTTP 200; 0 JS console errors.
- Live `kalistorik.com`: 10 key URLs all HTTP 200.
- canonical, Article/FAQPage JSON-LD, internal links, sitemap, 6-language cookie i18n verified.
