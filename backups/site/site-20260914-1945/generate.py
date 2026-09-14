#!/usr/bin/env python3
"""生成 6 语言静态镜像页。从 V6.1 index.html 复制，只做字符串替换。"""
import os

BASE = '/Users/zuo/kalistorik-site'
LANGS = ['en','fr','de','it','es','pt']
OG_LOCALE = {'en':'en_US','fr':'fr_FR','de':'de_DE','it':'it_IT','es':'es_ES','pt':'pt_PT'}

with open(f'{BASE}/index.html') as f:
    original = f.read()

for lang in LANGS:
    html = original
    
    # 1. <html lang="xx">
    html = html.replace('<html lang="en">', f'<html lang="{lang}">')
    
    # 2. <base href="/"> after <meta charset>
    html = html.replace(
        '<meta charset="UTF-8">',
        '<meta charset="UTF-8">\n<base href="/">'
    )
    
    # 3. Force language
    html = html.replace("setLang(sl||'en')", f"setLang('{lang}')")
    
    # 4. Language-SPECIFIC replacements FIRST (before hreflang sweep)
    # Canonical
    html = html.replace(
        '<link rel="canonical" href="https://kalistorik.com/?lang=en">',
        f'<link rel="canonical" href="https://kalistorik.com/{lang}/">'
    )
    # og:url
    html = html.replace(
        '<meta property="og:url" content="https://kalistorik.com/?lang=en">',
        f'<meta property="og:url" content="https://kalistorik.com/{lang}/">'
    )
    # og:locale
    html = html.replace(
        '<meta property="og:locale" content="en_US">',
        f'<meta property="og:locale" content="{OG_LOCALE[lang]}">'
    )
    
    # 5. NOW update all hreflang hrefs: /?lang=XX → /XX/
    for l in LANGS:
        html = html.replace(f'href="https://kalistorik.com/?lang={l}"', f'href="https://kalistorik.com/{l}/"')
    
    # Remove og:locale:alternate tags (redundant)
    import re
    html = re.sub(r'<meta property="og:locale:alternate"[^>]*>\n?', '', html)
    
    # Write
    os.makedirs(f'{BASE}/{lang}', exist_ok=True)
    out = f'{BASE}/{lang}/index.html'
    with open(out, 'w') as f:
        f.write(html)
    print(f'✅ {lang}/index.html  ({len(html)} bytes)')

print(f'\nDone. 6 pages generated.')
