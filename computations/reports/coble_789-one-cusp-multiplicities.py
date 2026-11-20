"""#789: the Sterk type of each of the seven R-orbits of primitive isotropic planes.

Serves thm:one-cusp-multiplicities and thm:cusp-diagram-tco.

Input is the committed record computations/reports/coble_gco_plane-orbits-run.txt,
which prints, for each of the seven star-decorated plane orbits (= the seven
R-orbits of primitive isotropic planes of T_Co, cor:coble-heegner-integral-plane-
descent), the discriminant-orbit sizes of the nonzero classes of the primitive
lines in that plane, under the heading

    endpoint incidence by decorated-plane orbit (vector orbit sizes):

The four vector-orbit sizes are the four P-orbits of
prop:coble-cong-point-stabilizer(2), and by thm:orbit-per-cusp the P-orbit of
[eta_k/2] has size

    k = 2 -> 2,   k = 3 -> 120,   k = 4 -> 270,   k = 5 -> 135 .

So the size list of a plane is the set of Sterk labels of its lines, i.e. its
type in the sense of AEGS Not. 3.1, and the multiplicity m_T of
thm:one-cusp-multiplicities is the number of plane orbits of type T.

This script reads the record, applies the dictionary, and reports m_T, the
degrees of the four 0-cusps and the edge count.

The dictionary itself is recomputed in computations/reports/coble_789-cusp-classes.py,
whose transcript gives the P-orbit size of each [eta_k/2].
"""
import re
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent
RECORD = ROOT / "coble_gco_plane-orbits-run.txt"

SIZE_TO_LABEL = {2: 2, 120: 3, 270: 4, 135: 5}   # thm:orbit-per-cusp

text = RECORD.read_text(errors="replace")
# the block after the heading, seven lines "  plane size NNNN: [(s, 1), ...]"
start = text.index("endpoint incidence by decorated-plane orbit")
block = text[start:]
lines = [ln for ln in block.splitlines() if re.match(r"\s+plane size\s+\d+:", ln)]
assert len(lines) == 7, ("expected seven decorated plane orbits", len(lines))

types = []
for ln in lines:
    n = int(re.search(r"plane size\s+(\d+):", ln).group(1))
    sizes = [int(m) for m in re.findall(r"\((\d+),", ln)]
    labels = sorted(SIZE_TO_LABEL[s] for s in sizes)
    types.append((n, labels))
    print("plane orbit of size %6d: line-orbit sizes %s -> Sterk labels %s"
          % (n, sizes, labels))

m = Counter(tuple(t[1]) for t in types)
print("")
print("multiplicities m_T (thm:one-cusp-multiplicities):")
for T in sorted(m):
    print("   type %-12s m_T = %d" % (str(T), m[T]))
assert sum(m.values()) == 7, sum(m.values())
# the four empty types containing label 1 do not occur in the record
assert all(1 not in T for T in m), "a plane of T_Co met the 0-cusp 1"
deg = {}
for k in (2, 3, 4, 5):
    deg[k] = sum(m[T] for T in m if k in T)
print("")
print("degrees of the 0-cusps (the number of 1-cusps in whose closure they lie):")
print("   " + ", ".join("0_%d: %d" % (k, deg[k]) for k in (2, 3, 4, 5)))
edges = sum(deg.values())
print("   total incidences (= flag orbits = edges): %d" % edges)
assert deg[2] == 1 and edges == 13, (deg, edges)
assert m[(2, 4, 5)] == 1 and m[(5,)] == 2
assert m[(3, 5)] == 2 and m[(3, 4)] == 1 and m[(4, 5)] == 1, dict(m)
print("")
print("conclusion: m = 1, 1, 2, 1, 2 for the types {2,4,5}, {4,5}, {3,5}, {3,4}, {5,5};")
print("(the type {5,5} of Sterk AEGS Not. 3.1 is the label set {5}, its closure meeting 0_5 twice)")
print("degrees 0_2 = 1, 0_3 = 3, 0_4 = 3, 0_5 = 6; 13 edges.")
print("This is the third alternative of thm:one-cusp-multiplicities(4).")
