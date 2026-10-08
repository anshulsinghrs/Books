"""Page 35 — Cookie Cutter Morning (Clover's kitchen table by the open window)."""
from math import sin, cos, radians, pi
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, scallop_blob, uid

TITLE = "Page 35 — Cookie Cutter Morning"


def star_pts(cx, cy, r1, r2, n=5, sy=1.0, rot=-90):
    pts = []
    for k in range(2 * n):
        r = r1 if k % 2 == 0 else r2
        a = radians(rot + 180 * k / n)
        pts.append((cx + r * cos(a), cy + r * sin(a) * sy))
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"


SHAPES = {
    "heart": "M0 9 C-12 0 -15 -9 -8 -13 C-4 -15 0 -12 0 -9 C0 -12 4 -15 8 -13 C15 -9 12 0 0 9 Z",
    "star": star_pts(0, 0, 14, 6.5),
    "flower": ("M0 -14 C6 -14 7 -7 4 -5 C9 -9 15 -4 11 1 C15 6 9 12 4 7 C6 12 2 15 0 15 "
               "C-2 15 -6 12 -4 7 C-9 12 -15 6 -11 1 C-15 -4 -9 -9 -4 -5 C-7 -7 -6 -14 0 -14 Z"),
    "leaf": "M0 14 C-12 4 -12 -8 0 -15 C12 -8 12 4 0 14 Z",
    "acorn": "M-9 -3 Q-9 12 0 15 Q9 12 9 -3 Q11 -5 10 -7 Q0 -15 -10 -7 Q-11 -5 -9 -3 Z",
    "bunny": ("M-9 14 Q-14 2 -7 -3 Q-11 -16 -7 -17 Q-3 -16 -3 -5 L3 -5 Q3 -16 7 -17 Q11 -16 7 -3 "
              "Q14 2 9 14 Z"),
    "round": "M-12 0 A12 12 0 1 0 12 0 A12 12 0 1 0 -12 0 Z",
}


def shape(name, x, y, s=1.0, sw=1.4, rot=0, sy=1.0):
    return (f'<path transform="translate({x} {y}) rotate({rot}) scale({s} {s*sy})" d="{SHAPES[name]}" '
            f'stroke-width="{sw/s:.2f}"/>')


def icing(name, x, y, s=1.0, rot=0):
    """Decorated baked cookie: shape + icing detail."""
    out = shape(name, x, y, s, 1.5, rot)
    k = f'translate({x} {y}) rotate({rot}) scale({s})'
    det = {
        "heart": '<circle cx="-5" cy="-6" r="1.8"/><circle cx="5" cy="-6" r="1.8"/><circle cx="0" cy="1" r="1.8"/>',
        "star": '<path d="M-6 -2 L-3 2 L0 -2 L3 2 L6 -2" fill="none"/>',
        "flower": '<circle r="4.5"/>',
        "round": '<path d="M0 0 m3 0 a3 3 0 1 1 -6 0 a6 6 0 1 1 12 0" fill="none"/>',
        "leaf": '<path d="M0 10 V-10" fill="none"/>',
        "acorn": '<path d="M-9 -3 Q0 1 9 -3" fill="none"/>',
        "bunny": '<circle cx="0" cy="6" r="3"/>',
    }[name]
    return out + f'<g transform="{k}" stroke-width="{1.0/s:.2f}">{det}</g>'


def cutter(name, x, y, s=1.0, rot=0):
    """Metal cutter seen from above: double outline (rim)."""
    return (shape(name, x, y, s * 1.12, 1.7, rot) + shape(name, x, y, s * 0.92, 1.1, rot))


