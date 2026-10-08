"""Recurring props, drawn once here so they look the same on every page (page units)."""
from math import sin, cos, radians, pi
from scene import clip_d, lines, uid, daisy, blossom, scallop_blob

# ---------------------------------------------------------------- shapes
def star_pts(cx, cy, r1, r2, n=5, sy=1.0, rot=-90):
    pts = []
    for k in range(2 * n):
        r = r1 if k % 2 == 0 else r2
        a = radians(rot + 180 * k / n)
        pts.append((cx + r * cos(a), cy + r * sin(a) * sy))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"


ICON = {  # tiny label icons (about 20 units), used instead of any text
    "heart": "M0 9 C-12 0 -15 -9 -8 -13 C-4 -15 0 -12 0 -9 C0 -12 4 -15 8 -13 C15 -9 12 0 0 9 Z",
    "star": star_pts(0, 0, 13, 6),
    "leaf": "M0 13 C-11 4 -11 -7 0 -14 C11 -7 11 4 0 13 Z M0 13 V-10",
    "flower": ("M0 -13 C6 -13 6 -6 3 -4 C8 -8 14 -3 10 1 C14 6 8 11 4 6 C5 11 2 14 0 14 "
               "C-2 14 -5 11 -4 6 C-8 11 -14 6 -10 1 C-14 -3 -8 -8 -3 -4 C-6 -6 -6 -13 0 -13 Z"),
    "moon": "M2 -12 A12 12 0 1 0 11 5 A9 9 0 0 1 2 -12 Z",
    "round": "M-11 0 A11 11 0 1 0 11 0 A11 11 0 1 0 -11 0 Z",
    "mushroom": "M-12 0 Q-12 -12 0 -12 Q12 -12 12 0 Z M-4 0 V9 H4 V0",
    "acorn": "M-8 -2 Q-8 11 0 13 Q8 11 8 -2 Z M-11 -2 Q0 -14 11 -2 Z",
    "berry": "M-6 2 A6 6 0 1 0 6 2 A6 6 0 1 0 -6 2 Z M0 -4 L-4 -10 M0 -4 L4 -10",
    "drop": "M0 -12 Q9 2 0 9 Q-9 2 0 -12 Z",
    "fish": "M-12 0 Q-2 -9 8 0 Q-2 9 -12 0 Z M8 0 L14 -6 L14 6 Z",
    "tree": "M0 -13 L10 4 H-10 Z M-2 4 V12 H2 V4",
    "egg": "M0 -12 C8 -12 9 2 8 5 C6 11 -6 11 -8 5 C-9 2 -8 -12 0 -12 Z",
    "cup": "M-9 -6 H7 V3 Q7 9 -1 9 Q-9 9 -9 3 Z M7 -3 Q12 -3 12 1 Q12 4 7 4",
    "note": "M-6 8 A4 3 0 1 1 -2 6 V-10 L8 -12 V4 A4 3 0 1 1 12 2 V-8 L-2 -6",
}


def icon(name, x, y, s=1.0, sw=1.1, rot=0):
    return (f'<path transform="translate({x:.1f} {y:.1f}) rotate({rot}) scale({s})" d="{ICON[name]}" '
            f'stroke-width="{sw/s:.2f}"/>')


def drop(x, y, s=1.0, sw=1.2):
    return (f'<path transform="translate({x:.1f} {y:.1f}) scale({s})" d="M0 -8 Q5.5 1 0 5 Q-5.5 1 0 -8 Z" '
            f'stroke-width="{sw/s:.2f}"/>')


# ---------------------------------------------------------------- tableware
MUG_PAT = {
    "hearts": lambda: "".join(f'<use href="#heart" transform="translate({x} {y}) scale(0.4)" stroke-width="2.4"/>' for x, y in ((-5, -10), (5, -3), (-5, 4))),
    "stripes": lambda: '<path d="M-14 -11 H14 M-14 -5 H14 M-14 1 H14 M-14 7 H14" fill="none" stroke-width="1"/>',
    "stars": lambda: "".join(f'<use href="#star5" transform="translate({x} {y}) scale(0.42)" stroke-width="2.2"/>' for x, y in ((-5, -8), (5, -1), (-4, 6))),
    "checks": lambda: '<path d="M-6 -16 V14 M0 -16 V14 M6 -16 V14 M-14 -8 H14 M-14 -2 H14 M-14 4 H14" fill="none" stroke-width="0.8"/>',
    "leaves": lambda: "".join(f'<path transform="translate({x} {y}) rotate({r})" d="M0 4 C-3 1 -3 -2 0 -5 C3 -2 3 1 0 4 Z" stroke-width="0.9"/>' for x, y, r in ((-6, -8, -30), (4, -4, 30), (-4, 4, -30))),
    "dots": lambda: "".join(f'<circle cx="{x}" cy="{y}" r="2" stroke-width="0.8"/>' for x, y in ((-6, -9), (2, -8), (-2, -1), (6, 0), (-6, 6), (3, 7))),
    "plain": lambda: "",
}


def mug(x, y, s=1.0, pat="plain", steam=False, handle="r"):
    """Mug with base centre at (x, y); 26 units tall at s=1."""
    hx = 1 if handle == "r" else -1
    d = "M-11 -24 H11 V-6 Q11 2 0 2 Q-11 2 -11 -6 Z"
    body = clip_d(d, f'<g transform="translate(0 -10)">{MUG_PAT[pat]()}</g>', 1.6 / s)
    out = (f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" stroke-width="{1.6/s:.2f}">'
           f'<path d="M{11*hx} -19 Q{20*hx} -19 {20*hx} -12 Q{20*hx} -5 {10*hx} -5" fill="none" stroke-width="{3.6/s:.2f}"/>'
           f'<path d="M{11*hx} -19 Q{20*hx} -19 {20*hx} -12 Q{20*hx} -5 {10*hx} -5" fill="none" stroke="#fff" stroke-width="{1.2/s:.2f}"/>'
           f'{body}<ellipse cy="-24" rx="11" ry="3" stroke-width="{1.2/s:.2f}"/>')
    if steam:
        out += f'<path d="M-4 -30 q-4 -6 0 -12 q4 -6 0 -12 M5 -30 q-4 -6 0 -12" fill="none" stroke-width="{1.1/s:.2f}"/>'
    return out + "</g>"


def steam_curl(x, y, s=1.0):
    """Closed S-shaped steam ribbon rising from (x, y)."""
    return (f'<path transform="translate({x:.1f} {y:.1f}) scale({s})" d="M-3 0 C-16 -10 9 -22 -4 -36 Q0 -40 4 -36 '
            f'C17 -22 -8 -10 3 0 Q0 3 -3 0 Z" stroke-width="{1.2/s:.2f}"/>')


def teacup(x, y, s=1.0):
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" stroke-width="{1.4/s:.2f}">'
            '<ellipse cy="0" rx="18" ry="4.5"/><path d="M13 -12 Q20 -12 20 -7 Q20 -2 12 -3" fill="none" stroke-width="2.4"/>'
            '<path d="M-13 -14 H13 Q12 -2 0 -1 Q-12 -2 -13 -14 Z"/><ellipse cy="-14" rx="13" ry="3"/>'
            '<path d="M-6 -8 Q0 -11 6 -8" fill="none" stroke-width="0.9"/></g>')


