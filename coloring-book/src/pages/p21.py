"""Page 21 — Painting the Hollow (over-the-shoulder on Lantern Hill)."""
from chars import char, dot, page, paw
from scene import clip_d, daisy, tuft, cottage_small, lines, pine, scallop_blob

TITLE = "Page 21 — Painting the Hollow"


def build():
    b = []
    # sky
    b.append('<use href="#cloud" transform="translate(236 96) scale(1.35)" stroke-width="1.2"/>')
    b.append('<use href="#cloud" transform="translate(330 176) scale(0.9)" stroke-width="1.4"/>')
    b.append('<use href="#cloud" transform="translate(540 182) scale(0.6)" stroke-width="1.8"/>')
    b.append('<circle cx="470" cy="96" r="26" stroke-width="1.6"/>')
    b.append(lines("M470 56 V64 M470 128 V136 M430 96 H438 M502 96 H510 M442 68 l6 6 M492 118 l6 6 M498 68 l-6 6 M448 118 l-6 6", 1.4))
    # far hills, then the valley of patchwork fields
    b.append('<path d="M30 262 C120 236 220 252 300 248 C380 244 460 226 600 238 L600 800 L30 800 Z" stroke-width="1.5"/>')
    valley = "M30 318 C150 306 250 326 360 318 C450 312 520 296 600 304 L600 800 L30 800 Z"
    fields = lines("M30 370 C160 360 300 378 600 352 M30 420 C200 410 340 430 600 402 M30 474 C200 462 360 482 600 452 M30 526 C200 516 360 534 600 506 "
                   "M120 314 L104 560 M230 322 L250 560 M330 320 L300 560 M420 314 L452 560 M510 300 L520 560 M180 320 L170 372 M470 308 L478 358", 1.2)
    fields += lines("M140 384 Q160 388 180 384 M140 396 Q160 400 180 396 M260 440 Q280 444 300 440 M260 452 Q280 456 300 452 M40 440 Q60 444 80 440 M40 452 Q60 456 80 452", 0.8)
    b.append(clip_d(valley, fields, 1.5))
    # winding river with the Hollow's cottages along it
    b.append('<path d="M474 306 C466 340 410 350 420 390 C432 436 520 430 520 480 C520 520 470 540 480 600 L566 600 '
             'C552 546 594 520 588 476 C582 424 482 426 474 388 C468 362 494 340 488 306 Z" stroke-width="1.5"/>')
    b.append(lines("M500 450 q8 -3 16 0 M532 500 q8 -3 16 0 M440 380 q6 -2 12 0", 0.9))
    for (x, y, w) in ((402, 366, 18), (384, 388, 16), (440, 340, 14), (548, 420, 18), (570, 444, 16),
                      (456, 452, 18), (486, 500, 16), (372, 424, 14), (520, 330, 12), (560, 368, 14)):
        b.append(cottage_small(x, y, w))
    # lone pine of Lantern Hill
    b.append('<rect x="92" y="420" width="15" height="170" stroke-width="1.7"/>')
    b.append(pine(99, [(118, 196, 32), (160, 256, 48), (210, 320, 62), (268, 392, 76), (330, 460, 88)], 1.7))
    b.append(lines("M88 176 l5 6 l5 -6 M108 226 l5 6 l5 -6 M72 236 l5 6 l5 -6 M96 290 l5 6 l5 -6 M60 300 l5 6 l5 -6 M120 296 l5 6 l5 -6 "
                   "M80 360 l5 6 l5 -6 M128 364 l5 6 l5 -6 M56 430 l5 6 l5 -6 M100 428 l5 6 l5 -6 M140 432 l5 6 l5 -6", 1))
    # grassy hilltop in the foreground
    b.append('<path d="M30 566 C140 552 260 560 360 574 C440 584 520 602 600 598 L600 800 L30 800 Z" stroke-width="1.8"/>')
    for (x, y, s) in ((270, 620, 1), (360, 650, 1.1), (560, 640, 1), (300, 690, 1), (460, 610, 0.9), (70, 640, 1)):
        b.append(tuft(x, y, s))
    b.append(daisy(250, 650, 11) + daisy(560, 700, 12) + daisy(330, 616, 9))

    # easel with the canvas (the same view in simple outline)
    b.append('<path d="M354 346 L360 346 L366 692 L358 692 Z" stroke-width="1.5"/>')
    b.append('<path d="M352 344 L362 344 L302 702 L292 700 Z" stroke-width="1.8"/>')
    b.append('<path d="M352 344 L362 344 L424 700 L414 702 Z" stroke-width="1.8"/>')
    b.append('<rect x="248" y="528" width="218" height="13" rx="3" stroke-width="1.8"/>')
    cv = "M262 384 H452 V528 H262 Z"
    mini = (lines("M262 470 C300 456 340 466 380 460 C410 456 430 448 452 452", 1.2)
            + '<circle cx="420" cy="414" r="11" stroke-width="1.2"/>'
            + '<path d="M410 462 C404 476 388 482 396 496 C404 508 430 506 430 528 L448 528 C444 506 418 500 414 490 C410 480 426 474 420 462 Z" stroke-width="1.1"/>'
            + '<path d="M290 470 L298 424 L306 470 Z" stroke-width="1.1"/>'
            + cottage_small(352, 490, 14) + cottage_small(374, 500, 12) + cottage_small(330, 504, 12)
            + '<use href="#cloud" transform="translate(320 408) scale(0.45)" stroke-width="2.4"/>')
    b.append(clip_d(cv, mini, 2.2, fill="#fff"))
    b.append(lines("M262 484 C300 478 340 486 370 482", 0.9))
    b.append('<rect x="348" y="368" width="18" height="22" rx="3" stroke-width="1.6"/>')
    b.append(dot(358, 336))  # Dot perched on the easel's top edge

    # Juniper, seen from behind, brush raised to the canvas
    jx, jy, js = 170, 748, 1.7
    b.append(char("ju", jx, jy, js, arms=(14, -146), back=True))
    px, py = paw("ju", jx, jy, js, "R", -146)
    b.append(f'<path d="M{px-3:.1f} {py+2:.1f} L{px+42:.1f} {py-58:.1f} L{px+47:.1f} {py-55:.1f} L{px+3:.1f} {py+5:.1f} Z" stroke-width="1.4"/>')
    b.append(f'<path d="M{px+41:.1f} {py-58:.1f} L{px+48:.1f} {py-54:.1f} L{px+53:.1f} {py-63:.1f} L{px+46:.1f} {py-67:.1f} Z" stroke-width="1.3"/>')
    b.append(f'<path d="M{px+46:.1f} {py-67:.1f} L{px+53:.1f} {py-63:.1f} Q{px+58:.1f} {py-76:.1f} {px+56:.1f} {py-82:.1f} Q{px+47:.1f} {py-78:.1f} {px+46:.1f} {py-67:.1f} Z" stroke-width="1.3"/>')
    b.append(f'<g transform="translate({jx} {jy}) scale({js})" stroke-width="{2/js:.3f}"><use href="#ju-arm" transform="translate(23 -68) rotate(-146)"/></g>')

    # paint box with Thimble mixing colours on the palette
    b.append('<rect x="398" y="652" width="104" height="46" rx="4" stroke-width="1.9"/>')
    b.append(lines("M398 666 H502", 1.2))
    b.append('<rect x="444" y="660" width="12" height="12" rx="2" stroke-width="1.2"/>')
    b.append('<path d="M452 652 C452 630 486 622 500 632 C512 640 506 652 496 652 Z" stroke-width="1.7"/>')
    b.append('<ellipse cx="478" cy="644" rx="5" ry="3.5" stroke-width="1"/>')
    for (x, y, r) in ((462, 642, 5), (470, 632, 4.5), (484, 630, 5), (496, 638, 4.5)):
        b.append(f'<path d="M{x-r} {y} Q{x-r} {y-r} {x} {y-r} Q{x+r} {y-r} {x+r} {y} Q{x+r*0.6} {y+r} {x} {y+r*0.8} Q{x-r*0.8} {y+r} {x-r} {y} Z" stroke-width="1"/>')
    tx, ty, ts = 424, 654, 1.7
    b.append(char("th", tx, ty, ts, arms=(18, -64), sit=True, mood="happy"))
    qx, qy = paw("th", tx, ty, ts, "R", -64)
    b.append(lines(f"M{qx:.1f} {qy:.1f} L{qx+20:.1f} {qy+4:.1f}", 1.6))
    # brushes in a jar
    b.append(lines("M520 662 L512 612 M528 662 L530 604 M536 662 L548 616", 1.6))
    b.append('<path d="M510 612 l-3 -12 l6 0 Z M528 604 l0 -12 l5 0 Z M548 616 l3 -12 l4 3 Z" stroke-width="1.1"/>')
    b.append('<path d="M512 656 H546 L544 700 Q529 704 514 700 Z" stroke-width="1.8"/>')
    b.append(lines("M513 670 H545", 1))
    # paint tubes, satchel and straw sun hat on the grass
    b.append('<path d="M364 718 L398 712 L400 724 L366 730 Q360 724 364 718 Z" stroke-width="1.4"/><rect x="398" y="713" width="8" height="10" rx="2" transform="rotate(-9 402 718)" stroke-width="1.2"/>')
    b.append('<path d="M372 744 L406 742 L407 754 L373 756 Q367 750 372 744 Z" stroke-width="1.4"/>')
    b.append('<rect x="290" y="700" width="70" height="52" rx="10" stroke-width="1.9"/>')
    b.append('<path d="M290 712 Q325 732 360 712 L360 704 Q325 690 290 704 Z" stroke-width="1.5"/>')
    b.append('<rect x="318" y="716" width="14" height="10" rx="2" stroke-width="1.2"/>')
    b.append('<ellipse cx="502" cy="738" rx="46" ry="12" stroke-width="1.9"/>')
    b.append('<path d="M476 736 Q478 708 502 708 Q526 708 528 736 Z" stroke-width="1.8"/>')
    b.append('<path d="M477 728 Q502 734 527 728 L527 736 Q502 742 477 736 Z" stroke-width="1.3"/>')
    return "".join(b)


def svg():
    return page(build(), TITLE)
