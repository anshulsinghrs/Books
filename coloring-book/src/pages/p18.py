"""Page 18 — Rain on the Round Window (Tofu in the hanging egg chair)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import teapot, teacup, plant, plant_pot, book_closed, book_open

TITLE = "Page 18 — Rain on the Round Window"
WX, WY, WR = 352, 236, 176


def rooftops():
    out = ""
    for (x, w, h, roof) in ((180, 70, 60, 34), (250, 60, 46, 28), (330, 84, 70, 40), (420, 64, 52, 30), (488, 80, 62, 36)):
        y = 400 - h
        out += (f'<rect x="{x}" y="{y}" width="{w}" height="{h + 20}" stroke-width="1.3"/>'
                f'<path d="M{x - 6} {y + 2} L{x + w/2} {y - roof} L{x + w + 6} {y + 2} Z" stroke-width="1.3"/>'
                f'<rect x="{x + w*0.35:.0f}" y="{y + 14}" width="{w*0.3:.0f}" height="16" stroke-width="1.1"/>')
    return out


def build():
    b = []
    # wall planks and floor
    b.append(clip_d("M30 30 H600 V620 H30 Z", lines(" ".join(f"M{x} 30 V620" for x in range(70, 600, 48)), 0.9), 1.4))
    b.append(clip_d("M30 620 H600 V800 H30 Z", lines("M30 660 H600 M30 710 H600", 1.0), 1.8))
    # the round window, rain streaming down the glass, rooftops beyond
    b.append(f'<circle cx="{WX}" cy="{WY}" r="{WR + 16}" stroke-width="2.4"/>')
    streaks = "".join(f'<path d="M{x} {y} q4 22 0 44 q-4 -20 0 -44 Z" stroke-width="1.1"/>'
                      for x in range(190, 520, 30) for y in ((70 + (x * 7) % 60), (190 + (x * 13) % 70)))
    inner = (f'<use href="#cloud" transform="translate(300 120) scale(1.2)" stroke-width="1.3"/>' + rooftops() + streaks
             + lines(f"M{WX} {WY - WR} V{WY + WR} M{WX - WR} {WY} H{WX + WR}", 2.6))
    b.append(clip_d(f"M{WX - WR} {WY} A{WR} {WR} 0 1 0 {WX + WR} {WY} A{WR} {WR} 0 1 0 {WX - WR} {WY} Z", inner, 1.6, fill="#fff"))
    b.append(f'<path d="M{WX - 150} {WY + WR + 10} H{WX + 150} L{WX + 140} {WY + WR + 26} H{WX - 140} Z" stroke-width="1.9"/>')
    # hanging trailing plant on its hook (Dot sits on the hook)
    b.append('<path d="M546 36 V64 Q546 74 536 74" fill="none" stroke-width="2"/>')
    b.append(dot(552, 52, 0.9))
    b.append(lines("M536 74 L512 124 M536 74 L560 124", 1.3))
    b.append(plant("vine", 536, 124, 1.0) + '<path d="M508 124 H564 Q564 156 536 158 Q508 156 508 124 Z" stroke-width="1.8"/>')
    # hanging woven egg chair swaying in from the left
    b.append(lines("M196 30 L176 210", 2.2))
    shell = "M176 210 C80 216 52 360 70 470 C84 560 150 610 210 606 C280 600 314 540 300 440 C292 340 260 216 176 210 Z"
    weave = lines(" ".join(f"M{x} 180 L{x + 300} 680 M{x + 300} 180 L{x} 680" for x in range(-280, 400, 30)), 0.9)
    b.append(clip_d(shell, weave, 2.4))
    b.append('<path d="M106 330 C120 260 230 250 266 330 C286 400 280 500 250 540 C200 580 130 570 104 520 C86 460 92 380 106 330 Z" stroke-width="2"/>')
    # Tofu reading inside with the big cable-knit blanket
    tx, ty, ts = 186, 530, 1.05
    b.append(char("to", tx, ty, ts, arms=(None, None), sit=True))
    blanket = "M96 520 Q140 506 186 516 Q236 524 276 512 L294 560 Q280 640 240 660 Q180 676 120 650 Q90 600 96 470 Z"
    cables = "".join(f'<path d="M{x - 7} 450 V690 M{x + 7} 450 V690" stroke-width="0.9"/>' + "".join(f'<path d="M{x - 6} {y} Q{x} {y - 3} {x + 6} {y + 8} M{x + 6} {y} Q{x} {y - 3} {x - 6} {y + 8}" stroke-width="0.9"/>' for y in range(452, 690, 12)) for x in (122, 166, 210, 254))
    b.append(clip_d(blanket, cables, 2))
    b.append(book_open(tx, ty - 80, 72, 40))
    b.append(arms_only("to", tx, ty, ts, (-150, 150)))
    b.append(lines("M150 600 Q180 636 214 600", 1))
    # tray on a low stool with teapot and cup, battery lantern, stack of books
    b.append('<path d="M396 650 H536 V666 H396 Z" stroke-width="1.9"/><path d="M406 666 L400 720 H412 L418 666 M514 666 L520 720 H532 L526 666" stroke-width="1.8"/>')
    b.append('<rect x="400" y="634" width="132" height="16" rx="4" stroke-width="1.8"/>')
    b.append(teapot(440, 636, 0.85) + teacup(504, 636, 1.15))
    b.append('<rect x="548" y="664" width="34" height="56" rx="6" stroke-width="1.8"/><rect x="552" y="676" width="26" height="30" rx="3" stroke-width="1.2"/>'
             + '<path d="M556 664 Q565 646 574 664" fill="none" stroke-width="2"/><circle cx="565" cy="691" r="6" stroke-width="1.1"/>')
    b.append(book_closed(330, 738, 92, 14) + book_closed(334, 724, 80, 14) + book_closed(328, 710, 86, 14) + book_closed(336, 696, 70, 14))
    return "".join(b)


def svg():
    return page(build(), TITLE)
