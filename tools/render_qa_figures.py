# -*- coding: utf-8 -*-
"""Supplementary quality-assessment graphics for the replication package.

Reads data/03_quality_assessment_scores.csv and data/04_quality_assessment_questions.csv
and renders three figures. No value is recomputed or reinterpreted: cells are shown
exactly as coded (Yes / Part. / No), and the one cell recorded as an em dash is drawn
as "not scored" rather than folded into No.

Palette: the documented blue ramp, ordinal steps #86b6ef -> #2a78d6 -> #104281,
validated with validate_palette.js --ordinal (all four checks pass).
"""
import csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
SRC = os.environ.get("PKG", _ROOT + "/")
OUT = os.environ.get("OUTDIR", os.path.join(_ROOT, "docs", "figures") + os.sep)
os.makedirs(OUT, exist_ok=True)

SURFACE, INK, INK2, MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#7a7975"
GRID = "#e8e7e3"
RAMP = {"No": "#86b6ef", "Part.": "#2a78d6", "Yes": "#104281"}
UNSCORED = "#dedcd6"
SERIES1 = "#2a78d6"
ORDER = ["No", "Part.", "Yes"]

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans", "Segoe UI", "Helvetica", "Arial"],
    "axes.linewidth": 0.8,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
    "svg.hashsalt": "iomt-hybrid-ids-slr",   # deterministic element ids
})

# SVG metadata carries a timestamp by default, which would make every rebuild differ
SVGMETA = {"Date": None}

rows = [r for r in csv.DictReader(open(SRC + "data/03_quality_assessment_scores.csv",
                                       encoding="utf-8-sig"))
        if r["ID"].strip().startswith("R")]
ITEMS = ["QA%d" % i for i in range(1, 11)]
SHORT = {
    "QA1": "Architecture described",     "QA2": "Unsup. + sup. combined",
    "QA3": "IoMT-relevant dataset",      "QA4": "Standard metrics reported",
    "QA5": "Beyond one benchmark",       "QA6": "Limitations discussed",
    "QA7": "Zero-day / unknown attacks", "QA8": "Explainability mechanism",
    "QA9": "Per-device profiling",       "QA10": "Adaptive thresholds / drift",
}
CORE = {"QA1", "QA2", "QA3", "QA4"}


def finish(ax):
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0, colors=INK2, labelsize=8.5)


def px(ax, n_px, axis="y"):
    """n pixels expressed in data units on the given axis (limits must be set)."""
    inv = ax.transData.inverted()
    o = inv.transform((0, 0))
    p = inv.transform((n_px, n_px))
    return abs(p[0] - o[0]) if axis == "x" else abs(p[1] - o[1])


def rcol(ax, x, y0, y1, w_data, color, r_px=4):
    """Column: square at the baseline, 4px rounded at the data end."""
    from matplotlib.path import Path
    import matplotlib.patches as mp
    r = min(px(ax, r_px, "x"), w_data / 2)
    ry = min(px(ax, r_px, "y"), abs(y1 - y0))
    x0, x1 = x - w_data / 2, x + w_data / 2
    v = [(x0, y0), (x0, y1 - ry), (x0, y1), (x0 + r, y1),
         (x1 - r, y1), (x1, y1), (x1, y1 - ry), (x1, y0), (x0, y0)]
    c = [Path.MOVETO, Path.LINETO, Path.CURVE3, Path.CURVE3,
         Path.LINETO, Path.CURVE3, Path.CURVE3, Path.LINETO, Path.CLOSEPOLY]
    ax.add_patch(mp.PathPatch(Path(v, c), facecolor=color, linewidth=0, zorder=3))


def legend_handles(include_unscored=True):
    h = [Rectangle((0, 0), 1, 1, facecolor=RAMP[k], linewidth=0) for k in ORDER]
    lab = ["No (0)", "Partial (0.5)", "Yes (1)"]
    if include_unscored:
        h.append(Rectangle((0, 0), 1, 1, facecolor=UNSCORED, linewidth=0))
        lab.append("not scored")
    return h, lab


