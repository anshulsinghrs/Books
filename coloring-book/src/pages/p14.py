"""Page 14 — Pebble's Treasure Shelf (cubbies; Miso on top)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import icon, plant, plant_pot, jar

TITLE = "Page 14 — Pebble's Treasure Shelf"
X0, Y0, CW, CH = 132, 150, 108, 150


def cell(c, r):
    return X0 + c * CW, Y0 + r * CH


def shell_spiral(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}"><path d="M-14 6 Q-16 -16 4 -16 Q18 -14 16 2 Q14 12 0 10 Z"/>'
            '<path d="M2 -2 m3 0 a3 3 0 1 1 -6 0 a6 6 0 1 1 12 0" fill="none" stroke-width="1"/><path d="M-14 6 L-22 10 L-12 12 Z"/></g>')


def shell_scallop(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}">'
            '<path d="M0 10 L-16 -6 Q-12 -18 0 -18 Q12 -18 16 -6 Z"/><path d="M0 10 L-8 -16 M0 10 V-18 M0 10 L8 -16" fill="none" stroke-width="0.9"/>'
            '<path d="M-6 10 H6 V14 H-6 Z"/></g>')


def stone(x, y, rx=14, ry=10):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" stroke-width="1.6"/>'
            f'<circle cx="{x - rx*0.3:.1f}" cy="{y - ry*0.2:.1f}" r="2" stroke-width="0.8"/><circle cx="{x + rx*0.35:.1f}" cy="{y + ry*0.25:.1f}" r="1.6" stroke-width="0.8"/>')


def build():
    b = []
    # wall with a little window of the river and wainscot
    b.append(clip_d("M30 640 H600 V800 H30 Z", lines(" ".join(f"M30 {y} H600" for y in range(670, 800, 34)), 1), 1.6))
    b.append('<path d="M40 120 Q40 70 80 70 Q120 70 120 120 V250 H40 Z" stroke-width="2"/>')
    b.append(clip_d("M48 120 Q48 78 80 78 Q112 78 112 120 V242 H48 Z",
                    '<path d="M48 190 Q80 180 112 192 V242 H48 Z" stroke-width="1.2"/>' + lines("M56 206 q8 -3 16 0 M84 220 q8 -3 16 0 M80 78 V242", 1.2), 1.4))
    # the cubby shelf: 4 x 3 compartments
    b.append(f'<rect x="{X0 - 14}" y="{Y0 - 14}" width="{4*CW + 28}" height="{3*CH + 28}" rx="6" stroke-width="2.4"/>')
    b.append(f'<rect x="{X0}" y="{Y0}" width="{4*CW}" height="{3*CH}" stroke-width="1.8"/>')
    for c in range(1, 4):
        b.append(f'<rect x="{X0 + c*CW - 5}" y="{Y0}" width="10" height="{3*CH}" stroke-width="1.6"/>')
    for r in range(1, 3):
        b.append(f'<rect x="{X0}" y="{Y0 + r*CH - 5}" width="{4*CW}" height="10" stroke-width="1.6"/>')
    # label tags (icons only) under each cubby
    icons = ["round", "drop", "leaf", "star", "heart", "flower", "tree", "berry", "moon", "acorn", "fish", "note"]
    for i in range(12):
        x, y = cell(i % 4, i // 4)
        b.append(f'<rect x="{x + CW/2 - 16:.0f}" y="{y + CH - 26:.0f}" width="32" height="16" rx="3" stroke-width="1.2"/>' + icon(icons[i], x + CW/2, y + CH - 18, 0.45, 0.9))
    # row 1: shells (with Dot), smooth stones, jar of sea glass, tiny boat
    x, y = cell(0, 0); b.append(shell_spiral(x + 34, y + 104) + shell_scallop(x + 76, y + 104, 1.1) + dot(x + 56, y + 86, 0.95))
    x, y = cell(1, 0); b.append(stone(x + 30, y + 112) + stone(x + 60, y + 114, 16, 10) + stone(x + 46, y + 96, 12, 8) + stone(x + 80, y + 104, 10, 8))
    x, y = cell(2, 0); b.append(jar(x + 54, y + 122, 44, 70))
    b.append("".join(f'<path d="M{x + 54 + dx} {y + 100 + dy} l6 -4 l5 5 l-6 4 Z" stroke-width="1"/>' for dx, dy in ((-14, 0), (2, -6), (-6, 10), (10, 8), (-12, 16))))
    x, y = cell(3, 0)
    b.append(f'<path d="M{x + 20} {y + 104} H{x + 88} L{x + 76} {y + 120} H{x + 32} Z" stroke-width="1.7"/>'
             f'<path d="M{x + 54} {y + 104} V{y + 40} L{x + 84} {y + 96} Z" stroke-width="1.6"/><path d="M{x + 50} {y + 48} L{x + 28} {y + 98} H{x + 50} Z" stroke-width="1.5"/>')
    # row 2: fern in a pot, snow globe, pinecone, lantern
    x, y = cell(0, 1); b.append(plant("fern", x + 54, y + 92, 0.7) + plant_pot(x + 54, y + 122, 44, 34, "zigzag"))
    x, y = cell(1, 1)
    b.append(f'<circle cx="{x + 54}" cy="{y + 76}" r="34" stroke-width="1.8"/><path d="M{x + 30} {y + 108} H{x + 78} L{x + 84} {y + 124} H{x + 24} Z" stroke-width="1.8"/>'
             f'<path d="M{x + 36} {y + 102} Q{x + 54} {y + 92} {x + 72} {y + 102}" fill="none" stroke-width="1.1"/>'
             f'<path d="M{x + 46} {y + 98} L{x + 54} {y + 70} L{x + 62} {y + 98} Z" stroke-width="1.2"/>'
             + "".join(f'<use href="#flake" transform="translate({x + dx} {y + dy}) scale(0.45)" stroke-width="2"/>' for dx, dy in ((38, 62), (70, 58), (56, 50))))
    x, y = cell(2, 1)
    cone = "".join(f'<path d="M{x + 54 + dx} {y + dy} q-8 6 0 12 q8 -6 0 -12 Z" stroke-width="1.1"/>' for dx, dy in ((-10, 74), (10, 74), (0, 64), (-14, 90), (0, 86), (14, 90), (-8, 104), (8, 104), (0, 54)))
    b.append(f'<ellipse cx="{x + 54}" cy="{y + 88}" rx="24" ry="36" stroke-width="1.8"/>' + cone + f'<path d="M{x + 54} {y + 52} V{y + 40}" stroke-width="2"/>')
    x, y = cell(3, 1)
    b.append(f'<path d="M{x + 38} {y + 54} L{x + 54} {y + 40} L{x + 70} {y + 54} Z" stroke-width="1.6"/><rect x="{x + 38}" y="{y + 54}" width="32" height="50" rx="3" stroke-width="1.7"/>'
             f'<path d="M{x + 34} {y + 104} H{x + 74} L{x + 70} {y + 118} H{x + 38} Z" stroke-width="1.6"/>'
             f'<path d="M{x + 54} {y + 96} Q{x + 46} {y + 84} {x + 54} {y + 66} Q{x + 62} {y + 84} {x + 54} {y + 96} Z" stroke-width="1.1"/>')
    # row 3: more shells, a stack of stones, a starfish and a box of shells
    x, y = cell(0, 2); b.append(shell_scallop(x + 40, y + 104, 1.3) + shell_spiral(x + 78, y + 110, 0.9))
    x, y = cell(1, 2); b.append(stone(x + 54, y + 114, 26, 12) + stone(x + 54, y + 92, 20, 10) + stone(x + 54, y + 74, 14, 8))
    x, y = cell(2, 2); b.append(f'<path transform="translate({x + 54} {y + 84}) scale(2.6)" d="{icon.__globals__["ICON"]["star"]}" stroke-width="0.7"/>')
    x, y = cell(3, 2)
    b.append(f'<rect x="{x + 22}" y="{y + 80}" width="64" height="40" rx="3" stroke-width="1.7"/>' + shell_scallop(x + 40, y + 74, 0.8) + shell_spiral(x + 70, y + 76, 0.7))
    # Miso supervising from the top of the shelf
    b.append(char("mi", 470, 108, 1.15, arms=(None, 20), rot=-90))
    # Pebble on her stool, placing a shell
    b.append('<path d="M40 740 L56 660 H136 L152 740 H140 L126 676 H66 L52 740 Z" stroke-width="1.8"/><rect x="48" y="650" width="96" height="14" rx="4" stroke-width="1.9"/>')
    px, py, ps = 96, 652, 1.75
    b.append(char("pb", px, py, ps, arms=(14, -156), head_rot=6))
    sx, sy = paw("pb", px, py, ps, "R", -156)
    b.append(shell_spiral(sx + 4, sy - 6, 1.1))
    b.append(arms_only("pb", px, py, ps, (None, -156)))
    return "".join(b)


def svg():
    return page(build(), TITLE)
