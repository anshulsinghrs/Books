"""Turn text into SVG path outlines (so the cover never depends on installed fonts)."""
import os
from functools import lru_cache
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = {"fredoka": "Fredoka.ttf", "nunito": "Nunito.ttf"}


@lru_cache(None)
def font(name, wght):
    f = TTFont(os.path.join(HERE, "fonts", FONTS[name]))
    axes = {a.axisTag for a in f["fvar"].axes}
    loc = {"wght": wght}
    if "wdth" in axes:
        loc["wdth"] = 100
    return instancer.instantiateVariableFont(f, loc)


def _kern(f):
    pairs = {}
    if "GPOS" not in f:
        return pairs
    for lookup in f["GPOS"].table.LookupList.Lookup:
        for st in lookup.SubTable:
            if lookup.LookupType == 9:
                st = st.ExtSubTable
            if getattr(st, "LookupType", None) != 2 or st.Format != 1:
                continue
            cov = st.Coverage.glyphs
            for i, ps in enumerate(st.PairSet):
                for pv in ps.PairValueRecord:
                    v = pv.Value1.XAdvance if pv.Value1 and hasattr(pv.Value1, "XAdvance") else 0
                    if v:
                        pairs[(cov[i], pv.SecondGlyph)] = v
    return pairs


@lru_cache(None)
def kerning(name, wght):
    return _kern(font(name, wght))


def text_width(s, name, wght, size, tracking=0):
    f = font(name, wght)
    cmap, hmtx = f.getBestCmap(), f["hmtx"]
    upm = f["head"].unitsPerEm
    kern = kerning(name, wght)
    w, prev = 0, None
    for ch in s:
        g = cmap.get(ord(ch))
        if g is None:
            continue
        if prev:
            w += kern.get((prev, g), 0)
        w += hmtx[g][0] + tracking * upm / 1000
        prev = g
    return w * size / upm - tracking * size / 1000


def text_path(s, x, y, size, name="fredoka", wght=600, anchor="middle", tracking=0):
    """SVG path data for string s with its baseline at y."""
    f = font(name, wght)
    cmap, hmtx, gs = f.getBestCmap(), f["hmtx"], f.getGlyphSet()
    upm = f["head"].unitsPerEm
    sc = size / upm
    w = text_width(s, name, wght, size, tracking)
    x0 = x - (w / 2 if anchor == "middle" else w if anchor == "end" else 0)
    kern = kerning(name, wght)
    pen = SVGPathPen(gs)
    cx, prev = 0, None
    for ch in s:
        g = cmap.get(ord(ch))
        if g is None:
            continue
        if prev:
            cx += kern.get((prev, g), 0)
        tp = TransformPen(pen, (sc, 0, 0, -sc, x0 + cx * sc, y))
        gs[g].draw(tp)
        cx += hmtx[g][0] + tracking * upm / 1000
        prev = g
    return pen.getCommands()
