"""Front matter, blank backing pages and back matter (these pages may carry text)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from chars import DEFS, char, dot, FX, FY, FW, FH
from scene import daisy, blossom, lines
from props import star, icon, quilt_patch, SYMBOLS

W, H = 612, 792
SERIF = "Caladea, Georgia, 'DejaVu Serif', serif"

DOT_KEY = [
    "on the chimney top", "on the shelf between two mugs", "on the bird feeder", "on the egg carton lid", "among the fern fronds",
    "on the butter dish rim", "on the pergola crossbeam", "on top of the ladder", "on the middle picture frame", "riding a bunting flag",
    "inside an empty pot", "on the rolling pin handle", "on the pincushion", "in a cubby among the shells", "under the window box",
    "on Clover's umbrella", "on the marshmallow jar lid", "on the plant hook", "on a game-box lid", "on the fort's peak",
    "on the easel's top edge", "on the lamp shade", "in the yarn basket", "on the scarecrow's hat", "on the oven chimney",
    "on a floating music note", "on the button jar lid", "on a branch above the squirrel", "on the tent's ridge pole", "on the stile post",
    "in Clover's basket", "under a mushroom cap", "on the signpost", "on a cattail", "on the cooling rack",
    "on the top tier", "on the bird-bath rim", "on an apple in the basket", "on the bell above the door", "riding a falling leaf",
    "in the door wreath", "on a pumpkin stem", "on the stove pipe's elbow", "on the snowman's hat", "on the telescope's tip",
    "asleep on the bookshelf", "on the star garland", "asleep on the mobile", "asleep on the chimney top", "on the mantel in a quilt square",
]


def txt(x, y, s, size=14, weight="400", anchor="middle", style="normal", outline=False, ls=0):
    if outline:
        return (f'<text x="{x}" y="{y}" font-family="{SERIF}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
                f'letter-spacing="{ls}" fill="#fff" stroke="#000" stroke-width="1.6" stroke-linejoin="round">{s}</text>')
    return (f'<text x="{x}" y="{y}" font-family="{SERIF}" font-size="{size}" font-weight="{weight}" font-style="{style}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}" fill="#000" stroke="none">{s}</text>')


def wrap(body, title):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="8.5in" height="11in" viewBox="0 0 {W} {H}">
<title>{title}</title>
{DEFS}
<rect width="{W}" height="{H}" fill="#fff"/>
<g fill="#fff" stroke="#000" stroke-linejoin="round" stroke-linecap="round" stroke-width="1.25">
{body}
</g>
</svg>
"""


def title_page():
    b = []
    b.append(txt(306, 190, "Cozy Little Friends", 62, "700", outline=True))
    b.append(txt(306, 236, "A Cute &amp; Cozy Coloring Book for Relaxation", 20, "400", style="italic"))
    b.append(lines("M196 262 H416", 1.2))
    b.append("".join(blossom(x, 262, 7, 1) for x in (186, 306, 426)))
    b.append('<path d="M70 640 Q306 600 542 640" fill="none" stroke-width="1.4"/>')
    cast = [("th", 102, 630, 1.0), ("pb", 152, 632, 1.0), ("mi", 210, 630, 1.0), ("cl", 268, 628, 1.0), ("br", 340, 626, 1.0),
            ("to", 426, 628, 1.0), ("ju", 494, 630, 1.0), ("pi", 548, 632, 0.9)]
    for c, x, y, s in cast:
        b.append(char(c, x, y, s, mood="happy" if c in ("cl", "br", "pi") else "open"))
    b.append(dot(306, 300, 1.4))
    b.append(txt(306, 352, "by Bookshelf", 20, "400", style="italic"))
    b.append(txt(306, 700, "Fifty gentle pages from one year in Honeyfern Hollow", 15, style="italic"))
    return wrap("".join(b), "Title page")


def copyright_page():
    b = []
    y = 520
    for k, line in enumerate((
            "Cozy Little Friends: A Cute &amp; Cozy Coloring Book for Relaxation",
            "Copyright © 2026 Bookshelf. All rights reserved.",
            "",
            "No part of this book may be reproduced, stored or transmitted in any form",
            "without written permission from the publisher, except that the owner of",
            "this copy may color and photocopy its pages for personal, non-commercial use.",
            "",
            "Characters, setting and illustrations are original to this book.",
            "First edition",
            "",
            "Printed single-sided: place a spare sheet behind the page you are coloring",
            "when using markers.")):
        b.append(txt(306, y + k * 18, line, 11.5))
    b.append(dot(306, 470, 1.2))
    return wrap("".join(b), "Copyright page")


