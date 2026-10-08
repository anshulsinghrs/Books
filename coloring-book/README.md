# Cozy Little Friends — production pipeline

Code-generated SVG line art for the 50-illustration coloring book (8.5 × 11 in KDP paperback, no bleed).

- `src/chars.py` — the character model: every friend, Dot and the eight quilt symbols as shared SVG parts. Pages only place characters with `char(...)`, so proportions and accessories never drift.
- `src/scene.py` — reusable scenery (fences, ferns, pumpkins, blossoms, clipping helper).
- `src/pages/pNN.py` — one module per page of the production bible.
- `src/model_sheet.py` — Stage 1 model sheet.
- `tools/render.mjs` — Chromium renderer: PNG previews, or `--pdf out.pdf a.svg b.svg ...` for an interior PDF.

Build: `python3 src/build.py [p01 p08 ...]` → `out/svg/*.svg` + `out/png/*.png`.

Page format: viewBox 612 × 792 pt; all art is clipped to the live area (x 45–576, y 36–756 = 0.625 in gutter side, 0.5 in elsewhere). Black #000 on white only; no text in illustrations; Dot appears once per page.

Status: Stage 1 (model sheet) and Stage 2 (benchmark pages 1, 8, 15, 21, 28, 35, 41, 50) done.