# ---------------------------------------------------------------- Fig A: heatmap
srt = sorted(rows, key=lambda r: (-float(r["Total"]), r["ID"]))
n = len(srt)
fig = plt.figure(figsize=(7.8, 9.4), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax = fig.add_axes([0.150, 0.050, 0.585, 0.868])
ax.set_facecolor(SURFACE)
GAP = 0.055
for yi, r in enumerate(srt):
    for xi, it in enumerate(ITEMS):
        c = RAMP.get(r[it].strip(), UNSCORED)
        ax.add_patch(Rectangle((xi + GAP, yi + GAP), 1 - 2 * GAP, 1 - 2 * GAP,
                               linewidth=0, facecolor=c))
ax.set_xlim(0, len(ITEMS))
ax.set_ylim(n, 0)
ax.set_xticks([i + .5 for i in range(len(ITEMS))])
ax.set_xticklabels([(i + "\u2009\u2022" if i in CORE else i) for i in ITEMS], fontsize=8.5)
ax.xaxis.set_ticks_position("top")
ax.set_yticks([i + .5 for i in range(n)])
ax.set_yticklabels([r["ID"] for r in srt], fontsize=7.4, fontfamily="monospace")
finish(ax)
for yi, r in enumerate(srt):
    ax.text(len(ITEMS) + 0.42, yi + .5, "%.1f" % float(r["Total"]),
            va="center", ha="left", fontsize=7.4, color=INK2)
ax.text(len(ITEMS) + 0.42, -0.62, "total", va="center", ha="left", fontsize=8, color=MUTED)
fig.text(0.150, 0.985, "Quality assessment, all 34 included studies",
         fontsize=13.5, color=INK, va="top")
fig.text(0.150, 0.958, "One row per study, ordered by total score. "
         "\u2022 marks the four core items gated at 2.0.",
         fontsize=9, color=INK2, va="top")
h, lab = legend_handles()
ax.legend(h, lab, loc="upper left", bbox_to_anchor=(1.155, 1.0), frameon=False,
          fontsize=8.5, labelcolor=INK2, handlelength=1.1, handleheight=1.1)
fig.savefig(OUT + "qa_heatmap.png", facecolor=SURFACE)
fig.savefig(OUT + "qa_heatmap.svg", facecolor=SURFACE, metadata=SVGMETA)
plt.close(fig)

# ------------------------------------------------- Fig B: per-item share, stacked
counts = {it: {k: 0 for k in ORDER} for it in ITEMS}
unscored = {it: 0 for it in ITEMS}
for r in rows:
    for it in ITEMS:
        v = r[it].strip()
        if v in counts[it]:
            counts[it][v] += 1
        else:
            unscored[it] += 1
order_items = sorted(ITEMS, key=lambda it: -(counts[it]["Yes"] + .5 * counts[it]["Part."]))
N = len(rows)
fig = plt.figure(figsize=(8.6, 4.6), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax = fig.add_axes([0.255, 0.155, 0.625, 0.700])
ax.set_facecolor(SURFACE)
ax.set_xlim(0, N)
ax.set_ylim(len(order_items) - 0.5, -0.5)          # inverted; set before measuring px
BH = px(ax, 22, "y")                                # bar thickness, under the 24px cap
for yi, it in enumerate(order_items):
    x = 0.0
    for k in ORDER:
        c = counts[it][k]
        if c:
            ax.barh(yi, c, left=x, height=BH, color=RAMP[k], linewidth=0, zorder=3)
            x += c
    if unscored[it]:
        ax.barh(yi, unscored[it], left=x, height=BH, color=UNSCORED, linewidth=0, zorder=3)
    # 2px surface gaps separate touching segments
    x = 0.0
    for k in ORDER[:-1]:
        x += counts[it][k]
        if 0 < x < N:
            ax.plot([x, x], [yi - BH / 2, yi + BH / 2], color=SURFACE, linewidth=2, zorder=4)
    ax.text(N + 0.6, yi, "%d" % counts[it]["Yes"], va="center", ha="left",
            fontsize=8.5, color=INK2)
ax.set_yticks(range(len(order_items)))
ax.set_yticklabels([SHORT[i] for i in order_items], fontsize=9)
ax.set_xticks([0, 10, 20, 30, N])
ax.set_xticklabels(["0", "10", "20", "30", "34"], fontsize=8.5)
finish(ax)
ax.text(N + 0.6, -0.95, "Yes", fontsize=8, color=MUTED, va="center", ha="left")
fig.text(0.045, 0.975, "Which quality criteria the corpus meets", fontsize=13.5,
         color=INK, va="top")
fig.text(0.045, 0.925, "Studies per item, ordered by how well the corpus scores. N = 34.",
         fontsize=9, color=INK2, va="top")
h, lab = legend_handles()
ax.legend(h, lab, loc="lower center", bbox_to_anchor=(0.5, -0.255), ncol=4,
          frameon=False, fontsize=8.5, labelcolor=INK2, handlelength=1.1, handleheight=1.1)
fig.savefig(OUT + "qa_items.png", facecolor=SURFACE)
fig.savefig(OUT + "qa_items.svg", facecolor=SURFACE, metadata=SVGMETA)
plt.close(fig)

# --------------------------------------------- Fig C: distribution of total scores
tot = [float(r["Total"]) for r in rows]
bins = {}
for t in tot:
    bins[t] = bins.get(t, 0) + 1
xs = sorted(bins)
ymax = max(bins.values())
fig = plt.figure(figsize=(8.6, 3.6), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax = fig.add_axes([0.070, 0.170, 0.895, 0.590])
ax.set_facecolor(SURFACE)
ax.set_xlim(min(xs) - .55, max(xs) + .55)
ax.set_ylim(0, ymax + 1.6)                          # headroom for the mean annotation
BW = px(ax, 24, "x")                                # column thickness at the cap
for g in range(2, ymax + 1, 2):
    ax.axhline(g, color=GRID, linewidth=0.8, zorder=1)
for x in xs:
    rcol(ax, x, 0, bins[x], BW, SERIES1)
    ax.text(x, bins[x] + 0.20, "%d" % bins[x], ha="center", va="bottom",
            fontsize=8.5, color=INK2)
mean = sum(tot) / len(tot)
ax.plot([mean, mean], [0, ymax + 1.05], color=INK, linewidth=1.0, zorder=5)
ax.text(mean + 0.10, ymax + 1.05, "mean %.2f" % mean, fontsize=8.5, color=INK,
        va="top", ha="left")
ax.set_xticks(xs)
ax.set_xticklabels(["%.1f" % x for x in xs], fontsize=8.5)
ax.set_yticks(range(0, ymax + 1, 2))
finish(ax)
fig.text(0.070, 0.972, "Distribution of total quality scores", fontsize=13.5,
         color=INK, va="top")
fig.text(0.070, 0.900, "Studies per total score out of 10. The paper reports only the "
         "mean, median and range.", fontsize=9, color=INK2, va="top")
fig.savefig(OUT + "qa_totals.png", facecolor=SURFACE)
fig.savefig(OUT + "qa_totals.svg", facecolor=SURFACE, metadata=SVGMETA)
plt.close(fig)

print("wrote to", os.path.abspath(OUT))
for f in sorted(os.listdir(OUT)):
    print("  %-18s %8d bytes" % (f, os.path.getsize(OUT + f)))
tally = {k: sum(counts[it][k] for it in ITEMS) for k in ORDER}
print("checksum: %d studies x 10 = %d cells | %s | unscored %d | sum %d"
      % (len(rows), len(rows) * 10, tally, sum(unscored.values()),
         sum(tally.values()) + sum(unscored.values())))
