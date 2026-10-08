"""Page 1 — Good Morning, Honeyfern Hollow (spring sunrise, establishing shot)."""
from chars import char, arms_only, dot, page, paw
from scene import (blossom, clip_d, daisy, tulip, tuft, cottage_small, ray, stone_grid,
                   picket_fence, scallop_blob, lines, uid)

TITLE = "Page 1 — Good Morning, Honeyfern Hollow"


def build():
    b = []
    # ---- sky: sun, rays, clouds
    sx, sy = 482, 350
    for a in (-70, -47, -23.5, 0, 23.5, 47, 70):
        b.append(ray(sx, sy, a, 54, 84, 6))
    b.append(f'<circle cx="{sx}" cy="{sy}" r="44" stroke-width="1.8"/>')
    b.append('<use href="#cloud" transform="translate(372 112) scale(1.45)" stroke-width="1.15"/>')
    b.append('<use href="#cloud" transform="translate(528 84) scale(0.8)" stroke-width="1.5"/>')
    b.append('<use href="#cloud" transform="translate(296 206) scale(0.62)" stroke-width="1.6"/>')
    # blossoming branch reaching in from the top-left corner
    b.append('<path d="M40 70 C90 62 140 70 196 92 C214 99 226 104 238 104 C224 110 206 106 190 100 C140 82 92 80 40 88 Z" stroke-width="1.8"/>')
    b.append('<path d="M120 76 C132 60 146 52 162 48 C150 58 140 66 128 79 Z" stroke-width="1.5"/>')
    b.append('<path d="M168 92 C176 108 178 122 174 136 C170 122 166 110 158 96 Z" stroke-width="1.5"/>')
    for (x, y, r, rt) in ((70, 64, 11, 10), (96, 92, 10, 40), (134, 66, 9, 0), (162, 46, 10, 20), (176, 138, 10, 30),
                          (204, 86, 11, 15), (238, 104, 9, 5), (150, 104, 8, 50), (56, 98, 8, 20)):
        b.append(blossom(x, y, r, 1.15, rt))
    b.append('<path d="M108 74 Q114 64 122 66 Q118 76 108 74 Z M218 96 Q228 88 236 92 Q228 100 218 96 Z" stroke-width="1.1"/>')
    b.append('<use href="#cloud" transform="translate(520 196) scale(0.85)" stroke-width="1.4"/>')
    b.append('<use href="#cloud" transform="translate(408 238) scale(0.6)" stroke-width="1.6"/>')
    # ---- far hill with the distant cottages, then near hill / lawn
    b.append('<path d="M30 380 C120 360 200 372 262 376 C332 380 402 350 482 350 C532 350 562 358 600 366 L600 800 L30 800 Z" stroke-width="1.6"/>')
    b.append(cottage_small(332, 382, 20))
    b.append(cottage_small(390, 366, 22))
    b.append(cottage_small(556, 366, 18))
    b.append('<path d="M30 470 C150 450 262 482 362 462 C442 448 522 432 600 442 L600 800 L30 800 Z" stroke-width="1.6"/>')
    # tree on the near hill
    b.append('<path d="M507 560 L509 492 L521 492 L523 560 Z" stroke-width="1.5"/>')
    b.append(scallop_blob(515, 470, 44, 38, n=10, bump=0.3, sw=1.7))
    b.append(lines("M500 466 Q510 474 522 468 M512 448 Q520 452 528 446", 0.8))

    # ---- cottage: chimney (behind roof), smoke, wall, roof
    b.append(clip_d("M104 226 H146 V380 H104 Z",
                    stone_grid(104, 226, 42, 154, 15, [[22, 20], [13, 17, 12], [18, 24], [10, 20, 12]], 1.0, 4), 1.8))
    b.append('<rect x="98" y="212" width="54" height="15" rx="3" stroke-width="1.8"/>')
    b.append(scallop_blob(117, 195, 7, 6, n=5, bump=0.35, sw=1.3) + scallop_blob(128, 176, 10, 9, n=6, bump=0.35, sw=1.3)
             + scallop_blob(150, 159, 13, 11, n=7, bump=0.35, sw=1.3) + scallop_blob(182, 148, 17, 13, n=8, bump=0.35, sw=1.3))
    b.append(dot(138, 203.5))  # Dot on the chimney top
    b.append(clip_d("M80 400 H336 V600 H80 Z",
                    '<path d="M80 584 H336" stroke-width="1.2"/>'
                    + "".join(f'<path d="M{x} 584 V600" stroke-width="1"/>' for x in range(110, 336, 34)), 1.8))
    b.append(clip_d("M60 414 L208 262 L356 414 Z",
                    "".join(f'<path d="M40 {y} H380" stroke-width="1.15"/>' for y in (292, 324, 356, 388))
                    + "".join(f'<path d="M{x + (16 if (r % 2) else 0)} {y0} V{y0 + 32}" stroke-width="1"/>'
                              for r, y0 in enumerate((260, 292, 324, 356, 388)) for x in range(70, 370, 32)),
                    2.0))
    b.append('<path d="M54 418 L208 256 L362 418" fill="none" stroke-width="2.4"/>')

    # round kitchen window with open shutters and Bramble inside
    wx, wy = 160, 478
    b.append(clip_d("M116 438 A32 40 0 0 0 116 518 Z", lines("M100 444 V512", 1), 1.6))
    b.append(clip_d("M204 438 A32 40 0 0 1 204 518 Z", lines("M220 444 V512", 1), 1.6))
    b.append('<use href="#heart" transform="translate(101 474) scale(0.85)" stroke-width="1.3"/>')
    b.append('<use href="#heart" transform="translate(219 474) scale(0.85)" stroke-width="1.3"/>')
    b.append(f'<circle cx="{wx}" cy="{wy}" r="38" stroke-width="1.4"/>')
    k = uid("w")
    bx, by, bs = 160, 552.5, 0.55
    b.append(f'<clipPath id="{k}"><circle cx="{wx}" cy="{wy}" r="37.3"/></clipPath>')
    b.append(f'<g clip-path="url(#{k})">'
             + char("br", bx, by, bs, arms=(None, None)) + '</g>')
    b.append(f'<path fill-rule="evenodd" d="M{wx-44} {wy} a44 44 0 1 0 88 0 a44 44 0 1 0 -88 0 Z '
             f'M{wx-38} {wy} a38 38 0 1 0 76 0 a38 38 0 1 0 -76 0 Z" stroke-width="1.9"/>')
    b.append(arms_only("br", bx, by, bs, (106, -106)))
    # window box with tulips
    for tx, lean in ((109, -5), (123, 0), (197, 0), (211, 5)):
        b.append(tulip(tx, 518, 14, lean, 0.9, leaf=False))
    b.append('<rect x="106" y="516" width="108" height="24" rx="3" stroke-width="1.8"/>')
    b.append(lines("M106 528 H214", 1))
    b.append("".join(f'<use href="#heart" transform="translate({hx} 534) scale(0.42)" stroke-width="2"/>' for hx in (128, 160, 192)))

    # round front door
    b.append('<path d="M254 600 V530 A38 38 0 0 1 330 530 V600 Z" stroke-width="1.8"/>')
    b.append(clip_d("M262 600 V530 A30 30 0 0 1 322 530 V600 Z",
                    lines("M277 500 V600 M292 500 V600 M307 500 V600", 1.0), 1.6))
    b.append('<circle cx="292" cy="530" r="10" stroke-width="1.4"/>' + lines("M282 530 H302 M292 520 V540", 0.9))
    b.append('<circle cx="312" cy="568" r="3.4" stroke-width="1.2"/>')
    b.append('<rect x="246" y="598" width="92" height="9" rx="3" stroke-width="1.6"/>')
    # bush at the cottage corner + lantern-free flower clump by the door
    b.append(scallop_blob(68, 584, 30, 22, n=8, bump=0.32, sw=1.6))
    b.append(daisy(58, 580, 9, 6) + daisy(80, 590, 8, 6))
    for tx, lean, h in ((342, -3, 22), (352, 2, 28)):
        b.append(tulip(tx, 606, h, lean, 0.9))

    # stepping-stone path from bottom right up to the door
    for (cx, cy, rx, ry) in ((512, 744, 30, 9), (496, 716, 27, 8.5), (466, 686, 24, 7.5),
                             (398, 660, 23, 7.5), (362, 636, 19, 7), (334, 620, 16, 6), (310, 609, 13, 5)):
        b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" stroke-width="1.5"/>')
    # lawn details
    for (x, y, s) in ((440, 602, 1), (560, 640, 1), (118, 640, 1.1), (210, 666, 1), (300, 650, 0.9), (520, 560, 0.9)):
        b.append(tuft(x, y, s))
    b.append(daisy(484, 618, 11) + daisy(558, 690, 10) + daisy(166, 660, 10) + daisy(258, 640, 9))

    # Clover arriving with her basket
    cx, cy = 398, 658
    b.append(char("cl", cx, cy, 1.0, arms=(150, -14), head_rot=-6))
    px, py = paw("cl", cx, cy, 1.0, "R", -14)
    ry0 = py + 12
    b.append(f'<g transform="translate({px} {ry0})">'
             + lines("M10 0 Q14 -12 18 -22 M16 0 Q24 -8 30 -14", 1.1)
             + daisy(18, -24, 8, 6, 1) + daisy(31, -16, 8, 6, 1)
             + '<ellipse cx="-11" cy="-3" rx="6" ry="8" stroke-width="1.2"/><ellipse cx="0" cy="-2" rx="5.5" ry="7.5" stroke-width="1.2"/>'
             + clip_d("M-24 0 H24 L20 26 Q0 30 -20 26 Z",
                      lines("M-28 9 H28 M-28 18 H28", 1) + lines("M-8 0 V30 M8 0 V30", 1), 1.6)
             + '<path d="M-22 1 Q0 -30 22 1" fill="none" stroke-width="2.6"/>'
             + '</g>')
    # redraw Clover's right paw over the handle so the grip reads
    b.append(f'<g transform="translate({cx} {cy})" stroke-width="2"><use href="#cl-arm" transform="translate(24 -54) rotate(-14)"/></g>')

    # foreground picket fence, gate posts and birdhouse mailbox
    b.append(picket_fence(56, 446, 702, 760, pw=16, gap=12))
    b.append('<rect x="452" y="706" width="14" height="60" stroke-width="1.8"/><circle cx="459" cy="701" r="5.5" stroke-width="1.6"/>')
    b.append('<rect x="540" y="664" width="14" height="100" stroke-width="1.8"/>')
    b.append('<rect x="526" y="630" width="42" height="34" rx="2" stroke-width="1.8"/>')
    b.append('<path d="M520 632 L547 608 L574 632 Z" stroke-width="1.8"/>')
    b.append('<circle cx="547" cy="646" r="7" stroke-width="1.5"/>')
    b.append('<rect x="543" y="657" width="8" height="4" rx="1.5" stroke-width="1"/>')
    return "".join(b)


def svg():
    return page(build(), TITLE)
