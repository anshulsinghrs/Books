"""Page 2 — The Kettle Song (Tofu at Bramble's stove)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import stove, kettle, teapot, tin, jar, mug, teacup, bowl, icon

TITLE = "Page 2 — The Kettle Song"


def build():
    b = []
    # wall clock (no numbers) above the shelf
    b.append('<circle cx="130" cy="94" r="34" stroke-width="2"/><circle cx="130" cy="94" r="27" stroke-width="1.1"/>'
             + lines("M130 70 V76 M130 112 V118 M106 94 H112 M148 94 H154 M130 94 L130 78 M130 94 L142 100", 1.4)
             + '<circle cx="130" cy="94" r="2.6" fill="#000" stroke="none"/>')
    # tiled backsplash, a small flower in every third tile
    tiles = ""
    for r, y in enumerate(range(180, 700, 42)):
        for c, x in enumerate(range(45, 580, 42)):
            if (r + c) % 3 == 0:
                tiles += (f'<g transform="translate({x+21} {y+21})" stroke-width="0.9"><circle cy="-6" r="4.2"/><circle cx="6" r="4.2"/>'
                          f'<circle cy="6" r="4.2"/><circle cx="-6" r="4.2"/><circle r="2.6"/></g>')
    tiles += lines(" ".join(f"M30 {y} H600" for y in range(222, 700, 42)) + " " + " ".join(f"M{x} 180 V700" for x in range(87, 600, 42)), 1.0)
    b.append(clip_d("M30 180 H600 V700 H30 Z", tiles, 1.6))
    # stove with pipe running up behind the shelf, kettle singing on top
    b.append(stove(160, 452, 196, 304, pipe_to=20))
    b.append(kettle(150, 452, 1.35))
    # gingham tea towel over the stove rail
    tw = "M226 466 H262 V540 Q244 546 226 540 Z"
    b.append(clip_d(tw, lines("M234 460 V550 M244 460 V550 M254 460 V550 M220 480 H268 M220 494 H268 M220 508 H268 M220 522 H268", 1.0), 1.6))
    b.append('<rect x="222" y="460" width="44" height="10" rx="3" stroke-width="1.5"/>')
    # shelf across the top: honey jar, tea tins, sugar bowl, two mugs with Dot between
    b.append('<rect x="30" y="150" width="570" height="13" rx="2" stroke-width="2"/>')
    b.append('<path d="M70 163 L84 190 H70 Z M560 163 L546 190 H560 Z" stroke-width="1.5"/>')
    b.append(jar(250, 150, 36, 48, "drop"))
    b.append('<path d="M256 108 L270 74" fill="none" stroke-width="2.4"/><ellipse cx="272" cy="70" rx="6" ry="8" transform="rotate(25 272 70)" stroke-width="1.5"/>'
             + lines("M268 64 L277 66 M266 70 L278 73", 0.9))
    b.append(tin(318, 150, 36, 46, "leaf") + tin(370, 150, 36, 46, "flower"))
    b.append(bowl(426, 150, 42, 22) + '<path d="M414 128 Q426 118 438 128 Z" stroke-width="1.4"/><circle cx="426" cy="118" r="3.4" stroke-width="1.2"/>')
    b.append(mug(476, 150, 1.0, "dots") + mug(530, 150, 1.0, "stripes"))
    b.append(dot(503, 141))
    # hanging mugs on hooks under the shelf
    for (x, pat) in ((220, "hearts"), (280, "stars"), (340, "leaves"), (400, "checks")):
        b.append(lines(f"M{x} 163 V174 q0 5 -5 5", 1.3))
        b.append(f'<g transform="translate({x - 10} 178) rotate(180)">' + mug(0, 0, 0.9, pat, handle="l") + "</g>")
    # Tofu, waist-up behind the counter: a teacup in one paw, the moon tin in the other
    tx, ty, ts = 432, 690, 2.2
    b.append(char("to", tx, ty, ts, arms=(None, None)))
    lx, ly = paw("to", tx, ty, ts, "L", 140)
    rx, ry = paw("to", tx, ty, ts, "R", 18)
    b.append(arms_only("to", tx, ty, ts, (140, None)))
    b.append(tin(lx, ly + 18, 40, 50, "moon"))
    b.append(f'<g transform="translate({tx} {ty}) scale({ts})" stroke-width="{2/ts:.3f}"><use href="#to-arm" transform="translate(-48 -70) rotate(140)"/></g>')
    b.append(arms_only("to", tx, ty, ts, (None, 18)))
    b.append(teacup(rx - 6, ry + 8, 1.8))
    # counter in front with the leaf teapot
    b.append(clip_d("M262 666 H600 V800 H262 Z", lines("M262 690 H600 M330 704 V800 M440 704 V800 M540 704 V800", 1.2), 2.0))
    b.append(teapot(330, 684, 0.95))
    b.append(lines("M300 730 H322 M352 742 H380 M470 724 H500 M560 748 H590", 0.9))
    return "".join(b)


def svg():
    return page(build(), TITLE)
