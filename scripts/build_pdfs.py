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
    # sibling links inside insights/*.md (e.g. NUMBERS_LEDGER.md) must resolve from report/
    def _ins(m):
        name = m.group(1)
        if (ROOT / "insights" / name).exists():
            return "](../insights/%s%s)" % (name, m.group(2) or "")
        return m.group(0)
    md = re.sub(r"\]\(([A-Z_]+\.md)(#[^)]*)?\)", _ins, md)
    return md


def first_sentences(text, n=2):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return " ".join(parts[:n])


def inline_svg(name):
    """Return the SVG file content as a raw HTML block (works in the saved HTML and in the Chrome print)."""
    svg = (ROOT / "assets" / name).read_text(encoding="utf-8")
    # scale to the page width: drop the fixed pixel size, keep the viewBox
    svg = re.sub(r'<svg([^>]*?) width="\d+" height="\d+"', r'<svg\1 width="100%"', svg, count=1)
    return '<div style="margin:12px 0">' + svg + "</div>"


def note_body(x):
    """Full hand-written note (headings demoted) or, for generated notes, the one-liner plus abstract."""
    p = ROOT / x["note"]
    text = p.read_text(encoding="utf-8") if p.exists() else ""
    if text.startswith("<!-- handwritten -->"):
        body = re.sub(r"^<!-- handwritten -->\n", "", text)
        body = re.sub(r"^# .*\n", "", body, count=1)          # title becomes our own heading
        body = demote(body, 3)                                  # ## -> #####
        return body.strip()
    return "%s\n\n**Abstract.** %s" % (ol.get(x["key"], ""), x["abstract"])


def paper_list(lang, full=False):
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
            authors = ", ".join(x["authors"][:8]) + (" et al." if len(x["authors"]) > 8 else "")
            if full:
                o.append("#### %d. %s" % (i, x["title"]))
                o.append("")
                o.append("*%s* — %s, arXiv [%s](https://arxiv.org/abs/%s)" % (authors, venue, x["arxiv"], x["arxiv"]))
                o.append("")
                o.append(note_body(x))
                o.append("")
            else:
                o.append("%d. **%s** (%s, arXiv [%s](https://arxiv.org/abs/%s)). *%s*" % (i, x["title"], venue, x["arxiv"], x["arxiv"], authors))
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
    if lang == "cn":
        o.append("# 0. %s\n" % T["ch"][6])
        o.append(inline_svg("fig1_timeline.svg"))
        o.append("")
        o.append(inline_svg("fig2_taxonomy.svg"))
        o.append("\n---\n")
    o.append("# 1. %s\n" % T["ch"][0])
    o.append(demote(trends, 1))
    for n, d in enumerate(dives, 2):
        o.append("\n---\n\n# %d. %s\n" % (n, T["ch"][n - 1]))
        o.append(demote(d, 1))
    o.append("\n---\n\n# 5. %s\n" % T["ch"][4])
    o.append(demote(matrix, 1))
    if lang == "cn":
        o.append("\n---\n\n# 6. %s\n" % T["ch"][7])
        o.append(demote(strip_h1(read("insights/OPEN_PROBLEMS.md")), 1))
        o.append("\n---\n\n# 7. %s\n" % T["ch"][8])
        o.append(demote(strip_h1(read("insights/NUMBERS_LEDGER.md")), 1))
        o.append("\n---\n\n# 8. %s\n" % T["ch"][5])
        o.append(T["list_intro_full"] + "\n")
        o.append(paper_list(lang, full=True))
    else:
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
            stem = "survey_full_report" if lang == "cn" else "survey_full_report_en"
            md_path = ROOT / "report" / (stem + ".md")
            md_path.write_text(consolidated(lang), encoding="utf-8")
            build(md_path, ROOT / "report" / (stem + ".pdf"), ROOT / "report" / (stem + ".html"))


if __name__ == "__main__":
    main()
