"""Page 42 — Painted Pumpkins (harvest table beside the garden shed)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, pumpkin, gourd, oak_leaf
from props import maple_leaf, icon, basket

TITLE = "Page 42 — Painted Pumpkins"


def painted(x, y, w, h, pat):
    out = pumpkin(x, y, w, h, 1.7)
    cy = y - h / 2
    if pat == "flowers":
        out += "".join(f'<g transform="translate({x + dx} {cy + dy})" stroke-width="1">' + "".join(f'<circle cx="0" cy="-4" r="3" transform="rotate({a})"/>' for a in range(0, 360, 72)) + '<circle r="2"/></g>'
                       for dx, dy in ((-w*0.25, -4), (w*0.05, 6), (w*0.28, -6)))
    elif pat == "swirls":
        out += lines(" ".join(f"M{x + dx:.0f} {cy + dy:.0f} m3 0 a3 3 0 1 1 -6 0 a6 6 0 1 1 12 0" for dx, dy in ((-w*0.24, 0), (w*0.04, -6), (w*0.26, 4))), 1.1)
    elif pat == "stars":
        out += "".join(f'<use href="#star5" transform="translate({x + dx:.0f} {cy + dy:.0f}) scale(0.55)" stroke-width="1.8"/>' for dx, dy in ((-w*0.26, -4), (0, 6), (w*0.26, -6), (-w*0.08, -h*0.25)))
    elif pat == "checks":
        out += lines(f"M{x - w*0.4:.0f} {cy:.0f} H{x + w*0.4:.0f} M{x - w*0.38:.0f} {cy + h*0.2:.0f} H{x + w*0.38:.0f}", 1.1)
    elif pat == "dots":
        out += "".join(f'<circle cx="{x + dx:.0f}" cy="{cy + dy:.0f}" r="3" stroke-width="1"/>' for dx in (-w*0.3, -w*0.1, w*0.1, w*0.3) for dy in (-h*0.15, h*0.15))
    return out


def build():
    b = []
    # autumn sky and the garden shed with vines on the right
    b.append('<use href="#cloud" transform="translate(180 90) scale(1.1)" stroke-width="1.4"/>')
    b.append(clip_d("M420 120 H600 V520 H420 Z", lines(" ".join(f"M{x} 120 V520" for x in range(440, 600, 20)), 1), 2))
    b.append('<path d="M400 130 L500 60 L620 130 Z" stroke-width="2"/><rect x="470" y="300" width="70" height="220" stroke-width="1.8"/><circle cx="530" cy="410" r="4" stroke-width="1.2"/>')
    b.append(lines("M420 140 C440 220 410 300 440 380 C460 440 430 480 440 520", 1.6))
    b.append("".join(oak_leaf(x, y, r, 1.0) for x, y, r in ((436, 170, 30), (424, 230, -40), (440, 290, 20), (432, 350, -30), (452, 410, 40), (436, 470, -20))))
    # sunflowers drying upside down under the eave
    b.append(lines("M440 130 H560", 1.4))
    for x in (460, 500, 540):
        b.append(lines(f"M{x} 130 V190", 1.6) + "".join(f'<ellipse cx="{x}" cy="{196 + 14}" rx="5" ry="10" transform="rotate({a} {x} 210)" stroke-width="1.1"/>' for a in range(0, 360, 36))
                 + f'<circle cx="{x}" cy="210" r="9" stroke-width="1.5"/>')
    b.append('<path d="M30 430 H600 V800 H30 Z" stroke-width="1.6"/>')
    # hay bale seat, basket of corn cobs
    b.append(clip_d("M40 470 H180 V560 H40 Z", lines(" ".join(f"M40 {y} q20 -4 40 0 q20 4 40 0 q20 -4 40 0 q20 4 40 0" for y in range(484, 560, 14)), 1), 2))
    b.append(lines("M40 500 H180 M40 530 H180", 3))
    for k, x in enumerate((90, 108, 126)):
        b.append(f'<ellipse cx="{x}" cy="{440 - (k % 2) * 6}" rx="8" ry="24" transform="rotate({-20 + k*20} {x} 440)" stroke-width="1.5"/>'
                 + lines(f"M{x - 4} {426} V{454} M{x + 4} 426 V454 M{x - 7} 434 H{x + 7} M{x - 7} 446 H{x + 7}", 0.8))
    b.append(basket(108, 470, 70, 30, handle=False))
    # Clover and Pebble behind the harvest table
    b.append(char("cl", 210, 620, 1.6, arms=(None, None), mood="happy"))
    b.append(char("pb", 410, 618, 1.75, arms=(None, None)))
    b.append('<path d="M110 566 H500 V594 H110 Z" stroke-width="2.2"/><path d="M134 594 V690 M476 594 V690" stroke-width="5"/><path d="M134 594 V690 M476 594 V690" stroke="#fff" stroke-width="2.4"/>')
    for x in (160, 462):
        b.append(f'<path d="M{x - 14} 566 V540 H{x + 14} V566 Z" stroke-width="1.6"/><ellipse cx="{x}" cy="540" rx="14" ry="5" stroke-width="1.4"/>')
    b.append(lines("M462 540 L478 504 M160 540 L148 510", 2.4))
    b.append(painted(256, 566, 86, 58, "swirls"))
    b.append(arms_only("cl", 210, 620, 1.6, (-40, -70)))
    b.append(lines("M244 500 L272 482", 2.2))
    b.append(painted(410, 566, 70, 50, "flowers"))
    b.append(arms_only("pb", 410, 618, 1.75, (-30, 30)))
    # Thimble on a small pumpkin, painting dots on the big one
    b.append(painted(330, 566, 50, 34, "dots"))
    b.append(char("th", 330, 534, 1.4, arms=(150, -50), mood="happy"))
    # foreground "shelf" of finished pumpkins and gourds (Dot on a stem)
    row = [(80, 740, 88, 60, "stars"), (180, 744, 70, 76, "checks"), (284, 742, 100, 66, "flowers"), (390, 744, 72, 52, "swirls"), (490, 742, 96, 70, "dots")]
    for (x, y, w, h, p) in row:
        b.append(painted(x, y, w, h, p))
    b.append(gourd(552, 744, 1.2, 12) + gourd(136, 750, 0.8, -10))
    b.append(dot(286, 660, 0.9))
    b.append(maple_leaf(240, 640, 30, 1.2) + maple_leaf(440, 650, -40, 1.1))
    return "".join(b)


def svg():
    return page(build(), TITLE)
