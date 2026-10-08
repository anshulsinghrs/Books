"""Page 17 — Cocoa Pour (still-life close-up; Bramble's arm, Pip peeking)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, scallop_blob
from props import mug, bowl, jar, drop, window_rect

TITLE = "Page 17 — Cocoa Pour"


def cream(x, y, s=1.0):
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({s})" stroke-width="{1.4/s:.2f}">'
            '<path d="M-20 0 Q-24 -10 -12 -12 Q-14 -22 -2 -22 Q0 -32 8 -28 Q16 -28 12 -18 Q24 -18 20 -6 Q24 0 20 2 Q0 6 -20 0 Z"/>'
            '<path d="M-12 -10 Q0 -14 12 -8 M-4 -20 Q4 -22 8 -18" fill="none" stroke-width="0.9"/></g>')


def marshmallows(x, y, s=1.0):
    return "".join(f'<rect x="{x + dx*s - 7*s:.1f}" y="{y + dy*s - 7*s:.1f}" width="{14*s:.1f}" height="{12*s:.1f}" rx="3" stroke-width="1.3" transform="rotate({r} {x + dx*s:.1f} {y + dy*s:.1f})"/>'
                   for dx, dy, r in ((-10, -4, -10), (6, -6, 12), (-1, -14, 4)))


def build():
    b = []
    # rain-streaked window behind, wall
    view = "".join(f'<path d="M{x} {y} q3 18 0 34 q-3 -16 0 -34 Z" stroke-width="1"/>' for x in range(320, 560, 34) for y in (80, 160, 240) )
    b.append(window_rect(300, 60, 250, 240, view + '<path d="M300 250 C360 236 440 248 560 232 V300 H300 Z" stroke-width="1.2"/>', (1, 1), True))
    b.append(lines("M30 400 H600", 1.4))
    # Pip peeking over the back edge of the table, marshmallow mustache
    b.append(char("pi", 512, 560, 1.6, arms=(None, None), head_rot=-10, mood="happy"))
    # table
    b.append(clip_d("M30 470 H600 V800 H30 Z", lines("M30 560 Q200 552 380 562 M30 680 Q260 670 600 684 M200 760 Q300 754 420 760", 1.0), 2))
    b.append(arms_only("pi", 512, 560, 1.6, (-30, 30)))
    hx, hy = 512 + 1.6 * 0, 560 - 1.6 * 80
    b.append(f'<path d="M{hx-26:.0f} {hy + 52:.0f} q6 -8 13 -2 q7 -6 13 0 q7 -6 13 0 q6 -6 13 2 q-26 12 -52 0 Z" stroke-width="1.4"/>')
    # Bramble's arm and paw entering from the upper left with the saucepan
    px, py = paw("br", -40, 330, 2.1, "R", -58)
    b.append(f'<g transform="translate({px:.1f} {py:.1f}) rotate(52) scale(1.6)" stroke-width="1.3">'
             '<rect x="-10" y="-8" width="80" height="16" rx="7"/>'
             '<path d="M64 -30 H160 V30 Q160 46 144 46 H80 Q64 46 64 30 Z"/><path d="M60 -34 H164 V-24 H60 Z"/>'
             '<path d="M160 -26 Q176 -26 178 -14" fill="none" stroke-width="2.4"/></g>')
    b.append(arms_only("br", -40, 330, 2.1, (None, -58)))
    # the pour into the middle mug
    b.append('<path d="M284 400 Q264 470 266 554 L278 554 Q276 474 294 404 Z" stroke-width="1.6"/>')
    # five patterned mugs in a curving row
    for (x, y, pat) in ((92, 690, "hearts"), (186, 640, "stripes"), (272, 616, "stars"), (360, 640, "checks"), (456, 690, "leaves")):
        b.append(mug(x, y, 2.5, pat))
    b.append(cream(92, 624, 1.8) + cream(456, 624, 1.8) + marshmallows(186, 570, 1.5) + marshmallows(360, 570, 1.5))
    b.append('<path d="M258 554 Q272 562 286 554" fill="none" stroke-width="1.1"/>')
    # marshmallow jar (Dot on the lid), cinnamon sticks, cream bowl, cookies, spoon
    b.append(jar(70, 520, 64, 82, None))
    b.append(marshmallows(62, 500, 1.2) + marshmallows(80, 478, 1.1))
    b.append(dot(70, 428))
    b.append(bowl(540, 740, 70, 30, "cream", "stripe"))
    b.append('<ellipse cx="360" cy="734" rx="62" ry="16" stroke-width="1.8"/><ellipse cx="360" cy="734" rx="48" ry="11" stroke-width="1"/>')
    for (x, y) in ((336, 724), (368, 720), (390, 730), (350, 738)):
        b.append(f'<circle cx="{x}" cy="{y}" r="13" stroke-width="1.5"/><circle cx="{x - 4}" cy="{y - 3}" r="1.6" fill="#000" stroke="none"/><circle cx="{x + 4}" cy="{y + 3}" r="1.6" fill="#000" stroke="none"/>')
    b.append(''.join(f'<rect x="{150 + k*4}" y="{714 - k*9}" width="70" height="10" rx="5" stroke-width="1.5" transform="rotate(-8 185 710)"/>' for k in range(3)))
    b.append(lines("M156 712 a5 5 0 0 1 0 10 M158 704 a4 4 0 0 1 0 8", 0.9))
    b.append('<path d="M40 750 L190 736 L190 744 L40 758 Z" stroke-width="1.5"/><ellipse cx="206" cy="738" rx="20" ry="11" transform="rotate(-6 206 738)" stroke-width="1.7"/>')
    return "".join(b)


def svg():
    return page(build(), TITLE)
