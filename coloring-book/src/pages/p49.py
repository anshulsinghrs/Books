"""Page 49 — The Sleeping Cabin (dollhouse cutaway of the winter cabin on Lantern Hill)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, pine
from props import lantern_hanging, cushion, snowflake, star

TITLE = "Page 49 — The Sleeping Cabin"


def logs(x0, y0, x1, y1, step=18):
    return lines(" ".join(f"M{x0} {y} H{x1}" for y in range(y0 + step, y1, step)), 0.9)


def blanket(x, y, w, h, pat):
    d = f"M{x} {y} Q{x + w/2} {y - 8} {x + w} {y} V{y + h} H{x} Z"
    inner = {"checks": lines(" ".join(f"M{x + k*w/6:.0f} {y - 10} V{y + h}" for k in range(1, 6)) + " " + " ".join(f"M{x} {y + k*h/3:.0f} H{x + w}" for k in range(1, 3)), 0.9),
             "dots": "".join(f'<circle cx="{x + i*w/5:.0f}" cy="{y + 6 + j*12}" r="2.5" stroke-width="0.8"/>' for i in range(1, 5) for j in range(int(h / 12))),
             "stripes": lines(" ".join(f"M{x + k*w/7:.0f} {y - 10} V{y + h}" for k in range(1, 7)), 1),
             "zigzag": lines(" ".join("M%d %d " % (x, yy) + " ".join(f"L{xx} {yy + (5 if (xx // 10) % 2 else -5)}" for xx in range(int(x), int(x + w) + 10, 10)) for yy in range(int(y) + 8, int(y + h), 14)), 0.9),
             "stars": "".join(f'<use href="#star4" transform="translate({x + i*w/4:.0f} {y + h/2:.0f}) scale(0.6)" stroke-width="1.6"/>' for i in range(1, 4)),
             "hearts": "".join(f'<use href="#heart" transform="translate({x + i*w/4:.0f} {y + h/2:.0f}) scale(0.55)" stroke-width="1.8"/>' for i in range(1, 4))}[pat]
    return clip_d(d, inner, 1.7)


def build():
    b = []
    # snowy night outside, pines at both sides
    for (x, y, s) in ((50, 80, 1.0), (560, 90, 0.8), (100, 140, 0.7), (520, 160, 1.0), (40, 300, 0.8), (580, 330, 0.9), (44, 520, 0.9), (584, 560, 0.8)):
        b.append(snowflake(x, y, s))
    for x in (40, 584):
        b.append(f'<rect x="{x - 6}" y="660" width="12" height="70" stroke-width="1.5"/>')
        b.append(pine(x, [(440, 540, 22), (500, 610, 30), (560, 670, 36)], 1.5, 3))
    b.append('<path d="M30 726 Q310 700 600 726 V800 H30 Z" stroke-width="1.8"/>')
    # stone chimney (Dot asleep on top)
    b.append('<rect x="150" y="70" width="40" height="100" stroke-width="1.9"/>' + lines("M150 90 H190 M150 110 H190 M150 130 H190 M150 150 H190 M170 70 V90 M160 90 V110 M180 110 V130 M165 130 V150", 1))
    b.append('<path d="M144 70 Q144 58 170 58 Q196 58 196 70 Z" stroke-width="1.7"/>')
    b.append(dot(170, 50, 0.85, sleep=True))
    # roof with snow
    b.append('<path d="M50 236 L310 60 L570 236 Z" stroke-width="2.2"/>')
    b.append('<path d="M40 240 L310 50 L580 240 L566 248 L310 70 L54 248 Z" stroke-width="1.8"/>')
    b.append('<path d="M60 230 Q40 236 46 222 L300 50 Q310 40 320 50 L574 222 Q580 236 560 230 L310 66 Z" stroke-width="1.6"/>')
    # cabin body and floors (logs inside every room)
    b.append('<rect x="74" y="236" width="472" height="490" stroke-width="2.4"/>')
    for (x0, y0, x1, y1) in ((80, 242, 540, 460), (80, 470, 540, 720)):
        b.append(clip_d(f"M{x0} {y0} H{x1} V{y1} H{x0} Z", logs(x0, y0, x1, y1), 1.2))
    b.append('<rect x="74" y="456" width="472" height="16" stroke-width="2"/><rect x="74" y="232" width="472" height="12" stroke-width="2"/>')
    b.append('<rect x="300" y="244" width="12" height="212" stroke-width="1.8"/>')
    b.append("".join(f'<circle cx="{x}" cy="{y}" r="7" stroke-width="1.3"/>' for x in (74, 546) for y in range(260, 720, 36)))
    # loft under the roof: Miso awake at the little window, Tofu in the hammock
    b.append(clip_d("M100 230 L310 88 L520 230 Z", logs(100, 88, 520, 230, 20), 1.4))
    b.append('<circle cx="236" cy="170" r="24" stroke-width="2"/>')
    b.append(clip_d("M218 170 A18 18 0 1 0 254 170 A18 18 0 1 0 218 170 Z", snowflake(230, 166, 0.6) + lines("M236 152 V188 M218 170 H254", 1.6), 1.2, fill="#fff"))
    b.append(char("mi", 290, 232, 0.6, arms=(140, -14), head_rot=-14))
    b.append(lines("M360 160 L370 200 M480 160 L470 200", 1.4))
    b.append(char("to", 420, 224, 0.5, arms=(None, None), mood="sleep"))
    b.append('<path d="M366 196 Q420 240 474 196 L474 204 Q420 252 366 204 Z" stroke-width="1.8"/>' + lines("M378 204 Q420 232 462 204", 0.9))
    b.append(lantern_hanging(330, 100, 0.6, 4))
    # upper floor left: Bramble in the big bed
    b.append('<rect x="96" y="380" width="16" height="74" stroke-width="1.6"/><rect x="96" y="440" width="190" height="14" stroke-width="1.6"/>')
    b.append(cushion(140, 392, 56, 30, "dots"))
    b.append(char("br", 180, 450, 0.62, arms=(None, None), mood="sleep"))
    b.append(blanket(118, 412, 168, 32, "checks"))
    b.append(lantern_hanging(200, 244, 0.6, 8))
    # upper floor right: Clover (top bunk) and Juniper (bottom bunk)
    b.append('<rect x="320" y="250" width="12" height="206" stroke-width="1.6"/><rect x="520" y="250" width="12" height="206" stroke-width="1.6"/>')
    b.append(char("cl", 404, 340, 0.55, arms=(None, None), mood="sleep"))
    b.append(blanket(334, 318, 186, 22, "hearts") + '<rect x="320" y="340" width="212" height="12" rx="2" stroke-width="1.7"/>')
    b.append(char("ju", 420, 432, 0.6, arms=(None, None), mood="sleep"))
    b.append(blanket(334, 418, 186, 24, "zigzag") + '<rect x="320" y="442" width="212" height="12" rx="2" stroke-width="1.7"/>')
    # ground floor left: stone fireplace with glowing embers, Pip curled in his basket bed
    b.append('<rect x="90" y="560" width="110" height="160" stroke-width="2"/>' + clip_d("M90 560 H200 V720 H90 Z", lines("M90 590 H200 M90 620 H200 M90 650 H200 M120 560 V590 M160 590 V620 M110 620 V650 M180 620 V650", 1), 2))
    b.append('<path d="M112 720 V672 A33 33 0 0 1 178 672 V720 Z" stroke-width="1.9"/>')
    b.append('<path d="M124 716 Q128 700 136 706 Q140 690 148 704 Q156 692 160 708 Q166 702 168 716 Z" stroke-width="1.3"/>')
    b.append(lines("M140 690 q-3 -6 0 -12 M156 688 q3 -6 0 -12", 1))
    b.append('<ellipse cx="236" cy="704" rx="44" ry="14" stroke-width="1.8"/>')
    b.append(char("pi", 236, 712, 0.55, arms=(None, None), mood="sleep", sit=True))
    b.append('<path d="M192 700 Q236 722 280 700 L276 716 Q236 736 196 716 Z" stroke-width="1.8"/>' + lines("M204 710 L208 722 M224 714 L226 728 M246 714 L246 728 M266 710 L264 722", 0.9))
    # stairs
    b.append(clip_d("M290 720 L370 472 H392 L312 720 Z", lines(" ".join(f"M280 {720 - k*24} H400" for k in range(1, 11)), 1.2), 1.8))
    # ground floor right: Pebble in a bathtub of pillows, Thimble in the dresser drawer
    b.append(char("pb", 440, 660, 0.62, arms=(None, None), mood="sleep"))
    b.append(cushion(410, 640, 40, 24, "stripes", -10) + cushion(470, 640, 40, 24, "dots", 10))
    b.append('<path d="M386 640 H496 Q496 692 460 696 H422 Q386 692 386 640 Z" stroke-width="2"/><path d="M380 636 H502 V646 H380 Z" stroke-width="1.7"/>'
             '<path d="M398 694 L392 712 H404 L408 696 M474 696 L478 712 H490 L484 694" stroke-width="1.6"/>')
    b.append('<rect x="506" y="560" width="34" height="160" stroke-width="1.9"/>' + lines("M506 600 H540 M506 640 H540 M506 680 H540", 1.4)
             + "".join(f'<circle cx="523" cy="{y}" r="3" stroke-width="1"/>' for y in (580, 620, 700)))
    b.append(char("th", 526, 658, 0.6, arms=(None, None), mood="sleep"))
    b.append(blanket(508, 650, 30, 12, "stars") + '<path d="M500 640 H548 V664 H500 Z" fill="none" stroke-width="1.7"/>')
    b.append(lantern_hanging(450, 472, 0.6, 8))
    return "".join(b)


def svg():
    return page(build(), TITLE)
