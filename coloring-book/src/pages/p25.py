"""Page 25 — Pie in the Garden Oven (brick dome oven in the cottage garden)."""
from math import sin, cos, radians, pi
from chars import char, arms_only, dot, page, paw, apron
from scene import clip_d, lines, scallop_blob
from props import bowl, icon

TITLE = "Page 25 — Pie in the Garden Oven"


def lattice_pie(x, y, rx=34, ry=11, s=1.0):
    pie = f"M{x - rx} {y} Q{x} {y - ry*2.2:.1f} {x + rx} {y} Q{x} {y + ry*0.9:.1f} {x - rx} {y} Z"
    lat = " ".join(f"M{x - rx + k*rx/3:.1f} {y - ry*2} L{x - rx + k*rx/3 + 14:.1f} {y + ry}" for k in range(-1, 7)) + " " + \
          " ".join(f"M{x + rx - k*rx/3:.1f} {y - ry*2} L{x + rx - k*rx/3 - 14:.1f} {y + ry}" for k in range(-1, 7))
    return (f'<path d="M{x - rx - 4} {y} Q{x} {y + ry*1.8:.1f} {x + rx + 4} {y} L{x + rx + 2} {y + 6} Q{x} {y + ry*2.3:.1f} {x - rx - 2} {y + 6} Z" stroke-width="1.6"/>'
            + clip_d(pie, lines(lat, 1.0), 1.6)
            + lines(" ".join(f"M{x - rx + k*8:.1f} {y + ry*0.25:.1f} q4 3 8 0" for k in range(int(2*rx/8))), 1.0))


def rose(x, y, r=10):
    return (f'<g transform="translate({x} {y})" stroke-width="1.2"><circle r="{r}"/><path d="M{-r*0.5:.1f} {-r*0.2:.1f} Q0 {-r*0.8:.1f} {r*0.5:.1f} {-r*0.2:.1f} '
            f'Q{r*0.4:.1f} {r*0.5:.1f} 0 {r*0.4:.1f} Q{-r*0.5:.1f} {r*0.3:.1f} {-r*0.2:.1f} 0" fill="none"/></g>')


