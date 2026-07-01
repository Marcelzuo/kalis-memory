# KALIS TORIK V6 Release Notes
2026-07-01

## Commits
02016ce fix: add Sofa Beds+Chairs options to contact form select
a6be427 fix: add Sofa Beds+Chairs to contact form Product dropdown
3313299 fix: unify picks.html i18n key names with index.html
4f57a39 fix: add JS drivers for quality-modal and promo-drawer
f4fd4da fix: picks.html __LANGS__ scope var→window
86dc516 fix: remove 48 dead __LANGS__ keys from removed components
6528b96 fix: remove .logo-light dead CSS
4783cb5 fix: wa.html hreflang add missing fr/de/it/es/pt
3dd55b9 fix: picks.html hreflang use distinct ?lang=XX URLs
8e809ef revert: remove FAQ QA items, keep title+desc
28b6246 fix: canonical/hreflang chain, schema price=0, empty src, CSS dead code, FAQ content, EN inq_success

## Fixed
- 404→200 catch-all
- pages.dev→.com redirect
- Contact form lowercase fields
- Canonical/hreflang chain fix
- Schema price=0 removed
- Modal i18n 6 languages
- Empty src→about:blank
- CSS dead code cleanup
- EN inq_success fix
- picks.html hreflang ?lang=XX
- wa.html hreflang 6 languages
- .logo-light dead CSS removed
- 48 dead __LANGS__ keys removed
- picks.html __LANGS__ scope fix
- quality/promo modal JS drivers
- picks.html i18n key unification
- Product dropdown 3→5 categories
