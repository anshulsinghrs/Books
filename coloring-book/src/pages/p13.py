"""Page 13 — The Quilt Begins (Thimble's Attic Studio)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines
from props import quilt_patch, icon, SYMBOLS

TITLE = "Page 13 — The Quilt Begins"


def spool(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.4/s:.2f}">'
            '<rect x="-11" y="-30" width="22" height="6" rx="2"/><rect x="-11" y="0" width="22" height="6" rx="2"/>'
            '<rect x="-8" y="-24" width="16" height="24"/><path d="M-8 -18 H8 M-8 -12 H8 M-8 -6 H8" fill="none" stroke-width="0.8"/></g>')


def scissors(x, y, rot, s=1.0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.6/s:.2f}">'
            '<path d="M0 -3 L60 -10 L62 -6 L2 3 Z"/><path d="M0 3 L60 10 L62 6 L2 -3 Z"/>'
            '<ellipse cx="-14" cy="-10" rx="12" ry="9"/><ellipse cx="-14" cy="-10" rx="7" ry="5"/>'
            '<ellipse cx="-14" cy="10" rx="12" ry="9"/><ellipse cx="-14" cy="10" rx="7" ry="5"/><circle cx="2" r="2.4"/></g>')


def build():
    b = []
    # sloped ceiling with beams angling across the top
    b.append(clip_d("M30 30 H600 V60 L30 250 Z",
                    lines(" ".join(f"M{x} 0 L{x - 120} 300" for x in range(80, 760, 70)), 1.0), 2))
    for k in range(3):
        y0 = 92 + k * 58
        b.append(f'<path d="M30 {y0 + 152} L600 {y0 - 38} L600 {y0 - 22} L30 {y0 + 168} Z" stroke-width="1.8"/>')
    b.append(lines("M30 250 L600 60", 2.2))
    # round window on the right wall
    b.append('<circle cx="504" cy="214" r="54" stroke-width="2.2"/><circle cx="504" cy="214" r="44" stroke-width="1.4"/>')
    b.append(clip_d("M460 214 A44 44 0 1 0 548 214 A44 44 0 1 0 460 214 Z",
                    '<use href="#cloud" transform="translate(498 202) scale(0.5)" stroke-width="2.6"/>' + lines("M504 170 V258 M460 214 H548", 2), 1.4, fill="#fff"))
    # pegboard of tools with the quilt sketch pinned up
    b.append('<rect x="120" y="260" width="250" height="170" rx="4" stroke-width="2"/>')
    b.append("".join(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#000" stroke="none"/>' for x in range(136, 360, 24) for y in range(276, 420, 24)
                     if not (232 < x < 360 and 268 < y < 420)))
    b.append('<rect x="240" y="276" width="114" height="132" rx="2" stroke-width="1.6"/>'
             + lines("M262 300 H332 V390 H262 Z M285 300 V390 M308 300 V390 M262 330 H332 M262 360 H332", 1.0)
             + '<circle cx="297" cy="282" r="4" stroke-width="1.2"/>')
    b.append('<rect x="136" y="288" width="12" height="98" rx="2" stroke-width="1.5"/>' + lines("M136 304 H142 M136 320 H144 M136 336 H142 M136 352 H144 M136 368 H142", 0.9))
    b.append(scissors(176, 300, 70, 0.7))
    b.append('<circle cx="206" cy="380" r="18" stroke-width="1.6"/><circle cx="206" cy="380" r="7" stroke-width="1.1"/>'
             + '<path d="M222 386 L236 412 L230 414 Z" stroke-width="1.2"/>')
    # rows of thread spools on a shelf
    for row, y in enumerate((330, 400)):
        b.append(f'<rect x="400" y="{y}" width="166" height="10" rx="2" stroke-width="1.7"/>')
        for k in range(6):
            b.append(spool(416 + k * 27, y, 0.95))
    # sewing table with the cutting mat and the eight symbol squares
    b.append('<path d="M40 462 H590 L600 586 H30 Z" stroke-width="2.2"/>')
    b.append('<rect x="30" y="586" width="570" height="26" stroke-width="2"/>' + '<rect x="250" y="592" width="120" height="14" rx="3" stroke-width="1.4"/><circle cx="310" cy="599" r="3" stroke-width="1.1"/>')
    b.append('<path d="M60 612 H90 V780 H60 Z M540 612 H570 V780 H540 Z" stroke-width="2"/>')
    mat = "M130 470 H430 L438 578 H120 Z"
    b.append(clip_d(mat, lines(" ".join(f"M{x} 470 L{x - 6} 578" for x in range(150, 440, 22)) + " " + " ".join(f"M110 {y} H440" for y in range(492, 578, 22)), 0.8), 1.7))
    # eight fabric squares laid out on the cutting mat, one symbol each
    for i, sym in enumerate(SYMBOLS):
        b.append(quilt_patch(146 + (i % 4) * 50, 478 + (i // 4) * 50, 44, 44, sym))
    # pincushion with Dot
    b.append('<path d="M470 520 Q462 490 496 486 Q530 490 522 520 Z" stroke-width="1.8"/>' + lines("M482 490 Q488 506 484 520 M496 486 V520 M510 490 Q504 506 508 520", 1)
             + '<rect x="468" y="518" width="56" height="10" rx="3" stroke-width="1.6"/>'
             + lines("M478 494 L470 476 M504 490 L512 472", 1.2) + '<circle cx="470" cy="475" r="2.6" stroke-width="1"/><circle cx="512" cy="471" r="2.6" stroke-width="1"/>')
    b.append(dot(492, 477))
    # Thimble on the table cutting with the oversized scissors
    tx, ty, ts = 380, 552, 1.5
    b.append(char("th", tx, ty, ts, arms=(None, None), mood="happy", head_rot=-6))
    b.append(quilt_patch(386, 530, 44, 40, pat='stripes', stitch=False) + scissors(392, 528, 20, 0.9))
    b.append(arms_only("th", tx, ty, ts, (-60, 10)))
    # drawer fronts and a basket of fabric scraps under the table
    b.append('<rect x="250" y="640" width="120" height="50" rx="3" stroke-width="1.6"/><circle cx="310" cy="665" r="3.5" stroke-width="1.2"/>')
    b.append('<path d="M410 700 H540 L530 756 H420 Z" stroke-width="1.9"/>' + lines("M412 716 H538 M414 732 H536 M450 700 L452 756 M490 700 L488 756", 1))
    b.append('<path d="M416 700 Q430 672 456 680 Q470 664 494 676 Q520 666 536 700 Z" stroke-width="1.6"/>' + lines("M440 690 l10 -6 M480 686 l10 -4", 0.9))
    # Juniper on the left, holding up fabric choices
    jx, jy, js = 118, 760, 1.55
    b.append(char("ju", jx, jy, js, arms=(None, None)))
    lx, ly = paw("ju", jx, jy, js, "L", 160)
    rx, ry = paw("ju", jx, jy, js, "R", -150)
    b.append(quilt_patch(lx - 50, ly - 56, 52, 52, pat="plaid") + quilt_patch(rx - 6, ry - 60, 52, 52, pat="dots"))
    b.append(arms_only("ju", jx, jy, js, (160, -150)))
    return "".join(b)


def svg():
    return page(build(), TITLE)
