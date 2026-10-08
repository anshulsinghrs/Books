"""Page 32 — Into Fernwood (worm's-eye view under giant mushrooms)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, fern
from props import lantern_hanging, snail

TITLE = "Page 32 — Into Fernwood"


def giant_mushroom(cx, cap_y, rx, ry, stem_w, stem_bottom, spots):
    out = (f'<path d="M{cx - stem_w/2} {stem_bottom} Q{cx - stem_w*0.6:.0f} {cap_y + ry*0.5:.0f} {cx - stem_w*0.4:.0f} {cap_y + 4} '
           f'H{cx + stem_w*0.4:.0f} Q{cx + stem_w*0.6:.0f} {cap_y + ry*0.5:.0f} {cx + stem_w/2} {stem_bottom} Z" stroke-width="2"/>')
    out += lines(f"M{cx - stem_w*0.5:.0f} {cap_y + ry*0.9:.0f} Q{cx} {cap_y + ry*1.1:.0f} {cx + stem_w*0.5:.0f} {cap_y + ry*0.9:.0f}", 1.3)
    under = f"M{cx - rx} {cap_y} Q{cx} {cap_y + ry*0.7:.0f} {cx + rx} {cap_y} Z"
    out += clip_d(under, lines(" ".join(f"M{cx} {cap_y + ry*0.6:.0f} L{cx - rx + k*2*rx/14:.0f} {cap_y - 2}" for k in range(15)), 0.9), 1.6)
    cap = f"M{cx - rx} {cap_y} Q{cx - rx} {cap_y - ry} {cx} {cap_y - ry} Q{cx + rx} {cap_y - ry} {cx + rx} {cap_y} Q{cx} {cap_y + ry*0.25:.0f} {cx - rx} {cap_y} Z"
    out += clip_d(cap, "".join(f'<ellipse cx="{cx + dx*rx:.0f}" cy="{cap_y - dy*ry:.0f}" rx="{r*rx:.0f}" ry="{r*rx*0.7:.0f}" stroke-width="1.3"/>' for dx, dy, r in spots), 2.2)
    return out


def build():
    b = []
    # towering giant mushrooms overhead
    b.append(giant_mushroom(150, 180, 150, 140, 70, 560, ((-0.5, 0.5, 0.12), (0.1, 0.7, 0.1), (0.55, 0.4, 0.1), (-0.1, 0.3, 0.08))))
    b.append(giant_mushroom(470, 140, 170, 120, 76, 560, ((-0.45, 0.45, 0.1), (0.15, 0.65, 0.12), (0.6, 0.3, 0.08), (-0.05, 0.25, 0.07))))
    b.append(dot(212, 232, 0.95))  # Dot under a mushroom cap
    # ground: stream with footbridge and stepping stones, mossy log
    b.append('<path d="M30 520 C200 500 400 512 600 500 V800 H30 Z" stroke-width="1.6"/>')
    stream = "M30 640 C140 620 220 660 330 640 C430 622 520 650 600 636 V700 C520 714 430 690 330 708 C220 726 140 690 30 708 Z"
    b.append(clip_d(stream, lines("M60 664 q14 -6 28 0 M180 676 q14 -6 28 0 M380 668 q14 -6 28 0 M500 676 q14 -6 28 0", 1.1), 1.8))
    for (x, y) in ((80, 672), (140, 680)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="22" ry="10" stroke-width="1.7"/>')
    b.append('<path d="M380 620 Q450 590 540 620 L540 634 Q450 606 380 634 Z" stroke-width="1.9"/>'
             + lines(" ".join(f"M{x} {612 - (x - 380)*0.2 if x < 460 else 596 + (x - 460)*0.3:.0f} V{630 - (x - 380)*0.2 if x < 460 else 614 + (x - 460)*0.3:.0f}" for x in range(394, 540, 18)), 1)
             + '<path d="M384 620 V660 M536 620 V660" stroke-width="3"/>')
    b.append('<path d="M30 560 H260 Q280 560 280 580 Q280 600 260 600 H30 Z" stroke-width="2"/><ellipse cx="260" cy="580" rx="14" ry="20" stroke-width="1.8"/>'
             '<ellipse cx="260" cy="580" rx="7" ry="10" stroke-width="1"/>'
             + lines(" ".join(f"M{x} 560 q8 -8 16 0" for x in range(40, 250, 16)), 1.1))
    # ferns and small mushroom clusters, a snail
    b.append(fern(50, 520, 110, 20, 14, 7, 12) + fern(560, 520, 110, -20, -14, 7, 12) + fern(590, 800, 120, -30, -16, 7, 13) + fern(30, 800, 120, 30, 16, 7, 13))
    for (x, y, s) in ((300, 760, 1.0), (330, 766, 0.7), (520, 750, 0.8)):
        b.append(f'<path transform="translate({x} {y}) scale({s})" d="M-6 0 Q-7 -12 -5 -18 H5 Q7 -12 6 0 Z" stroke-width="{1.4/s:.2f}"/>'
                 f'<path transform="translate({x} {y}) scale({s})" d="M-17 -16 Q-16 -34 0 -35 Q16 -34 17 -16 Q0 -12 -17 -16 Z" stroke-width="{1.4/s:.2f}"/>')
    b.append(snail(440, 760, 1.0))
    # Miso with the magnifying glass at the left mushroom
    mx, my, ms = 220, 600, 1.3
    b.append(char("mi", mx, my, ms, arms=(None, 20), head_rot=-8))
    gx, gy = paw("mi", mx, my, ms, "L", 130)
    b.append(f'<path d="M{gx:.1f} {gy:.1f} L{gx - 24:.1f} {gy - 22:.1f}" stroke-width="5"/><path d="M{gx:.1f} {gy:.1f} L{gx - 24:.1f} {gy - 22:.1f}" stroke="#fff" stroke-width="2"/>'
             f'<circle cx="{gx - 36:.1f}" cy="{gy - 34:.1f}" r="18" stroke-width="2.4"/><circle cx="{gx - 36:.1f}" cy="{gy - 34:.1f}" r="13" stroke-width="1"/>'
             + lines(f"M{gx - 44:.1f} {gy - 42:.1f} q4 -4 8 -2", 1))
    b.append(arms_only("mi", mx, my, ms, (130, None)))
    # Juniper pointing ahead with the lantern, Thimble riding on his shoulder
    jx, jy, js = 400, 610, 1.3
    b.append(char("ju", jx, jy, js, arms=(14, -110), brows=True))
    lx, ly = paw("ju", jx, jy, js, "L", 14)
    b.append(lantern_hanging(lx, ly, 0.9, 10))
    b.append(char("th", jx - 30 * js, jy - 76 * js, 1.25, arms=(30, -120), sit=True, mood="happy"))
    return "".join(b)


def svg():
    return page(build(), TITLE)
