"""Page 5 — Watering the Green Friends (Clover's sunroom plant stand)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, scallop_blob
from props import plant, plant_pot, icon

TITLE = "Page 5 — Watering the Green Friends"


def build():
    b = []
    # tall paned sunroom windows
    for x in (60, 230, 400):
        b.append(f'<rect x="{x}" y="50" width="150" height="520" rx="6" stroke-width="2"/>')
        b.append(clip_d(f"M{x+8} 58 H{x+142} V562 H{x+8} Z",
                        lines(f"M{x+75} 58 V562 M{x+8} 180 H{x+142} M{x+8} 310 H{x+142} M{x+8} 440 H{x+142}", 1.8)
                        + lines(f"M{x+20} 80 L{x+40} 110 M{x+30} 76 L{x+52} 108", 1), 1.4))
    b.append('<use href="#cloud" transform="translate(140 120) scale(0.8)" stroke-width="1.8"/>')
    b.append('<path d="M30 572 H600 V800 H30 Z" stroke-width="1.8"/>')
    b.append(clip_d("M30 572 H600 V800 H30 Z", lines(" ".join(f"M30 {y} H600" for y in range(612, 800, 40)) + " "
                    + " ".join(f"M{x + (40 if (y // 40) % 2 else 0)} {y} V{y+40}" for y in range(572, 800, 40) for x in range(30, 600, 80)), 1.0), 1.8))
    # macrame hanger with a trailing plant
    b.append(lines("M120 36 V70 M120 70 L92 150 M120 70 L148 150 M120 70 L120 150", 1.3))
    b.append("".join(f'<path d="M{x} {y} l5 -6 l5 6 l-5 6 Z" stroke-width="1"/>' for x, y in ((99, 120), (115, 116), (131, 120))))
    b.append(plant("vine", 120, 150, 0.9) + '<path d="M90 150 H150 Q150 182 120 184 Q90 182 90 150 Z" stroke-width="1.7"/>')
    # three-tier plant stand rising to the top of the page
    b.append('<path d="M330 120 L294 740 H306 L342 120 Z M494 120 L530 740 H518 L482 120 Z" stroke-width="1.9"/>')
    for (y, x0, x1) in ((300, 316, 508), (480, 304, 520), (640, 296, 528)):
        b.append(f'<rect x="{x0}" y="{y}" width="{x1 - x0}" height="12" rx="2" stroke-width="1.9"/>')
    b.append('<rect x="320" y="120" width="184" height="12" rx="2" stroke-width="1.9"/>')
    # top tier: tiny succulent + Thimble
    b.append(plant("succulent", 440, 108, 0.9) + plant_pot(440, 120, 26, 18, "dots"))
    b.append(char("th", 380, 120, 1.25, arms=(None, -128)))
    tx, ty = paw("th", 380, 120, 1.25, "R", -128)
    b.append(f'<g transform="translate({tx:.1f} {ty:.1f}) rotate(70)" stroke-width="1.3"><path d="M-6 -8 H6 L5 6 Q0 9 -5 6 Z"/>'
             '<circle cx="-2" cy="-3" r="1"/><circle cx="2" cy="0" r="1"/><circle cx="-1" cy="3" r="1"/></g>')
    b.append(arms_only("th", 380, 120, 1.25, (None, -128)))
    b.append(lines(f"M{tx + 8:.1f} {ty + 6:.1f} Q{tx + 18:.1f} {ty + 12:.1f} {tx + 22:.1f} {ty + 24:.1f}", 1))
    # middle tiers: fern (Dot hides among the fronds), round cactus, flowering pot, snake plant
    b.append(plant("fern", 350, 286, 0.95) + plant_pot(350, 300, 44, 36, "zigzag"))
    b.append(dot(366, 246))
    b.append(plant("cactus", 452, 286, 1.0) + plant_pot(452, 300, 40, 32, "stripes"))
    b.append(plant("flowers", 340, 466, 1.0) + plant_pot(340, 480, 44, 36, "scallops"))
    b.append(plant("snake", 412, 466, 0.95) + plant_pot(412, 480, 40, 34, "dots"))
    b.append(plant("herb", 478, 466, 1.1) + plant_pot(478, 480, 38, 30, "stripes"))
    # bottom tier: trailing vine, split-leaf, flowering pot
    b.append(plant("split", 410, 626, 0.85) + plant_pot(410, 640, 48, 38, "stripes"))
    b.append(plant("vine", 330, 628, 0.8) + plant_pot(330, 640, 40, 32, "dots"))
    b.append(plant("flowers", 490, 626, 0.9) + plant_pot(490, 640, 40, 32, "zigzag"))
    # Clover with the long-spout watering can, plant mister at her feet
    cx, cy, cs = 160, 744, 1.55
    b.append(char("cl", cx, cy, cs, arms=(12, -110), head_rot=-12))
    wx, wy = paw("cl", cx, cy, cs, "R", -110)
    b.append(f'<g transform="translate({wx:.1f} {wy:.1f}) rotate(-12)" stroke-width="1.8">'
             '<path d="M30 -14 L118 -54 L122 -46 L36 -2 Z"/><path d="M114 -60 L130 -52 L124 -40 L110 -48 Z"/>'
             '<path d="M-10 -30 H40 V20 Q40 28 15 28 Q-10 28 -10 20 Z"/><path d="M-10 -30 Q15 -44 40 -30" fill="none" stroke-width="1.2"/>'
             '<path d="M-10 -20 Q-30 -20 -30 0 Q-30 18 -10 16" fill="none" stroke-width="4"/>'
             '<path d="M-10 -20 Q-30 -20 -30 0 Q-30 18 -10 16" fill="none" stroke="#fff" stroke-width="1.4"/></g>')
    b.append(arms_only("cl", cx, cy, cs, (None, -110)))
    b.append("".join(f'<path d="M{x} {y} q2 4 0 7 q-2 -3 0 -7 Z" stroke-width="1"/>' for x, y in ((294, 474), (300, 490), (290, 500))))
    b.append('<rect x="250" y="700" width="30" height="46" rx="6" stroke-width="1.7"/><path d="M256 700 V684 H274 V700 M262 684 V674 H284 V682 H274" stroke-width="1.5"/>'
             + icon("drop", 265, 726, 0.6))
    return "".join(b)


def svg():
    return page(build(), TITLE)
