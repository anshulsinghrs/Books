"""Reusable scenery pieces (page units). All return closed, colourable shapes."""
from math import sin, cos, radians, pi, degrees, atan2

_cid = [0]


def uid(prefix="c"):
    _cid[0] += 1
    return f"{prefix}{_cid[0]}"


def clip_d(d, inner, sw=1.5, fill="none"):
    """Closed path `d` with `inner` lines clipped to it, outline redrawn on top."""
    i = uid("k")
    return (f'<clipPath id="{i}"><path d="{d}"/></clipPath><path d="{d}" stroke-width="{sw}"/>'
            f'<g clip-path="url(#{i})" fill="{fill}">{inner}</g><path d="{d}" fill="none" stroke-width="{sw}"/>')


def daisy(x, y, r=12, n=7, sw=1.1):
    pet = []
    for k in range(n):
        a = 360 * k / n
        pet.append(f'<ellipse cx="0" cy="{-r*0.62:.1f}" rx="{r*0.3:.1f}" ry="{r*0.45:.1f}" transform="rotate({a:.1f})"/>')
    return (f'<g transform="translate({x} {y})" stroke-width="{sw}">' + "".join(pet)
            + f'<circle r="{r*0.33:.1f}"/></g>')


def tulip(x, y, h=30, lean=0, s=1.0, leaf=True):
    tx, ty = x + lean, y - h
    out = f'<path d="M{x} {y} Q{x + lean*0.2} {y - h*0.5} {tx} {ty}" fill="none" stroke-width="1.1"/>'
    if leaf:
        lx = -1 if lean >= 0 else 1
        out += (f'<path d="M{x} {y} Q{x + lx*12*s} {y - h*0.45} {x + lx*4*s} {y - h*0.75} '
                f'Q{x + lx*2*s} {y - h*0.35} {x} {y} Z" stroke-width="1"/>')
    out += (f'<path transform="translate({tx} {ty}) scale({s})" d="M-6 1 Q-7.5 -8 -5 -13 L-2.2 -8.5 L0 -14 '
            f'L2.2 -8.5 L5 -13 Q7.5 -8 6 1 Q0 4.5 -6 1 Z" stroke-width="1.2"/>')
    return out


def tuft(x, y, s=1.0):
    return (f'<path transform="translate({x} {y}) scale({s})" d="M-8 0 Q-6 -6 -9 -11 M-3 0 Q-2 -9 -4 -15 '
            f'M2 0 Q3 -8 7 -12 M6 0 Q8 -4 11 -6" fill="none" stroke-width="1"/>')


def cottage_small(x, y, w=22, s=1.0):
    """Tiny distant cottage, base centre at (x, y)."""
    h = w * 0.62
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="1.1">'
            f'<rect x="{-w/2}" y="{-h}" width="{w}" height="{h}"/>'
            f'<path d="M{-w/2-3} {-h} L0 {-h-w*0.55} L{w/2+3} {-h} Z"/>'
            f'<rect x="{-w*0.12}" y="{-h*0.6}" width="{w*0.24}" height="{h*0.6}"/></g>')


def ray(cx, cy, ang, r1, r2, half=5.5):
    a = radians(ang)
    ux, uy = sin(a), -cos(a)
    px, py = -uy, ux
    x1, y1 = cx + ux*r1 + px*half, cy + uy*r1 + py*half
    x2, y2 = cx + ux*r1 - px*half, cy + uy*r1 - py*half
    tx, ty = cx + ux*r2, cy + uy*r2
    return f'<path d="M{x1:.1f} {y1:.1f} L{tx:.1f} {ty:.1f} L{x2:.1f} {y2:.1f} Z" stroke-width="1.25"/>'


def stone_grid(x0, y0, w, h, row_h, pattern, sw=1.0, rx=4):
    """Irregular stone courses filling a rectangle (stones share edges)."""
    out = []
    y = y0
    r = 0
    while y < y0 + h - 0.1:
        rh = min(row_h, y0 + h - y)
        widths = pattern[r % len(pattern)]
        x = x0
        k = 0
        while x < x0 + w - 0.1:
            sw_ = widths[k % len(widths)]
            ww = min(sw_, x0 + w - x)
            out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{ww:.1f}" height="{rh:.1f}" rx="{rx}" stroke-width="{sw}"/>')
            x += ww
            k += 1
        y += rh
        r += 1
    return "".join(out)


