#!/usr/bin/env python3
"""Generate notes/<key>_<arxiv>.md for every paper in the manifest.

Each note = metadata + hand-written Chinese one-line positioning (scripts/oneliners_cn.json)
+ original abstract + links to repo assets and to the core deep dives of the same family.
Core papers get a short note that points at their full reports.
All non-ASCII UI strings live in scripts/strings_cn.json (this script stays ASCII-only because the
editor's Write tool is not UTF-8 safe on this machine).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
man = json.load(open(os.path.join(HERE, "papers_manifest.json"), encoding="utf-8"))
ol = json.load(open(os.path.join(HERE, "oneliners_cn.json"), encoding="utf-8"))
tax = json.load(open(os.path.join(HERE, "taxonomy.json"), encoding="utf-8"))
S = json.load(open(os.path.join(HERE, "strings_cn.json"), encoding="utf-8"))

CORE_REPORT = {
    "EventVLA": ("reports/01_eventvla_cn.md", "reports/01_eventvla_en.md"),
    "TRACE": ("reports/02_trace_cn.md", "reports/02_trace_en.md"),
    "SAI": ("reports/03_sai_cn.md", "reports/03_sai_en.md"),
}
FAMILY_CORE = {
    "event": ["EventVLA"], "dense": ["EventVLA"], "bench": ["EventVLA", "TRACE"],
    "latent": ["TRACE"], "agentic": ["EventVLA", "TRACE"], "world": ["EventVLA"],
    "multi": ["SAI"], "survey": ["EventVLA", "TRACE", "SAI"], "background": ["TRACE", "SAI"],
}

os.makedirs(os.path.join(ROOT, "notes"), exist_ok=True)
n = kept = 0
HANDWRITTEN = "<!-- handwritten -->"
for x in man:
    key, aid = x["key"], x["arxiv"]
    path = os.path.join(ROOT, x["note"])
    authors = ", ".join(x["authors"])
    links = ["[arXiv](https://arxiv.org/abs/%s)" % aid, "[PDF](https://arxiv.org/pdf/%s)" % aid]
    if os.path.exists(os.path.join(ROOT, x["pdf"])):
        links.append("[%s](../%s)" % (S["repo_pdf"], x["pdf"]))
    if os.path.exists(os.path.join(ROOT, x["zh"])):
        links.append("[%s](../%s)" % (S["zh_pdf"], x["zh"]))
    sep = " " + S["dot"] + " "
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            text = f.read()
        if text.startswith(HANDWRITTEN):
            # keep the hand-written body, refresh only the asset-link line of the metadata block
            new_lines = []
            for line in text.split("\n"):
                if line.startswith("> [arXiv](https://arxiv.org/abs/"):
                    line = "> " + sep.join(links)
                new_lines.append(line)
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(new_lines))
            kept += 1
            continue
    lines = ["# " + x["title"], ""]
    venue = x["venue"] or ("arXiv " + x["published"][:4])
    lines.append("> **arXiv %s**%s%s%s%s %s%s%s `%s` / %s" % (
        aid, sep, venue, sep, S["submitted"], x["published"], sep, S["family"], x["group"], tax[x["group"]]["title_cn"]))
    lines.append("> *%s*" % authors)
    lines.append("> " + sep.join(links))
    lines.append("")
    lines.append("## " + S["one_line"])
    lines.append("")
    lines.append(ol.get(key, ""))
    lines.append("")
    if key in CORE_REPORT:
        cn, en = CORE_REPORT[key]
        lines.append(S["core_pointer"] % (S["core_name"][key], cn, en))
        lines.append("")
    else:
        rel = FAMILY_CORE.get(x["group"], [])
        if rel:
            refs = S["list_sep"].join("[%s](../%s)" % (S["core_name"][c], CORE_REPORT[c][0]) for c in rel)
            lines.append("## " + S["relation"])
            lines.append("")
            lines.append(S["relation_body"] % (tax[x["group"]]["title_cn"], refs))
            lines.append("")
    lines.append("## " + S["abstract"])
    lines.append("")
    lines.append(x["abstract"])
    lines.append("")
    if x.get("comment"):
        lines.append("*arXiv comment: %s*" % x["comment"])
        lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    n += 1
print("wrote %d notes, kept %d handwritten notes" % (n, kept))
