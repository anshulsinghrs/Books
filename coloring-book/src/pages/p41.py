"""Page 41 — Sweater Weather (all eight friends, autumn porch portrait)."""
from chars import char, dot, page, paw, TORSO_BOX
from scene import clip_d, lines, pumpkin, gourd, oak_leaf, scallop_blob

TITLE = "Page 41 — Sweater Weather"
S = 1.15


# ---------------- knit patterns (model units of each friend's torso)
def _box(c):
    return TORSO_BOX[c]


def p_cable(c):
    x0, y0, x1, y1 = _box(c)
    out = ""
    for x in range(int(x0) + 6, int(x1), 22):
        out += f'<path d="M{x-7} {y0} V{y1} M{x+7} {y0} V{y1}" stroke-width="0.9"/>'
        y = y0 + 4
        while y < y1:
            out += f'<path d="M{x-6} {y} Q{x} {y-3} {x+6} {y+8} M{x+6} {y} Q{x} {y-3} {x-6} {y+8}" stroke-width="0.9"/>'
            y += 11
    out += '<path d="M-14 -112 L0 -74 L14 -112" stroke-width="1.1"/>'
    return out


def p_grid(c, item, dx, dy, offset=True):
    x0, y0, x1, y1 = _box(c)
    out = ""
    r = 0
    y = y0 + dy * 0.6
    while y < y1:
        x = x0 + (dx / 2 if (offset and r % 2) else 0)
        while x < x1 + dx:
            out += item(x, y, r)
            x += dx
        y += dy
        r += 1
    return out


def p_hearts(c):
    return p_grid(c, lambda x, y, r: f'<use href="#heart" transform="translate({x:.1f} {y:.1f}) scale(0.62)" stroke-width="1.3"/>', 15, 13)


