#!/usr/bin/env python3
"""Query the arXiv API for memory-VLA literature and print compact hits (id, date, title).

Usage: python3 scripts/arxiv_search.py "QUERY" [max_results]
Results are cached under translations/.cache_arxiv/ to stay polite to the API.
"""
import hashlib
import os
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

NS = {"a": "http://www.w3.org/2005/Atom"}
CACHE = os.path.join(os.path.dirname(__file__), "..", "translations", ".cache_arxiv")


def search(query: str, max_results: int = 50, sort: str = "submittedDate"):
    os.makedirs(CACHE, exist_ok=True)
    key = hashlib.md5(f"{query}|{max_results}|{sort}".encode()).hexdigest()
    path = os.path.join(CACHE, key + ".xml")
    if os.path.exists(path):
        data = open(path, "rb").read()
    else:
        url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"search_query": query, "start": 0, "max_results": max_results,
             "sortBy": sort, "sortOrder": "descending"})
        req = urllib.request.Request(url, headers={"User-Agent": "awesome_memory_vla/1.0 (research use)"})
        data = urllib.request.urlopen(req, timeout=60).read()
        open(path, "wb").write(data)
        time.sleep(3)
    root = ET.fromstring(data)
    hits = []
    for e in root.findall("a:entry", NS):
        aid = e.find("a:id", NS).text.rsplit("/", 1)[-1]
        title = " ".join(e.find("a:title", NS).text.split())
        pub = e.find("a:published", NS).text[:10]
        authors = [x.find("a:name", NS).text for x in e.findall("a:author", NS)]
        summ = " ".join(e.find("a:summary", NS).text.split())
        hits.append({"id": aid, "date": pub, "title": title, "authors": authors, "summary": summ})
    return hits


if __name__ == "__main__":
    q = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    for h in search(q, n):
        print(f"{h['id']:<14} {h['date']}  {h['title']}")
