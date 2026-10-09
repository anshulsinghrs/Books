"""Cozy Little Friends — Volume 1 front cover (8.5 x 11 in, front cover only).

The friends are the book's own character parts (src/chars.py), reused
unchanged: this file only adds fill colours to a copy of the shared <defs>
and places the cast with chars.char(). Text is set from the bundled OFL fonts
(cover/fonts) and converted to outlines, so the print SVG never depends on
installed fonts. A second, editable SVG keeps the text live with the fonts
embedded.

Series system (reuse for Volumes 2 and 3): same title lock-up, top "VOLUME n"
stitched tab, honey "50 Coloring Illustrations" rosette, quilt-patch strip
along the bottom with BOOKSHELF beneath it, stitched inner border.

usage: python3 cover.py   -> out/cover-front-v1.svg (trim, outlined text),
       out/cover-front-v1-editable.svg (live text, fonts embedded),
       out/cover-front-v1-bleed.svg (same art + 0.125 in bleed all round)
"""
import base64
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "src"))
sys.path.insert(0, HERE)

import chars  # noqa: E402
from chars import DEFS, char  # noqa: E402
from textpath import text_path, text_width  # noqa: E402

W, H = 612, 792
SAFE = 27  # 0.375 in: all text and key art stays inside this inset

# ------------------------------------------------------------------ palette
INK = "#3B2F2C"        # warm dark line
CREAM = "#FBF3E3"
IVORY = "#FFFBF2"
SAGE = "#8FAE88"
FOREST = "#3E6B4E"
ROSE = "#D98C8E"
BLUSH = "#EBA9A4"
TERRA = "#C9785A"
TERRA_D = "#A6553A"
HONEY = "#E9B949"
POWDER = "#9DC0DA"
LAV = "#B9AFCF"
AUTUMN = "#E08A3C"
GRASS = "#A9C59A"
GRASS_D = "#8FB27F"

FUR = {"br": "#A8754E", "cl": "#F1E6D6", "mi": "#E6A564", "ju": "#D9804A",
       "pi": "#F2DFC1", "to": "#FBF8F2", "pb": "#8C6650", "th": "#BDB5C8"}
DOT_BROWN = "#A5714F"
PANDA = "#55505E"

