#!/usr/bin/env python3
"""Generate README.md (Chinese-first) and README_en.md in the awesome-ml4co style.

Layout: title + badges + language switch; tagline; features; Content table (one anchor per
taxonomy group); one section per group with an intro paragraph and numbered entries
(**Title.** Venue. [paper] [pdf] [zh] [report] [note] / *authors*); Trends & Insights;
Deliverables; Reproduce; Contributing; Citation; License.
This script is ASCII-only; all prose lives in scripts/readme_text.json and scripts/taxonomy.json.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
man = json.load(open(os.path.join(HERE, "papers_manifest.json"), encoding="utf-8"))
tax = json.load(open(os.path.join(HERE, "taxonomy.json"), encoding="utf-8"))
TXT = json.load(open(os.path.join(HERE, "readme_text.json"), encoding="utf-8"))
CORE_REPORT = {
    "EventVLA": ("reports/01_eventvla_cn.md", "reports/01_eventvla_en.md"),
    "TRACE": ("reports/02_trace_cn.md", "reports/02_trace_en.md"),
    "SAI": ("reports/03_sai_cn.md", "reports/03_sai_en.md"),
}
groups = sorted(tax.keys(), key=lambda g: tax[g]["order"])
by_group = {g: [x for x in man if x["group"] == g] for g in groups}
for g in groups:
    by_group[g].sort(key=lambda x: x["published"], reverse=True)
# core papers keep the canonical order EventVLA, TRACE, SAI
by_group["core"].sort(key=lambda x: ["EventVLA", "TRACE", "SAI"].index(x["key"]))

TL = {"cn": {"pdf": "pdf", "zh": "\u4e2d\u8bd1", "report": "\u89e3\u8bfb", "note": "note"},
      "en": {"pdf": "pdf", "zh": "zh", "report": "report", "note": "note"}}


def slug(h):
    """GitHub-style anchor for an English heading: lowercase, drop punctuation, spaces -> hyphens."""
    import re
    s = h.lower().strip()
    s = re.sub(r"[^a-z0-9 \-]", "", s)
    return s.replace(" ", "-")


def entry(i, x, lang):
    t = TL[lang]
    venue = x["venue"] or ("arXiv " + x["published"][:4])
    links = ["[paper](https://arxiv.org/abs/%s)" % x["arxiv"]]
    if os.path.exists(os.path.join(ROOT, x["pdf"])):
        links.append("[%s](%s)" % (t["pdf"], x["pdf"]))
    if os.path.exists(os.path.join(ROOT, x["zh"])):
        links.append("[%s](%s)" % (t["zh"], x["zh"]))
    if x["key"] in CORE_REPORT:
        rep = CORE_REPORT[x["key"]][0 if lang == "cn" else 1]
        links.append("[%s](%s)" % (t["report"], rep))
    links.append("[%s](%s)" % (t["note"], x["note"]))
    title = x["title"].rstrip(".")
    if not title.endswith(("?", "!")):
        title += "."
    lines = ["%d. **%s** %s. %s" % (i, title, venue, " ".join(links)), ""]
    lines.append("    *%s*" % ", ".join(x["authors"]))
    lines.append("")
    return "\n".join(lines)


def build(lang):
    T = TXT[lang]
    o = []
    o.append("# " + T["title"])
    o.append("")
    o.append("[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    o.append("[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)")
    o.append("[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)")
    o.append("![papers](https://img.shields.io/badge/papers-%d-orange)" % len(man))
    o.append("")
    o.append("[English](README_en.md) | \u4e2d\u6587" if lang == "cn" else "English | [\u4e2d\u6587](README.md)")
    o.append("")
    o.append(T["tagline"])
    o.append("")
    o.append(T["intro"])
    o.append("")
    o.append(T["maintained"])
    o.append("")
    # deliverables table right after the intro (awesome_ICL convention)
    o.append("## " + T["deliverables_title"])
    o.append("")
    o.append(T["deliverables_head"])
    for d in T["deliverables"]:
        o.append(d)
    o.append("")
    o.append("> " + T["numbers_warning"])
    o.append("")
    o.append("## " + T["figures_title"])
    o.append("")
    o.append("![Figure 1 - Timeline](assets/fig1_timeline.svg)")
    o.append("")
    o.append(T["fig1_caption"])
    o.append("")
    o.append("![Figure 2 - Taxonomy](assets/fig2_taxonomy.svg)")
    o.append("")
    o.append(T["fig2_caption"])
    o.append("")
    o.append("## " + T["why_title"])
    o.append("")
    o.append(T["why_body"])
    o.append("")
    o.append("**%s**:" % T["features_title"])
    o.append("")
    for f in T["features"]:
        o.append("- " + f)
    o.append("")
    o.append("## [%s](#content)" % T["content"])
    o.append("")
    # headings stay English-only so GitHub anchors are identical in both READMEs
    trends_h = "%d. Trends & Insights" % (len(groups) + 1)
    deliv_h = "%d. Recommended Reading Order" % (len(groups) + 2)
    o.append("<table>")
    for g in groups:
        h = "%d. %s" % (tax[g]["order"], tax[g]["title_en"])
        label = h if lang == "en" else "%s (%s)" % (h, tax[g]["title_cn"])
        o.append('<tr><td colspan="2"><a href="#%s">%s</a></td></tr>' % (slug(h), label))
    o.append('<tr><td colspan="2"><a href="#%s">%s</a></td></tr>' % (slug(trends_h), trends_h if lang == "en" else trends_h + " (" + T["trends_title"] + ")"))
    o.append('<tr><td colspan="2"><a href="#%s">%s</a></td></tr>' % (slug(deliv_h), deliv_h if lang == "en" else deliv_h + " (" + T["reading_title"] + ")"))
    o.append("</table>")
    o.append("")
    o.append(T["legend"])
    o.append("")
    for g in groups:
        h = "%d. %s" % (tax[g]["order"], tax[g]["title_en"])
        o.append("### [%s](#content)" % h)
        o.append("")
        if lang == "cn":
            o.append("**%s** ? %s" % (tax[g]["title_cn"], tax[g]["intro_cn"]))
        else:
            o.append(tax[g]["intro_en"])
        o.append("")
        for i, x in enumerate(by_group[g], 1):
            o.append(entry(i, x, lang))
    o.append("### [%s](#content)" % trends_h)
    o.append("")
    o.append(T["trends_body"])
    o.append("")
    for i, s in enumerate(T["insights"], 1):
        o.append("%d. %s" % (i, s))
    o.append("")
    o.append("### [%s](#content)" % deliv_h)
    o.append("")
    o.append(T["reading_body"])
    o.append("")
    o.append("### " + T["repro_title"])
    o.append("")
    o.append(T["repro_body"])
    o.append("")
    o.append(T["tools"])
    o.append("")
    o.append("## " + T["contrib_title"])
    o.append("")
    o.append(T["contrib_body"])
    o.append("")
    o.append("## " + T["cite_title"])
    o.append("")
    o.append(T["cite_body"])
    o.append("")
    o.append("## License")
    o.append("")
    o.append(T["license"])
    o.append("")
    return "\n".join(o)


open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write(build("cn"))
open(os.path.join(ROOT, "README_en.md"), "w", encoding="utf-8").write(build("en"))
print("wrote README.md and README_en.md (%d papers, %d groups)" % (len(man), len(groups)))
