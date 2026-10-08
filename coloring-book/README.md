# Cozy Little Friends — production pipeline

Code-generated SVG line art for the 50-illustration coloring book (8.5 × 11 in KDP paperback, no bleed).

- `src/chars.py` — the character model: every friend, Dot and the eight quilt symbols as shared SVG parts. Pages only place characters with `char(...)`, so proportions and accessories never drift.
- `src/scene.py` — reusable scenery (fences, ferns, pumpkins, blossoms, clipping helper).
- `src/pages/pNN.py` — one module per page of the production bible.
- `src/model_sheet.py` — Stage 1 model sheet.
- `tools/render.mjs` — Chromium renderer: PNG previews, or `--pdf out.pdf a.svg b.svg ...` for an interior PDF.

Build: `python3 src/build.py [p01 p08 ...]` → `out/svg/*.svg` + `out/png/*.png`.

Page format: viewBox 612 × 792 pt; all art is clipped to the live area (x 45–576, y 36–756 = 0.625 in gutter side, 0.5 in elsewhere). Black #000 on white only; no text in illustrations; Dot appears once per page.

- `src/props.py` — recurring props (teapot, stove, mugs, pancake stack, umbrellas, quilt patches…) so returning objects stay identical.
- `src/matter.py` — front matter, blank backing page, back matter (Thank you + Dot answer key).
- `tools/validate.py` — book-level checks (XML, size, B/W, no text, one Dot, margins, solid-black areas, duplicates) → `out/validation.json`.
- `tools/assemble.py` — builds `out/Cozy-Little-Friends-interior.pdf` (110 pages).

Full rebuild: `python3 src/build.py && python3 src/matter.py && python3 tools/validate.py && python3 tools/assemble.py`

Status: all 50 illustrations done and validated; interior PDF assembled (proof in `out/proof/`).
