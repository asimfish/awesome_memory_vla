#!/usr/bin/env python3
"""Render (1) every reports/*.md to reports/pdf/*.pdf and (2) the consolidated bilingual report
report/awesome_memory_vla_report_{cn,en}.{md,html,pdf}, assembled from the trends report, the three
deep dives, the design-space matrix and the annotated paper list. Uses scripts/md2pdf.py
(Markdown -> styled HTML -> PDF via headless Chrome). ASCII-only script; prose in report_text.json.
"""
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from md2pdf import build  # noqa: E402

man = json.load(open(HERE / "papers_manifest.json", encoding="utf-8"))
tax = json.load(open(HERE / "taxonomy.json", encoding="utf-8"))
ol = json.load(open(HERE / "oneliners_cn.json", encoding="utf-8"))
RT = json.load(open(HERE / "report_text.json", encoding="utf-8"))
groups = sorted(tax.keys(), key=lambda g: tax[g]["order"])


def read(p):
    return (ROOT / p).read_text(encoding="utf-8")


def demote(md, n):
    out, in_code = [], False
    for line in md.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        if not in_code and re.match(r"^#{1,6} ", line):
            line = "#" * n + line
        out.append(line)
    return "\n".join(out)


def strip_h1(md):
    return re.sub(r"^# .*\n", "", md, count=1)


def relink(md):
    """Make repo-relative links resolve from report/ (../ prefix) and turn sibling-report links into
    plain text (they are all inside this document)."""
    md = re.sub(r"\[([^\]]+)\]\((?:0[1-4]_[a-z_]+\.md)(?:#[^)]*)?\)", r"\1", md)
    return md


def first_sentences(text, n=2):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return " ".join(parts[:n])


def paper_list(lang):
    o = []
    for g in groups:
        o.append("### %s" % (tax[g]["title_en"] if lang == "en" else "%s / %s" % (tax[g]["title_cn"], tax[g]["title_en"])))
        o.append("")
        o.append(tax[g]["intro_en" if lang == "en" else "intro_cn"])
        o.append("")
        items = sorted([x for x in man if x["group"] == g], key=lambda x: x["published"], reverse=True)
        if g == "core":
            items.sort(key=lambda x: ["EventVLA", "TRACE", "SAI"].index(x["key"]))
        for i, x in enumerate(items, 1):
            venue = x["venue"] or ("arXiv " + x["published"][:4])
            o.append("%d. **%s** (%s, arXiv [%s](https://arxiv.org/abs/%s)). *%s*" % (
                i, x["title"], venue, x["arxiv"], x["arxiv"], ", ".join(x["authors"][:8]) + (" et al." if len(x["authors"]) > 8 else "")))
            o.append("")
            body = ol.get(x["key"], "") if lang == "cn" else first_sentences(x["abstract"], 2)
            o.append("    %s" % body)
            o.append("")
    return "\n".join(o)


def consolidated(lang):
    T = RT[lang]
    sfx = lang
    trends = strip_h1(read("reports/04_trends_insights_%s.md" % sfx))
    dives = [strip_h1(read("reports/0%d_%s_%s.md" % (i, k, sfx))) for i, k in ((1, "eventvla"), (2, "trace"), (3, "sai"))]
    matrix = strip_h1(read("insights/DESIGN_SPACE_MATRIX.md"))
    o = ['---\ntitle: "%s"\nsubtitle: "%s"\ndate: %s\n---\n' % (T["title"], T["subtitle"], __import__("datetime").date.today().isoformat())]
    o.append(T["preface"] + "\n")
    o.append("## %s\n" % T["toc_title"])
    for t in T["toc"]:
        o.append("- " + t)
    o.append("\n---\n")
    o.append("# 1. %s\n" % T["ch"][0])
    o.append(demote(trends, 1))
    for n, d in enumerate(dives, 2):
        o.append("\n---\n\n# %d. %s\n" % (n, T["ch"][n - 1]))
        o.append(demote(d, 1))
    o.append("\n---\n\n# 5. %s\n" % T["ch"][4])
    o.append(demote(matrix, 1))
    o.append("\n---\n\n# 6. %s\n" % T["ch"][5])
    o.append(T["list_intro"] + "\n")
    o.append(paper_list(lang))
    o.append("\n---\n\n# %s\n" % T["appendix_title"])
    o.append(T["appendix"])
    md = "\n".join(o)
    md = relink(md)
    return md


def main():
    (ROOT / "reports" / "pdf").mkdir(parents=True, exist_ok=True)
    (ROOT / "report").mkdir(parents=True, exist_ok=True)
    only = sys.argv[1] if len(sys.argv) > 1 else "all"
    if only in ("all", "reports"):
        for md in sorted((ROOT / "reports").glob("*.md")):
            build(md, ROOT / "reports" / "pdf" / (md.stem + ".pdf"))
    if only in ("all", "consolidated"):
        for lang in ("cn", "en"):
            md_path = ROOT / "report" / ("awesome_memory_vla_report_%s.md" % lang)
            md_path.write_text(consolidated(lang), encoding="utf-8")
            build(md_path, ROOT / "report" / ("awesome_memory_vla_report_%s.pdf" % lang),
                  ROOT / "report" / ("awesome_memory_vla_report_%s.html" % lang))


if __name__ == "__main__":
    main()
