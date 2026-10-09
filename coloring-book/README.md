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

## Cover — Volume 1 (front cover only)

- `cover/cover.py` — the front cover. It reuses `src/chars.py` unchanged and only adds fill colours to a copy of the shared parts. Run `python3 cover/cover.py`, then `node cover/render_cover.mjs cover/out/<name>.svg cover/out/<name>.png` (300 DPI by default).
- `cover/out/cover-front-v1.svg` — print master: 8.5 × 11 in trim, all text converted to outlines (no font dependency), layered groups (`background`, `scenery`, `characters`, `garden`, `series-border`, `badge`, `type`).
- `cover/out/cover-front-v1-editable.svg` — the same art with live text and the OFL fonts (Fredoka, Nunito; licences in `cover/fonts/`) embedded.
- `cover/out/cover-front-v1-bleed.svg` / `.png` — the same art with 0.125 in bleed on every side (8.75 × 11.25 in, 2625 × 3375 px).
- `cover/out/cover-front-v1.png` — 2550 × 3300 px (300 DPI).
- `cover/qc_cover.mjs` — checks that type, badge, friends and Dot sit inside the 0.375 in safe area.

Full wrap (back + spine + front): `python3 cover/wrap.py`.
- Output: `cover/out/cover-wrap-v1.svg`, `.pdf` and `.png`.
- The PDF is the KDP upload file: 17.4977 × 11.25 in, vector, 0.125 in bleed.
- PDF export: `node cover/render_cover.mjs --pdf in.svg out.pdf`, then `python3 cover/fix_pdf_size.py out.pdf 17.4977 11.25`, because Chromium rounds the page size.
- Spine: 110 pages × 0.002252 in (white paper, black-and-white interior) = 0.2477 in. Change `PAGES` or `PAPER` in `wrap.py` if the interior or paper changes.
- The back cover's bottom-right 2 × 1.2 in area is left clear for KDP's barcode.
- `cover-wrap-v1-guides.*` shows trim, spine folds, safe areas and the barcode box. It is a proof only, not for print.

Series kit for Volumes 2 and 3: the two-tone Fredoka title lock-up, the stitched sage "VOLUME n" tab, the honey "50 Coloring Illustrations" rosette, the quilt-patch strip with BOOKSHELF beneath it, and the stitched cream border.
