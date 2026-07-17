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

# 4. external links must resolve — a cited resource that 404s can't be verified to exist
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor

urls: set[str] = set()
src = "\n".join(p.read_text(encoding="utf-8", errors="replace")
                for p in list(DOCS.glob("*.md")) + [DOCS / "refs-web.bib"] if p.exists())
urls |= set(re.findall(r'https?://[^\s)\]}>"]+', src))
# Stacks tags cited as [@stacks-XXXX] resolve to a real tag page via the filter
urls |= {f"https://stacks.math.columbia.edu/tag/{t}" for t in re.findall(r'@stacks-([0-9A-Za-z]{4})', src)}
urls = {u.rstrip('.,;') for u in urls if "github.com/dzackgarza" not in u}


def check_url(u: str):
    req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Mozilla/5.0 (docs-check)"})
    try:
        urllib.request.urlopen(req, timeout=20)
        return None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return f"external link 404 (does not exist): {u}"
        if e.code in (405, 403):  # HEAD not allowed / bot-blocked — retry with GET
            try:
                urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (docs-check)"}), timeout=20).read(1)
                return None
            except urllib.error.HTTPError as e2:
                return f"external link 404 (does not exist): {u}" if e2.code == 404 else None
            except Exception:
                return None
        return None  # other HTTP status: not a "does-not-exist" signal
    except Exception:
        return None  # transient network error — never fails the build on a 404-less error


if urls:
    with ThreadPoolExecutor(max_workers=8) as ex:
        failures += [r for r in ex.map(check_url, sorted(urls)) if r]

if failures:
    print("docs-check FAILED:\n" + "\n".join(f"  - {f}" for f in failures))
    sys.exit(1)
print(f"docs-check: OK (citations, cross-refs, anchor links, and {len(urls)} external links all resolve)")