def teapot(x, y, s=1.0):
    """The cottage teapot (leaf pattern) — base centre at (x, y), ~60 wide at s=1."""
    body = "M-26 0 Q-34 -26 -14 -36 H14 Q34 -26 26 0 Q0 6 -26 0 Z"
    leaves = "".join(f'<path transform="translate({lx} {ly}) rotate({r})" d="M0 5 C-4 1 -4 -3 0 -7 C4 -3 4 1 0 5 Z M0 5 V-4" stroke-width="0.9"/>'
                     for lx, ly, r in ((-14, -20, -40), (0, -16, 0), (14, -20, 40), (-8, -8, -20), (8, -8, 20)))
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" stroke-width="{1.7/s:.2f}">'
            '<path d="M24 -24 Q40 -26 44 -40 L48 -38 Q44 -18 26 -12 Z"/>'
            '<path d="M-26 -26 Q-44 -26 -42 -14 Q-40 -4 -26 -8" fill="none" stroke-width="3.8"/>'
            '<path d="M-26 -26 Q-44 -26 -42 -14 Q-40 -4 -26 -8" fill="none" stroke="#fff" stroke-width="1.4"/>'
            + clip_d(body, leaves, 1.7 / s) +
            '<path d="M-16 -36 Q0 -46 16 -36 Z"/><circle cy="-46" r="4.5"/></g>')


def kettle(x, y, s=1.0, steam=True):
    out = (f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" stroke-width="{1.8/s:.2f}">'
           '<path d="M28 -18 Q44 -24 50 -42 L55 -40 Q50 -14 30 -8 Z"/>'
           '<path d="M-30 0 Q-40 -34 -16 -44 H16 Q40 -34 30 0 Q0 6 -30 0 Z"/>'
           '<path d="M-30 -10 Q0 -4 30 -10" fill="none" stroke-width="1.1"/>'
           '<path d="M-18 -44 Q-16 -70 0 -70 Q16 -70 18 -44" fill="none" stroke-width="4"/>'
           '<path d="M-18 -44 Q-16 -70 0 -70 Q16 -70 18 -44" fill="none" stroke="#fff" stroke-width="1.4"/>'
           '<path d="M-12 -44 Q0 -52 12 -44 Z"/><circle cy="-51" r="4"/>')
    out += "</g>"
    if steam:
        out += steam_curl(x + 54 * s, y - 50 * s, s) + steam_curl(x + 70 * s, y - 92 * s, s * 0.8)
    return out


def stove(x, y, w=150, h=170, pipe_to=None):
    """Bramble's cast-iron wood stove: top at y, centre x."""
    l, r = x - w / 2, x + w / 2
    out = []
    if pipe_to is not None:
        out.append(f'<rect x="{x - 12}" y="{pipe_to}" width="24" height="{y - pipe_to}" stroke-width="1.8"/>')
        out.append(f'<rect x="{x - 16}" y="{y - (y - pipe_to) * 0.5:.0f}" width="32" height="10" rx="2" stroke-width="1.5"/>')
    out.append(f'<rect x="{l - 6}" y="{y}" width="{w + 12}" height="14" rx="3" stroke-width="2"/>')
    out.append(f'<rect x="{l}" y="{y + 14}" width="{w}" height="{h - 34}" rx="6" stroke-width="2"/>')
    out.append(f'<rect x="{l + 6}" y="{y + 14 + h - 34}" width="{w - 12}" height="8" stroke-width="1.6"/>')
    out.append(f'<path d="M{l + 12} {y + h - 12} L{l + 6} {y + h} H{l + 22} L{l + 24} {y + h - 12} Z '
               f'M{r - 12} {y + h - 12} L{r - 6} {y + h} H{r - 22} L{r - 24} {y + h - 12} Z" stroke-width="1.6"/>')
    dx, dy, dw, dh = x - w * 0.3, y + 32, w * 0.6, h * 0.42
    out.append(f'<rect x="{dx:.1f}" y="{dy:.1f}" width="{dw:.1f}" height="{dh:.1f}" rx="5" stroke-width="1.8"/>')
    fx, fy = x, dy + dh * 0.78
    out.append(f'<path d="M{fx - 14:.1f} {fy:.1f} C{fx - 20:.1f} {fy - 18:.1f} {fx - 6:.1f} {fy - 26:.1f} {fx - 2:.1f} {fy - 38:.1f} '
               f'C{fx + 4:.1f} {fy - 26:.1f} {fx + 14:.1f} {fy - 22:.1f} {fx + 10:.1f} {fy - 10:.1f} '
               f'C{fx + 16:.1f} {fy - 14:.1f} {fx + 18:.1f} {fy - 6:.1f} {fx + 14:.1f} {fy:.1f} Z" stroke-width="1.4"/>')
    out.append(f'<rect x="{dx + dw + 6:.1f}" y="{dy + dh / 2 - 4:.1f}" width="14" height="8" rx="3" stroke-width="1.4"/>')
    out.append(lines(f"M{l + 10} {y + 22} H{r - 10}", 1))
    return "".join(out)


def jar(x, y, w=30, h=40, ico=None, sw=1.6):
    """Jar with lid, base centre (x, y)."""
    out = (f'<path d="M{x - w/2} {y - h + 8} H{x + w/2} V{y - 6} Q{x + w/2} {y} {x} {y} Q{x - w/2} {y} {x - w/2} {y - 6} Z" stroke-width="{sw}"/>'
           f'<rect x="{x - w/2 - 2}" y="{y - h}" width="{w + 4}" height="10" rx="3" stroke-width="{sw*0.9:.2f}"/>')
    if ico:
        out += f'<rect x="{x - w*0.32:.1f}" y="{y - h*0.62:.1f}" width="{w*0.64:.1f}" height="{h*0.4:.1f}" rx="2" stroke-width="1"/>'
        out += icon(ico, x, y - h * 0.42, min(w, h) / 46, 1.0)
    return out


def tin(x, y, w=34, h=44, ico="leaf"):
    return (f'<rect x="{x - w/2}" y="{y - h}" width="{w}" height="{h}" rx="3" stroke-width="1.6"/>'
            f'<rect x="{x - w/2 - 2}" y="{y - h - 8}" width="{w + 4}" height="10" rx="2" stroke-width="1.5"/>'
            f'<circle cx="{x}" cy="{y - h/2}" r="{w*0.32:.1f}" stroke-width="1.1"/>' + icon(ico, x, y - h / 2, w / 60, 1.0))


