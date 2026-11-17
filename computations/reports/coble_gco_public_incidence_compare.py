"""Compare the public integral Gamma_Co,2 incidence graph with finite cusp lifting.

The public edges are the 13 lines labelled '[Gamma_{Co,2}] edge' in
https://github.com/dzackgarza/sage-extensions/actions/runs/43556671111
at sage-extensions revision 3147ea330f1f91bef3ae20006210dcbdc4456323.
The finite edges are from coble_gco_plane-orbits-run.txt, the exact enumeration
of G_Co acting on (J,star,c), at research revision 9aab2bd3f1.

The labels L0..L3 and P0..P6 in the public output are arbitrary representative
indices. The finite labels are vector-orbit sizes and decorated-plane orbit
sizes, not integral orbit cardinalities. Graph isomorphism, not equality of
these labels, is the comparison invariant.
"""
from itertools import permutations
import ast
import re
import subprocess
import sys
from pathlib import Path

public = {
    (0, 0), (3, 0), (2, 0), (3, 1), (1, 1), (3, 2), (2, 2),
    (1, 3), (2, 3), (2, 4), (1, 5), (2, 5), (2, 6),
}
finite = {
    (2, 2160), (135, 2160), (270, 2160),
    (135, 3150), (120, 7560), (135, 7560), (135, 9450),
    (120, 22680), (135, 22680), (120, 69120), (270, 69120),
    (135, 75600), (270, 75600),
}
# Optional source verification: read the actual public workflow log rather than
# trusting the copied index pairs.  The default mode remains offline/reproducible.
if "--verify-public-source" in sys.argv:
    log = subprocess.run(
        ["gh", "run", "view", "43556671111", "-R", "dzackgarza/sage-extensions", "--log"],
        check=True, text=True, capture_output=True,
    ).stdout
    matches = re.findall(r"\[Gamma_\{Co,2\}\] edge \d+: L(\d+) < P(\d+)", log)
    extracted = {(int(l), int(p)) for l, p in matches}
    assert len(matches) == 13 and extracted == public, (len(matches), extracted ^ public)
    print("public source edges verified against workflow log:", len(matches))

    # Directly classify the actual public integral plane representatives in
    # T_Co = <2> + U(2) + E8(-2), using their parity classes in A_T. The
    # negative E8 Cartan Gram in Sage's standard simple-root order has the
    # seven edges below (cf. CartanMatrix(['E',8])).
    plane_rows = re.findall(
        r"\[Gamma_\{Co,2\}\] plane cusp (\d+): (\(\(.*?\)\))", log
    )
    assert len(plane_rows) == 7
    e8_edges = ((0, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7))

    def vector_type(vector):
        v = tuple(int(x) % 2 for x in vector)
        assert len(v) == 11 and v[0] == 0
        u, e = v[1:3], v[3:]
        q_e = (sum(e) - sum(e[a] * e[b] for a, b in e8_edges)) % 2
        assert (u[0] * u[1] + q_e) % 2 == 0
        if u == (0, 0):
            assert any(e) and q_e == 0
            return "A"
        if not any(e):
            assert u in ((1, 0), (0, 1))
            return "B"
        if u == (1, 1):
            assert q_e == 1
            return "D"
        assert q_e == 0
        return "C"

    directly_computed = {}
    for idx, source in plane_rows:
        v, w = ast.literal_eval(source)
        assert len(v) == len(w) == 11
        third = tuple(a + b for a, b in zip(v, w))
        directly_computed[int(idx)] = "".join(sorted(map(vector_type, (v, w, third))))
    assert set(directly_computed) == set(range(7))
    print("public plane types computed directly from integral representatives:", directly_computed)

    line_rows = re.findall(
        r"\[Gamma_\{Co,2\}\] line cusp (\d+): (\(\(.*?\),\))", log
    )
    assert len(line_rows) == 4
    directly_computed_lines = {
        int(idx): vector_type(ast.literal_eval(source)[0]) for idx, source in line_rows
    }
    assert set(directly_computed_lines) == set(range(4))
    print("public line types computed directly from integral representatives:",
          directly_computed_lines)

# Verify the other copied edge set against the committed finite enumeration.
finite_log = Path(__file__).with_name("coble_gco_plane-orbits-run.txt").read_text()
finite_rows = re.findall(r"plane size\s+(\d+): \[((?:\(\d+, \d+\)(?:, )?)+)\]", finite_log)
extracted_finite = {
    (int(vector), int(plane))
    for plane, entries in finite_rows
    for vector, multiplicity in re.findall(r"\((\d+), (\d+)\)", entries)
    if int(multiplicity) == 1
}
assert len(finite_rows) == 7 and extracted_finite == finite
print("finite source edges verified against committed transcript:", len(extracted_finite))

line_types = (2, 120, 135, 270)
plane_types = (2160, 3150, 7560, 9450, 22680, 69120, 75600)
assert len(public) == len(finite) == 13
assert {l for l, _ in public} == set(range(4))
assert {p for _, p in public} == set(range(7))
assert {l for l, _ in finite} == set(line_types)
assert {p for _, p in finite} == set(plane_types)

witnesses = []
for lines in permutations(line_types):
    # Preserve the degree of each line vertex before comparing adjacency.
    if any(sum(l == i for l, _ in public) != sum(l == lines[i] for l, _ in finite)
           for i in range(4)):
        continue
    for planes in permutations(plane_types):
        if {(lines[l], planes[p]) for l, p in public} == finite:
            witnesses.append((lines, planes))
print("public edges:", len(public), "finite edges:", len(finite))
print("graph isomorphisms:", len(witnesses))
assert witnesses
lines, planes = witnesses[0]
print("public line index -> finite vector orbit size:", dict(enumerate(lines)))
print("public plane index -> finite decorated-plane orbit size:", dict(enumerate(planes)))
print("mapped public edge set equals finite edge set:",
      {(lines[l], planes[p]) for l, p in public} == finite)

# The four graph isomorphisms need not distinguish individual decorated-plane
# orbits. Check whether the graph-inferred undecorated type is independent of
# which isomorphism is chosen. This is a combinatorial inference conditional
# on the graph comparison, not a direct invariant computation on public
# integral representatives.
finite_plane_class = {
    2160: "ABC", 3150: "AAA", 9450: "AAA", 7560: "ADD",
    22680: "ADD", 69120: "CCD", 75600: "ACC",
}
classifications = {
    tuple(finite_plane_class[planes[p]] for p in range(7))
    for _, planes in witnesses
}
print("distinct finite-plane type assignments:", len(classifications))
assert len(classifications) == 1
print("public plane index -> graph-inferred finite-plane type:",
      dict(enumerate(next(iter(classifications)))))
if "--verify-public-source" in sys.argv:
    assert directly_computed == dict(enumerate(next(iter(classifications))))
    print("direct integral discriminant types equal graph-inferred types:", True)
    finite_vector_type = {2: "B", 120: "D", 135: "A", 270: "C"}
    assert all(directly_computed_lines[i] == finite_vector_type[lines[i]]
               for i in range(4))
    print("direct integral line types equal graph-inferred types:", True)
