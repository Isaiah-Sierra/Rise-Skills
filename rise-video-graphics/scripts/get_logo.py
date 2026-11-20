#!/usr/bin/env python3
"""Export a product logo, unaltered, from an installed open logo library.

Libraries (install once, in a scratch folder, not in the video project):
    npm install --ignore-scripts @iconify-json/logos simple-icons
@iconify-json/logos is Gil Barbara's "SVG Logos" set (CC0): official marks in full color.
simple-icons (CC0) holds one-color marks with each brand's official hex. Prefer the first.

usage:
    get_logo.py <node_modules dir> search <word>        list matching names in both sets
    get_logo.py <node_modules dir> logos <name> <out.svg>
    get_logo.py <node_modules dir> simple <slug> <out.svg>
The file is written exactly as the library ships it: never recolor, crop or redraw it.
"""
import json, sys, pathlib

nm = pathlib.Path(sys.argv[1]); cmd = sys.argv[2]
logos = nm / "@iconify-json/logos/icons.json"
simple = nm / "simple-icons/icons"

if cmd == "search":
    w = sys.argv[3].lower()
    if logos.exists():
        d = json.loads(logos.read_text())
        print("logos:", [k for k in d["icons"] if w in k])
    if simple.exists():
        print("simple:", sorted(p.stem for p in simple.glob("*.svg") if w in p.stem))
elif cmd == "logos":
    d = json.loads(logos.read_text())
    i = d["icons"][sys.argv[3]]
    w, h = i.get("width", d.get("width", 256)), i.get("height", d.get("height", 256))
    pathlib.Path(sys.argv[4]).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{i["body"]}</svg>\n')
elif cmd == "simple":
    pathlib.Path(sys.argv[4]).write_text((simple / f"{sys.argv[3]}.svg").read_text())
else:
    sys.exit(__doc__)