# ------------------------------------------------- coloured copy of the defs
# (old substring, new substring). Every substring must exist in DEFS; shapes
# and ids are untouched, only fill attributes / filled underlays are added.
JU_MASK = "M-46 2 Q-24 0 -12 8 Q-6 12 0 10 Q6 12 12 8 Q24 0 46 2"
COLOR = [
    ('fill="#000"', 'fill="#2A2220"'),
    ('stroke="#000"', 'stroke="#2A2220"'),
    ('<ellipse id="blush" rx="5.5" ry="3.2" stroke-width="0.8"/>',
     f'<ellipse id="blush" rx="5.5" ry="3.2" fill="{BLUSH}" stroke="none"/>'),
    # Dot
    ('<g id="dot">', f'<g id="dot" fill="{DOT_BROWN}">'),
    ('<g id="dot-sleep">', f'<g id="dot-sleep" fill="{DOT_BROWN}">'),
    ('<path d="M9.3 -5.6 L13.2 -4.4 L9.3 -3 Z" stroke-width="0.9"/>',
     f'<path d="M9.3 -5.6 L13.2 -4.4 L9.3 -3 Z" fill="{HONEY}" stroke-width="0.9"/>'),
    # Bramble: sage knitted vest, cream V, honey acorn pin
    ('<circle r="7.5" stroke-width="1"/>', '<circle r="7.5" fill="#E9C6A6" stroke-width="1"/>'),
    ('<ellipse cy="12" rx="17" ry="12.5" stroke-width="1.25"/>',
     '<ellipse cy="12" rx="17" ry="12.5" fill="#EED8BC" stroke-width="1.25"/>'),
    ('<g id="br-torso">\n  <use href="#br-tp"/>\n  <g clip-path="url(#br-tc)" fill="none">',
     f'<g id="br-torso">\n  <use href="#br-tp" fill="{SAGE}"/>\n  <g clip-path="url(#br-tc)" fill="none">'
     f'<path d="M-60 -47 Q0 -36 60 -47 V0 H-60 Z" fill="{FUR["br"]}" stroke="none"/>'),
    ('<path d="M-14 -112 L0 -74 L14 -112" stroke-width="1.25"/>',
     f'<path d="M-14 -112 L0 -74 L14 -112 Z" fill="{FUR["br"]}" stroke-width="1.25"/>'),
    ('<g id="br-torso-back">\n  <use href="#br-tp"/>', f'<g id="br-torso-back">\n  <use href="#br-tp" fill="{SAGE}"/>'),
    ('<ellipse cy="4" rx="5" ry="6"/><path d="M-6.5 0.5 Q0 -8 6.5 0.5 Z"/>',
     f'<ellipse cy="4" rx="5" ry="6" fill="{HONEY}"/><path d="M-6.5 0.5 Q0 -8 6.5 0.5 Z" fill="#8A5A3A"/>'),
    # Clover: pink inner ears, green clover clip, cream belly, white tail
    ('<path d="M-15 -32 C-21 -54 -19 -70 -14 -72 C-9 -70 -8 -54 -10 -34 Z" stroke-width="1"/>',
     f'<path d="M-15 -32 C-21 -54 -19 -70 -14 -72 C-9 -70 -8 -54 -10 -34 Z" fill="{BLUSH}" stroke-width="1"/>'),
    ('<path d="M10 -32 C8 -46 10 -58 16 -62 C18 -54 17 -42 16 -32 Z" stroke-width="1"/>',
     f'<path d="M10 -32 C8 -46 10 -58 16 -62 C18 -54 17 -42 16 -32 Z" fill="{BLUSH}" stroke-width="1"/>'),
    ('<g transform="translate(33 -61)" stroke-width="0.9">', '<g transform="translate(33 -61)" stroke-width="0.9" fill="#7DA66E">'),
    ('<ellipse cy="-32" rx="13" ry="15" stroke-width="1"/>', f'<ellipse cy="-32" rx="13" ry="15" fill="{IVORY}" stroke-width="1"/>'),
    ('<g id="cl-tail">', f'<g id="cl-tail" fill="{IVORY}">'),
    # Miso: pink inner ears, cream belly, powder-blue collar, gold fish charm
    ('<path d="M-28 -20 Q-30 -32 -27 -34 Q-21 -31 -17 -26 Z" stroke-width="1"/>',
     f'<path d="M-28 -20 Q-30 -32 -27 -34 Q-21 -31 -17 -26 Z" fill="{BLUSH}" stroke-width="1"/>'),
    ('<path d="M28 -20 Q30 -32 27 -34 Q21 -31 17 -26 Z" stroke-width="1"/>',
     f'<path d="M28 -20 Q30 -32 27 -34 Q21 -31 17 -26 Z" fill="{BLUSH}" stroke-width="1"/>'),
    ('<ellipse cy="-20" rx="11" ry="12" stroke-width="1"/>', f'<ellipse cy="-20" rx="11" ry="12" fill="{IVORY}" stroke-width="1"/>'),
    ('<path d="M-17 -44 Q0 -37 17 -44 L17 -39 Q0 -32 -17 -39 Z" stroke-width="1.2"/>',
     f'<path d="M-17 -44 Q0 -37 17 -44 L17 -39 Q0 -32 -17 -39 Z" fill="{POWDER}" stroke-width="1.2"/>'),
    ('<circle cy="-34" r="1.4" stroke-width="0.8"/>', '<circle cy="-34" r="1.4" fill="#F2D06B" stroke-width="0.8"/>'),
    ('<g transform="translate(0 -29)" stroke-width="0.9">', '<g transform="translate(0 -29)" stroke-width="0.9" fill="#F2D06B">'),
    # Juniper: cream muzzle, bib and tail tip, dark ear tips and paws, rose scarf
    (f'<path clip-path="url(#ju-hc)" d="{JU_MASK}" fill="none" stroke-width="1.25"/>',
     f'<path clip-path="url(#ju-hc)" d="{JU_MASK} V60 H-46 Z" fill="{IVORY}" stroke="none"/>'
     f'<path clip-path="url(#ju-hc)" d="{JU_MASK}" fill="none" stroke-width="1.25"/>'),
    ('<path d="M-34.7 -48 L-24.3 -48" fill="none" stroke-width="1.25"/>',
     '<path d="M-34.7 -48 L-34 -58 Q-33 -60 -31 -58 L-24.3 -48 Z" fill="#5A3B2E" stroke-width="1.25"/>'),
    ('<path d="M34.7 -48 L24.3 -48" fill="none" stroke-width="1.25"/>',
     '<path d="M34.7 -48 L34 -58 Q33 -60 31 -58 L24.3 -48 Z" fill="#5A3B2E" stroke-width="1.25"/>'),
    ('<path d="M-32 -20 L-31.5 -42 L-19 -27 Z" stroke-width="1"/>', f'<path d="M-32 -20 L-31.5 -42 L-19 -27 Z" fill="{IVORY}" stroke-width="1"/>'),
    ('<path d="M32 -20 L31.5 -42 L19 -27 Z" stroke-width="1"/>', f'<path d="M32 -20 L31.5 -42 L19 -27 Z" fill="{IVORY}" stroke-width="1"/>'),
    ('<path clip-path="url(#ju-tailc)" d="M36 -86 Q52 -80 72 -86" fill="none" stroke-width="1.25"/>',
     f'<path clip-path="url(#ju-tailc)" d="M36 -86 Q52 -80 72 -86 V-120 H36 Z" fill="{IVORY}" stroke="none"/>'
     '<path clip-path="url(#ju-tailc)" d="M36 -86 Q52 -80 72 -86" fill="none" stroke-width="1.25"/>'),
    ('<path clip-path="url(#ju-tc)" d="M-26 -76 L-17 -50',
     f'<path clip-path="url(#ju-tc)" d="M-26 -76 L-17 -50 L-11 -56 L-5 -44 L0 -50 L5 -44 L11 -56 L17 -50 L26 -76 '
     f'L26 -90 L-26 -90 Z" fill="{IVORY}" stroke="none"/><path clip-path="url(#ju-tc)" d="M-26 -76 L-17 -50'),
    ('<g id="ju-scarf" stroke-width="1.2">', f'<g id="ju-scarf" stroke-width="1.2" fill="{ROSE}">'),
    ('<g id="ju-knot-back" stroke-width="1.2">', f'<g id="ju-knot-back" stroke-width="1.2" fill="{ROSE}">'),
    ('<g stroke-width="1.2"><path d="M-21 -80 Q0 -72', f'<g stroke-width="1.2" fill="{ROSE}"><path d="M-21 -80 Q0 -72'),
    ('<g id="ju-feet">', '<g id="ju-feet" fill="#5A3B2E">'),
    ('<g id="ju-feet-sit">', '<g id="ju-feet-sit" fill="#5A3B2E">'),
    # Pip: brown ears, eye patch and back spot, white muzzle, rose hat
    ('<path d="M-30 -20 C-46 -16 -50 10 -44 28 C-40 36 -32 32 -30 22 C-28 10 -26 -6 -24 -16 Z"/>',
     '<path d="M-30 -20 C-46 -16 -50 10 -44 28 C-40 36 -32 32 -30 22 C-28 10 -26 -6 -24 -16 Z" fill="#B98A5F"/>'),
    ('<path d="M30 -20 C46 -16 50 10 44 28 C40 36 32 32 30 22 C28 10 26 -6 24 -16 Z"/>',
     '<path d="M30 -20 C46 -16 50 10 44 28 C40 36 32 32 30 22 C28 10 26 -6 24 -16 Z" fill="#B98A5F"/>'),
    ('<path d="M-23 8 C-23 0 -12 -2 -6 3 C-1 9 -3 18 -11 20 C-19 22 -23 15 -23 8 Z" stroke-width="1.25"/>',
     '<path d="M-23 8 C-23 0 -12 -2 -6 3 C-1 9 -3 18 -11 20 C-19 22 -23 15 -23 8 Z" fill="#B98A5F" stroke-width="1.25"/>'),
    ('<ellipse cy="24" rx="12" ry="8.5" stroke-width="1.25"/>', f'<ellipse cy="24" rx="12" ry="8.5" fill="{IVORY}" stroke-width="1.25"/>'),
    ('<path d="M4 -16 C4 -24 16 -25 18 -17 C19 -9 8 -7 4 -16 Z" stroke-width="1.2"/>',
     '<path d="M4 -16 C4 -24 16 -25 18 -17 C19 -9 8 -7 4 -16 Z" fill="#B98A5F" stroke-width="1.2"/>'),
    ('<g id="pi-hat">\n  <use href="#pi-domep"/>\n  <g clip-path="url(#pi-domec)" fill="none" stroke-width="1.25">',
     f'<g id="pi-hat">\n  <use href="#pi-domep" fill="{ROSE}"/>\n  <g clip-path="url(#pi-domec)" fill="none" stroke-width="1.25">'
     f'<path d="M-40 -20 Q0 -26 40 -20 L40 -32 Q0 -38 -40 -32 Z" fill="{IVORY}" stroke="none"/>'),
    ('<path d="M-39 -12 Q0 -18 39 -12 L39 -1 Q0 -7 -39 -1 Z"/>', f'<path d="M-39 -12 Q0 -18 39 -12 L39 -1 Q0 -7 -39 -1 Z" fill="{SAGE}"/>'),
    ('<use href="#scallop" transform="translate(0 -52)"/>', '<use href="#scallop" transform="translate(0 -52)" fill="#EBC35E"/>'),
    # Tofu: panda markings, honey crescent pendant
    ('<circle cx="-36" cy="-34" r="13"/><circle cx="36" cy="-34" r="13"/>',
     f'<circle cx="-36" cy="-34" r="13" fill="{PANDA}"/><circle cx="36" cy="-34" r="13" fill="{PANDA}"/>'),
    ('<path d="M-10 -10 C-4 -4 -8 10 -18 14 C-28 18 -32 8 -28 0 C-24 -8 -16 -14 -10 -10 Z" stroke-width="1.25"/>',
     '<path d="M-10 -10 C-4 -4 -8 10 -18 14 C-28 18 -32 8 -28 0 C-24 -8 -16 -14 -10 -10 Z" fill="#7A7484" stroke-width="1.25"/>'),
    ('<path d="M10 -10 C4 -4 8 10 18 14 C28 18 32 8 28 0 C24 -8 16 -14 10 -10 Z" stroke-width="1.25"/>',
     '<path d="M10 -10 C4 -4 8 10 18 14 C28 18 32 8 28 0 C24 -8 16 -14 10 -10 Z" fill="#7A7484" stroke-width="1.25"/>'),
    ('<path clip-path="url(#to-tc)" d="M-70 -60 Q0 -40 70 -60" fill="none" stroke-width="1.25"/>',
     f'<path clip-path="url(#to-tc)" d="M-70 -60 Q0 -40 70 -60 V-100 H-70 Z" fill="{PANDA}" stroke="none"/>'
     '<path clip-path="url(#to-tc)" d="M-70 -60 Q0 -40 70 -60" fill="none" stroke-width="1.25"/>'),
    ('<path d="M-22 -82 L0 -48 L22 -82" fill="none" stroke-width="1"/>', '<path d="M-22 -82 L0 -48 L22 -82" fill="none" stroke="#EBC35E" stroke-width="1.4"/>'),
    ('<use href="#crescent" transform="translate(-1 -40)" stroke-width="1.2"/>',
     '<use href="#crescent" transform="translate(-1 -40)" stroke-width="1.2" fill="#EBC35E"/>'),
    ('<path id="to-arm" ', f'<path id="to-arm" fill="{PANDA}" '),
    ('<g id="to-legs">', f'<g id="to-legs" fill="{PANDA}">'),
    ('<g id="to-legs-sit">', f'<g id="to-legs-sit" fill="{PANDA}">'),
    ('<ellipse cx="-30" cy="1" rx="8" ry="6.5" stroke-width="1"/><ellipse cx="30" cy="1" rx="8" ry="6.5" stroke-width="1"/>',
     '<ellipse cx="-30" cy="1" rx="8" ry="6.5" fill="#8A8494" stroke-width="1"/><ellipse cx="30" cy="1" rx="8" ry="6.5" fill="#8A8494" stroke-width="1"/>'),
    # Pebble: powder-blue striped top, cream whisker pads, terracotta pouch, lavender pebble
    ('<ellipse cx="-7" cy="8" rx="8" ry="6" stroke-width="1.2"/><ellipse cx="7" cy="8" rx="8" ry="6" stroke-width="1.2"/>',
     f'<ellipse cx="-7" cy="8" rx="8" ry="6" fill="{IVORY}" stroke-width="1.2"/><ellipse cx="7" cy="8" rx="8" ry="6" fill="{IVORY}" stroke-width="1.2"/>'),
    ('<g id="pb-torso">\n  <use href="#pb-tp"/>\n  <g clip-path="url(#pb-tc)" fill="none">',
     f'<g id="pb-torso">\n  <use href="#pb-tp" fill="{POWDER}"/>\n  <g clip-path="url(#pb-tc)" fill="none">'
     f'<path d="M-40 -44 Q0 -39 40 -44 V-32 Q0 -27 -40 -32 Z" fill="{IVORY}" stroke="none"/>'
     f'<path d="M-40 -20 Q0 -14 40 -20 V0 H-40 Z" fill="{FUR["pb"]}" stroke="none"/>'),
    ('<ellipse cx="14" cy="-17" rx="5" ry="3.5" stroke-width="1"/>', f'<ellipse cx="14" cy="-17" rx="5" ry="3.5" fill="{LAV}" stroke-width="1"/>'),
    ('<path d="M7 -18 L21 -18 L21 -9 Q21 -4 14 -4 Q7 -4 7 -9 Z" stroke-width="1.2"/>',
     f'<path d="M7 -18 L21 -18 L21 -9 Q21 -4 14 -4 Q7 -4 7 -9 Z" fill="{TERRA}" stroke-width="1.2"/>'),
    # Thimble: pink inner ears and cheeks, honey pencil, rose tail bow
    ('<circle cx="-19" cy="-14" r="9" stroke-width="0.9"/>', f'<circle cx="-19" cy="-14" r="9" fill="{BLUSH}" stroke-width="0.9"/>'),
    ('<circle cx="19" cy="-14" r="9" stroke-width="0.9"/>', f'<circle cx="19" cy="-14" r="9" fill="{BLUSH}" stroke-width="0.9"/>'),
    ('<path d="M-15 -2.6 L9 -2.6 L15 0 L9 2.6 L-15 2.6 Z"/><path d="M-15 -2.6 L-19 -2.6 L-19 2.6 L-15 2.6 Z"/>',
     f'<path d="M-15 -2.6 L9 -2.6 L15 0 L9 2.6 L-15 2.6 Z" fill="{HONEY}"/><path d="M-15 -2.6 L-19 -2.6 L-19 2.6 L-15 2.6 Z" fill="{ROSE}"/>'),
    ('<ellipse cx="-11.5" cy="7" rx="3.2" ry="1.9" stroke-width="0.6"/><ellipse cx="11.5" cy="7" rx="3.2" ry="1.9" stroke-width="0.6"/>',
     f'<ellipse cx="-11.5" cy="7" rx="3.2" ry="1.9" fill="{BLUSH}" stroke="none"/><ellipse cx="11.5" cy="7" rx="3.2" ry="1.9" fill="{BLUSH}" stroke="none"/>'),
    ('<path d="M29 -33 L22 -37 L23 -28 Z"/><path d="M29 -33 L35 -39 L36 -30 Z"/><circle cx="29" cy="-33" r="2"/>',
     f'<g fill="{ROSE}"><path d="M29 -33 L22 -37 L23 -28 Z"/><path d="M29 -33 L35 -39 L36 -30 Z"/><circle cx="29" cy="-33" r="2"/></g>'),
    # quilt symbols: honey fill reads well on every patch colour
    ('<g id="sym-acorn">', f'<g id="sym-acorn" fill="{IVORY}">'),
]


