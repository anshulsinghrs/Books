"""Page 45 — Counting Stars on Lantern Hill (winter night)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, pine, cottage_small, tuft
from props import star, mug, lantern_hanging, icon

TITLE = "Page 45 — Counting Stars on Lantern Hill"


def constellation(pts, closed=False):
    d = "M" + " L".join(f"{x} {y}" for x, y in pts) + (" Z" if closed else "")
    return (f'<path d="{d}" fill="none" stroke-width="1" stroke-dasharray="3 5"/>'
            + "".join(f'<use href="#star4" transform="translate({x} {y}) scale(0.55)" stroke-width="2"/>' for x, y in pts))


def build():
    b = []
    # big moon with craters, cloud band
    b.append('<circle cx="470" cy="130" r="58" stroke-width="2"/><circle cx="450" cy="112" r="12" stroke-width="1.2"/><circle cx="490" cy="150" r="9" stroke-width="1.2"/><circle cx="478" cy="104" r="6" stroke-width="1.1"/>')
    b.append('<path d="M40 330 Q120 300 200 320 Q260 290 340 318 Q420 296 500 322 Q560 306 600 320 V352 Q500 360 400 346 Q300 360 200 348 Q120 360 40 350 Z" stroke-width="1.5"/>')
    # constellations shaped like a teacup, an acorn, a fish and a crescent
    b.append(constellation([(80, 120), (150, 120), (140, 170), (90, 170)], True) + constellation([(150, 130), (176, 144), (148, 158)]))
    b.append(constellation([(250, 70), (280, 60), (310, 70), (300, 110), (280, 126), (260, 110)], True))
    b.append(constellation([(220, 230), (260, 210), (300, 230), (260, 250), (220, 230), (200, 214), (200, 246)]))
    b.append(constellation([(390, 220), (360, 250), (370, 290), (410, 300), (384, 274), (382, 244), (390, 220)]))
    # stars in three sizes
    for (x, y, s, k) in ((60, 60, 1.0, 5), (190, 90, 0.7, 4), (350, 50, 1.1, 5), (560, 60, 0.8, 4), (380, 140, 0.6, 5), (540, 230, 1.0, 5), (120, 260, 0.8, 4),
                         (330, 280, 0.6, 4), (460, 270, 0.7, 5), (60, 200, 0.6, 5), (580, 160, 0.6, 4), (230, 160, 0.5, 5)):
        b.append(star(x, y, s * 1.6, k))
    # snowy hill
    b.append('<path d="M30 520 C150 460 300 470 420 520 C500 552 560 560 600 556 V800 H30 Z" stroke-width="1.8"/>')
    b.append('<path d="M180 800 C240 650 420 600 600 610 V800 Z" stroke-width="1.5"/>')
    # the Hollow's lit windows far below (lower right)
    for (x, y) in ((420, 680), (470, 700), (530, 672), (560, 720), (380, 730), (500, 740)):
        b.append(cottage_small(x, y, 22) + f'<rect x="{x + 2}" y="{y - 11}" width="6" height="5" stroke-width="1"/>')
    # the lone pine on the right edge
    b.append('<rect x="550" y="500" width="14" height="70" stroke-width="1.7"/>')
    b.append(pine(557, [(330, 410, 34), (380, 470, 50), (430, 530, 62)], 1.7, 4))
    # Tofu wrapped in a blanket, pointing; Miso at the telescope (Dot on the tip)
    b.append(lines("M90 520 L130 420 M170 520 L130 420 M130 520 L130 420", 2.4))
    b.append('<path d="M102 432 L196 368 L206 384 L112 448 Z" stroke-width="2"/><path d="M196 362 L214 352 L222 368 L206 384 Z" stroke-width="1.8"/><circle cx="130" cy="420" r="6" stroke-width="1.5"/>')
    b.append(dot(220, 343, 0.9))
    b.append(char("mi", 104, 520, 1.05, arms=(160, -130), head_rot=-10))
    tx, ty, ts = 300, 556, 1.0
    b.append(char("to", tx, ty, ts, arms=(None, -160), sit=True))
    blanket = f"M{tx - 70} {ty - 70} Q{tx - 40} {ty - 104} {tx - 20} {ty - 80} Q{tx} {ty - 64} {tx + 30} {ty - 80} Q{tx + 70} {ty - 70} {tx + 70} {ty + 16} H{tx - 74} Z"
    b.append(clip_d(blanket, lines(" ".join(f"M{x} {ty - 110} V{ty + 10}" for x in range(tx - 70, tx + 80, 16)), 1), 2))
    b.append(f'<use href="#to-pendant" transform="translate({tx} {ty}) scale({ts})" stroke-width="{2/ts:.2f}"/>')
    # thermos, two cups, star map with icons only, lantern
    b.append('<rect x="380" y="510" width="22" height="46" rx="5" stroke-width="1.7"/><rect x="378" y="502" width="26" height="12" rx="3" stroke-width="1.6"/>')
    b.append(mug(420, 558, 0.8, "stars") + mug(446, 562, 0.8, "dots"))
    b.append('<path d="M200 580 L280 570 L286 610 L206 620 Z" stroke-width="1.6"/>' + icon("star", 226, 590, 0.4) + icon("moon", 262, 588, 0.4) + lines("M220 606 L266 600", 0.9).replace('fill="none"', 'fill="none" stroke-dasharray="2 3"'))
    b.append(lantern_hanging(60, 560, 0.9, 0))
    b.append("".join(tuft(x, y, 1) for x, y in ((40, 600), (160, 620), (300, 640), (100, 700), (250, 720))))
    return "".join(b)


def svg():
    return page(build(), TITLE)
