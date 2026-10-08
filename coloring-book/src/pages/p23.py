"""Page 23 — The Very Long Scarf (Tofu knits, Bramble holds the skein)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import ribbon, yarn_ball, teacup, window_rect, basket

TITLE = "Page 23 — The Very Long Scarf"


def build():
    b = []
    # wall, window, floor
    b.append(window_rect(330, 70, 220, 200, '<use href="#cloud" transform="translate(410 130) scale(0.8)" stroke-width="1.7"/>'
                         '<path d="M330 220 C380 206 460 216 550 200 V270 H330 Z" stroke-width="1.3"/>', (1, 1)))
    b.append(lines("M30 470 H600", 1.4))
    b.append(clip_d("M30 470 H600 V800 H30 Z", lines(" ".join(f"M30 {y} H600" for y in range(510, 800, 44)), 1), 1.4))
    # side table with teacup between them
    b.append('<ellipse cx="350" cy="420" rx="44" ry="11" stroke-width="1.9"/><path d="M344 430 L340 500 H360 L356 430 Z" stroke-width="1.7"/>'
             '<ellipse cx="350" cy="502" rx="26" ry="6" stroke-width="1.6"/>' + teacup(350, 416, 1.1))
    # rocking chair with Tofu knitting
    b.append(lines("M96 170 V430 M246 170 V430", 6) + '<path d="M96 170 V430 M246 170 V430" stroke="#fff" stroke-width="3"/>')
    b.append('<path d="M90 160 Q171 130 252 160 L252 182 Q171 152 90 182 Z" stroke-width="1.9"/>')
    b.append(lines(" ".join(f"M{x} 176 V400" for x in (126, 156, 186, 216)), 4) + lines(" ".join(f"M{x} 176 V400" for x in (126, 156, 186, 216)), 1.4).replace('stroke-width="1.4"', 'stroke="#fff" stroke-width="1.4"'))
    b.append('<rect x="120" y="300" width="104" height="70" rx="12" stroke-width="1.6"/>')
    tx, ty, ts = 172, 450, 1.08
    b.append(char("to", tx, ty, ts, arms=(None, None), sit=True))
    b.append('<path d="M80 444 H262 V462 H80 Z" stroke-width="2"/>')
    b.append('<path d="M100 462 L92 540 M244 462 L252 540" stroke-width="5"/><path d="M100 462 L92 540 M244 462 L252 540" stroke="#fff" stroke-width="2"/>')
    b.append('<path d="M40 548 Q170 590 300 534 L304 544 Q170 604 36 558 Z" stroke-width="1.9"/>')
    # the very long scarf: from Tofu's needles in an S-curve across the floor
    b.append(ribbon([((172, 410), (172, 520), (60, 520), (70, 610)),
                     ((70, 610), (80, 700), (260, 720), (330, 660)),
                     ((330, 660), (390, 606), (500, 640), (560, 720))], 34, 14))
    b.append(lines("M146 392 L206 430 M198 392 L140 432", 2.6))
    b.append(arms_only("to", tx, ty, ts, (-40, 40)))
    # Bramble on his footstool holding the skein between his paws
    b.append('<path d="M386 640 Q386 600 440 600 H500 Q554 600 554 640 V676 H386 Z" stroke-width="2"/>' + lines("M386 650 H554", 1.1)
             + '<path d="M398 676 V706 H412 V676 M528 676 V706 H542 V676" stroke-width="1.7"/>')
    bx, by, bs = 470, 618, 1.15
    b.append(char("br", bx, by, bs, arms=(None, None), sit=True, mood="happy"))
    lx, ly = paw("br", bx, by, bs, "L", 60)
    rx, ry = paw("br", bx, by, bs, "R", -60)
    b.append(f'<path d="M{lx:.1f} {ly - 6:.1f} Q{(lx + rx)/2:.1f} {ly - 20:.1f} {rx:.1f} {ry - 6:.1f} L{rx:.1f} {ry + 6:.1f} Q{(lx + rx)/2:.1f} {ly - 6:.1f} {lx:.1f} {ly + 6:.1f} Z" stroke-width="1.6"/>'
             + lines(f"M{lx:.1f} {ly:.1f} Q{(lx + rx)/2:.1f} {ly - 13:.1f} {rx:.1f} {ry:.1f}", 0.8))
    b.append(arms_only("br", bx, by, bs, (60, -60)))
    b.append(lines(f"M{lx + 10:.1f} {ly - 8:.1f} C360 440 260 380 196 412", 1.1))
    # yarn basket with six balls (Dot in the basket)
    b.append(yarn_ball(420, 700, 16) + yarn_ball(452, 694, 18) + yarn_ball(486, 702, 15) + yarn_ball(436, 726, 14) + yarn_ball(470, 724, 16) + yarn_ball(502, 726, 13))
    b.append(basket(462, 754, 120, 40, handle=False))
    b.append(dot(512, 694, 0.9))
    return "".join(b)


def svg():
    return page(build(), TITLE)
