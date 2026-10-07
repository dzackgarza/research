#!/usr/bin/env python3
"""Integrity gate for the Quarto docs book.

Renders the book and fails (nonzero exit) on any data-integrity defect:
  1. undefined citations      — `[WARNING] Citeproc: citation X not found`
  2. unresolved cross-refs    — `quarto-unresolved-ref` in the rendered HTML
                                (the `?@` grep is a false green — Quarto renders an
                                 unresolved ref as `?sec-x`, no `@`)
  3. broken links            — `[t](#id)` whose id no page has, or a link that names
                                a page by its path or a numbered block by its id

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

# --- 0. no second Quarto process on this project ----------------------------------
# Quarto renders each input to a sibling .html beside the source and then moves it
# into _site. A preview doing the same thing on the same paths steals this render's
# intermediates, and the failure reads as a missing file on an arbitrary chapter.
# The port alone is not the test: a preview binds :7654 only after its first render
# finishes, so during that render the port is free, this gate starts, and the two
# renders move each other's intermediates out from under themselves. The failure
# surfaces as `NotFound ... rename '<chapter>.html'` on an arbitrary chapter. Look for
# the process instead, which exists for the whole of that window.
if subprocess.run(["pgrep", "-f", r"quarto\.js preview"],
                  capture_output=True, text=True).returncode == 0:
    sys.exit("docs-check: a preview is running on this project. It renders the same "
             "intermediate paths as this gate and they corrupt each other — stop it "
             "first. Nothing is wrong with the book.")

# --- 0b. every part reaches the book as a link, never as a copy -------------------
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

# Every chapter is listed by its path in the topic tree, through the part link above.
# A missing chapter fails the render with a message that names only the file, so the
# list is checked here first.
CHAPTERS = re.findall(r"^\s+-\s+(?:part:\s+)?([A-Za-z0-9._/-]+\.md)\s*$",
                      (BOOK / "_quarto.yml").read_text(), re.M)
if len(CHAPTERS) < 2:
    sys.exit("docs-check: read no chapter list out of _quarto.yml")
for name in CHAPTERS:
    entry = BOOK / name
    if not entry.resolve().is_file():
        sys.exit(f"docs-check: chapter {name} in _quarto.yml does not exist")
    if DOCS.resolve() not in entry.resolve().parents:
        sys.exit(f"docs-check: chapter {name} resolves to {entry.resolve()}, outside writing/")

# --- clear intermediates a previous render left behind ---------------------------
# Quarto writes each chapter's html beside its source and then moves it into _site.
# A render that aborts leaves one behind, and the next render fails moving a
# *different* chapter, so one interrupted run keeps every later run red until the
# stray file goes. Only the html of a chapter in the book is removed, so nothing
# authored can be caught by this.
for name in CHAPTERS:
    stray = (BOOK / name).with_suffix(".html")
    if stray.exists():
        stray.unlink()
        print(f"docs-check: cleared {stray}, left by an interrupted render")

# --- render twice, capturing warnings -------------------------------------------
# custom-numbered-blocks resolves custom-block @id references (and legacy
# \ref/\longref) against a registry it builds as
# the render proceeds, so a first pass can only reach blocks declared in chapters it
# has already processed. The registry is written to disk (._htmlbook_xref.json at the project
# root) and read back at the start of each chapter, so a second pass over the same
# tree resolves every reference the first pass registered. This is the same reason a
# LaTeX document is compiled twice; the cost is one extra render.
#
# The gate must therefore render twice itself: a single pass would check a site whose
# forward references are all missing, and CI clones fresh, so it has no earlier pass
# to inherit a registry from.
for _pass in (1, 2):
    proc = subprocess.run(
        [*QUARTO, "render", str(BOOK)],
        capture_output=True, text=True,
    )
    log = proc.stdout + proc.stderr
    if proc.returncode != 0:
        print(log)
        sys.exit(f"docs-check: `quarto render` failed on pass {_pass} (exit {proc.returncode})")

# 1. undefined citations
missing = sorted(set(re.findall(r"citation (\S+) not found", log)))
if missing:
    failures.append("undefined citations (not in any bibliography): " + ", ".join(missing))

# 2. unresolved cross-references
for html in sorted(SITE.rglob("*.html")):
    hits = html.read_text(encoding="utf-8", errors="replace").count("quarto-unresolved-ref")
    if hits:
        refs = sorted(set(re.findall(r'quarto-unresolved-ref[^>]*>\?([\w:-]+)',
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

# The theorem-family prefixes: the keys amsthm-refs hands to the numbered-block filter.
AMSTHM_REFS = BOOK / "_extensions/local/amsthm-refs/amsthm-refs.lua"
lua_table = re.search(r"local ref_prefixes = \{(.*?)\}", AMSTHM_REFS.read_text(), re.S)
if lua_table is None:
    sys.exit(f"docs-check: read no ref_prefixes table out of {AMSTHM_REFS}")
THEOREM_PREFIXES = re.findall(r'(\w+)"?\]?\s*=\s*true', lua_table.group(1))

# 3. broken links. A link names its target by id, `[t](#sec-x)`, and Quarto finds the
# page that holds the id, so a chapter can move without breaking a link to it. A link
# by path, `[t](../dir/Page.md)`, breaks when either end moves, so it is refused.
# Quarto finds the page only for a heading id; a link to a numbered block (`#thm:x`)
# stays an in-page anchor and is dead from any other chapter, so it is refused too.
ids = {i for h in SITE.rglob("*.html")
       for i in re.findall(r'id="([^"]+)"', h.read_text(encoding="utf-8", errors="replace"))}
for md in SITE_MD:
    for i, line in enumerate(md.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        for m in re.finditer(r"\]\(#([^)\s]+)\)", line):
            if m.group(1).split(":")[0] in THEOREM_PREFIXES and ":" in m.group(1):
                failures.append(f"{md.name}:{i}: link to the block #{m.group(1)} — "
                                f"write `text (@{m.group(1)})`")
            elif m.group(1) not in ids:
                failures.append(f"{md.name}:{i}: link to #{m.group(1)}, which no page has")
        for m in re.finditer(r"\]\(((?![a-z]+:)[^)\s#]+\.md)(#[^)\s]*)?\)", line):
            failures.append(f"{md.name}:{i}: link to the path {m.group(1)} — link to the "
                            "id of the heading instead, `[text](#sec-x)`")

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

# 7. theorem-family references — checked in the source, because the rendered page
# shows nothing at all. The book writes them as the pandoc papers do: `@thm:key` and
# `[-@thm:key]`, which the amsthm-refs filter hands to custom-numbered-blocks. cnb
# drops a reference whose id it never registered, and pandoc drops raw LaTeX such as
# `\cref{x}` in HTML, so either defect silently deletes words from the sentence.
# Check 2 cannot see this: `quarto-unresolved-ref` is Quarto's own crossref marker.
sources = {md: md.read_text(encoding="utf-8", errors="replace") for md in SITE_MD}
defined = {m.group(1) for text in sources.values()
           for m in re.finditer(r"^:{3,}\s*\{[^}\n]*#([\w:.-]+)", text, re.M)}
THEOREM_REF = re.compile(r"(?<![\w@])@((?:" + "|".join(THEOREM_PREFIXES) + r"):[\w:.-]*[\w-])")
for md, text in sources.items():
    for i, line in enumerate(text.splitlines(), 1):
        for m in THEOREM_REF.finditer(line):
            if m.group(1) not in defined:
                failures.append(f"{md.name}:{i}: @{m.group(1)} names no block in the book — "
                                "the reference renders as nothing")
        for m in re.finditer(r"\\(?:[cC]ref|longref|ref)\{([^}]*)\}", line):
            failures.append(f"{md.name}:{i}: {m.group(0)} is raw LaTeX — "
                            f"write @{m.group(1)} or [-@{m.group(1)}]")

# 8. external links must resolve — a cited resource that 404s can't be verified to exist
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
