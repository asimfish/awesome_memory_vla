#!/usr/bin/env python3
"""Draw assets/timeline.svg: one dot per paper by submission month, coloured by taxonomy group,
with the three core papers labelled. Pure-Python SVG, no plotting dependency."""
import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
man = json.load(open(os.path.join(HERE, "papers_manifest.json"), encoding="utf-8"))
tax = json.load(open(os.path.join(HERE, "taxonomy.json"), encoding="utf-8"))

COLORS = {
    "core": "#d62728", "survey": "#7f7f7f", "bench": "#8c564b", "event": "#ff7f0e",
    "dense": "#1f77b4", "latent": "#2ca02c", "agentic": "#9467bd", "world": "#17becf",
    "multi": "#e377c2", "background": "#bcbd22",
}
groups = sorted(tax.keys(), key=lambda g: tax[g]["order"])

# month index from 2024-01 to 2026-09
def midx(d):
    y, m = int(d[:4]), int(d[5:7])
    return (y - 2024) * 12 + (m - 1)

START, END = midx("2024-01"), midx("2026-09")
W, H = 1400, 470
L, R, T, B = 70, 30, 40, 110
plot_w = W - L - R
x_of = lambda i: L + (i - START) / (END - START) * plot_w

cols = defaultdict(list)
for x in man:
    cols[midx(x["published"])].append(x)

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif">',
       f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
       f'<text x="{L}" y="24" font-size="17" font-weight="700" fill="#222">Memory for VLA / visuomotor policies: {len(man)} papers by arXiv submission month (colour = family)</text>']
base_y = H - B
svg.append(f'<line x1="{L}" y1="{base_y}" x2="{W-R}" y2="{base_y}" stroke="#333" stroke-width="1.2"/>')
for i in range(START, END + 1):
    y, m = 2024 + i // 12, i % 12 + 1
    xx = x_of(i)
    if m in (1, 4, 7, 10):
        svg.append(f'<line x1="{xx:.1f}" y1="{base_y}" x2="{xx:.1f}" y2="{base_y+6}" stroke="#333"/>')
        svg.append(f'<text x="{xx:.1f}" y="{base_y+20}" font-size="11" text-anchor="middle" fill="#333">{y}-{m:02d}</text>')
    else:
        svg.append(f'<line x1="{xx:.1f}" y1="{base_y}" x2="{xx:.1f}" y2="{base_y+3}" stroke="#999"/>')
    n = len(cols.get(i, []))
    if n:
        svg.append(f'<text x="{xx:.1f}" y="{base_y-8 - n*13 - 4}" font-size="10" text-anchor="middle" fill="#666">{n}</text>')

r = 5.2
order = {g: k for k, g in enumerate(groups)}
for i, papers in cols.items():
    papers = sorted(papers, key=lambda p: (order[p["group"]], p["published"]))
    xx = x_of(i)
    for k, p in enumerate(papers):
        yy = base_y - 8 - k * 13 - r
        c = COLORS[p["group"]]
        title = p["title"].replace("&", "&amp;").replace("<", "&lt;")
        svg.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="{r}" fill="{c}" stroke="#fff" stroke-width="1"><title>{p["key"]}: {title} ({p["arxiv"]})</title></circle>')
        if p["group"] == "core":
            # label to the left of the June-2026 column, one row per core paper
            row = {"TRACE": 0, "SAI": 1, "EventVLA": 2}[p["key"]]
            tx, ty = xx - 60, base_y - 300 + row * 16
            svg.append(f'<line x1="{xx-r:.1f}" y1="{yy:.1f}" x2="{tx+4:.1f}" y2="{ty-4:.1f}" stroke="{c}" stroke-width="1" stroke-dasharray="3,2"/>')
            svg.append(f'<text x="{tx:.1f}" y="{ty:.1f}" font-size="12" font-weight="700" text-anchor="end" fill="{c}">{p["key"]} ({p["published"][5:]})</text>')

# legend, two rows
lx, ly = L, H - 44
for k, g in enumerate(groups):
    if k == 5:
        lx, ly = L, H - 22
    label = tax[g]["title_en"].split(":")[0]
    svg.append(f'<circle cx="{lx+6}" cy="{ly}" r="5" fill="{COLORS[g]}"/>')
    svg.append(f'<text x="{lx+16}" y="{ly+4}" font-size="11" fill="#333">{label}</text>')
    lx += 16 + 6.3 * len(label) + 26
svg.append("</svg>")
os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
open(os.path.join(ROOT, "assets", "timeline.svg"), "w", encoding="utf-8").write("\n".join(svg))
print("wrote assets/timeline.svg")
