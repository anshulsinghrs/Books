"""Book-level validation of the 50 coloring illustrations.

usage: python3 tools/validate.py   (run after src/build.py has written out/svg and out/png)
"""
import glob, os, re, sys, json
import xml.dom.minidom as md
import numpy as np
from PIL import Image


def erode(m, it):
    for _ in range(it):
        e = m.copy()
        e[1:, :] &= m[:-1, :]; e[:-1, :] &= m[1:, :]; e[:, 1:] &= m[:, :-1]; e[:, :-1] &= m[:, 1:]
        m = e
    return m

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SVG = os.path.join(ROOT, "out", "svg")
PNG = os.path.join(ROOT, "out", "png")
LIVE = (45, 36, 576, 756)         # live-area frame (pt)
SCALE = 1.6                       # PNG preview scale (px per pt)

rows, problems = [], []
hashes = {}
for n in range(1, 51):
    name = f"p{n:02d}"
    f = os.path.join(SVG, name + ".svg")
    r = {"page": n}
    if not os.path.exists(f):
        problems.append(f"{name}: missing"); continue
    s = open(f).read()
    try:
        md.parseString(s); r["xml"] = "ok"
    except Exception as e:
        r["xml"] = f"ERROR {e}"; problems.append(f"{name}: invalid XML")
    r["size"] = 'width="8.5in" height="11in" viewBox="0 0 612 792"' in s
    if not r["size"]: problems.append(f"{name}: wrong page size")
    body = s.split("</defs>", 2)[-1]
    colors = set(re.findall(r'(?:fill|stroke)="([^"]+)"', s)) - {"#000", "#fff", "none"}
    colors = {c for c in colors if not c.startswith("url(")}
    r["colors"] = sorted(colors)
    if colors: problems.append(f"{name}: non-B/W colours {colors}")
    r["text"] = len(re.findall(r"<text|<image|<foreignObject", s))
    if r["text"]: problems.append(f"{name}: text/image element present")
    dots = re.findall(r'href="#dot(?:-sleep)?" transform="translate\(([-\d.]+) ([-\d.]+)\)', body)
    r["dot"] = len(dots)
    if len(dots) != 1: problems.append(f"{name}: Dot count {len(dots)}")
    for x, y in dots:
        x, y = float(x), float(y)
        if not (LIVE[0] + 12 < x < LIVE[2] - 12 and LIVE[1] + 12 < y < LIVE[3] - 8):
            problems.append(f"{name}: Dot near/over the margin at ({x:.0f},{y:.0f})")
    bad = [d for d in re.findall(r' d="([^"]*)"', s) if re.search(r"nan|inf|None", d, re.I)]
    r["bad_paths"] = len(bad)
    if bad: problems.append(f"{name}: {len(bad)} broken path(s)")
    # raster checks
    im = np.asarray(Image.open(os.path.join(PNG, name + ".png")).convert("L"))
    h, w = im.shape
    ink = im < 128
    x0, y0, x1, y1 = [int(v * SCALE) for v in LIVE]
    outside = ink.copy(); outside[y0 - 4:y1 + 4, x0 - 4:x1 + 4] = False
    r["ink_outside_live"] = int(outside.sum())
    if outside.sum(): problems.append(f"{name}: {outside.sum()} ink px outside the live area")
    # large solid black regions: erode the ink mask; what survives is thick black
    er = erode(ink, 6)
    ys, xs = np.nonzero(er)
    cells = {}
    for yy, xx in zip(ys, xs):
        cells[(yy // 24, xx // 24)] = cells.get((yy // 24, xx // 24), 0) + 1
    # pupils/noses of close-up friends survive a little; a real filled area survives in the thousands
    r["solid_black_px_after_erosion"] = int(er.sum())
    big = [f"{v}px@({c[1]*24/SCALE:.0f},{c[0]*24/SCALE:.0f})pt" for c, v in cells.items() if v > 400]
    if er.sum() > 1500 or big: problems.append(f"{name}: large solid black area {big[:4]} total={int(er.sum())}")
    r["ink_pct"] = round(float(ink.mean()) * 100, 1)
    small = np.asarray(Image.fromarray(im).resize((64, 83)), dtype=float) / 255
    hashes[name] = small
    rows.append(r)

# near-duplicate pages
names = sorted(hashes)
dups = []
for i, a in enumerate(names):
    for b in names[i + 1:]:
        diff = float(np.abs(hashes[a] - hashes[b]).mean())
        if diff < 0.03:
            dups.append((a, b, round(diff, 4)))
if dups: problems.append(f"near-duplicate pages: {dups}")

json.dump({"pages": rows, "problems": problems}, open(os.path.join(ROOT, "out", "validation.json"), "w"), indent=1)
print(f"pages checked: {len(rows)}; problems: {len(problems)}")
for p in problems: print("  -", p)
