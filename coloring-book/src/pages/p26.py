"""Page 26 — Porch Concert (Bramble's porch steps as a little stage)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, daisy
from props import plant, icon, plant_pot

TITLE = "Page 26 — Porch Concert"


def note(x, y, s=1.0, double=False):
    if double:
        return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}"><ellipse cx="-10" cy="10" rx="7" ry="5" transform="rotate(-20 -10 10)"/>'
                '<ellipse cx="12" cy="6" rx="7" ry="5" transform="rotate(-20 12 6)"/><path d="M-4 9 V-16 L18 -20 V5 M-4 -10 L18 -14" fill="none" stroke-width="2"/></g>')
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}"><ellipse cx="0" cy="10" rx="8" ry="6" transform="rotate(-20 0 10)"/>'
            '<path d="M7 8 V-18 Q16 -12 18 -4" fill="none" stroke-width="2"/></g>')


def build():
    b = []
    # porch roof trim (as on page 41), siding, railing, hanging ferns
    b.append(clip_d("M30 70 H600 V430 H30 Z", lines(" ".join(f"M30 {y} H600" for y in range(92, 430, 22)), 1.0), 1.5))
    b.append('<rect x="30" y="20" width="570" height="50" stroke-width="2"/>' + "".join(f'<path d="M{x} 70 a12 12 0 0 0 24 0" stroke-width="1.4"/>' for x in range(36, 600, 24)) + lines("M30 48 H600", 1.1))
    b.append('<path d="M40 70 V300 Q40 270 0 270" fill="none" stroke-width="1"/>')
    for x in (100, 520):
        b.append(lines(f"M{x} 70 V96 M{x} 96 L{x - 24} 130 M{x} 96 L{x + 24} 130", 1.2))
        b.append(plant("fern", x, 130, 0.7) + f'<path d="M{x - 26} 130 H{x + 26} Q{x + 26} 160 {x} 162 Q{x - 26} 160 {x - 26} 130 Z" stroke-width="1.8"/>')
    # floating music notes curving across the top (Dot rides one)
    for (x, y, s, d) in ((180, 210, 1.2, False), (240, 180, 1.0, True), (310, 170, 1.3, False), (380, 186, 1.0, True), (446, 214, 1.2, False), (130, 250, 0.9, True), (500, 260, 0.9, False)):
        b.append(note(x, y, s, d))
    b.append(dot(316, 181, 0.85))
    # railing along the porch behind Tofu
    b.append(lines("M30 330 H600 M30 410 H600", 6) + lines("M30 330 H600 M30 410 H600", 2.4).replace('stroke-width="2.4"', 'stroke="#fff" stroke-width="2.4"'))
    b.append("".join(f'<rect x="{x}" y="336" width="10" height="70" rx="2" stroke-width="1.4"/>' for x in range(46, 600, 30)))
    # steps: porch floor, two steps, ground
    b.append(clip_d("M30 430 H600 V470 H30 Z", lines(" ".join(f"M{x} 430 V470" for x in range(80, 600, 60)), 1), 1.8))
    b.append('<rect x="30" y="470" width="570" height="24" stroke-width="1.8"/><rect x="30" y="494" width="570" height="64" stroke-width="1.6"/>')
    b.append('<rect x="30" y="558" width="570" height="24" stroke-width="1.8"/><rect x="30" y="582" width="570" height="54" stroke-width="1.6"/>')
    b.append('<path d="M30 636 H600 V800 H30 Z" stroke-width="1.6"/>')
    # Tofu at the top with the wooden flute
    tx, ty, ts = 312, 470, 1.0
    b.append(char("to", tx, ty, ts, arms=(None, None), sit=True, mood="sleep"))
    b.append('<rect x="250" y="378" width="120" height="10" rx="5" stroke-width="1.7" transform="rotate(-6 310 383)"/>'
             + "".join(f'<circle cx="{x}" cy="{383 - (x - 310)*0.1:.1f}" r="1.8" stroke-width="0.9"/>' for x in (270, 286, 334, 350)))
    b.append(arms_only("to", tx, ty, ts, (-150, 150)))
    # Clover with the accordion, Pebble with the ukulele (middle step)
    cx, cy = 170, 562
    b.append(char("cl", cx, cy, 1.1, arms=(None, None), sit=True, mood="happy"))
    acc = f"M{cx - 34} {cy - 70} L{cx + 34} {cy - 70} L{cx + 34} {cy - 30} L{cx - 34} {cy - 30} Z"
    b.append(f'<rect x="{cx - 50}" y="{cy - 74}" width="16" height="48" rx="3" stroke-width="1.7"/><rect x="{cx + 34}" y="{cy - 74}" width="16" height="48" rx="3" stroke-width="1.7"/>')
    b.append(clip_d(acc, lines(" ".join(f"M{cx - 34 + k*8} {cy - 70} L{cx - 30 + k*8} {cy - 50} L{cx - 34 + k*8} {cy - 30}" for k in range(9)), 1.0), 1.7))
    b.append("".join(f'<circle cx="{cx - 42}" cy="{cy - 66 + k*9}" r="2" stroke-width="0.9"/>' for k in range(5)))
    b.append(arms_only("cl", cx, cy, 1.1, (-40, 40)))
    px, py = 440, 566
    b.append(char("pb", px, py, 1.25, arms=(None, None), sit=True, mood="happy"))
    b.append(f'<g transform="translate({px} {py - 34}) rotate(-30)" stroke-width="1.7"><path d="M-30 0 C-30 -16 -14 -18 -8 -10 C0 -18 14 -14 14 0 C14 14 0 18 -8 10 C-14 18 -30 16 -30 0 Z"/>'
             '<circle cx="-6" cy="0" r="5" stroke-width="1.2"/><rect x="14" y="-4" width="56" height="8" rx="2"/><rect x="70" y="-6" width="14" height="12" rx="3"/>'
             '<path d="M-22 -2 H76 M-22 2 H76" fill="none" stroke-width="0.7"/></g>')
    b.append(arms_only("pb", px, py, 1.25, (-40, 20)))
    # Pip bouncing on the bottom step with the tambourine
    b.append(char("pi", 310, 640, 1.2, arms=(14, -170), mood="happy", wag=True))
    qx, qy = paw("pi", 310, 640, 1.2, "R", -170)
    b.append(f'<circle cx="{qx + 18:.1f}" cy="{qy - 46:.1f}" r="22" stroke-width="2"/><circle cx="{qx + 18:.1f}" cy="{qy - 46:.1f}" r="15" stroke-width="1.2"/>'
             + "".join(f'<ellipse cx="{qx + 18 + 18.5*__import__("math").cos(a):.1f}" cy="{qy - 46 + 18.5*__import__("math").sin(a):.1f}" rx="4" ry="2.4" stroke-width="1"/>' for a in [k*1.047 for k in range(6)]))
    b.append(arms_only("pi", 310, 640, 1.2, (None, -170)))
    b.append(lines("M272 548 l-8 -6 M270 560 l-10 0 M350 548 l8 -6 M352 560 l10 0", 1.2))
    # music stand with a sheet of note symbols (no text)
    b.append(lines("M96 740 V610 M76 750 L96 740 L116 750", 2.4))
    b.append('<path d="M60 560 H132 L126 612 H66 Z" stroke-width="1.9"/>' + lines("M70 574 H122 M70 586 H122 M70 598 H122", 0.9)
             + note(84, 574, 0.45) + note(108, 588, 0.45, True))
    # lemonade pitcher and glasses on a little table, big flower pot by the steps
    b.append('<ellipse cx="500" cy="680" rx="62" ry="12" stroke-width="1.9"/><path d="M494 690 V752 H506 V690" stroke-width="1.7"/>')
    b.append('<path d="M460 676 Q456 640 466 626 L462 616 H490 Q494 640 490 676 Z" stroke-width="1.7"/><path d="M490 632 Q504 634 502 652 Q500 664 490 664" fill="none" stroke-width="2.4"/>'
             + '<circle cx="474" cy="650" r="8" stroke-width="1.1"/>' + lines("M474 642 V658 M466 650 H482", 0.8))
    b.append('<path d="M516 676 L512 646 H536 L532 676 Z M540 676 L536 650 H558 L554 676 Z" stroke-width="1.5"/>')
    b.append(plant("flowers", 60, 690, 1.3) + plant_pot(60, 752, 70, 56, "stripes"))
    return "".join(b)


def svg():
    return page(build(), TITLE)