def p_dots(c):
    return p_grid(c, lambda x, y, r: f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.8" stroke-width="0.8"/>', 11, 10)


def p_leaves(c):
    return p_grid(c, lambda x, y, r: f'<path transform="translate({x:.1f} {y:.1f}) rotate({35 if r % 2 else -35})" d="M0 6 C-5 2 -5 -3 0 -7 C5 -3 5 2 0 6 Z M0 6 V-5" stroke-width="0.8"/>', 15, 13)


def p_stripes(c):
    x0, y0, x1, y1 = _box(c)
    return "".join(f'<path d="M{x0-5} {y:.1f} H{x1+5}" stroke-width="1"/>' for y in [y0 + 8 + 9 * k for k in range(12)] if y < y1)


def p_fairisle(c):
    x0, y0, x1, y1 = _box(c)
    out = ""
    for yb in (y0 + 20, y0 + 52):
        out += f'<path d="M{x0-5} {yb} H{x1+5} M{x0-5} {yb+14} H{x1+5}" stroke-width="1"/>'
        out += '<path d="M' + " L".join(f"{x0 - 5 + 7*k:.1f} {yb + (3 if k % 2 else 11)}" for k in range(int((x1 - x0) / 7) + 3)) + '" stroke-width="0.9"/>'
    return out + p_grid(c, lambda x, y, r: f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="#000" stroke="none"/>' if (y0 + 38 < y < y0 + 46) else "", 12, 8)


def p_diamonds(c):
    x0, y0, x1, y1 = _box(c)
    out = ""
    for k in range(-6, 8):
        x = x0 + k * 13
        out += f'<path d="M{x} {y0} L{x + (y1 - y0)} {y1} M{x + (y1 - y0)} {y0} L{x} {y1}" stroke-width="0.9"/>'
    return out


def p_stars(c):
    return p_grid(c, lambda x, y, r: f'<use href="#star5" transform="translate({x:.1f} {y:.1f}) scale(0.42)" stroke-width="1.6"/>', 11, 10)


def build():
    b = []
    # ---- porch roof, wall siding, window, door with wreath
    b.append(clip_d("M30 70 H600 V530 H30 Z", lines(" ".join(f"M30 {y} H600" for y in range(92, 530, 22)), 1.0), 1.5))
    b.append('<rect x="30" y="20" width="570" height="50" stroke-width="2"/>')
    b.append("".join(f'<path d="M{x} 70 a12 12 0 0 0 24 0" stroke-width="1.4"/>' for x in range(36, 600, 24)))
    b.append(lines("M30 48 H600", 1.1))
    b.append('<rect x="548" y="80" width="22" height="452" stroke-width="1.9"/>')
    b.append('<rect x="324" y="112" width="200" height="176" rx="4" stroke-width="2"/>')
    view = ('<path d="M332 230 C380 214 440 224 516 210 V280 H332 Z" stroke-width="1.3"/>'
            + '<rect x="380" y="180" width="10" height="46" stroke-width="1.3"/>' + scallop_blob(385, 166, 34, 28, 9, 0.3, 1.5)
            + oak_leaf(470, 160, 30, 1.0) + oak_leaf(492, 196, -20, 0.9) + oak_leaf(440, 202, 60, 0.9))
    b.append(clip_d("M332 120 H516 V280 H332 Z", view, 1.5, fill="#fff"))
    b.append(lines("M424 120 V280 M332 200 H516", 2.2))
    b.append('<rect x="314" y="286" width="220" height="12" rx="3" stroke-width="1.8"/>')
    # lantern hanging from the porch roof
    b.append(lines("M262 70 V92", 1.3))
    b.append('<path d="M248 104 L262 92 L276 104 Z" stroke-width="1.5"/><rect x="250" y="104" width="24" height="34" rx="2" stroke-width="1.6"/>'
             '<path d="M246 138 H278 L274 146 H250 Z" stroke-width="1.5"/>' + lines("M262 104 V138", 1)
             + '<path d="M262 128 Q256 120 262 112 Q268 120 262 128 Z" stroke-width="1"/>')
    # round-top door
    b.append('<path d="M60 528 V272 A70 70 0 0 1 200 272 V528 Z" stroke-width="2"/>')
    b.append(clip_d("M72 528 V272 A58 58 0 0 1 188 272 V528 Z", lines("M101 200 V528 M130 200 V528 M159 200 V528", 1.1), 1.7))
    b.append('<circle cx="178" cy="420" r="4.5" stroke-width="1.4"/>')
    # wreath of leaves and berries with a bow; Dot nestles in it
    wx, wy = 130, 300
    b.append(f'<circle cx="{wx}" cy="{wy}" r="42" stroke-width="1.8"/><circle cx="{wx}" cy="{wy}" r="22" stroke-width="1.6"/>')
    import math
    for k in range(14):
        a = 2 * math.pi * k / 14
        x, y = wx + 32 * math.cos(a), wy + 32 * math.sin(a)
        b.append(oak_leaf(round(x, 1), round(y + 10, 1), math.degrees(a) + 90, 0.72, 1.1))
    for k in range(7):
        a = 2 * math.pi * k / 7 + 0.3
        b.append(f'<circle cx="{wx + 26*math.cos(a):.1f}" cy="{wy + 26*math.sin(a):.1f}" r="3.6" stroke-width="1.1"/>')
    b.append(f'<path d="M{wx} {wy+42} L{wx-18} {wy+32} L{wx-18} {wy+52} Z M{wx} {wy+42} L{wx+18} {wy+32} L{wx+18} {wy+52} Z" stroke-width="1.4"/>'
             f'<path d="M{wx-4} {wy+46} L{wx-12} {wy+70} L{wx-4} {wy+66} Z M{wx+4} {wy+46} L{wx+12} {wy+70} L{wx+4} {wy+66} Z" stroke-width="1.3"/>'
             f'<circle cx="{wx}" cy="{wy+42}" r="5" stroke-width="1.4"/>')
    b.append(dot(wx + 20, wy - 25, 0.9))

    # ---- porch floor and steps
    b.append(clip_d("M30 528 H600 V562 H30 Z", lines(" ".join(f"M{x} 528 V562" for x in range(70, 600, 56)), 1.0), 1.8))
    b.append('<rect x="30" y="562" width="570" height="24" stroke-width="1.8"/>')
    b.append('<rect x="30" y="586" width="570" height="20" stroke-width="1.6"/>')
    b.append('<rect x="30" y="606" width="570" height="24" stroke-width="1.8"/>')
    b.append('<rect x="30" y="630" width="570" height="22" stroke-width="1.6"/>')
    b.append('<path d="M30 652 H600 V800 H30 Z" stroke-width="1.8"/>')

    # ---- top tier: Bramble (Thimble on his shoulder), Tofu, Juniper
    b.append(char("br", 262, 545, S, arms=(14, -14), sweater=p_cable("br"), mood="happy"))
    mx, my = paw("br", 262, 545, S, "R", -14)
    b.append(f'<path d="M{mx-10:.1f} {my-16:.1f} H{mx+10:.1f} V{my+4:.1f} Q{mx+10:.1f} {my+10:.1f} {mx:.1f} {my+10:.1f} Q{mx-10:.1f} {my+10:.1f} {mx-10:.1f} {my+4:.1f} Z" stroke-width="1.6"/>'
             f'<path d="M{mx+10:.1f} {my-12:.1f} q9 0 9 7 q0 7 -9 7" fill="none" stroke-width="1.6"/>'
             + lines(f"M{mx-4:.1f} {my-22:.1f} q-3 -4 0 -8 M{mx+4:.1f} {my-22:.1f} q-3 -4 0 -8", 1))
    b.append(f'<g transform="translate(262 545) scale({S})" stroke-width="{2/S:.3f}"><use href="#br-sleeve" transform="translate(44 -94) rotate(-14)"/></g>')
    b.append(char("to", 382, 552, S, arms=(14, -14), sweater=p_fairisle("to")))
    b.append(char("ju", 494, 548, S, arms=(14, -150), sweater=p_leaves("ju"), brows=True))
    b.append(char("th", 194, 438, S, arms=(30, -150), sit=True, sweater=p_stars("th"), mood="happy"))

    # ---- Tofu's very long scarf (from page 23) around Thimble, Bramble and Tofu
    scarf = ("M174 522 Q168 470 180 418 L206 414 Q228 418 240 425 L284 425 Q318 424 350 459 "
             "L414 460 Q432 476 432 548")
    b.append(f'<path d="{scarf}" fill="none" stroke-width="15"/>')
    b.append(f'<path d="{scarf}" fill="none" stroke="#fff" stroke-width="11.6" stroke-linecap="butt"/>')
    b.append(f'<path d="{scarf}" fill="none" stroke-width="11.6" stroke-linecap="butt" stroke-dasharray="1.3 13"/>')
    for (x, y) in ((174, 522), (432, 548)):
        b.append(f'<rect x="{x-7.5}" y="{y}" width="15" height="10" stroke-width="1.4"/>'
                 + lines(f"M{x-5} {y+10} V{y+20} M{x} {y+10} V{y+21} M{x+5} {y+10} V{y+20}", 1.3))

    # ---- front row: Clover, Pip, Pebble, Miso
    b.append(char("cl", 200, 654, S, arms=(14, -150), sweater=p_hearts("cl"), mood="happy"))
    b.append(char("pi", 296, 654, S, arms=(14, -14), sweater=p_stripes("pi"), wag=True))
    b.append(char("pb", 384, 656, S, arms=(30, -30), sweater=p_diamonds("pb")))
    b.append(char("mi", 470, 656, S, arms=(14, -14), sweater=p_dots("mi")))

    # ---- pumpkins and gourds on the steps, leaves on the ground
    b.append(pumpkin(92, 606, 72, 52) + pumpkin(64, 652, 50, 36) + pumpkin(132, 652, 40, 30))
    b.append(pumpkin(552, 606, 46, 36) + gourd(560, 652, 1.0, 10) + gourd(530, 652, 0.85, -12))
    for (cx, cy, rx, ry) in ((300, 676, 40, 11), (280, 706, 44, 12), (306, 740, 48, 13)):
        b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" stroke-width="1.6"/>')
    b.append(pumpkin(470, 744, 56, 40) + gourd(420, 748, 0.9, 20))
    for (x, y) in ((140, 700), (380, 700), (210, 744)):
        b.append(f'<ellipse cx="{x}" cy="{y+6}" rx="5.5" ry="7" stroke-width="1.2"/><path d="M{x-7} {y+1} Q{x} {y-8} {x+7} {y+1} Z" stroke-width="1.2"/>')
    for (x, y, r, s) in ((90, 720, 30, 1.3), (180, 742, -40, 1.2), (380, 736, 80, 1.3),
                         (540, 716, -60, 1.3), (250, 704, 120, 1.1), (500, 690, 40, 1.0)):
        b.append(oak_leaf(x, y, r, s, 1.2))
    return "".join(b)


def svg():
    return page(build(), TITLE)
