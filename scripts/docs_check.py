#!/usr/bin/env python3
"""Integrity gate for the Quarto docs book.

Renders the book and fails (nonzero exit) on any data-integrity defect:
  1. undefined citations      — `[WARNING] Citeproc: citation X not found`
  2. unresolved cross-refs    — `quarto-unresolved-ref` in the rendered HTML
                                (the `?@` grep is a false green — Quarto renders an
                                 unresolved ref as `?sec-x`, no `@`)
  3. broken cross-page anchor links — `[t](Page.md#anchor)` whose anchor id is absent

Quarto binary from $QUARTO (default `quarto`). Run: `just docs-check`.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

DOCS = Path("docs")
SITE = DOCS / "_site"
QUARTO = os.environ.get("QUARTO", "quarto")

failures: list[str] = []

# --- render, capturing warnings -------------------------------------------------
proc = subprocess.run(
    [QUARTO, "render", str(DOCS)],
    capture_output=True, text=True,
)
log = proc.stdout + proc.stderr
if proc.returncode != 0:
    print(log)
    sys.exit(f"docs-check: `quarto render` failed (exit {proc.returncode})")

# 1. undefined citations
missing = sorted(set(re.findall(r"citation (\S+) not found", log)))
if missing:
    failures.append("undefined citations (not in any bibliography): " + ", ".join(missing))

# 2. unresolved cross-references
for html in sorted(SITE.glob("*.html")):
    hits = html.read_text(encoding="utf-8", errors="replace").count("quarto-unresolved-ref")
    if hits:
        refs = sorted(set(re.findall(r'quarto-unresolved-ref[^>]*>\?([\w-]+)',
                                     html.read_text(encoding="utf-8", errors="replace"))))
        failures.append(f"{html.name}: {hits} unresolved cross-ref(s): {', '.join(refs)}")

# 3. broken cross-page anchor links
ids = {h.stem: set(re.findall(r'id="([^"]+)"', h.read_text(encoding="utf-8", errors="replace")))
       for h in SITE.glob("*.html")}
for md in DOCS.glob("*.md"):
    for m in re.finditer(r'\]\(([A-Za-z0-9\-]+)\.(?:md|html)#([^)]+)\)', md.read_text(encoding="utf-8", errors="replace")):
        page, anchor = m.group(1), m.group(2)
        if page in ids and anchor not in ids[page]:
            failures.append(f"{md.name}: broken anchor link -> {page}#{anchor}")

if failures:
    print("docs-check FAILED:\n" + "\n".join(f"  - {f}" for f in failures))
    sys.exit(1)
print("docs-check: OK (citations resolve, cross-refs resolve, anchor links resolve)")
