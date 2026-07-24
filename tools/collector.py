#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════╗
║  米迦勒团队 · 信息采集系统 v2              ║
║  15 个直连源，不依赖搜索引擎                 ║
╚══════════════════════════════════════════════╝

用法:
  python3 collector.py scan <领域>     frontend / browser / review / all
  python3 collector.py source <源名>   单源拉取
  python3 collector.py custom <关键词> 自定义搜索
  python3 collector.py list           列出所有源
"""
import urllib.request, json, re, html as HTML, sys
from concurrent.futures import ThreadPoolExecutor, as_completed

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}
TIMEOUT = 12

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        resp = urllib.request.urlopen(req, timeout=TIMEOUT)
        return resp.read().decode("utf-8", errors="replace")
    except:
        return None

def item(title, url="", summary="", score="", source="", domain=""):
    return {"title": str(title)[:150], "url": str(url)[:200], "summary": str(summary)[:200], "score": str(score), "source": source, "domain": domain}

# ═══════════════════════════════════════════════
#  信息源
# ═══════════════════════════════════════════════

def src_hackernews():
    body = fetch("https://hacker-news.firebaseio.com/v0/topstories.json")
    if not body: return []
    ids = json.loads(body)[:10]
    items = []
    for hid in ids:
        d = json.loads(fetch(f"https://hacker-news.firebaseio.com/v0/item/{hid}.json") or "{}")
        items.append(item(d.get("title",""), d.get("url", f"https://news.ycombinator.com/item?id={hid}"),
            "", f"{d.get('score',0)}pts/{d.get('descendants',0)}💬", "HackerNews", "tech"))
    return items

def src_github():
    body = fetch("https://github.com/trending")
    if not body: return []
    repos = re.findall(r'<h2[^>]*class="[^"]*h3[^"]*"[^>]*>.*?<a[^>]*href="(/[^"]+)"[^>]*>(.*?)</a>.*?</h2>.*?<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', body, re.DOTALL)
    items = []
    for path, name, desc in repos[:10]:
        name = re.sub(r'<[^>]+>', '', name).strip().replace('\n',' ').replace('  ','')
        desc = re.sub(r'<[^>]+>', '', desc).strip()[:150]
        items.append(item(name, f"https://github.com{path}", desc, "⭐ trending", "GitHub", "tech"))
    return items

def src_devto():
    body = fetch("https://dev.to/api/articles?per_page=10")
    if not body: return []
    items = []
    for a in json.loads(body)[:10]:
        items.append(item(a.get("title",""), a.get("url",""), a.get("description","")[:150],
            f"{a.get('positive_reactions_count',0)}❤️", "Dev.to", "tech"))
    return items

def src_v2ex():
    body = fetch("https://www.v2ex.com/api/topics/hot.json")
    if not body: return []
    items = []
    for t in json.loads(body)[:10]:
        items.append(item(t.get("title",""), f"https://v2ex.com/t/{t['id']}",
            f"节点:{t.get('node',{}).get('title','')}", f"{t.get('replies',0)}回", "V2EX", "cn_tech"))
    return items

def src_juejin():
    body = fetch("https://api.juejin.cn/content_api/v1/content/article_rank?category_id=1&type=hot&size=10")
    if not body: return []
    items = []
    for d in json.loads(body).get("data", [])[:10]:
        c = d.get("content", {})
        info = c.get("article_info", {})
        items.append(item(info.get("title",""), f"https://juejin.cn/post/{info.get('article_id','')}",
            info.get("brief_content","")[:150], f"{info.get('digg_count',0)}赞", "掘金", "cn_tech"))
    return items

def src_npm():
    body = fetch("https://api.npmjs.org/downloads/point/last-week/react,vue,angular,svelte,preact,solid-js,qwik,astro,next,nuxt")
    if not body: return []
    data = json.loads(body)
    items = []
    for pkg, info in sorted(data.items(), key=lambda x: -x[1].get("downloads",0)):
        items.append(item(f"{pkg} {info.get('downloads',0):,}周下载", f"https://www.npmjs.com/package/{pkg}",
            "", f"📦{info.get('downloads',0):,}", "NPM", "frontend"))
    return items

def src_producthunt():
    body = fetch("https://www.producthunt.com/")
    if not body: return []
    ld = re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', body, re.DOTALL)
    items, seen = [], set()
    for block in ld:
        try:
            data = json.loads(block)
            for d in (data if isinstance(data, list) else [data]):
                if d.get("@type") == "Product" and d.get("name") not in seen:
                    seen.add(d["name"])
                    items.append(item(d.get("name",""), d.get("url",""), d.get("description","")[:150], "🚀 PH", "ProductHunt", "product"))
        except: pass
    return items[:8]

def src_huggingface():
    """HuggingFace 每日 AI 论文"""
    body = fetch("https://huggingface.co/api/daily_papers?limit=8")
    if not body: return []
    items = []
    for p in json.loads(body)[:8]:
        paper = p.get("paper", {})
        items.append(item(paper.get("title",""), f"https://huggingface.co/papers/{paper.get('id','')}",
            paper.get("summary","")[:200].replace("\n"," "), f"👍{p.get('upvotes',0)}", "HuggingFace", "ai"))
    return items

def src_arxiv():
    """arXiv CS.AI 最新论文"""
    body = fetch("https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&max_results=8")
    if not body: return []
    entries = re.findall(r'<entry>(.*?)</entry>', body, re.DOTALL)
    items = []
    for e in entries[:8]:
        title = re.search(r'<title[^>]*>(.*?)</title>', e).group(1).strip()
        link = re.search(r'<id[^>]*>(.*?)</id>', e).group(1).strip()
        summary = re.search(r'<summary[^>]*>(.*?)</summary>', e).group(1).strip()[:200]
        published = re.search(r'<published[^>]*>(.*?)</published>', e).group(1)[:10]
        items.append(item(title, link, summary, published, "arXiv", "ai"))
    return items

def src_stackoverflow():
    """StackOverflow JS 热门问题"""
    body = fetch("https://api.stackexchange.com/2.3/questions?order=desc&sort=hot&tagged=javascript&site=stackoverflow&pagesize=8")
    if not body: return []
    items = []
    for q in json.loads(body).get("items", [])[:8]:
        items.append(item(q["title"], q["link"], "", f"👍{q['score']} | {q['answer_count']}答", "StackOverflow", "tech"))
    return items

def src_ruanyifeng():
    """阮一峰的网络日志"""
    body = fetch("https://www.ruanyifeng.com/blog/atom.xml")
    if not body: return []
    entries = re.findall(r'<entry>(.*?)</entry>', body, re.DOTALL)
    items = []
    for e in entries[:6]:
        title = re.search(r'<title[^>]*>(.*?)</title>', e).group(1).strip()
        link = re.search(r'<link[^>]*href="([^"]+)"', e).group(1).strip()
        updated = re.search(r'<updated[^>]*>(.*?)</updated>', e).group(1)[:10]
        items.append(item(title, link, "", updated, "阮一峰", "cn_tech"))
    return items

def src_caniuse():
    """Can I Use 浏览器兼容性更新"""
    body = fetch("https://caniuse.com/feed.php")
    if not body: return []
    # feed.php returns an HTML page with latest update info
    title_m = re.search(r'<title>(.*?)</title>', body)
    h3_m = re.search(r'<h3[^>]*>(.*?)</h3>', body)
    update = title_m.group(1).strip() if title_m else (h3_m.group(1).strip() if h3_m else "")
    items = [item(update, "https://caniuse.com/feed.php", "浏览器兼容性最新变更", "", "CanIUse", "frontend")]
    return items

def src_nvd():
    """NVD 最新 CVE 漏洞"""
    body = fetch("https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=6&pubStartDate=2026-06-01T00:00:00.000&pubEndDate=2026-07-31T23:59:59.000")
    if not body: return []
    items = []
    for v in json.loads(body).get("vulnerabilities", [])[:6]:
        cve = v.get("cve", {})
        cid = cve.get("id", "")
        desc = (cve.get("descriptions", [{}])[0].get("value", "")[:200])
        score = cve.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseScore", "?")
        items.append(item(cid, f"https://nvd.nist.gov/vuln/detail/{cid}", desc, f"CVSS {score}", "NVD", "security"))
    return items

def src_crates():
    """Crates.io Rust 热门库"""
    body = fetch("https://crates.io/api/v1/crates?per_page=8&sort=recent-downloads")
    if not body: return []
    items = []
    for c in json.loads(body).get("crates", [])[:8]:
        items.append(item(f"{c['name']} v{c.get('max_stable_version','?')}", f"https://crates.io/crates/{c['name']}",
            c.get("description","")[:150], f"📦{c.get('recent_downloads',0):,}", "Crates.io", "rust"))
    return items


def src_sejournal():
    """Search Engine Journal — SEO 行业动态"""
    body = fetch("https://www.searchenginejournal.com/feed/")
    if not body: return []
    items = []
    for m in re.findall(r"<item>(.*?)</item>", body, re.DOTALL)[:6]:
        t = re.search(r"<title>(.*?)</title>", m)
        l = re.search(r"<link>(.*?)</link>", m)
        d = re.search(r"<pubDate>(.*?)</pubDate>", m)
        items.append(item(t.group(1) if t else "", l.group(1) if l else "",
            "", d.group(1)[:16] if d else "", "SEJournal", "seo"))
    return items

def src_ahrefs():
    """Ahrefs Blog — SEO/营销"""
    body = fetch("https://ahrefs.com/blog/feed/")
    if not body: return []
    items = []
    for m in re.findall(r"<item>(.*?)</item>", body, re.DOTALL)[:6]:
        t = re.search(r"<title>(.*?)</title>", m)
        l = re.search(r"<link>(.*?)</link>", m)
        items.append(item(t.group(1) if t else "", l.group(1) if l else "",
            "", "", "Ahrefs", "seo"))
    return items

def src_buffer():
    """Buffer Blog — 社媒运营"""
    body = fetch("https://buffer.com/resources/feed/")
    if not body: return []
    items = []
    for m in re.findall(r"<item>(.*?)</item>", body, re.DOTALL)[:6]:
        t = re.search(r"<title>(.*?)</title>", m)
        l = re.search(r"<link>(.*?)</link>", m)
        items.append(item(t.group(1) if t else "", l.group(1) if l else "",
            "", "", "Buffer", "social"))
    return items

def src_supplychain():
    """Supply Chain Dive — 供应链/外贸"""
    body = fetch("https://www.supplychaindive.com/feeds/news/")
    if not body: return []
    items = []
    for m in re.findall(r"<item>(.*?)</item>", body, re.DOTALL)[:6]:
        t = re.search(r"<title>(.*?)</title>", m)
        l = re.search(r"<link>(.*?)</link>", m)
        s = re.search(r"<description>(.*?)</description>", m)
        items.append(item(t.group(1) if t else "", l.group(1) if l else "",
            (s.group(1)[:150] if s else ""), "", "SupplyChain", "trade"))
    return items




def src_custom(keyword, n=8):
    try:
        from ddgs import DDGS
        results = list(DDGS().text(keyword, max_results=n))
        return [item(r["title"], r["href"], r["body"][:200], "", "Search", "custom") for r in results]
    except ImportError:
        return [item("ddgs not installed", "", "pip3 install ddgs", "", "Error", "")]

# ═══════════════════════════════════════════════
#  领域预设
# ═══════════════════════════════════════════════

SOURCES = {
    "hackernews":    (src_hackernews,    "HackerNews 头条"),
    "github":        (src_github,        "GitHub Trending"),
    "devto":         (src_devto,         "Dev.to 热门"),
    "v2ex":          (src_v2ex,          "V2EX 热帖"),
    "juejin":        (src_juejin,        "掘金热榜"),
    "npm":           (src_npm,           "NPM 下载量"),
    "producthunt":   (src_producthunt,   "ProductHunt 新品"),
    "huggingface":   (src_huggingface,   "HF 每日论文"),
    "arxiv":         (src_arxiv,         "arXiv CS.AI"),
    "stackoverflow": (src_stackoverflow, "StackOverflow 热门"),
    "ruanyifeng":    (src_ruanyifeng,    "阮一峰周刊"),
    "caniuse":       (src_caniuse,       "Can I Use 更新"),
    "nvd":           (src_nvd,           "NVD 漏洞"),
    "crates":        (src_crates,        "Crates.io Rust"),
    "sejournal":     (src_sejournal,     "SEJournal SEO"),
    "ahrefs":        (src_ahrefs,        "Ahrefs Blog"),
    "buffer":        (src_buffer,        "Buffer 社媒"),
    "supplychain":   (src_supplychain,   "Supply Chain Dive"),

}

DOMAINS = {
    "frontend": {
        "label": "🎨 玛门 · 前端",
        "sources": ["hackernews","github","devto","npm","juejin","v2ex","stackoverflow","caniuse","ruanyifeng","producthunt"],
        "keywords": ["CSS 2026 new features", "JavaScript framework 2026", "frontend performance 2026"],
    },
    "browser": {
        "label": "🖥️ 撒旦 · 浏览器/自动化",
        "sources": ["hackernews","github","devto","v2ex","stackoverflow","producthunt","crates"],
        "keywords": ["Playwright 2026", "browser automation", "Chrome DevTools Protocol", "web scraping"],
    },
    "business": {
        "label": "💼 老板 · 商业情报",
        "sources": ["sejournal","ahrefs","buffer","supplychain","hackernews","v2ex"],
        "keywords": [
            "B2B social media marketing 2026",
            "Instagram new features update 2026",
            "Google SEO algorithm update July 2026",
            "supply chain international trade news 2026",
            "LinkedIn content strategy personal brand B2B",
            "Kalistorik TORIK",
        ],
    },
    "review": {
        "label": "📋 路西法 · 审查/知识/AI",
        "sources": ["hackernews","devto","v2ex","juejin","arxiv","huggingface","nvd","ruanyifeng"],
        "keywords": ["code review agent 2026", "static analysis tool", "LLM knowledge base", "AI paper 2026"],
    },
}

# ═══════════════════════════════════════════════
#  引擎
# ═══════════════════════════════════════════════

def collect_domain(name):
    if name not in DOMAINS:
        print(f"未知: {name}. 可用: {list(DOMAINS.keys())}")
        return
    cfg = DOMAINS[name]
    print(f"\n{'='*60}\n  {cfg['label']}\n{'='*60}\n")
    all_items = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {}
        for s in cfg["sources"]:
            if s in SOURCES:
                futures[ex.submit(SOURCES[s][0])] = s
        for f in as_completed(futures):
            s = futures[f]
            try:
                items = f.result()
                print(f"  📡 {SOURCES[s][1]}: {len(items)}条")
                all_items.extend(items)
            except Exception as e:
                print(f"  ❌ {s}: {e}")
    for kw in cfg.get("keywords", []):
        items = src_custom(kw, 3)
        print(f"  🔍 「{kw}」: {len(items)}条")
        all_items.extend(items)
    print(f"\n  📊 总计 {len(all_items)} 条\n")
    by_src = {}
    for it in all_items:
        by_src.setdefault(it["source"], []).append(it)
    n = 1
    for src, items in by_src.items():
        print(f"── {src} ──")
        for it in items:
            print(f"  {n}. [{it['title'][:90]}]")
            if it["url"]: print(f"     {it['url'][:130]}")
            if it["summary"]: print(f"     {it['summary'][:150]}")
            if it["score"]: print(f"     {it['score']}")
            n += 1
            print()

def collect_source(name):
    if name not in SOURCES:
        print(f"未知源: {name}\n可用: {', '.join(SOURCES.keys())}")
        return
    items = SOURCES[name][0]()
    print(f"\n── {SOURCES[name][1]} ({len(items)}条) ──\n")
    for i, it in enumerate(items, 1):
        print(f"  {i}. [{it['title'][:90]}]")
        if it["url"]: print(f"     {it['url'][:130]}")
        if it["summary"]: print(f"     {it['summary'][:150]}")
        if it["score"]: print(f"     {it['score']}")
        print()

def collect_custom(kw):
    items = src_custom(kw, 10)
    print(f"\n── 「{kw}」({len(items)}条) ──\n")
    for i, it in enumerate(items, 1):
        print(f"  {i}. [{it['title'][:90]}]")
        print(f"     {it['url'][:130]}")
        if it["summary"]: print(f"     {it['summary'][:200]}")
        print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "scan":
        d = sys.argv[2] if len(sys.argv) > 2 else "all"
        for k in (DOMAINS if d == "all" else [d]):
            collect_domain(k)
    elif cmd == "source":
        collect_source(sys.argv[2]) if len(sys.argv) > 2 else print("用法: collector.py source <源名>")
    elif cmd == "custom":
        collect_custom(sys.argv[2]) if len(sys.argv) > 2 else print("用法: collector.py custom <关键词>")
    elif cmd == "list":
        print("源:", ", ".join(SOURCES.keys()))
        print("领域:", ", ".join(DOMAINS.keys()))
        for d, c in DOMAINS.items():
            print(f"  {d}: {c['sources']}")
    else:
        print(f"未知: {cmd}")
        print(__doc__)
