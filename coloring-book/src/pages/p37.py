"""Page 37 — Garden Tea Party (round lace table under the rose arch)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, scallop_blob
from props import teapot, teacup, bowl, mug

TITLE = "Page 37 — Garden Tea Party"


def rose(x, y, r=11):
    return (f'<g transform="translate({x} {y})" stroke-width="1.2"><circle r="{r}"/><path d="M{-r*0.5:.1f} {-r*0.2:.1f} Q0 {-r*0.8:.1f} {r*0.5:.1f} {-r*0.2:.1f} '
            f'Q{r*0.4:.1f} {r*0.5:.1f} 0 {r*0.4:.1f} Q{-r*0.5:.1f} {r*0.3:.1f} {-r*0.2:.1f} 0" fill="none"/></g>')


def iron_chair(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{2/s:.2f}" fill="none">'
            '<path d="M-30 0 V-110 Q-30 -130 0 -130 Q30 -130 30 -110 V0"/>'
            '<path d="M-14 -40 C-30 -60 -10 -80 0 -64 C10 -80 30 -60 14 -40 M0 -64 V-110 M-18 -96 C-26 -110 -6 -116 -6 -104 M18 -96 C26 -110 6 -116 6 -104"/>'
            '<path d="M-36 -30 H36"/></g>')


def build():
    b = []
    # hedge, sky, rose arch framing the top half
    b.append('<use href="#cloud" transform="translate(310 120) scale(1)" stroke-width="1.5"/>')
    b.append("".join(scallop_blob(x, 380, 70, 50, 9, 0.3, 1.6) for x in range(50, 640, 110)))
    b.append('<path d="M30 400 H600 V800 H30 Z" stroke-width="1.6"/>')
    arch = "M70 800 V260 Q70 70 310 70 Q550 70 550 260 V800"
    b.append(f'<path d="{arch}" fill="none" stroke-width="22"/><path d="{arch}" fill="none" stroke="#fff" stroke-width="16"/>')
    b.append(lines("M70 400 V800 M550 400 V800", 1))
    for (x, y) in ((70, 300), (82, 220), (110, 150), (160, 104), (220, 80), (290, 70), (360, 74), (420, 92), (480, 130), (520, 190), (546, 260), (550, 340),
                   (68, 380), (552, 420), (70, 460), (550, 500)):
        b.append(f'<path d="M{x + 10} {y + 6} q12 -2 16 8 q-12 2 -16 -8 Z M{x - 10} {y + 6} q-12 -2 -16 8 q12 2 16 -8 Z" stroke-width="1"/>' + rose(x, y, 12))
    # wrought-iron chairs, Tofu (left) and Juniper (right)
    b.append(iron_chair(150, 560, 1.0) + iron_chair(440, 560, 0.9))
    b.append(char("to", 150, 560, 1.0, arms=(-20, -40), sit=True))
    b.append(char("ju", 438, 560, 1.0, arms=(30, -20), sit=True))
    # round lace table
    b.append('<ellipse cx="300" cy="560" rx="200" ry="50" stroke-width="2.2"/>')
    lace = "M100 560 Q100 600 300 616 Q500 600 500 560 " + " ".join(f"a10 10 0 0 1 -20 4" for _ in range(20))
    b.append(f'<path d="M100 560 C100 610 200 620 300 622 C400 620 500 610 500 560" stroke-width="2"/>')
    b.append(lines(" ".join(f"M{x} {600 + 14*((x - 300) / 200)**2:.0f} a8 8 0 0 0 16 0" for x in range(110, 490, 16)), 1.2))
    b.append(lines(" ".join(f"M{x} 600 V740" for x in (280, 320)), 6) + lines("M280 600 V740 M320 600 V740", 2.6).replace('stroke-width="2.6"', 'stroke="#fff" stroke-width="2.6"'))
    b.append('<ellipse cx="300" cy="746" rx="60" ry="12" stroke-width="1.8"/>')
    # three-tier stand with sandwiches, scones and small cakes
    b.append('<rect x="296" y="420" width="8" height="132" stroke-width="1.5"/>')
    for (y, rx) in ((548, 60), (500, 46), (456, 34)):
        b.append(f'<ellipse cx="300" cy="{y}" rx="{rx}" ry="8" stroke-width="1.7"/>')
    for (x, y) in ((262, 540), (300, 536), (338, 540)):
        b.append(f'<path d="M{x - 14} {y} L{x + 14} {y} L{x} {y - 16} Z" stroke-width="1.3"/>' + lines(f"M{x - 9} {y - 5} H{x + 9}", 0.8))
    for (x, y) in ((276, 494), (324, 494)):
        b.append(f'<path d="M{x - 12} {y} Q{x - 12} {y - 18} {x} {y - 18} Q{x + 12} {y - 18} {x + 12} {y} Z" stroke-width="1.3"/>' + lines(f"M{x - 10} {y - 8} H{x + 10}", 0.9))
    b.append('<rect x="288" y="436" width="24" height="18" rx="2" stroke-width="1.3"/><circle cx="300" cy="431" r="5" stroke-width="1.2"/>')
    # floral teapot, cups, sugar bowl with tongs, milk jug, vase of roses
    b.append(teapot(196, 568, 0.85) + teacup(380, 566, 1.05) + teacup(240, 590, 1.0))
    b.append(bowl(420, 590, 34, 18) + lines("M412 568 L426 582 M416 566 L428 580", 1.2))
    b.append('<path d="M146 596 Q140 570 150 560 H168 Q178 570 172 596 Z" stroke-width="1.6"/><path d="M150 562 L142 556" stroke-width="1.5"/>')
    b.append('<path d="M350 612 Q340 580 352 560 H370 Q382 580 372 612 Z" stroke-width="1.6"/>' + rose(354, 548, 9) + rose(370, 540, 9) + rose(362, 556, 8))
    # Thimble sitting in a teacup like a tiny armchair
    b.append(teacup(300, 616, 1.8))
    b.append(char("th", 300, 592, 1.1, arms=(30, -30), sit=True, mood="happy"))
    b.append('<path d="M277 588 H323 Q322 606 300 608 Q278 606 277 588 Z" stroke-width="1.5"/>')
    # Bramble, his back partly to the viewer, in the foreground
    b.append(char("br", 448, 806, 1.2, arms=(30, -30), back=True, sit=True))
    # bird bath (Dot on the rim)
    b.append('<g transform="translate(-410 50)"><path d="M500 690 H540 L532 600 H508 Z" stroke-width="1.8"/><ellipse cx="520" cy="694" rx="30" ry="8" stroke-width="1.6"/>'
             '<path d="M476 594 Q520 620 564 594 Z" stroke-width="1.8"/><ellipse cx="520" cy="594" rx="44" ry="10" stroke-width="1.8"/></g>')
    b.append(dot(94, 626, 0.9))

    return "".join(b)


def svg():
    return page(build(), TITLE)