def pancake_stack(x, y, n=10, w=110, th=11, drips=True):
    """The pancake tower from page 4 — base centre (x, y)."""
    out = [f'<ellipse cx="{x}" cy="{y}" rx="{w*0.62:.1f}" ry="9" stroke-width="1.8"/>']
    for k in range(n):
        yy = y - 4 - k * th
        ww = w / 2 - (k % 3) * 2
        out.append(f'<path d="M{x - ww:.1f} {yy:.1f} Q{x - ww - 3:.1f} {yy - th/2:.1f} {x - ww:.1f} {yy - th:.1f} '
                   f'H{x + ww:.1f} Q{x + ww + 3:.1f} {yy - th/2:.1f} {x + ww:.1f} {yy:.1f} Q{x} {yy + 3:.1f} {x - ww:.1f} {yy:.1f} Z" stroke-width="1.4"/>')
    top = y - 4 - n * th
    out.append(f'<ellipse cx="{x}" cy="{top:.1f}" rx="{w/2:.1f}" ry="8" stroke-width="1.5"/>')
    if drips:
        out.append(f'<path d="M{x - w*0.38:.1f} {top:.1f} Q{x} {top - 9:.1f} {x + w*0.38:.1f} {top:.1f} '
                   f'Q{x + w*0.4:.1f} {top + 24:.1f} {x + w*0.32:.1f} {top + 26:.1f} Q{x + w*0.26:.1f} {top + 22:.1f} {x + w*0.24:.1f} {top + 6:.1f} '
                   f'Q{x} {top + 10:.1f} {x - w*0.2:.1f} {top + 6:.1f} Q{x - w*0.24:.1f} {top + 34:.1f} {x - w*0.31:.1f} {top + 34:.1f} '
                   f'Q{x - w*0.38:.1f} {top + 30:.1f} {x - w*0.38:.1f} {top:.1f} Z" stroke-width="1.3"/>')
    out.append(f'<rect x="{x - 12}" y="{top - 13:.1f}" width="24" height="12" rx="3" stroke-width="1.5"/>')
    return "".join(out)


def bowl(x, y, w=60, h=26, fill=None, pat=None):
    """Bowl base centre (x, y). fill: 'berries' | 'cream' | None."""
    out = ""
    if fill == "berries":
        for k in range(7):
            out += f'<circle cx="{x - w*0.32 + k * w*0.11:.1f}" cy="{y - h + (k % 2) * 4 - 2:.1f}" r="{w*0.07:.1f}" stroke-width="1.1"/>'
    if fill == "cream":
        out += f'<path d="M{x - w*0.4:.1f} {y - h} Q{x - w*0.3:.1f} {y - h - 14} {x:.1f} {y - h - 18} Q{x + w*0.3:.1f} {y - h - 14} {x + w*0.4:.1f} {y - h} Z" stroke-width="1.3"/>'
    out += (f'<path d="M{x - w/2} {y - h} Q{x - w/2} {y} {x} {y} Q{x + w/2} {y} {x + w/2} {y - h} Z" stroke-width="1.7"/>'
            f'<ellipse cx="{x}" cy="{y - h}" rx="{w/2}" ry="{h*0.18:.1f}" stroke-width="1.4"/>')
    if pat == "stripe":
        out += lines(f"M{x - w*0.46:.1f} {y - h*0.55:.1f} Q{x} {y - h*0.3:.1f} {x + w*0.46:.1f} {y - h*0.55:.1f}", 1.0)
    return out


# ---------------------------------------------------------------- house
def picture(x, y, w, h, kind="tree", sw=1.8):
    """Framed picture: kind tree | mountain | teacup | flower | heart | landscape."""
    inner = {
        "tree": f'<rect x="{-3}" y="{h*0.05:.1f}" width="6" height="{h*0.25:.1f}"/>' + f'<circle cy="{-h*0.08:.1f}" r="{min(w, h)*0.22:.1f}"/>',
        "mountain": f'<path d="M{-w*0.36:.1f} {h*0.26:.1f} L{-w*0.08:.1f} {-h*0.2:.1f} L{w*0.06:.1f} {h*0.02:.1f} L{w*0.16:.1f} {-h*0.08:.1f} L{w*0.36:.1f} {h*0.26:.1f} Z"/>',
        "teacup": f'<g transform="translate(0 {h*0.12:.1f}) scale({min(w, h)/60:.2f})">' + '<path d="M-13 -14 H13 Q12 -2 0 -1 Q-12 -2 -13 -14 Z"/><path d="M13 -11 Q20 -11 19 -6 Q18 -2 12 -4" fill="none"/><ellipse cy="0" rx="18" ry="4"/></g>',
        "flower": f'<path d="M0 {h*0.3:.1f} V0" fill="none"/>' + f'<g transform="scale({min(w, h)/60:.2f})">' + "".join(f'<circle cx="0" cy="-8" r="6" transform="rotate({72*k})"/>' for k in range(5)) + '<circle r="4"/></g>',
        "heart": f'<use href="#heart" transform="scale({min(w, h)/36:.2f})"/>',
        "moon": f'<use href="#crescent" transform="scale({min(w, h)/28:.2f})"/>',
    }[kind]
    return (f'<g transform="translate({x} {y})" stroke-width="{sw}"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="3"/>'
            f'<rect x="{-w/2 + 7}" y="{-h/2 + 7}" width="{w - 14}" height="{h - 14}" rx="1" stroke-width="1.1"/>'
            f'<g stroke-width="1.2">{inner}</g></g>')


def floorboards(x0, y0, x1, y1, step=60, vp=None, sw=1.0):
    d = f"M{x0} {y0} H{x1} V{y1} H{x0} Z"
    if vp:
        inner = " ".join(f"M{vp[0] + (x - vp[0]) * 0.15:.0f} {y0} L{x} {y1}" for x in range(x0 - 400, x1 + 400, step))
    else:
        inner = " ".join(f"M{x0} {y} H{x1}" for y in range(y0 + step, y1, step))
    return clip_d(d, lines(inner, sw), 1.6)


def rug_round(x, y, rx, ry, rings=3):
    out = f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" stroke-width="1.8"/>'
    for k in range(1, rings):
        f = 1 - k / (rings + 0.6)
        out += f'<ellipse cx="{x}" cy="{y}" rx="{rx*f:.1f}" ry="{ry*f:.1f}" stroke-width="1.1"/>'
    return out


