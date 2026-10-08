"""Page 22 — Sketchbook Desk (Miso drawing under the skylight)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import mug, plant, plant_pot, icon, book_open

TITLE = "Page 22 — Sketchbook Desk"


def pencil(x, y, rot, L=60, s=1.0):
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot}) scale({s})" stroke-width="{1.3/s:.2f}">'
            f'<path d="M0 -4 H{L} L{L + 12} 0 L{L} 4 H0 Z"/><path d="M0 0 H{L}" fill="none" stroke-width="{0.8/s:.2f}"/>'
            f'<path d="M{L} -4 V4" fill="none"/><path d="M{L + 8} -1.4 L{L + 12} 0 L{L + 8} 1.4 Z" fill="#000"/>'
            f'<rect x="-8" y="-4" width="8" height="8" rx="2"/></g>')


def paper(x, y, w, h, rot, kind):
    inner = {"teacup": icon("cup", 0, 4, 1.3), "flower": icon("flower", 0, 2, 1.3), "moon": icon("moon", 0, 2, 1.3)}[kind]
    return (f'<g transform="translate({x} {y}) rotate({rot})"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" stroke-width="1.5"/>'
            f'{inner}<circle cy="{-h/2 + 7}" r="4" stroke-width="1.2"/></g>')


def build():
    b = []
    # slanted skylight above
    b.append('<path d="M240 36 H560 L520 170 H200 Z" stroke-width="2.2"/>')
    b.append(clip_d("M252 46 H546 L512 160 H216 Z", '<use href="#cloud" transform="translate(330 100) scale(0.9)" stroke-width="1.6"/>'
                    + lines("M394 46 L362 160 M240 104 H530", 2.2), 1.4, fill="#fff"))
    b.append(lines("M30 200 H600", 1.2))
    # corkboard with pinned drawings
    b.append('<rect x="54" y="214" width="270" height="190" rx="5" stroke-width="2.2"/><rect x="64" y="224" width="250" height="170" stroke-width="1.2"/>')
    b.append("".join(f'<circle cx="{x}" cy="{y}" r="1.6" stroke-width="0.8"/>' for x in range(78, 310, 28) for y in range(238, 390, 28)))
    b.append(paper(118, 300, 76, 92, -6, "teacup") + paper(206, 280, 70, 80, 4, "flower") + paper(276, 330, 60, 76, -3, "moon"))
    # desk (side view)
    b.append('<rect x="40" y="476" width="420" height="20" rx="3" stroke-width="2.2"/>')
    b.append('<rect x="56" y="496" width="20" height="260" stroke-width="2"/><rect x="420" y="496" width="20" height="260" stroke-width="2"/>')
    b.append('<rect x="76" y="496" width="150" height="70" stroke-width="1.8"/><circle cx="151" cy="531" r="4" stroke-width="1.2"/>')
    # bendy lamp arcing over the desk (Dot on the shade)
    b.append('<ellipse cx="110" cy="472" rx="34" ry="8" stroke-width="1.8"/>')
    b.append('<path d="M106 466 C96 360 160 290 250 300 L252 312 C170 304 110 368 116 466 Z" stroke-width="1.8"/>')
    b.append('<path d="M240 292 L300 300 L322 352 Q288 368 250 350 Z" stroke-width="2"/>' + lines("M262 352 Q286 362 312 352", 1))
    b.append(dot(276, 286))
    b.append(lines("M272 372 L262 400 M292 374 L296 402 M310 366 L330 392", 1.1))
    # sketchbook with doodles of the friends' faces
    b.append(book_open(300, 470, 140, 54, 0))
    for (x, y, k) in ((256, 446, "bear"), (288, 452, "bunny"), (322, 446, "cat"), (350, 452, "panda")):
        ears = {"bear": f'<circle cx="{x-7}" cy="{y-8}" r="4"/><circle cx="{x+7}" cy="{y-8}" r="4"/>',
                "bunny": f'<ellipse cx="{x-4}" cy="{y-14}" rx="3" ry="8"/><ellipse cx="{x+4}" cy="{y-14}" rx="3" ry="8"/>',
                "cat": f'<path d="M{x-9} {y-4} L{x-8} {y-14} L{x-2} {y-8} Z M{x+9} {y-4} L{x+8} {y-14} L{x+2} {y-8} Z"/>',
                "panda": f'<circle cx="{x-8}" cy="{y-8}" r="4"/><circle cx="{x+8}" cy="{y-8}" r="4"/>'}[k]
        b.append(f'<g stroke-width="1">{ears}<circle cx="{x}" cy="{y}" r="10"/><circle cx="{x-3}" cy="{y-1}" r="1.2" fill="#000" stroke="none"/>'
                 f'<circle cx="{x+3}" cy="{y-1}" r="1.2" fill="#000" stroke="none"/><path d="M{x-2} {y+4} Q{x} {y+6} {x+2} {y+4}" fill="none"/></g>')
    b.append(lines("M240 462 q10 -6 20 0 q10 6 20 0 M330 466 q8 -8 16 0", 0.9))
    # jar of pencils, mug of pencils, eraser, cactus
    b.append(pencil(186, 432, -100, 44) + pencil(196, 430, -80, 50) + pencil(178, 436, -116, 40))
    b.append('<path d="M168 476 V430 H210 V476 Z" stroke-width="1.8"/>' + lines("M168 444 H210", 1))
    b.append(pencil(430, 436, -96, 38) + pencil(440, 436, -74, 42))
    b.append(mug(436, 478, 1.4, "dots"))
    b.append('<rect x="226" y="462" width="24" height="12" rx="3" stroke-width="1.5"/>' + lines("M236 462 V474", 0.9))
    b.append(plant("cactus", 70, 452, 0.8) + plant_pot(70, 476, 32, 24, "zigzag"))
    # rug and wastebasket of drafts
    b.append('<ellipse cx="300" cy="736" rx="250" ry="26" stroke-width="1.8"/><ellipse cx="300" cy="736" rx="210" ry="18" stroke-width="1.1"/>')
    b.append('<path d="M260 640 H340 L330 730 H270 Z" stroke-width="1.9"/>' + lines("M262 660 H338 M266 700 H334", 1)
             + '<path d="M270 640 L278 620 L296 626 L304 640 Z M304 640 L316 616 L334 624 L332 640 Z" stroke-width="1.3"/>')
    # crumpled paper ball on the floor
    b.append('<path d="M150 724 L162 702 L184 706 L196 724 L184 744 L160 742 Z" stroke-width="1.6"/>' + lines("M162 702 L172 722 L184 706 M172 722 L160 742 M172 722 L196 724", 0.9))
    # Miso on her tall stool, drawing
    b.append('<path d="M470 540 L452 756 M530 540 L548 756 M500 540 V756" stroke-width="5"/>'
             '<path d="M470 540 L452 756 M530 540 L548 756 M500 540 V756" stroke="#fff" stroke-width="2"/>'
             '<rect x="454" y="530" width="92" height="14" rx="5" stroke-width="2"/><path d="M462 680 H540" stroke-width="5"/><path d="M462 680 H540" stroke="#fff" stroke-width="2"/>')
    mx, my, ms = 500, 534, 1.6
    b.append(char("mi", mx, my, ms, arms=(None, 10), sit=True, head_rot=-8))
    px, py = paw("mi", mx, my, ms, "L", 66)
    b.append(pencil(px - 2, py + 2, 150, 34, 1.0))
    b.append(arms_only("mi", mx, my, ms, (66, None)))
    return "".join(b)


def svg():
    return page(build(), TITLE)
