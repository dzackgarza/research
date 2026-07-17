#!/usr/bin/env python3
"""Add a web citation to docs/refs-web.bib by scraping its canonical source.

Citations can't be hallucinated: the BibTeX comes from the publisher's own
/cite page, never from the model.

  cite_add.py nlab "category of elements"      # or a full ncatlab.org URL
  cite_add.py stacks 0A8C                       # validates the tag exists

nLab: scrapes <page>/cite, extracts the canonical `@misc{nlab:...}` entry, and
appends it to docs/refs-web.bib (deduped). Cite it as [@nlab:<slug>].
Stacks: one global entry (The25); this only verifies the tag resolves. Cite it
as [@stacks-<tag>] — the stacks-tags.lua filter links it to the tag page.
"""
import re
import sys
import urllib.request
from pathlib import Path

BIB = Path("docs/refs-web.bib")
UA = {"User-Agent": "Mozilla/5.0 (docs cite_add)"}


def fetch(url: str) -> str:
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30).read().decode("utf-8", "replace")


def add_nlab(arg: str) -> None:
    if arg.startswith("http"):
        base = arg.rstrip("/").removesuffix("/cite")
    else:
        base = "https://ncatlab.org/nlab/show/" + arg.strip().replace(" ", "+")
    # fetch() follows redirects and raises on 404 — a page that cannot be verified
    # to exist is never cited. Resolve to the canonical page the redirect lands on.
    resp = urllib.request.urlopen(urllib.request.Request(base + "/cite", headers=UA), timeout=30)
    final = resp.geturl().removesuffix("/cite")
    html = resp.read().decode("utf-8", "replace")
    m = re.search(r"@misc\{nlab:[^@]*?\n\}", html.replace("&amp;", "&"), re.S)
    if not m:
        sys.exit(f"cite_add: could not find a BibTeX entry at {final}/cite")
    entry = m.group(0).strip()
    # normalize the key to a valid citekey (nLab emits commas/spaces, which are illegal
    # and break the whole bibliography parse). Derive it deterministically from the slug.
    slug = final.rsplit("/show/", 1)[-1]
    key = "nlab:" + re.sub(r"[^A-Za-z0-9_-]", "", slug.replace("+", "_").replace(",", ""))
    entry = re.sub(r"^@misc\{[^\n]*,", f"@misc{{{key},", entry, count=1)
    existing = BIB.read_text() if BIB.exists() else ""
    if f"{{{key}," in existing:
        print(f"already present: [@{key}]")
        return
    BIB.write_text(existing.rstrip() + "\n\n" + entry + "\n")
    print(f"added [@{key}] from {final}/cite")


def check_stacks(tag: str) -> None:
    tag = tag.strip().upper()
    try:
        urllib.request.urlopen(urllib.request.Request(
            f"https://stacks.math.columbia.edu/tag/{tag}", headers=UA), timeout=30).read(1)
    except Exception as e:
        sys.exit(f"cite_add: Stacks tag {tag} does not resolve ({e})")
    print(f"Stacks tag {tag} verified. Cite as [@stacks-{tag}] (links via The25).")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("nlab", "stacks"):
        sys.exit(__doc__)
    (add_nlab if sys.argv[1] == "nlab" else check_stacks)(sys.argv[2])