def belongs_page():
    b = [f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="none" stroke-width="2.6"/>']
    b.append('<rect x="96" y="180" width="420" height="300" rx="24" stroke-width="2.2"/><rect x="108" y="192" width="396" height="276" rx="18" stroke-width="1.2"/>')
    b.append(txt(306, 280, "This book belongs to", 34, "700", outline=True))
    b.append(lines("M150 380 H462", 1.4))
    b.append("".join(blossom(x, y, 12, 1.2) for x, y in ((96, 180), (516, 180), (96, 480), (516, 480))))
    b.append(char("th", 250, 680, 2.2, arms=(150, -14), mood="happy"))
    b.append(char("pi", 380, 690, 1.5, arms=(14, -150), mood="happy", wag=True))
    b.append(dot(462, 571, 1.2))
    b.append("".join(daisy(x, 720, 12, 7) for x in (100, 160, 470, 530)))
    return wrap("".join(b), "This book belongs to")


def test_page():
    b = [f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="none" stroke-width="2.6"/>']
    b.append(txt(306, 100, "Color Test Page", 34, "700", outline=True))
    b.append(txt(306, 132, "Try your pencils, pens and markers here first.", 14, style="italic"))
    shapes = []
    for r in range(5):
        for c in range(5):
            x, y = 110 + c * 98, 200 + r * 96
            k = (r + c) % 5
            if k == 0:
                shapes.append(f'<circle cx="{x}" cy="{y}" r="34" stroke-width="2"/>')
            elif k == 1:
                shapes.append(f'<use href="#heart" transform="translate({x} {y + 6}) scale(4)" stroke-width="0.5"/>')
            elif k == 2:
                shapes.append(f'<use href="#star5" transform="translate({x} {y}) scale(3.6)" stroke-width="0.55"/>')
            elif k == 3:
                shapes.append(f'<rect x="{x - 32}" y="{y - 32}" width="64" height="64" rx="10" stroke-width="2"/>')
            else:
                shapes.append(f'<use href="#scallop" transform="translate({x} {y}) scale(3.4)" stroke-width="0.6"/>')
    b.append("".join(shapes))
    b.append(char("mi", 306, 740, 1.2, arms=(150, -150), mood="happy"))
    b.append(dot(518, 707, 1.0))
    return wrap("".join(b), "Color test page")


def meet_page():
    b = [f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="none" stroke-width="2.6"/>']
    b.append(txt(306, 96, "Meet the Friends", 36, "700", outline=True))
    b.append(txt(306, 124, "of Honeyfern Hollow", 15, style="italic"))
    cast = [("br", "Bramble", "gentle bear · keeps the stove warm"), ("cl", "Clover", "sunny rabbit · loves her garden"),
            ("mi", "Miso", "curious cat · draws and stargazes"), ("ju", "Juniper", "friendly fox · maps, painting, plans"),
            ("pi", "Pip", "playful puppy · games and leaf piles"), ("to", "Tofu", "quiet panda · books, tea and naps"),
            ("pb", "Pebble", "bubbly otter · collects smooth stones"), ("th", "Thimble", "tiny mouse · sews the friendship quilt")]
    scale = {"br": 0.62, "cl": 0.72, "mi": 0.9, "ju": 0.72, "pi": 0.85, "to": 0.66, "pb": 0.95, "th": 1.5}
    for i, (c, name, line) in enumerate(cast):
        col, row = i % 2, i // 2
        x0, y0 = 70 + col * 260, 150 + row * 140
        b.append(f'<rect x="{x0}" y="{y0}" width="230" height="124" rx="14" stroke-width="1.6"/>')
        b.append(char(c, x0 + 52, y0 + 116, scale[c], mood="happy" if c in ("cl", "pi") else "open"))
        b.append(txt(x0 + 160, y0 + 52, name, 20, "700"))
        part1, part2 = line.split(" · ")
        b.append(txt(x0 + 160, y0 + 76, part1, 12, style="italic") + txt(x0 + 160, y0 + 94, part2, 11.5))
    b.append(dot(110, 732, 1.4))
    b.append(txt(140, 738, "…and Dot the wren, who hides on every page. Can you spot Dot?", 14, style="italic", anchor="start"))
    return wrap("".join(b), "Meet the friends")


def thanks_page():
    b = [f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="none" stroke-width="2.6"/>']
    b.append(txt(306, 150, "Thank You", 50, "700", outline=True))
    for k, line in enumerate(("for spending a year in Honeyfern Hollow.",
                              "We hope these pages brought you a few slow, cozy moments.", "",
                              "Did you find Dot on every page?",
                              "All of Dot's hiding places are listed on the next page.", "",
                              "If you enjoyed this book, a short review helps other colorists find it,",
                              "and the friends will be glad to welcome you back to the Hollow.")):
        b.append(txt(306, 196 + k * 22, line, 15, style="italic" if k in (0, 1) else "normal"))
    for i, sym in enumerate(SYMBOLS):
        b.append(quilt_patch(146 + (i % 4) * 82, 420 + (i // 4) * 82, 76, 76, sym))
    b.append(char("br", 230, 740, 0.62, mood="happy") + char("th", 300, 740, 1.2, mood="happy") + char("to", 380, 740, 0.62, mood="happy"))
    b.append(dot(306, 403, 1.1))
    return wrap("".join(b), "Thank you")


def dot_key_page():
    b = [f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="none" stroke-width="2.6"/>']
    b.append(txt(306, 92, "Where Dot Was Hiding", 32, "700", outline=True))
    for i, where in enumerate(DOT_KEY):
        col, row = i // 25, i % 25
        b.append(txt(76 + col * 262, 132 + row * 24, f"Page {i + 1} — {where}", 11.5, anchor="start"))
    b.append(dot(306, 752, 1.0))
    return wrap("".join(b), "Where Dot was hiding")


def blank_page():
    return wrap("", "Blank backing page")


PAGES = {"fm1_title": title_page, "fm2_copyright": copyright_page, "fm3_belongs": belongs_page, "fm5_test": test_page,
         "fm7_meet": meet_page, "bm1_thanks": thanks_page, "bm2_dotkey": dot_key_page, "blank": blank_page}

if __name__ == "__main__":
    out = os.path.join(HERE, "..", "out", "svg")
    for k, f in PAGES.items():
        open(os.path.join(out, k + ".svg"), "w").write(f())
    print("wrote", len(PAGES))
