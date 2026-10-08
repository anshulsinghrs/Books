"""Page 46 — One More Chapter (bedtime story in the guest bedroom)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import quilt_patch, book_closed, icon, star, book_open

TITLE = "Page 46 — One More Chapter"


def bunk_quilt(x, y, w, h, motifs):
    d = f"M{x} {y} H{x + w} V{y + h} H{x} Z"
    cells = ""
    cw = w / 5
    for i in range(5):
        for j in range(2):
            cx, cy = x + i * cw, y + j * h / 2
            cells += f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{cw:.1f}" height="{h/2:.1f}" stroke-width="1.1"/>'
            cells += icon(motifs[(i + j) % len(motifs)], cx + cw / 2, cy + h / 4, 0.5, 0.9)
    return clip_d(d, cells, 1.8)


def build():
    b = []
    # wall, dormer window with a starry view
    b.append(clip_d("M30 30 H600 V560 H30 Z", lines(" ".join(f"M30 {y} H600" for y in range(80, 560, 50)), 0.8), 1.4))
    b.append('<path d="M230 260 V140 L310 70 L390 140 V260 Z" stroke-width="2.2"/>')
    b.append(clip_d("M244 252 V146 L310 88 L376 146 V252 Z",
                    star(270, 150, 0.9) + star(340, 130, 1.2, 4) + star(300, 210, 0.8) + star(352, 210, 0.9, 4) + '<path d="M300 120 A16 16 0 1 0 316 140 A12 12 0 0 1 300 120 Z" stroke-width="1.4"/>'
                    + lines("M310 88 V252 M244 190 H376", 2), 1.4, fill="#fff"))
    b.append('<rect x="220" y="258" width="180" height="12" rx="3" stroke-width="1.8"/>')
    # bookshelf (Dot asleep on top)
    b.append('<rect x="420" y="190" width="140" height="200" stroke-width="2"/>' + lines("M420 256 H560 M420 322 H560", 1.8))
    for k, w in enumerate((14, 12, 16, 12, 14, 18)):
        x = 428 + sum((14, 12, 16, 12, 14, 18)[:k]) + k * 2
        b.append(f'<rect x="{x}" y="{208 + (k % 2) * 4}" width="{w}" height="{46 - (k % 2) * 4}" rx="1" stroke-width="1.2"/>')
        b.append(f'<rect x="{x}" y="{274 + (k % 3) * 3}" width="{w}" height="{46 - (k % 3) * 3}" rx="1" stroke-width="1.2"/>')
    b.append('<path d="M440 384 Q440 344 470 344 Q500 344 500 384 Z" stroke-width="1.6"/>' + lines("M450 360 q6 -6 12 0 M474 356 q6 -6 12 0", 1))
    b.append(dot(490, 181, 0.85).replace('href="#dot"', 'href="#dot-sleep"'))
    # bunk bed with ladder: Pip on top, Pebble below, peeking out from patchwork quilts
    b.append('<rect x="40" y="140" width="16" height="560" stroke-width="2"/><rect x="230" y="140" width="16" height="560" stroke-width="2"/>')
    b.append(char("pi", 120, 300, 1.0, arms=(None, None), mood="sleep"))
    b.append(bunk_quilt(56, 250, 174, 60, ("star", "moon", "heart")))
    b.append('<rect x="40" y="310" width="206" height="18" rx="3" stroke-width="2"/><rect x="40" y="228" width="206" height="10" rx="3" stroke-width="1.6"/>')
    b.append(lines("M60 228 V250 M100 228 V250 M140 228 V250 M180 228 V250 M220 228 V250", 0).replace('stroke-width="0"', 'stroke-width="1"'))
    b.append(char("pb", 130, 540, 1.1, arms=(None, None), mood="sleep"))
    b.append(bunk_quilt(56, 500, 174, 66, ("flower", "leaf", "heart")))
    b.append('<rect x="40" y="566" width="206" height="20" rx="3" stroke-width="2"/>')
    # plush whale and stuffed star
    b.append('<path d="M160 498 Q170 470 200 474 Q222 478 220 494 L230 486 L230 504 L218 498 Q200 512 174 506 Z" stroke-width="1.6"/><circle cx="182" cy="488" r="2" fill="#000" stroke="none"/>')
    b.append(star(80, 300, 1.4))
    # ladder
    b.append('<path d="M246 330 L272 700 H284 L258 330 Z" stroke-width="1.7"/>' + "".join(f'<rect x="{246 + k*2.2:.0f}" y="{350 + k*44}" width="30" height="8" rx="2" stroke-width="1.4"/>' for k in range(8)))
    # mushroom night-light
    b.append('<path d="M80 660 Q80 640 98 640 Q116 640 116 660 Z" stroke-width="1.6"/><rect x="92" y="660" width="12" height="18" rx="3" stroke-width="1.5"/>' + lines("M84 640 l-8 -8 M98 632 V622 M112 640 l8 -8", 1))
    # braided rug and slippers
    b.append('<ellipse cx="300" cy="720" rx="200" ry="30" stroke-width="1.8"/><ellipse cx="300" cy="720" rx="170" ry="22" stroke-width="1.1"/><ellipse cx="300" cy="720" rx="140" ry="15" stroke-width="1"/>')
    b.append('<path d="M150 724 Q150 704 170 704 Q186 704 186 724 Z M196 726 Q196 706 216 706 Q232 706 232 726 Z" stroke-width="1.6"/>')
    # Bramble in the armchair, three-quarter from behind, reading
    b.append('<path d="M340 760 V560 Q340 470 440 470 Q540 470 540 560 V760 Z" stroke-width="2.2"/>' + lines("M360 560 Q440 540 520 560", 1))
    b.append(char("br", 440, 730, 1.15, arms=(40, -40), back=True, sit=True))
    b.append('<path d="M320 760 V640 Q320 610 350 610 Q380 610 380 640 V760 Z M500 760 V640 Q500 610 530 610 Q560 610 560 640 V760 Z" stroke-width="2.2"/>')
    b.append(book_open(470, 580, 90, 50, 0))
    b.append('<path d="M484 548 A10 10 0 1 0 494 562 A8 8 0 0 1 484 548 Z" stroke-width="1.3"/>' + star(500, 548, 0.7) + lines("M434 556 H460 M434 566 H458", 0.9))
    return "".join(b)


def svg():
    return page(build(), TITLE)
