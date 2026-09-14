#!/usr/bin/env python3
"""Regenerate docs/refs-web.bib from canonical sources.

Every entry is re-scraped from its own nLab /cite page, so any hand-edit is
overwritten and any page that has 404'd blocks (forcing an audit). This is why
refs-web.bib is never hand-maintained: `just cite-nlab <page>` adds; this
refreshes. Run: `just refs-web-refresh`.
"""
import re
from pathlib import Path

import cite_add  # sibling module

BIB = Path("docs/refs-web.bib")
HEADER = (
    "% Project-local citations scraped from canonical sources (nLab /cite, etc.).\n"
    "% Mixed with the shared ~/.pandoc bib at resolve time. Add via `just cite-nlab <url>`;\n"
    "% regenerate via `just refs-web-refresh` — this file is never hand-edited.\n"
)

urls = re.findall(r"howpublished\s*=\s*\{\\url\{(https://ncatlab\.org/nlab/show/[^}]+)\}\}", BIB.read_text())
BIB.write_text(HEADER)
for url in urls:
    cite_add.add_nlab(url)
print(f"regenerated refs-web.bib from {len(urls)} canonical nLab sources")
