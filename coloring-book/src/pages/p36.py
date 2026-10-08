"""Page 36 — Cupcake Stand (Miso pipes, Pebble places a strawberry)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import cupcake, shaker, bowl, icon

TITLE = "Page 36 — Cupcake Stand"


def tier(x, y, rx):
    sc = " ".join(f"M{x - rx + k*12} {y + 8} a6 6 0 0 0 12 0" for k in range(int(2 * rx / 12)))
    return (f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{rx*0.16:.1f}" stroke-width="2"/>'
            f'<path d="M{x - rx} {y} V{y + 8} H{x + rx} V{y} Z" stroke-width="1.6"/>' + lines(sc, 1.1))


def strawberry(x, y, s=1.0):
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" stroke-width="{1.4/s:.2f}">'
            '<path d="M0 12 C-11 4 -11 -8 -4 -10 Q0 -11 4 -10 C11 -8 11 4 0 12 Z"/>'
            '<path d="M-6 -10 L-2 -16 L0 -11 L2 -16 L6 -10 Q0 -6 -6 -10 Z"/>'
            '<circle cx="-4" cy="-2" r="0.9" fill="#000" stroke="none"/><circle cx="4" cy="0" r="0.9" fill="#000" stroke="none"/><circle cx="0" cy="5" r="0.9" fill="#000" stroke="none"/></g>')


def build():
    b = []
    # wall with a scalloped shelf and hanging whisks; counter
    b.append(clip_d("M30 30 H600 V470 H30 Z", lines(" ".join(f"M30 {y} H600" for y in range(80, 470, 70)), 0.9) +
                    "".join(f'<use href="#heart" transform="translate({x + (35 if (y // 70) % 2 else 0)} {y + 35}) scale(0.45)" stroke-width="2.2"/>' for x in range(60, 600, 70) for y in range(10, 470, 70)), 1.4))
    b.append(clip_d("M30 470 H600 V800 H30 Z", lines("M30 520 H600 M60 600 Q160 594 260 600 M380 700 Q460 694 560 700", 1), 2))
    # the three-tier stand rising up the centre-left
    sx = 230
    b.append('<rect x="224" y="150" width="12" height="350" stroke-width="1.8"/><circle cx="230" cy="140" r="10" stroke-width="1.6"/>')
    b.append(tier(sx, 500, 150) + tier(sx, 360, 112) + tier(sx, 232, 76))
    b.append('<path d="M200 520 L190 540 H270 L260 520 Z" stroke-width="1.8"/>')
    tops = [("swirl", "berry", "cherry", "sprinkles"), ("flower", "flag", "blueberry"), ("swirl", "berry")]
    for (y, xs, tp) in ((500, (120, 190, 270, 340), tops[0]), (360, (160, 230, 300), tops[1]), (232, (196, 264), tops[2])):
        for x, t in zip(xs, tp):
            b.append(cupcake(x, y - 2, 1.25, t))
    b.append(dot(196, 151, 0.9))
    # Miso piping a towering swirl, piping bag in paw
    mx, my, ms = 470, 560, 1.75
    b.append(char("mi", mx, my, ms, arms=(None, None), head_rot=-6))
    lx, ly = paw("mi", mx, my, ms, "L", 120)
    b.append(f'<g transform="translate({lx:.1f} {ly:.1f}) rotate(-130) scale(1.7)" stroke-width="1.1"><path d="M-14 -40 L14 -40 L4 0 L-4 0 Z"/>'
             '<path d="M-14 -40 Q0 -50 14 -40" fill="none"/><path d="M-4 0 L0 10 L4 0 Z"/><path d="M-6 -20 H6" fill="none" stroke-width="1"/></g>')
    b.append(arms_only("mi", mx, my, ms, (120, -20)))
    b.append(cupcake(360, 640, 1.6, "swirl") + '<path d="M348 556 Q360 536 372 556 Z" stroke-width="1.4"/>')
    # Pebble on her stool placing a strawberry
    b.append('<path d="M48 760 L62 690 H140 L154 760 H142 L130 704 H72 L60 760 Z" stroke-width="1.8"/><rect x="54" y="680" width="94" height="14" rx="4" stroke-width="1.9"/>')
    px, py, ps = 100, 682, 1.6
    b.append(char("pb", px, py, ps, arms=(14, -150)))
    qx, qy = paw("pb", px, py, ps, "R", -150)
    b.append(strawberry(qx + 4, qy - 10, 1.2))
    b.append(arms_only("pb", px, py, ps, (None, -150)))
    # bowls of frosting, strawberries, blueberries, sprinkle shakers
    b.append(bowl(260, 640, 80, 34, "cream", "stripe"))
    b.append(bowl(250, 740, 76, 30) + strawberry(232, 708) + strawberry(254, 704) + strawberry(272, 710))
    b.append(bowl(370, 740, 66, 28, "berries"))
    b.append(shaker(470, 740, "star") + shaker(510, 744, "heart") + shaker(550, 740, "flower"))
    return "".join(b)


def svg():
    return page(build(), TITLE)
