"""Page 50 — Under the Friendship Quilt (finale inside a four-season wreath)."""
import math
from chars import char, dot, page, paw
from scene import clip_d, lines, blossom, daisy, oak_leaf, uid

TITLE = "Page 50 — Under the Friendship Quilt"
CX, CY, RI, RO = 310, 398, 222, 262
S = 0.75


def pt(theta, r):
    a = math.radians(theta)
    return CX + r * math.sin(a), CY - r * math.cos(a)


def sunflower(x, y, r=17):
    pet = "".join(f'<ellipse cx="0" cy="{-r*0.72:.1f}" rx="{r*0.22:.1f}" ry="{r*0.4:.1f}" transform="rotate({k*30})"/>' for k in range(12))
    seeds = "".join(f'<circle cx="{r*0.2*math.cos(a):.1f}" cy="{r*0.2*math.sin(a):.1f}" r="1.1" fill="#000" stroke="none"/>'
                    for a in [k * math.pi / 3 for k in range(6)])
    return (f'<g transform="translate({x:.1f} {y:.1f})" stroke-width="1.2">{pet}'
            f'<circle r="{r*0.38:.1f}" stroke-width="1.4"/>{seeds}</g>')


def pine_sprig(x, y, rot, s=1.0):
    needles = "".join(f'<path d="M0 {-k*5} l-7 -6 M0 {-k*5} l7 -6" />' for k in range(1, 6))
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot}) scale({s})" fill="none" stroke-width="{1.2/s:.2f}">'
            f'<path d="M0 6 V-30"/>{needles}</g>')


def holly(x, y, rot):
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot})" stroke-width="1.2">'
            '<path d="M0 0 Q-4 -5 -10 -4 Q-9 -9 -14 -12 Q-8 -13 -6 -18 Q-2 -12 0 -10 Z"/>'
            '<path d="M0 0 Q4 -5 10 -4 Q9 -9 14 -12 Q8 -13 6 -18 Q2 -12 0 -10 Z"/>'
            '<circle cx="-3" cy="2" r="3.4"/><circle cx="3.5" cy="2.5" r="3.4"/><circle cy="-2" r="3.4"/></g>')


def bow(x, y, rot):
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot})" stroke-width="1.5">'
            '<path d="M0 0 L-16 -11 Q-20 0 -16 11 Z"/><path d="M0 0 L16 -11 Q20 0 16 11 Z"/>'
            '<path d="M-3 2 L-10 22 L-4 19 L-1 24 Z"/><path d="M3 2 L10 22 L4 19 L1 24 Z"/>'
            '<circle r="5"/></g>')


def wreath():
    b = []
    b.append(f'<path fill-rule="evenodd" d="M{CX-RO} {CY} a{RO} {RO} 0 1 0 {2*RO} 0 a{RO} {RO} 0 1 0 {-2*RO} 0 Z '
             f'M{CX-RI} {CY} a{RI} {RI} 0 1 0 {2*RI} 0 a{RI} {RI} 0 1 0 {-2*RI} 0 Z" stroke-width="2.2"/>')
    rm = (RI + RO) / 2
    # spring blossoms — upper left (left -> top)
    for k, th in enumerate(range(279, 357, 9)):
        x, y = pt(th, rm + (6 if k % 2 else -6))
        lx, ly = pt(th + 6, rm + (-10 if k % 2 else 10))
        b.append(f'<path transform="translate({lx:.1f} {ly:.1f}) rotate({th + 90})" d="M0 0 C-4 -5 -4 -11 0 -15 C4 -11 4 -5 0 0 Z" stroke-width="1.1"/>')
        b.append(blossom(round(x, 1), round(y, 1), 14, 1.2, th))
    # summer sunflowers and daisies — upper right
    for k, th in enumerate(range(9, 86, 11)):
        x, y = pt(th, rm + (5 if k % 2 else -4))
        b.append(sunflower(x, y, 18) if k % 2 == 0 else daisy(round(x, 1), round(y, 1), 15, 8, 1.2))
    # autumn oak leaves and acorns — lower right
    for k, th in enumerate(range(97, 177, 8)):
        x, y = pt(th, rm + (7 if k % 2 else -7))
        if k % 2 == 0:
            b.append(oak_leaf(round(x, 1), round(y + 14, 1), th + 40 + (k % 3) * 25, 1.45, 1.2))
        else:
            b.append(f'<g transform="translate({x:.1f} {y:.1f}) rotate({th - 90})" stroke-width="1.2"><ellipse cy="5" rx="7" ry="9"/>'
                     '<path d="M-9 0 Q0 -10 9 0 Q0 3 -9 0 Z"/><path d="M0 -5 V-10" fill="none"/></g>')
    # winter pine, holly and snowflakes — lower left
    for k, th in enumerate(range(185, 268, 8)):
        x, y = pt(th, rm)
        if k % 3 == 0:
            b.append(holly(x, y, th))
        elif k % 3 == 1:
            b.append(pine_sprig(x, y + 14, th + 160, 1.35))
        else:
            b.append(f'<use href="#flake" transform="translate({x:.1f} {y:.1f}) scale(1.45)" stroke-width="1.0"/>')
    for th in (0, 90, 180, 270):
        x, y = pt(th, rm)
        b.append(bow(x, y, th))
    return "".join(b)


