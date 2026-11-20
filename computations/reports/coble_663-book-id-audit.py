"""research#663: the book-wide id audit -- declared Div ids against pandoc, and every @ref.

The corpus's TRAPS.md names two silent failures: a fenced div that does not start a block never
becomes a Div, and a reference whose id was never registered disappears from the rendered page while
the source gate still passes.  This script runs both checks over every page under writing/, excluding
the Quarto project directory itself, and prints one line per failure.

Check 1 (fence defects): every id declared by ``^:::\s*{...#id`` must appear as a Div identifier in
``pandoc -f markdown -t native``.

Check 2 (@ref resolution): every ``@kind:id`` must name an id declared somewhere under writing/, or
an external scheme (``nlab:``) that the book's own stack filter resolves.

Usage: python3 computations/reports/coble_663-book-id-audit.py
"""
import pathlib
import re
import subprocess

ROOT = pathlib.Path("writing")
pages = [p for p in ROOT.rglob("*.md") if ".book" not in p.parts]
print(f"pages under writing/ (excluding .book): {len(pages)}")

declared, refs, defects = {}, {}, []
parsed_all = set()
for page in sorted(pages):
    src = page.read_text(errors="ignore")
    dec = re.findall(r'^:::\s*\{[^}]*#([A-Za-z0-9:_-]+)', src, re.M)
    for d in dec:
        declared.setdefault(d, []).append(str(page))
    for m in re.finditer(r'(?<![@\w-])@((?:[a-z]+):[A-Za-z0-9_][A-Za-z0-9_:.-]*)', src):
        refs.setdefault(m.group(1).rstrip('.:'), []).append(str(page))
    nat = subprocess.run(["pandoc", "-f", "markdown", "-t", "native", str(page)],
                         capture_output=True, text=True)
    parsed = set(re.findall(r'\(\s*"([A-Za-z0-9:_-]+)"\s*,\s*\[', nat.stdout))
    parsed_all |= parsed
    defects += [(str(page), d) for d in dec if d not in parsed]

print(f"distinct ids declared by ::: fences: {len(declared)}")
print(f"distinct Div identifiers pandoc parsed: {len(parsed_all)}")
print()
print(f"CHECK 1 -- fence defects (declared by a ::: fence but not parsed as a Div): {len(defects)}")
for page, d in defects:
    print(f"   {page}: {d}")
print()
EXTERNAL = ("nlab:",)
unresolved = [(k, v) for k, v in refs.items()
              if k not in declared and k not in parsed_all and not k.startswith(EXTERNAL)]
print(f"CHECK 2 -- @refs resolving to no id and to no external scheme: {len(unresolved)}")
for k, v in sorted(unresolved):
    print(f"   {k}: {sorted(set(v))}")
print()
print("External schemes not checked here, resolved by the book's stack filter:",
      ", ".join(s.rstrip(':') for s in EXTERNAL))
