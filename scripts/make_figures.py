#!/usr/bin/env python3
"""Draw the two overview figures as SVG (light version for README, dark version for the slides):
  assets/fig1_timeline.svg      one swim-lane per family, one dot per paper by arXiv month, stars for the core papers
  assets/fig2_taxonomy.svg      taxonomy tree: root -> 10 families (with counts) -> 26 sub-classes with example papers
Data: scripts/papers_manifest.json + scripts/fig_text.json (labels). ASCII-only script.
Also writes assets/timeline.svg (alias of fig1 light) for backward compatibility and PDFs via svg2pdf.py."""
import json
import os
import subprocess
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
man = json.load(open(os.path.join(HERE, "papers_manifest.json"), encoding="utf-8"))
tax = json.load(open(os.path.join(HERE, "taxonomy.json"), encoding="utf-8"))
T = json.load(open(os.path.join(HERE, "fig_text.json"), encoding="utf-8"))
groups = sorted(tax.keys(), key=lambda g: tax[g]["order"])
COLORS = {"core": "#d62728", "survey": "#7f7f7f", "bench": "#8c564b", "event": "#ff7f0e", "dense": "#1f77b4",
          "latent": "#2ca02c", "agentic": "#9467bd", "world": "#17becf", "multi": "#e377c2", "background": "#bcbd22"}
FONT = "PingFang SC, Hiragino Sans GB, Helvetica Neue, Helvetica, Arial, sans-serif"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def theme(dark):
    return {"bg": "#0b1220" if dark else "#ffffff", "ink": "#e8eefb" if dark else "#1a202e",
            "muted": "#93a3c0" if dark else "#5a6478", "line": "#2e405f" if dark else "#d9dee8",
            "lane": "#111b2e" if dark else "#f4f6fa", "band": "rgba(251,191,36,0.18)" if dark else "rgba(255,159,64,0.18)"}


def midx(d):
    return (int(d[:4]) - 2024) * 12 + int(d[5:7]) - 1


def fig1(dark):
    th = theme(dark)
    START, END = midx("2024-01"), midx("2026-09")
    W, H = 1500, 640
    L, R, TOP, B = 230, 40, 70, 70
    lane_h = (H - TOP - B) / len(groups)
    x_of = lambda i: L + (i - START) / (END - START) * (W - L - R)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">',
         f'<rect width="{W}" height="{H}" fill="{th["bg"]}"/>',
         f'<text x="{L}" y="30" font-size="17" font-weight="700" fill="{th["ink"]}">{esc(T["fig1_title"])}</text>',
         f'<text x="{L}" y="50" font-size="12" fill="{th["muted"]}">{esc(T["fig1_title_en"])}</text>']
    # convergence band (June 2026)
    xb0, xb1 = x_of(midx("2026-06")) - 9, x_of(midx("2026-06")) + 9
    o.append(f'<rect x="{xb0:.1f}" y="{TOP}" width="{xb1-xb0:.1f}" height="{H-TOP-B}" fill="{th["band"]}"/>')
    o.append(f'<text x="{(xb0+xb1)/2:.1f}" y="{TOP-8}" font-size="11" text-anchor="middle" fill="#d97706" font-weight="600">2026-06</text>')
    for k, g in enumerate(groups):
        y0 = TOP + k * lane_h
        if k % 2 == 0:
            o.append(f'<rect x="{L}" y="{y0:.1f}" width="{W-L-R}" height="{lane_h:.1f}" fill="{th["lane"]}"/>')
        n = sum(1 for x in man if x["group"] == g)
        o.append(f'<text x="{L-12}" y="{y0+lane_h/2+4:.1f}" font-size="12.5" text-anchor="end" fill="{th["ink"]}">{esc(T["lanes"][g])} <tspan fill="{th["muted"]}">({n})</tspan></text>')
        o.append(f'<circle cx="{L-222}" cy="{y0+lane_h/2:.1f}" r="5" fill="{COLORS[g]}"/>')
    # month axis
    ax_y = H - B + 4
    o.append(f'<line x1="{L}" y1="{ax_y}" x2="{W-R}" y2="{ax_y}" stroke="{th["muted"]}" stroke-width="1"/>')
    for i in range(START, END + 1):
        y, m = 2024 + i // 12, i % 12 + 1
        xx = x_of(i)
        if m in (1, 4, 7, 10):
            o.append(f'<line x1="{xx:.1f}" y1="{ax_y}" x2="{xx:.1f}" y2="{ax_y+6}" stroke="{th["muted"]}"/>')
            o.append(f'<text x="{xx:.1f}" y="{ax_y+20}" font-size="11" text-anchor="middle" fill="{th["muted"]}">{y}-{m:02d}</text>')
        else:
            o.append(f'<line x1="{xx:.1f}" y1="{ax_y}" x2="{xx:.1f}" y2="{ax_y+3}" stroke="{th["line"]}"/>')
    # dots: stack within a lane-month, spreading vertically
    cell = defaultdict(list)
    for x in man:
        cell[(x["group"], midx(x["published"]))].append(x)
    for (g, i), papers in cell.items():
        k = groups.index(g)
        yc = TOP + k * lane_h + lane_h / 2
        xx = x_of(i)
        n = len(papers)
        for j, p in enumerate(sorted(papers, key=lambda p: p["published"])):
            off = (j - (n - 1) / 2) * 9.5
            yy = yc + off
            title = esc(p["title"])
            if g == "core":
                o.append(f'<text x="{xx:.1f}" y="{yy+5:.1f}" font-size="15" text-anchor="middle" fill="{COLORS[g]}"><title>{p["key"]}: {title}</title>&#9733;</text>')
            else:
                o.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="4.3" fill="{COLORS[g]}" stroke="{th["bg"]}" stroke-width="0.8"><title>{p["key"]}: {title} ({p["arxiv"]})</title></circle>')
    # label the three core papers to the right of the star
    core = sorted([x for x in man if x["group"] == "core"], key=lambda x: x["published"])
    yc = TOP + lane_h / 2
    for j, p in enumerate(core):
        xx = x_of(midx(p["published"]))
        ty = yc - 12 + j * 14
        o.append(f'<text x="{xx+16:.1f}" y="{ty:.1f}" font-size="11.5" font-weight="700" fill="{COLORS["core"]}">{p["key"]} ({p["published"][5:]})</text>')
    o.append("</svg>")
    return "\n".join(o)


