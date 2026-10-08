"""Page 8 — The Book Loft (Tofu in the wingback chair, Thimble on the armrest)."""
import random
from chars import char, arms_only, dot, page
from scene import clip_d, lines, uid

TITLE = "Page 8 — The Book Loft"

CX = 330            # room corner
FLOOR_C = 470       # floor line height at the corner


def yL(x, c):
    """Left wall: y of a horizontal line that sits at height c on the corner."""
    edge = 20 + (c - 50) * 1.286
    t = (CX - x) / (CX - 45)
    return c + (edge - c) * t


def yR(x, c):
    edge = 25 + (c - 50) * 1.238
    t = (x - CX) / (576 - CX)
    return c + (edge - c) * t


def board(fy, xa, xb, c, t=7):
    a1, b1 = fy(xa, c), fy(xb, c)
    k = 1.25 if xa < CX else 1.2
    return (f'<path d="M{xa} {a1:.1f} L{xb} {b1:.1f} L{xb} {b1 + t*(k if xb in (45, 576) else 1):.1f} '
            f'L{xa} {a1 + t*(k if xa in (45, 576) else 1):.1f} Z" stroke-width="1.4"/>')


def books(fy, xa, xb, c_top, c_bot, seed, gap_end=0.0, lean=True):
    """Books standing on the board at c_bot, under the board at c_top."""
    rnd = random.Random(seed)
    out = []
    x = xa + 3
    end = xb - 3 - (xb - xa) * gap_end
    leaned = False
    while x < end - 8:
        w = rnd.choice((11, 12, 13, 14, 15, 16, 18))
        x2 = min(x + w, end)
        if x2 - x < 8:
            break
        bh1 = (fy(x, c_bot) - fy(x, c_top) - 8) * rnd.uniform(0.62, 0.9)
        f = bh1 / (fy(x, c_bot) - fy(x, c_top))
        bh2 = (fy(x2, c_bot) - fy(x2, c_top)) * f
        y1, y2 = fy(x, c_bot), fy(x2, c_bot)
        if lean and not leaned and rnd.random() < 0.22 and x2 + 22 < end:
            # one leaning book per bay
            leaned = True
            out.append(f'<path d="M{x:.1f} {y1:.1f} L{x + 14:.1f} {y1 - bh1*0.95:.1f} L{x + 14 + w:.1f} {y1 - bh1*0.95 + 3:.1f} '
                       f'L{x + w + 2:.1f} {y2:.1f} Z" stroke-width="1.2"/>')
            x = x + w + 6
            continue
        out.append(f'<path d="M{x:.1f} {y1:.1f} V{y1 - bh1:.1f} L{x2:.1f} {y2 - bh2:.1f} V{y2:.1f} Z" stroke-width="1.2"/>')
        style = rnd.random()
        if style < 0.45:
            out.append(lines(f"M{x:.1f} {y1 - bh1*0.18:.1f} L{x2:.1f} {y2 - bh2*0.18:.1f} "
                             f"M{x:.1f} {y1 - bh1*0.82:.1f} L{x2:.1f} {y2 - bh2*0.82:.1f}", 0.75))
        elif style < 0.7:
            cxm, cym = (x + x2) / 2, (y1 + y2) / 2 - bh1 * 0.5
            out.append(f'<ellipse cx="{cxm:.1f}" cy="{cym:.1f}" rx="{(x2 - x)*0.26:.1f}" ry="{(x2-x)*0.3:.1f}" stroke-width="0.75"/>')
        x = x2
    return "".join(out)


