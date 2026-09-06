#!/usr/bin/env python3
"""Markdown -> styled HTML -> PDF via headless Chrome. CJK-safe, KaTeX math."""
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional

import markdown

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
:root { --ink:#1a202e; --muted:#5a6478; --accent:#1a56db; --line:#d9dee8; --bg-soft:#f4f6fa; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", sans-serif;
  color: var(--ink); font-size: 10.5pt; line-height: 1.75; margin: 0; }
main { max-width: 100%; }
h1 { font-size: 21pt; line-height: 1.3; border-bottom: 3px solid var(--accent);
  padding-bottom: 10px; margin: 0 0 14px; letter-spacing: .01em; }
h2 { font-size: 14.5pt; margin: 26px 0 10px; padding-left: 10px;
  border-left: 4px solid var(--accent); line-height: 1.35; break-after: avoid; }
h3 { font-size: 12pt; margin: 18px 0 8px; break-after: avoid; }
p { margin: 7px 0; text-align: justify; }
a { color: var(--accent); text-decoration: none; }
strong { color: #0f1420; }
blockquote { margin: 10px 0; padding: 8px 14px; background: var(--bg-soft);
  border-left: 4px solid #9db3dd; color: var(--muted); font-size: 9.5pt; border-radius: 0 6px 6px 0; }
blockquote p { margin: 3px 0; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 9pt; line-height: 1.55; }
th { background: #eef2f9; color: #223; text-align: left; font-weight: 600; }
th, td { border: 1px solid var(--line); padding: 5px 8px; vertical-align: top; }
tr:nth-child(even) td { background: #fafbfd; }
tr { break-inside: avoid; }
code { font-family: "SF Mono", Menlo, "Heiti SC", monospace; font-size: .88em;
  background: var(--bg-soft); padding: 1px 4px; border-radius: 4px; }
pre { background: #0f1420; color: #e6ecf7; padding: 12px 14px; border-radius: 8px;
  overflow-x: hidden; white-space: pre-wrap; font-size: 8.5pt; line-height: 1.5; }
pre code { background: none; color: inherit; padding: 0; }
ul, ol { margin: 7px 0; padding-left: 22px; }
li { margin: 3px 0; }
hr { border: none; border-top: 1px solid var(--line); margin: 20px 0; }
.katex { font-size: 1.02em; }
.katex-display { margin: 10px 0; }
@page { size: A4; margin: 18mm 16mm 20mm; }
h1, h2, h3 { page-break-after: avoid; }
table, pre { page-break-inside: auto; }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="utf-8">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
 onload="renderMathInElement(document.body,{{delimiters:[{{left:'$$',right:'$$',display:true}},{{left:'$',right:'$',display:false}}]}});"></script>
<style>{css}</style></head>
<body><main>{body}</main></body></html>
"""


def _front_matter(text: str):
    """Turn a YAML front-matter block (title/subtitle/date) into a Markdown title block."""
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        return text, ""
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    head = ""
    if meta.get("title"):
        head += "# " + meta["title"] + "\n\n"
    if meta.get("subtitle"):
        head += "*" + meta["subtitle"] + "*\n\n"
    if meta.get("date"):
        head += meta["date"] + "\n\n"
    return head + text[m.end():], meta.get("title", "")


def build(md_path: Path, pdf_path: Path, html_path: Optional[Path] = None) -> None:
    text = md_path.read_text(encoding="utf-8")
    text, fm_title = _front_matter(text)
    # consecutive "> " lines are one paragraph in Markdown; keep them on separate lines
    lines = text.split("\n")
    for i in range(len(lines) - 1):
        if lines[i].startswith("> ") and lines[i + 1].startswith("> ") and not lines[i].endswith("  "):
            lines[i] = lines[i] + "  "
    text = "\n".join(lines)
    # Protect $$...$$ and $...$ from markdown mangling (esp. _ inside math)
    stash: list[str] = []

    def _stash(m: re.Match) -> str:
        stash.append(m.group(0))
        return f"\x02MATH{len(stash) - 1}\x03"

    text = re.sub(r"\$\$.*?\$\$", _stash, text, flags=re.S)
    text = re.sub(r"(?<![\\$])\$(?!\s)([^$\n]+?)(?<!\s)\$(?!\d)", _stash, text)

    html = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists", "smarty"])
    for i, chunk in enumerate(stash):
        html = html.replace(f"\x02MATH{i}\x03", chunk)

    title = re.search(r"^# (.+)$", text, re.M)
    doc = TEMPLATE.format(title=(title.group(1) if title else (fm_title or md_path.stem)), css=CSS, body=html)

    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(doc)
        tmp = f.name
    if html_path is not None:
        html_path.parent.mkdir(parents=True, exist_ok=True)
        html_path.write_text(doc, encoding="utf-8")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", "--virtual-time-budget=8000", f"file://{tmp}"],
        check=True, capture_output=True, timeout=600,
    )
    print(f"OK {pdf_path}")


if __name__ == "__main__":
    build(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]) if len(sys.argv) > 3 else None)
