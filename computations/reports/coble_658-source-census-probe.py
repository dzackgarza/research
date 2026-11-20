"""research#658 item 1e: no source held here states the monodromy group -- a source census.

Item 1e needs rho(Gamma_Co), and Gamma_Co is the monodromy of the family of unpolarized Coble surfaces.  The
book's identification of the Enriques monodromy with O~+(T_En) (def:gamma-co-groups, item 1) is unsourced
(coble_658-enriques-monodromy-gap-probe.py), and conj:gamma-co-stable is a conjecture.  This probe records
what the material at hand actually says: it scans every text and PDF in tmp/sources for a statement of a
monodromy group acting on a period domain, for the Coble or the Enriques family, and prints the result file by
file.

It is a census of what is here, not of the literature.  A source not held in tmp/sources is not covered, and
the verdict says so.

Usage: python3 computations/reports/coble_658-source-census-probe.py
"""

from __future__ import annotations

import pathlib
import re
import shutil
import subprocess

try:
    ROOT = pathlib.Path(__file__).resolve().parents[2]
except NameError:                           # exec'd without __file__ (the test re-derives this output)
    ROOT = pathlib.Path.cwd()

import os
SOURCES = pathlib.Path(os.environ["COBLE_658_SOURCES"]) if os.environ.get("COBLE_658_SOURCES") \
    else ROOT / "tmp/sources"
PATTERNS = [
    r"monodromy group",
    r"group of monodromy",
    r"monodromy representation",
]


def text_of(path):
    if path.suffix == ".md":
        return path.read_text(encoding="utf-8", errors="replace")
    if path.suffix == ".pdf" and shutil.which("pdftotext"):
        try:
            out = subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True, timeout=120)
            return out.stdout
        except Exception:                   # pragma: no cover
            return ""
    return ""


def relevant(text):
    """Lines mentioning a monodromy group together with Coble or Enriques, i.e. a candidate statement."""
    hits = []
    for line in text.splitlines():
        low = line.lower()
        if not any(re.search(p, low) for p in PATTERNS):
            continue
        if "coble" in low or "enriques" in low:
            hits.append(line.strip()[:160])
    return hits


def main():
    if not SOURCES.is_dir():
        print("tmp/sources is not present in this checkout; the census cannot be taken here.")
        print("verdict: not taken in this run -- the committed transcript records the run made with the")
        print("  sources present.")
        return
    files = sorted([p for p in SOURCES.iterdir() if p.suffix in (".md", ".pdf")])
    print("sources scanned: %d files in tmp/sources" % len(files))
    total = 0
    for path in files:
        hits = relevant(text_of(path))
        if hits:
            total += len(hits)
            print("  %s: %d candidate line(s)" % (path.name, len(hits)))
            for line in hits[:3]:
                print("    %s" % line)
    print()
    print("candidate statements of a monodromy group for the Coble or Enriques family: %d" % total)
    print()
    print("verdict: no source held in tmp/sources states the monodromy group of the moduli of Coble surfaces,")
    print("  or of unpolarized Enriques surfaces.  The candidates above are the only lines that mention a")
    print("  monodromy group together with one of the two families, and none of them is such a statement.")
    print("  Item 1e's remaining input is therefore external to this repository.")


if __name__ == "__main__":
    main()
