"""Page 28 — Picnic Under the Old Oak (Fernwood, six friends)."""
import random
from chars import char, dot, page, paw
from scene import (clip_d, lines, oak_leaf, fern, foxglove, mushroom, daisy, tuft, scallop_blob)

TITLE = "Page 28 — Picnic Under the Old Oak"

BACK_Y, FRONT_Y = 522, 790
BL, BR = (196, 572), (20, 640)   # blanket back-edge x-range, front-edge x-range
ROWS = [0, 0.15, 0.32, 0.52, 0.75, 1.0]


def bpt(u, f):
    y = BACK_Y + (FRONT_Y - BACK_Y) * f
    xl = BL[0] + (BR[0] - BL[0]) * f
    xr = BL[1] + (BR[1] - BL[1]) * f
    return xl + (xr - xl) * u, y


def canopy():
    rnd = random.Random(7)
    pts = []
    x = 640
    while x > -20:
        pts.append(x)
        x -= rnd.choice((54, 60, 66, 72))
    pts.append(-30)
    base = lambda x: 300 + 26 * __import__("math").sin(x / 70.0)
    d = f"M-30 -10 H640 V{base(640):.0f} "
    for i in range(len(pts) - 1):
        x1, x2 = pts[i], pts[i + 1]
        dep = rnd.choice((26, 32, 38))
        d += f"Q{(x1 + x2) / 2:.0f} {base((x1 + x2) / 2) + dep:.0f} {x2} {base(x2):.0f} "
    return d + "Z"


