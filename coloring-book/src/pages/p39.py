"""Page 39 — The Hollow Bakery (Bramble hands Juniper a boxed cake)."""
from chars import char, arms_only, dot, page, paw, apron
from scene import clip_d, lines
from props import chef_hat, icon, cupcake

TITLE = "Page 39 — The Hollow Bakery"


def croissant(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}"><path d="M-22 4 Q-18 -14 0 -16 Q18 -14 22 4 Q14 0 10 6 Q0 0 -10 6 Q-14 0 -22 4 Z"/>'
            '<path d="M-10 6 Q-6 -8 0 -16 M10 6 Q6 -8 0 -16" fill="none" stroke-width="1"/></g>')


def roll(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}"><ellipse rx="18" ry="11"/>'
            '<path d="M0 0 m3 0 a3 2 0 1 1 -6 0 a7 5 0 1 1 14 0 a11 8 0 1 1 -22 0" fill="none" stroke-width="1"/></g>')


def tart(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}"><path d="M-18 0 L-14 -10 H14 L18 0 Z"/><ellipse cy="-10" rx="14" ry="4"/>'
            '<circle cx="-6" cy="-12" r="3.4"/><circle cx="2" cy="-13" r="3.4"/><circle cx="8" cy="-10" r="3"/></g>')


def macaron(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}"><ellipse cy="-4" rx="11" ry="5"/><rect x="-10" y="-3" width="20" height="4" rx="2"/><ellipse cy="4" rx="11" ry="5"/></g>')


def build():
    b = []
    # checkerboard floor (large squares)
    fl = "M30 600 H600 V800 H30 Z"
    chk = "".join(f'<rect x="{x}" y="{y}" width="50" height="40" fill="#fff" stroke-width="1"/>' for x in range(30, 600, 50) for y in range(600, 800, 40))
    chk += "".join(f'<path d="M{x + 10} {y + 8} H{x + 40} V{y + 32} H{x + 10} Z" stroke-width="0.8"/>' for x in range(30, 600, 100) for y in range(600, 800, 80))
    b.append(clip_d(fl, chk, 1.6))
    # left wall: front window with the striped awning outside, door with the bell
    b.append('<rect x="44" y="120" width="140" height="200" rx="4" stroke-width="2"/>')
    aw = "M44 128 H184 V170 " + " ".join(f"Q{184 - 10 - k*20} 186 {184 - 20 - k*20} 170" for k in range(7)) + " Z"
    b.append(clip_d("M52 128 H176 V312 H52 Z", '<use href="#cloud" transform="translate(110 240) scale(0.6)" stroke-width="2"/>' +
                    clip_d(aw, lines(" ".join(f"M{x} 120 V190" for x in range(54, 190, 20)), 4), 1.6), 1.4, fill="#fff"))
    b.append(lines("M114 128 V312", 2.2))
    b.append('<path d="M44 600 V380 Q44 340 90 340 Q136 340 136 380 V600 Z" stroke-width="2"/><circle cx="122" cy="480" r="4" stroke-width="1.3"/>')
    b.append('<rect x="56" y="386" width="68" height="60" rx="4" stroke-width="1.5"/>' + lines("M90 386 V446", 1.2))
    b.append('<path d="M90 330 V318 M78 316 H102" stroke-width="1.6"/><path d="M78 334 Q78 316 90 316 Q102 316 102 334 Z" stroke-width="1.7"/><circle cx="90" cy="337" r="3" stroke-width="1.2"/>')
    b.append(dot(90, 306, 0.9))
    # back wall: shelves with baskets of bread, chalkboard menu with food icons
    b.append('<rect x="210" y="70" width="380" height="12" rx="2" stroke-width="1.8"/><rect x="210" y="190" width="380" height="12" rx="2" stroke-width="1.8"/>')
    for x in (230, 330, 430):
        b.append(f'<path d="M{x} 70 L{x + 6} 36 L{x + 12} 70 Z M{x + 16} 70 L{x + 24} 30 L{x + 32} 70 Z M{x + 36} 70 L{x + 42} 40 L{x + 48} 70 Z" stroke-width="1.5"/>')
        b.append(f'<path d="M{x - 6} 70 H{x + 56} L{x + 50} 82 H{x} Z" stroke-width="1.6"/>')
    for x in (240, 320, 400, 480, 560):
        b.append(f'<path d="M{x - 24} 190 Q{x - 24} 156 {x} 154 Q{x + 24} 156 {x + 24} 190 Z" stroke-width="1.7"/>' + lines(f"M{x - 12} 170 l8 -8 M{x} 172 l8 -8", 1))
    b.append('<rect x="250" y="226" width="150" height="110" rx="4" stroke-width="2.4"/><rect x="260" y="236" width="130" height="90" stroke-width="1.2"/>')
    b.append(icon("cup", 286, 262, 1.0) + icon("heart", 326, 262, 0.8) + icon("star", 362, 262, 0.8) + lines("M276 300 H374 M276 314 H350", 1))
    # old-fashioned scale
    b.append('<path d="M450 340 H530 L520 356 H460 Z" stroke-width="1.8"/><rect x="484" y="300" width="12" height="40" stroke-width="1.5"/>'
             '<circle cx="490" cy="296" r="20" stroke-width="1.8"/><circle cx="490" cy="296" r="14" stroke-width="1"/>' + lines("M490 296 L498 286", 1.4)
             + '<path d="M458 280 H522 Q518 268 490 268 Q462 268 458 280 Z" stroke-width="1.5"/>')
    # Bramble behind the counter in baker's cap and apron
    bx, by, bs = 380, 560, 1.45
    b.append(char("br", bx, by, bs, arms=(None, None), outfit=apron("br", bs, top_frac=0.45), mood="happy"))
    b.append(chef_hat(bx, by - 150 * bs - 30, 1.15))
    # curved glass display case along the counter
    b.append('<rect x="200" y="470" width="400" height="130" stroke-width="2.2"/>' + lines("M200 540 H600", 1.6))
    b.append('<path d="M200 470 Q206 410 240 404 H600 V470 Z" stroke-width="2"/>' + lines("M232 414 Q218 430 214 460 M246 412 Q236 430 234 458", 1))
    b.append(croissant(260, 462) + croissant(310, 464) + roll(370, 462) + roll(414, 462) + macaron(462, 462) + macaron(490, 462) + macaron(518, 462))
    b.append(tart(260, 532) + tart(306, 532) + tart(352, 532))
    b.append('<rect x="420" y="490" width="90" height="42" rx="4" stroke-width="1.8"/><path d="M420 506 H510" fill="none" stroke-width="1"/>'
             '<path d="M420 490 Q465 474 510 490" stroke-width="1.5"/>' + "".join(f'<circle cx="{x}" cy="486" r="4" stroke-width="1.1"/>' for x in (434, 452, 470, 488, 506)))
    b.append(lines("M230 560 H330 M380 576 H480 M520 560 H580", 1))
    # cake box tied with string, passed across the counter
    b.append('<rect x="198" y="352" width="96" height="76" rx="3" stroke-width="2"/>' + lines("M246 352 V428 M198 390 H294", 1.4)
             + '<path d="M246 352 Q230 334 238 328 Q248 330 246 352 Q262 334 256 328 Q244 330 246 352 Z" stroke-width="1.3"/>')
    b.append(arms_only("br", bx, by, bs, (60, -14)))
    # Juniper reaching for the cake box
    jx, jy, js = 160, 742, 1.45
    b.append(char("ju", jx, jy, js, arms=(14, -150), brows=True))
    return "".join(b)


def svg():
    return page(build(), TITLE)
