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
