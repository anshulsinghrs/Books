"""Stage 1 — character model sheet (reference only; carries labels)."""
from chars import DEFS, char, dot

W, H = 1200, 930
S = 1.25
BASE = 440

LINEUP = [  # id, x, name, species, height note, accessory
    ("br", 112, "Bramble", "brown bear", "1.0", "knit vest + acorn pin (left chest)"),
    ("cl", 236, "Clover", "rabbit", "0.65 (0.85 ears)", "clover clip, folded left ear"),
    ("mi", 371, "Miso", "cat", "0.55", "round collar + fish charm"),
    ("ju", 505, "Juniper", "fox", "0.75", "dotted neckerchief, knot right"),
    ("pi", 671, "Pip", "puppy", "0.6", "striped pom-pom hat"),
    ("to", 837, "Tofu", "panda", "0.85, widest", "crescent-moon pendant"),
    ("pb", 1010, "Pebble", "river otter", "0.5", "belt pouch + lucky pebble"),
    ("th", 1100, "Thimble", "mouse", "0.3", "pencil behind right ear, tail bow"),
]

SYMS = [("acorn", "Bramble"), ("clover", "Clover"), ("fish", "Miso"), ("star", "Juniper"),
        ("pompom", "Pip"), ("moon", "Tofu"), ("pebble", "Pebble"), ("needle", "Thimble")]


def txt(x, y, s, size=13, weight="400", anchor="middle", fill="#222"):
    return (f'<text x="{x}" y="{y}" font-family="Georgia, serif" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" stroke="none">{s}</text>')


def build():
    b = []
    b.append(txt(40, 52, "Cozy Little Friends — character model sheet", 26, "700", "start"))
    b.append(txt(40, 76, "Relative heights to Bramble (1.0). Every page places the cast from these exact parts.", 13, "400", "start", "#555"))
    # height guides
    for f in (1.0, 0.75, 0.5, 0.25):
        y = BASE - 200 * S * f
        b.append(f'<path d="M30 {y} H1170" stroke="#bbb" stroke-width="0.8" stroke-dasharray="4 5" fill="none"/>')
        b.append(txt(1172, y + 4, f"{f:g}", 10, "400", "start", "#999"))
    b.append(f'<path d="M30 {BASE} H1170" stroke="#999" stroke-width="1" fill="none"/>')
    for c, x, name, sp, hgt, acc in LINEUP:
        b.append(char(c, x, BASE, S))
        b.append(txt(x, BASE + 30, name, 16, "700"))
        b.append(txt(x, BASE + 48, f"{sp} · {hgt}", 11.5, "400", "middle", "#555"))
    # accessory notes, two rows to avoid overlap
    for i, (c, x, name, sp, hgt, acc) in enumerate(LINEUP):
        b.append(txt(x, BASE + 66 + (i % 2) * 15, acc, 10.5, "400", "middle", "#777"))

    # Dot
    b.append(txt(40, 570, "Dot the wren — hidden on every page", 16, "700", "start"))
    b.append(dot(140, 680, 4.2))
    b.append(dot(270, 700, 1.0))
    b.append(txt(270, 730, "actual size", 10.5, "400", "middle", "#777"))
    b.append(dot(330, 700, 1.0, sleep=True))
    b.append(txt(330, 730, "asleep", 10.5, "400", "middle", "#777"))

    # quilt symbols
    b.append(txt(420, 570, "Friendship-quilt patches (one per friend)", 16, "700", "start"))
    for i, (sym, who) in enumerate(SYMS):
        x = 420 + i * 95
        b.append(f'<rect x="{x}" y="600" width="80" height="80" rx="4" stroke-width="2"/>')
        b.append(f'<rect x="{x+6}" y="606" width="68" height="68" rx="2" fill="none" stroke-width="0.8" stroke-dasharray="3 3"/>')
        b.append(f'<use href="#sym-{sym}" transform="translate({x+40} 640) scale(1.3)" stroke-width="1.5"/>')
        b.append(txt(x + 40, 700, who, 12, "400", "middle", "#555"))

    # face style + expressions
    b.append(txt(420, 770, "Faces: solid oval eyes with one upper-right highlight · outlined blush ovals left open · no teeth · happy and sleepy eyes for quiet pages",
                 11.5, "400", "start", "#555"))
    b.append(char("cl", 470, 905, 0.55, mood="happy"))
    b.append(char("pi", 540, 905, 0.55, mood="happy", wag=True))
    b.append(char("to", 620, 905, 0.55, mood="sleep", sit=True))
    b.append(char("ju", 710, 905, 0.55, brows=True))
    b.append(char("th", 770, 905, 0.9, mood="happy"))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<title>Character model sheet</title>
{DEFS}
<rect width="{W}" height="{H}" fill="#fff"/>
<g fill="#fff" stroke="#000" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.25">
{''.join(b)}
</g>
</svg>
"""


if __name__ == "__main__":
    import sys
    open(sys.argv[1], "w").write(build())
