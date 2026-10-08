"""Page 15 — Noses to the Glass (rain outside Bramble's round kitchen window)."""
from math import sin, cos, radians
from chars import char, dot, page
from scene import clip_d, daisy, lines, uid

TITLE = "Page 15 — Noses to the Glass"
WX, WY = 300, 286


def drop(x, y, s=1.0, sw=1.2):
    return (f'<path transform="translate({x:.1f} {y:.1f}) scale({s})" d="M0 -8 Q5.5 1 0 5 Q-5.5 1 0 -8 Z" '
            f'stroke-width="{sw}"/>')


def ring_seg(cx, cy, r1, r2, a0, a1):
    def p(r, a):
        return cx + r * sin(radians(a)), cy - r * cos(radians(a))
    x0, y0 = p(r2, a0); x1, y1 = p(r2, a1); x2, y2 = p(r1, a1); x3, y3 = p(r1, a0)
    return (f'<path d="M{x0:.1f} {y0:.1f} A{r2} {r2} 0 0 1 {x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} '
            f'A{r1} {r1} 0 0 0 {x3:.1f} {y3:.1f} Z" stroke-width="1.5"/>')


def build():
    b = []
    # plaster wall with a few stones
    for (x, y, w, h) in ((70, 520, 46, 26), (476, 470, 50, 24), (96, 110, 40, 22), (500, 120, 44, 24), (60, 300, 30, 40)):
        b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" stroke-width="1.2"/>')
    # roof eave with scalloped shingles and a gutter
    b.append('<rect x="30" y="20" width="560" height="44" stroke-width="1.6"/>')
    b.append("".join(f'<path d="M{x} 64 a14 14 0 0 0 28 0" stroke-width="1.3"/>' for x in range(34, 590, 28)))
    b.append(lines("M30 44 H590", 1.1))
    b.append('<rect x="30" y="76" width="560" height="14" rx="7" stroke-width="1.8"/>')
    # drainpipe down the right wall
    b.append('<path d="M548 90 H562 V532 Q562 556 540 556 H520 V542 H540 Q548 542 548 532 Z" stroke-width="1.8"/>')
    b.append('<rect x="544" y="200" width="22" height="8" rx="2" stroke-width="1.2"/><rect x="544" y="400" width="22" height="8" rx="2" stroke-width="1.2"/>')
    # ivy climbing the left wall (behind the shutter)
    b.append(lines("M64 650 C58 560 92 500 76 430 C62 370 96 300 86 220 C82 180 96 140 120 110", 1.6))
    for (x, y, r) in ((60, 600, -30), (80, 560, 40), (70, 512, -40), (86, 470, 30), (68, 420, -30),
                      (88, 380, 40), (76, 330, -35), (94, 280, 35), (82, 236, -30), (92, 190, 30), (104, 146, -20), (122, 114, 20)):
        b.append(f'<use href="#heart" transform="translate({x} {y}) rotate({r + 180}) scale(1.35)" stroke-width="1.1"/>')

    # stone ring around the window
    for k in range(18):
        b.append(ring_seg(WX, WY, 150, 178, k * 20, (k + 1) * 20))
    # open shutters with hearts
    b.append(clip_d(f"M122 {WY-122} A66 122 0 0 0 122 {WY+122} Z", lines("M100 140 V440", 1.1), 1.9))
    b.append(clip_d(f"M478 {WY-122} A66 122 0 0 1 478 {WY+122} Z", lines("M500 140 V440", 1.1), 1.9))
    b.append(f'<use href="#heart" transform="translate(84 {WY-36}) scale(1.4)" stroke-width="1.4"/>')
    b.append(f'<use href="#heart" transform="translate(516 {WY-36}) scale(1.4)" stroke-width="1.4"/>')
    b.append(f'<use href="#heart" transform="translate(84 {WY+40}) scale(1.4)" stroke-width="1.4"/>')
    b.append(f'<use href="#heart" transform="translate(516 {WY+40}) scale(1.4)" stroke-width="1.4"/>')
    # window: frame ring, glass, friends inside
    b.append(f'<circle cx="{WX}" cy="{WY}" r="150" stroke-width="2.2"/>')
    k = uid("g")
    b.append(f'<clipPath id="{k}"><circle cx="{WX}" cy="{WY}" r="131"/></clipPath>')
    inside = []
    inside.append(f'<circle cx="{WX}" cy="{WY}" r="131" stroke-width="1.4"/>')
    # warm kitchen behind: hanging lamp
    inside.append(lines(f"M{WX} 150 V184", 1.2))
    inside.append(f'<path d="M{WX-24} 208 Q{WX-22} 184 {WX} 184 Q{WX+22} 184 {WX+24} 208 Z" stroke-width="1.6"/>')
    inside.append(f'<ellipse cx="{WX}" cy="212" rx="7" ry="5" stroke-width="1.2"/>')
    inside.append(char("mi", 234, 432, 1.8, arms=(150, -150), head_rot=4))
    inside.append(char("pi", 368, 450, 1.8, arms=(150, -150), head_rot=-4))
    # raindrops running down the glass
    for (x, y, s) in ((300, 262, 1.1), (290, 316, 0.9), (306, 360, 1.0), (300, 404, 1.2), (190, 226, 0.9),
                      (420, 236, 0.9), (196, 396, 1.0), (420, 392, 1.0), (262, 196, 0.8), (344, 198, 0.8)):
        inside.append(drop(x, y, s, 1.1))
    inside.append(lines(f"M{WX+92} {WY-80} A120 120 0 0 1 {WX+118} {WY-26} M{WX+84} {WY-96} A126 126 0 0 1 {WX+90} {WY-90}", 1.4))
    b.append(f'<g clip-path="url(#{k})">' + "".join(inside) + "</g>")
    b.append(f'<path fill-rule="evenodd" d="M{WX-150} {WY} a150 150 0 1 0 300 0 a150 150 0 1 0 -300 0 Z '
             f'M{WX-131} {WY} a131 131 0 1 0 262 0 a131 131 0 1 0 -262 0 Z" stroke-width="2.2"/>')
    # stone sill with the snail
    b.append('<rect x="128" y="444" width="344" height="20" rx="5" stroke-width="2"/>')
    b.append('<path d="M186 444 Q184 436 194 435 L226 437 Q236 440 234 444 Z" stroke-width="1.5"/>')
    b.append(lines("M193 436 L188 423 M198 435 L197 421", 1.2))
    b.append('<circle cx="188" cy="422" r="2" fill="#000" stroke="none"/><circle cx="197" cy="420" r="2" fill="#000" stroke="none"/>')
    b.append('<circle cx="216" cy="426" r="13" stroke-width="1.6"/>' + lines("M216 426 m3 0 a3 3 0 1 1 -6 0 a6 6 0 1 1 12 0 a9 9 0 1 1 -18 0", 1.1))

    # window box on brackets, daisies bowed by rain
    for (x, lean) in ((206, -16), (250, -24), (300, 10), (350, 24), (396, 16)):
        b.append(lines(f"M{x} 494 Q{x} 468 {x + lean} 478", 1.2))
        b.append(f'<path d="M{x} 494 Q{x-12} 482 {x-14} 470 Q{x-2} 478 {x} 494 Z" stroke-width="1"/>')
        b.append(f'<g transform="translate({x + lean} 480) rotate({lean*1.6}) scale(1 0.72)">' + daisy(0, 0, 17, 8, 1.3) + '</g>')
    b.append('<path d="M176 492 H424 L418 536 H182 Z" stroke-width="2"/>')
    b.append(lines("M180 504 H420", 1.1))
    b.append("".join(f'<use href="#heart" transform="translate({x} 522) scale(0.8)" stroke-width="1.5"/>' for x in (240, 300, 360)))
    b.append('<path d="M196 536 H228 Q228 566 202 570 H196 Z M372 536 H404 V570 H398 Q372 566 372 536 Z" stroke-width="1.6"/>')
    # stone string course under the box, where Dot keeps dry
    b.append('<rect x="110" y="578" width="380" height="16" rx="4" stroke-width="1.8"/>')
    b.append(lines("M180 578 V594 M260 578 V594 M340 578 V594 M420 578 V594", 1.0))
    b.append(dot(300, 568.5))

    # rain barrel with the spout pouring in
    b.append('<path d="M520 548 Q512 560 512 590 L522 590 Q522 566 528 556 Z" stroke-width="1.3"/>')
    b.append('<path d="M462 596 Q458 650 466 704 H550 Q558 650 554 596 Z" stroke-width="2"/>')
    b.append(lines("M460 624 Q508 632 556 624 M462 682 Q508 690 554 682", 1.3))
    b.append(lines("M478 600 Q476 650 480 700 M500 602 V704 M520 602 V704 M540 600 Q542 650 538 700", 0.9))
    b.append('<ellipse cx="508" cy="596" rx="46" ry="10" stroke-width="2"/>')
    b.append('<path d="M500 594 Q506 580 512 594 Q518 584 524 594 Z" stroke-width="1.2"/>')
    b.append(drop(492, 578, 0.8) + drop(532, 574, 0.8))

    # ground, cobbles and puddles
    b.append('<path d="M30 650 H600 V800 H30 Z" stroke-width="1.8"/>')
    cob = ""
    for r, y in enumerate((650, 676, 704, 734)):
        off = 0 if r % 2 == 0 else 26
        for x in range(30 + off - 52, 600, 52):
            cob += f'<rect x="{x+2}" y="{y+2}" width="48" height="{24 + (r == 3)*8}" rx="10" stroke-width="1.1"/>'
    b.append(clip_d("M30 650 H600 V800 H30 Z", cob, 1.8))
    for (x, y, rx, ry) in ((160, 714, 74, 16), (340, 738, 82, 15)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" stroke-width="1.6"/>')
        b.append(f'<ellipse cx="{x+8}" cy="{y}" rx="{rx*0.55:.0f}" ry="{ry*0.5:.0f}" stroke-width="1.1"/>')
        b.append(f'<ellipse cx="{x+12}" cy="{y}" rx="{rx*0.22:.0f}" ry="{ry*0.22:.0f}" stroke-width="1"/>')

    # falling rain, evenly spaced, kept off the window and the friends
    for row in range(14):
        y = 112 + row * 46
        for col in range(12):
            x = 64 + col * 46 + (23 if row % 2 else 0)
            dx, dy = x - WX, y - WY
            if dx * dx + dy * dy < 190 * 190:
                continue
            if 170 < x < 440 and 440 < y < 600:
                continue
            if 450 < x < 566 and 540 < y < 712:
                continue
            if x > 540 and y < 560:
                continue
            if y > 650:
                continue
            b.append(drop(x, y, 1.15))
    return "".join(b)


def svg():
    return page(build(), TITLE)
