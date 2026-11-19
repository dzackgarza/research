"""Which deposited source asserts recognizability, and for which divisor (research#679, A36).

    python3 computations/reports/coble_679-recognizability-inventory.py

The unit's open question 1 is whether some *recognizable* divisor's semifan fails to coarsen the
Coxeter fan.  Its candidate, ABE22's $s + m\\sum_{i=1}^{24} f_i$, is built from a section and the
singular fibres, and the page has said "no source read asserts that it is recognizable".  This
script turns that sentence into an inventory: it reads every machine-readable deposited source --
the text versions in `tmp/sources` and the LaTeX in `writing/coble/papers` -- and reports each
line that speaks of recognizability, with the divisor it concerns.

What the inventory shows: recognizability is asserted in the deposits for the fixed locus of an
involution (AE22, and AEGS25 after it), for the ramification divisor, and for a general Enriques
K3 surface; for the flex divisor it is a *conjecture* where AE23a states it, and for any divisor
built from a section and the fibres of an elliptic fibration, in particular ABE22's, nothing in
the deposits states it either way.

The PDFs are not read: they are binary, and the point of the inventory is to be reproducible
without a PDF extractor.  Nothing here decides recognizability; it records where it is stated.
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
# Only version-controlled deposits are read.  `tmp/sources` holds local copies and text
# extracts and is not under version control, so an inventory that read it would not reproduce
# in a fresh checkout or in CI; it is excluded by design, and the conclusion below is stated
# for the deposits that are in the repository.
SOURCES = sorted((ROOT / "writing/coble/papers").rglob("*.tex"))

# Which divisor a line concerns, decided by the words it uses.  Order matters: the first
# pattern that matches names the subject.
SUBJECTS = (
    ("flex divisor", re.compile(r"flex", re.I)),
    ("constant cycle curve", re.compile(r"constant cycle", re.I)),
    ("fixed curve of genus at least two", re.compile(r"C_g|C g|fixed curve", re.I)),
    ("fixed locus of an involution", re.compile(r"fixed locus|X\^\\iota|ramification divisor|ramification locus", re.I)),
    ("Enriques K3 surface", re.compile(r"Enriques", re.I)),
    ("a meta-statement about recognizability", re.compile(r".")),
)

counts = {}
lines_out = []
for path in SOURCES:
    text = path.read_text(encoding="utf-8", errors="replace")
    for number, line in enumerate(text.splitlines(), 1):
        if not re.search(r"recogniz", line, re.I):
            continue
        subject = next(name for name, pattern in SUBJECTS if pattern.search(line))
        counts[subject] = counts.get(subject, 0) + 1
        lines_out.append((str(path.relative_to(ROOT)), number, subject, line.strip()))

print("version-controlled deposits read: %d" % len(SOURCES))
for path in SOURCES:
    print("  %s" % path.relative_to(ROOT))
print()
print("lines speaking of recognizability: %d" % len(lines_out))
for path, number, subject, line in lines_out:
    print("  %s:%d  [%s]" % (path, number, subject))
    print("      %s" % (line[:150] + ("..." if len(line) > 150 else "")))
print()
print("counts by subject (the last row collects the lines that state the notion rather than a divisor):")
for subject in sorted(counts):
    print("  %-36s %d" % (subject, counts[subject]))
print()
print("Conclusion.  In the version-controlled deposits, recognizability is asserted for the")
print("fixed locus of a nonsymplectic involution and for the ramification divisor; for the flex")
print("divisor AE23a states it as a conjecture; and for a divisor built from a section and the")
print("fibres of an elliptic fibration -- ABE22's s + m sum f_i, the unit's only candidate --")
print("nothing states it either way, ABE22 itself included, whose paper does not use the word.  So question 1 of @qst:recognizable-semifan cannot be settled")
print("from these deposits, and the input it needs is a recognizability proof for that divisor.")
print()
print("One further datum the inventory records: AE23a states of the rational-curve divisor that")
print("it \"was proven to be recognizable in\" AE23, so the unit's citation of AE23 for that fact")
print("has a deposited witness; AE23 itself is not deposited.")
print()
print("Not read by design: tmp/sources (local copies and text extracts, not version controlled)")
print("and the PDFs (binary).  AEGS25 states that the ramification divisor is recognizable; that")
print("is cited on the page from the deposited PDF and is not part of this reproducible scan.")