def room():
    b = []
    # wallpaper of tiny stars and the mantelpiece
    b.append(lines(" ".join(f"M{x} {y} l0 0" for x in range(100, 520, 40) for y in range(190, 250, 30)), 0.1))
    for (x, y) in ((176, 214), (440, 214), (230, 190), (390, 190)):
        b.append(f'<use href="#star4" transform="translate({x} {y}) scale(0.7)" stroke-width="1.6"/>')
    # fireplace
    b.append('<rect x="196" y="258" width="228" height="140" stroke-width="2"/>')
    b.append(clip_d("M196 258 H424 V398 H196 Z",
                    lines("M196 290 H424 M196 322 H424 M196 354 H424 M240 258 V290 M300 258 V290 M370 258 V290 "
                          "M220 290 V322 M400 290 V322 M216 322 V354 M404 322 V354 M228 354 V398 M392 354 V398", 1.0), 2.0))
    b.append('<path d="M252 398 V328 A58 58 0 0 1 368 328 V398 Z" stroke-width="2"/>')
    b.append('<path d="M262 392 L358 380 L360 392 L264 400 Z M262 380 L358 392 L356 400 L260 390 Z" stroke-width="1.5"/>')
    b.append('<path d="M286 384 C276 360 292 342 300 324 C304 340 316 346 312 364 C322 356 326 340 324 330 C340 350 342 372 330 386 Z" stroke-width="1.5"/>')
    b.append('<path d="M300 382 C294 368 302 356 306 348 C310 360 318 366 314 380 Z" stroke-width="1.2"/>')
    # mantel shelf + garland
    b.append('<rect x="176" y="246" width="268" height="14" rx="3" stroke-width="2"/>')
    g = "M180 260 " + " ".join(f"Q{x+22} 280 {x+44} 260" for x in range(180, 440, 44))
    b.append(f'<path d="{g}" fill="none" stroke-width="7"/><path d="{g}" fill="none" stroke="#fff" stroke-width="4.4"/>')
    b.append("".join(f'<circle cx="{x+22}" cy="272" r="3.4" stroke-width="1.1"/>' for x in range(180, 440, 44)))
    # keepsakes from the year
    b.append('<path d="M196 246 L204 196 H262 L266 246 Z" stroke-width="1.8"/>')   # Juniper's painting (page 21)
    b.append(clip_d("M208 202 H258 V240 H210 Z",
                    lines("M208 226 C222 220 236 224 258 218", 1.0) + '<circle cx="246" cy="210" r="5" stroke-width="1"/>'
                    + '<path d="M236 240 C232 232 242 228 238 220 L246 220 C248 228 240 232 248 240 Z" stroke-width="0.9"/>'
                    + '<path d="M216 224 L220 208 L224 224 Z" stroke-width="0.9"/>', 1.2))
    b.append('<path d="M282 214 H310 V240 Q310 246 296 246 Q282 246 282 240 Z" stroke-width="1.6"/><rect x="280" y="206" width="32" height="9" rx="2" stroke-width="1.4"/>')
    b.append('<ellipse cx="290" cy="238" rx="5" ry="3.8" stroke-width="1"/><ellipse cx="302" cy="237" rx="5" ry="4" stroke-width="1"/>'
             '<ellipse cx="296" cy="229" rx="5" ry="3.6" stroke-width="1"/><ellipse cx="290" cy="221" rx="4.5" ry="3.4" stroke-width="1"/>')
    b.append('<path d="M356 246 L352 208 L384 204 L388 242 Z" stroke-width="1.6"/>')   # pressed-flower card
    b.append(blossom(370, 222, 10, 1) + lines("M370 228 Q372 236 370 240", 1))
    # the long scarf draped over the mantel end
    sc = "M404 246 Q408 236 420 240 Q430 244 426 300"
    b.append(f'<path d="{sc}" fill="none" stroke-width="15"/><path d="{sc}" fill="none" stroke="#fff" stroke-width="11.6" stroke-linecap="butt"/>'
             f'<path d="{sc}" fill="none" stroke-width="11.6" stroke-linecap="butt" stroke-dasharray="1.3 12"/>')
    b.append('<rect x="419" y="300" width="15" height="9" stroke-width="1.3" transform="rotate(-4 426 304)"/>' + lines("M422 309 V318 M427 309 V319 M432 309 V318", 1.2))
    # Dot on the mantel, wrapped in a tiny quilt square
    b.append(dot(334, 237.5, 0.95))
    b.append('<path d="M326 232 L340 230 L342 244 L328 246 Z" stroke-width="1.2"/><path d="M328.5 234 L338.5 232.6 L340 241.6 L330 243 Z" fill="none" stroke-width="0.7" stroke-dasharray="1.6 1.6"/>')
    # pillows peeking at both ends
    b.append('<path d="M104 420 Q130 402 160 418 Q168 446 156 474 Q128 488 104 474 Q94 446 104 420 Z" stroke-width="1.8"/>' + lines("M110 446 Q130 440 152 446", 1))
    b.append('<path d="M464 418 Q492 404 518 420 Q526 446 516 474 Q490 488 464 474 Q456 446 464 418 Z" stroke-width="1.8"/>' + '<circle cx="490" cy="446" r="6" stroke-width="1.1"/>')

    # ---- the friends, back to front
    b.append(char("br", 310, 442, S, arms=(56, -56), sit=True, mood="happy"))
    b.append(char("ju", 202, 452, S, arms=(14, -40), sit=True))
    jx, jy = paw("ju", 202, 452, S, "R", -40)
    b.append(mug(jx, jy))
    b.append(char("to", 418, 454, S, arms=(40, -14), sit=True, mood="happy"))
    tx, ty = paw("to", 418, 454, S, "L", 40)
    b.append(mug(tx, ty))
    # Thimble on top of the pile, tying the last ribbon
    b.append(char("th", 310, 298, S * 1.2, arms=(-40, 40), sit=True, mood="happy"))
    b.append(lines("M318 300 C344 318 352 360 356 486", 1.6))
    b.append('<path d="M310 290 L298 282 L298 296 Z M310 290 L322 282 L322 296 Z" stroke-width="1.2"/><circle cx="310" cy="290" r="2.6" stroke-width="1.1"/>')
    b.append(char("cl", 162, 500, S, arms=(14, -14), sit=True, mood="happy"))
    b.append(char("mi", 260, 506, S, arms=(14, -14), sit=True))
    b.append(char("pi", 362, 506, S, arms=(14, -40), sit=True, mood="happy"))
    px_, py_ = paw("pi", 362, 506, S, "R", -40)
    b.append(mug(px_ + 2, py_))

    # ---- the finished friendship quilt
    qd = ("M100 640 L104 470 Q112 452 128 462 Q150 486 176 490 Q244 484 310 490 Q376 484 444 490 "
          "Q470 486 492 462 Q508 452 516 470 L520 640 Z")
    cols = [148, 202, 256, 310, 364, 418, 472]
    patch = lines(" ".join(f"M{x} 470 V552" for x in cols) + " M60 496 H560 M60 552 H560 "
                  + " ".join(f"M{x} 552 V640" for x in (202, 256, 364, 418)) + " M60 610 H560", 1.6)
    stitch = (f'<path d="M60 501 H560 M60 547 H560 M60 557 H560 M60 605 H560 '
              + " ".join(f"M{x-5} 470 V640 M{x+5} 470 V640" for x in cols) + '" stroke-width="0.8" stroke-dasharray="3 3"/>')
    syms = [("acorn", 175), ("clover", 229), ("fish", 283), ("star", 337), ("pompom", 391), ("moon", 445)]
    sy = "".join(f'<use href="#sym-{n}" transform="translate({x} 524) scale(0.95)" stroke-width="1.5"/>' for n, x in syms)
    sy += '<use href="#sym-pebble" transform="translate(229 581) scale(0.95)" stroke-width="1.5"/>'
    sy += '<use href="#sym-needle" transform="translate(391 581) scale(0.9)" stroke-width="1.5"/>'
    b.append(clip_d(qd, patch + stitch + sy, 2.2))
    b.append(f'<path d="M104 478 Q112 462 128 472 Q150 496 176 500 Q244 494 310 500 Q376 494 444 500 Q470 496 492 472 Q508 462 516 478" '
             f'fill="none" stroke-width="0.8" stroke-dasharray="3 3"/>')
    # Pebble on the quilt in front, holding her lucky pebble
    b.append(char("pb", 310, 622, S * 1.05, arms=(-30, 30), sit=True, mood="happy"))
    return "".join(b)


