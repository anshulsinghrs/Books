"""Page 6 — Breakfast Tray Prep (bird's-eye view of the counter)."""
from math import sin, cos, radians
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, daisy
from props import icon

TITLE = "Page 6 — Breakfast Tray Prep"


def orange(x, y, r=15):
    seg = " ".join(f"M{x} {y} L{x + r*0.72*cos(radians(a)):.1f} {y + r*0.72*sin(radians(a)):.1f}" for a in range(0, 360, 45))
    return (f'<circle cx="{x}" cy="{y}" r="{r}" stroke-width="1.5"/><circle cx="{x}" cy="{y}" r="{r*0.78:.1f}" stroke-width="1"/>'
            + lines(seg, 0.9))


def strawberry(x, y, rot=0, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.3/s:.2f}">'
            '<path d="M0 12 C-12 4 -12 -8 -4 -10 Q0 -11 4 -10 C12 -8 12 4 0 12 Z"/>'
            '<path d="M0 8 C-6 2 -6 -4 0 -6 C6 -4 6 2 0 8 Z" stroke-width="0.9"/>'
            '<circle cx="-5" cy="-2" r="0.9" fill="#000" stroke="none"/><circle cx="5" cy="-1" r="0.9" fill="#000" stroke="none"/><circle cx="0" cy="5" r="0.9" fill="#000" stroke="none"/></g>')


def egg_cup(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="19" stroke-width="1.6"/><circle cx="{x}" cy="{y}" r="15" stroke-width="1"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="11" ry="12" stroke-width="1.4"/><path d="M{x-7} {y-3} l3 3 l3 -3 l3 3 l3 -3" fill="none" stroke-width="0.9"/>')


def jam_top(x, y, ico):
    return (f'<circle cx="{x}" cy="{y}" r="22" stroke-width="1.7"/><circle cx="{x}" cy="{y}" r="17" stroke-width="1.1"/>'
            + icon(ico, x, y, 0.75, 1.0))


def napkin(x, y, rot, w=70):
    sc = " ".join(f"M{-w/2 + k*10} {-w/2} a5 5 0 0 1 10 0" for k in range(int(w / 10)))
    sq = f"M{-w/2} {-w/2} H{w/2} V{w/2} H{-w/2} Z"
    edge = "".join(f'<path transform="rotate({r})" d="{sc}" stroke-width="1.1"/>' for r in (0, 90, 180, 270))
    return (f'<g transform="translate({x} {y}) rotate({rot})">{edge}<path d="{sq}" stroke-width="1.6"/>'
            f'<path d="M{-w/2 + 7} {-w/2 + 7} H{w/2 - 7} V{w/2 - 7} H{-w/2 + 7} Z" fill="none" stroke-width="0.8" stroke-dasharray="3 3"/></g>')


def build():
    b = []
    # wooden counter planks fill the page
    b.append(clip_d("M30 160 H600 V800 H30 Z", lines(" ".join(f"M30 {y} H600" for y in range(232, 800, 72))
                    + " " + " ".join(f"M{x} {y} V{y + 72}" for y in range(160, 800, 72) for x in ((150 + y) % 260 + 40, (150 + y) % 260 + 300)), 1.1)
                    + lines("M80 196 q20 -6 40 0 M420 268 q20 -6 40 0 M120 480 q20 -6 40 0 M500 560 q20 -6 40 0 M300 700 q20 -6 40 0", 0.8), 1.8))
    # Juniper at the top edge, leaning over the cutting board
    jx, jy, js = 312, 236, 1.55
    b.append(char("ju", jx, jy, js, arms=(None, None), head_rot=4))
    b.append(lines("M30 160 H600", 2.2))
    # cutting board with the round loaf and slices
    b.append('<rect x="214" y="176" width="200" height="124" rx="16" stroke-width="2"/><circle cx="398" cy="238" r="6" stroke-width="1.4"/>')
    b.append('<circle cx="270" cy="238" r="44" stroke-width="1.9"/>' + lines("M244 214 Q270 206 296 214 M240 236 Q270 228 300 236 M244 258 Q270 250 296 262", 1.1))
    for k in range(3):
        x = 326 + k * 20
        b.append(f'<rect x="{x}" y="200" width="16" height="76" rx="7" stroke-width="1.6"/><rect x="{x + 3}" y="204" width="10" height="68" rx="5" stroke-width="0.9"/>')
    b.append(arms_only("ju", jx, jy, js, (-8, 26)))
    kx, ky = paw("ju", jx, jy, js, "L", 26)
    b.append(f'<g transform="translate({kx:.1f} {ky:.1f}) rotate(118)" stroke-width="1.5"><rect x="-6" y="-4" width="26" height="9" rx="4"/>'
             '<path d="M20 -4 H74 Q78 0 74 5 H20 Z"/></g>')
    b.append(arms_only("ju", jx, jy, js, (-8, None)))
    # the wooden tray
    b.append('<rect x="160" y="326" width="330" height="290" rx="24" stroke-width="2.2"/>'
             '<rect x="176" y="342" width="298" height="258" rx="16" stroke-width="1.3"/>'
             '<rect x="296" y="330" width="58" height="10" rx="5" stroke-width="1.3"/><rect x="296" y="602" width="58" height="10" rx="5" stroke-width="1.3"/>')
    b.append(napkin(236, 404, 10) + napkin(410, 530, -12, 64))
    b.append(egg_cup(236, 404) + egg_cup(410, 530))
    b.append(jam_top(330, 384, "berry") + jam_top(384, 400, "heart"))
    # vase of daisies (top view)
    b.append('<circle cx="440" cy="390" r="15" stroke-width="1.6"/>' + daisy(440, 372, 12, 7) + daisy(456, 394, 11, 7) + daisy(424, 398, 11, 7) + daisy(442, 412, 10, 7))
    # fruit plate: strawberries and orange rounds
    b.append('<circle cx="270" cy="520" r="62" stroke-width="1.9"/><circle cx="270" cy="520" r="50" stroke-width="1.1"/>')
    b.append(orange(250, 500) + orange(288, 492) + orange(296, 532))
    b.append(strawberry(246, 540, -20) + strawberry(268, 552, 10) + strawberry(232, 516, -60))
    # butter dish with Dot on its rim
    b.append('<rect x="352" y="440" width="80" height="54" rx="10" stroke-width="1.8"/><rect x="368" y="452" width="48" height="30" rx="4" stroke-width="1.4"/>'
             + lines("M376 460 l10 14 M392 458 l10 14", 0.9))
    b.append(dot(436, 432, 0.95))
    # Pebble at the left side, leaning in to arrange a strawberry
    px, py, ps, pr = 20, 560, 1.85, 72
    b.append(char("pb", px, py, ps, arms=(None, None), rot=pr))
    b.append(arms_only("pb", px, py, ps, (-30, 10), rot=pr))
    sx, sy = paw("pb", px, py, ps, "R", 10, rot=pr)
    b.append(strawberry(sx + 8, sy, 70, 1.1))
    # spare strawberry bowl and orange on the counter
    b.append('<circle cx="540" cy="250" r="34" stroke-width="1.8"/><circle cx="540" cy="250" r="26" stroke-width="1"/>'
             + strawberry(530, 244, 20) + strawberry(552, 256, -30) + strawberry(540, 236, 80))
    b.append(orange(540, 680, 22) + orange(500, 700, 16))
    b.append(napkin(110, 690, 20, 70))
    return "".join(b)


def svg():
    return page(build(), TITLE)