def fig2(dark):
    th = theme(dark)
    W = 1500
    rows = []  # (group, leaf_label, examples)
    for g in groups:
        for leaf in T["leaves"][g]:
            rows.append((g, leaf[0], leaf[1]))
    row_h = 21
    H = 90 + len(rows) * row_h + 6 * len(groups) + 40
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">',
         f'<rect width="{W}" height="{H}" fill="{th["bg"]}"/>',
         f'<text x="40" y="30" font-size="17" font-weight="700" fill="{th["ink"]}">{esc(T["fig2_title"])}</text>',
         f'<text x="40" y="50" font-size="12" fill="{th["muted"]}">{esc(T["fig2_title_en"])}</text>']
    x_root, x_grp, x_leaf, x_ex = 60, 330, 640, 1010
    top = 80
    y = top
    group_spans = []
    for g in groups:
        leaves = [r for r in rows if r[0] == g]
        y0 = y
        for (_, label, ex) in leaves:
            yy = y + row_h / 2
            o.append(f'<line x1="{x_grp+250}" y1="{yy:.1f}" x2="{x_leaf-10}" y2="{yy:.1f}" stroke="{th["line"]}" stroke-width="1"/>')
            o.append(f'<circle cx="{x_leaf-10}" cy="{yy:.1f}" r="3" fill="{COLORS[g]}"/>')
            o.append(f'<text x="{x_leaf}" y="{yy+4.5:.1f}" font-size="12.5" fill="{th["ink"]}">{esc(label)}</text>')
            o.append(f'<text x="{x_ex}" y="{yy+4.5:.1f}" font-size="11.5" fill="{th["muted"]}">{esc(ex)}</text>')
            y += row_h
        y1 = y
        yc = (y0 + y1) / 2
        n = sum(1 for x in man if x["group"] == g)
        o.append(f'<rect x="{x_grp}" y="{yc-11:.1f}" width="250" height="22" rx="6" fill="{COLORS[g]}" opacity="0.92"/>')
        o.append(f'<text x="{x_grp+125}" y="{yc+4.5:.1f}" font-size="12.5" font-weight="700" text-anchor="middle" fill="#ffffff">{tax[g]["order"]}. {esc(T["lanes"][g])} ({n})</text>')
        # vertical connector spanning the leaves
        o.append(f'<line x1="{x_grp+250}" y1="{y0+row_h/2:.1f}" x2="{x_grp+250}" y2="{y1-row_h/2:.1f}" stroke="{th["line"]}" stroke-width="1"/>')
        group_spans.append(yc)
        y += 6
    # root
    yr = (group_spans[0] + group_spans[-1]) / 2
    o.append(f'<rect x="{x_root}" y="{yr-26:.1f}" width="200" height="52" rx="8" fill="{th["lane"]}" stroke="{th["line"]}"/>')
    for k, line in enumerate(T["root"].split("\n")):
        o.append(f'<text x="{x_root+100}" y="{yr-4+k*17:.1f}" font-size="{14 if k==0 else 11.5}" font-weight="{700 if k==0 else 400}" text-anchor="middle" fill="{th["ink"]}">{esc(line)}</text>')
    o.append(f'<line x1="{x_root+200}" y1="{yr:.1f}" x2="{x_grp-30}" y2="{yr:.1f}" stroke="{th["line"]}" stroke-width="1.2"/>')
    o.append(f'<line x1="{x_grp-30}" y1="{group_spans[0]:.1f}" x2="{x_grp-30}" y2="{group_spans[-1]:.1f}" stroke="{th["line"]}" stroke-width="1.2"/>')
    for yc in group_spans:
        o.append(f'<line x1="{x_grp-30}" y1="{yc:.1f}" x2="{x_grp}" y2="{yc:.1f}" stroke="{th["line"]}" stroke-width="1.2"/>')
    o.append("</svg>")
    return "\n".join(o)


def main():
    out = os.path.join(ROOT, "assets")
    os.makedirs(out, exist_ok=True)
    for name, fn in (("fig1_timeline", fig1), ("fig2_taxonomy", fig2)):
        for dark in (False, True):
            p = os.path.join(out, name + ("_dark" if dark else "") + ".svg")
            open(p, "w", encoding="utf-8").write(fn(dark))
            print("wrote", os.path.relpath(p, ROOT))
    # backward-compatible alias used by README and the Beamer deck
    open(os.path.join(out, "timeline.svg"), "w", encoding="utf-8").write(fig1(False))
    for svg in ("fig1_timeline.svg", "fig2_taxonomy.svg", "timeline.svg"):
        subprocess.run([sys.executable, os.path.join(HERE, "svg2pdf.py"), os.path.join(out, svg), os.path.join(out, svg + ".pdf")], check=True)


if __name__ == "__main__":
    main()