def cushion(x, y, w, h, pat="plain", rot=0, tassel=False):
    d = (f"M{-w/2} {-h/2 + 6} Q{-w/2} {-h/2} {-w/2 + 6} {-h/2} Q0 {-h/2 + 6} {w/2 - 6} {-h/2} Q{w/2} {-h/2} {w/2} {-h/2 + 6} "
         f"Q{w/2 - 5} 0 {w/2} {h/2 - 6} Q{w/2} {h/2} {w/2 - 6} {h/2} Q0 {h/2 - 6} {-w/2 + 6} {h/2} Q{-w/2} {h/2} {-w/2} {h/2 - 6} Q{-w/2 + 5} 0 {-w/2} {-h/2 + 6} Z")
    inner = ""
    if pat == "stripes":
        inner = lines(" ".join(f"M{x_} {-h} V{h}" for x_ in range(int(-w/2) + 9, int(w/2), 10)), 1)
    elif pat == "dots":
        inner = "".join(f'<circle cx="{xx}" cy="{yy}" r="2.4" stroke-width="0.9"/>' for xx in range(int(-w/2) + 8, int(w/2) - 4, 12) for yy in range(int(-h/2) + 8, int(h/2) - 4, 12))
    elif pat == "flower":
        inner = blossom(0, 0, min(w, h) * 0.35, 1.1)
    elif pat == "heart":
        inner = f'<use href="#heart" transform="scale({min(w, h)/30:.2f})" stroke-width="{30/min(w, h):.2f}"/>'
    elif pat == "zigzag":
        inner = lines("M" + " L".join(f"{-w/2 + k*8:.0f} {(-4 if k % 2 else 4)}" for k in range(int(w/8) + 2)), 1)
    out = f'<g transform="translate({x} {y}) rotate({rot})">' + clip_d(d, inner, 1.7) + "</g>"
    if tassel:
        out += "".join(f'<path transform="translate({x} {y}) rotate({rot})" d="M{sx*w/2} {sy*h/2} l{sx*5} {sy*5} l{sx*-2} {sy*5} l{sx*5} {sy*-2} Z" stroke-width="1.1"/>'
                       for sx in (-1, 1) for sy in (-1, 1))
    return out


def plant_pot(x, y, w=40, h=34, pat="plain"):
    """Flowerpot (base centre x, y) with a pattern band."""
    d = f"M{x - w/2} {y - h + 8} H{x + w/2} L{x + w*0.38:.1f} {y} H{x - w*0.38:.1f} Z"
    inner = ""
    if pat == "stripes":
        inner = lines(" ".join(f"M{x - w} {yy:.1f} H{x + w}" for yy in (y - h*0.55, y - h*0.3)), 1)
    elif pat == "dots":
        inner = "".join(f'<circle cx="{x - w*0.3 + k*w*0.2:.1f}" cy="{y - h*0.4 + (k % 2)*6:.1f}" r="2.6" stroke-width="0.9"/>' for k in range(4))
    elif pat == "zigzag":
        inner = lines("M" + " L".join(f"{x - w/2 + k*6:.1f} {y - h*0.42 + (4 if k % 2 else -4):.1f}" for k in range(int(w/6) + 2)), 1)
    elif pat == "scallops":
        inner = lines(" ".join(f"M{x - w/2 + k*8:.1f} {y - h*0.5:.1f} a4 4 0 0 0 8 0" for k in range(int(w/8) + 1)), 1)
    return clip_d(d, inner, 1.7) + f'<rect x="{x - w/2 - 3}" y="{y - h}" width="{w + 6}" height="10" rx="2" stroke-width="1.7"/>'


def plant(kind, x, y, s=1.0):
    """Foliage growing up from (x, y) (draw before the pot)."""
    g = f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.3/s:.2f}">'
    if kind == "fern":
        from scene import fern
        body = fern(0, 0, 60, -40, -10, 5, 9) + fern(0, 0, 66, 0, 8, 5, 9) + fern(0, 0, 58, 40, 10, 5, 9)
    elif kind == "vine":
        body = ('<path d="M-10 0 C-30 20 -36 50 -30 80 M10 0 C30 26 30 56 40 84" fill="none"/>'
                + "".join(f'<use href="#heart" transform="translate({xx} {yy}) rotate(180) scale(0.8)"/>' for xx, yy in ((-22, 22), (-32, 46), (-30, 72), (22, 26), (30, 52), (38, 78))))
    elif kind == "cactus":
        body = ('<path d="M-16 0 Q-20 -30 0 -34 Q20 -30 16 0 Z"/><path d="M0 -34 V0 M-9 -30 Q-12 -14 -9 0 M9 -30 Q12 -14 9 0" fill="none" stroke-width="0.9"/>'
                + "".join(f'<path d="M{xx} {yy} l-3 -3 M{xx} {yy} l3 -3" fill="none" stroke-width="0.8"/>' for xx, yy in ((-13, -14), (13, -18), (0, -26), (-5, -8), (6, -6))) + blossom(0, -36, 7, 1))
    elif kind == "snake":
        body = "".join(f'<path d="M{xx} 0 Q{xx + lean} -40 {xx + lean*1.6} -{hh} Q{xx + lean*0.6 + 6} -40 {xx + 8} 0 Z"/>' for xx, lean, hh in ((-14, -6, 62), (-4, 2, 76), (6, 8, 58)))
    elif kind == "flowers":
        body = ('<path d="M-8 0 Q-12 -20 -16 -34 M0 0 V-40 M8 0 Q12 -20 16 -30" fill="none"/>'
                + '<path d="M0 -10 Q-14 -16 -16 -26 Q-4 -22 0 -10 Z M0 -16 Q14 -22 16 -32 Q4 -28 0 -16 Z"/>'
                + daisy(-16, -38, 9, 6, 1.1) + daisy(0, -46, 10, 7, 1.1) + daisy(16, -34, 8, 6, 1.1))
    elif kind == "succulent":
        body = "".join(f'<path transform="rotate({r})" d="M0 0 Q-6 -8 0 -16 Q6 -8 0 0 Z"/>' for r in (-60, -30, 0, 30, 60))
    elif kind == "split":
        body = ('<path d="M0 0 Q-6 -40 -30 -60 M0 0 Q4 -50 20 -76 M0 0 Q10 -30 40 -44" fill="none"/>'
                + "".join(f'<g transform="translate({xx} {yy}) rotate({r})"><path d="M0 0 C-22 -4 -28 -30 0 -40 C28 -30 22 -4 0 0 Z"/>'
                          '<path d="M0 -2 V-34 M-14 -26 L-6 -22 M14 -26 L6 -22 M-16 -12 L-6 -12 M16 -12 L6 -12" fill="none" stroke-width="0.9"/></g>'
                          for xx, yy, r in ((-30, -56, -40), (20, -72, 10), (40, -42, 60))))
    elif kind == "herb":
        body = "".join(f'<path d="M{xx} 0 Q{xx} -12 {xx + lean} -24" fill="none"/><ellipse cx="{xx + lean}" cy="-26" rx="4" ry="7" transform="rotate({lean*4} {xx + lean} -26)"/>'
                       f'<ellipse cx="{xx + lean*0.5 - 5}" cy="-14" rx="3" ry="6" transform="rotate(-40 {xx + lean*0.5 - 5} -14)"/>'
                       for xx, lean in ((-8, -6), (0, 0), (8, 6)))
    else:
        body = ""
    return g + body + "</g>"


def lantern_hanging(x, y, s=1.0, chain=24):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.5/s:.2f}">'
            f'<path d="M0 0 V{chain}" fill="none" stroke-width="{1.2/s:.2f}"/>'
            f'<path d="M-12 {chain + 12} L0 {chain} L12 {chain + 12} Z"/>'
            f'<rect x="-11" y="{chain + 12}" width="22" height="30" rx="2"/>'
            f'<path d="M-14 {chain + 42} H14 L10 {chain + 49} H-10 Z"/>'
            f'<path d="M0 {chain + 34} Q-5 {chain + 27} 0 {chain + 19} Q5 {chain + 27} 0 {chain + 34} Z" stroke-width="{1/s:.2f}"/></g>')


