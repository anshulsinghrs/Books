"""Page 47 — Pajama Party (Juniper's den: pillows flying, sleeping bags like spokes)."""
from math import sin, cos, radians
from chars import char, arms_only, dot, page, paw, TORSO_BOX
from scene import clip_d, lines
from props import cushion, bowl, mug, icon, star_pts

TITLE = "Page 47 — Pajama Party"


def pj(c, kind):
    x0, y0, x1, y1 = TORSO_BOX[c]
    pts = [(x0 + (x1 - x0) * (i + 0.5) / 4 + (5 if j % 2 else 0), y0 + (y1 - y0) * (j + 0.6) / 4) for i in range(4) for j in range(4)]
    if kind == "stripes":
        return "".join(f'<path d="M{x0 - 5} {y0 + k*(y1 - y0)/6:.1f} H{x1 + 5}" stroke-width="1"/>' for k in range(1, 6))
    if kind == "checks":
        return "".join(f'<path d="M{x0 + k*(x1 - x0)/5:.1f} {y0} V{y1} M{x0} {y0 + k*(y1 - y0)/5:.1f} H{x1}" stroke-width="0.8"/>' for k in range(1, 5))
    ref = {"stars": "star5", "hearts": "heart", "moons": "crescent"}[kind]
    sc = {"stars": 0.4, "hearts": 0.55, "moons": 0.6}[kind]
    return "".join(f'<use href="#{ref}" transform="translate({x:.1f} {y:.1f}) scale({sc})" stroke-width="{1/sc:.2f}"/>' for x, y in pts)


def sleep_mask(x, y, w):
    return (f'<path d="M{x - w/2} {y} Q{x - w/2} {y - 10} {x - 6} {y - 8} Q{x} {y - 4} {x + 6} {y - 8} Q{x + w/2} {y - 10} {x + w/2} {y} '
            f'Q{x + w/4} {y + 8} {x} {y + 2} Q{x - w/4} {y + 8} {x - w/2} {y} Z" stroke-width="1.5"/>')


def sleeping_bag(cx, cy, ang, L=220, W=86, pat="dots"):
    d = f"M{-W/2} 40 V{L - 30} Q{-W/2} {L} 0 {L} Q{W/2} {L} {W/2} {L - 30} V40 Q{W/2} 20 0 20 Q{-W/2} 20 {-W/2} 40 Z"
    inner = {"dots": "".join(f'<circle cx="{x}" cy="{y}" r="4" stroke-width="1"/>' for x in range(-30, 40, 20) for y in range(60, L, 30)),
             "stripes": lines(" ".join(f"M{-W} {y} H{W}" for y in range(60, L, 22)), 1),
             "zigzag": lines(" ".join("M%d %d " % (-W, y) + " ".join(f"L{x} {y + (8 if (x // 12) % 2 else -8)}" for x in range(-W, W, 12)) for y in range(70, L, 40)), 1),
             "stars": "".join(f'<use href="#star4" transform="translate({x} {y}) scale(0.7)" stroke-width="1.5"/>' for x in (-20, 20) for y in range(70, L, 44)),
             "hearts": "".join(f'<use href="#heart" transform="translate({x} {y}) scale(0.8)" stroke-width="1.3"/>' for x in (-20, 20) for y in range(70, L, 44))}[pat]
    return (f'<g transform="translate({cx} {cy}) rotate({ang})">' + clip_d(d, inner, 2) +
            f'<path d="M{-W/2} 52 Q0 40 {W/2} 52" fill="none" stroke-width="1.4"/></g>')


def feather(x, y, rot, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.2/s:.2f}"><path d="M0 0 C-8 -10 -6 -26 2 -34 C8 -24 8 -10 0 0 Z"/>'
            '<path d="M0 4 V-30 M0 -10 L-4 -16 M0 -18 L4 -24" fill="none" stroke-width="0.8"/></g>')