def picket_fence(x0, x1, top, base, pw=16, gap=12, rails=((0.3, 10), (0.68, 10))):
    out = []
    hgt = base - top
    for fr, rh in rails:
        ry = top + hgt * fr
        out.append(f'<rect x="{x0-4}" y="{ry:.1f}" width="{x1-x0+8}" height="{rh}" stroke-width="1.25"/>')
    x = x0
    while x + pw <= x1 + 0.1:
        out.append(f'<path d="M{x} {base} V{top+10} L{x+pw/2} {top} L{x+pw} {top+10} V{base} Z" stroke-width="1.5"/>')
        x += pw + gap
    return "".join(out)


def scallop_blob(cx, cy, rx, ry, n=9, bump=0.28, sw=1.5):
    """A closed bumpy outline (bush, tree canopy, cloud)."""
    pts = []
    for k in range(n):
        a = 2*pi*k/n - pi/2
        pts.append((cx + rx*cos(a), cy + ry*sin(a)))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f} "
    for k in range(n):
        x1, y1 = pts[k]
        x2, y2 = pts[(k+1) % n]
        mx, my = (x1+x2)/2, (y1+y2)/2
        ox, oy = mx - cx, my - cy
        L = (ox*ox+oy*oy) ** 0.5 or 1
        bx, by = mx + ox/L*bump*min(rx, ry), my + oy/L*bump*min(rx, ry)
        d += f"Q{bx:.1f} {by:.1f} {x2:.1f} {y2:.1f} "
    return f'<path d="{d}Z" stroke-width="{sw}"/>'


def lines(d, sw=1.0):
    return f'<path d="{d}" fill="none" stroke-width="{sw}"/>'


def blossom(x, y, r=9, sw=1.1, rot=0):
    """Five-petal blossom (spring)."""
    pet = "".join(f'<circle cx="0" cy="{-r*0.55:.1f}" r="{r*0.48:.1f}" transform="rotate({72*k})"/>' for k in range(5))
    return (f'<g transform="translate({x} {y}) rotate({rot})" stroke-width="{sw}">{pet}'
            f'<circle r="{r*0.3:.1f}"/></g>')


def branch(d_center, width_pts):
    """Unused placeholder kept for API symmetry."""
    return ""


def pine(x, tiers, sw=1.6, teeth=5):
    """Tiered pine. tiers = [(y_apex, y_bottom, half_width), ...] drawn bottom tier first."""
    out = []
    for (ya, yb, hw) in sorted(tiers, key=lambda t: -t[1]):
        d = f"M{x} {ya} L{x + hw} {yb} "
        for k in range(teeth):
            xr = x + hw - 2 * hw * k / teeth
            xl = x + hw - 2 * hw * (k + 1) / teeth
            d += f"Q{(xr + xl) / 2:.1f} {yb - 9:.1f} {xl:.1f} {yb} "
        d += "Z"
        out.append(f'<path d="{d}" stroke-width="{sw}"/>')
    return "".join(out)


OAK_LEAF = ("M0 0 C-4 -3 -10 -3 -8 -8 C-13 -10 -11 -16 -6 -15 C-9 -21 -4 -26 0 -22 "
            "C4 -26 9 -21 6 -15 C11 -16 13 -10 8 -8 C10 -3 4 -3 0 0 Z")


def oak_leaf(x, y, rot=0, s=1.0, sw=1.1):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{sw/s:.2f}">'
            f'<path d="{OAK_LEAF}"/><path d="M0 3 V-19" fill="none" stroke-width="{0.8/s:.2f}"/></g>')


def fern(x, y, length=90, ang=-10, curve=18, n=7, leaf=10, sw=1.1):
    """Fern frond: curved stem with paired leaflets (closed ellipses)."""
    out = []
    a = radians(ang)
    ux, uy = sin(a), -cos(a)
    px, py = cos(a), sin(a)
    ex, ey = x + ux * length + px * curve, y + uy * length + py * curve
    cx, cy = x + ux * length * 0.5 + px * curve * 0.2, y + uy * length * 0.5 + py * curve * 0.2
    out.append(f'<path d="M{x} {y} Q{cx:.1f} {cy:.1f} {ex:.1f} {ey:.1f}" fill="none" stroke-width="{sw+0.2}"/>')
    for k in range(1, n + 1):
        t = k / (n + 1)
        bx = (1-t)**2 * x + 2*(1-t)*t*cx + t*t*ex
        by = (1-t)**2 * y + 2*(1-t)*t*cy + t*t*ey
        tx = 2*(1-t)*(cx - x) + 2*t*(ex - cx)
        ty = 2*(1-t)*(cy - y) + 2*t*(ey - cy)
        tl = (tx*tx + ty*ty) ** 0.5
        tx, ty = tx/tl, ty/tl
        size = leaf * (1.1 - 0.6 * t)
        deg = __import__("math").degrees(__import__("math").atan2(ty, tx))
        for side in (-1, 1):
            ox, oy = -ty * side * size * 0.75, tx * side * size * 0.75
            out.append(f'<ellipse cx="{bx+ox:.1f}" cy="{by+oy:.1f}" rx="{size*0.85:.1f}" ry="{size*0.38:.1f}" '
                       f'transform="rotate({deg + side*55:.1f} {bx+ox:.1f} {by+oy:.1f})" stroke-width="{sw}"/>')
    out.append(f'<ellipse cx="{ex:.1f}" cy="{ey:.1f}" rx="{leaf*0.35:.1f}" ry="{leaf*0.25:.1f}" stroke-width="{sw}"/>')
    return "".join(out)