def paper_lantern(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}">'
            '<path d="M0 -40 V-26" fill="none"/><rect x="-9" y="-28" width="18" height="6" rx="2"/>'
            '<ellipse cy="0" rx="20" ry="24"/><path d="M-19 -8 Q0 -4 19 -8 M-19 8 Q0 12 19 8 M0 -24 V24" fill="none" stroke-width="0.9"/>'
            '<rect x="-9" y="22" width="18" height="6" rx="2"/></g>')


def bunting(points, motifs=("star", "heart", "leaf", "flower"), size=26):
    """Triangle flags along a sagging string through the given points."""
    from scene import lines as _l
    (x0, y0), (x1, y1) = points[0], points[-1]
    sag = points[1][1] if len(points) == 3 else (y0 + y1) / 2 + 30
    out = [f'<path d="M{x0} {y0} Q{(x0 + x1)/2:.0f} {2*sag - (y0 + y1)/2:.0f} {x1} {y1}" fill="none" stroke-width="1.4"/>']
    n = int(abs(x1 - x0) / (size * 1.25))
    for k in range(1, n):
        t = k / n
        qx = (x0 + x1) / 2
        qy = 2 * sag - (y0 + y1) / 2
        x = (1 - t)**2 * x0 + 2 * (1 - t) * t * qx + t * t * x1
        y = (1 - t)**2 * y0 + 2 * (1 - t) * t * qy + t * t * y1
        out.append(f'<path d="M{x - size/2:.1f} {y:.1f} H{x + size/2:.1f} L{x:.1f} {y + size*1.15:.1f} Z" stroke-width="1.5"/>')
        if motifs:
            out.append(icon(motifs[k % len(motifs)], x, y + size * 0.42, size / 70, 1.0))
    return "".join(out)


def window_rect(x, y, w, h, view="", muntins=(1, 1), sill=True, sw=2.0):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" stroke-width="{sw}"/>'
    out += clip_d(f"M{x+8} {y+8} H{x+w-8} V{y+h-8} H{x+8} Z", view, 1.5, fill="#fff")
    ml = " ".join(f"M{x + w*k/(muntins[0]+1):.1f} {y+8} V{y+h-8}" for k in range(1, muntins[0] + 1))
    ml += " " + " ".join(f"M{x+8} {y + h*k/(muntins[1]+1):.1f} H{x+w-8}" for k in range(1, muntins[1] + 1))
    out += lines(ml, 2.2)
    if sill:
        out += f'<rect x="{x - 10}" y="{y + h - 2}" width="{w + 20}" height="12" rx="3" stroke-width="1.8"/>'
    return out


def book_open(x, y, w=60, h=36, lines_=3, sw=1.5):
    """Open book seen from the front/above, gutter at x."""
    hw = w / 2
    out = (f'<path d="M{x - hw - 3} {y - h + 4} L{x - hw - 3} {y + 4} Q{x - hw/2} {y} {x} {y + 6} Q{x + hw/2} {y} {x + hw + 3} {y + 4} L{x + hw + 3} {y - h + 4} Z" stroke-width="{sw}"/>'
           f'<path d="M{x} {y - h + 6} Q{x - hw/2} {y - h} {x - hw} {y - h + 3} L{x - hw} {y} Q{x - hw/2} {y - 4} {x} {y + 2} Z" stroke-width="{sw*0.85:.2f}"/>'
           f'<path d="M{x} {y - h + 6} Q{x + hw/2} {y - h} {x + hw} {y - h + 3} L{x + hw} {y} Q{x + hw/2} {y - 4} {x} {y + 2} Z" stroke-width="{sw*0.85:.2f}"/>')
    ls = ""
    for k in range(lines_):
        yy = y - h + 12 + k * (h - 16) / max(lines_, 1)
        ls += f"M{x - hw + 6} {yy:.1f} Q{x - hw/2} {yy - 3:.1f} {x - 5} {yy + 1:.1f} M{x + 5} {yy + 1:.1f} Q{x + hw/2} {yy - 3:.1f} {x + hw - 6} {yy:.1f} "
    return out + lines(ls, 0.75)


def book_closed(x, y, w=40, h=10, rot=0, band=True):
    out = f'<g transform="translate({x} {y}) rotate({rot})"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="2" stroke-width="1.5"/>'
    if band:
        out += lines(f"M{w/2 - 8} {-h/2 + 1.5} V{h/2 - 1.5} M{-w/2 + 6} {-h/2 + 1.5} V{h/2 - 1.5}", 0.8)
    return out + "</g>"


def snail(x, y, s=1.0, flip=False):
    f = -1 if flip else 1
    return (f'<g transform="translate({x} {y}) scale({f*s} {s})" stroke-width="{1.4/s:.2f}">'
            '<path d="M-24 0 Q-26 -8 -16 -9 L12 -7 Q22 -4 20 0 Z"/>'
            '<path d="M-18 -8 L-23 -21 M-13 -9 L-14 -23" fill="none" stroke-width="1.2"/>'
            '<circle cx="-23" cy="-22" r="2" fill="#000" stroke="none"/><circle cx="-14" cy="-24" r="2" fill="#000" stroke="none"/>'
            '<circle cx="2" cy="-18" r="13"/>'
            '<path d="M2 -18 m3 0 a3 3 0 1 1 -6 0 a6 6 0 1 1 12 0 a9 9 0 1 1 -18 0" fill="none" stroke-width="1.1"/></g>')


def butterfly(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.2/s:.2f}">'
            '<path d="M0 0 C-14 -20 -26 -10 -18 0 C-26 8 -14 18 0 4 Z"/><path d="M0 0 C14 -20 26 -10 18 0 C26 8 14 18 0 4 Z"/>'
            '<circle cx="-12" cy="-6" r="3"/><circle cx="12" cy="-6" r="3"/><ellipse cx="0" cy="2" rx="2" ry="8"/>'
            '<path d="M0 -6 L-4 -14 M0 -6 L4 -14" fill="none"/></g>')


def duck(x, y, s=1.0, flip=False):
    f = -1 if flip else 1
    return (f'<g transform="translate({x} {y}) scale({f*s} {s})" stroke-width="{1.5/s:.2f}">'
            '<path d="M-18 0 Q-22 -16 -6 -16 Q0 -16 4 -12 Q14 -14 18 -6 Q14 4 0 4 Q-14 4 -18 0 Z"/>'
            '<circle cx="-12" cy="-22" r="8"/><path d="M-20 -22 L-28 -20 L-20 -18 Z"/><circle cx="-14" cy="-24" r="1.4" fill="#000" stroke="none"/>'
            '<path d="M-4 -8 Q4 -4 10 -8" fill="none" stroke-width="1"/></g>')


