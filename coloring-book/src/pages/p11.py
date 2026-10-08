"""Page 11 — Potting Bench (Clover repots a big split-leaf plant)."""
from chars import char, arms_only, dot, page, paw, apron
from scene import clip_d, lines
from props import plant, plant_pot, window_rect, icon

TITLE = "Page 11 — Potting Bench"


def big_leaf(x, y, rot, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.8/s:.2f}">'
            '<path d="M0 0 C-60 -6 -80 -80 0 -110 C80 -80 60 -6 0 0 Z"/>'
            '<path d="M-38 -40 L-14 -46 M-46 -66 L-18 -66 M38 -40 L14 -46 M46 -66 L18 -66 M-30 -88 L-10 -84 M30 -88 L10 -84" fill="none" stroke-width="2.6" stroke="#fff"/>'
            f'<path d="M0 4 V-100 M0 -30 L-40 -42 M0 -30 L40 -42 M0 -56 L-46 -68 M0 -56 L46 -68 M0 -80 L-30 -90 M0 -80 L30 -90" fill="none" stroke-width="{1.0/s:.2f}"/></g>')


def cactus(x, y, h=34, w=22):
    return (f'<path d="M{x - w/2} {y} Q{x - w/2 - 2} {y - h} {x} {y - h - 4} Q{x + w/2 + 2} {y - h} {x + w/2} {y} Z" stroke-width="1.6"/>'
            + lines(f"M{x} {y - h - 2} V{y} M{x - w*0.25:.1f} {y - h + 4} V{y} M{x + w*0.25:.1f} {y - h + 4} V{y}", 0.9)
            + "".join(f'<path d="M{x + dx:.1f} {y - dy} l-3 -3 M{x + dx:.1f} {y - dy} l3 -3" fill="none" stroke-width="0.8"/>'
                      for dx, dy in ((-w*0.4, h*0.5), (w*0.4, h*0.6), (0, h*0.85))))


def build():
    b = []
    # window behind the bench
    b.append(window_rect(150, 90, 300, 300, '<use href="#cloud" transform="translate(240 160) scale(0.9)" stroke-width="1.6"/>'
                         '<path d="M150 300 C220 280 320 296 450 276 V400 H150 Z" stroke-width="1.3"/>', (1, 1), True))
    b.append(lines("M30 430 H600", 1.4))
    # Clover (with her pocket apron) behind the bench
    cx, cy, cs = 228, 650, 1.75
    b.append(char("cl", cx, cy, cs, arms=(None, None), outfit=apron("cl", cs, top_frac=0.3), head_rot=6))
    # bench top and shelf below
    b.append('<path d="M40 560 H590 V588 H40 Z" stroke-width="2.2"/>' + lines("M60 574 H160 M300 572 H420", 0.9))
    b.append(clip_d("M40 588 H590 V800 H40 Z", lines(" ".join(f"M40 {y} H590" for y in range(612, 800, 30)), 0.9), 1.6))
    b.append('<rect x="60" y="588" width="18" height="180" stroke-width="1.8"/><rect x="552" y="588" width="18" height="180" stroke-width="1.8"/>')
    b.append('<rect x="60" y="680" width="510" height="14" stroke-width="1.8"/>')
    # stacked terracotta pots and a bag of soil on the shelf
    for k in range(4):
        b.append(f'<path d="M{100 - k*2} {680 - 14*k} H{160 + k*2} L{156 + k*2} {666 - 14*k} H{104 - k*2} Z" stroke-width="1.6"/>')
    b.append('<rect x="96" y="610" width="68" height="14" rx="2" stroke-width="1.7"/>')
    b.append('<path d="M214 680 Q206 620 222 598 L260 592 Q302 600 300 640 Q304 664 296 680 Z" stroke-width="1.9"/>'
             + '<path d="M222 598 Q232 584 244 594 Q254 582 262 594" fill="none" stroke-width="1.3"/>' + icon("leaf", 258, 640, 1.0, 1.2))
    b.append('<path d="M340 680 C330 660 370 650 380 664 C400 650 430 664 424 680 Z" stroke-width="1.5"/>')
    # seed packets with flower icons, trowel, spray bottle
    for (x, rot, ico) in ((106, -8, "flower"), (140, 6, "leaf"), (172, -4, "berry")):
        b.append(f'<g transform="translate({x} 548) rotate({rot})"><rect x="-16" y="-26" width="32" height="40" rx="2" stroke-width="1.5"/>'
                 f'<path d="M-16 -18 H16" fill="none" stroke-width="1"/>' + icon(ico, 0, -2, 0.7) + "</g>")
    b.append('<path d="M470 552 L520 540 L522 548 L472 560 Z" stroke-width="1.5"/><path d="M520 536 L556 528 Q566 538 556 548 L522 552 Z" stroke-width="1.6"/>')
    b.append('<path d="M520 560 V510 Q520 500 530 500 H544 V488 H530 V478 H556 V500 Q566 500 566 510 V560 Z" stroke-width="1.7"/>'
             + '<path d="M530 478 L520 470 L530 466 Z" stroke-width="1.2"/>' + icon("drop", 543, 534, 0.8))
    # three small cacti and the trailing vine
    b.append(cactus(420, 540, 30, 20) + plant_pot(420, 560, 30, 22, "dots"))
    b.append(cactus(452, 536, 24, 16) + plant_pot(452, 560, 26, 20, "stripes"))
    b.append(cactus(386, 538, 40, 18) + plant_pot(386, 560, 26, 22, "zigzag"))
    b.append(plant("vine", 96, 470, 0.9) + plant_pot(96, 486, 44, 34, "scallops"))
    b.append('<rect x="70" y="486" width="52" height="10" stroke-width="1.5"/>' + lines("M76 496 V560 M116 496 V560", 1.6))
    # the big split-leaf plant being repotted, with an empty pot (Dot inside)
    b.append(plant("split", 306, 516, 1.75) + plant_pot(306, 558, 80, 58, "stripes"))
    b.append(lines("M258 504 q6 -6 12 0 M318 498 q6 -6 12 0", 1.2))
    b.append(arms_only("cl", cx, cy, cs, (-30, -60)))
    b.append(plant_pot(488, 560, 46, 38, "plain"))
    b.append(dot(488, 520, 0.95))
    # big leaves framing the page edges (top-left and right)
    b.append(big_leaf(60, 220, 130, 1.3) + big_leaf(100, 100, 160, 1.0) + big_leaf(600, 300, -110, 1.25) + big_leaf(590, 150, -140, 0.95))
    return "".join(b)


def svg():
    return page(build(), TITLE)
