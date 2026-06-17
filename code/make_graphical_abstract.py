"""
Graphical abstract – PSF-CTF paper   v5
Changes from v4:
  - All font sizes ~1.7x larger for legibility at text-width scale
  - City network icons bigger (s=55, lw=1.8, spread 2.2), 3 cities
  - Math formulas removed — plain readable text only
  - Red borders/fills -> warm amber (#E06010 / #FFF3E0)
  - Footer: light-blue background, dark ink text (no black fill)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.lines import Line2D

# Palette
B    = "#2171B5";  BL   = "#DEEBF7"   # blue   – decay / transfer
O    = "#D95F02";  OL   = "#FEE6C0"   # orange – OSM / open features
AMB  = "#E06010";  AMBL = "#FFF3E0"   # amber  – bottleneck (replaces harsh red)
G    = "#238B45"                       # green  – good match
GRY  = "#5A5A5A";  GLT  = "#F2F2F2"   # grey
INK  = "#1A1A1A"
FBKG = "#E8F4FC"                       # footer background (light blue)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size":   13,
    "axes.linewidth": 0,
})

FW, FH = 10.0, 8.2
fig = plt.figure(figsize=(FW, FH), dpi=200)
ax  = fig.add_axes([0.005, 0.005, 0.990, 0.990])
ax.set_xlim(0, 100); ax.set_ylim(0, 82)
ax.axis("off")
fig.patch.set_facecolor("white")
RNG = np.random.default_rng(42)

def box(x, y, w, h, fc, ec=INK, lw=1.6, z=2):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0,rounding_size=0.9",
        fc=fc, ec=ec, lw=lw, zorder=z))

def tx(x, y, s, sz=13, c=INK, bold=False, italic=False,
       ha="center", va="center", z=6):
    ax.text(x, y, s, fontsize=sz, color=c,
            fontweight="bold" if bold else "normal",
            style="italic" if italic else "normal",
            ha=ha, va=va, zorder=z)

def arrow(x1, y1, x2, y2, c=GRY, lw=2.0, ms=14, z=4, style="-|>"):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(
                    arrowstyle=style, color=c, lw=lw, mutation_scale=ms),
                zorder=z)

def draw_building(x, y):
    ax.add_patch(Rectangle((x - 1.4, y), 0.8, 1.2, fc="#7F8C8D", ec=INK, lw=0.6, zorder=4))
    ax.add_patch(Rectangle((x + 0.6, y), 0.8, 1.2, fc="#7F8C8D", ec=INK, lw=0.6, zorder=4))
    ax.add_patch(Rectangle((x - 0.6, y), 1.2, 2.0, fc="#2C3E50", ec=INK, lw=0.6, zorder=4))
    roof = plt.Polygon([[x - 0.6, y + 2.0], [x, y + 2.5], [x + 0.6, y + 2.0]], fc="#2C3E50", ec=INK, lw=0.6, zorder=4)
    ax.add_patch(roof)
    ax.plot([x - 0.3, x - 0.3], [y + 0.5, y + 1.0], c="white", lw=0.6, zorder=5)
    ax.plot([x + 0.3, x + 0.3], [y + 0.5, y + 1.0], c="white", lw=0.6, zorder=5)
    ax.plot([x - 0.3, x - 0.3], [y + 1.2, y + 1.7], c="white", lw=0.6, zorder=5)
    ax.plot([x + 0.3, x + 0.3], [y + 1.2, y + 1.7], c="white", lw=0.6, zorder=5)

# SECTION TITLES
tx(24,  79.5, "\u2460  Decay Calibration",         sz=15.5, bold=True, c=B)
tx(74,  79.5, "\u2461  Target-City Estimation",     sz=15.5, bold=True, c=O)

# ════════════════════════ COLUMN 1  x:2-46 ══════════════════════════════════
C1 = 2.0;  C1W = 44.0;  M1 = C1 + C1W / 2

# A. Source cities  [y:63-77, h=14]
box(C1, 63, C1W, 14, BL, ec=B, lw=2.2)
tx(M1, 74.5, "SOURCE CITIES", sz=13.5, bold=True, c=B)

city_pts = [(9.5,  70.0, "New York"),
            (24.0, 70.0, "Chicago"),
            (38.5, 70.0, "Houston")]
for (cx, cy, nm) in city_pts:
    pts = RNG.uniform(-2.2, 2.2, (5, 2))
    pts[:, 1] *= 0.45
    for i in range(5):
        for j in range(i + 1, 5):
            if RNG.uniform() < 0.55:
                ax.plot([cx + pts[i, 0], cx + pts[j, 0]],
                        [cy + pts[i, 1], cy + pts[j, 1]],
                        c=B, lw=1.8, alpha=0.38, zorder=3)
    ax.scatter(cx + pts[:, 0], cy + pts[:, 1],
               s=55, c=[B] * 5, alpha=0.80, zorder=4)
    tx(cx, cy - 2.5, nm, sz=9.5, bold=True, c=B)

arrow(M1, 62.5, M1, 61.0, c=B, lw=2.2)

# B. Aggregate distance histogram  [y:48-60, h=12]
box(C1, 48, C1W, 12, BL, ec=B, lw=2.2)
tx(M1, 57.5, "Aggregate Distance Distribution", sz=12.0, bold=True, c=B)

bars = [1.0, 0.76, 0.52, 0.34, 0.20, 0.11, 0.06]
bx0 = C1 + 11.0;  bw = 2.8;  base = 49.8
for k, bv in enumerate(bars):
    ax.add_patch(Rectangle(
        (bx0 + k * (bw + 0.38), base), bw, bv * 4.2,
        fc=B, ec="white", lw=0.4, alpha=0.88, zorder=4))
ax.annotate("", xy=(bx0 + 7 * (bw + 0.38) + 0.4, base),
            xytext=(bx0 - 0.6, base),
            arrowprops=dict(arrowstyle="->", color=GRY, lw=1.0), zorder=5)
tx(M1, 48.8, "commute distance", sz=11, c=GRY)

arrow(M1, 47.5, M1, 46.0, c=B, lw=2.2)

# C. Calibrate + decay curve  [y:33-45, h=12]
box(C1,       31, 20.0, 14, B, ec=B, lw=2.2)
tx(C1 + 10.0, 38.0, "Tanner model", sz=13.5, bold=True, c="white")

box(C1 + 21.0, 31, 22.0, 14, "white", ec=B, lw=2.2)
tx(C1 + 32.0, 43.2, "Mobility Decay", sz=12.0, bold=True, c=B)
xc = np.linspace(0, 1, 80); yc = np.exp(-3.2 * xc)
ax.plot(C1 + 25.5 + xc * 13.5, 33.5 + yc * 7.5, c=B, lw=2.8, zorder=5)
# Y-axis
ax.annotate("", xy=(C1 + 25.5, 33.5 + 8.5), xytext=(C1 + 25.5, 32.8),
            arrowprops=dict(arrowstyle="->", color=GRY, lw=0.9), zorder=5)
# X-axis
ax.annotate("", xy=(C1 + 39.5, 33.5), xytext=(C1 + 24.8, 33.5),
            arrowprops=dict(arrowstyle="->", color=GRY, lw=0.9), zorder=5)
tx(C1 + 24.2, 41.5, "f(d)", sz=10, c=GRY)
tx(C1 + 36.0, 32.2, "distance (d)", sz=10, c=GRY)

arrow(M1, 29.5, M1, 24.2, c=B, lw=2.5, ms=15)
tx(22.2, 26.8, "transferred\ndecay", sz=11, italic=True, c=B, ha="right")


# ════════════════════════ COLUMN 2  x:52-96 ═════════════════════════════════
C2 = 52.0;  C2W = 44.0;  M2 = C2 + C2W / 2

# D. Target city  [y:63-77, h=14]
box(C2, 63, C2W, 14, GLT, ec=GRY, lw=1.8)
tx(M2, 74.5, "TARGET CITY", sz=13.5, bold=True, c=GRY)
for r in range(2):
    for c in range(3):
        draw_building(C2 + 8.5 + c * 13.5, 64.2 + r * 4.5)

arrow(C2 + 14, 62.5, C2 + 11.5, 61.0, c=O,   lw=2.2)
arrow(C2 + 30, 62.5, C2 + 32.5, 61.0, c=AMB, lw=2.2)

# E. Attraction model  [y:48-60, h=12]
box(C2, 48, 20, 12, OL, ec=O, lw=2.2)
tx(C2 + 10, 57.5, "Attraction Score",   sz=11.5, bold=True, c=O)
# Map pin icon
px_att = C2 + 10.0
py_att = 52.6
ax.add_patch(plt.Circle((px_att, py_att + 1.2), 0.9, fc="#E74C3C", ec="#C0392B", lw=0.6, zorder=5))
ax.add_patch(plt.Polygon([[px_att - 0.78, py_att + 0.8], [px_att + 0.78, py_att + 0.8], [px_att, py_att]], fc="#E74C3C", ec="#C0392B", lw=0.6, zorder=5))
ax.add_patch(plt.Circle((px_att, py_att + 1.2), 0.35, fc="white", zorder=6))
tx(C2 + 10, 50.0, "Destination A", sz=11.5, c=INK)
arrow(C2 + 10, 47.5, 44.0, 23.5, c=O, lw=2.2)

# F. Outflow model  [y:48-60, h=12]  (amber = hard part)
box(C2 + 24, 48, 20, 12, AMBL, ec=AMB, lw=2.5)
tx(C2 + 34, 57.5, "Outflow Model",       sz=11.5, bold=True, c=AMB)
# Network icon
px_out = C2 + 34.0
py_out = 53.0
pts_out = [(px_out - 1.2, py_out), (px_out + 1.2, py_out), (px_out, py_out + 1.2)]
for i in range(3):
    for j in range(i + 1, 3):
        ax.plot([pts_out[i][0], pts_out[j][0]], [pts_out[i][1], pts_out[j][1]], c=GRY, lw=1.2, zorder=4)
for n_x, n_y in pts_out:
    ax.scatter(n_x, n_y, s=55, c=B, edgecolors=INK, linewidths=0.8, zorder=5)
tx(C2 + 34, 51.2, "Trip Production O",  sz=11.5, c=INK)
tx(C2 + 34, 49.5, "hard to transfer",    sz=11.5, bold=True,   c=AMB)
arrow(C2 + 34, 47.5, 56.0, 23.5, c=AMB, lw=2.2)


# ════════════════════════ ASSEMBLY BOX  x:2-96  y:10-23  h=13 ══════════════
box(2, 10, 94, 13, GLT, ec=GRY, lw=1.8)
tx(34, 20.0, "Predicted OD Matrix", sz=15, bold=True, c=INK)
tx(34, 14.5,
   r"$\mathit{flow}(i \to j) = O_i \times A_j \times f(\mathrm{distance}_{ij})$",
   sz=13.5, c=INK)

mxs = 72.5;  mys = 11.2;  nc = 5;  cs = 1.9
od  = RNG.uniform(0.15, 1.0, (nc, nc)) ** 1.4
for i in range(nc):
    for j in range(nc):
        ax.add_patch(Rectangle(
            (mxs + j * cs, mys + i * cs),
            cs * 0.87, cs * 0.87,
            fc=plt.cm.Blues(0.25 + 0.70 * od[i, j]),
            ec="white", lw=0.3, zorder=4))
ax.plot([mxs - 0.5, mxs + nc * cs - 0.5], [21.3, 21.3], c=GRY, lw=0.8, zorder=3)
ax.text(mxs + (nc * cs) / 2.0 - 0.5, 21.3, "OD", fontsize=11, color=GRY, fontweight="bold",
        ha="center", va="center", bbox=dict(facecolor=GLT, edgecolor="none", pad=1.5), zorder=4)


# ════════════════════════ FOOTER  y:0.5-8  h=7.5  light-blue background ═════
box(2, 0.5, 96, 7.5, FBKG, ec=B, lw=2.0)
tx(50.0, 5.7,
   "Aggregate distance distributions are near-sufficient for mobility-decay calibration.",
   sz=13.5, bold=True, c=INK)
tx(50.0, 2.7,
   "The bottleneck is trip-production estimation \u2014 not decay transfer.",
   sz=13.5, bold=True, italic=True, c=B)


# Save
HERE   = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.normpath(os.path.join(HERE, "..", "figures"))
os.makedirs(FIGDIR, exist_ok=True)

for ext, dpi in [(".pdf", None), (".png", 240)]:
    path = os.path.join(FIGDIR, "graphical_abstract" + ext)
    kw = dict(bbox_inches="tight", pad_inches=0.08)
    if dpi:
        kw["dpi"] = dpi
    fig.savefig(path, **kw)
    print("Saved:", path)