def foxglove(x, y, h=120, sw=1.1):
    out = [f'<path d="M{x} {y} Q{x+4} {y-h*0.5} {x} {y-h}" fill="none" stroke-width="{sw+0.3}"/>']
    out.append(f'<path d="M{x} {y} Q{x-18} {y-16} {x-22} {y-34} Q{x-6} {y-24} {x} {y} Z" stroke-width="{sw}"/>')
    out.append(f'<path d="M{x} {y-8} Q{x+18} {y-22} {x+22} {y-40} Q{x+6} {y-30} {x} {y-8} Z" stroke-width="{sw}"/>')
    n = 6
    for k in range(n):
        yy = y - h * 0.35 - k * (h * 0.6 / n)
        side = -1 if k % 2 else 1
        s = 1.0 - k * 0.09
        bx = x + side * 5
        out.append(f'<path transform="translate({bx} {yy:.1f}) scale({side*s:.2f} {s:.2f})" '
                   f'd="M0 -5 Q12 -7 14 4 Q10 9 6 6 Q3 10 0 6 Z" stroke-width="{sw/s:.2f}"/>')
    out.append(f'<circle cx="{x}" cy="{y-h-3}" r="3" stroke-width="{sw}"/>')
    return "".join(out)


def mushroom(x, y, s=1.0, sw=1.3, spots=True):
    out = (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{sw/s:.2f}">'
           f'<path d="M-6 0 Q-7 -12 -5 -18 H5 Q7 -12 6 0 Z"/>'
           f'<path d="M-17 -16 Q-16 -34 0 -35 Q16 -34 17 -16 Q0 -12 -17 -16 Z"/>')
    if spots:
        out += '<circle cx="-7" cy="-25" r="3"/><circle cx="5" cy="-28" r="2.6"/><circle cx="10" cy="-20" r="2"/>'
    return out + "</g>"


def pumpkin(x, y, w=60, h=44, sw=1.6, stem=True):
    """Ribbed pumpkin, base centre at (x, y)."""
    cy = y - h / 2
    out = [f'<ellipse cx="{x - w*0.28:.1f}" cy="{cy:.1f}" rx="{w*0.26:.1f}" ry="{h*0.48:.1f}" stroke-width="{sw}"/>',
           f'<ellipse cx="{x + w*0.28:.1f}" cy="{cy:.1f}" rx="{w*0.26:.1f}" ry="{h*0.48:.1f}" stroke-width="{sw}"/>',
           f'<ellipse cx="{x}" cy="{cy:.1f}" rx="{w*0.3:.1f}" ry="{h*0.5:.1f}" stroke-width="{sw}"/>']
    if stem:
        out.append(f'<path d="M{x-3} {y-h+3:.1f} Q{x-4} {y-h-10:.1f} {x+2} {y-h-12:.1f} L{x+5} {y-h-9:.1f} Q{x+2} {y-h-4:.1f} {x+3} {y-h+3:.1f} Z" stroke-width="{sw*0.85:.2f}"/>')
        out.append(f'<path d="M{x+4} {y-h-4:.1f} q8 -6 12 2 q-6 4 -12 -2 Z" stroke-width="{sw*0.7:.2f}"/>')
    return "".join(out)


def gourd(x, y, s=1.0, rot=0, sw=1.4):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{sw/s:.2f}">'
            f'<path d="M-14 0 Q-16 -14 -6 -18 Q-6 -30 0 -32 Q6 -30 6 -18 Q16 -14 14 0 Q0 6 -14 0 Z"/>'
            f'<path d="M0 -32 V-38" fill="none"/><path d="M-8 -14 Q0 -10 8 -14" fill="none" stroke-width="{0.9/s:.2f}"/></g>')
