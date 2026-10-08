"""Page 38 — Orchard Fruit Picnic (above Lilypad Pond)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import basket, bowl

TITLE = "Page 38 — Orchard Fruit Picnic"


def apple(x, y, r=11):
    return (f'<path d="M{x} {y - r*0.7:.1f} C{x - r*1.3:.1f} {y - r*1.3:.1f} {x - r*1.4:.1f} {y + r*0.9:.1f} {x} {y + r:.1f} '
            f'C{x + r*1.4:.1f} {y + r*0.9:.1f} {x + r*1.3:.1f} {y - r*1.3:.1f} {x} {y - r*0.7:.1f} Z" stroke-width="1.5"/>'
            f'<path d="M{x} {y - r*0.7:.1f} Q{x + 2} {y - r*1.3:.1f} {x + 4} {y - r*1.5:.1f}" fill="none" stroke-width="1.3"/>')


def pear(x, y, r=10):
    return (f'<path d="M{x} {y - r*1.5:.1f} Q{x - r*0.6:.1f} {y - r*1.4:.1f} {x - r*0.6:.1f} {y - r*0.5:.1f} Q{x - r*1.2:.1f} {y} {x - r:.1f} {y + r*0.6:.1f} '
            f'Q{x} {y + r*1.3:.1f} {x + r:.1f} {y + r*0.6:.1f} Q{x + r*1.2:.1f} {y} {x + r*0.6:.1f} {y - r*0.5:.1f} Q{x + r*0.6:.1f} {y - r*1.4:.1f} {x} {y - r*1.5:.1f} Z" stroke-width="1.5"/>'
            f'<path d="M{x} {y - r*1.5:.1f} V{y - r*2:.1f}" stroke-width="1.3"/>')


def leaf_pair(x, y, rot):
    return (f'<g transform="translate({x} {y}) rotate({rot})" stroke-width="1.2"><path d="M0 0 C-6 -6 -6 -16 0 -22 C6 -16 6 -6 0 0 Z" transform="rotate(-30)"/>'
            '<path d="M0 0 C-6 -6 -6 -16 0 -22 C6 -16 6 -6 0 0 Z" transform="rotate(30)"/></g>')


def build():
    b = []
    # pond glimmering in the background, slope of the orchard
    b.append('<path d="M240 300 C320 280 480 290 600 280 V380 C480 390 340 386 240 370 Z" stroke-width="1.6"/>' + lines("M300 330 q14 -4 28 0 M420 320 q14 -4 28 0 M520 350 q14 -4 28 0", 1))
    b.append('<path d="M30 360 C200 380 400 390 600 372 V800 H30 Z" stroke-width="1.6"/>')
    from scene import scallop_blob
    b.append('<rect x="458" y="230" width="14" height="120" stroke-width="1.6"/>' + scallop_blob(465, 200, 64, 48, 10, 0.3, 1.6) + "".join(apple(x, y, 8) for x, y in ((440, 196), (486, 186), (470, 220))))
    # tree trunk and branches framing the top and left edges
    b.append('<path d="M30 800 V300 Q60 200 30 120 V800 Z M30 260 Q90 220 100 120 L112 124 Q104 228 44 290 Z" stroke-width="1.8"/>')
    b.append('<path d="M60 790 L80 300 Q90 220 140 180 L148 192 Q104 228 96 300 L84 790 Z" stroke-width="2"/>')
    b.append(lines("M70 400 q-4 30 0 60 M74 560 q4 30 0 60", 1))
    b.append('<path d="M30 60 C160 70 300 90 460 50 C520 36 560 50 600 40 L600 56 C560 64 520 52 466 64 C300 106 160 86 30 80 Z" stroke-width="1.8"/>')
    b.append('<path d="M140 180 C220 140 300 130 380 76 L386 88 C306 146 224 156 148 192 Z" stroke-width="1.7"/>')
    for (x, y, r) in ((90, 62, 160), (150, 70, 200), (220, 82, 170), (300, 84, 200), (370, 72, 160), (430, 58, 190), (200, 150, 10), (270, 128, -20),
                      (330, 104, 20), (110, 150, 30), (70, 110, 0), (500, 52, 180), (540, 60, 170), (420, 110, 20), (480, 90, 160), (560, 100, 200)):
        b.append(leaf_pair(x, y, r))
    b.append("".join(apple(x, y) for x, y in ((120, 96), (190, 110), (260, 112), (340, 104), (410, 92), (236, 168), (300, 148), (520, 76), (566, 70))))
    b.append(pear(160, 196, 10) + pear(360, 128, 10))
    # wooden ladder standing left of centre, Pebble climbing to pick an apple
    b.append('<path d="M196 730 L226 200 H238 L210 730 Z M288 730 L262 200 H274 L302 730 Z" stroke-width="1.8"/>')
    for k in range(1, 10):
        y = 730 - k * 54
        b.append(f'<rect x="{205 + k*3}" y="{y}" width="{88 - k*5}" height="9" rx="2" stroke-width="1.5"/>')
    px, py, ps = 250, 352, 1.25
    b.append(char("pb", px, py, ps, arms=(14, -160), mood="happy"))
    ax, ay = paw("pb", px, py, ps, "R", -160)
    b.append(apple(ax + 2, ay - 10, 12))
    b.append(arms_only("pb", px, py, ps, (None, -160)))
    # picnic blanket with a fruit pattern in the lower right
    bl = "M380 560 L590 540 L600 760 L330 760 Z"
    pat = "".join(f'<circle cx="{x}" cy="{y}" r="8" stroke-width="1.1"/><path d="M{x} {y - 8} q2 -5 6 -6" fill="none" stroke-width="0.9"/>' for x in range(390, 600, 46) for y in range(570, 760, 46))
    b.append(clip_d(bl, pat + lines("M330 610 L600 590 M330 680 L600 660", 1), 2))
    # baskets of apples, pears and plums; sliced watermelon; cherries; juice jug
    b.append(basket(440, 620, 70, 34, handle=False) + apple(424, 590) + apple(448, 586) + apple(462, 594))
    b.append(basket(540, 610, 64, 32, handle=False) + pear(528, 584) + pear(552, 582))
    b.append(basket(500, 700, 60, 30, handle=False) + "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="8" stroke-width="1.4"/>' for x, y in ((486, 670), (504, 666), (520, 672))))
    b.append('<path d="M370 740 L440 740 A35 35 0 0 1 370 740 Z" transform="rotate(180 405 740) translate(0 -20)" stroke-width="1.8"/>')
    b.append('<path d="M376 720 Q405 760 434 720 Z" stroke-width="1.8"/><path d="M382 720 Q405 750 428 720 Z" stroke-width="1.1"/>'
             + "".join(f'<path d="M{x} {y} q2 4 0 6 q-2 -2 0 -6 Z" fill="#000" stroke="none"/>' for x, y in ((396, 728), (406, 734), (416, 728))))
    b.append(bowl(560, 750, 54, 22) + "".join(f'<circle cx="{x}" cy="{y}" r="6" stroke-width="1.2"/><path d="M{x} {y - 6} Q{x + 4} {y - 16} {x + 8} {y - 18}" fill="none" stroke-width="1"/>' for x, y in ((548, 726), (562, 722), (576, 728))))
    b.append('<path d="M456 750 V706 Q456 696 466 696 H478 Q488 696 488 706 V750 Z" stroke-width="1.7"/><path d="M488 712 Q500 714 498 728 Q496 738 488 738" fill="none" stroke-width="2.4"/>')
    # Pip below holding up the basket
    qx, qy, qs = 336, 680, 1.4
    b.append(char("pi", qx, qy, qs, arms=(14, None), mood="happy", wag=True, head_rot=-8))
    hx, hy = paw("pi", qx, qy, qs, "R", -150)
    b.append(apple(hx + 6, hy + 2, 11) + apple(hx + 30, hy, 11) + pear(hx + 50, hy + 4, 9))
    b.append(basket(hx + 28, hy + 46, 82, 40, handle=True))
    b.append(dot(hx + 30, hy - 20, 0.9))
    b.append(arms_only("pi", qx, qy, qs, (None, -150)))
    return "".join(b)


def svg():
    return page(build(), TITLE)
