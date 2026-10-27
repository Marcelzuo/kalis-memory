# Site Backup v6.6 (2026-10-27)

Source repo: `Marcelzuo/kalistorik-site`
Source commit: `b765cff`

## Scope
This snapshot contains the full site code/config except `images/` (unchanged, see `backups/site/site-20260914-2224/images`), `docs/`, `.git`, `.wrangler`, and `node_modules`.

## Changes since v6.5 (site-20261027-v6.5-blog-eudr-shipping-cookie)
- feat: remove WhatsApp contact channels (`5787cd0`)
- fix: redirect removed WhatsApp routes to contact (`b765cff`)

## Removed
- `wa.html` (WhatsApp landing page) deleted
- WhatsApp nav icon, footer icon, contact section card, form field, and i18n keys removed across home + 6 language mirrors
- WhatsApp references removed from 4 service pages, 8 blog pages, 404, sitemap, llms.txt, llms-full.txt, and contact API payload/email

## Contact strategy
- Email is now the primary channel: `hello@kalistorik.com`
- Old `/wa` and `/wa.html` now 301 to `/en/#contact`

## Verification
- `rg` for `whatsapp|wa.me|wa_business|contact_whatsapp|social_wa|api.whatsapp` in site code: 0 hits (only internal `ledger.md` history remains)
- 17 affected HTML pages: headless Chrome 0 JS console errors, tag balance OK, JSON-LD valid, `sitemap.xml` well-formed
- Live: `/`, `/en/`, `/blog/`, `/factories.html`, `/quality.html` HTTP 200; production HTML contains no WhatsApp strings; `/wa` and `/wa.html` return 301 to `/en/#contact`
