"""Page 19 — Game Afternoon (board game around the coffee table)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import cushion, bowl, icon, rug_round

TITLE = "Page 19 — Game Afternoon"


def die(x, y, s=1.0, pips=(5, 3)):
    d = {1: [(0, 0)], 2: [(-4, -4), (4, 4)], 3: [(-4, -4), (0, 0), (4, 4)], 5: [(-4, -4), (4, -4), (0, 0), (-4, 4), (4, 4)]}
    out = (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.5/s:.2f}">'
           '<path d="M-10 -6 L0 -12 L12 -6 L12 8 L2 14 L-10 8 Z"/><path d="M-10 -6 L2 0 L12 -6 M2 0 V14" fill="none"/>')
    out += "".join(f'<circle cx="{-4 + dx*0.5:.1f}" cy="{4 + dy*0.6 + dx*0.2:.1f}" r="1.3" fill="#000" stroke="none"/>' for dx, dy in d[pips[0]])
    out += "".join(f'<circle cx="{7 + dx*0.45:.1f}" cy="{4 + dy*0.6 - dx*0.2:.1f}" r="1.3" fill="#000" stroke="none"/>' for dx, dy in d[pips[1]])
    return out + "</g>"


def pawn(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.3/s:.2f}"><path d="M-6 0 Q-7 -10 0 -12 Q7 -10 6 0 Z"/>'
            '<path d="M-8 -10 Q0 -20 8 -10 Q0 -7 -8 -10 Z"/><path d="M0 -16 V-19" fill="none"/></g>')


def build():
    b = []
    # wall, window seat edge and floor
    b.append(clip_d("M30 30 H600 V250 H30 Z", lines(" ".join(f"M{x} 30 V250" for x in range(60, 600, 40)), 0.9), 1.4))
    b.append('<rect x="30" y="244" width="570" height="12" stroke-width="1.6"/>')
    # braided rug
    b.append(rug_round(310, 520, 280, 210, 3))
    b.append(lines(" ".join(f"M{310 + 270*__import__('math').cos(a/10):.1f} {520 + 202*__import__('math').sin(a/10):.1f} l4 -6" for a in range(0, 63, 2)), 1))
    # stack of game boxes with icon lids (Dot on top)
    for k, (w, ico) in enumerate(((118, "star"), (104, "leaf"), (110, "mushroom"))):
        y = 300 - k * 30
        b.append(f'<rect x="{486 - w/2}" y="{y}" width="{w}" height="28" rx="3" stroke-width="1.8"/>' + lines(f"M{486 - w/2} {y + 8} H{486 + w/2}", 1)
                 + icon(ico, 486, y + 18, 0.45, 1))
    b.append(dot(492, 231))
    # Pip behind the table cheering (dice just rolled)
    b.append(char("pi", 310, 420, 1.15, arms=(160, -160), mood="happy", wag=True, sit=True))
    # floor cushions with tassels under Juniper and Miso
    b.append(cushion(126, 560, 120, 60, "zigzag", 0, tassel=True) + cushion(494, 560, 120, 60, "dots", 0, tassel=True))
    b.append(char("ju", 120, 560, 1.15, arms=(14, -40), sit=True))
    b.append(char("mi", 494, 560, 1.25, arms=(40, -14), sit=True))
    # low coffee table
    top = "M178 406 H442 L478 560 H142 Z"
    b.append(f'<path d="{top}" stroke-width="2.2"/><path d="M142 560 H478 V578 H142 Z" stroke-width="1.9"/>')
    b.append('<path d="M156 578 H174 V610 H156 Z M446 578 H464 V610 H446 Z" stroke-width="1.8"/>')
    # the board with a winding path of icon squares, tilted toward the viewer
    board = "M206 418 H414 L440 540 H180 Z"
    b.append(f'<path d="{board}" stroke-width="2"/>')
    path = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (1, 1), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2)]
    icons = ["star", "leaf", "mushroom", "star", "leaf", "mushroom", "star", "leaf", "mushroom", "star", "leaf", "heart"]
    for k, (c, r) in enumerate(path):
        yt = 428 + r * 36
        f0, f1 = (yt - 418) / 122, (yt + 30 - 418) / 122
        xl0, xr0 = 206 - 26 * f0 + 10, 414 + 26 * f0 - 10
        xl1, xr1 = 206 - 26 * f1 + 10, 414 + 26 * f1 - 10
        w0, w1 = (xr0 - xl0) / 4, (xr1 - xl1) / 4
        p = f"M{xl0 + c*w0 + 2:.1f} {yt} L{xl0 + (c + 1)*w0 - 2:.1f} {yt} L{xl1 + (c + 1)*w1 - 2:.1f} {yt + 30} L{xl1 + c*w1 + 2:.1f} {yt + 30} Z"
        b.append(f'<path d="{p}" stroke-width="1.4"/>' + icon(icons[k], (xl0 + xl1) / 2 + (c + 0.5) * (w0 + w1) / 2, yt + 15, 0.55, 1))
    b.append(pawn(262, 458, 1.3) + pawn(374, 494, 1.3))
    b.append(die(330, 384, 1.3, (5, 3)) + die(360, 398, 1.2, (2, 1)))
    # card deck and popcorn bowl
    b.append(''.join(f'<rect x="{150 + k*6}" y="{430 - k*3}" width="28" height="38" rx="3" stroke-width="1.4" transform="rotate({-12 + k*8} {164 + k*6} {449 - k*3})"/>' for k in range(3)))
    b.append(icon("heart", 180, 446, 0.5) + icon("star", 186, 442, 0.4))
    b.append(bowl(440, 560, 74, 30))
    for k in range(7):
        b.append(f'<path d="M{410 + k*9} {530 - (k % 2)*6} q-6 -6 0 -11 q4 -6 10 -2 q6 -3 7 4 q4 6 -3 9 q-4 4 -9 0 Z" stroke-width="1.1"/>')
    # Thimble on the near edge of the table
    b.append(char("th", 312, 600, 1.35, arms=(150, -40), mood="happy"))
    b.append(cushion(312, 640, 90, 44, "heart", 0, tassel=True))
    return "".join(b)


def svg():
    return page(build(), TITLE)
