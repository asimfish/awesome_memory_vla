#!/usr/bin/env python3
"""Apply surgical layout patches to translated PDFs, as recorded in scripts/zh_patches.json.

Patch kinds:
  draw_line        -- redraw a table rule the layout engine erased (geometry copied from the original)
  overlay_original -- white-out a region and show the original English page region on top (used where
                      the engine garbled a multi-row table)
The patches are idempotent (re-applying draws the same content again). Usage: python3 scripts/apply_zh_patches.py [KEY]
"""
import json
import os
import shutil
import sys

import fitz

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
patches = json.load(open(os.path.join(HERE, "zh_patches.json"), encoding="utf-8"))
only = sys.argv[1] if len(sys.argv) > 1 else None
for key, plist in patches.items():
    if only and key != only:
        continue
    zh_path = os.path.join(ROOT, "papers", "zh", "%s_zh.pdf" % key)
    en_path = os.path.join(ROOT, "papers", "pdf", "%s.pdf" % key)
    if not os.path.exists(zh_path):
        print("skip %s (no translated PDF)" % key)
        continue
    zh = fitz.open(zh_path)
    en = fitz.open(en_path)
    for p in plist:
        page = zh.load_page(p["page"] - 1)
        if p["kind"] == "draw_line":
            (x0, y0), (x1, y1) = p["from"], p["to"]
            page.draw_line(fitz.Point(x0, y0), fitz.Point(x1, y1), color=(0, 0, 0), width=p.get("width", 0.8))
        elif p["kind"] == "overlay_original":
            rect = fitz.Rect(*p["rect"])
            # remove the garbled translated text objects (not just hide them), then show the original region
            page.add_redact_annot(rect)
            try:
                page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE, graphics=fitz.PDF_REDACT_LINE_ART_NONE)
            except TypeError:  # older PyMuPDF without the graphics argument
                page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
            page.draw_rect(rect, color=None, fill=(1, 1, 1), overlay=True)
            page.show_pdf_page(rect, en, p["page"] - 1, clip=rect)
        else:
            raise SystemExit("unknown patch kind %s" % p["kind"])
        print("%s p%d %s" % (key, p["page"], p["kind"]))
    zh.save(zh_path + ".tmp", garbage=1, deflate=True)
    zh.close()
    shutil.move(zh_path + ".tmp", zh_path)
print("done")