def colour_defs():
    d = DEFS
    for old, new in COLOR:
        n = d.count(old)
        assert n >= 1, f"colour target missing: {old[:60]}"
        d = d.replace(old, new)
    return d


S = 0.74  # one scale for the whole cast keeps the bible's relative heights


def friend(c, x, y, **kw):
    return f'<g fill="{FUR[c]}">' + char(c, x, y, S, **kw) + "</g>"


def dot_at(x, y, s=0.85, flip=False):
    fx = -1 if flip else 1
    return f'<use href="#dot" transform="translate({x} {y}) scale({fx*s} {s})" stroke-width="1.4"/>'


# ------------------------------------------------------------------ helpers
def P(d, fill="none", sw=1.6, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke-width="{sw}"{extra}/>'


def blob(cx, cy, rx, ry, n=9, bump=0.28, fill="#fff", sw=1.6):
    """Scalloped cloud/foliage outline."""
    from math import cos, sin, pi
    pts = []
    for k in range(n):
        a0, a1 = 2 * pi * k / n, 2 * pi * (k + 1) / n
        am = (a0 + a1) / 2
        x0, y0 = cx + rx * cos(a0), cy + ry * sin(a0)
        x1, y1 = cx + rx * cos(a1), cy + ry * sin(a1)
        qx, qy = cx + rx * (1 + bump) * cos(am), cy + ry * (1 + bump) * sin(am)
        pts.append((x0, y0, qx, qy, x1, y1))
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f} " + " ".join(f"Q{q[2]:.1f} {q[3]:.1f} {q[4]:.1f} {q[5]:.1f}" for q in pts) + " Z"
    return P(d, fill, sw)


