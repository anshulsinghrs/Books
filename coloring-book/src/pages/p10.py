"""Page 10 — Hanging the Bunting (Juniper on the stepladder, Pebble steadies it)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, blossom
from props import bunting, picture, basket, icon

TITLE = "Page 10 — Hanging the Bunting"


def frame(x, y, w, h, fancy=False, kind=None):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" stroke-width="1.9"/><rect x="{x + 8}" y="{y + 8}" width="{w - 16}" height="{h - 16}" stroke-width="1.1"/>'
    if fancy:
        for cx, cy in ((x, y), (x + w, y), (x, y + h), (x + w, y + h)):
            out += f'<circle cx="{cx}" cy="{cy}" r="7" stroke-width="1.4"/><circle cx="{cx}" cy="{cy}" r="3" stroke-width="1"/>'
    if kind:
        out += picture(x + w / 2, y + h / 2, w - 16, h - 16, kind, 1.1)
    return out


def build():
    b = []
    # floor planks in perspective (low angle)
    b.append(clip_d("M30 640 H600 V800 H30 Z", lines(" ".join(f"M{310 + (x - 310) * 0.35:.0f} 640 L{x} 800" for x in range(-300, 940, 70)) + " M30 690 H600", 1.0), 1.8))
    b.append('<rect x="30" y="626" width="570" height="14" stroke-width="1.6"/>')
    # gallery wall: some frames filled, some still empty
    b.append(frame(70, 250, 92, 116, True, "flower") + frame(178, 220, 120, 88) + frame(178, 324, 56, 70, False, "heart")
             + frame(246, 324, 52, 70) + frame(70, 384, 92, 74, False, "mountain") + frame(178, 412, 120, 74, True))
    # string of bulb lights and the bunting drooping across the top
    lights = "M40 92 Q220 190 420 118"
    b.append(f'<path d="{lights}" fill="none" stroke-width="1.4"/>')
    for k in range(1, 9):
        t = k / 9
        x = (1 - t)**2 * 40 + 2 * (1 - t) * t * 220 + t * t * 420
        y = (1 - t)**2 * 92 + 2 * (1 - t) * t * 190 + t * t * 118
        b.append(f'<rect x="{x - 4:.1f}" y="{y:.1f}" width="8" height="7" stroke-width="1.1"/><path d="M{x - 6:.1f} {y + 7:.1f} Q{x - 8:.1f} {y + 20:.1f} {x:.1f} {y + 22:.1f} Q{x + 8:.1f} {y + 20:.1f} {x + 6:.1f} {y + 7:.1f} Z" stroke-width="1.2"/>')
    jpx, jpy = paw("ju", 464, 400, 1.15, "L", 150)
    b.append(bunting([(40, 54), (200, 170), (round(jpx), round(jpy))], ("star", "heart", "leaf", "flower"), 30))
    b.append(dot(150, 131))
    # wooden stepladder
    b.append('<path d="M384 720 L456 300 H472 L412 720 Z M560 720 L486 300 H470 L538 720 Z" stroke-width="2"/>')
    for (y, xl, xr) in ((620, 400, 540), (510, 418, 522), (400, 430, 500)):
        b.append(f'<rect x="{xl}" y="{y}" width="{xr - xl}" height="12" rx="2" stroke-width="1.8"/>')
    b.append('<rect x="446" y="288" width="52" height="16" rx="3" stroke-width="1.9"/>')
    # Juniper up the ladder, reaching left with the end of the bunting
    jx, jy, js = 464, 400, 1.15
    b.append(char("ju", jx, jy, js, arms=(150, -30), head_rot=-8, brows=True))
    # Pebble steadying the ladder and passing up a picture frame
    px, py, ps = 342, 744, 1.5
    b.append(char("pb", px, py, ps, arms=(None, -70), head_rot=6))
    fx, fy = paw("pb", px, py, ps, "L", 120)
    b.append(frame(fx - 64, fy - 40, 64, 54, False, "tree"))
    b.append(arms_only("pb", px, py, ps, (120, None)))
    # toolbox and basket of dried flowers on the floor
    b.append('<rect x="456" y="686" width="104" height="54" rx="4" stroke-width="2"/>' + lines("M456 704 H560", 1.2)
             + '<path d="M486 686 V672 H530 V686" fill="none" stroke-width="3"/><rect x="500" y="698" width="16" height="10" rx="2" stroke-width="1.2"/>'
             + '<path d="M470 686 L490 656 L496 660 L478 686 Z" stroke-width="1.3"/>')
    b.append(lines("M88 676 Q84 630 70 604 M100 676 Q100 620 104 596 M112 676 Q118 630 134 610", 1.2))
    for (x, y) in ((70, 600), (104, 590), (136, 606), (86, 620), (120, 618)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="9" stroke-width="1.1"/>')
    b.append(basket(100, 720, 80, 46, handle=False))
    return "".join(b)


def svg():
    return page(build(), TITLE)
