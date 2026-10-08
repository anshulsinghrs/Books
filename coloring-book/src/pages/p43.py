"""Page 43 — By the Stove (first frosty evening; the quilt nearly finished)."""
from math import sin, cos, radians
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import stove, kettle, mug, quilt_patch, SYMBOLS, icon

TITLE = "Page 43 — By the Stove"


def frost_fern(x, y, rot, s=1.0):
    fr = "".join(f'<path d="M0 {-k*8} l-6 -6 M0 {-k*8} l6 -6" />' for k in range(1, 6))
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" fill="none" stroke-width="{1/s:.2f}"><path d="M0 0 V-46"/>{fr}</g>'


def orange_slice(x, y, r=9):
    seg = " ".join(f"M{x} {y} L{x + r*0.75*cos(radians(a)):.1f} {y + r*0.75*sin(radians(a)):.1f}" for a in range(0, 360, 60))
    return f'<circle cx="{x}" cy="{y}" r="{r}" stroke-width="1.3"/>' + lines(seg, 0.8)


def build():
    b = []
    # wall and floor
    b.append(clip_d("M30 30 H600 V560 H30 Z", lines(" ".join(f"M{x} 30 V560" for x in range(70, 600, 46)), 0.9), 1.4))
    b.append(clip_d("M30 560 H600 V800 H30 Z", lines("M30 610 H600 M30 680 H600", 1), 1.6))
    # frosted window, upper left
    b.append('<rect x="60" y="70" width="190" height="200" rx="4" stroke-width="2.2"/>')
    frost = "".join(frost_fern(x, y, r, 1.0) for x, y, r in ((80, 180, 30), (100, 250, 10), (226, 120, -150), (236, 250, -20), (150, 160, 60), (190, 230, -60)))
    b.append(clip_d("M68 78 H242 V262 H68 Z", '<use href="#star4" transform="translate(120 110) scale(0.8)" stroke-width="1.5"/><use href="#star5" transform="translate(196 140) scale(0.7)" stroke-width="1.6"/>' + frost
                    + lines("M155 78 V262 M68 170 H242", 2.2), 1.4, fill="#fff"))
    b.append('<rect x="50" y="268" width="210" height="12" rx="3" stroke-width="1.8"/>')
    # the stove (centre right) with pipe elbow (Dot), kettle and the pot of spiced cider
    b.append('<rect x="408" y="140" width="24" height="90" stroke-width="1.8"/><path d="M408 140 Q408 110 438 110 H600 V134 H438 Q432 134 432 140 Z" stroke-width="1.8"/>')
    b.append('<rect x="402" y="112" width="36" height="14" rx="3" stroke-width="1.6"/>')
    b.append(dot(420, 101, 0.9))
    b.append(stove(420, 400, 190, 200, pipe_to=230))
    b.append(kettle(372, 400, 0.9, steam=True))
    b.append('<path d="M436 400 V362 H506 V400 Z" stroke-width="1.8"/><rect x="430" y="354" width="82" height="10" rx="3" stroke-width="1.6"/>'
             + lines("M444 352 L452 326 M460 352 L468 320", 3) + orange_slice(480, 344, 9) + orange_slice(496, 348, 8)
             + '<use href="#star5" transform="translate(462 340) scale(0.6)" stroke-width="1.8"/>')
    # log basket and mittens
    b.append('<path d="M530 600 H590 L584 650 H536 Z" stroke-width="1.8"/>' + lines("M532 616 H588 M534 632 H586", 1)
             + "".join(f'<ellipse cx="{x}" cy="590" rx="9" ry="8" stroke-width="1.5"/>' for x in (540, 560, 580)))
    b.append('<path d="M340 270 Q330 250 344 246 L346 236 Q352 232 356 238 L358 246 Q370 252 362 272 Z" stroke-width="1.5"/>' + lines("M340 262 H362", 1))
    b.append(lines("M330 230 H380", 1.4))
    # sheepskin rug
    b.append('<path d="M150 640 Q140 600 200 594 Q300 584 400 596 Q470 604 460 644 Q470 690 400 700 Q300 712 200 702 Q140 690 150 640 Z" stroke-width="1.8"/>'
             + lines(" ".join(f"M{x} {y} q6 -6 12 0" for x in range(180, 440, 30) for y in (620, 650, 680)), 1))
    # friends in a warm semicircle: Juniper, Miso, Tofu with mugs
    for (c, x, y, s, a, pat) in (("ju", 270, 600, 1.1, (-40, 40), "stripes"), ("mi", 340, 640, 1.15, (-40, 40), "hearts"), ("to", 520, 560, 1.0, (-40, 40), "stars")):
        b.append(char(c, x, y, s, arms=(None, None), sit=True, mood="happy" if c == "mi" else "open"))
        lx, ly = paw(c, x, y, s, "L", a[0])
        rx, ry = paw(c, x, y, s, "R", a[1])
        b.append(mug((lx + rx) / 2, max(ly, ry) + 8, 1.1, pat, steam=True))
        b.append(arms_only(c, x, y, s, a))
    # plate of shortbread
    b.append('<ellipse cx="430" cy="700" rx="46" ry="12" stroke-width="1.7"/>' + "".join(f'<rect x="{x}" y="{686}" width="20" height="14" rx="2" stroke-width="1.3"/>' for x in (406, 428, 450))
             + lines("M412 690 h2 M418 694 h2 M434 690 h2 M440 694 h2 M456 690 h2", 1.2))
    # the nearly finished quilt across Thimble's lap and spilling over the floor
    q = "M30 600 Q100 560 190 580 L250 760 H30 Z"
    patches = "".join(quilt_patch(30 + (i % 3) * 72 - (i // 3) * 10, 572 + (i // 3) * 64, 66, 60, sym) for i, sym in enumerate(SYMBOLS[:6]))
    patches += quilt_patch(60, 700, 66, 60, SYMBOLS[6]) + quilt_patch(130, 700, 66, 60, SYMBOLS[7])
    b.append(clip_d(q, patches, 2.2))
    b.append(f'<path d="M36 606 Q100 568 186 588" fill="none" stroke-width="1" stroke-dasharray="4 3"/>')
    b.append(char("th", 160, 586, 1.4, arms=(-150, 30), mood="happy"))
    b.append(lines("M150 556 L136 544", 1.2) + lines("M136 544 C120 530 110 560 130 572", 1))
    return "".join(b)


def svg():
    return page(build(), TITLE)
