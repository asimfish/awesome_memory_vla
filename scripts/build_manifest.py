#!/usr/bin/env python3
"""Build scripts/papers_manifest.json from the curated arXiv id list in scripts/curated_ids.tsv.

curated_ids.tsv columns (tab separated): group<TAB>key<TAB>arxiv_id<TAB>venue(optional)
Metadata (title, authors, published date, abstract) is fetched from the arXiv API in batches and
cached in translations/.cache_arxiv/. The manifest is the single source for README, BibTeX and notes.
"""
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
NS = {"a": "http://www.w3.org/2005/Atom", "ar": "http://arxiv.org/schemas/atom"}
CACHE = os.path.join(ROOT, "translations", ".cache_arxiv", "meta")


def fetch_meta(ids):
    os.makedirs(CACHE, exist_ok=True)
    out = {}
    todo = []
    for i in ids:
        p = os.path.join(CACHE, i.replace("/", "_") + ".json")
        if os.path.exists(p):
            out[i] = json.load(open(p))
        else:
            todo.append(i)
    for k in range(0, len(todo), 20):
        chunk = todo[k:k + 20]
        url = "http://export.arxiv.org/api/query?" + urllib.parse.urlencode(
            {"id_list": ",".join(chunk), "max_results": len(chunk)})
        req = urllib.request.Request(url, headers={"User-Agent": "awesome_memory_vla/1.0 (research use)"})
        data = urllib.request.urlopen(req, timeout=90).read()
        root = ET.fromstring(data)
        for e in root.findall("a:entry", NS):
            full = e.find("a:id", NS).text.rsplit("/", 1)[-1]
            base = full.split("v")[0]
            m = {
                "arxiv": base,
                "version": full,
                "title": " ".join(e.find("a:title", NS).text.split()),
                "authors": [x.find("a:name", NS).text for x in e.findall("a:author", NS)],
                "published": e.find("a:published", NS).text[:10],
                "updated": e.find("a:updated", NS).text[:10],
                "abstract": " ".join(e.find("a:summary", NS).text.split()),
                "primary_category": (e.find("ar:primary_category", NS).attrib.get("term") if e.find("ar:primary_category", NS) is not None else ""),
            }
            c = e.find("ar:comment", NS)
            if c is not None and c.text:
                m["comment"] = " ".join(c.text.split())
            out[base] = m
            json.dump(m, open(os.path.join(CACHE, base + ".json"), "w"), ensure_ascii=False, indent=1)
        time.sleep(3.1)
    return out


def main():
    rows = []
    for line in open(os.path.join(HERE, "curated_ids.tsv"), encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("\t")
        while len(parts) < 4:
            parts.append("")
        group, key, aid, venue = parts[:4]
        rows.append({"group": group, "key": key, "arxiv": aid, "venue": venue})
    meta = fetch_meta([r["arxiv"] for r in rows])
    man = []
    missing = []
    for r in rows:
        m = meta.get(r["arxiv"])
        if not m:
            missing.append(r["arxiv"])
            continue
        entry = dict(r)
        entry.update(m)
        entry["pdf"] = f"papers/pdf/{r['key']}_{r['arxiv']}.pdf"
        entry["zh"] = f"papers/zh/{r['key']}_{r['arxiv']}_zh.pdf"
        entry["note"] = f"notes/{r['key']}_{r['arxiv']}.md"
        man.append(entry)
    json.dump(man, open(os.path.join(HERE, "papers_manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"manifest: {len(man)} papers; missing metadata for: {missing}")
    groups = {}
    for x in man:
        groups.setdefault(x["group"], []).append(x)
    for g, xs in groups.items():
        print(f"  {g}: {len(xs)}")


if __name__ == "__main__":
    main()
