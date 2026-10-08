"""Page 30 — Meadow Path (panorama, the friends small in a big summer meadow)."""
from chars import char, dot, page, paw
from scene import clip_d, lines, daisy, scallop_blob, tuft
from props import butterfly, sun_hat

TITLE = "Page 30 — Meadow Path"


def poppy(x, y, r=16):
    return (f'<g transform="translate({x} {y})" stroke-width="1.4">'
            + "".join(f'<path transform="rotate({a})" d="M0 0 C-{r*0.9:.0f} -{r*0.3:.0f} -{r*0.8:.0f} -{r:.0f} 0 -{r:.0f} C{r*0.8:.0f} -{r:.0f} {r*0.9:.0f} -{r*0.3:.0f} 0 0 Z"/>' for a in (0, 90, 180, 270))
            + f'<circle r="{r*0.28:.1f}"/></g>')


def cornflower(x, y, r=12):
    return (f'<g transform="translate({x} {y})" stroke-width="1.2">'
            + "".join(f'<path transform="rotate({a})" d="M0 0 L-3 -{r:.0f} L0 -{r*0.8:.0f} L3 -{r:.0f} Z"/>' for a in range(0, 360, 36))
            + f'<circle r="{r*0.3:.1f}"/></g>')


def clover_bloom(x, y, r=9):
    return (f'<use href="#scallop" transform="translate({x} {y}) scale({r/10:.2f})" stroke-width="{1.2*10/r:.2f}"/>'
            f'<circle cx="{x}" cy="{y}" r="{r*0.45:.1f}" stroke-width="1"/>')


def build():
    b = []
    b.append('<use href="#cloud" transform="translate(150 90) scale(1.3)" stroke-width="1.3"/><use href="#cloud" transform="translate(420 70) scale(1)" stroke-width="1.5"/>'
             '<use href="#cloud" transform="translate(520 170) scale(0.7)" stroke-width="1.8"/>')
    # distant hills and the windmill
    b.append('<path d="M30 300 C120 260 220 270 300 290 C380 310 460 260 600 270 V800 H30 Z" stroke-width="1.5"/>')
    b.append('<path d="M30 360 C160 330 300 350 420 340 C500 334 560 344 600 340 V800 H30 Z" stroke-width="1.5"/>')
    b.append('<path d="M448 300 L456 236 H476 L484 300 Z" stroke-width="1.6"/><path d="M452 240 L466 222 L480 240 Z" stroke-width="1.5"/>')
    for a in (20, 110, 200, 290):
        b.append(f'<path transform="translate(466 236) rotate({a})" d="M0 0 L6 -4 L46 -10 L46 4 L6 4 Z" stroke-width="1.4"/>')
    b.append('<circle cx="466" cy="236" r="4" stroke-width="1.3"/>')
    # winding S-path from the lower left to the horizon
    path = "M60 800 C120 700 300 690 300 600 C300 520 160 500 200 440 C230 396 300 380 330 352 L350 352 C330 384 270 400 250 444 C226 500 360 520 370 600 C380 690 240 720 200 800 Z"
    b.append(f'<path d="{path}" stroke-width="1.8"/>')
    # tall grass texture
    b.append("".join(tuft(x, y, 0.9) for x, y in ((90, 420), (420, 420), (520, 470), (110, 520), (470, 540), (80, 600), (540, 610), (440, 650))))
    # wooden stile with Dot on the post
    b.append('<rect x="392" y="440" width="12" height="96" stroke-width="1.7"/><rect x="464" y="440" width="12" height="96" stroke-width="1.7"/>'
             '<rect x="380" y="466" width="110" height="10" rx="2" stroke-width="1.6"/><rect x="380" y="500" width="110" height="10" rx="2" stroke-width="1.6"/>'
             '<rect x="404" y="522" width="60" height="9" rx="2" stroke-width="1.5"/>')
    b.append(dot(398, 430.5))
    # the friends, small in the landscape: Pebble, Clover, Tofu (in his sun hat, walking stick)
    b.append(char("pb", 236, 466, 0.55, arms=(30, -30), mood="happy"))
    b.append(char("cl", 270, 474, 0.6, arms=(20, -150), mood="happy"))
    b.append(char("to", 316, 490, 0.62, arms=(14, -20)))
    hx, hy = 316, 490 - 0.62 * 156
    b.append(sun_hat(hx, hy, 70))
    wx, wy = paw("to", 316, 490, 0.62, "R", -20)
    b.append(lines(f"M{wx + 2:.1f} {wy - 30:.1f} L{wx + 6:.1f} {wy + 30:.1f}", 2.4))
    # big foreground flowers framing the lower edge
    b.append(lines("M70 760 Q66 690 80 640 M150 770 Q156 700 140 660 M480 770 Q470 700 490 650 M550 770 Q560 720 540 670 M240 780 Q236 740 250 710 M410 780 Q414 740 400 712", 2))
    b.append('<path d="M80 700 Q50 690 40 670 Q66 670 80 700 Z M140 710 Q170 700 180 680 Q156 680 140 710 Z M490 700 Q520 690 530 670 Q504 672 490 700 Z" stroke-width="1.3"/>')
    b.append(poppy(80, 636, 26) + daisy(140, 650, 22, 9) + cornflower(250, 704, 18) + clover_bloom(400, 706, 14)
             + poppy(490, 644, 24) + daisy(540, 660, 22, 9) + cornflower(46, 720, 16) + clover_bloom(580, 730, 12))
    b.append(daisy(120, 560, 12, 8) + poppy(520, 560, 14) + cornflower(90, 500, 10) + daisy(460, 590, 11, 7) + clover_bloom(560, 520, 9))
    b.append(''.join(daisy(x, y, 7, 6, 1) if (x + y) % 3 else clover_bloom(x, y, 6) for x, y in ((70, 450), (150, 470), (380, 560), (430, 470), (560, 400), (100, 680), (520, 500), (330, 650), (420, 620), (60, 560))))
    b.append(butterfly(200, 380, 1.1, -10) + butterfly(420, 400, 0.9, 15) + butterfly(150, 610, 1.2, 10))
    return "".join(b)


def svg():
    return page(build(), TITLE)
