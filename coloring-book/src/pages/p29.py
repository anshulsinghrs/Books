"""Page 29 — Making Camp (edge of Lantern Hill among tall pines)."""
from chars import char, arms_only, dot, page, paw
from scene import clip_d, lines, pine, tuft, daisy
from props import kettle, mug, icon, lantern_hanging

TITLE = "Page 29 — Making Camp"


def pinecone(x, y, s=1.0, rot=0):
    sc = "".join(f'<path d="M{dx} {dy} q-6 5 0 10 q6 -5 0 -10 Z"/>' for dx, dy in ((-5, -4), (5, -4), (0, -12), (-6, 6), (6, 6), (0, -2)))
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})" stroke-width="{1.1/s:.2f}"><ellipse rx="11" ry="16"/>{sc}</g>'


def backpack(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})" stroke-width="{1.6/s:.2f}">'
            '<path d="M-26 0 V-46 Q-26 -62 0 -62 Q26 -62 26 -46 V0 Z"/>'
            '<path d="M-26 -40 Q0 -30 26 -40 L24 -56 Q0 -66 -24 -56 Z"/><rect x="-5" y="-40" width="10" height="9" rx="2"/>'
            '<rect x="-16" y="-24" width="32" height="20" rx="5"/>'
            '<rect x="-34" y="-82" width="58" height="20" rx="4"/><ellipse cx="24" cy="-72" rx="7" ry="10"/><ellipse cx="24" cy="-72" rx="3" ry="5" stroke-width="1"/>'
            '<path d="M-14 -82 V-62 M8 -82 V-62" fill="none" stroke-width="1"/></g>')


def build():
    b = []
    b.append('<use href="#cloud" transform="translate(300 80) scale(1)" stroke-width="1.5"/>')
    # row of pines along the back, one tall pine cropping off the top right
    for (x, base, h, w) in ((70, 420, 200, 60), (140, 410, 240, 70), (230, 420, 180, 56), (310, 400, 230, 66), (400, 420, 200, 60)):
        b.append(f'<rect x="{x - 6}" y="{base - 30}" width="12" height="40" stroke-width="1.4"/>')
        b.append(pine(x, [(base - h, base - h*0.55, w*0.5), (base - h*0.7, base - h*0.25, w*0.75), (base - h*0.45, base, w)], 1.5, 4))
    b.append('<rect x="508" y="300" width="24" height="160" stroke-width="1.8"/>')
    b.append(pine(520, [(0, 120, 46), (60, 220, 66), (140, 320, 86), (220, 420, 100)], 1.8, 5))
    b.append(lines("M500 150 l5 6 l5 -6 M540 250 l5 6 l5 -6 M470 340 l5 6 l5 -6 M556 380 l5 6 l5 -6", 1))
    b.append('<path d="M30 420 C200 404 400 416 600 400 V800 H30 Z" stroke-width="1.6"/>')
    # A-frame tent with an open flap and guy ropes (Dot on the ridge pole)
    b.append(lines("M40 600 L80 330 M250 600 L210 330", 1.2))
    b.append('<path d="M70 600 L150 330 L230 600 Z" stroke-width="2.2"/>' + lines("M110 466 L150 330 L190 466", 1))
    b.append('<path d="M150 400 L118 600 H182 Z" stroke-width="1.6"/>')
    b.append('<path d="M150 400 L182 600 L214 560 Z" stroke-width="1.8"/>')
    b.append('<rect x="146" y="314" width="8" height="20" stroke-width="1.4"/>' + lines("M40 600 l6 -2 M250 600 l-6 -2", 2))
    b.append(dot(150, 304))
    # lantern on a hook post
    b.append('<rect x="262" y="470" width="8" height="130" stroke-width="1.6"/>' + lines("M266 474 H290", 2))
    b.append(lantern_hanging(288, 474, 0.9, 10))
    # stone fire ring with the unlit wood
    for k in range(10):
        import math
        a = 2 * math.pi * k / 10
        x, y = 360 + 52 * math.cos(a), 640 + 18 * math.sin(a)
        b.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="15" ry="10" stroke-width="1.6"/>')
    b.append('<path d="M330 640 L370 610 L376 616 L338 646 Z M392 638 L350 614 L346 620 L386 644 Z" stroke-width="1.5"/>')
    # Pip proudly dragging a long stick toward the ring
    b.append(char("pi", 250, 716, 1.25, arms=(60, -14), mood="happy", wag=True))
    sx, sy = paw("pi", 250, 716, 1.25, "L", 60)
    b.append(f'<path d="M{sx:.1f} {sy - 4:.1f} L{sx - 140:.1f} {sy + 50:.1f} L{sx - 138:.1f} {sy + 58:.1f} L{sx + 2:.1f} {sy + 4:.1f} Z" stroke-width="1.6"/>'
             + lines(f"M{sx - 60:.1f} {sy + 22:.1f} l-8 -16 M{sx - 100:.1f} {sy + 38:.1f} l-4 14", 1.4))
    b.append(arms_only("pi", 250, 716, 1.25, (60, None)))
    # Juniper studying the map, compass at his feet
    jx, jy, js = 470, 744, 1.25
    b.append(char("ju", jx, jy, js, arms=(None, None), brows=True))
    lx, ly = paw("ju", jx, jy, js, "L", -40)
    b.append(f'<path d="M{lx - 30:.0f} {ly - 40:.0f} L{lx + 60:.0f} {ly - 46:.0f} L{lx + 64:.0f} {ly + 14:.0f} L{lx - 26:.0f} {ly + 20:.0f} Z" stroke-width="1.8"/>'
             + lines(f"M{lx:.0f} {ly - 43:.0f} L{lx + 4:.0f} {ly + 17:.0f} M{lx + 30:.0f} {ly - 45:.0f} L{lx + 34:.0f} {ly + 16:.0f}", 0.9)
             + icon("tree", lx - 14, ly - 18, 0.7) + icon("star", lx + 46, ly - 22, 0.6)
             + f'<path d="M{lx + 4:.0f} {ly + 6:.0f} Q{lx + 14:.0f} {ly - 10:.0f} {lx + 22:.0f} {ly + 4:.0f} Q{lx + 30:.0f} {ly + 14:.0f} {lx + 40:.0f} {ly - 4:.0f}" fill="none" stroke-width="1.2"/>')
    b.append(arms_only("ju", jx, jy, js, (-40, 40)))
    b.append('<circle cx="380" cy="736" r="14" stroke-width="1.7"/><circle cx="380" cy="736" r="10" stroke-width="1"/><path d="M380 728 L383 736 L380 744 L377 736 Z" stroke-width="1" fill="#000"/>')
    # backpacks with bedrolls, folding stool with kettle and enamel mugs, pinecones
    b.append(backpack(80, 720, 1.0) + backpack(144, 740, 0.85))
    b.append(lines("M400 520 L450 580 M450 520 L400 580", 4) + '<rect x="392" y="512" width="66" height="10" rx="3" stroke-width="1.7"/>')
    b.append(kettle(412, 510, 0.45, steam=False) + mug(446, 512, 0.75, "dots"))
    b.append(mug(330, 748, 1.0, "plain"))
    b.append(pinecone(560, 620, 0.9, 20) + pinecone(208, 650, 0.8, -30) + pinecone(60, 620, 0.8, 10))
    b.append(tuft(250, 650) + tuft(420, 640) + tuft(580, 700))
    return "".join(b)


def svg():
    return page(build(), TITLE)