def frog(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}">'
            '<path d="M-16 0 Q-18 -16 0 -16 Q18 -16 16 0 Z"/><circle cx="-8" cy="-16" r="6"/><circle cx="8" cy="-16" r="6"/>'
            '<circle cx="-8" cy="-16" r="2.4" fill="#000" stroke="none"/><circle cx="8" cy="-16" r="2.4" fill="#000" stroke="none"/>'
            '<path d="M-6 -6 Q0 -2 6 -6" fill="none" stroke-width="1.1"/>'
            '<ellipse cx="-14" cy="0" rx="7" ry="3.5"/><ellipse cx="14" cy="0" rx="7" ry="3.5"/></g>')


def sun_hat(x, y, w=70, rot=0, band=True):
    """Straw sun hat sitting at (x, y) = brim centre."""
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot})" stroke-width="1.7">'
            f'<ellipse rx="{w/2}" ry="{w*0.14:.1f}"/>'
            f'<path d="M{-w*0.27:.1f} 0 Q{-w*0.26:.1f} {-w*0.36:.1f} 0 {-w*0.37:.1f} Q{w*0.26:.1f} {-w*0.36:.1f} {w*0.27:.1f} 0 Z"/>'
            + (f'<path d="M{-w*0.27:.1f} -2 Q0 4 {w*0.27:.1f} -2 L{w*0.27:.1f} {-w*0.1:.1f} Q0 {-w*0.04:.1f} {-w*0.27:.1f} {-w*0.1:.1f} Z" stroke-width="1.2"/>' if band else "")
            + "</g>")


def basket(x, y, w=70, h=40, handle=True, lid=False):
    d = f"M{x - w/2} {y - h} H{x + w/2} L{x + w*0.42:.1f} {y} Q{x} {y + 4} {x - w*0.42:.1f} {y} Z"
    weave = lines(" ".join(f"M{x - w} {y - h + k*h/4:.1f} H{x + w}" for k in range(1, 4)) + " "
                  + " ".join(f"M{x - w/2 + k*w/5:.1f} {y - h} V{y + 4}" for k in range(1, 5)), 1.0)
    out = clip_d(d, weave, 1.8)
    if lid:
        out += f'<path d="M{x - w/2 - 4} {y - h} Q{x} {y - h - 18} {x + w/2 + 4} {y - h} Q{x} {y - h + 6} {x - w/2 - 4} {y - h} Z" stroke-width="1.7"/>'
    if handle:
        out = (f'<path d="M{x - w*0.32:.1f} {y - h} Q{x} {y - h - w*0.6:.1f} {x + w*0.32:.1f} {y - h}" fill="none" stroke-width="5"/>'
               f'<path d="M{x - w*0.32:.1f} {y - h} Q{x} {y - h - w*0.6:.1f} {x + w*0.32:.1f} {y - h}" fill="none" stroke="#fff" stroke-width="2"/>') + out
    return out


def leaf_simple(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.2/s:.2f}">'
            '<path d="M0 0 C-8 -6 -8 -18 0 -26 C8 -18 8 -6 0 0 Z"/><path d="M0 2 V-22" fill="none" stroke-width="0.8"/></g>')


def maple_leaf(x, y, rot=0, s=1.0):
    d = "M0 4 L-3 -2 L-12 0 L-9 -6 L-16 -12 L-8 -13 L-9 -20 L-3 -16 L0 -26 L3 -16 L9 -20 L8 -13 L16 -12 L9 -6 L12 0 L3 -2 Z"
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.2/s:.2f}">'
            f'<path d="{d}" stroke-linejoin="round"/><path d="M0 6 V-18" fill="none" stroke-width="0.8"/></g>')


def ginkgo_leaf(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.2/s:.2f}">'
            '<path d="M0 0 L-12 -20 Q-4 -26 0 -20 Q4 -26 12 -20 Z"/><path d="M0 0 V6" fill="none"/></g>')


def acorn(x, y, s=1.0, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.2/s:.2f}">'
            '<ellipse cy="6" rx="5.5" ry="7"/><path d="M-7 1 Q0 -8 7 1 Q0 4 -7 1 Z"/><path d="M0 -4 V-8" fill="none"/></g>')


def snowflake(x, y, s=1.0):
    return f'<use href="#flake" transform="translate({x} {y}) scale({s})" stroke-width="{1.1/s:.2f}"/>'


def star(x, y, s=1.0, k=5):
    ref = "star5" if k == 5 else "star4"
    return f'<use href="#{ref}" transform="translate({x} {y}) scale({s})" stroke-width="{1.3/s:.2f}"/>'


def quilt_patch(x, y, w, h, sym=None, pat=None, stitch=True, sw=1.6):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" stroke-width="{sw}"/>'
    if pat:
        inner = {
            "plaid": " ".join(f"M{x + k*w/5:.1f} {y} V{y + h}" for k in range(1, 5)) + " " + " ".join(f"M{x} {y + k*h/5:.1f} H{x + w}" for k in range(1, 5)),
            "stripes": " ".join(f"M{x + k*w/6:.1f} {y} L{x + k*w/6 - h*0.3:.1f} {y + h}" for k in range(1, 8)),
        }.get(pat)
        if inner:
            out = clip_d(f"M{x} {y} H{x + w} V{y + h} H{x} Z", lines(inner, 0.8), sw)
        if pat == "dots":
            out += "".join(f'<circle cx="{x + w*(0.2 + 0.3*i):.1f}" cy="{y + h*(0.2 + 0.3*j):.1f}" r="2.2" stroke-width="0.8"/>' for i in range(3) for j in range(3) if (i, j) != (1, 1))
    if stitch:
        out += f'<rect x="{x + 4}" y="{y + 4}" width="{w - 8}" height="{h - 8}" fill="none" stroke-width="0.8" stroke-dasharray="3 3"/>'
    if sym:
        out += (f'<g transform="translate({x + w/2:.1f} {y + h/2:.1f}) scale({min(w, h)/48:.2f})" stroke-width="{1.4*48/min(w, h):.2f}">'
                f'<use href="#sym-{sym}" transform="scale(0.85)"/></g>')
    return out


SYMBOLS = ["acorn", "clover", "fish", "star", "pompom", "moon", "pebble", "needle"]


