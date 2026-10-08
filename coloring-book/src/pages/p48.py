"""Page 48 — Moonlit Room (Tofu asleep under the Book Loft's round window)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import star, plant, plant_pot, book_closed

TITLE = "Page 48 — Moonlit Room"
WX, WY, WR = 306, 210, 150


def build():
    b = []
    # wall and floor
    b.append(clip_d("M30 30 H600 V600 H30 Z", lines(" ".join(f"M{x} 30 V600" for x in range(64, 600, 46)), 0.8), 1.4))
    b.append(clip_d("M30 600 H600 V800 H30 Z", lines("M30 650 H600 M30 710 H600", 1), 1.6))
    # round window with the full moon and stars, curtains drawn back
    b.append(f'<circle cx="{WX}" cy="{WY}" r="{WR + 14}" stroke-width="2.4"/>')
    sky = (f'<circle cx="{WX + 20}" cy="{WY - 10}" r="70" stroke-width="2"/><circle cx="{WX}" cy="{WY - 30}" r="14" stroke-width="1.3"/>'
           f'<circle cx="{WX + 50}" cy="{WY + 20}" r="10" stroke-width="1.3"/><circle cx="{WX + 36}" cy="{WY - 44}" r="7" stroke-width="1.2"/><circle cx="{WX - 10}" cy="{WY + 26}" r="8" stroke-width="1.2"/>'
           + star(WX - 100, WY - 60, 1.3) + star(WX - 90, WY + 70, 1.0, 4) + star(WX + 110, WY - 80, 1.0, 4) + star(WX + 120, WY + 80, 1.2)
           + star(WX - 40, WY - 120, 0.8) + star(WX - 120, WY + 10, 0.8, 4))
    b.append(clip_d(f"M{WX - WR} {WY} A{WR} {WR} 0 1 0 {WX + WR} {WY} A{WR} {WR} 0 1 0 {WX - WR} {WY} Z", sky, 1.6, fill="#fff"))
    for side in (-1, 1):
        x0 = WX + side * (WR + 40)
        d = f"M{x0} 40 H{x0 - side*60} Q{x0 - side*20} 200 {x0 - side*30} 300 Q{x0 - side*44} 350 {x0} 380 Z"
        b.append(clip_d(d, lines(" ".join(f"M{x0 - side*k*12} 40 Q{x0 - side*k*8} 200 {x0 - side*k*10} 380" for k in range(1, 5)), 1), 2))
    b.append('<rect x="100" y="36" width="412" height="10" rx="5" stroke-width="1.8"/>')
    # low shelves on both sides
    for x0 in (30, 470):
        b.append(f'<rect x="{x0}" y="420" width="130" height="180" stroke-width="2"/>' + lines(f"M{x0} 480 H{x0 + 130} M{x0} 540 H{x0 + 130}", 1.8))
        for row, y in enumerate((420, 480, 540)):
            xx = x0 + 8
            for k, w in enumerate((12, 16, 10, 14, 12)):
                if (row + k) % 4 == 3:
                    xx += w + 4
                    continue
                b.append(f'<rect x="{xx}" y="{y + 10 + (k % 2) * 4}" width="{w}" height="{48 - (k % 2) * 4}" rx="1" stroke-width="1.1"/>')
                xx += w + 3
    b.append(plant("fern", 96, 410, 0.7) + plant_pot(96, 420, 40, 30, "dots"))
    # nightstand with a candle-style lamp and a closed book
    b.append('<rect x="470" y="370" width="110" height="10" rx="2" stroke-width="1.7"/>')
    b.append(book_closed(510, 362, 56, 12) + '<rect x="546" y="320" width="14" height="44" rx="3" stroke-width="1.6"/>'
             '<path d="M553 320 Q546 308 553 296 Q560 308 553 320 Z" stroke-width="1.3"/><ellipse cx="553" cy="366" rx="14" ry="4" stroke-width="1.4"/>')
    # the bed: Tofu asleep, moon pendant on his chest; puffy diamond-stitched duvet, knit throw
    b.append('<rect x="140" y="380" width="330" height="40" rx="12" stroke-width="2.2"/>')
    b.append('<path d="M180 460 Q170 400 230 400 H380 Q440 400 430 460 Z" stroke-width="1.9"/>')
    b.append(char("to", 306, 526, 1.15, arms=(None, None), mood="sleep"))
    duvet = "M120 520 Q306 490 492 520 L510 690 Q306 714 102 690 Z"
    diam = " ".join(f"M{x} 480 L{x + 220} 720 M{x + 220} 480 L{x} 720" for x in range(-200, 600, 44))
    b.append(clip_d(duvet, lines(diam, 0.9) + "".join(f'<circle cx="{x}" cy="{y}" r="2" stroke-width="0.8"/>' for x in range(130, 500, 44) for y in (542, 586, 630, 674)), 2.2))
    throw = "M120 640 Q306 618 492 640 L506 700 Q306 724 106 700 Z"
    b.append(clip_d(throw, lines(" ".join("M100 %d " % y + " ".join(f"L{x} {y + (6 if (x // 12) % 2 else -6)}" for x in range(100, 520, 12)) for y in range(650, 720, 18)), 1), 2))
    b.append(arms_only("to", 306, 526, 1.15, (-30, 30)))
    b.append('<path d="M100 690 H512 V760 H100 Z" stroke-width="2"/>' + lines("M100 712 H512", 1.2))
    # sleeping cat-shaped pillow and slippers
    b.append('<path d="M392 470 Q384 440 420 436 Q456 440 452 470 Z" stroke-width="1.7"/><path d="M398 446 L396 428 L408 440 Z M446 446 L448 428 L436 440 Z" stroke-width="1.5"/>'
             + lines("M408 456 q4 3 8 0 M428 456 q4 3 8 0 M420 462 v3", 1))
    b.append('<path d="M520 740 Q520 718 542 718 Q562 718 562 740 Z M568 742 Q568 722 586 722 L586 742 Z" stroke-width="1.6"/>')
    # hanging mobile of moons and stars from the upper left (Dot asleep on its top bar)
    b.append(lines("M120 50 V90 M70 90 H170 M76 90 V140 M120 90 V120 M164 90 V150", 1.3))
    b.append('<rect x="66" y="86" width="108" height="7" rx="3" stroke-width="1.5"/>')
    b.append('<use href="#crescent" transform="translate(76 150) scale(1.5)" stroke-width="1"/>' + star(120, 130, 1.0) + star(164, 160, 0.9, 4))
    b.append(dot(140, 76.5, 0.85, sleep=True))
    return "".join(b)


def svg():
    return page(build(), TITLE)
