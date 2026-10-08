"""Page 7 — Breakfast Together (all eight under the blossoming pergola)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, blossom, scallop_blob
from props import teapot, pancake_stack, mug, lantern_hanging, icon

TITLE = "Page 7 — Breakfast Together"
VP = (310, 330)


def tpt(u, f):
    """Point on the table top: u 0..1 across, f 0 (far end) .. 1 (near edge)."""
    y = 420 + (760 - 420) * f
    xl = 262 + (130 - 262) * f
    xr = 358 + (490 - 358) * f
    return xl + (xr - xl) * u, y


def chair_back(x, y, w, h, kind):
    if kind == "ladder":
        return (f'<path d="M{x - w/2} {y} V{y - h} M{x + w/2} {y} V{y - h}" stroke-width="5"/>'
                + "".join(f'<rect x="{x - w/2}" y="{y - h + 8 + k*h*0.25:.1f}" width="{w}" height="{h*0.12:.1f}" rx="3" stroke-width="1.5"/>' for k in range(3))
                + f'<path d="M{x - w/2} {y} V{y - h} M{x + w/2} {y} V{y - h}" stroke="#fff" stroke-width="2.4"/>')
    if kind == "round":
        return (f'<path d="M{x - w/2} {y} V{y - h*0.6:.1f} A{w/2} {h*0.4:.1f} 0 0 1 {x + w/2} {y - h*0.6:.1f} V{y} Z" stroke-width="1.8"/>'
                f'<path d="M{x - w/2 + 8} {y} V{y - h*0.6:.1f} A{w/2 - 8} {h*0.4 - 8:.1f} 0 0 1 {x + w/2 - 8} {y - h*0.6:.1f} V{y} Z" stroke-width="1.1"/>')
    if kind == "spindle":
        return (f'<path d="M{x - w/2} {y - h} H{x + w/2} V{y - h + 12} H{x - w/2} Z" stroke-width="1.8"/>'
                + lines(" ".join(f"M{x - w/2 + 4 + k*(w - 8)/4:.1f} {y - h + 12} V{y}" for k in range(5)), 2.4))
    return (f'<path d="M{x - w/2} {y} V{y - h + 10} Q{x} {y - h - 10} {x + w/2} {y - h + 10} V{y} Z" stroke-width="1.8"/>'
            + f'<use href="#heart" transform="translate({x} {y - h*0.55:.1f}) scale({w/40:.2f})" stroke-width="{1.2*40/w:.2f}"/>')


def build():
    b = []
    # garden beyond: hedge and distant trees
    b.append('<path d="M30 400 C120 380 200 392 310 384 C420 376 500 392 600 380 V800 H30 Z" stroke-width="1.5"/>')
    b.append(scallop_blob(150, 330, 70, 54, 10, 0.3, 1.5) + scallop_blob(480, 320, 80, 60, 10, 0.3, 1.5))
    b.append(lines("M150 384 V360 M480 380 V356", 1.5))
    b.append(clip_d("M30 400 C120 380 200 392 310 384 C420 376 500 392 600 380 V430 H30 Z",
                    lines(" ".join(f"M{x} 380 Q{x + 10} 405 {x} 430" for x in range(40, 600, 30)), 0.9), 1.5))
    # pergola: back posts, beams, front posts with vines
    b.append('<rect x="214" y="250" width="12" height="190" stroke-width="1.6"/><rect x="394" y="250" width="12" height="190" stroke-width="1.6"/>')
    b.append('<rect x="200" y="242" width="220" height="12" stroke-width="1.6"/>')
    for x in (230, 270, 310, 350, 390):
        b.append(f'<path d="M{x - 4} 248 L{(x - VP[0]) * 3.4 + VP[0] - 8:.0f} 60 H{(x - VP[0]) * 3.4 + VP[0] + 8:.0f} L{x + 4} 248 Z" stroke-width="1.5"/>')
    b.append('<rect x="30" y="54" width="570" height="22" stroke-width="2"/>' + lines("M60 62 q20 -4 40 0 M300 66 q20 -4 40 0", 0.9))
    b.append('<rect x="48" y="76" width="26" height="700" stroke-width="2"/><rect x="546" y="76" width="26" height="700" stroke-width="2"/>')
    b.append(lines("M58 200 q-4 20 0 40 M560 300 q4 20 0 40", 0.9))
    # blossoming vines along the beams
    b.append(lines("M40 70 Q120 92 200 70 Q280 92 360 70 Q440 92 590 70 M60 76 Q40 200 64 330 M560 76 Q584 200 556 330", 1.6))
    for (x, y) in ((70, 84), (110, 74), (156, 90), (204, 78), (250, 92), (298, 80), (346, 92), (394, 78), (440, 90), (488, 78), (532, 90),
                   (60, 140), (72, 200), (56, 260), (66, 316), (562, 140), (550, 210), (566, 270), (556, 320)):
        b.append(blossom(x, y, 11, 1.1))
    b.append(lantern_hanging(170, 76, 1.0, 30) + lantern_hanging(450, 76, 1.0, 30))
    b.append(dot(258, 233.5))  # Dot on the pergola crossbeam
    # chairs behind the friends
    b.append(chair_back(118, 560, 74, 120, "ladder") + chair_back(178, 470, 50, 80, "round") + chair_back(226, 420, 40, 64, "spindle")
             + chair_back(504, 560, 74, 120, "spindle") + chair_back(446, 470, 50, 80, "heart") + chair_back(394, 420, 40, 64, "ladder"))
    # far end: Pebble on a stool at the head of the table
    b.append(char("pb", 310, 414, 0.62, arms=(20, -20), sit=True, mood="happy"))
    # left side, far to near: Miso, Clover, Bramble ; right side: Pip, Juniper, Tofu
    b.append(char("mi", 226, 452, 0.62, arms=(-30, 14), sit=True))
    b.append(char("pi", 394, 452, 0.66, arms=(-14, 30), sit=True, mood="happy", wag=True))
    b.append(char("cl", 178, 530, 0.78, arms=(-30, 14), sit=True, mood="happy"))
    b.append(char("ju", 446, 528, 0.8, arms=(-14, 30), sit=True))
    # the long table with a striped runner
    (ax, ay), (bx, by), (cx, cy), (dx, dy) = tpt(0, 0), tpt(1, 0), tpt(1, 1), tpt(0, 1)
    top = f"M{ax:.1f} {ay:.1f} L{bx:.1f} {by:.1f} L{cx:.1f} {cy:.1f} L{dx:.1f} {dy:.1f} Z"
    run = ""
    (r1x, r1y), (r2x, r2y), (r3x, r3y), (r4x, r4y) = tpt(0.36, 0), tpt(0.64, 0), tpt(0.64, 1), tpt(0.36, 1)
    runner = f"M{r1x:.1f} {r1y:.1f} L{r2x:.1f} {r2y:.1f} L{r3x:.1f} {r3y:.1f} L{r4x:.1f} {r4y:.1f} Z"
    for f in (0.12, 0.26, 0.42, 0.6, 0.8):
        (sx1, sy1), (sx2, sy2) = tpt(0.36, f), tpt(0.64, f)
        run += f"M{sx1:.1f} {sy1:.1f} L{sx2:.1f} {sy2:.1f} "
    b.append(f'<path d="{top}" stroke-width="2"/>')
    b.append(clip_d(runner, lines(run, 1.2), 1.5))
    b.append(f'<path d="M{ax:.1f} {ay:.1f} V{ay + 10:.1f} L{bx:.1f} {by + 10:.1f} V{by:.1f}" stroke-width="1.5"/>')
    # dishes on the table: tray from page 6, pancake stack from page 4, teapot from page 2
    b.append(mug(246, 446, 0.55, "dots") + mug(374, 446, 0.55, "stars") + mug(222, 520, 0.7, "hearts") + mug(398, 520, 0.7, "leaves"))
    b.append('<rect x="342" y="560" width="96" height="66" rx="10" stroke-width="1.8"/><rect x="350" y="568" width="80" height="50" rx="6" stroke-width="1"/>'
             '<circle cx="372" cy="592" r="11" stroke-width="1.4"/><ellipse cx="372" cy="592" rx="6" ry="7" stroke-width="1.1"/>'
             '<circle cx="408" cy="590" r="13" stroke-width="1.4"/>' + icon("berry", 408, 590, 0.6))
    b.append(pancake_stack(236, 640, 8, 80, 10))
    b.append(teapot(310, 520, 0.8))
    b.append(char("th", 310, 484, 0.72, arms=(150, -150), mood="happy"))
    b.append('<path d="M296 470 Q310 452 324 470 Q310 476 296 470 Z" stroke-width="1"/>')
    for (x, y, s) in ((300, 444, 0.55), (320, 700, 0.9)):
        b.append(f'<path transform="translate({x} {y}) scale({s})" d="M-8 0 Q-12 -24 -4 -30 H4 Q12 -24 8 0 Z" stroke-width="{1.6/s:.2f}"/>'
                 + blossom(x - 8 * s, y - 40 * s, 10 * s, 1.1) + blossom(x + 8 * s, y - 44 * s, 10 * s, 1.1) + blossom(x, y - 54 * s, 10 * s, 1.1))
    for (x, y) in ((196, 700), (426, 700), (214, 590), (406, 600)):
        b.append(f'<ellipse cx="{x}" cy="{y}" rx="34" ry="12" stroke-width="1.6"/><ellipse cx="{x}" cy="{y}" rx="24" ry="8" stroke-width="1"/>')
    b.append('<ellipse cx="196" cy="696" rx="18" ry="6" stroke-width="1.3"/><ellipse cx="196" cy="692" rx="18" ry="6" stroke-width="1.3"/>')
    b.append(lines("M150 690 L156 712 M244 688 L240 712 M474 690 L470 712", 1.6))
    # near corners: Bramble (left) and Tofu (right)
    b.append(char("br", 104, 744, 0.92, arms=(14, -40), sit=True, mood="happy"))
    mx, my = paw("br", 104, 744, 0.92, "R", -40)
    b.append(mug(mx + 4, my + 6, 0.9, "checks", steam=True))
    b.append(char("to", 518, 748, 0.92, arms=(40, -14), sit=True))
    tx, ty = paw("to", 518, 748, 0.92, "L", 40)
    b.append(mug(tx - 2, ty + 8, 0.9, "stripes", steam=True, handle="l"))
    return "".join(b)


def svg():
    return page(build(), TITLE)