def umbrella(x, y, r=70, pat="dots", rot=0, ribs=6):
    """Umbrella canopy centred over the shaft top at (x, y); shaft hangs down 1.4 r."""
    d = f"M{-r} 0 A{r} {r*0.72:.1f} 0 0 1 {r} 0 " + " ".join(
        f"Q{r - (k + 0.5) * 2*r/ribs:.1f} {-r*0.12:.1f} {r - (k + 1) * 2*r/ribs:.1f} 0" for k in range(ribs)) + " Z"
    inner = " ".join(f"M0 {-r*0.72:.1f} Q{(-r + k*2*r/ribs)*0.55:.1f} {-r*0.4:.1f} {-r + k*2*r/ribs:.1f} 0" for k in range(1, ribs))
    pat_s = ""
    if pat == "dots":
        pat_s = "".join(f'<circle cx="{dx*r:.1f}" cy="{dy*r:.1f}" r="{r*0.07:.1f}" stroke-width="1"/>' for dx, dy in ((-0.6, -0.2), (-0.25, -0.45), (0.15, -0.3), (0.5, -0.45), (0.65, -0.15), (-0.1, -0.12), (0.3, -0.62), (-0.45, -0.55)))
    elif pat == "stripes":
        pat_s = lines(" ".join(f"M{-r} {-r*f:.1f} H{r}" for f in (0.2, 0.38, 0.54)), 1.0)
    elif pat == "scallops":
        pat_s = lines(" ".join(f"M{-r + k*12:.1f} {-r*0.18:.1f} a6 6 0 0 0 12 0" for k in range(int(2*r/12))), 1.0)
    from scene import uid as _u
    k = _u("u")
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot})">'
            f'<path d="M0 0 V{r*1.3:.1f} q0 10 -9 10 q-9 0 -9 -8" fill="none" stroke-width="2.6"/>'
            f'<clipPath id="{k}"><path d="{d}"/></clipPath><path d="{d}" stroke-width="2"/>'
            f'<g clip-path="url(#{k})" fill="none">{pat_s}<path d="{inner}" stroke-width="1.1"/></g>'
            f'<path d="{d}" fill="none" stroke-width="2"/><path d="M0 {-r*0.72:.1f} v-10" stroke-width="2.4"/><circle cy="{-r*0.72 - 12:.1f}" r="3" stroke-width="1.3"/></g>')


def boots(c, s):
    """Rain boots over a friend's feet (model units, pass as char front=)."""
    from chars import CAST
    fx = {"cl": 14, "ju": 13, "pb": 10, "pi": 11, "mi": 10, "br": 24, "to": 22, "th": 6}[c]
    w = {"cl": 13, "ju": 11, "pb": 9, "pi": 10, "mi": 9, "br": 15, "to": 15, "th": 6}[c]
    out = ""
    for sx in (-1, 1):
        x = sx * fx
        out += (f'<path d="M{x - w*0.7:.1f} {-w*1.8:.1f} H{x + w*0.7:.1f} V{-w*0.3:.1f} Q{x + w*1.2:.1f} {-w*0.3:.1f} {x + w*1.2:.1f} 1 '
                f'H{x - w*1.2:.1f} Q{x - w*1.2:.1f} {-w*0.3:.1f} {x - w*0.7:.1f} {-w*0.3:.1f} Z" stroke-width="{1.6/s:.2f}"/>'
                f'<path d="M{x - w*0.7:.1f} {-w*1.4:.1f} H{x + w*0.7:.1f}" fill="none" stroke-width="{1/s:.2f}"/>')
    return out


def raincoat(c):
    """Raincoat pattern for the sweater system: placket, toggles, pockets."""
    from chars import TORSO_BOX
    x0, y0, x1, y1 = TORSO_BOX[c]
    h = y1 - y0
    out = f'<path d="M0 {y0} V{y1 + 4}" stroke-width="1.1"/>'
    for k in range(3):
        yy = y0 + h * (0.28 + 0.22 * k)
        out += f'<rect x="-4" y="{yy - 1.6:.1f}" width="8" height="3.2" rx="1.2" stroke-width="0.9"/>'
    out += (f'<rect x="{x0 + (x1 - x0)*0.14:.1f}" y="{y0 + h*0.55:.1f}" width="{(x1 - x0)*0.22:.1f}" height="{h*0.18:.1f}" rx="2" stroke-width="0.9"/>'
            f'<rect x="{x1 - (x1 - x0)*0.36:.1f}" y="{y0 + h*0.55:.1f}" width="{(x1 - x0)*0.22:.1f}" height="{h*0.18:.1f}" rx="2" stroke-width="0.9"/>')
    return out


def splash(x, y, s=1.0):
    return (f'<path transform="translate({x} {y}) scale({s})" d="M-16 0 L-12 -10 L-7 -2 L-3 -14 L1 -3 L6 -13 L8 -2 L13 -9 L16 0 Z" stroke-width="{1.2/s:.2f}"/>')


def puddle(x, y, rx, ry):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" stroke-width="1.6"/>'
            f'<ellipse cx="{x + rx*0.1:.1f}" cy="{y}" rx="{rx*0.55:.1f}" ry="{ry*0.5:.1f}" stroke-width="1.1"/>')


def cobbles(x0, y0, x1, y1, w=46, h=24):
    out = ""
    r = 0
    y = y0
    while y < y1:
        off = (w / 2) if r % 2 else 0
        x = x0 - w + off
        while x < x1:
            out += f'<rect x="{x + 2:.1f}" y="{y + 2:.1f}" width="{w - 4}" height="{h - 4}" rx="9" stroke-width="1.1"/>'
            x += w
        y += h
        r += 1
    return out


def _bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3 * p0[0] + 3*u*u*t * p1[0] + 3*u*t*t * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3*u*u*t * p1[1] + 3*u*t*t * p2[1] + t**3 * p3[1])


def ribbon(curves, w=30, seg=16, bands=("stripes", "zigzag", "hearts"), band_len=5, sw=1.8):
    """Knitted scarf along cubic curves [(p0,p1,p2,p3), ...]: closed segments with banded patterns."""
    pts = []
    for (p0, p1, p2, p3) in curves:
        for k in range(seg):
            pts.append(_bez(p0, p1, p2, p3, k / seg))
    pts.append(curves[-1][3])
    left, right = [], []
    for i, (x, y) in enumerate(pts):
        a = pts[max(i - 1, 0)]
        c = pts[min(i + 1, len(pts) - 1)]
        dx, dy = c[0] - a[0], c[1] - a[1]
        L = (dx * dx + dy * dy) ** 0.5 or 1
        nx, ny = -dy / L * w / 2, dx / L * w / 2
        left.append((x + nx, y + ny))
        right.append((x - nx, y - ny))
    out = []
    for i in range(len(pts) - 1):
        quad = f"M{left[i][0]:.1f} {left[i][1]:.1f} L{left[i+1][0]:.1f} {left[i+1][1]:.1f} L{right[i+1][0]:.1f} {right[i+1][1]:.1f} L{right[i][0]:.1f} {right[i][1]:.1f} Z"
        band = bands[(i // band_len) % len(bands)]
        out.append(f'<path d="{quad}" stroke-width="1.1"/>')
        cx = (left[i][0] + right[i+1][0]) / 2
        cy = (left[i][1] + right[i+1][1]) / 2
        if band == "zigzag":
            m1 = ((left[i][0] + right[i][0]) / 2, (left[i][1] + right[i][1]) / 2)
            m2 = ((left[i+1][0] + right[i+1][0]) / 2, (left[i+1][1] + right[i+1][1]) / 2)
            out.append(lines(f"M{(left[i][0]*0.7 + right[i][0]*0.3):.1f} {(left[i][1]*0.7 + right[i][1]*0.3):.1f} "
                             f"L{(m1[0] + m2[0])/2*1 + 0:.1f} {(m1[1] + m2[1])/2:.1f} "
                             f"L{(left[i+1][0]*0.7 + right[i+1][0]*0.3):.1f} {(left[i+1][1]*0.7 + right[i+1][1]*0.3):.1f}", 0.8))
        elif band == "hearts" and i % 2 == 0:
            out.append(f'<use href="#heart" transform="translate({cx:.1f} {cy:.1f}) scale({w/44:.2f})" stroke-width="{44/w:.2f}"/>')
        elif band == "stripes":
            out.append(lines(f"M{(left[i][0] + left[i+1][0])/2:.1f} {(left[i][1] + left[i+1][1])/2:.1f} L{(right[i][0] + right[i+1][0])/2:.1f} {(right[i][1] + right[i+1][1])/2:.1f}", 0.8))
    edge = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in left) + " M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in right)
    out.append(f'<path d="{edge}" fill="none" stroke-width="{sw}"/>')
    (ex, ey), (fx, fy) = left[-1], right[-1]
    out.append(lines(" ".join(f"M{ex + (fx - ex)*k/5:.1f} {ey + (fy - ey)*k/5:.1f} l{(pts[-1][0] - pts[-2][0])*0.8:.1f} {(pts[-1][1] - pts[-2][1])*0.8:.1f}" for k in range(1, 5)), 1.3))
    return "".join(out)


def yarn_ball(x, y, r=16):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" stroke-width="1.7"/>'
            + lines(f"M{x - r*0.8:.1f} {y - r*0.4:.1f} Q{x} {y - r*0.1:.1f} {x + r*0.7:.1f} {y + r*0.6:.1f} "
                    f"M{x - r*0.5:.1f} {y - r*0.85:.1f} Q{x + r*0.2:.1f} {y - r*0.3:.1f} {x + r*0.9:.1f} {y + r*0.1:.1f} "
                    f"M{x - r*0.9:.1f} {y + r*0.2:.1f} Q{x - r*0.1:.1f} {y + r*0.4:.1f} {x + r*0.3:.1f} {y + r*0.9:.1f}", 1.0))