def flower5(x, y, r, petal, centre, sw=1.0):
    from math import cos, sin, radians
    out = [f'<g transform="translate({x} {y})" stroke-width="{sw}">']
    for k in range(5):
        a = radians(72 * k - 90)
        out.append(f'<circle cx="{r*0.55*cos(a):.1f}" cy="{r*0.55*sin(a):.1f}" r="{r*0.45:.1f}" fill="{petal}"/>')
    out.append(f'<circle r="{r*0.32:.1f}" fill="{centre}"/></g>')
    return "".join(out)


def daisy(x, y, r, petal=IVORY, centre=HONEY, n=7, sw=0.9):
    out = [f'<g transform="translate({x} {y})" stroke-width="{sw}">']
    for k in range(n):
        out.append(f'<ellipse cy="{-r*0.62:.1f}" rx="{r*0.3:.1f}" ry="{r*0.45:.1f}" transform="rotate({360*k/n:.1f})" fill="{petal}"/>')
    out.append(f'<circle r="{r*0.33:.1f}" fill="{centre}"/></g>')
    return "".join(out)


def tulip(x, y, h, col, lean=0):
    tx, ty = x + lean, y - h
    return (P(f"M{x} {y} Q{x + lean*0.2} {y - h*0.5} {tx} {ty}", sw=1.2, extra=f' stroke="{FOREST}"')
            + P(f"M{x} {y} Q{x - 9} {y - h*0.45} {x - 3} {y - h*0.75} Q{x - 1.5} {y - h*0.35} {x} {y} Z", "#7DA66E", 0.9)
            + f'<path transform="translate({tx} {ty})" d="M-6 1 Q-7.5 -8 -5 -13 L-2.2 -8.5 L0 -14 L2.2 -8.5 L5 -13 '
              f'Q7.5 -8 6 1 Q0 4.5 -6 1 Z" fill="{col}" stroke-width="1.1"/>')


def maple(x, y, rot, col, s=1.0):
    d = ("M0 -11 L2.5 -5 L7 -7 L5.5 -1.5 L10 0 L5 3 L6 7 L1 5 L0 10 L-1 5 L-6 7 L-5 3 L-10 0 "
         "L-5.5 -1.5 L-7 -7 L-2.5 -5 Z")
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1/s:.2f}">'
            f'<path d="{d}" fill="{col}"/><path d="M0 10 V14 M0 6 V-6" fill="none"/></g>')


