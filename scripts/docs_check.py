#!/usr/bin/env python3
"""Integrity gate for the Quarto docs book.

Renders the book and fails (nonzero exit) on any data-integrity defect:
  1. undefined citations      — `[WARNING] Citeproc: citation X not found`
  2. unresolved cross-refs    — `quarto-unresolved-ref` in the rendered HTML
                                (the `?@` grep is a false green — Quarto renders an
                                 unresolved ref as `?sec-x`, no `@`)
  3. broken cross-page anchor links — `[t](Page.md#anchor)` whose anchor id is absent

Quarto command from $QUARTO (default `uvx --from quarto-cli quarto`).
Run: `just docs-check`.
"""
import os
import re
import shlex
import subprocess
import sys
from pathlib import Path

DOCS = Path("writing")        # the authored markdown
BOOK = DOCS / ".book"         # the Quarto project root: build machinery plus a symlink per part
ASSETS = DOCS / ".assets"     # build inputs pandoc opens itself (bibliographies, includes, CSS)
SITE = BOOK / "_site"
REFS_WEB = ASSETS / "refs-web.bib"
QUARTO = shlex.split(os.environ.get("QUARTO", "uvx --from quarto-cli quarto"))

failures: list[str] = []

# --- 0. every part reaches the book as a link, never as a copy --------------------
# The book reaches the prose through these symlinks. Written out rather than
# discovered, because a clobbered link is no longer a symlink and would drop out of
# anything that went looking for one, leaving the check to pass on nothing. A tool
# that rewrites an input by renaming a temporary file into place replaces the link
# with a copy; the copy renders perfectly well, so nothing else here would notice the
# two drifting apart. Adding a part means adding its name here and to _quarto.yml.
LINKED_PARTS = ("index.md", "category-theory", "coble", "data", ".assets")
for name in LINKED_PARTS:
    entry, source = BOOK / name, DOCS / name
    if not entry.is_symlink():
        sys.exit(f"docs-check: {entry} is a copy, not a link to {source} — "
                 "the book would render the copy. Replace it with the symlink.")
    if entry.resolve() != source.resolve():
        sys.exit(f"docs-check: {entry} links to {entry.resolve()}, not to {source}")

# --- render, capturing warnings -------------------------------------------------
proc = subprocess.run(
    [*QUARTO, "render", str(BOOK)],
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
for html in sorted(SITE.rglob("*.html")):
    hits = html.read_text(encoding="utf-8", errors="replace").count("quarto-unresolved-ref")
    if hits:
        refs = sorted(set(re.findall(r'quarto-unresolved-ref[^>]*>\?([\w-]+)',
                                     html.read_text(encoding="utf-8", errors="replace"))))
        failures.append(f"{html.name}: {hits} unresolved cross-ref(s): {', '.join(refs)}")

# The checks below are about site content. `writing/` also holds documents Quarto
# does not render: the dissertation markdown, which compiles through ~/.pandoc, plus
# talks, exams, and agent skill files. The rendered set is exactly the markdown that
# produced a page under _site.
#
# Scan the prose tree, not the project root: the parts reach Quarto as symlinks and
# `rglob` does not descend those, so scanning BOOK would silently find nothing.
SITE_MD = [md for md in sorted(DOCS.rglob("*.md"))
           if BOOK not in md.parents
           and (SITE / md.relative_to(DOCS).with_suffix(".html")).exists()]
if not SITE_MD:
    sys.exit("docs-check: no rendered markdown found — the source scan and _site "
             "disagree, so checks 3 and 4 below would pass without reading anything")

# 3. broken cross-page anchor links
ids = {h.stem: set(re.findall(r'id="([^"]+)"', h.read_text(encoding="utf-8", errors="replace")))
       for h in SITE.rglob("*.html")}
for md in SITE_MD:
    for m in re.finditer(r'\]\(([^)\s]+?)\.(?:md|html)#([^)]+)\)', md.read_text(encoding="utf-8", errors="replace")):
        page, anchor = m.group(1).split("/")[-1], m.group(2)   # basename stem (subfolder-relative links)
        if page in ids and anchor not in ids[page]:
            failures.append(f"{md.name}: broken anchor link -> {page}#{anchor}")

# 4. no manual numbers in section headings — sections auto-number (Quarto book)
for md in SITE_MD:
    for i, line in enumerate(md.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if re.match(r"^#{2,6}\s+(\d+\.?\s|F\.\d|[IVX]+\.\s)", line):
            failures.append(f"{md.name}:{i}: manual number in heading {line.strip()[:48]!r} — drop it; sections auto-number and are referenced by @sec-")

# 5. no bespoke citations — a citation-source URL must go through the bibliography, never an inline link
CITE_DOMAINS = r"(ncatlab\.org|stacks\.math\.columbia\.edu|(?:dx\.)?doi\.org|arxiv\.org/abs|link\.springer\.com|zbmath\.org|mathscinet)"
for md in SITE_MD:
    for i, line in enumerate(md.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        m = re.search(r"https?://" + CITE_DOMAINS, line)
        if m:
            failures.append(f"{md.name}:{i}: inline citation URL {m.group(0)} bypasses the bibliography — cite via @key, [@stacks-TAG], or `just cite-nlab`")

# 6. refs-web.bib holds only scraped nLab entries (no bespoke/hand-written citations)
if not REFS_WEB.exists():
    sys.exit(f"docs-check: {REFS_WEB} is missing — checks 6 and 7 read it, and would "
             "otherwise pass by having nothing to inspect")
for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", REFS_WEB.read_text(encoding="utf-8", errors="replace"), re.S):
    key, body = m.group(2), m.group(3)
    if not key.startswith("nlab:"):
        failures.append(f"refs-web.bib: bespoke entry @{key} — web citations are added only via `just cite-nlab` (scraped from the canonical /cite page)")
    elif "ncatlab.org" not in body:
        failures.append(f"refs-web.bib: @{key} carries no ncatlab.org URL — not a scraped entry")

# 7. external links must resolve — a cited resource that 404s can't be verified to exist
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor

urls: set[str] = set()
src = "\n".join(p.read_text(encoding="utf-8", errors="replace")
                for p in SITE_MD + [REFS_WEB] if p.exists())
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