def build():
    b = []
    # ---------- shelving: uprights and boards on both walls
    levels = [50, 120, 210, 300, 390]
    left_up = [45, 140, 235, CX]
    right_up = [CX, 420, 500, 576]
    # books, bay by bay (row r spans levels[r] .. levels[r+1])
    seed = 3
    for r in range(4):
        ct, cb = levels[r], levels[r + 1]
        for i in range(3):
            xa, xb = left_up[i], left_up[i + 1]
            if i == 1 and r < 2:
                continue  # round window lives here
            gap = 0.42 if (i == 0 and r == 1) else 0.0
            b.append(books(yL, xa + 4, xb - 4, ct, cb, seed, gap)); seed += 1
            xa, xb = right_up[i], right_up[i + 1]
            gap = 0.5 if (i == 0 and r == 2) else 0.0
            b.append(books(yR, xa + 4, xb - 4, ct, cb, seed, gap)); seed += 1
    for r, c in enumerate(levels[1:]):
        for i in range(3):
            if not (i == 1 and r == 0):
                b.append(board(yL, left_up[i], left_up[i + 1], c))
            b.append(board(yR, right_up[i], right_up[i + 1], c))
    # base cupboards between the last board and the floor
    for i in range(3):
        xa, xb = left_up[i], left_up[i + 1]
        b.append(f'<path d="M{xa+6} {yL(xa+6, 398):.1f} L{xb-6} {yL(xb-6, 398):.1f} L{xb-6} {yL(xb-6, 462):.1f} L{xa+6} {yL(xa+6, 462):.1f} Z" stroke-width="1.2"/>')
        b.append(f'<circle cx="{(xa+xb)/2:.1f}" cy="{yL((xa+xb)/2, 430):.1f}" r="3" stroke-width="1"/>')
        xa, xb = right_up[i], right_up[i + 1]
        b.append(f'<path d="M{xa+6} {yR(xa+6, 398):.1f} L{xb-6} {yR(xb-6, 398):.1f} L{xb-6} {yR(xb-6, 462):.1f} L{xa+6} {yR(xa+6, 462):.1f} Z" stroke-width="1.2"/>')
        b.append(f'<circle cx="{(xa+xb)/2:.1f}" cy="{yR((xa+xb)/2, 430):.1f}" r="3" stroke-width="1"/>')
    for x in left_up:
        b.append(f'<path d="M{x-4} 0 H{x+4} V{yL(x, FLOOR_C)+2:.1f} H{x-4} Z" stroke-width="1.5"/>')
    for x in right_up[1:]:
        b.append(f'<path d="M{x-4} 0 H{x+4} V{yR(x, FLOOR_C)+2:.1f} H{x-4} Z" stroke-width="1.5"/>')
    b.append(lines(f"M{CX} 0 V{FLOOR_C}", 1.8))

    # cat-shaped bookend at the gap in the top-left bay; globe in the right corner bay
    cbx, cby = 118, yL(118, 210)
    b.append(f'<g transform="translate({cbx} {cby})" stroke-width="1.3">'
             '<path d="M-16 0 C-18 -14 -6 -22 6 -20 C14 -18 18 -10 16 0 Z"/>'
             '<path d="M14 0 C22 -2 24 -8 20 -12 C18 -8 16 -4 10 -2 Z"/>'
             '<path d="M-14 -10 L-18 -22 L-8 -16 Z M-6 -18 L-4 -28 L2 -18 Z" />'
             '<circle cx="-10" cy="-12" r="9"/>'
             '<path d="M-16 -22 L-17 -30 L-11 -21 Z M-6 -21 L-3 -29 L-2 -18 Z"/>'
             '<path d="M-14 -12 Q-12.5 -10.5 -11 -12 M-9 -12 Q-7.5 -10.5 -6 -12" fill="none" stroke-width="0.8"/></g>')
    gx, gy = 372, yR(372, 300)
    b.append(f'<g transform="translate({gx} {gy})" stroke-width="1.3">'
             '<path d="M-12 0 H12 L8 -5 H-8 Z"/><path d="M0 -5 V-10" fill="none"/>'
             '<path d="M-17 -30 A19 19 0 0 0 10 -12" fill="none" stroke-width="1.6"/>'
             '<circle cx="-4" cy="-26" r="15"/>'
             '<path d="M-19 -26 H11 M-4 -41 Q-14 -26 -4 -11 M-4 -41 Q6 -26 -4 -11" fill="none" stroke-width="0.8"/>'
             '<path d="M-12 -34 Q-6 -36 -4 -30 Q-10 -28 -12 -34 Z M0 -22 Q6 -24 6 -18 Q2 -16 0 -22 Z" stroke-width="0.8"/></g>')

    # round loft window in the middle bay of the left wall
    wx, wy = 188, 128
    b.append(f'<ellipse cx="{wx}" cy="{wy}" rx="44" ry="62" stroke-width="2"/>')
    b.append(f'<ellipse cx="{wx}" cy="{wy}" rx="36" ry="52" stroke-width="1.5"/>')
    b.append(clip_d(f"M{wx-36} {wy} A36 52 0 1 0 {wx+36} {wy} A36 52 0 1 0 {wx-36} {wy} Z",
                    '<use href="#cloud" transform="translate(178 104) scale(0.42)" stroke-width="2.6"/>'
                    '<use href="#cloud" transform="translate(206 150) scale(0.32)" stroke-width="3.2"/>'
                    + lines(f"M{wx} {wy-60} V{wy+60} M{wx-40} {wy} H{wx+40}", 2.4), 1.5, fill="#fff"))
    b.append(f'<path d="M{wx-48} {wy+66} Q{wx} {wy+70} {wx+48} {wy+62} L{wx+48} {wy+70} Q{wx} {wy+78} {wx-48} {wy+74} Z" stroke-width="1.5"/>')

    # ---------- floor, boards and rug
    fl = f"M45 {yL(45, FLOOR_C):.1f} L{CX} {FLOOR_C} L576 {yR(576, FLOOR_C):.1f} L576 760 L45 760 Z"
    fb = ""
    for k in range(1, 10):
        t = k * 0.115
        px, py = CX - 285 * t, FLOOR_C + 90 * t
        fb += f"M{px:.1f} {py:.1f} L{px + 400:.1f} {py + 122:.1f} "
        if k % 2 == 0:
            fb += f"M{px + 120 + 30*k % 90:.1f} {py + 36.6 + (30*k % 90)*0.305:.1f} l-6 18 "
    b.append(clip_d(fl, lines(fb, 1.0), 1.6))
    b.append('<ellipse cx="226" cy="676" rx="178" ry="50" stroke-width="1.6"/>')
    b.append('<ellipse cx="226" cy="676" rx="146" ry="38" stroke-width="1.2"/>')
    b.append('<ellipse cx="226" cy="676" rx="110" ry="26" stroke-width="1"/>')

    # ---------- floor lamp with a fringed shade
    b.append('<ellipse cx="78" cy="692" rx="22" ry="6" stroke-width="1.6"/>')
    b.append('<rect x="75" y="404" width="7" height="286" stroke-width="1.5"/>')
    b.append('<path d="M48 408 L60 362 H100 L112 408 Z" stroke-width="1.8"/>')
    b.append(lines("M54 386 H106", 1))
    b.append("".join(f'<path d="M{x} 408 a5 5 0 0 0 10 0" stroke-width="1.1"/>' for x in range(50, 110, 10)))

    # ---------- wingback chair, Tofu, Thimble
    tuft = ""
    for k in range(-6, 7):
        tuft += f"M{220 + k*26 - 80} 360 L{220 + k*26 + 80} 520 M{220 + k*26 + 80} 360 L{220 + k*26 - 80} 520 "
    b.append(clip_d("M140 610 V470 C140 400 160 380 220 376 C280 380 300 400 300 470 V610 Z", lines(tuft, 0.9), 2.0))
    b.append("".join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#000" stroke="none"/>' for (x, y) in
                     ((194, 400), (246, 400), (168, 426), (220, 426), (272, 426))))
    b.append('<path d="M144 404 C118 412 106 444 110 484 L114 552 L146 552 Z" stroke-width="1.9"/>')
    b.append('<path d="M296 404 C322 412 334 444 330 484 L326 552 L294 552 Z" stroke-width="1.9"/>')
    b.append('<path d="M150 598 Q220 590 290 598 L290 626 Q220 632 150 626 Z" stroke-width="1.8"/>')
    tx, ty, ts = 220, 596, 1.0
    b.append(char("to", tx, ty, ts, arms=(None, None), sit=True))
    # thick open book on Tofu's lap
    b.append('<path d="M164 566 L164 608 Q194 602 220 613 Q246 602 276 608 L276 566 Z" stroke-width="1.8"/>')
    b.append('<path d="M220 567 Q196 557 170 562 L170 602 Q196 597 220 606 Z" stroke-width="1.6"/>')
    b.append('<path d="M220 567 Q244 557 270 562 L270 602 Q244 597 220 606 Z" stroke-width="1.6"/>')
    b.append(lines("M178 572 Q196 567 212 573 M178 581 Q196 576 212 582 M178 590 Q196 585 212 591 "
                   "M228 573 Q244 567 262 572 M228 582 Q244 576 262 581 M228 591 Q244 585 262 590", 0.75))
    b.append(arms_only("to", tx, ty, ts, (-9, 9)))
    # armrests in front
    b.append('<path d="M104 646 V562 C104 542 118 534 132 536 C146 538 152 548 150 562 V646 Z" stroke-width="2"/>')
    b.append('<circle cx="127" cy="558" r="11" stroke-width="1.5"/>' + lines("M127 553 a5 5 0 1 1 -4 6", 1))
    b.append('<path d="M290 646 V562 C290 548 296 538 310 536 C324 534 336 542 336 562 V646 Z" stroke-width="2"/>')
    b.append('<circle cx="313" cy="558" r="11" stroke-width="1.5"/>' + lines("M313 553 a5 5 0 1 0 4 6", 1))
    b.append('<path d="M100 640 H340 V664 Q220 672 100 664 Z" stroke-width="2"/>')
    b.append(lines("M140 642 V667 M180 642 V669 M220 642 V670 M260 642 V669 M300 642 V667", 1))
    b.append('<path d="M110 664 H124 L122 682 H112 Z M316 664 H330 L328 682 H318 Z" stroke-width="1.6"/>')
    # Thimble on the right armrest with a matchbook-sized book
    hx, hy = 313, 538
    b.append(char("th", hx, hy, 1.0, arms=(None, None)))
    b.append('<path d="M313 520 Q306 517 302 519 V530 Q306 528 313 531 Z" stroke-width="1"/>'
             '<path d="M313 520 Q320 517 324 519 V530 Q320 528 313 531 Z" stroke-width="1"/>')
    b.append(arms_only("th", hx, hy, 1.0, (-60, 60)))

    # ---------- side table with teacup and two small books
    b.append('<path d="M372 616 L369 680 H387 L384 616 Z" stroke-width="1.6"/>')
    b.append('<ellipse cx="378" cy="684" rx="22" ry="5.5" stroke-width="1.5"/>')
    b.append('<ellipse cx="378" cy="610" rx="36" ry="10" stroke-width="1.8"/>')
    b.append('<rect x="384" y="594" width="30" height="8" rx="1.5" stroke-width="1.2"/><rect x="387" y="586" width="25" height="8" rx="1.5" stroke-width="1.2"/>')
    b.append('<ellipse cx="364" cy="606" rx="16" ry="4.5" stroke-width="1.3"/>')
    b.append('<ellipse cx="376" cy="597" rx="5" ry="4.5" stroke-width="1.3"/>')
    b.append('<path d="M354 588 H374 Q374 604 364 604 Q354 604 354 588 Z" stroke-width="1.4"/>')
    b.append(lines("M360 582 q-4 -5 0 -10 q4 -5 0 -10 M368 582 q-4 -5 0 -10", 1))

    # ---------- rolling library ladder on the right wall, with Dot on top
    b.append('<path d="M330 92 H600 V100 H330 Z" stroke-width="1.5"/>')
    for (x1, y1, x2, y2) in ((444, 728, 490, 84), (512, 734, 556, 84)):
        b.append(f'<path d="M{x1-5} {y1} L{x2-4} {y2} Q{x2} {y2-6} {x2+4} {y2} L{x1+5} {y1} Z" stroke-width="1.9"/>')
    for k in range(1, 12):
        t = k / 12
        lx, ly = 444 + (490 - 444) * t, 728 + (84 - 728) * t
        rx, ry = 512 + (556 - 512) * t, 734 + (84 - 734) * t
        b.append(f'<path d="M{lx+4:.1f} {ly-3:.1f} L{rx-4:.1f} {ry-3:.1f} L{rx-4:.1f} {ry+4:.1f} L{lx+4:.1f} {ly+4:.1f} Z" stroke-width="1.3"/>')
    b.append('<circle cx="444" cy="736" r="9" stroke-width="1.6"/><circle cx="444" cy="736" r="3" stroke-width="1"/>')
    b.append('<circle cx="512" cy="742" r="9" stroke-width="1.6"/><circle cx="512" cy="742" r="3" stroke-width="1"/>')
    b.append(dot(553, 72))

    # ---------- stacks of books on the floor
    def stack(x, y, specs):
        out = ""
        for (dx, w, h) in specs:
            out += f'<rect x="{x+dx}" y="{y-h}" width="{w}" height="{h}" rx="2" stroke-width="1.5"/>'
            out += lines(f"M{x+dx+w-8} {y-h+2} V{y-2}", 0.8)
            y -= h
        return out
    b.append(stack(56, 748, ((0, 86, 13), (6, 74, 12), (-2, 80, 14), (8, 64, 11), (14, 52, 12))))
    b.append(stack(350, 750, ((0, 76, 13), (8, 62, 12), (2, 70, 11))))
    return "".join(b)


def svg():
    return page(build(), TITLE)
