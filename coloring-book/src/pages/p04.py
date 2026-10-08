"""Page 4 — Pancake Tower (Bramble flips, Pip watches)."""
from chars import char, arms_only, dot, page, paw, apron
from scene import clip_d, lines
from props import stove, pancake_stack, bowl, jar, mug, icon

TITLE = "Page 4 — Pancake Tower"


def build():
    b = []
    # kitchen wall: plank wainscot and a shelf
    b.append(clip_d("M30 470 H600 V800 H30 Z", lines(" ".join(f"M{x} 470 V800" for x in range(60, 600, 40)), 1.0), 1.6))
    b.append('<rect x="30" y="462" width="570" height="10" stroke-width="1.6"/>')
    b.append('<rect x="420" y="300" width="150" height="10" rx="2" stroke-width="1.8"/>')
    b.append(jar(446, 300, 30, 40, "berry") + jar(486, 300, 30, 46, "egg") + mug(530, 300, 0.9, "checks"))
    # Bramble's round kitchen window (inside view) with the pancake's path across it
    b.append('<circle cx="150" cy="190" r="86" stroke-width="2.2"/><circle cx="150" cy="190" r="72" stroke-width="1.5"/>')
    b.append(clip_d("M78 190 A72 72 0 1 0 222 190 A72 72 0 1 0 78 190 Z",
                    '<use href="#cloud" transform="translate(130 170) scale(0.7)" stroke-width="2"/>'
                    '<path d="M70 236 C110 222 160 232 230 218 V280 H70 Z" stroke-width="1.3"/>' + lines("M150 110 V270 M70 190 H230", 2.2), 1.5, fill="#fff"))
    b.append('<path d="M64 270 H236 L230 284 H70 Z" stroke-width="1.8"/>')
    # rail of hanging pans
    b.append('<rect x="400" y="70" width="170" height="8" rx="4" stroke-width="1.6"/>')
    for (x, r) in ((430, 22), (486, 28), (540, 18)):
        b.append(lines(f"M{x} 78 V92", 1.3) + f'<rect x="{x-4}" y="92" width="8" height="34" rx="3" stroke-width="1.5"/>'
                 + f'<circle cx="{x}" cy="{126 + r}" r="{r}" stroke-width="1.8"/><circle cx="{x}" cy="{126 + r}" r="{r - 6}" stroke-width="1"/>')
    # stove at lower left with the mixing bowl and whisk
    b.append(stove(118, 520, 150, 236, pipe_to=300))
    b.append('<rect x="98" y="290" width="40" height="14" rx="3" stroke-width="1.6"/>')
    b.append(bowl(84, 520, 64, 30, "cream", "stripe"))
    b.append('<path d="M98 492 L132 450" fill="none" stroke-width="3"/><path d="M128 452 Q122 430 134 424 Q146 430 138 456 Z" stroke-width="1.3"/>'
             + lines("M132 424 Q128 440 134 452 M138 426 Q140 440 136 454", 0.8))
    # the flying pancake with motion arcs
    b.append('<g transform="translate(-44 14)">')
    b.append('<path d="M290 136 Q340 104 398 124 Q410 140 394 154 Q340 172 290 158 Q276 148 290 136 Z" stroke-width="2"/>'
             '<path d="M300 142 Q340 128 390 136" fill="none" stroke-width="1"/>')
    b.append(lines("M300 300 Q290 236 300 180 M282 318 Q270 260 280 214 M420 160 Q460 210 470 270 M436 150 Q480 196 492 246", 1.3))
    b.append('</g>')
    # table end at right with the tower, Pip kneeling on his stool behind it
    b.append(char("pi", 446, 566, 1.6, arms=(None, None), mood="open", head_rot=10))
    table = "M330 548 H600 V600 H330 Z"
    b.append(clip_d(table, lines("M330 570 Q390 566 450 572 M480 584 Q530 580 590 584", 1.0), 2))
    b.append('<rect x="330" y="600" width="270" height="22" stroke-width="1.8"/>'
             '<path d="M346 622 H372 V760 H346 Z M560 622 H586 V760 H560 Z" stroke-width="1.8"/>' + lines("M358 660 q-4 10 0 20", 0.8))
    b.append(arms_only("pi", 446, 566, 1.6, (-34, 34)))
    b.append(pancake_stack(530, 566, 10, 104))
    b.append(bowl(372, 590, 56, 26, "berries"))
    # syrup jug
    b.append('<path d="M424 588 Q414 560 426 544 V534 H446 V544 Q458 560 448 588 Z" stroke-width="1.7"/>'
             '<path d="M446 546 Q460 546 460 558 Q460 568 450 570" fill="none" stroke-width="2.4"/>'
             '<path d="M426 536 L418 528 L428 530 Z" stroke-width="1.2"/>' + icon("drop", 436, 568, 0.6))
    # egg carton with Dot on the lid
    b.append('<path d="M440 600 H518 L514 612 H444 Z" stroke-width="1.5"/>')
    b.append('<path d="M440 600 L446 584 H512 L518 600 Z" stroke-width="1.6"/>' + lines("M462 584 L460 600 M480 584 V600 M498 584 L500 600", 0.9))
    b.append(dot(482, 575))
    # Bramble flips the pancake (checked apron)
    bx, by, bs = 196, 756, 1.85
    b.append(char("br", bx, by, bs, arms=(16, -168), outfit=apron("br", bs), head_rot=-6))
    px, py = paw("br", bx, by, bs, "R", -168)
    b.append(f'<g transform="translate({px:.1f} {py:.1f}) rotate(-78)" stroke-width="1.8">'
             '<rect x="-5" y="-6" width="46" height="12" rx="5"/>'
             '<circle cx="72" cy="0" r="32"/><circle cx="72" cy="0" r="25" stroke-width="1.2"/></g>')
    b.append(arms_only("br", bx, by, bs, (None, -168)))
    return "".join(b)


def svg():
    return page(build(), TITLE)