def mug(x, y):
    return (f'<path d="M{x-9:.1f} {y-13:.1f} H{x+9:.1f} V{y+3:.1f} Q{x+9:.1f} {y+8:.1f} {x:.1f} {y+8:.1f} Q{x-9:.1f} {y+8:.1f} {x-9:.1f} {y+3:.1f} Z" stroke-width="1.5"/>'
            f'<path d="M{x+9:.1f} {y-9:.1f} q7 0 7 6 q0 6 -7 6" fill="none" stroke-width="1.5"/>'
            f'<path d="M{x-7:.1f} {y-13:.1f} Q{x-4:.1f} {y-19:.1f} {x:.1f} {y-14:.1f} Q{x+4:.1f} {y-19:.1f} {x+7:.1f} {y-13:.1f} Z" stroke-width="1.1"/>')


def build():
    b = []
    # starry winter night around the wreath
    for (x, y, k, s) in ((80, 80, 5, 1.0), (150, 60, 4, 0.8), (240, 92, 5, 0.7), (380, 92, 4, 0.8), (470, 62, 5, 0.9), (540, 104, 4, 1.0),
                         (76, 160, 4, 0.7), (548, 180, 5, 0.7), (72, 690, 5, 1.0), (140, 728, 4, 0.8), (230, 712, 5, 0.7),
                         (390, 716, 4, 0.8), (480, 734, 5, 0.9), (548, 680, 4, 1.0), (70, 610, 4, 0.7), (552, 610, 5, 0.7)):
        if k == 5:
            b.append(f'<use href="#star5" transform="translate({x} {y}) scale({s*1.5})" stroke-width="{1.3/(s*1.5):.2f}"/>')
        else:
            b.append(f'<use href="#star4" transform="translate({x} {y}) scale({s*1.5})" stroke-width="{1.3/(s*1.5):.2f}"/>')
    for (x, y) in ((110, 120), (500, 140), (300, 64), (96, 650), (520, 700), (310, 736)):
        b.append(f'<use href="#flake" transform="translate({x} {y}) scale(1.3)" stroke-width="1.1"/>')
    # the room, clipped to the wreath's inner circle
    k = uid("r")
    b.append(f'<clipPath id="{k}"><circle cx="{CX}" cy="{CY}" r="{RI}"/></clipPath>')
    b.append(f'<circle cx="{CX}" cy="{CY}" r="{RI}" stroke-width="1.5"/>')
    b.append(f'<g clip-path="url(#{k})">{room()}</g>')
    b.append(wreath())
    return "".join(b)


def svg():
    return page(build(), TITLE)
