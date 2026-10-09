"""Cozy Little Friends — Volume 1 full KDP paperback wrap (back + spine + front).

Spine width follows KDP's formula for a black-and-white interior on WHITE
paper: pages x 0.002252 in. The interior PDF is 110 pages, so the spine is
0.2477 in. Change PAGES / PAPER below if the interior or paper changes.

Layout (left to right): 0.125 in bleed | back 8.5 in | spine | front 8.5 in | 0.125 in bleed,
11.25 in tall (0.125 in bleed top and bottom).

usage: python3 wrap.py -> out/cover-wrap-v1.svg (print, text outlined)
                          out/cover-wrap-v1-guides.svg (same + trim/spine/safe/barcode guides, NOT for print)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import cover as C  # noqa: E402
from cover import (P, T, blob, daisy, flower5, maple, friend, dot_at, colour_defs, sky_gradient, hills,  # noqa: E402
                   INK, CREAM, IVORY, SAGE, FOREST, ROSE, HONEY, POWDER, LAV, TERRA, TERRA_D, AUTUMN, W, H)
from textpath import text_path, text_width, font  # noqa: E402

PAGES = 110
PAPER = {"white": 0.002252, "cream": 0.0025}["white"]
BLEED = 9                       # 0.125 in
SPINE = PAGES * PAPER * 72      # pt
TW = 2 * BLEED + 2 * W + SPINE  # total width, pt
TH = 2 * BLEED + H
BX0 = BLEED                     # back panel trim, left
SX0 = BLEED + W                 # spine, left fold
XC = SX0 + SPINE / 2            # spine centre
FX0 = SX0 + SPINE               # front panel trim, left
# KDP barcode area on the back (2 x 1.2 in, 0.25 in from the trim and spine edges), in back-panel units
BARCODE = (W - 18 - 144, H - 18 - 86.4, W - 18, H - 18)


def wrap_lines(text, width, name, wght, size):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if text_width(trial, name, wght, size) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    return lines + [cur] if cur else lines


BLURB = ("Welcome to Honeyfern Hollow, a little village where the kettle is always warm and every season "
         "brings something to celebrate. Spend one gentle year with eight good friends: Bramble the bear, "
         "Clover the rabbit, Miso the cat, Juniper the fox, Pip the puppy, Tofu the panda, Pebble the otter "
         "and Thimble the mouse. Bake pancakes, splash through spring puddles, pick apples, stitch a "
         "friendship quilt and gather by the fire as the snow falls.")
DOT_LINE = "And look out for Dot, a tiny wren hiding on every page!"
FEATURES = [
    "50 original illustrations, from spring blossoms to snowy evenings",
    "Bold, clean outlines with roomy spaces for pencils, pens or markers",
    "Every illustration printed on its own page, blank on the back",
    "A color test page, a meet-the-friends page and a Dot answer key",
]


def back_panel():
    b = []
    # stitched border, as on the front
    b.append(f'<rect x="20" y="20" width="{W-40}" height="{H-40}" rx="16" fill="none" stroke="{IVORY}" '
             f'stroke-width="1.6" stroke-dasharray="6 5"/>')
    # a few seasonal sprigs in the top corners
    b.append(flower5(54, 58, 14, "#FBE3E6", ROSE) + flower5(80, 40, 9, "#FBE3E6", ROSE))
    b.append(maple(560, 54, 18, AUTUMN, 1.1) + maple(536, 76, -24, HONEY, 0.8))
    b.append(f'<use href="#flake" transform="translate(572 92) scale(0.9)" stroke="{POWDER}" stroke-width="2.4"/>')
    b.append(daisy(44, 96, 10))
    # heading
    b.append(T("Welcome to Honeyfern Hollow", 306, 92, 31, "fredoka", 600, FOREST, outline=(IVORY, 8)))
    b.append("".join(f'<use href="#heart" transform="translate({x} 112) scale(0.6)" fill="{c}" stroke-width="1.6"/>'
                     for x, c in ((290, ROSE), (306, HONEY), (322, SAGE))))
    # blurb card
    x0, x1, y0 = 56, W - 56, 128
    tx0, tw = x0 + 30, (x1 - x0) - 60
    size, lead = 12.6, 19
    body = wrap_lines(BLURB, tw, "nunito", 600, size)
    dot_l = wrap_lines(DOT_LINE, tw, "nunito", 800, size)
    y = y0 + 40
    txt = []
    for ln in body:
        txt.append(T(ln, 306, y, size, "nunito", 600, INK))
        y += lead
    y += 8
    for ln in dot_l:
        txt.append(T(ln, 306, y, size, "nunito", 800, TERRA_D))
        y += lead
    y += 14
    txt.append(T("INSIDE THIS BOOK", 306, y, 10, "nunito", 900, FOREST, tracking=220))
    y += 24
    cols = [ROSE, HONEY, SAGE, POWDER]
    for i, f in enumerate(FEATURES):
        w = text_width(f, "nunito", 700, 12)
        fx = 306 - (w + 20) / 2
        txt.append(f'<rect x="{fx:.1f}" y="{y-10}" width="11" height="11" rx="2" fill="{cols[i]}" stroke-width="1"/>'
                   f'<rect x="{fx+2:.1f}" y="{y-8}" width="7" height="7" rx="1" fill="none" stroke="{IVORY}" stroke-width="0.6" stroke-dasharray="1.5 1.2"/>')
        txt.append(T(f, fx + 20, y, 12, "nunito", 700, INK, anchor="start"))
        y += 21
    y1 = y + 8
    b.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" rx="18" fill="{IVORY}" stroke-width="1.6"/>')
    b.append(f'<rect x="{x0+7}" y="{y0+7}" width="{x1-x0-14}" height="{y1-y0-14}" rx="13" fill="none" stroke="{SAGE}" '
             f'stroke-width="1.1" stroke-dasharray="4 3"/>')
    b.append("".join(txt))
    # Dot perched on the card's top edge
    b.append(f'<g id="back-dot">{dot_at(x1 - 40, y0 - 7, 0.95)}</g>')
    return "".join(b), y1


def back_friends():
    """All eight friends in a line on the lawn (same parts, same scale ratios as the book)."""
    s0 = C.S
    C.S = 0.56
    row = [("th", 46, dict(mood="happy", arms=(150, -14))), ("pb", 104, dict(mood="happy")),
           ("mi", 168, dict(mood="happy")), ("cl", 234, dict(mood="happy", arms=(14, -150))),
           ("br", 316, dict(mood="happy", arms=(16, -16))), ("to", 406, dict(mood="happy")),
           ("ju", 484, dict(mood="happy")), ("pi", 552, dict(mood="happy", arms=(14, -150), wag=True))]
    out = "".join(friend(c, x, 650, **kw) for c, x, kw in row)
    C.S = s0
    return out


def back_ground_details():
    b = []
    for x, h, c in ((24, 24, ROSE), (440, 22, LAV), (520, 18, HONEY)):
        b.append(C.tulip(x, 672, h, c))
    for x, y, r, c in ((60, 668, 8, IVORY), (274, 678, 8, "#FBE3E6"), (140, 680, 7, IVORY), (356, 676, 8, IVORY)):
        b.append(daisy(x, y, r, c))
    b.append(C.tufts([(190, 664), (440, 676), (20, 690), (300, 690)]))
    return "".join(b)


def imprint():
    b = [T("BOOKSHELF", 200, 724, 14, "nunito", 900, FOREST, tracking=320)]
    b.append(P("M150 734 H250", sw=1.2, extra=f' stroke="{FOREST}"'))
    b.append(T("Copyright © 2026 Bookshelf. All rights reserved.", 200, 752, 8, "nunito", 600, INK))
    return "".join(b)


def spine():
    f = font("fredoka", 600)
    cap_f = f["OS/2"].sCapHeight / f["head"].unitsPerEm
    n = font("nunito", 900)
    cap_n = n["OS/2"].sCapHeight / n["head"].unitsPerEm

    def vtext(s, yc, size, name, wght, fill, cap, tracking=0):
        d = text_path(s, 0, 0, size, name, wght, "middle", tracking)
        return (f'<path d="{d}" transform="translate({XC - cap*size/2:.2f} {yc + BLEED}) rotate(90)" '
                f'fill="{fill}" stroke="none"/>')
    out = [vtext("VOLUME 1", 70, 6.6, "nunito", 900, TERRA_D, cap_n, 180),
           vtext("COZY LITTLE FRIENDS", 262, 10, "fredoka", 600, FOREST, cap_f, 40),
           vtext("BOOKSHELF", 452, 6.6, "nunito", 900, FOREST, cap_n, 260)]
    return "".join(out), cap_f * 10


def build(guides=False):
    C.chars.OUTLINE_PT = 1.7
    back_txt, card_bottom = back_panel()
    spine_txt, spine_cap = spine()
    defs = colour_defs()
    clips = (f'<clipPath id="half-back"><rect x="-1" y="-1" width="{XC + 1}" height="{TH + 2}"/></clipPath>'
             f'<clipPath id="half-front"><rect x="{XC}" y="-1" width="{TW - XC + 1}" height="{TH + 2}"/></clipPath>')
    layers = [
        # one continuous sky; the front's hills, and their mirror image on the back, meet at the spine
        f'<g id="background"><rect width="{TW}" height="{TH}" fill="url(#sky)" stroke="none"/>'
        f'<g clip-path="url(#half-front)"><g transform="translate({FX0} {BLEED})">{hills()}</g></g>'
        f'<g clip-path="url(#half-back)"><g transform="translate({2*XC - FX0:.3f} {BLEED}) scale(-1 1)">{hills(distant=False)}</g></g></g>',
        f'<g id="back" transform="translate({BX0} {BLEED})">'
        f'<use href="#cloud" transform="translate(110 520) scale(0.8)" fill="#fff" stroke="#fff" stroke-width="1"/>'
        f'<use href="#cloud" transform="translate(500 500) scale(0.55)" fill="#fff" stroke="#fff" stroke-width="1"/>'
        f'{back_txt}{back_ground_details()}<g id="back-friends">{back_friends()}</g><g id="imprint">{imprint()}</g></g>',
        f'<g id="spine">{spine_txt}</g>',
        f'<g id="front" transform="translate({FX0:.3f} {BLEED})">{C.front_layers(background=False)}</g>',
    ]
    g = ""
    if guides:
        bx = BX0 + BARCODE[0]
        g = (f'<g id="guides" fill="none" stroke-width="0.8">'
             f'<rect x="{BLEED}" y="{BLEED}" width="{TW - 2*BLEED:.2f}" height="{H}" stroke="#E0218A"/>'
             f'<path d="M{SX0} 0 V{TH} M{FX0:.2f} 0 V{TH}" stroke="#1F6FEB"/>'
             f'<rect x="{BX0 + 27}" y="{BLEED + 27}" width="{W - 54}" height="{H - 54}" stroke="#16A34A" stroke-dasharray="4 3"/>'
             f'<rect x="{FX0 + 27:.2f}" y="{BLEED + 27}" width="{W - 54}" height="{H - 54}" stroke="#16A34A" stroke-dasharray="4 3"/>'
             f'<rect x="{bx}" y="{BLEED + BARCODE[1]}" width="144" height="86.4" stroke="#E0218A" fill="#E0218A" fill-opacity="0.12"/>'
             f'</g>')
    title = "Cozy Little Friends — Volume 1 full paperback cover (back, spine, front)"
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{TW/72:.4f}in" height="{TH/72:.4f}in" viewBox="0 0 {TW:.3f} {TH}">
<title>{title}</title>
{defs}
<defs>{sky_gradient()}{clips}</defs>
<rect width="{TW:.3f}" height="{TH}" fill="{CREAM}"/>
<g fill="#fff" stroke="{INK}" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.25">
{"".join(layers)}
{g}
</g>
</svg>
"""
    return svg, card_bottom, spine_cap


if __name__ == "__main__":
    out = os.path.join(HERE, "out")
    svg, card_bottom, cap = build()
    open(os.path.join(out, "cover-wrap-v1.svg"), "w").write(svg)
    open(os.path.join(out, "cover-wrap-v1-guides.svg"), "w").write(build(guides=True)[0])
    print(f"spine {SPINE/72:.4f} in ({SPINE:.2f} pt), wrap {TW/72:.4f} x {TH/72:.4f} in; "
          f"blurb card ends y={card_bottom:.0f}; spine cap height {cap:.1f} pt, side margins {(SPINE-cap)/2:.1f} pt")