def build():
    b = []
    # distant trunks and forest floor
    for (x, w) in ((300, 26), (470, 22), (560, 30)):
        b.append(f'<path d="M{x} 250 V530 H{x + w} V250 Z" stroke-width="1.4"/>')
        b.append(lines(f"M{x + w*0.4:.0f} 340 q-3 20 0 40 M{x + w*0.6:.0f} 430 q3 20 0 40", 0.8))
    b.append('<path d="M30 512 C200 500 400 510 640 498 L640 800 L30 800 Z" stroke-width="1.5"/>')
    # foxgloves and ferns along the back edge
    b.append(foxglove(452, 522, 120) + foxglove(566, 520, 150) + foxglove(236, 520, 104))
    b.append(fern(480, 528, 80, -30, -16, 6, 11) + fern(500, 530, 92, 12, 18, 6, 11))
    b.append(fern(330, 528, 70, -20, -12, 5, 10) + fern(348, 530, 74, 18, 14, 5, 10))
    b.append(fern(590, 528, 80, -18, -10, 6, 11))
    # the old oak trunk with its hollow and the squirrel
    b.append('<path d="M58 250 C66 330 70 420 62 520 C56 548 36 560 30 566 L30 580 C70 576 92 562 108 552 '
             'C122 566 150 578 196 580 C176 562 168 544 168 520 C162 430 166 330 176 250 Z" stroke-width="2.2"/>')
    b.append(lines("M86 290 Q80 340 88 390 M150 300 Q156 340 150 380 M90 450 Q84 480 92 506 M150 470 Q156 500 148 526", 1.1))
    b.append('<path d="M168 438 C190 430 214 424 238 426 L238 436 C216 436 194 442 170 452 Z" stroke-width="1.6"/>')
    b.append(oak_leaf(236, 432, 70, 1.0))
    b.append(dot(210, 420))  # Dot on the branch above the squirrel
    b.append('<ellipse cx="116" cy="500" rx="26" ry="34" stroke-width="2"/>')
    b.append('<ellipse cx="116" cy="502" rx="19" ry="27" stroke-width="1.2"/>')
    # squirrel peeking out (a visitor, not one of the friends)
    b.append('<path d="M100 498 C86 480 92 454 112 460 C100 470 104 484 112 492 Z" stroke-width="1.4"/>')
    b.append('<path d="M110 480 L106 468 L116 474 Z M126 476 L130 464 L134 478 Z" stroke-width="1.3"/>')
    b.append('<circle cx="122" cy="490" r="14" stroke-width="1.6"/>')
    b.append('<circle cx="117" cy="488" r="2" fill="#000" stroke="none"/><circle cx="128" cy="488" r="2" fill="#000" stroke="none"/>')
    b.append('<ellipse cx="122" cy="495" rx="2.2" ry="1.6" fill="#000" stroke="none"/>')
    b.append('<ellipse cx="112" cy="512" rx="6" ry="4.5" stroke-width="1.3"/><ellipse cx="130" cy="512" rx="6" ry="4.5" stroke-width="1.3"/>')
    # branches, then the great canopy built from overlapping leaf clumps
    b.append('<path d="M150 330 C210 290 300 270 400 262 L404 278 C310 288 222 310 168 352 Z" stroke-width="1.8"/>')
    b.append('<path d="M100 330 C80 300 60 280 30 270 L30 286 C56 296 74 314 86 338 Z" stroke-width="1.8"/>')
    rnd = random.Random(5)
    clumps = [(80, 40), (210, 30), (350, 44), (480, 30), (600, 50),
              (20, 140), (150, 130), (290, 140), (420, 128), (560, 140),
              (80, 236), (220, 232), (360, 240), (500, 236), (620, 230),
              (150, 300), (290, 304), (430, 298), (570, 296), (30, 300)]
    for (x, y) in clumps:
        x += rnd.uniform(-22, 22); y += rnd.uniform(-14, 14)
        b.append(scallop_blob(round(x), round(y), rnd.uniform(58, 92), rnd.uniform(44, 62), n=rnd.choice((8, 9, 10)), bump=0.26, sw=1.8))
        b.append(lines(f"M{x-26} {y+10} Q{x-12} {y-4} {x+4} {y+8} M{x+12} {y-18} Q{x+24} {y-26} {x+34} {y-14}", 0.9))
    rnd = random.Random(11)
    for k in range(22):
        x = 40 + k * 26 + rnd.uniform(-6, 6)
        y = 348 + rnd.uniform(-6, 8)
        b.append(oak_leaf(x, y, rnd.uniform(150, 210), rnd.uniform(1.05, 1.3)))
    for (x, y) in ((262, 352), (434, 350)):
        b.append(f'<path d="M{x} {y-8} V{y}" fill="none" stroke-width="1.1"/><ellipse cx="{x}" cy="{y+9}" rx="5.5" ry="7" stroke-width="1.2"/>'
                 f'<path d="M{x-7} {y+4} Q{x} {y-5} {x+7} {y+4} Z" stroke-width="1.2"/>')
    b.append(mushroom(44, 578, 0.9) + mushroom(70, 586, 0.7))

    # gingham blanket in perspective
    grid = ""
    for k in range(1, 10):
        u = k / 10
        x1, y1 = bpt(u, 0)
        x2, y2 = bpt(u, 1)
        grid += f"M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} "
    for f in ROWS[1:-1]:
        x1, y1 = bpt(0, f)
        x2, y2 = bpt(1, f)
        grid += f"M{x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} "
    (ax, ay), (bx, by), (cx_, cy_), (dx, dy) = bpt(0, 0), bpt(1, 0), bpt(1, 1), bpt(0, 1)
    b.append(clip_d(f"M{ax:.1f} {ay:.1f} L{bx:.1f} {by:.1f} L{cx_:.1f} {cy_:.1f} L{dx:.1f} {dy:.1f} Z", lines(grid, 1.2), 2.0))

    # ---- back row: Juniper (thermos cup), Bramble (the lattice pie), Tofu (sandwich)
    s = 0.95
    b.append(char("ju", 272, 580, s, arms=(12, -40), sit=True))
    qx, qy = paw("ju", 272, 580, s, "R", -40)
    b.append(f'<path d="M{qx-6:.1f} {qy-14:.1f} H{qx+8:.1f} L{qx+6:.1f} {qy+2:.1f} H{qx-4:.1f} Z" stroke-width="1.4"/>')
    b.append(char("br", 392, 586, s, arms=(17, -17), sit=True, mood="happy"))
    b.append('<ellipse cx="392" cy="544" rx="40" ry="12" stroke-width="1.8"/>')
    b.append(clip_d("M356 540 Q392 522 428 540 Q392 552 356 540 Z",
                    lines("M366 530 L380 548 M380 526 L396 550 M396 524 L410 548 M410 526 L422 544 "
                          "M362 542 L376 526 M378 546 L394 524 M394 548 L410 526 M410 546 L422 532", 1), 1.4))
    b.append(lines("M352 546 q4 4 8 0 q4 4 8 0 q4 4 8 0 q4 4 8 0 q4 4 8 0 q4 4 8 0 q4 4 8 0 q4 4 8 0 q4 4 8 0 q4 4 8 0", 1))
    b.append(f'<g transform="translate(392 586) scale({s})" stroke-width="{2/s:.3f}">'
             '<use href="#br-arm" transform="translate(-44 -94) rotate(17)"/><use href="#br-arm" transform="translate(44 -94) rotate(-17)"/></g>')
    b.append(char("to", 512, 600, s, arms=(150, -14), sit=True))
    sx, sy = paw("to", 512, 600, s, "L", 150)
    b.append(f'<path d="M{sx-14:.1f} {sy+6:.1f} L{sx+12:.1f} {sy+6:.1f} L{sx-1:.1f} {sy-16:.1f} Z" stroke-width="1.5"/>'
             + lines(f"M{sx-9:.1f} {sy+1:.1f} L{sx+7:.1f} {sy+1:.1f}", 1))
    b.append(f'<g transform="translate(512 600) scale({s})" stroke-width="{2/s:.3f}"><use href="#to-arm" transform="translate(-48 -70) rotate(150)"/></g>')

    # ---- food in the middle of the blanket
    b.append('<rect x="316" y="600" width="24" height="44" rx="6" stroke-width="1.7"/><rect x="314" y="592" width="28" height="12" rx="4" stroke-width="1.6"/>'
             + lines("M316 616 H340", 1))
    b.append('<ellipse cx="410" cy="648" rx="40" ry="11" stroke-width="1.7"/>')
    for (x, y) in ((388, 640), (412, 636), (434, 642)):
        b.append(f'<path d="M{x-14} {y+6} L{x+14} {y+6} L{x} {y-14} Z" stroke-width="1.4"/>' + lines(f"M{x-9} {y} L{x+9} {y}", 0.9))
    for (x, y) in ((250, 734), (520, 744), (366, 742)):
        b.append(f'<ellipse cx="{x}" cy="{y+6}" rx="5.5" ry="7" stroke-width="1.2"/><path d="M{x-7} {y+1} Q{x} {y-8} {x+7} {y+1} Z" stroke-width="1.2"/>')

    # ---- front row: Pebble with the berry bowl, Miso with lemonade, lemonade jug
    b.append(char("pb", 300, 712, 1.0, arms=(-28, -10), sit=True))
    b.append('<path d="M266 682 Q268 704 286 706 Q304 704 306 682 Z" stroke-width="1.7"/>')
    for (x, y) in ((274, 680), (284, 676), (294, 679), (279, 670), (290, 669), (300, 682)):
        b.append(f'<circle cx="{x}" cy="{y}" r="5" stroke-width="1.1"/>')
    b.append('<g transform="translate(300 712)" stroke-width="2"><use href="#pb-arm" transform="translate(-19 -48) rotate(-28)"/></g>')
    b.append(char("mi", 450, 716, 1.0, arms=(10, -150), sit=True))
    gx, gy = paw("mi", 450, 716, 1.0, "R", -150)
    b.append(f'<path d="M{gx-6:.1f} {gy-22:.1f} H{gx+8:.1f} L{gx+6:.1f} {gy+2:.1f} H{gx-4:.1f} Z" stroke-width="1.4"/>'
             + lines(f"M{gx-5:.1f} {gy-14:.1f} H{gx+7:.1f}", 0.9))
    b.append(f'<g transform="translate(450 716)" stroke-width="2"><use href="#mi-arm" transform="translate(17 -38) rotate(-150)"/></g>')
    b.append('<path d="M540 674 Q560 674 560 696 Q560 714 542 716" fill="none" stroke-width="5"/>')
    b.append('<path d="M540 674 Q560 674 560 696 Q560 714 542 716" fill="none" stroke="#fff" stroke-width="2"/>')
    b.append('<path d="M500 668 L492 658 L512 662 Q536 660 540 668 Q546 700 536 730 Q520 736 504 730 Q494 700 500 668 Z" stroke-width="1.9"/>')
    b.append(lines("M500 680 Q520 686 540 680", 1))
    b.append('<circle cx="520" cy="704" r="11" stroke-width="1.3"/>' + lines("M520 693 V715 M509 704 H531 M512 696 L528 712 M528 696 L512 712", 0.8))

    # ---- wicker basket and Pip offering a sandwich to the squirrel
    b.append(clip_d("M128 690 H226 L216 742 Q177 750 138 742 Z",
                    lines("M120 704 H236 M120 718 H236 M120 732 H236", 1.1)
                    + lines("M146 690 L150 750 M166 690 L168 750 M186 690 L186 750 M206 690 L204 750", 1.1), 1.9))
    b.append('<path d="M124 690 Q177 670 230 690 Q177 698 124 690 Z" stroke-width="1.8"/>')
    b.append('<path d="M150 684 Q177 648 204 684" fill="none" stroke-width="2.6"/>')
    px_, py_ = 214, 650
    b.append(char("pi", px_, py_, 1.0, arms=(124, -14), wag=True, head_rot=-8))
    hx, hy = paw("pi", px_, py_, 1.0, "L", 124)
    b.append(f'<path d="M{hx-22:.1f} {hy-2:.1f} L{hx+4:.1f} {hy+6:.1f} L{hx-4:.1f} {hy-18:.1f} Z" stroke-width="1.5"/>'
             + lines(f"M{hx-15:.1f} {hy:.1f} L{hx-1:.1f} {hy+4:.1f}", 1))
    b.append(f'<g transform="translate({px_} {py_})" stroke-width="2"><use href="#pi-arm" transform="translate(-20 -42) rotate(124)"/></g>')
    return "".join(b)


def svg():
    return page(build(), TITLE)
