"""Page 31 — Flower Crown (macro, flower height)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, daisy, blossom
from props import basket

TITLE = "Page 31 — Flower Crown"


def bluebell_stem(x0, y0, x1, y1, bells):
    out = [f'<path d="M{x0} {y0} Q{(x0 + x1)/2 + 30} {(y0 + y1)/2} {x1} {y1}" fill="none" stroke-width="2.6"/>']
    for (bx, by, r) in bells:
        out.append(lines(f"M{bx} {by - 18} Q{bx + 4} {by - 26} {bx + 2} {by - 34}", 1.4))
        out.append(f'<path transform="translate({bx} {by}) rotate(10)" d="M-{r} 0 Q-{r} -{r*1.6} 0 -{r*1.7} Q{r} -{r*1.6} {r} 0 '
                   f'L{r*0.7:.1f} -{r*0.3:.1f} L{r*0.35:.1f} 0 L0 -{r*0.3:.1f} L-{r*0.35:.1f} 0 L-{r*0.7:.1f} -{r*0.3:.1f} Z" stroke-width="1.7"/>')
    return "".join(out)


def big_bloom(x, y, r=60):
    out = f'<g transform="translate({x} {y})" stroke-width="1.8">'
    for ring, n, rr in ((1.0, 6, 0.55), (0.7, 5, 0.45), (0.42, 4, 0.36)):
        for k in range(n):
            a = 360 * k / n + ring * 30
            out += f'<ellipse cx="0" cy="{-r*ring*0.6:.1f}" rx="{r*rr:.1f}" ry="{r*ring*0.55:.1f}" transform="rotate({a:.0f})"/>'
    return out + f'<circle r="{r*0.18:.1f}"/></g>'


def build():
    b = []
    b.append('<use href="#cloud" transform="translate(300 90) scale(1.4)" stroke-width="1.3"/>')
    # towering stems and leaves
    b.append(lines("M130 800 Q120 500 150 260 M250 800 Q262 560 240 420 M330 800 Q320 640 340 520", 3))
    for (x, y, r) in ((136, 520, -30), (250, 600, 40), (328, 680, -40), (150, 380, 30)):
        b.append(f'<path transform="translate({x} {y}) rotate({r})" d="M0 0 C-30 -10 -40 -50 0 -90 C40 -50 30 -10 0 0 Z" stroke-width="1.7"/>'
                 + f'<path transform="translate({x} {y}) rotate({r})" d="M0 0 V-80" fill="none" stroke-width="1"/>')
    # bluebell stem with Thimble climbing up to pick a blossom
    b.append(bluebell_stem(60, 800, 200, 120, [(208, 150, 18), (176, 206, 20), (214, 246, 18), (190, 300, 16)]))
    b.append(char("th", 120, 300, 1.7, arms=(-150, 140), head_rot=-10, rot=12))
    # big rose-like wild bloom and daisies
    b.append(big_bloom(256, 400, 64))
    b.append(daisy(340, 506, 40, 12, 1.6) + daisy(90, 640, 34, 11, 1.5))
    b.append('<circle cx="160" cy="720" r="16" stroke-width="1.5"/>' + daisy(220, 740, 26, 10, 1.4))
    # clover flowers
    for (x, y) in ((40, 520), (300, 720), (380, 640)):
        b.append(f'<use href="#scallop" transform="translate({x} {y}) scale(1.7)" stroke-width="0.8"/><circle cx="{x}" cy="{y}" r="7" stroke-width="1.1"/>')
    b.append(lines("M470 560 Q480 400 460 250", 3) + '<path d="M472 420 Q506 400 516 370 Q488 384 472 420 Z" stroke-width="1.5"/>' + daisy(460, 230, 44, 13, 1.6))
    # bumblebee and ladybug
    b.append('<g transform="translate(330 200) rotate(-10)" stroke-width="1.6"><ellipse cx="-6" cy="-18" rx="12" ry="9"/><ellipse cx="8" cy="-20" rx="12" ry="9"/>'
             '<ellipse rx="22" ry="15"/><path d="M-8 -14 Q-12 0 -8 14 M4 -15 Q0 0 4 15" fill="none" stroke-width="5"/>'
             '<path d="M-8 -14 Q-12 0 -8 14 M4 -15 Q0 0 4 15" fill="none" stroke="#fff" stroke-width="2"/><circle cx="24" cy="-2" r="8"/>'
             '<circle cx="27" cy="-4" r="1.6" fill="#000" stroke="none"/><path d="M28 -9 Q32 -18 38 -18" fill="none"/></g>')
    b.append('<g transform="translate(340 470) rotate(30)" stroke-width="1.5"><circle cx="0" cy="-12" r="7"/><ellipse rx="15" ry="13"/><path d="M0 -13 V13" fill="none"/>'
             '<circle cx="-7" cy="-2" r="3"/><circle cx="7" cy="-2" r="3"/><circle cx="-6" cy="7" r="2.6"/><circle cx="6" cy="7" r="2.6"/></g>')
    # Clover's face and paws, large, peeking in from the right with the half-woven crown
    cx, cy, cs = 560, 940, 3.0
    b.append(char("cl", cx, cy, cs, arms=(None, None), head_rot=-8, mood="happy"))
    crown = "M370 610 C380 560 460 540 520 560"
    b.append(f'<path d="{crown}" fill="none" stroke-width="8"/><path d="{crown}" fill="none" stroke="#fff" stroke-width="5"/>')
    b.append(daisy(384, 590, 14, 8) + blossom(420, 566, 13) + daisy(460, 556, 14, 8) + blossom(498, 556, 12))
    b.append(lines("M352 640 Q362 620 370 610 M520 560 Q540 566 548 580", 1.6))
    b.append(arms_only("cl", cx, cy, cs, (60, 40)))
    # Clover's flower basket (Dot inside)
    b.append(daisy(452, 690, 14, 8) + blossom(486, 684, 12) + daisy(516, 694, 12, 7))
    b.append(basket(484, 760, 120, 60, handle=True))
    b.append(dot(470, 676, 0.95))
    return "".join(b)


def svg():
    return page(build(), TITLE)
