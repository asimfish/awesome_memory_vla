#!/usr/bin/env python3
"""Convert assets/timeline.svg to assets/timeline.svg.pdf with headless Chrome (keeps the sans-serif
fonts that MuPDF's SVG renderer replaces with a serif fallback). Page size follows the SVG viewBox."""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT = Path(__file__).resolve().parent.parent
svg_path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "assets" / "timeline.svg"
pdf_path = Path(sys.argv[2]) if len(sys.argv) > 2 else svg_path.with_suffix(".svg.pdf")
svg = svg_path.read_text(encoding="utf-8")
m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
w, h = int(m.group(1)), int(m.group(2))
html = ("<!DOCTYPE html><html><head><meta charset='utf-8'><style>@page{size:%dpx %dpx;margin:0}"
        "html,body{margin:0;padding:0}svg{display:block}</style></head><body>%s</body></html>") % (w, h, svg)
with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
    f.write(html)
    tmp = f.name
subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                "--print-to-pdf=%s" % pdf_path, "--virtual-time-budget=3000", "file://%s" % tmp],
               check=True, capture_output=True, timeout=120)
print("OK", pdf_path)