def T(s, x, y, size, font="fredoka", wght=600, fill=FOREST, anchor="middle", tracking=0, outline=None, shadow=None,
      editable=False):
    """Outlined (or live) text. outline=(colour, width) draws a halo behind the glyphs."""
    if editable:
        fam = {"fredoka": "Fredoka", "nunito": "Nunito"}[font]
        ta = {"middle": "middle", "start": "start", "end": "end"}[anchor]
        base = (f'font-family="{fam}" font-weight="{wght}" font-size="{size}" text-anchor="{ta}" '
                f'letter-spacing="{tracking*size/1000:.2f}"')
        txt = s.replace("&", "&amp;")
        out = ""
        if shadow:
            out += f'<text x="{x+shadow[1]}" y="{y+shadow[2]}" {base} fill="{shadow[0]}" stroke="none">{txt}</text>'
        if outline:
            out += (f'<text x="{x}" y="{y}" {base} fill="{outline[0]}" stroke="{outline[0]}" '
                    f'stroke-width="{outline[1]}" stroke-linejoin="round">{txt}</text>')
        return out + f'<text x="{x}" y="{y}" {base} fill="{fill}" stroke="none">{txt}</text>'
    d = text_path(s, x, y, size, font, wght, anchor, tracking)
    out = ""
    if shadow:
        out += f'<path d="{d}" transform="translate({shadow[1]} {shadow[2]})" fill="{shadow[0]}" stroke="none"/>'
    if outline:
        out += f'<path d="{d}" fill="{outline[0]}" stroke="{outline[0]}" stroke-width="{outline[1]}" stroke-linejoin="round"/>'
    return out + f'<path d="{d}" fill="{fill}" stroke="none"/>'


# ------------------------------------------------------------------ pieces
def sky():
    return (f'<rect x="-20" y="-20" width="{W+40}" height="{H+40}" fill="url(#sky)" stroke="none"/>'
            '<use href="#cloud" transform="translate(70 318) scale(0.9)" fill="#fff" stroke="#fff" stroke-width="1"/>'
            '<use href="#cloud" transform="translate(452 300) scale(0.6)" fill="#fff" stroke="#fff" stroke-width="1"/>')


def hills():
    b = [P("M-20 524 C90 486 170 500 250 510 C340 520 420 470 520 474 C560 476 600 486 632 496 V812 H-20 Z", "#B9D1AE", 1.4),
         P("M-20 563 C120 540 260 566 380 552 C470 542 550 530 632 540 V812 H-20 Z", GRASS, 1.5)]
    # distant cottages of the Hollow, tiny
    for x, y in ((470, 480), (505, 476)):
        b.append(P(f"M{x-8} {y} V{y-9} L{x} {y-16} L{x+8} {y-9} V{y} Z", IVORY, 1.0))
        b.append(P(f"M{x-10} {y-8} L{x} {y-18} L{x+10} {y-8}", sw=1.0, extra=f' stroke="{TERRA_D}"'))
    return "".join(b)


def blossom_tree():
    """Spring: a blossom tree at the left edge."""
    b = [P("M58 560 C60 520 56 480 62 450 L76 450 C78 480 74 520 80 560 Z", "#9C7456", 1.6),
         P("M66 470 C52 456 44 446 38 432", sw=1.4), P("M70 462 C86 448 96 440 108 430", sw=1.4)]
    b.append(blob(72, 410, 50, 44, n=10, bump=0.3, fill="#F4CBD0", sw=1.7))
    for x, y in ((48, 392), (70, 380), (96, 398), (60, 420), (88, 428), (40, 418), (104, 416), (76, 404)):
        b.append(flower5(x, y, 9, "#FBE3E6", ROSE, 0.8))
    return "".join(b)


def autumn_tree():
    """Autumn: a maple turning orange behind the bench."""
    b = [P("M532 600 C534 560 528 520 536 488 L550 488 C552 520 548 560 552 600 Z", "#9C7456", 1.6)]
    b.append(blob(542, 452, 46, 46, n=10, bump=0.3, fill=AUTUMN, sw=1.7))
    b.append(blob(522, 470, 22, 18, n=6, bump=0.3, fill="#EFA65A", sw=1.2))
    b.append(blob(560, 438, 18, 15, n=6, bump=0.3, fill="#EFA65A", sw=1.2))
    for x, y, r, c in ((498, 528, 20, "#E9B949"), (488, 566, -30, AUTUMN), (566, 540, 40, TERRA)):
        b.append(maple(x, y, r, c, 0.8))
    return "".join(b)


