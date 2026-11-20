#!/usr/bin/env python3
r"""research#787, acceptance item 4: every page that uses Gamma_Co or Gamma_{Co,2}
cites the D2 definitions.

The braced spelling \Gamma_{\Co} is the same symbol as \Gamma_\Co, and the first
version of this checker matched only the unbraced spelling; two pages using the
braced one were reported as not using the symbol at all.

Run from the repository root:  python3 computations/reports/787-gamma-citation-check.py
Exit status 0 iff no page uses a symbol without citing a definition.
"""
import glob
import re
import sys

USE = [
    re.compile(r'\\Gamma_(?:\{\\Co\}|\\Co)(?![A-Za-z0-9])'),
    re.compile(r'\\Gamma_\{\\Co,\s*2\}'),
]
CITES = ['def:coble-family-unpolarized', 'def:coble-family-degree-two']


def uses(text):
    return [p.pattern for p in USE if p.search(text)]


def cites(text):
    return [c for c in CITES if c in text]


def main():
    bad = []
    pages = 0
    for path in sorted(glob.glob('writing/**/*.md', recursive=True)):
        text = open(path, encoding='utf-8', errors='ignore').read()
        if not uses(text):
            continue
        pages += 1
        if not cites(text):
            first = None
            for i, line in enumerate(text.split('\n'), 1):
                if any(p.search(line) for p in USE):
                    first = (i, line.strip()[:110])
                    break
            bad.append((path, first))
    for path, first in bad:
        print(f'MISSING  {path}:{first[0]}\n         {first[1]}')
    print(f'pages using the symbols: {pages}; pages citing no D2 definition: {len(bad)}')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
