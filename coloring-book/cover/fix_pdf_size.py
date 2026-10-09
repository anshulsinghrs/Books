"""Set a PDF's page box to an exact size in inches (Chromium rounds page sizes to whole CSS pixels)."""
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

src, w_in, h_in = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
r = PdfReader(src)
wtr = PdfWriter()
for p in r.pages:
    top = float(p.mediabox.top)
    box = RectangleObject([0, top - h_in * 72, w_in * 72, top])
    p.mediabox = box
    p.cropbox = box
    wtr.add_page(p)
with open(src, "wb") as f:
    wtr.write(f)
print(f"{src}: {w_in} x {h_in} in")
