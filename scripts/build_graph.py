#!/usr/bin/env python3
"""Regenerate the interactive category graph from its DOT manifest."""

import subprocess
from pathlib import Path

DOT = Path("docs/lean/category-graph.dot")
TEMPLATE = Path("docs/lean/_category-graph-template.html")
OUT = Path("docs/lean/category-graph.html")

svg = subprocess.run(
    ["dot", "-Tsvg", str(DOT)],
    capture_output=True,
    text=True,
    check=True,
).stdout
svg = svg[svg.find("<svg") :]

template = TEMPLATE.read_text()
assert template.count("%SVG%") == 1
OUT.write_text(template.replace("%SVG%", svg))
print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