def build():
    b = []
    # low ceiling beams and the paper-star garland (Dot on the garland)
    b.append(clip_d("M30 30 H600 V90 H30 Z", lines("M30 60 H600", 1) + lines(" ".join(f"M{x} 30 V90" for x in range(80, 600, 120)), 1.4), 2))
    gl = "M30 110 Q310 190 600 110"
    b.append(f'<path d="{gl}" fill="none" stroke-width="1.4"/>')
    for k in range(1, 10):
        t = k / 10
        x = (1 - t)**2 * 30 + 2 * (1 - t) * t * 310 + t * t * 600
        y = (1 - t)**2 * 110 + 2 * (1 - t) * t * 190 + t * t * 110
        b.append(f'<path d="{star_pts(x, y + 16, 16, 7)}" stroke-width="1.5"/>' + lines(f"M{x:.1f} {y + 16:.1f} L{x:.1f} {y:.1f}", 0.9))
    b.append(dot(186, 136, 0.85))
    # board game box from page 19 in the corner
    b.append('<rect x="490" y="196" width="96" height="30" rx="3" stroke-width="1.8"/>' + lines("M490 206 H586", 1) + icon("star", 538, 216, 0.5))
    b.append('<rect x="496" y="226" width="88" height="28" rx="3" stroke-width="1.8"/>' + icon("mushroom", 540, 242, 0.45))
    # sleeping bags radiating out from the centre like spokes
    for (ang, pat) in ((200, "dots"), (240, "stripes"), (120, "zigzag"), (160, "stars"), (80, "hearts")):
        b.append(sleeping_bag(310, 470, ang, 230, 86, pat))
    b.append('<circle cx="310" cy="470" r="40" stroke-width="2"/>')
    b.append(bowl(310, 486, 70, 30))
    for k in range(6):
        b.append(f'<path d="M{284 + k*10} {454 - (k % 2)*6} q-6 -6 0 -11 q4 -6 10 -2 q6 -3 7 4 q4 6 -3 9 q-4 4 -9 0 Z" stroke-width="1.1"/>')
    # the friends in pajamas (masks pushed up), pillows mid-air
    b.append(char("ju", 120, 420, 1.15, arms=(14, -160), sweater=pj("ju", "stars"), mood="happy"))
    b.append(sleep_mask(120, 420 - 136 * 1.15, 54))
    b.append(char("cl", 490, 430, 1.15, arms=(160, -14), sweater=pj("cl", "hearts"), mood="happy"))
    b.append(sleep_mask(490, 430 - 116 * 1.15, 48))
    b.append(char("mi", 140, 700, 1.25, arms=(30, -30), sweater=pj("mi", "moons"), sit=True, mood="happy"))
    b.append(mug(140, 690, 1.0, "dots", steam=True))
    b.append(char("pi", 480, 700, 1.2, arms=(150, -40), sweater=pj("pi", "stripes"), mood="happy", wag=True))
    b.append(char("th", 330, 612, 1.4, arms=(150, -150), sweater=pj("th", "checks"), mood="happy"))
    b.append(sleep_mask(330, 612 - 56 * 1.4, 26))
    b.append(mug(250, 600, 0.9, "stars") + mug(390, 606, 0.9, "hearts"))
    # pillows arcing from the left to the upper right, feathers floating
    b.append(cushion(170, 260, 80, 56, "stripes", -20) + cushion(300, 220, 74, 52, "dots", 10) + cushion(430, 262, 80, 56, "heart", 20))
    b.append(lines("M120 300 Q160 220 220 190 M380 190 Q440 210 470 240", 1.2))
    for (x, y, r) in ((240, 170, 30), (360, 150, -40), (220, 330, 60), (400, 330, -20), (520, 320, 40), (90, 230, -30), (300, 330, 10)):
        b.append(feather(x, y, r))
    # slippers
    b.append('<path d="M40 760 Q40 740 60 740 Q80 740 80 760 Z M86 760 Q86 742 104 742 Q122 742 122 760 Z" stroke-width="1.6"/>')
    return "".join(b)


def svg():
    return page(build(), TITLE)
