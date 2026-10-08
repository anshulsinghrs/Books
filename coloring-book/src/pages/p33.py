"""Page 33 — Tandem Ride (side profile along the country lane)."""
from math import sin, cos, radians
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, daisy, scallop_blob, blossom

TITLE = "Page 33 — Tandem Ride"


def wheel(x, y, r=52):
    spokes = " ".join(f"M{x} {y} L{x + r*0.86*cos(radians(a)):.1f} {y + r*0.86*sin(radians(a)):.1f}" for a in range(0, 360, 30))
    return (f'<circle cx="{x}" cy="{y}" r="{r}" stroke-width="2.4"/><circle cx="{x}" cy="{y}" r="{r*0.86:.1f}" stroke-width="1.3"/>'
            + lines(spokes, 1.0) + f'<circle cx="{x}" cy="{y}" r="6" stroke-width="1.5"/>')


def build():
    b = []
    b.append('<use href="#cloud" transform="translate(140 90) scale(1.2)" stroke-width="1.4"/><use href="#cloud" transform="translate(470 120) scale(0.9)" stroke-width="1.6"/>')
    # rolling fields with a small bridge
    b.append('<path d="M30 300 C150 260 260 290 360 280 C460 270 520 250 600 262 V800 H30 Z" stroke-width="1.5"/>')
    b.append(clip_d("M30 340 C140 320 300 350 600 320 V800 H30 Z", lines("M30 380 C200 370 400 386 600 360 M200 340 L180 420 M420 330 L440 410", 1.1), 1.5))
    b.append('<path d="M460 360 Q500 330 540 360 L540 372 Q500 344 460 372 Z" stroke-width="1.7"/>' + lines("M470 364 V376 M500 350 V362 M530 364 V376", 1))
    # hedgerow with blossoms
    b.append("".join(scallop_blob(x, 430, 50, 34, 8, 0.3, 1.6) for x in range(60, 620, 90)))
    b.append("".join(blossom(x, y, 9, 1.1) for x, y in ((60, 410), (130, 434), (220, 414), (310, 436), (390, 410), (470, 432), (560, 412))))
    # wooden fence
    b.append(lines(" ".join(f"M{x} 450 V530" for x in range(50, 600, 70)), 6) + lines(" ".join(f"M{x} 450 V530" for x in range(50, 600, 70)), 3).replace('stroke-width="3"', 'stroke="#fff" stroke-width="3"'))
    b.append('<rect x="30" y="470" width="570" height="9" stroke-width="1.5"/><rect x="30" y="500" width="570" height="9" stroke-width="1.5"/>')
    # signpost with arrow icons (Dot on top)
    b.append('<rect x="80" y="380" width="10" height="170" stroke-width="1.7"/><path d="M90 396 H140 L152 408 L140 420 H90 Z M80 430 H36 L26 442 L36 454 H80 Z" stroke-width="1.6"/>'
             + lines("M100 408 H132 M126 402 L132 408 L126 414 M70 442 H40 M46 436 L40 442 L46 448", 1.2))
    b.append(dot(85, 371))
    # the lane
    b.append('<path d="M30 640 H600 V800 H30 Z" stroke-width="1.6"/>' + lines("M60 700 H110 M180 720 H240 M330 704 H380 M460 726 H530", 1.2))
    b.append("".join(daisy(x, y, 9, 6) for x, y in ((50, 600), (560, 610), (300, 610), (430, 600))))
    # tandem bicycle (side view)
    b.append(wheel(160, 640) + wheel(450, 640))
    frame = "M160 640 L230 560 L330 640 L400 560 L450 640 M230 560 H400 M330 640 L280 560"
    b.append(f'<path d="{frame}" fill="none" stroke-width="6"/><path d="{frame}" fill="none" stroke="#fff" stroke-width="3"/>')
    b.append('<circle cx="330" cy="640" r="12" stroke-width="1.8"/>' + lines("M318 640 H342 M330 628 V652", 1.3))
    b.append('<path d="M400 560 L410 520 M410 520 H440" fill="none" stroke-width="4"/><circle cx="436" cy="516" r="5" stroke-width="1.4"/>')
    # front basket with Miso
    b.append(char("mi", 470, 534, 0.9, arms=(30, -30), mood="happy", tail=False))
    b.append(clip_d("M432 520 H508 L500 560 H440 Z", lines("M432 532 H508 M432 546 H508 M452 520 V560 M470 520 V560 M488 520 V560", 1), 1.9))
    # rear rack with the picnic bundle
    b.append('<path d="M160 580 H210" stroke-width="4"/><path d="M128 552 Q150 532 186 546 Q200 560 188 576 H130 Q118 568 128 552 Z" stroke-width="1.8"/>'
             + lines("M156 540 L150 576 M140 548 L170 548", 1.1))
    # Bramble (back seat) and Clover (front seat, scarf flying)
    b.append('<path d="M214 548 H252 L246 560 H220 Z M376 548 H414 L408 560 H382 Z" stroke-width="1.7"/>')
    b.append(char("br", 232, 576, 0.95, arms=(-60, -70), sit=True, mood="happy"))
    b.append('<path d="M366 446 Q330 440 300 452 Q312 460 300 470 Q334 462 366 462 Z" stroke-width="1.5"/>' + lines("M300 452 l-10 -4 M300 470 l-10 4", 1.1))
    b.append(char("cl", 392, 578, 0.9, arms=(-60, -70), sit=True, mood="happy"))
    # Pip running alongside
    b.append(char("pi", 530, 752, 0.85, arms=(140, -40), mood="happy", wag=True, head_rot=-6))
    b.append(lines("M476 720 h-20 M480 734 h-24", 1.2))
    return "".join(b)


def svg():
    return page(build(), TITLE)
