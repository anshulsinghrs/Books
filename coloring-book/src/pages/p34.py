"""Page 34 — Lazy Afternoon at Lilypad Pond."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, blossom
from props import duck, sun_hat, icon

TITLE = "Page 34 — Lazy Afternoon at Lilypad Pond"


def lily_pad(x, y, r=28, flower=False):
    ry = r * 0.45
    out = (f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{ry:.1f}" stroke-width="1.6"/>'
           f'<path d="M{x} {y} L{x + r + 2} {y - ry*0.5:.1f} L{x + r + 2} {y + ry*0.5:.1f} Z" fill="#fff" stroke="none"/>'
           + lines(f"M{x + r*0.96:.1f} {y - ry*0.42:.1f} L{x} {y} L{x + r*0.96:.1f} {y + ry*0.42:.1f} M{x} {y} L{x - r*0.7:.1f} {y - ry*0.4:.1f} M{x} {y} L{x - r*0.6:.1f} {y + ry*0.5:.1f}", 1.0))
    if flower:
        out += "".join(f'<path transform="translate({x - 4} {y - 4}) rotate({a})" d="M0 0 C-5 -6 -4 -14 0 -18 C4 -14 5 -6 0 0 Z" stroke-width="1.2"/>' for a in (-50, -25, 0, 25, 50))
    return out


def cattail(x, y, h=150, lean=0):
    return (f'<path d="M{x} {y} Q{x + lean*0.4} {y - h*0.5} {x + lean} {y - h}" fill="none" stroke-width="2"/>'
            f'<rect x="{x + lean - 7}" y="{y - h - 4}" width="14" height="40" rx="7" stroke-width="1.8"/>'
            f'<path d="M{x} {y - 20} Q{x - 20} {y - 70} {x - 10} {y - 120} Q{x - 8} {y - 70} {x} {y - 20} Z" stroke-width="1.3"/>')


def dragonfly(x, y, rot=0):
    wing = "M0 0 C10 -16 34 -18 40 -10 C34 -2 14 0 0 0 Z"
    return (f'<g transform="translate({x} {y}) rotate({rot})" stroke-width="1.3">'
            f'<path d="{wing}"/><path d="{wing}" transform="scale(-1 1)"/><path d="{wing}" transform="scale(1 -0.8)"/><path d="{wing}" transform="scale(-1 -0.8)"/>'
            '<path d="M12 -6 L24 -10 M-12 -6 L-24 -10" fill="none" stroke-width="0.8"/>'
            '<ellipse cy="18" rx="3" ry="22"/><circle cy="-6" r="5"/></g>')


def build():
    b = []
    # far bank and sky
    b.append('<use href="#cloud" transform="translate(150 80) scale(1.1)" stroke-width="1.4"/>')
    b.append('<path d="M30 230 C140 210 300 236 600 214 V800 H30 Z" stroke-width="1.6"/>')
    pond = "M30 290 C200 270 400 296 600 276 V800 H30 Z"
    b.append(clip_d(pond, lines("M70 340 q20 -6 40 0 M300 320 q20 -6 40 0 M110 470 q20 -6 40 0 M480 380 q20 -6 40 0", 1), 1.6))
    # the flat sunning rock and ducklings
    b.append('<path d="M60 310 Q70 280 140 284 Q200 288 196 312 Q130 324 60 310 Z" stroke-width="1.9"/>' + lines("M90 300 q20 -6 40 0", 1))
    b.append(duck(300, 330, 0.9) + duck(332, 338, 0.55) + duck(356, 342, 0.55) + duck(380, 346, 0.5))
    # Pebble floating on her back, lucky pebble on her tummy
    px, py = 400, 486
    b.append('<ellipse cx="400" cy="490" rx="110" ry="30" stroke-width="1.4"/><ellipse cx="400" cy="490" rx="150" ry="44" stroke-width="1.1"/>')
    b.append(char("pb", px + 50, py - 2, 1.45, arms=(-30, 30), rot=-90, mood="happy"))
    b.append('<ellipse cx="420" cy="468" rx="13" ry="9" stroke-width="1.6"/><ellipse cx="415" cy="465" rx="4" ry="2.4" stroke-width="0.9"/>')
    # lily pads and flowers
    b.append(lily_pad(250, 410, 30, True) + lily_pad(540, 430, 26) + lily_pad(330, 600, 34, True) + lily_pad(520, 560, 28, True) + lily_pad(200, 520, 24))
    b.append(dragonfly(220, 230, 20) + dragonfly(480, 300, -15))
    # cattails at the water's edge (Dot perches on one)
    b.append(cattail(560, 680, 200, -10) + cattail(530, 700, 160, 10) + cattail(586, 700, 140, 6))
    b.append(dot(552, 466, 0.95))
    # the wooden dock entering diagonally from the lower left
    dock = "M30 600 L240 560 L330 740 L30 800 Z"
    b.append(clip_d(dock, lines(" ".join(f"M{30 + k*30} {600 - k*6} L{30 + k*30 + 60} {800 - k*12}" for k in range(-3, 12)), 1.1), 2.2))
    b.append('<path d="M236 562 L246 600 L330 740 L322 744 L236 600 Z" stroke-width="1.6"/><rect x="226" y="560" width="14" height="70" stroke-width="1.6"/>')
    # Tofu on the dock, feet dangling, fishing rod resting beside him
    tx, ty, ts = 200, 640, 1.15
    b.append(lines("M230 610 L360 380", 3) + lines("M360 380 Q380 460 370 540", 1))
    b.append('<circle cx="370" cy="548" r="7" stroke-width="1.5"/>' + lines("M363 548 H377", 1))
    b.append(char("to", tx, ty, ts, arms=(20, -20), sit=True, mood="sleep"))
    b.append(sun_hat(tx, ty - 166 * ts + 20, 110))
    # bucket on the dock
    b.append('<path d="M80 650 H124 L118 700 H86 Z" stroke-width="1.8"/><ellipse cx="102" cy="650" rx="22" ry="6" stroke-width="1.5"/><path d="M80 650 Q102 620 124 650" fill="none" stroke-width="1.6"/>')
    # weeping willow branches draping from the top right
    for k, x in enumerate(range(400, 640, 26)):
        end = 180 + (k % 3) * 40
        b.append(lines(f"M{x} 30 Q{x - 10} {end / 2:.0f} {x - 4} {end}", 1.4))
        for j in range(4):
            yy = 50 + j * (end - 50) / 4
            b.append(f'<ellipse cx="{x - 4 - (j % 2) * 8}" cy="{yy:.0f}" rx="4" ry="12" transform="rotate({20 if j % 2 else -20} {x - 4 - (j % 2) * 8} {yy:.0f})" stroke-width="1.1"/>')
    return "".join(b)


def svg():
    return page(build(), TITLE)
