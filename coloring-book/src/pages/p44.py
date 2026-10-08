"""Page 44 — First Snow Evening (the cottage garden at dusk)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, pine, cottage_small
from props import lantern_hanging, scarf, snowflake

TITLE = "Page 44 — First Snow Evening"


def snow_cap(x, y, w, h=10):
    return f'<path d="M{x - 4} {y} Q{x - 6} {y - h} {x + w*0.25:.0f} {y - h} Q{x + w*0.5:.0f} {y - h - 4} {x + w*0.75:.0f} {y - h} Q{x + w + 6} {y - h} {x + w + 4} {y} Z" stroke-width="1.6"/>'


def build():
    b = []
    # dusk sky with the moon rising, distant cottages of the Hollow
    b.append('<path d="M110 70 A30 30 0 1 0 140 120 A24 24 0 0 1 110 70 Z" stroke-width="1.8"/>')
    b.append('<path d="M30 330 C160 300 260 320 360 310 V800 H30 Z" stroke-width="1.5"/>')
    b.append(cottage_small(90, 320, 26) + cottage_small(170, 310, 22) + cottage_small(250, 314, 24))
    b.append(snow_cap(77, 312, 26, 6) + snow_cap(159, 302, 22, 6) + snow_cap(238, 306, 24, 6))
    # Bramble's cottage, set back on the upper right: stone chimney, round door, round window glowing
    b.append(clip_d("M454 100 H496 V230 H454 Z", lines(" ".join(f"M454 {y} H496" for y in range(115, 230, 15)) + " " + " ".join(f"M{475 + (10 if (y // 15) % 2 else -10)} {y} V{y + 15}" for y in range(100, 230, 15)), 1), 1.8))
    b.append(snow_cap(452, 100, 46, 10))
    b.append(clip_d("M340 260 H600 V430 H340 Z", "", 1.9))
    b.append('<path d="M320 266 L470 150 L620 266 Z" stroke-width="2"/><path d="M314 268 Q316 246 340 246 L470 140 L600 246 Q624 246 626 268 Q470 262 314 268 Z" stroke-width="1.8"/>')
    b.append('<circle cx="410" cy="340" r="36" stroke-width="2"/><circle cx="410" cy="340" r="29" stroke-width="1.3"/>' + lines("M410 311 V369 M381 340 H439", 1.8)
             + lines("M392 322 l-6 -6 M428 322 l6 -6 M392 358 l-6 6 M428 358 l6 6", 1))
    b.append(snow_cap(372, 382, 76, 8))
    b.append('<path d="M500 430 V362 A30 30 0 0 1 560 362 V430 Z" stroke-width="1.9"/><circle cx="548" cy="398" r="3.5" stroke-width="1.2"/>')
    b.append(lantern_hanging(486, 300, 0.8, 16))
    # picket fence capped with snow, pine trees, bird feeder with a snow cap
    b.append("".join(f'<path d="M{x} 470 V440 L{x + 7} 432 L{x + 14} 440 V470 Z" stroke-width="1.3"/>' + snow_cap(x, 438, 14, 5) for x in range(330, 600, 24)) + lines("M326 448 H600 M326 462 H600", 1.2))
    for (x, base, h) in ((60, 470, 150), (130, 480, 120)):
        b.append(f'<rect x="{x - 6}" y="{base - 20}" width="12" height="30" stroke-width="1.4"/>')
        b.append(pine(x, [(base - h, base - h * 0.55, 30), (base - h * 0.7, base - h * 0.25, 44), (base - h * 0.45, base, 56)], 1.6, 4))
        b.append(snow_cap(x - 22, base - h * 0.55, 44, 6) + snow_cap(x - 36, base - h * 0.25, 72, 6))
    b.append('<rect x="276" y="380" width="8" height="120" stroke-width="1.5"/><path d="M258 384 L280 366 L302 384 Z" stroke-width="1.6"/>'
             '<rect x="262" y="384" width="36" height="24" stroke-width="1.6"/><path d="M256 408 H304 V414 H256 Z" stroke-width="1.4"/>' + snow_cap(256, 372, 48, 10))
    # stack of firewood under snow
    b.append("".join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="11" stroke-width="1.5"/><circle cx="{x}" cy="{y}" r="4" stroke-width="0.9"/>'
                     for x, y in ((520, 520), (544, 520), (568, 520), (532, 500), (556, 500), (544, 480))) + snow_cap(518, 470, 52, 8))
    # snowy garden ground
    b.append('<path d="M30 500 Q200 480 400 500 Q520 510 600 500 V800 H30 Z" stroke-width="1.6"/>')
    # the snowman in a spare pom-pom hat like Pip's (Dot on the hat)
    b.append('<circle cx="140" cy="640" r="62" stroke-width="2"/><circle cx="140" cy="548" r="44" stroke-width="2"/><circle cx="140" cy="476" r="32" stroke-width="2"/>')
    b.append('<circle cx="128" cy="470" r="3.4" fill="#000" stroke="none"/><circle cx="152" cy="470" r="3.4" fill="#000" stroke="none"/>'
             '<path d="M140 478 L170 486 L140 486 Z" stroke-width="1.5"/>'
             + "".join(f'<circle cx="140" cy="{y}" r="5" stroke-width="1.4"/>' for y in (530, 556, 610, 640)))
    b.append(lines("M100 540 L58 510 M66 516 L56 500 M180 540 L222 506 M214 512 L226 496", 2.6))
    b.append('<g transform="translate(140 468) scale(0.95)"><use href="#pi-hat" transform="translate(0 -20)" stroke-width="2.1"/></g>')
    b.append(dot(140, 400, 0.9))
    # Pip and Clover finishing the snowman (scarves and mittens on)
    b.append(char("pi", 226, 690, 1.15, arms=(110, -14), mood="happy", wag=True))
    b.append(scarf(226, 690 - 46 * 1.15, 44, 1.0, -1))
    b.append(char("cl", 60, 744, 1.15, arms=(14, -120), mood="happy", front='<path d="M-20 -56 Q0 -50 20 -56 L20 -46 Q0 -40 -20 -46 Z" stroke-width="1.3"/>'))
    # Pebble making a snow angel
    b.append('<path transform="translate(-30 0)" d="M330 640 C280 600 290 560 330 580 C330 540 400 540 400 580 C440 560 450 600 400 640 C420 680 380 720 365 700 C350 720 310 680 330 640 Z" stroke-width="1.5"/>')
    b.append(char("pb", 335, 670, 1.1, arms=(150, -150), mood="happy"))
    # Bramble pulling the sled with the lantern toward the cottage
    b.append('<path d="M470 740 H570 Q588 740 588 724 M470 740 Q454 740 454 724" fill="none" stroke-width="3"/>'
             '<rect x="472" y="704" width="112" height="20" rx="4" stroke-width="2"/>' + lines("M488 724 V738 M566 724 V738", 2.4))
    b.append(lantern_hanging(530, 642, 0.9, 6))
    b.append(char("br", 430, 744, 1.0, arms=(30, -60), head_rot=-6))
    bx, by = paw("br", 430, 744, 1.0, "R", -60)
    b.append(lines(f"M{bx:.0f} {by:.0f} Q470 700 476 712", 1.6))
    b.append(scarf(430, 744 - 106, 52, 1.0, 1))
    # snowflakes of two sizes
    for k, (x, y) in enumerate(((60, 120), (200, 60), (300, 120), (390, 70), (560, 60), (240, 200), (330, 200), (180, 260), (540, 180), (80, 230),
                                 (380, 460), (300, 540), (470, 560), (560, 640), (250, 760), (40, 400), (220, 440))):
        b.append(snowflake(x, y, 1.3 if k % 2 else 0.85))
    return "".join(b)


def svg():
    return page(build(), TITLE)