def build():
    b = []
    b.append('<use href="#cloud" transform="translate(160 90) scale(1.1)" stroke-width="1.4"/><use href="#cloud" transform="translate(330 130) scale(0.7)" stroke-width="1.8"/>')
    # climbing rose fence along the back
    b.append(lines(" ".join(f"M{x} 160 V420" for x in range(50, 380, 40)) + " M40 200 H380 M40 380 H380", 5)
             + lines(" ".join(f"M{x} 160 V420" for x in range(50, 380, 40)) + " M40 200 H380 M40 380 H380", 2).replace('stroke-width="2"', 'stroke="#fff" stroke-width="2"'))
    b.append(lines("M40 300 Q100 250 160 290 Q220 330 280 270 Q330 230 380 280", 1.6))
    for (x, y) in ((70, 286), (120, 262), (178, 300), (236, 310), (292, 262), (350, 252), (100, 330), (260, 330), (330, 300)):
        b.append(rose(x, y, 11) + f'<path d="M{x + 10} {y + 8} q10 -2 14 6 q-10 2 -14 -6 Z" stroke-width="1"/>')
    b.append('<path d="M30 430 H600 V800 H30 Z" stroke-width="1.6"/>')
    # brick dome oven on the right third
    b.append('<rect x="352" y="430" width="230" height="130" stroke-width="2"/>')
    b.append(clip_d("M352 430 H582 V560 H352 Z", lines(" ".join(f"M352 {y} H582" for y in range(452, 560, 22)) + " " +
                    " ".join(f"M{x + (22 if (y // 22) % 2 else 0)} {y} V{y + 22}" for y in range(430, 560, 22) for x in range(352, 600, 44)), 1), 2))
    dome = "M360 430 C360 300 420 230 467 230 C514 230 574 300 574 430 Z"
    courses = " ".join(f"M{467 - (107 - k*12)} 430 C{467 - (107 - k*12)} {320 + k*14} {467 - 30 + k*3} {244 + k*16} 467 {244 + k*16} C{467 + 30 - k*3} {244 + k*16} {467 + (107 - k*12)} {320 + k*14} {467 + (107 - k*12)} 430" for k in range(1, 8))
    radial = " ".join(f"M{467 + 110*cos(radians(a)):.0f} {430 - 200*sin(radians(a)):.0f} L467 430" for a in range(15, 170, 15))
    joints = " ".join(f"M{467 + dx} {256 + k*16 + 2} v12" for k in range(0, 11) for dx in range(-100 + (k % 2)*12, 110, 24))
    b.append(clip_d(dome, lines(courses, 1.0) + lines(joints, 0.8), 2.2))
    b.append('<path d="M420 430 V380 A47 47 0 0 1 514 380 V430 Z" stroke-width="2.2"/>')
    b.append('<path d="M408 430 V380 A59 59 0 0 1 526 380 V430" fill="none" stroke-width="1.6"/>')
    b.append('<path d="M438 430 Q446 400 456 410 Q462 386 470 404 Q480 392 484 412 Q494 404 496 430 Z" stroke-width="1.3"/>')
    b.append('<rect x="452" y="186" width="30" height="50" stroke-width="2"/><rect x="446" y="178" width="42" height="12" rx="2" stroke-width="1.8"/>')
    b.append(dot(467, 169))
    # wooden prep table with cherries, rolling pin, mitts and the cooling rack
    b.append('<rect x="40" y="470" width="200" height="16" rx="3" stroke-width="2"/><path d="M52 486 V600 H64 V486 M216 486 V600 H228 V486" stroke-width="1.8"/>')
    b.append(bowl(82, 470, 56, 24))
    for (x, y) in ((68, 448), (82, 444), (96, 448), (76, 438), (90, 436)):
        b.append(f'<circle cx="{x}" cy="{y}" r="6" stroke-width="1.2"/>' + lines(f"M{x} {y - 6} q2 -10 8 -12", 0.9))
    b.append('<path d="M120 466 L200 456 L202 466 L122 476 Z" stroke-width="1.6"/>')
    b.append('<path d="M206 470 Q200 440 216 436 Q232 440 230 470 Z" stroke-width="1.5"/><path d="M228 452 Q238 444 236 460" fill="none" stroke-width="1.5"/>')
    b.append('<rect x="140" y="520" width="80" height="40" rx="4" stroke-width="1.6"/>' + lines("M150 520 V560 M170 520 V560 M190 520 V560 M210 520 V560 M140 540 H220", 1))
    # Juniper approaching from the left with the second pie
    jx, jy, js = 140, 742, 1.35
    b.append(char("ju", jx, jy, js, arms=(None, None), outfit=apron("ju", js, top_frac=0.5)))
    lx, ly = paw("ju", jx, jy, js, "L", -50)
    b.append(f'<rect x="{lx - 20:.0f}" y="{ly - 4:.0f}" width="110" height="10" rx="4" stroke-width="1.8"/>')
    b.append(lattice_pie(lx + 35, ly - 6, 34, 11))
    b.append(arms_only("ju", jx, jy, js, (-50, -70)))
    # Bramble angled toward the oven, sliding the pie in on the long peel
    bx, by, bs = 330, 752, 1.38
    b.append(char("br", bx, by, bs, arms=(None, None), outfit=apron("br", bs), head_rot=8))
    rx, ry = paw("br", bx, by, bs, "R", -100)
    b.append(f'<path d="M{rx - 10:.0f} {ry + 10:.0f} L{rx:.0f} {ry - 2:.0f} L455 418 L449 424 Z" stroke-width="1.8"/>'
             '<path d="M436 424 H498 Q506 424 506 430 H428 Q428 424 436 424 Z" stroke-width="1.8"/>')
    b.append(lattice_pie(467, 420, 30, 9))
    b.append(arms_only("br", bx, by, bs, (-60, -100)))
    # firewood stack in the lower foreground
    for r in range(3):
        for k in range(4 - r):
            x, y = 456 + r * 18 + k * 36, 736 - r * 30
            b.append(f'<rect x="{x - 40}" y="{y - 14}" width="40" height="28" stroke-width="1.4"/>'
                     f'<ellipse cx="{x}" cy="{y}" rx="16" ry="14" stroke-width="1.7"/><ellipse cx="{x}" cy="{y}" rx="9" ry="8" stroke-width="1"/><circle cx="{x}" cy="{y}" r="2.6" stroke-width="0.9"/>')
    return "".join(b)


def svg():
    return page(build(), TITLE)
