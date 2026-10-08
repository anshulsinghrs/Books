"""Page 12 — Bread Day (Bramble kneads, Thimble shapes a tiny loaf)."""
from chars import char, arms_only, dot, page, paw, apron
from scene import clip_d, lines, scallop_blob
from props import teapot, mug, jar

TITLE = "Page 12 — Bread Day"


def plate(x, y, r, border):
    out = f'<circle cx="{x}" cy="{y}" r="{r}" stroke-width="1.7"/><circle cx="{x}" cy="{y}" r="{r*0.62:.1f}" stroke-width="1.1"/>'
    if border == "dots":
        out += "".join(f'<circle cx="{x + r*0.8*__import__("math").cos(a*0.5236):.1f}" cy="{y + r*0.8*__import__("math").sin(a*0.5236):.1f}" r="2.4" stroke-width="0.9"/>' for a in range(12))
    elif border == "zigzag":
        import math
        pts = [(x + (r*0.88 if k % 2 else r*0.7)*math.cos(k*math.pi/12), y + (r*0.88 if k % 2 else r*0.7)*math.sin(k*math.pi/12)) for k in range(24)]
        out += f'<path d="M{" L".join(f"{a:.1f} {b_:.1f}" for a, b_ in pts)} Z" fill="none" stroke-width="0.9"/>'
    elif border == "scallop":
        out += f'<use href="#scallop" transform="translate({x} {y}) scale({r*0.085:.2f})" fill="none" stroke-width="{0.9/(r*0.085):.2f}"/>'
    elif border == "heart":
        out += f'<use href="#heart" transform="translate({x} {y}) scale({r/24:.2f})" stroke-width="{1.0*24/r:.2f}"/>'
    return out


def build():
    b = []
    # hutch in the background
    b.append('<path d="M300 70 H576 V560 H300 Z" stroke-width="2.2"/><path d="M290 60 H590 V78 H290 Z" stroke-width="2"/>')
    b.append(clip_d("M312 86 H564 V440 H312 Z", lines("M312 210 H564 M312 330 H564", 2), 1.6))
    for (x, y, r, k) in ((350, 160, 34, "dots"), (430, 156, 38, "zigzag"), (512, 160, 34, "scallop"),
                         (360, 280, 30, "heart"), (432, 278, 34, "plain"), (510, 280, 30, "dots")):
        b.append(plate(x, y, r, k))
    b.append(lines("M312 198 H564 M312 318 H564", 1))
    b.append(teapot(370, 430, 0.75) + mug(450, 430, 0.85, "stripes") + mug(492, 430, 0.85, "hearts") + jar(536, 430, 28, 40, "flower"))
    b.append('<rect x="312" y="448" width="252" height="104" stroke-width="1.6"/>' + lines("M438 448 V552", 1.6)
             + '<circle cx="426" cy="500" r="4" stroke-width="1.3"/><circle cx="450" cy="500" r="4" stroke-width="1.3"/>')
    # Bramble kneading behind the table
    bx, by, bs = 186, 660, 1.6
    b.append(char("br", bx, by, bs, arms=(None, None), outfit=apron("br", bs), mood="happy"))
    # flour sack
    b.append('<path d="M46 560 Q38 470 64 440 L72 424 L96 430 L104 446 Q130 470 120 560 Z" stroke-width="1.9"/>'
             + lines("M66 440 Q84 452 102 446", 1.2) + '<use href="#star4" transform="translate(84 506) scale(1.4)" stroke-width="1"/>')
    # table
    b.append(clip_d("M30 540 H600 V610 H30 Z", lines("M60 560 Q140 556 220 562 M380 590 Q460 586 560 592", 1), 2.2))
    b.append('<rect x="30" y="610" width="570" height="24" stroke-width="2"/>')
    cloth = "M30 634 H600 V700 " + " ".join(f"Q{x - 24} 716 {x - 48} 700" for x in range(600, 20, -48)) + " Z"
    b.append(clip_d(cloth, lines(" ".join(f"M{x} 634 V720" for x in range(54, 600, 48)), 1.1), 1.8))
    b.append('<path d="M60 706 H90 V780 H60 Z M530 706 H560 V780 H530 Z" stroke-width="2"/>')
    # dough ball under Bramble's paws
    b.append('<path d="M136 560 Q130 520 186 516 Q242 520 236 560 Q186 572 136 560 Z" stroke-width="2"/>' + lines("M160 536 Q176 528 192 534", 1))
    b.append(arms_only("br", bx, by, bs, (-26, 26)))
    # three bowls of rising dough under striped cloths
    for x in (300, 372, 444):
        b.append(f'<path d="M{x - 32} 556 Q{x - 30} 580 {x} 582 Q{x + 30} 580 {x + 32} 556 Z" stroke-width="1.8"/>')
        cloth = f"M{x - 36} 558 Q{x - 30} 524 {x} 520 Q{x + 30} 524 {x + 36} 558 Q{x + 20} 552 {x + 8} 562 Q{x - 10} 552 {x - 36} 558 Z"
        b.append(clip_d(cloth, lines(f"M{x - 20} 510 L{x - 30} 570 M{x - 6} 510 L{x - 12} 570 M{x + 8} 510 L{x + 6} 570 M{x + 22} 510 L{x + 24} 570", 1), 1.6))
    # braided loaf and round loaf with a scored leaf
    b.append('<ellipse cx="536" cy="566" rx="36" ry="24" stroke-width="1.9"/>' + lines("M536 548 V586 M536 556 L520 546 M536 556 L552 546 M536 568 L516 558 M536 568 L556 558 M536 580 L522 572 M536 580 L550 572", 1.1))
    b.append('<path d="M470 600 C464 590 480 582 492 588 C500 578 516 580 518 590 C530 584 544 590 540 602 C548 610 536 620 526 614 '
             'C518 624 500 624 496 614 C486 622 470 618 474 608 C464 610 462 602 470 600 Z" stroke-width="1.8"/>'
             + lines("M486 590 Q490 604 484 614 M506 586 Q512 600 506 616 M526 590 Q530 604 524 614", 1))
    # rolling pin (Dot on its handle)
    b.append('<rect x="250" y="590" width="120" height="20" rx="9" stroke-width="1.9"/><rect x="226" y="595" width="26" height="10" rx="5" stroke-width="1.6"/><rect x="368" y="595" width="26" height="10" rx="5" stroke-width="1.6"/>')
    b.append(dot(382, 586.5))
    # Thimble in a little flour cloud, shaping her tiny loaf
    b.append(scallop_blob(448, 640, 46, 30, 9, 0.35, 1.3))
    b.append(char("th", 448, 664, 1.5, arms=(-40, 40), mood="happy"))
    b.append('<ellipse cx="448" cy="652" rx="12" ry="7" stroke-width="1.4"/>' + lines("M442 650 l4 -3 M448 650 l4 -3", 0.8))
    b.append(arms_only("th", 448, 664, 1.5, (-40, 40)))
    return "".join(b)


def svg():
    return page(build(), TITLE)
