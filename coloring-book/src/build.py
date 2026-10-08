"""Build page SVGs (and PNG previews). usage: python3 build.py [p01 p08 ...]"""
import importlib, sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.join(HERE, "..", "out")
names = sys.argv[1:] or sorted(f[:-3] for f in os.listdir(os.path.join(HERE, "pages")) if f.startswith("p") and f.endswith(".py"))
files = []
for n in names:
    m = importlib.import_module(f"pages.{n}")
    path = os.path.join(OUT, "svg", f"{n}.svg")
    open(path, "w").write(m.svg())
    files.append(path)
subprocess.run(["node", os.path.join(HERE, "..", "tools", "render.mjs"), os.path.join(OUT, "png")] + files, check=True)
