"""Page 40 — The Great Leaf Pile (autumn lane outside the cottage)."""
import random
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, oak_leaf, scallop_blob, pumpkin
from props import maple_leaf, ginkgo_leaf, leaf_simple, acorn

TITLE = "Page 40 — The Great Leaf Pile"


def any_leaf(k, x, y, rot, s):
    f = (oak_leaf, maple_leaf, ginkgo_leaf, leaf_simple)[k % 4]
    if f is oak_leaf:
        return oak_leaf(x, y, rot, s, 1.2)
    return f(x, y, rot, s)


def build():
    b = []
    rnd = random.Random(40)
    # autumn trees lining the lane
    for (x, w) in ((70, 90), (540, 100)):
        b.append(f'<path d="M{x - 12} 520 Q{x - 8} 380 {x - 4} 300 H{x + 8} Q{x + 10} 380 {x + 14} 520 Z" stroke-width="1.8"/>'
                 + lines(f"M{x} 340 q-4 30 0 60 M{x + 4} 430 q4 30 0 60", 0.9))
        b.append(scallop_blob(x, 200, w, 120, 11, 0.28, 1.8))
        b.append("".join(any_leaf(k, x + rnd.uniform(-w*0.6, w*0.6), 200 + rnd.uniform(-80, 80), rnd.uniform(0, 360), 0.9) for k in range(7)))
    b.append('<path d="M30 470 H600 V800 H30 Z" stroke-width="1.6"/>')
    # low stone wall and garden fence with a pumpkin on a post
    from scene import stone_grid
    b.append(clip_d("M30 430 H300 V490 H30 Z", stone_grid(30, 430, 270, 60, 20, [[46, 38, 52], [30, 50, 40], [40, 44, 36]], 1.1, 6), 1.8))
    b.append(lines(" ".join(f"M{x} 410 V490" for x in range(330, 600, 34)), 6) + lines(" ".join(f"M{x} 410 V490" for x in range(330, 600, 34)), 3).replace('stroke-width="3"', 'stroke="#fff" stroke-width="3"'))
    b.append('<rect x="320" y="430" width="280" height="8" stroke-width="1.5"/><rect x="320" y="462" width="280" height="8" stroke-width="1.5"/>')
    b.append('<rect x="458" y="370" width="16" height="120" stroke-width="1.8"/>' + pumpkin(466, 370, 54, 40))
    # wheelbarrow and rake
    b.append('<path d="M440 580 H560 L540 630 H460 Z" stroke-width="2"/><circle cx="548" cy="644" r="16" stroke-width="2"/><circle cx="548" cy="644" r="5" stroke-width="1.2"/>'
             + lines("M440 586 L404 600 M466 630 L460 660", 3.4))
    b.append("".join(any_leaf(k, 460 + k * 16, 578 - (k % 2) * 8, k * 50, 0.8) for k in range(6)))
    # the big leaf pile at the lower centre
    pile = "M120 760 Q120 640 210 610 Q300 580 380 616 Q470 650 470 760 Z"
    b.append(f'<path d="{pile}" stroke-width="2"/>')
    pl = "".join(any_leaf(k, rnd.uniform(140, 450), rnd.uniform(630, 760), rnd.uniform(0, 360), rnd.uniform(1.0, 1.4)) for k in range(26))
    b.append(clip_d(pile, pl, 2))
    # Juniper with the rake, Miso tossing an armful
    jx, jy, js = 110, 640, 1.3
    b.append(char("ju", jx, jy, js, arms=(14, -60), mood="happy"))
    rx, ry = paw("ju", jx, jy, js, "R", -60)
    b.append(f'<path d="M{rx - 30:.0f} {ry - 60:.0f} L{rx + 70:.0f} {ry + 90:.0f}" stroke-width="5"/><path d="M{rx - 30:.0f} {ry - 60:.0f} L{rx + 70:.0f} {ry + 90:.0f}" stroke="#fff" stroke-width="2"/>'
             f'<path d="M{rx + 50:.0f} {ry + 92:.0f} L{rx + 96:.0f} {ry + 74:.0f}" stroke-width="5"/>'
             + lines(" ".join(f"M{rx + 52 + k*8:.0f} {ry + 92 - k*3.2:.0f} l4 12" for k in range(6)), 1.6))
    b.append(arms_only("ju", jx, jy, js, (None, -60)))
    b.append(char("mi", 520, 750, 1.3, arms=(160, -160), mood="happy"))
    b.append("".join(any_leaf(k, 520 + rnd.uniform(-50, 50), 560 + rnd.uniform(-40, 30), rnd.uniform(0, 360), 0.9) for k in range(6)))
    # Pip leaping, at the peak of his jump, motion ticks around his tail
    b.append(char("pi", 300, 520, 1.3, arms=(150, -150), mood="happy", wag=True, rot=-10))
    b.append(lines("M232 460 q-10 -6 -20 0 M236 480 q-12 0 -22 6 M374 420 l10 -8 M380 440 l12 -4", 1.3))
    # leaves spiralling down from the upper right into the pile (Dot rides one)
    sp = [(560, 60), (500, 90), (430, 110), (370, 150), (420, 210), (480, 260), (440, 320), (360, 340), (250, 360), (200, 300), (170, 390), (230, 440), (380, 470), (400, 540)]
    for k, (x, y) in enumerate(sp):
        b.append(any_leaf(k, x, y, k * 40, 1.25))
    b.append(maple_leaf(330, 92, 20, 1.6))
    b.append(dot(330, 64, 0.9))
    b.append(acorn(80, 740) + acorn(500, 690) + acorn(560, 740, 1.1, 30))
    return "".join(b)


def svg():
    return page(build(), TITLE)
