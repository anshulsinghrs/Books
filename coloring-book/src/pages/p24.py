"""Page 24 — The Vegetable Patch (Clover's garden)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, scallop_blob, daisy
from props import icon, snail, sun_hat

TITLE = "Page 24 — The Vegetable Patch"


def sunflower(x, y, r=26):
    import math
    pet = "".join(f'<ellipse cx="0" cy="{-r*0.75:.1f}" rx="{r*0.22:.1f}" ry="{r*0.42:.1f}" transform="rotate({k*24})"/>' for k in range(15))
    grid = "".join(f'<circle cx="{r*0.22*math.cos(a):.1f}" cy="{r*0.22*math.sin(a):.1f}" r="1.3" fill="#000" stroke="none"/>' for a in [k*math.pi/4 for k in range(8)])
    return (f'<g transform="translate({x} {y})" stroke-width="1.3">{pet}<circle r="{r*0.42:.1f}" stroke-width="1.6"/>'
            f'<circle r="{r*0.26:.1f}" stroke-width="0.9"/>{grid}</g>')


def bed(pts, inner):
    d = "M" + " L".join(f"{x} {y}" for x, y in pts) + " Z"
    return clip_d(d, inner, 2)


def cabbage(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}"><path d="M-22 4 Q-26 -14 -10 -20 Q0 -30 10 -20 Q26 -14 22 4 Q0 12 -22 4 Z"/>'
            '<path d="M-12 2 Q-14 -10 0 -14 Q14 -10 12 2 Z"/><path d="M-4 -2 Q0 -8 4 -2" fill="none"/></g>')


def lettuce(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.3/s:.2f}"><path d="M-18 4 Q-24 -6 -14 -12 Q-14 -22 -2 -20 Q6 -26 12 -18 Q24 -16 20 -4 Q24 4 16 6 Q0 10 -18 4 Z"/>'
            '<path d="M-6 4 Q-4 -8 0 -14 M6 4 Q8 -6 4 -14" fill="none" stroke-width="0.9"/></g>')


def carrot_top(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.2/s:.2f}"><path d="M-6 0 Q-6 -6 0 -7 Q6 -6 6 0 Z"/>'
            '<path d="M0 -6 Q-8 -20 -12 -26 Q-4 -22 0 -10 Z M0 -6 Q0 -22 2 -30 Q6 -20 2 -8 Z M0 -6 Q8 -18 14 -22 Q8 -12 2 -6 Z"/></g>')


def build():
    b = []
    b.append('<use href="#cloud" transform="translate(300 80) scale(1.1)" stroke-width="1.4"/>')
    b.append('<path d="M30 170 C200 150 400 168 600 150 V800 H30 Z" stroke-width="1.6"/>')
    # picket fence along the back
    b.append("".join(f'<path d="M{x} 210 V180 L{x + 7} 172 L{x + 14} 180 V210 Z" stroke-width="1.3"/>' for x in range(150, 420, 24)) + lines("M146 188 H424 M146 202 H424", 1.2))
    # garden shed (planks)
    b.append(clip_d("M430 130 H570 V300 H430 Z", lines(" ".join(f"M{x} 130 V300" for x in range(448, 570, 18)), 1.0), 2))
    b.append('<path d="M418 136 L500 76 L582 136 Z" stroke-width="2"/><path d="M470 300 V220 H514 V300 Z" stroke-width="1.7"/><circle cx="506" cy="262" r="3" stroke-width="1.1"/>')
    # scarecrow made of a broom and a hat (Dot on the hat)
    b.append(lines("M360 330 V200 M330 236 H392", 4) + lines("M360 330 V200 M330 236 H392", 1.6).replace('stroke-width="1.6"', 'stroke="#fff" stroke-width="1.6"'))
    b.append('<path d="M344 236 H376 L382 300 H338 Z" stroke-width="1.7"/>' + lines("M348 300 L344 316 M360 300 V318 M372 300 L376 316", 1.1))
    b.append('<circle cx="360" cy="206" r="16" stroke-width="1.7"/>' + lines("M352 204 h4 M364 204 h4 M354 212 Q360 216 366 212", 1.2))
    b.append(sun_hat(360, 192, 54))
    b.append(dot(366, 163, 0.95))
    # raised beds receding from lower right to upper left
    b.append(bed([(130, 250), (330, 250), (350, 320), (110, 320)],
                 "".join(cabbage(x, 296, 0.9) for x in (160, 210, 260, 310))))
    b.append('<path d="M110 320 H350 V334 H110 Z" stroke-width="1.8"/>')
    trellis = lines(" ".join(f"M{x} 340 V420" for x in range(200, 470, 34)) + " M196 360 H470 M196 390 H470", 1.4)
    pea = "".join(f'<path d="M{x} {y} q8 -4 14 2 q-6 6 -14 -2 Z" stroke-width="1.1"/>' for x, y in ((216, 372), (252, 398), (286, 366), (318, 400), (356, 374), (392, 398), (430, 368)))
    tendril = lines(" ".join(f"M{x} 360 q-6 8 0 14 q6 6 0 12" for x in range(214, 460, 34)), 0.9)
    b.append(bed([(180, 420), (480, 420), (500, 500), (160, 500)], "".join(lettuce(x, 470, 1.0) for x in (210, 270, 330, 390, 450))))
    b.append(trellis + tendril + pea)
    b.append('<path d="M160 500 H500 V516 H160 Z" stroke-width="1.8"/>')
    b.append(bed([(300, 590), (590, 590), (600, 690), (280, 690)], "".join(carrot_top(x, 640, 1.2) for x in range(330, 590, 40))))
    b.append('<path d="M280 690 H600 V710 H280 Z" stroke-width="1.8"/>')
    # seed markers with vegetable icons
    for (x, y, ico) in ((120, 316, "leaf"), (166, 496, "berry"), (296, 686, "drop")):
        b.append(f'<path d="M{x} {y} V{y - 30}" stroke-width="2.4"/><rect x="{x - 14}" y="{y - 52}" width="28" height="24" rx="3" stroke-width="1.5"/>' + icon(ico, x, y - 40, 0.55))
    # sunflowers towering along the left edge
    for (x, top, r) in ((66, 140, 30), (104, 230, 26), (60, 360, 28)):
        b.append(lines(f"M{x} {top} V760", 3) + f'<path d="M{x} {top + 120} Q{x + 26} {top + 100} {x + 34} {top + 80} Q{x + 10} {top + 96} {x} {top + 120} Z M{x} {top + 180} Q{x - 24} {top + 160} {x - 30} {top + 140} Q{x - 8} {top + 158} {x} {top + 180} Z" stroke-width="1.3"/>')
        b.append(sunflower(x, top, r))
    # Clover pulling the giant carrot
    cx, cy, cs = 400, 640, 1.25
    b.append('<path d="M396 608 Q364 640 332 728 Q330 744 342 738 Q388 664 420 616 Z" stroke-width="2"/>' + lines("M370 640 l10 4 M356 672 l10 4 M346 700 l9 4", 1.1))
    b.append('<path d="M406 612 Q396 580 384 560 Q404 574 410 600 Z M410 610 Q414 574 420 552 Q428 576 416 606 Z M414 612 Q434 588 448 576 Q440 598 420 616 Z" stroke-width="1.4"/>')
    b.append(char("cl", cx + 50, cy + 50, cs, arms=(70, 40), head_rot=-10, mood="happy"))
    # Pebble pushing the wheelbarrow of vegetables between the beds
    b.append(char("pb", 120, 610, 1.25, arms=(-70, -70)))
    b.append('<path d="M150 548 H260 L240 596 H170 Z" stroke-width="2"/><circle cx="252" cy="606" r="14" stroke-width="1.9"/><circle cx="252" cy="606" r="4" stroke-width="1.1"/>'
             + lines("M150 556 L128 572 M176 596 L170 616", 3))
    b.append(cabbage(186, 548, 0.8) + lettuce(222, 546, 0.8) + '<path d="M200 540 Q206 520 240 516 L242 524 Q212 530 206 544 Z" stroke-width="1.3"/>')
    # watering can, gloves and the snail
    b.append('<path d="M520 520 H566 V560 Q566 568 543 568 Q520 568 520 560 Z" stroke-width="1.8"/><path d="M520 530 L490 508 L494 502 L522 520 Z" stroke-width="1.5"/>'
             '<path d="M566 530 Q580 530 580 544 Q580 556 566 556" fill="none" stroke-width="3"/>')
    b.append('<g transform="translate(190 744) rotate(-10)" stroke-width="1.5"><path d="M-12 0 V-22 Q-12 -26 -8 -26 V-36 Q-8 -40 -4 -40 Q0 -40 0 -36 V-26 V-38 Q0 -42 4 -42 Q8 -42 8 -38 V-26 V-34 Q8 -38 12 -38 Q16 -38 16 -34 V-10 L22 -18 Q26 -22 28 -16 L18 2 Z"/><path d="M-12 -8 H18" fill="none" stroke-width="1"/></g>')
    b.append('<g transform="translate(236 744) rotate(12)" stroke-width="1.5"><path d="M-12 0 V-22 Q-12 -26 -8 -26 V-36 Q-8 -40 -4 -40 Q0 -40 0 -36 V-26 V-38 Q0 -42 4 -42 Q8 -42 8 -38 V-26 V-34 Q8 -38 12 -38 Q16 -38 16 -34 V-10 L22 -18 Q26 -22 28 -16 L18 2 Z"/><path d="M-12 -8 H18" fill="none" stroke-width="1"/></g>')
    b.append(snail(130, 726, 0.9))
    b.append(daisy(560, 740, 11) + daisy(470, 750, 10))
    return "".join(b)


def svg():
    return page(build(), TITLE)
