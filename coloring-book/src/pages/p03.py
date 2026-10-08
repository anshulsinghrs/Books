"""Page 3 — Window Seat Pages (Miso reading in the window seat)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, scallop_blob, daisy, tulip, blossom
from props import mug, plant_pot, plant, cushion, book_open

TITLE = "Page 3 — Window Seat Pages"


def build():
    b = []
    arch_o = "M78 480 V250 A232 200 0 0 1 542 250 V480 Z"
    arch_i = "M94 470 V252 A216 186 0 0 1 526 252 V470 Z"
    b.append(f'<path d="{arch_o}" stroke-width="2.2"/>')
    view = ('<path d="M80 360 C180 340 300 352 540 330 V480 H80 Z" stroke-width="1.4"/>'
            + '<use href="#cloud" transform="translate(380 140) scale(1.1)" stroke-width="1.4"/>'
            + '<use href="#cloud" transform="translate(470 220) scale(0.7)" stroke-width="2"/>'
            + '<rect x="408" y="270" width="16" height="80" stroke-width="1.5"/>' + scallop_blob(416, 250, 54, 44, 10, 0.3, 1.6)
            + "".join(f'<path d="M{x} 470 V420 L{x+7} 410 L{x+14} 420 V470 Z" stroke-width="1.3"/>' for x in range(100, 540, 24))
            + lines("M90 432 H540 M90 456 H540", 1.2)
            + tulip(128, 410, 30, -4) + tulip(300, 410, 34, 3) + tulip(476, 410, 30, 4)
            # branch with the bird feeder (Dot is the bird Miso watches)
            + '<path d="M80 120 C140 128 200 120 250 104 L252 114 C204 130 144 138 80 132 Z" stroke-width="1.6"/>'
            + blossom(130, 122, 10) + blossom(226, 108, 9)
            + lines("M190 120 V156", 1.2)
            + '<path d="M168 168 L190 154 L212 168 Z" stroke-width="1.6"/><rect x="172" y="168" width="36" height="34" stroke-width="1.6"/>'
            + '<path d="M164 202 H216 V210 H164 Z" stroke-width="1.5"/>' + lines("M178 180 H202 M178 190 H202", 0.9)
            + '<path d="M200 214 H230" fill="none" stroke-width="2"/>'
            + '<use href="#dot" transform="translate(218 206) scale(1)" stroke-width="1.3"/>')
    b.append(clip_d(arch_i, view, 1.6, fill="#fff"))
    b.append(lines("M232 74 V470 M388 74 V470 M94 300 H526", 2.4))
    # morning light rays on the glass
    b.append(lines("M420 90 L470 150 M440 84 L500 150 M462 82 L520 146", 1.0))
    # sill with mug and potted herbs
    b.append('<rect x="70" y="466" width="480" height="16" rx="4" stroke-width="2"/>')
    b.append(mug(140, 468, 1.1, "hearts", steam=True))
    b.append(plant("herb", 218, 452, 1.0) + plant_pot(218, 468, 38, 28, "dots"))
    b.append(plant("herb", 270, 452, 0.9) + plant_pot(270, 468, 34, 26, "stripes"))
    # curtains tied back, floral print
    rod = '<rect x="40" y="40" width="540" height="10" rx="5" stroke-width="1.8"/>'
    lc = "M44 50 H150 C140 180 120 300 118 400 C120 430 134 460 150 520 L44 540 Z"
    rc = "M576 50 H470 C480 180 500 300 502 400 C500 430 486 460 470 520 L576 540 Z"
    flowers = "".join(blossom(x, y, 8, 0.9) for x in range(56, 580, 34) for y in range(70, 560, 40) if (x // 34 + y // 40) % 2 == 0)
    b.append(clip_d(lc, lines("M90 60 Q96 260 110 420 M66 60 Q70 300 80 520", 1.0) + flowers, 1.9))
    b.append(clip_d(rc, lines("M530 60 Q524 260 510 420 M554 60 Q550 300 540 520", 1.0) + flowers, 1.9))
    b.append('<path d="M104 392 Q124 384 140 396 Q126 412 106 408 Z M480 396 Q496 384 516 392 L514 408 Q494 412 480 396 Z" stroke-width="1.6"/>')
    b.append(rod)
    # window seat with cushions
    b.append('<path d="M44 540 H576 V600 H44 Z" stroke-width="2"/>')
    b.append(lines("M44 556 H576", 1.2))
    b.append(clip_d("M44 600 H576 V800 H44 Z", lines("M60 618 H200 V740 H60 Z M222 618 H398 V740 H222 Z M420 618 H560 V740 H420 Z", 1.3), 2))
    # knitted throw draped over the seat front
    throw = "M70 548 H300 L292 700 Q250 716 220 700 Q190 690 160 704 Q120 716 80 700 Z"
    zz = " ".join("M40 %d " % y + " ".join(f"L{x} {y + (8 if (x // 16) % 2 else -8)}" for x in range(40, 320, 16)) for y in range(580, 720, 34))
    b.append(clip_d(throw, lines(zz, 1.1), 1.9))
    b.append("".join(f'<path d="M{x} {y} l-3 12 M{x} {y} l3 12" fill="none" stroke-width="1.2"/>' for x, y in ((90, 703), (130, 709), (180, 700), (230, 703), (270, 704))))
    # books stacked on the floor
    for k, (dx, w) in enumerate(((0, 70), (6, 60), (-4, 66))):
        b.append(f'<rect x="{440 + dx}" y="{744 - 13*(k+1)}" width="{w}" height="13" rx="2" stroke-width="1.5"/>')
    b.append(cushion(120, 512, 100, 70, "stripes", -6, tassel=True))
    b.append(cushion(230, 520, 86, 62, "dots", 5))
    b.append(cushion(330, 518, 80, 60, "flower", -4))
    # Miso, curled up with a book, glancing up at the feeder
    mx, my, ms = 448, 600, 2.15
    b.append(char("mi", mx, my, ms, arms=(None, None), sit=True, head_rot=-10))
    b.append(book_open(mx, my - 8, 96, 50))
    b.append(arms_only("mi", mx, my, ms, (-30, 30)))
    return "".join(b)


def svg():
    return page(build(), TITLE)
