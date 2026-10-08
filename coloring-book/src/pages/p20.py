"""Page 20 — The Blanket Fort (cutaway; flashlight stories inside)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import cushion, book_open, quilt_patch

TITLE = "Page 20 — The Blanket Fort"


def chair(x, y, h=260, mirror=1):
    return (f'<path d="M{x - 30} {y} V{y - h} H{x + 30} V{y} M{x - 30} {y - h + 30} H{x + 30} M{x - 30} {y - h + 70} H{x + 30}" fill="none" stroke-width="6"/>'
            f'<path d="M{x - 30} {y} V{y - h} H{x + 30} V{y} M{x - 30} {y - h + 30} H{x + 30} M{x - 30} {y - h + 70} H{x + 30}" fill="none" stroke="#fff" stroke-width="3"/>')


def build():
    b = []
    # living-room wall and floor behind
    b.append(clip_d("M30 30 H600 V560 H30 Z", lines(" ".join(f"M{x} 30 V560" for x in range(60, 600, 44)), 0.9), 1.4))
    b.append('<path d="M30 560 H600 V800 H30 Z" stroke-width="1.6"/>' + lines("M30 600 H600 M30 660 H600", 1))
    b.append(chair(96, 560) + chair(524, 560))
    # back wall of the fort: a patchwork blanket
    back = "M86 300 L310 156 L534 300 V640 H86 Z"
    patches = ""
    for r in range(8):
        for c in range(12):
            x, y = 80 + c * 40, 150 + r * 40
            if (r + c) % 3 == 0:
                patches += f'<circle cx="{x + 20}" cy="{y + 20}" r="5" stroke-width="0.9"/>'
            elif (r + c) % 3 == 1:
                patches += f'<path d="M{x + 8} {y + 8} L{x + 32} {y + 32} M{x + 32} {y + 8} L{x + 8} {y + 32}" fill="none" stroke-width="0.8"/>'
    patches += lines(" ".join(f"M{x} 140 V660" for x in range(80, 560, 40)) + " " + " ".join(f"M60 {y} H560" for y in range(150, 660, 40)), 1.0)
    b.append(clip_d(back, patches, 2))
    # roof: striped blanket draped over the chair backs, fairy lights along the edge
    roof = "M60 312 L310 140 L560 312 L548 330 L310 168 L72 330 Z"
    b.append(clip_d(roof, lines(" ".join(f"M{x} 100 L{x - 200} 400" for x in range(100, 900, 26)), 1.0), 2))
    for k in range(1, 12):
        t = k / 12
        for (x0, y0, x1, y1) in ((72, 334, 310, 172), (310, 172, 548, 334)):
            x, y = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t + 6
            b.append(f'<circle cx="{x:.1f}" cy="{y + 8:.1f}" r="5" stroke-width="1.2"/><rect x="{x - 2.5:.1f}" y="{y:.1f}" width="5" height="4" stroke-width="0.9"/>')
    b.append('<rect x="294" y="128" width="32" height="12" rx="3" stroke-width="1.6"/>' + lines("M310 128 V118", 1.4))
    b.append(dot(310, 113))
    # clothespins holding the roof
    for x, y in ((96, 314), (524, 314)):
        b.append(f'<rect x="{x - 5}" y="{y - 18}" width="10" height="34" rx="3" stroke-width="1.5"/>' + lines(f"M{x} {y - 18} V{y + 16}", 0.9))
    # pillow pile on the floor of the fort
    b.append(cushion(170, 610, 120, 60, "stripes", -6) + cushion(310, 624, 140, 64, "dots", 3) + cushion(450, 610, 120, 60, "zigzag", 6))
    # friends inside: Clover, Pip (with the flashlight), Pebble, Thimble
    b.append(char("cl", 160, 620, 1.3, arms=(-30, 20), sit=True, mood="happy"))
    b.append(char("pi", 290, 626, 1.3, arms=(14, -150), sit=True, mood="happy"))
    fx, fy = paw("pi", 290, 626, 1.3, "R", -150)
    b.append(f'<path d="M{fx + 4:.1f} {fy - 10:.1f} L{fx + 130:.1f} {fy - 170:.1f} L{fx + 190:.1f} {fy - 110:.1f} L{fx + 14:.1f} {fy - 2:.1f} Z" stroke-width="1.2" stroke-dasharray="5 4"/>')
    b.append(f'<g transform="translate({fx:.1f} {fy:.1f}) rotate(-40)" stroke-width="1.6"><rect x="-6" y="-26" width="14" height="30" rx="3"/><path d="M-9 -26 H11 L14 -38 H-12 Z"/></g>')
    b.append(arms_only("pi", 290, 626, 1.3, (None, -150)))
    b.append(char("pb", 404, 630, 1.4, arms=(-20, 20), sit=True))
    b.append(book_open(404, 604, 66, 34))
    b.append(arms_only("pb", 404, 630, 1.4, (-20, 20)))
    b.append(book_open(160, 594, 70, 36))
    b.append(char("th", 486, 604, 1.6, arms=(150, -20), mood="happy"))
    # plate of cookies at the front
    b.append('<ellipse cx="320" cy="690" rx="70" ry="18" stroke-width="1.8"/><ellipse cx="320" cy="690" rx="54" ry="12" stroke-width="1"/>')
    for (x, y) in ((294, 682), (322, 678), (346, 686), (312, 692)):
        b.append(f'<circle cx="{x}" cy="{y}" r="14" stroke-width="1.5"/><circle cx="{x - 4}" cy="{y - 3}" r="1.7" fill="#000" stroke="none"/><circle cx="{x + 5}" cy="{y + 3}" r="1.7" fill="#000" stroke="none"/>')
    # the front blanket pulled back like a curtain on the left
    curtain = "M40 300 L180 210 C150 300 120 420 140 560 C150 620 130 680 100 740 L40 740 Z"
    b.append(clip_d(curtain, lines(" ".join(f"M{x} 200 Q{x + 30} 480 {x - 10} 760" for x in range(40, 200, 22)), 1.1)
                    + "".join(quilt_patch(x, y, 34, 34, pat="dots" if (x + y) % 2 else None, stitch=False) for x in range(40, 200, 68) for y in range(260, 760, 68)), 2.2))
    b.append('<path d="M110 520 Q134 506 156 520 Q134 540 112 534 Z" stroke-width="1.7"/>')
    b.append(f'<rect x="146" y="504" width="10" height="30" rx="3" stroke-width="1.5"/>')
    return "".join(b)


def svg():
    return page(build(), TITLE)