def cupcake(x, y, s=1.0, top="swirl"):
    """Cupcake with pleated liner, base centre (x, y), ~44 tall at s=1."""
    liner = "M-16 -22 H16 L12 0 H-12 Z"
    pleats = " ".join(f"M{-14 + k*4} -22 L{-11 + k*3.1:.1f} 0" for k in range(1, 8))
    out = f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" stroke-width="{1.5/s:.2f}">'
    out += clip_d(liner, f'<path d="{pleats}" fill="none" stroke-width="{0.9/s:.2f}"/>', 1.5 / s)
    out += ('<path d="M-19 -22 Q-22 -32 -12 -34 Q-12 -44 0 -44 Q12 -44 12 -34 Q22 -32 19 -22 Q0 -18 -19 -22 Z"/>'
            '<path d="M-14 -34 Q0 -30 14 -34" fill="none" stroke-width="1"/>')
    if top == "swirl":
        out += '<path d="M-10 -42 Q-10 -52 0 -52 Q10 -52 10 -42 Q0 -38 -10 -42 Z"/><path d="M-4 -52 Q0 -60 4 -52 Z"/>'
    elif top == "berry":
        out += ('<path d="M0 -40 C-9 -44 -9 -54 -3 -56 Q0 -57 3 -56 C9 -54 9 -44 0 -40 Z"/>'
                '<path d="M-4 -56 L0 -61 L4 -56" fill="none"/><circle cx="-2" cy="-49" r="0.8" fill="#000" stroke="none"/><circle cx="3" cy="-47" r="0.8" fill="#000" stroke="none"/>')
    elif top == "cherry":
        out += '<circle cy="-48" r="6"/><path d="M0 -54 Q2 -62 8 -64" fill="none"/>'
    elif top == "flower":
        out += "".join(f'<circle cx="0" cy="-48" r="3.6" transform="rotate({a} 0 -44)"/>' for a in range(0, 360, 72)) + '<circle cy="-44" r="2.4"/>'
    elif top == "sprinkles":
        out += "".join(f'<rect x="{dx}" y="{dy}" width="5" height="2" rx="1" transform="rotate({r} {dx} {dy})" stroke-width="0.8"/>' for dx, dy, r in ((-10, -34, 30), (4, -38, -20), (-2, -42, 60), (8, -30, 10), (-6, -28, -40)))
    elif top == "flag":
        out += '<path d="M2 -40 V-62" fill="none"/><path d="M2 -62 L16 -57 L2 -52 Z"/>' + '<use href="#heart" transform="translate(8 -57) scale(0.28)" stroke-width="3"/>'
    elif top == "blueberry":
        out += '<circle cx="-5" cy="-44" r="4.5"/><circle cx="5" cy="-44" r="4.5"/><circle cx="0" cy="-50" r="4.5"/>'
    return out + "</g>"


def shaker(x, y, ico="star"):
    return (f'<path d="M{x - 12} {y} V{y - 34} Q{x} {y - 40} {x + 12} {y - 34} V{y} Z" stroke-width="1.6"/>'
            f'<path d="M{x - 12} {y - 34} Q{x - 12} {y - 48} {x} {y - 48} Q{x + 12} {y - 48} {x + 12} {y - 34}" stroke-width="1.6"/>'
            f'<circle cx="{x - 4}" cy="{y - 42}" r="1.2" fill="#000" stroke="none"/><circle cx="{x + 4}" cy="{y - 42}" r="1.2" fill="#000" stroke="none"/>'
            + icon(ico, x, y - 16, 0.5, 1))


def chef_hat(x, y, s=1.0):
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" stroke-width="{1.7/s:.2f}">'
            '<path d="M-26 0 V-14 Q-40 -18 -36 -34 Q-30 -48 -14 -42 Q-8 -58 8 -52 Q24 -56 28 -40 Q42 -34 34 -18 Q30 -14 26 -14 V0 Z"/>'
            '<path d="M-26 -10 H26" fill="none" stroke-width="1.1"/><path d="M-8 -14 V-30 M8 -14 V-32" fill="none" stroke-width="0.9"/></g>')


def scarf(x, y, w, s=1.0, tail=1):
    """Short striped winter scarf around a neck centred at (x, y) on the page."""
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" stroke-width="{1.5/s:.2f}">'
            f'<path d="M{-w/2} -6 Q0 2 {w/2} -6 L{w/2} 4 Q0 12 {-w/2} 4 Z"/>'
            f'<path d="M{tail*w*0.25:.1f} 2 L{tail*w*0.3:.1f} 34 L{tail*w*0.3 + tail*12:.1f} 34 L{tail*w*0.25 + tail*12:.1f} 2 Z"/>'
            f'<path d="M{tail*w*0.27:.1f} 14 L{tail*w*0.27 + tail*12:.1f} 14 M{tail*w*0.28:.1f} 24 L{tail*w*0.28 + tail*12:.1f} 24" fill="none" stroke-width="{0.9/s:.2f}"/>'
            f'<path d="M{-w*0.25:.1f} -4 V6 M0 -2 V8 M{w*0.25:.1f} -4 V6" fill="none" stroke-width="{0.9/s:.2f}"/></g>')