def cottage():
    b = []
    # chimney (stone) with a cap of snow (winter), smoke
    b.append(clip_rect_stones(150, 336, 40, 100))
    b.append(P("M144 336 H196 V324 H144 Z", "#C9BFB6", 1.7))
    b.append(blob(170, 322, 26, 6, n=6, bump=0.45, fill="#fff", sw=1.3))  # snow on the chimney cap
    b.append(blob(186, 300, 9, 7, n=5, bump=0.4, fill="#F4F1EC", sw=1.2) + blob(204, 286, 12, 9, n=6, bump=0.4, fill="#F4F1EC", sw=1.2))
    # wall
    b.append(P("M118 430 H418 V600 H118 Z", "#F4E6CC", 1.8))
    b.append(P("M118 586 H418", sw=1.1))
    # roof
    roof = "M98 436 L268 304 L438 436 Z"
    b.append(f'<clipPath id="roofc"><path d="{roof}"/></clipPath>')
    b.append(P(roof, TERRA, 2.0))
    rows = "".join(f'<path d="M80 {y} H460" fill="none" stroke-width="1.1"/>' for y in (334, 364, 394, 424))
    tiles = "".join(f'<path d="M{x + (14 if r % 2 else 0)} {y0} V{y0 + 30}" fill="none" stroke-width="0.9"/>'
                    for r, y0 in enumerate((304, 334, 364, 394, 424)) for x in range(96, 450, 28))
    scallops = "".join(f'<path d="M{x} {y} q14 12 28 0" fill="{TERRA_D}" fill-opacity="0.25" stroke-width="0.9"/>'
                       for y in (334, 364, 394, 424) for x in range(82 + (14 if (y // 30) % 2 else 0), 450, 28))
    b.append(f'<g clip-path="url(#roofc)">{scallops}{rows}{tiles}</g>')
    b.append(P("M92 440 L268 300 L444 440", sw=3.2, extra=f' stroke="{INK}"'))
    # round attic window
    b.append(f'<circle cx="268" cy="384" r="17" fill="{IVORY}" stroke-width="1.6"/><circle cx="268" cy="384" r="11" fill="#CFE0EA" stroke-width="1.1"/>'
             + P("M257 384 H279 M268 373 V395", sw=0.9))
    # seasonal bunting under the eaves: blossom, sun, leaf, snowflake
    b.append(P("M128 444 Q268 476 408 444", sw=1.1))
    flags = [(150, ROSE, "b"), (190, HONEY, "s"), (230, SAGE, "b"), (268, AUTUMN, "l"), (306, POWDER, "f"),
             (346, LAV, "b"), (386, HONEY, "s")]
    for x, col, motif in flags:
        t = (x - 128) / 280
        y = (1 - t) ** 2 * 444 + 2 * (1 - t) * t * 476 + t ** 2 * 444
        b.append(P(f"M{x-10} {y-2:.1f} L{x+10} {y-2:.1f} L{x} {y+20:.1f} Z", col, 1.2))
        if motif == "f":
            b.append(f'<use href="#flake" transform="translate({x} {y+6:.1f}) scale(0.5)" stroke="#fff" stroke-width="2.2"/>')
        elif motif == "s":
            b.append(f'<circle cx="{x}" cy="{y+5:.1f}" r="3.2" fill="#fff" stroke="none"/>')
        elif motif == "l":
            b.append(P(f"M{x} {y+12:.1f} Q{x-5} {y+5:.1f} {x} {y:.1f} Q{x+5} {y+5:.1f} {x} {y+12:.1f} Z", "#fff", 0))
        else:
            b.append(f'<circle cx="{x}" cy="{y+5:.1f}" r="2.6" fill="#fff" stroke="none"/>')

    # round kitchen window with shutters, window box of tulips
    wx, wy = 176, 500
    b.append(P(f"M{wx-44} {wy-36} A30 38 0 0 0 {wx-44} {wy+36} Z", SAGE, 1.5))
    b.append(P(f"M{wx+44} {wy-36} A30 38 0 0 1 {wx+44} {wy+36} Z", SAGE, 1.5))
    b.append(f'<use href="#heart" transform="translate({wx-58} {wy}) scale(0.75)" fill="{IVORY}" stroke-width="1.3"/>')
    b.append(f'<use href="#heart" transform="translate({wx+58} {wy}) scale(0.75)" fill="{IVORY}" stroke-width="1.3"/>')
    b.append(f'<circle cx="{wx}" cy="{wy}" r="38" fill="{HONEY}" stroke-width="1.8"/>')
    b.append(f'<circle cx="{wx}" cy="{wy}" r="31" fill="#FCE7B0" stroke-width="1.4"/>')
    b.append(P(f"M{wx-31} {wy} H{wx+31} M{wx} {wy-31} V{wy+31}", sw=1.6, extra=f' stroke="{HONEY}"'))
    b.append(P(f"M{wx-31} {wy} H{wx+31} M{wx} {wy-31} V{wy+31}", sw=0.6))
    # a kettle steaming on the sill inside (cosy glow)
    for tx, col in ((wx-38, ROSE), (wx-24, HONEY), (wx+24, LAV), (wx+38, ROSE)):
        b.append(tulip(tx, wy+38, 14, col))
    b.append(P(f"M{wx-46} {wy+36} H{wx+46} V{wy+56} H{wx-46} Z", TERRA, 1.7))
    b.append("".join(f'<use href="#heart" transform="translate({hx} {wy+46}) scale(0.4)" fill="{IVORY}" stroke-width="2"/>' for hx in (wx-24, wx, wx+24)))

    # round front door with a holly wreath (winter)
    dx = 344
    b.append(P(f"M{dx-36} 600 V532 A36 36 0 0 1 {dx+36} 532 V600 Z", IVORY, 1.8))
    b.append(P(f"M{dx-29} 600 V532 A29 29 0 0 1 {dx+29} 532 V600 Z", "#7FA6C4", 1.6))
    b.append(P(f"M{dx-14} 506 V600 M{dx} 503 V600 M{dx+14} 506 V600", sw=0.9))
    b.append(f'<circle cx="{dx+18}" cy="566" r="3.4" fill="{HONEY}" stroke-width="1.1"/>')
    wreath = []
    from math import cos, sin, radians
    for k in range(10):
        a = radians(36 * k)
        wreath.append(f'<ellipse cx="{dx + 12*cos(a):.1f}" cy="{530 + 12*sin(a):.1f}" rx="5.5" ry="3" '
                      f'transform="rotate({36*k + 90} {dx + 12*cos(a):.1f} {530 + 12*sin(a):.1f})" fill="#4F8358" stroke-width="0.8"/>')
    b.append("".join(wreath))
    b.append("".join(f'<circle cx="{dx+x}" cy="{530+y}" r="2.4" fill="#C8484A" stroke-width="0.7"/>' for x, y in ((-4, 12), (1, 14), (5, 11))))
    b.append(P(f"M{dx-44} 600 H{dx+44} V608 H{dx-44} Z", "#C9BFB6", 1.5))
    # autumn pumpkins by the step
    for x, y, w, h, col in ((404, 606, 30, 22, AUTUMN), (424, 611, 20, 15, "#E9B949")):
        b.append(P(f"M{x} {y-h} C{x-w*0.9} {y-h} {x-w*0.9} {y} {x} {y} C{x+w*0.9} {y} {x+w*0.9} {y-h} {x} {y-h} Z", col, 1.4))
        b.append(P(f"M{x} {y-h} Q{x-w*0.35} {y-h/2} {x} {y} M{x} {y-h} Q{x+w*0.35} {y-h/2} {x} {y}", sw=0.9))
        b.append(P(f"M{x} {y-h} q1 -5 4 -6", sw=1.6, extra=' stroke="#5A3B2E"'))
    return "".join(b)


def clip_rect_stones(x, y, w, h):
    d = f"M{x} {y} H{x+w} V{y+h} H{x} Z"
    stones = []
    rh = 13
    for r in range(int(h / rh) + 1):
        y0 = y + r * rh
        off = 0 if r % 2 == 0 else 11
        for k in range(-1, 4):
            x0 = x + off + k * 21
            stones.append(f'<rect x="{x0+1}" y="{y0+1}" width="19" height="{rh-2}" rx="4" fill="#D6CEC4" stroke-width="0.9"/>')
    return (f'<clipPath id="chim"><path d="{d}"/></clipPath>' + P(d, "#C9BFB6", 1.7)
            + f'<g clip-path="url(#chim)">{"".join(stones)}</g>' + P(d, "none", 1.7))


def sunflowers():
    """Summer: sunflowers against the cottage's sunny side."""
    b = []
    for x, top, s in ((432, 520, 1.0), (458, 548, 0.85)):
        b.append(P(f"M{x} 640 Q{x+4} {(top+640)/2} {x} {top}", sw=2.2, extra=f' stroke="{FOREST}"'))
        b.append(P(f"M{x+1} {top+50} q14 -10 20 4 q-12 6 -20 -4 Z", "#7DA66E", 1.0))
        b.append(f'<g transform="translate({x} {top}) scale({s})">')
        for k in range(12):
            b.append(f'<ellipse cy="-14" rx="4.5" ry="9" transform="rotate({30*k})" fill="{HONEY}" stroke-width="1"/>')
        b.append('<circle r="9" fill="#8A5A3A" stroke-width="1.2"/></g>')
    return "".join(b)


def bench_and_quilt():
    b = []
    # back slats and posts
    b.append(P("M440 588 H576 V598 H440 Z", "#B98A5F", 1.5) + P("M440 606 H576 V616 H440 Z", "#B98A5F", 1.5))
    b.append(P("M446 584 V646 H454 V584 Z", "#9C7456", 1.4) + P("M562 584 V646 H570 V584 Z", "#9C7456", 1.4))
    # seat and legs
    b.append(P("M434 640 H580 V650 H434 Z", "#B98A5F", 1.6))
    b.append(P("M444 650 V690 H452 V650 Z", "#9C7456", 1.4) + P("M562 650 V690 H570 V650 Z", "#9C7456", 1.4))
    # the friendship quilt, folded in a stack on the bench (patches show on the folds)
    cols = [ROSE, HONEY, SAGE, POWDER, LAV, TERRA, "#F2D06B", "#E6A564"]
    x0, wq = 438, 56
    for i, (y, hq) in enumerate(((628, 12), (617, 11), (607, 10))):
        b.append(P(f"M{x0} {y} H{x0+wq} Q{x0+wq+4} {y+hq/2} {x0+wq} {y+hq} H{x0} Q{x0-4} {y+hq/2} {x0} {y} Z", IVORY, 1.4))
        for k in range(5):
            px = x0 + 2 + k * 11
            b.append(f'<rect x="{px}" y="{y+1.5}" width="10" height="{hq-3}" fill="{cols[(k + i*3) % 8]}" stroke-width="0.6"/>')
        b.append(P(f"M{x0} {y} H{x0+wq} Q{x0+wq+4} {y+hq/2} {x0+wq} {y+hq} H{x0} Q{x0-4} {y+hq/2} {x0} {y} Z", sw=1.4))
    return "".join(b)


def stones():
    return "".join(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#D6CEC4" stroke-width="1.3"/>'
                   for cx, cy, rx, ry in ((344, 620, 22, 5.5), (350, 638, 25, 6), (344, 658, 28, 6.5)))


def garden_front():
    b = []
    # flower border across the front
    for x, y, r, c in ((48, 690, 9, IVORY), (468, 694, 9, IVORY), (548, 694, 10, "#FBE3E6"), (500, 700, 8, IVORY),
                       (186, 700, 8, "#FBE3E6")):
        b.append(daisy(x, y, r, c))
    for x, h, c in ((40, 26, ROSE), (64, 22, HONEY), (522, 24, LAV), (574, 20, ROSE), (446, 22, TERRA)):
        b.append(tulip(x, 704, h, c))
    return "".join(b)


def tufts(pts):
    return "".join(P(f"M{x-6} {y} Q{x-4} {y-8} {x-1} {y-11} M{x} {y} Q{x} {y-9} {x+2} {y-13} M{x+6} {y} Q{x+5} {y-7} {x+3} {y-10}",
                     sw=1.0, extra=f' stroke="{FOREST}"') for x, y in pts)


def cast():
    b = []
    # back row
    b.append(friend("ju", 74, 648, arms=(150, -14), mood="happy"))
    b.append(friend("br", 252, 650, arms=(16, -16), mood="happy"))
    # Tofu resting on the bench beside the folded quilt; Thimble sits on the quilt
    b.append(friend("to", 532, 644, sit=True, mood="happy", arms=(10, -10)))
    b.append(friend("th", 466, 607, sit=True, mood="happy", arms=(150, -14)))
    # front row
    b.append(friend("mi", 136, 700, mood="open"))
    b.append(friend("pb", 214, 702, mood="happy", arms=(14, -150)))
    b.append(friend("cl", 300, 702, mood="happy", arms=(14, -14)))
    b.append(friend("pi", 396, 702, mood="happy", arms=(14, -150), wag=True))
    return "".join(b)


def badge(editable):
    """'50 Coloring Illustrations' honey rosette (series element)."""
    cx, cy = 526, 342
    from math import cos, sin, radians
    pts = []
    for k in range(32):
        a = radians(k * 360 / 32)
        r = 56 if k % 2 == 0 else 50
        pts.append(f"{cx + r*cos(a):.1f} {cy + r*sin(a):.1f}")
    out = [P("M" + " L".join(pts) + " Z", HONEY, 1.6),
           f'<circle cx="{cx}" cy="{cy}" r="44" fill="{IVORY}" stroke-width="1.2"/>',
           f'<circle cx="{cx}" cy="{cy}" r="40" fill="none" stroke="{HONEY}" stroke-width="1" stroke-dasharray="3 2.5"/>']
    out.append(T("50", cx, cy + 6, 38, "fredoka", 700, TERRA_D, editable=editable))
    out.append(T("COLORING", cx, cy + 19, 8, "nunito", 900, FOREST, tracking=40, editable=editable))
    out.append(T("ILLUSTRATIONS", cx, cy + 28.5, 7, "nunito", 900, FOREST, tracking=20, editable=editable))
    return "".join(out)


def quilt_strip():
    """Bottom border: a row of friendship-quilt patches (series motif)."""
    cols = [ROSE, HONEY, SAGE, POWDER, LAV, TERRA, "#F2D06B", "#E6A564"]
    syms = ["acorn", "clover", "fish", "star", "pompom", "moon", "pebble", "needle"]
    n, x0, x1, y, h = 12, SAFE + 9, W - SAFE - 9, 712, 30
    w = (x1 - x0) / n
    out = [f'<rect x="{x0-4}" y="{y-4}" width="{x1-x0+8}" height="{h+8}" rx="6" fill="{IVORY}" stroke-width="1.4"/>']
    for k in range(n):
        x = x0 + k * w
        out.append(f'<rect x="{x:.2f}" y="{y}" width="{w:.2f}" height="{h}" fill="{cols[k % 8]}" stroke-width="1.1"/>')
        out.append(f'<rect x="{x+3:.2f}" y="{y+3}" width="{w-6:.2f}" height="{h-6}" fill="none" stroke="{IVORY}" stroke-width="0.8" stroke-dasharray="2.5 2"/>')
        if k % 2 == 0:
            s = 0.5
            out.append(f'<g transform="translate({x + w/2:.2f} {y + h/2}) scale({s})" stroke-width="{1.2/s:.2f}" fill="{IVORY}">'
                       f'<use href="#sym-{syms[(k // 2) % 8]}"/></g>')
        else:
            out.append(f'<use href="#heart" transform="translate({x + w/2:.2f} {y + h/2 + 2}) scale(0.75)" fill="{IVORY}" stroke-width="1.4"/>')
    return "".join(out)


def text_block(editable):
    out = []
    # VOLUME 1 stitched tab
    vw = 104
    out.append(f'<rect x="{306 - vw/2}" y="34" width="{vw}" height="24" rx="12" fill="{SAGE}" stroke-width="1.4"/>')
    out.append(f'<rect x="{306 - vw/2 + 4}" y="38" width="{vw - 8}" height="16" rx="8" fill="none" stroke="{IVORY}" stroke-width="0.8" stroke-dasharray="3 2.4"/>')
    out.append(T("VOLUME 1", 306, 51, 11, "nunito", 900, IVORY, tracking=160, editable=editable))
    # title lock-up
    out.append(T("Cozy Little", 306, 136, 86, "fredoka", 600, TERRA, outline=(IVORY, 12), shadow=("#E2C9A8", 3, 5),
                 editable=editable))
    out.append(T("Friends", 306, 236, 128, "fredoka", 600, FOREST, outline=(IVORY, 14), shadow=("#C9D8BD", 3, 6),
                 editable=editable))
    # subtitle
    out.append(T("A Cute & Cozy Coloring Book for Relaxation", 306, 272, 19.5, "nunito", 800, TERRA_D,
                 outline=(CREAM, 5), editable=editable))
    # imprint
    out.append(T("BOOKSHELF", 306, 762, 13, "nunito", 900, FOREST, tracking=320, editable=editable))
    return "".join(out)


def font_face():
    css = []
    for fam, fn in (("Fredoka", "Fredoka.ttf"), ("Nunito", "Nunito.ttf")):
        data = base64.b64encode(open(os.path.join(HERE, "fonts", fn), "rb").read()).decode()
        css.append(f'@font-face{{font-family:"{fam}";src:url(data:font/ttf;base64,{data}) format("truetype");font-weight:200 1000;}}')
    return "<style>" + "".join(css) + "</style>"


def build(editable=False, bleed=False):
    chars.OUTLINE_PT = 1.7
    body = [
        f'<g id="background">{sky()}{hills()}</g>',
        f'<g id="scenery">{blossom_tree()}{autumn_tree()}{cottage()}{sunflowers()}{bench_and_quilt()}{stones()}'
        f'{tufts([(110, 610), (270, 618), (420, 660), (40, 640), (590, 660), (300, 690)])}</g>',
        # Dot, tucked beside the chimney smoke
        f'<g id="dot-hidden">{dot_at(178, 316, 0.8)}</g>',
        f'<g id="characters">{cast()}</g>',
        f'<g id="garden">{garden_front()}</g>',
        f'<g id="series-border"><rect x="20" y="20" width="{W-40}" height="{H-40}" rx="16" fill="none" stroke="{IVORY}" '
        f'stroke-width="1.6" stroke-dasharray="6 5"/>{quilt_strip()}</g>',
        f'<g id="badge">{badge(editable)}</g>',
        f'<g id="type">{text_block(editable)}</g>',
    ]
    defs = colour_defs()
    grad = (f'<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{CREAM}"/><stop offset="0.3" stop-color="#F3F1E6"/>'
            f'<stop offset="0.6" stop-color="#D5E6EF"/><stop offset="1" stop-color="#D5E6EF"/></linearGradient>'
            + (font_face() if editable else "") + '</defs>')
    title = "Cozy Little Friends: A Cute &amp; Cozy Coloring Book for Relaxation — Volume 1 front cover"
    if bleed:
        b = 9  # 0.125 in
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" width="8.75in" height="11.25in" '
                f'viewBox="{-b} {-b} {W + 2*b} {H + 2*b}">')
    else:
        head = f'<svg xmlns="http://www.w3.org/2000/svg" width="8.5in" height="11in" viewBox="0 0 {W} {H}">'
    return f"""{head}
<title>{title}</title>
{defs}
{grad}
<rect x="-20" y="-20" width="{W+40}" height="{H+40}" fill="{CREAM}"/>
<g fill="#fff" stroke="{INK}" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.25">
{"".join(body)}
</g>
</svg>
"""


if __name__ == "__main__":
    out = os.path.join(HERE, "out")
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "cover-front-v1.svg"), "w").write(build(False))
    open(os.path.join(out, "cover-front-v1-editable.svg"), "w").write(build(True))
    open(os.path.join(out, "cover-front-v1-bleed.svg"), "w").write(build(False, bleed=True))
    print("wrote cover-front-v1.svg, -editable.svg, -bleed.svg")
