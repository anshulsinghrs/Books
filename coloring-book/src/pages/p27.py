"""Page 27 — Patchwork Afternoon (Thimble's Attic Studio, the quilt half-sewn)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, blossom
from props import quilt_patch, paper_lantern, bunting, jar, icon, SYMBOLS

TITLE = "Page 27 — Patchwork Afternoon"


def build():
    b = []
    # sloped ceiling and beams, as in the studio on page 13
    b.append(clip_d("M30 30 H600 V60 L30 250 Z", lines(" ".join(f"M{x} 0 L{x - 120} 300" for x in range(80, 760, 70)), 1.0), 2))
    for k in range(3):
        y0 = 92 + k * 58
        b.append(f'<path d="M30 {y0 + 152} L600 {y0 - 38} L600 {y0 - 22} L30 {y0 + 168} Z" stroke-width="1.8"/>')
    # round window, open (the inner sash swung in)
    b.append('<circle cx="504" cy="236" r="54" stroke-width="2.2"/><circle cx="504" cy="236" r="44" stroke-width="1.4"/>')
    b.append(clip_d("M460 236 A44 44 0 1 0 548 236 A44 44 0 1 0 460 236 Z", '<use href="#cloud" transform="translate(500 226) scale(0.5)" stroke-width="2.6"/>', 1.4, fill="#fff"))
    b.append('<path d="M460 236 Q440 200 450 186 Q470 220 470 260 Q460 250 460 236 Z" stroke-width="1.6"/>')
    # garland of fabric triangles and two paper lanterns
    b.append(bunting([(40, 270), (300, 330), (560, 250)], None, 30))
    b.append(paper_lantern(130, 150, 1.0) + paper_lantern(380, 120, 0.9))
    b.append(lines("M130 110 V70 M380 84 V50", 1.2))
    # Clover behind the table folding a paper lantern; spools on a rack
    for k in range(6):
        b.append(f'<g transform="translate({60 + k*26} 410)" stroke-width="1.4"><rect x="-10" y="-26" width="20" height="5" rx="2"/><rect x="-10" y="0" width="20" height="5" rx="2"/>'
                 '<rect x="-7" y="-21" width="14" height="21"/><path d="M-7 -14 H7 M-7 -7 H7" fill="none" stroke-width="0.8"/></g>')
    b.append('<rect x="40" y="414" width="170" height="8" rx="2" stroke-width="1.6"/>')
    cx, cy, cs = 200, 520, 1.35
    b.append(char("cl", cx, cy, cs, arms=(None, None), mood="happy"))
    b.append(char("th", 400, 452, 1.5, arms=(None, None), mood="happy"))
    # craft table
    b.append('<path d="M40 440 H590 L600 520 H30 Z" stroke-width="2.2"/>')
    lx, ly = paw("cl", cx, cy, cs, "L", -30)
    b.append(f'<g transform="translate({lx + 18:.0f} {ly - 4:.0f})" stroke-width="1.4"><rect x="-14" y="-16" width="28" height="6" rx="2"/>'
             '<path d="M-14 -10 H14 L18 -2 L14 6 L18 14 L14 22 H-14 L-18 14 L-14 6 L-18 -2 Z"/><rect x="-14" y="22" width="28" height="6" rx="2"/></g>')
    b.append(arms_only("cl", cx, cy, cs, (-30, 30)))
    # flower press and pressed-flower cards
    b.append('<rect x="80" y="452" width="64" height="40" rx="3" stroke-width="1.8"/><rect x="80" y="462" width="64" height="8" stroke-width="1.2"/>'
             + "".join(f'<circle cx="{x}" cy="{y}" r="4" stroke-width="1.2"/>' for x, y in ((88, 458), (136, 458), (88, 486), (136, 486))))
    b.append('<rect x="272" y="460" width="40" height="50" rx="2" stroke-width="1.5" transform="rotate(-8 292 485)"/>' + blossom(290, 482, 10, 1)
             + '<rect x="300" y="470" width="40" height="46" rx="2" stroke-width="1.5" transform="rotate(10 320 493)"/>' + blossom(320, 494, 9, 1))
    # sewing machine (simple outline), ribbon spools, button jar with Dot
    b.append('<path d="M450 500 V450 Q450 430 470 430 H560 Q576 430 576 446 V500 Z" stroke-width="2"/>'
             '<path d="M470 500 V470 Q470 458 482 458 H560 V500" fill="none" stroke-width="1.4"/><rect x="440" y="500" width="146" height="10" rx="2" stroke-width="1.8"/>'
             '<path d="M500 458 V478 M494 478 H506" fill="none" stroke-width="1.6"/><circle cx="560" cy="446" r="6" stroke-width="1.2"/>')
    b.append('<ellipse cx="236" cy="500" rx="16" ry="6" stroke-width="1.5"/><rect x="220" y="484" width="32" height="16" stroke-width="1.5"/><ellipse cx="236" cy="484" rx="16" ry="6" stroke-width="1.5"/>'
             + lines("M252 492 Q270 506 262 520", 1.4))
    b.append(jar(394, 512, 40, 48, None))
    for (x, y, h) in ((384, 494, 2), (402, 490, 4), (392, 504, 4), (406, 504, 2)):
        b.append(f'<circle cx="{x}" cy="{y}" r="5" stroke-width="1.1"/>' + ("".join(f'<circle cx="{x + dx}" cy="{y + dy}" r="0.9" fill="#000" stroke="none"/>' for dx, dy in ((-1.6, -1.6), (1.6, 1.6), (-1.6, 1.6), (1.6, -1.6))[:h])))
    b.append(dot(394, 455, 0.9))
    b.append(arms_only("th", 400, 452, 1.5, (-30, 30)))
    b.append(lines("M396 440 L420 424", 1.4))
    # the half-sewn quilt draping over the front edge toward the reader
    q = "M60 520 H560 L572 760 H48 Z"
    patches = ""
    for i, sym in enumerate(SYMBOLS):
        c, r = i % 4, i // 4
        patches += quilt_patch(84 + c * 116, 538 + r * 106, 104, 96, sym)
    b.append(clip_d(q, patches, 2.2))
    b.append(lines("M60 528 H560", 0.8).replace('fill="none"', 'fill="none" stroke-dasharray="3 3"'))
    b.append('<rect x="438" y="644" width="108" height="98" stroke-width="1.6" stroke-dasharray="5 4" fill="#fff"/>')
    b.append(quilt_patch(470, 670, 70, 64, "needle").replace('<rect x="470" y="670"', '<rect x="470" y="670" transform="rotate(8 505 702)"'))
    return "".join(b)


def svg():
    return page(build(), TITLE)