def build():
    b = []
    # ---- wall: open window with a summer view and breezy eyelet curtains
    b.append('<rect x="186" y="74" width="240" height="214" rx="6" stroke-width="2"/>')
    view = ('<circle cx="380" cy="122" r="20" stroke-width="1.5"/>'
            + lines("M380 90 V96 M380 148 V154 M348 122 H354 M406 122 H412 M357 99 l4 4 M399 141 l4 4 M403 99 l-4 4 M361 141 l-4 4", 1.2)
            + '<use href="#cloud" transform="translate(262 112) scale(0.7)" stroke-width="2"/>'
            + '<path d="M190 236 C240 220 300 230 422 214 V288 H190 Z" stroke-width="1.4"/>'
            + '<rect x="282" y="186" width="10" height="44" stroke-width="1.3"/>' + scallop_blob(287, 176, 30, 24, 8, 0.3, 1.5)
            + "".join(f'<path d="M{x} 262 V244 L{x+5} 238 L{x+10} 244 V262 Z" stroke-width="1.2"/>' for x in range(196, 420, 18))
            + lines("M190 250 H422", 1.1))
    b.append(clip_d("M194 82 H418 V280 H194 Z", view, 1.6, fill="#fff"))
    b.append(lines("M306 82 V280 M194 180 H418", 2.2))
    b.append('<rect x="176" y="286" width="260" height="14" rx="3" stroke-width="1.8"/>')
    b.append('<rect x="150" y="56" width="312" height="8" rx="4" stroke-width="1.6"/><circle cx="150" cy="60" r="7" stroke-width="1.5"/><circle cx="462" cy="60" r="7" stroke-width="1.5"/>')
    eyelets = "".join(f'<circle cx="{x}" cy="{y}" r="2.6"/>' for y in range(84, 300, 26) for x in range(120, 520, 22))
    lc = "M164 62 C176 120 186 170 214 220 C232 252 262 268 290 262 C262 286 214 300 190 304 C160 240 150 150 152 62 Z"
    rc = "M448 62 C440 120 432 170 404 222 C388 250 360 262 334 258 C362 282 404 296 428 302 C454 240 462 150 460 62 Z"
    b.append(clip_d(lc, eyelets.replace("<circle", '<circle stroke-width="0.9"'), 1.8))
    b.append(clip_d(rc, eyelets.replace("<circle", '<circle stroke-width="0.9"'), 1.8))
    # utensil rail and a shelf of mixing bowls
    b.append('<rect x="56" y="150" width="96" height="7" rx="3.5" stroke-width="1.5"/>')
    b.append(lines("M76 157 V178 M104 157 V176 M132 157 V178", 1.1))
    b.append('<path d="M70 178 Q76 174 82 178 L80 244 Q76 250 72 244 Z" stroke-width="1.4"/><ellipse cx="76" cy="186" rx="9" ry="12" stroke-width="1.4"/>')
    b.append('<path d="M98 176 H110 L108 228 H100 Z" stroke-width="1.4"/><path d="M96 228 H112 Q112 262 104 266 Q96 262 96 228 Z" stroke-width="1.4"/>')
    b.append('<path d="M126 178 Q132 174 138 178 L136 214 H128 Z" stroke-width="1.4"/>'
             '<path d="M124 214 Q132 274 140 214 Z" stroke-width="1.4"/>' + lines("M127 224 Q132 262 137 224 M132 214 V262", 0.8))
    b.append('<rect x="470" y="200" width="100" height="8" rx="2" stroke-width="1.6"/>')
    b.append('<path d="M478 200 L486 220 L478 224 Z M560 200 L552 220 L560 224 Z" stroke-width="1.3"/>')
    b.append('<path d="M480 200 Q480 178 500 176 H540 Q560 178 560 200 Z" stroke-width="1.6"/>')
    b.append('<path d="M488 176 Q490 160 506 158 H534 Q550 160 552 176 Z" stroke-width="1.5"/>')
    b.append(lines("M484 188 H556", 0.9))

    # ---- tiled backsplash behind the table
    tiles = ""
    for r, y in enumerate(range(416, 520, 34)):
        for c, x in enumerate(range(40, 600, 34)):
            if (r * 3 + c) % 3 == 0:
                tiles += f'<g transform="translate({x+17} {y+17})" stroke-width="0.9"><circle cy="-6" r="4"/><circle cx="6" r="4"/><circle cy="6" r="4"/><circle cx="-6" r="4"/><circle r="2.6"/></g>'
    tiles += lines(" ".join(f"M30 {y} H600" for y in range(450, 520, 34)) + " " + " ".join(f"M{x} 416 V520" for x in range(74, 600, 34)), 1.0)
    b.append(clip_d("M30 416 H600 V520 H30 Z", tiles, 1.6))
    # ---- friends behind the table: Clover (tall), Pip (middle), Thimble (on the table)
    b.append(char("cl", 196, 578, 1.4, arms=(None, None), head_rot=-4))
    b.append(char("pi", 420, 566, 1.4, arms=(None, None), mood="happy", head_rot=6))
    # chair back behind Pip (he kneels on the chair)

    # ---- table top, wood grain
    top = "M50 520 H562 L620 744 H-10 Z"
    b.append(clip_d(top, lines("M60 560 Q120 556 160 562 M470 690 Q520 686 600 692 M30 700 Q70 696 110 702", 1.0), 2.0))
    b.append('<path d="M-10 744 H620 V770 H-10 Z" stroke-width="2"/>')
    # dough sheet with cut-out holes and Clover's heart cutter
    dough = "M150 546 C200 536 300 538 446 546 C462 576 456 616 440 644 C340 654 230 656 140 644 C124 612 132 574 150 546 Z"
    holes = (shape("round", 380, 568, 0.9, 1.3, sy=0.6) + shape("flower", 414, 620, 0.9, 1.3, sy=0.6)
             + shape("leaf", 236, 630, 0.9, 1.3, 70, 0.65) + shape("heart", 172, 620, 0.85, 1.3, sy=0.6))
    b.append(clip_d(dough, holes, 2.0))
    b.append(cutter("heart", 196, 556, 1.1))
    b.append(arms_only("cl", 196, 578, 1.4, (-12, 12)))
    # Pip's nibble: a pinched corner of dough in his paw
    nx, ny = paw("pi", 420, 566, 1.4, "L", -150)
    b.append(f'<path d="M{nx-8:.1f} {ny-2:.1f} Q{nx-4:.1f} {ny-12:.1f} {nx+6:.1f} {ny-8:.1f} Q{nx+10:.1f} {ny:.1f} {nx+2:.1f} {ny+4:.1f} Q{nx-8:.1f} {ny+4:.1f} {nx-8:.1f} {ny-2:.1f} Z" stroke-width="1.4"/>')
    b.append(f'<g transform="translate(420 566) scale(1.4)" stroke-width="1.43"><use href="#pi-arm" transform="translate(-20 -42) rotate(-150)"/><use href="#pi-arm" transform="translate(20 -42) rotate(-20)"/></g>')
    # Thimble standing inside the star cutter on the dough
    sp_back = star_pts(300, 614, 44, 20, sy=0.42)
    b.append(f'<path d="{sp_back}" stroke-width="1.8"/>')
    b.append(f'<path d="{star_pts(300, 614, 38, 17, sy=0.42)}" stroke-width="1.1"/>')
    b.append(char("th", 300, 618, 1.3, arms=(150, -150), mood="happy"))
    # front lip of the cutter over Thimble's feet
    k = uid("f")
    b.append(f'<clipPath id="{k}"><rect x="200" y="618" width="200" height="40"/></clipPath>'
             f'<g clip-path="url(#{k})"><path d="{sp_back}" fill="none" stroke-width="1.8"/></g>')

    # ---- sprinkles jars, rolling pin and loose cutters
    for (x, icon) in ((74, "heart"), (108, "star")):
        b.append(f'<path d="M{x-14} 506 H{x+14} V532 Q{x+14} 540 {x} 540 Q{x-14} 540 {x-14} 532 Z" stroke-width="1.6"/>')
        b.append(f'<rect x="{x-15}" y="496" width="30" height="11" rx="3" stroke-width="1.5"/>')
        b.append(shape(icon, x, 522, 0.45, 1.2))
        b.append("".join(f'<rect x="{x - 12 + 6*j}" y="{490 - 3*(j % 2)}" width="3" height="4" rx="1" stroke-width="0.8"/>' for j in range(5)) if x == 70 else "")
    b.append('<path d="M40 676 L118 650 L124 666 L46 692 Z" stroke-width="1.8"/>')
    b.append('<path d="M30 690 L44 684 L50 700 L36 706 Z M120 652 L134 646 L140 662 L126 668 Z" stroke-width="1.6"/>')
    b.append(cutter("bunny", 70, 600, 1.1, -8) + cutter("acorn", 84, 728, 0.95, 10))
    b.append(cutter("leaf", 500, 712, 1.0, 30) + cutter("flower", 554, 724, 0.95))
    # recipe card with picture icons only
    b.append('<path d="M490 470 L554 464 L560 522 L496 528 Z" stroke-width="1.6"/>')
    b.append('<ellipse cx="508" cy="486" rx="6" ry="8" stroke-width="1.1"/>' + shape("heart", 528, 486, 0.4, 1.1)
             + shape("star", 545, 484, 0.4, 1.1) + lines("M504 504 H548 M506 514 H536", 1))

    # ---- cooling rack of decorated cookies (Dot perches on it)
    rack = "M456 588 H566 L586 672 H448 Z"
    b.append(clip_d(rack, lines("M440 608 H590 M440 630 H590 M440 652 H590 M478 580 L476 680 M504 580 L506 680 M530 580 L536 680 M554 580 L564 680", 1.0), 2.0))
    b.append('<path d="M454 672 V682 M582 672 V682" stroke-width="2"/>')
    b.append(icing("heart", 484, 614, 1.0) + icing("star", 536, 610, 1.0, 10) + icing("flower", 498, 654, 0.95) + icing("round", 556, 652, 1.0))
    b.append(dot(468, 579))

    # ---- baking tray of unbaked cookies in the foreground
    tray = "M150 670 H438 L456 740 H128 Z"
    b.append(f'<path d="M142 664 H446 L466 748 H118 Z" stroke-width="2"/>')
    b.append(f'<path d="{tray}" stroke-width="1.4"/>')
    for (n, x, y, s, r) in (("star", 190, 688, 1.0, 0), ("heart", 252, 688, 1.0, 0), ("bunny", 316, 688, 0.95, 0),
                            ("leaf", 384, 688, 1.0, 40), ("acorn", 180, 722, 1.0, 0), ("flower", 248, 722, 1.0, 0),
                            ("round", 318, 722, 0.95, 0), ("heart", 392, 722, 1.0, 10)):
        b.append(shape(n, x, y, s, 1.6, r))
    return "".join(b)


def svg():
    return page(build(), TITLE)
