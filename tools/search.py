#!/usr/bin/env python3
"""
米迦勒团队统一搜索工具 v2
=========================
支持渠道：
  通用: DDG (ddgs) — 覆盖中英文、新闻、技术、金融等全领域
  AI:  豆包 (doubao) / DeepSeek / Kimi / 元宝
  国内: 微信搜一搜 / B站 / 知乎 / 头条 / 百度百科
  海外: Google / DDG

用法:
  python3 search.py <渠道> <关键词> [条数]

渠道:
  text    通用文本搜索 (DDG, 中英文全覆盖)
  news    新闻搜索 (DDG)
  cn      中文搜索 (DDG)
  weixin  微信搜一搜 (公众号文章)
  bilibili B站视频搜索
  doubao  豆包 AI 搜索
  google  Google 搜索 (需浏览器)
  ddg     DDG 搜索 (需浏览器)
"""
import sys, subprocess, json
from ddgs import DDGS

def search_ddg_text(query, n=5):
    """通用文本搜索 - 覆盖中英文全领域"""
    results = list(DDGS().text(query, max_results=n))
    return [{"title": r["title"], "url": r["href"], "snippet": r["body"]} for r in results]

def search_ddg_news(query, n=5):
    """新闻搜索"""
    results = list(DDGS().news(query, max_results=n))
    return [{"title": r["title"], "url": r["url"], "source": r.get("source","")} for r in results]

def search_weixin(query, n=5):
    """微信搜一搜 - 公众号文章"""
    try:
        r = subprocess.run(
            ["opencli", "weixin", "search", query, "--format", "json"],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(r.stdout)
        items = data if isinstance(data, list) else data.get("results", [])
        return [{"title": i.get("title",""), "url": i.get("url",""), "snippet": i.get("summary",""), "date": i.get("publish_time","")} for i in items[:n]]
    except Exception as e:
        return [{"error": str(e)}]

def search_bilibili(query, n=5):
    """B站搜索"""
    try:
        r = subprocess.run(
            ["opencli", "bilibili", "search", query, "--format", "json"],
            capture_output=True, text=True, timeout=30
        )
        data = json.loads(r.stdout)
        items = data if isinstance(data, list) else data.get("results", [])
        return [{"title": i.get("title",""), "url": i.get("url",""), "author": i.get("author",""), "plays": i.get("score","")} for i in items[:n]]
    except Exception as e:
        return [{"error": str(e)}]

def search_doubao(query):
    """豆包 AI 搜索"""
    try:
        r = subprocess.run(
            ["opencli", "doubao", "ask", query, "--format", "json"],
            capture_output=True, text=True, timeout=60
        )
        data = json.loads(r.stdout)
        msgs = data if isinstance(data, list) else data.get("messages", data.get("results", []))
        return [{"role": m.get("Role",""), "text": m.get("Text","")[:500]} for m in msgs]
    except Exception as e:
        return [{"error": str(e)}]

CHANNELS = {
    "text": lambda q, n: search_ddg_text(q, n),
    "news": lambda q, n: search_ddg_news(q, n),
    "cn": lambda q, n: search_ddg_text(q, n),
    "weixin": lambda q, n: search_weixin(q, n),
    "bilibili": lambda q, n: search_bilibili(q, n),
    "doubao": lambda q, n: search_doubao(q),
}

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: search.py <渠道> <关键词> [条数]")
        print("渠道:", ", ".join(CHANNELS.keys()))
        sys.exit(1)

    channel = sys.argv[1]
    query = sys.argv[2]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 5

    if channel not in CHANNELS:
        print(f"未知渠道: {channel}. 可用: {', '.join(CHANNELS.keys())}")
        sys.exit(1)

    results = CHANNELS[channel](query, n)
    for r in results:
        title = r.get("title", r.get("role", "?"))[:120]
        url = r.get("url", "")
        snippet = r.get("snippet", r.get("text", ""))
        extra = ""
        if "source" in r: extra += f" | {r['source']}"
        if "date" in r: extra += f" | {r['date']}"
        if "author" in r: extra += f" | UP: {r['author']}"
        if "plays" in r: extra += f" | 播放: {r['plays']}"
        print(f"[{title}]{extra}")
        if url: print(f"  {url[:150]}")
        if snippet: print(f"  {snippet[:250]}")
        print()
