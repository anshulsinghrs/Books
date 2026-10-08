"""Assemble the KDP interior: front matter, 50 illustrations each backed by a blank page, back matter."""
import os, subprocess, json
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SVG = os.path.join(ROOT, "out", "svg")
seq = ["fm1_title", "fm2_copyright", "fm3_belongs", "blank", "fm5_test", "blank", "fm7_meet", "blank"]
for n in range(1, 51):
    seq += [f"p{n:02d}", "blank"]
seq += ["bm1_thanks", "bm2_dotkey"]
files = [os.path.join(SVG, s + ".svg") for s in seq]
out = os.path.join(ROOT, "out", "Cozy-Little-Friends-interior.pdf")
subprocess.run(["node", os.path.join(ROOT, "tools", "render.mjs"), "--pdf", out] + files, check=True)
json.dump(seq, open(os.path.join(ROOT, "out", "interior-sequence.json"), "w"), indent=0)
print(len(seq), "pages ->", out)
