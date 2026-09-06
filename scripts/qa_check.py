#!/usr/bin/env python3
"""Repository QA: every text file decodes as UTF-8, no seed placeholders remain, and every
relative Markdown link / image resolves to an existing file. Exit code 1 on any failure."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXT_EXT = {".md", ".json", ".html", ".tex", ".py", ".sh", ".bib", ".tsv", ".svg", ".txt"}
SKIP_DIRS = {".git", "translations", "__pycache__"}
problems = []
n_files = n_links = 0
link_re = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for fn in filenames:
        p = os.path.join(dirpath, fn)
        ext = os.path.splitext(fn)[1]
        if ext not in TEXT_EXT:
            continue
        n_files += 1
        raw = open(p, "rb").read()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            problems.append("NOT UTF-8: %s (%s)" % (os.path.relpath(p, ROOT), e))
            continue
        if "@@BODY@@" in text and fn not in ("qa_check.py", "seed_utf8.sh"):
            problems.append("PLACEHOLDER LEFT: %s" % os.path.relpath(p, ROOT))
        if ext == ".md":
            for m in link_re.finditer(text):
                target = m.group(1)
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                target = target.split("#")[0]
                if not target:
                    continue
                n_links += 1
                full = os.path.normpath(os.path.join(dirpath, target))
                if not os.path.exists(full):
                    problems.append("BROKEN LINK in %s -> %s" % (os.path.relpath(p, ROOT), target))

print("checked %d text files, %d relative links" % (n_files, n_links))
if problems:
    for x in problems:
        print(x)
    sys.exit(1)
print("QA OK")
