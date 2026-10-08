"""Page 9 — Sofa Pile (Bramble, Pip upside-down, Tofu; Miso on the backrest)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import picture, cushion, rug_round

TITLE = "Page 9 — Sofa Pile"


def granny(x, y, w):
    c = w / 2
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{w}" stroke-width="1.3"/>'
            f'<rect x="{x + 6}" y="{y + 6}" width="{w - 12}" height="{w - 12}" stroke-width="0.9"/>'
            + "".join(f'<circle cx="{x + c + dx:.1f}" cy="{y + c + dy:.1f}" r="{w*0.11:.1f}" stroke-width="0.9"/>' for dx, dy in ((0, -w*0.15), (w*0.15, 0), (0, w*0.15), (-w*0.15, 0)))
            + f'<circle cx="{x + c}" cy="{y + c}" r="{w*0.08:.1f}" stroke-width="0.9"/>')


def build():
    b = []
    # wallpaper of small sprigs
    sprigs = ""
    for r, y in enumerate(range(60, 420, 52)):
        for x in range(50 + (26 if r % 2 else 0), 600, 52):
            sprigs += (f'<g transform="translate({x} {y})" stroke-width="0.9"><path d="M0 8 Q1 0 0 -8" fill="none"/>'
                       '<path d="M0 2 Q-7 -1 -7 -6 Q-1 -4 0 2 Z"/><path d="M0 -2 Q7 -5 7 -10 Q1 -8 0 -2 Z"/></g>')
    b.append(clip_d("M30 30 H600 V430 H30 Z", sprigs, 1.2))
    b.append('<rect x="30" y="426" width="570" height="12" stroke-width="1.5"/>')
    # three framed pictures: a tree, a mountain, a teacup
    b.append(picture(150, 190, 84, 104, "tree") + picture(310, 160, 112, 86, "mountain") + picture(470, 190, 84, 104, "teacup"))
    b.append(dot(312, 108))
    # sofa back and rolled arms
    b.append('<path d="M70 500 V320 Q70 286 110 284 H510 Q550 286 550 320 V500 Z" stroke-width="2.2"/>')
    b.append(lines("M200 290 V490 M310 290 V490 M420 290 V490", 1.0))
    # Miso napping along the backrest
    b.append(char("mi", 446, 254, 1.05, arms=(None, 10), rot=-90, mood="sleep"))
    b.append(cushion(124, 436, 76, 64, "dots", -10, tassel=True) + cushion(216, 432, 70, 60, "zigzag", 6)
             + cushion(318, 428, 66, 58, "heart", -4) + cushion(410, 432, 70, 60, "stripes", 5) + cushion(500, 436, 76, 64, "flower", 10))
    b.append('<path d="M86 500 H534 V566 H86 Z" stroke-width="2"/>' + lines("M86 512 H534 M236 512 V566 M386 512 V566", 1.1))
    # Bramble (left) and Tofu (right) sunk into the cushions
    b.append(char("br", 168, 560, 1.0, arms=(30, -18), sit=True, mood="happy"))
    b.append(char("to", 452, 566, 1.0, arms=(18, -30), sit=True))
    b.append('<path d="M44 600 H576 V618 H44 Z" stroke-width="1.8"/><path d="M70 618 L66 640 H86 L84 618 Z M536 618 L534 640 H554 L550 618 Z" stroke-width="1.6"/>')
    # crocheted granny-square throw across their laps
    throw = "M110 556 Q200 540 300 552 Q400 566 520 556 L528 676 Q420 690 300 682 Q190 690 102 676 Z"
    gs = "".join(granny(x, y, 46) for x in range(96, 540, 46) for y in range(540, 700, 46))
    b.append(clip_d(throw, gs, 2))
    b.append("".join(f'<path d="M{x} {682 + (x % 3)} l-3 14 M{x} {682 + (x % 3)} l3 14" fill="none" stroke-width="1.2"/>' for x in range(116, 524, 24)))
    # Pip flopped upside-down in the middle, legs in the air
    b.append(char("pi", 308, 420, 1.0, arms=(200, 160), rot=180, mood="happy", wag=False))
    # rolled arms over everything at the sides
    b.append('<path d="M44 600 V430 Q44 392 82 392 Q118 392 118 430 V600 Z" stroke-width="2.2"/><circle cx="81" cy="428" r="22" stroke-width="1.5"/>'
             + lines("M81 418 a10 10 0 1 1 -8 12", 1.1))
    b.append('<path d="M502 600 V430 Q502 392 540 392 Q576 392 576 430 V600 Z" stroke-width="2.2"/><circle cx="539" cy="428" r="22" stroke-width="1.5"/>'
             + lines("M539 418 a10 10 0 1 0 8 12", 1.1))
    # floor, rug, footstool with slippers
    b.append('<path d="M30 640 H600 V800 H30 Z" stroke-width="1.5"/>' + lines("M30 680 H600 M30 724 H600", 0.9))
    b.append(rug_round(260, 712, 200, 40, 4))
    b.append('<path d="M420 690 Q420 660 470 660 H520 Q570 660 570 690 V716 H420 Z" stroke-width="2"/>' + lines("M420 696 H570", 1.1)
             + '<path d="M430 716 V740 H442 V716 M548 716 V740 H560 V716" stroke-width="1.6"/>')
    for x in (448, 506):
        b.append(f'<path d="M{x} 670 Q{x} 652 {x + 18} 652 Q{x + 36} 652 {x + 36} 670 Z" stroke-width="1.6"/><path d="M{x + 4} 662 Q{x + 18} 656 {x + 32} 662" fill="none" stroke-width="1"/>')
    return "".join(b)


def svg():
    return page(build(), TITLE)
