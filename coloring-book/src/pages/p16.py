"""Page 16 — Umbrella Parade (Clover, Juniper, Pebble down the cobbled lane)."""
from chars import char, dot, page, paw
from scene import clip_d, lines, scallop_blob, daisy
from props import umbrella, boots, raincoat, splash, puddle, cobbles, drop, duck, frog

TITLE = "Page 16 — Umbrella Parade"


def cottage(x, y, w, h, roof=40):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" stroke-width="1.8"/>'
            f'<path d="M{x - 10} {y + 2} L{x + w/2} {y - roof} L{x + w + 10} {y + 2} Z" stroke-width="1.8"/>'
            + clip_d(f"M{x - 10} {y + 2} L{x + w/2} {y - roof} L{x + w + 10} {y + 2} Z",
                     lines(" ".join(f"M{x - 20} {y - roof + k*14} H{x + w + 20}" for k in range(1, 4)), 0.9), 1.8)
            + f'<rect x="{x + w*0.18:.0f}" y="{y + h*0.25:.0f}" width="{w*0.24:.0f}" height="{h*0.3:.0f}" stroke-width="1.4"/>'
            + f'<path d="M{x + w*0.58:.0f} {y + h} V{y + h*0.45:.0f} Q{x + w*0.7:.0f} {y + h*0.32:.0f} {x + w*0.82:.0f} {y + h*0.45:.0f} V{y + h} Z" stroke-width="1.4"/>')


def build():
    b = []
    # cottages lining the lane, hedge, ground
    b.append(cottage(56, 210, 110, 90, 46) + cottage(190, 240, 80, 66, 34) + cottage(330, 230, 96, 76, 40) + cottage(456, 196, 110, 104, 50))
    b.append('<path d="M30 300 H600 V800 H30 Z" stroke-width="1.6"/>')
    lane = "M180 300 H290 L600 760 H40 Z"
    b.append(clip_d(lane, cobbles(30, 300, 600, 800, 44, 22), 1.8))
    b.append(scallop_blob(520, 380, 90, 56, 10, 0.3, 1.7) + scallop_blob(590, 470, 70, 60, 9, 0.3, 1.7))
    b.append("".join(daisy(x, y, 8, 6, 1) for x, y in ((480, 360), (530, 400), (560, 352), (574, 460))))
    # lamppost with a hanging flower basket
    b.append('<rect x="84" y="250" width="12" height="380" stroke-width="1.8"/><path d="M74 630 H106 L110 646 H70 Z" stroke-width="1.8"/>')
    b.append('<path d="M70 250 H110 L102 214 H78 Z" stroke-width="1.8"/><path d="M76 214 L90 196 L104 214 Z" stroke-width="1.6"/>'
             + lines("M90 214 V250", 1.1))
    b.append(lines("M96 290 H130 M126 290 V306", 1.6) + '<path d="M108 306 H144 Q144 328 126 330 Q108 328 108 306 Z" stroke-width="1.6"/>'
             + daisy(114, 302, 8, 6, 1) + daisy(130, 298, 8, 6, 1) + daisy(142, 304, 7, 6, 1))
    # duck family following behind
    b.append(duck(174, 426, 1.0, True) + duck(146, 438, 0.6, True) + duck(122, 446, 0.6, True) + duck(100, 452, 0.55, True))
    # puddles along the way, frog on a stone
    b.append(puddle(150, 700, 70, 18) + puddle(380, 650, 60, 14) + puddle(560, 740, 50, 13))
    b.append('<ellipse cx="96" cy="684" rx="26" ry="11" stroke-width="1.6"/>' + frog(96, 678, 0.95))
    # the parade, back to front, umbrellas at three heights
    for (c, x, y, s, r, pat) in (("cl", 210, 470, 1.05, 80, "dots"), ("ju", 326, 608, 1.25, 88, "scallops"), ("pb", 458, 742, 1.45, 76, "stripes")):
        ux, uy = paw(c, x, y, s, "R", -175)
        b.append(umbrella(ux, uy - 1.3 * r, r, pat, rot=0))
        b.append(char(c, x, y, s, arms=(14, -175), sweater=raincoat(c), front=boots(c, s), mood="happy" if c != "ju" else "open"))
        if c == "cl":
            b.append(dot(ux, uy - 1.3 * r - r * 0.72 - 23))
        b.append(splash(x - 18 * s, y + 2, 0.8) + splash(x + 18 * s, y + 2, 0.8))
    # rain, spaced evenly, kept off the umbrellas
    for row in range(12):
        for col in range(11):
            x = 60 + col * 50 + (25 if row % 2 else 0)
            y = 60 + row * 52
            if (130 < x < 320 and 150 < y < 480) or (230 < x < 440 and 270 < y < 620) or (370 < x < 560 and 440 < y < 760):
                continue
            if y > 300 and x < 260 and y > 640:
                continue
            b.append(drop(x, y, 1.1))
    return "".join(b)


def svg():
    return page(build(), TITLE)
