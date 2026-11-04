"""The eight connected components' integral null vectors, and the four cusp classes.

    $HOME/.udocker/bin/proot_x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/writing/coble/scripts/certificates/cusp_null_vectors.py

Input: the validated 24-root Gram matrix of AET Figure 1 (rank 19 over QQ, kernel 5) and the
eight connected components of Table 1 / Lemma 4.5, each with its extended node braced.  Eight,
not seven: A~17, D~10, E~7, E~8^(1), E~8^(2), A~1, D~16, A~1^*.

For each component this prints the integral null vector (the one in the chosen primitive
normalization), its square, and its agreement with the Kac marks of the affine type from
CartanType([letter, rank, 1]).a().  Then, for each of the four cusps, that the two components'
null vectors agree as classes in N -- Lemma 4.7, G(a1 - a2) = 0 -- so the cusp has a single
null vector, which is what the isotropic reduction needs.
"""
import sys

from sage.all import ZZ, Matrix, vector
from sage.combinat.root_system.cartan_type import CartanType

print("python", sys.version.split()[0])

CAND = dict(
    one=[(i, (i + 1) % 18) for i in range(18)] + [(0, 18), (6, 19), (12, 20)],
    two=[(18, 21), (21, 9), (19, 22), (22, 15), (20, 23), (23, 3)],
    six=[(21, 22), (22, 23), (23, 21)],
)
G = [[0] * 24 for _ in range(24)]
for i in range(24):
    G[i][i] = -2
for key, mult in (("one", 1), ("two", 2), ("six", 6)):
    for a, b in CAND[key]:
        G[a][b] = G[b][a] = mult
G = Matrix(ZZ, G)
print("Gram: rank", G.rank(), "kernel", 24 - G.rank())

# the eight components, in Table 1's order, extended node braced
CHAINS = [
    ("A~17",    list(range(18)), ("A", 17), 0),
    ("D~10",    [18, 17] + list(range(8)) + [19], ("D", 10), 17),
    ("E~7",     list(range(9, 16)) + [20], ("E", 7), 15),
    ("E~8^(1)", [13, 14, 15, 16, 17, 0, 1, 2, 18], ("E", 8), 13),
    ("E~8^(2)", [4, 5, 6, 7, 8, 9, 10, 11, 19], ("E", 8), 19),
    ("A~1",     [20, 23], ("A", 1), 20),
    ("D~16",    [19, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 18], ("D", 16), 18),
    ("A~1*",    [3, 23], ("A", 1), 3),
]

nulls = {}
for name, chain, (letter, rank), extended in CHAINS:
    block = Matrix(ZZ, [[G[a, b] for b in chain] for a in chain])
    basis = block.kernel().basis_matrix()
    assert basis.nrows() == 1, (name, basis.nrows())
    a = [x for x in basis[0]]
    scale = min(abs(x) for x in a if x != 0)
    a = [x / scale for x in a]
    assert all(x in ZZ for x in a), (name, a)
    a = [int(x) for x in a]
    full = [0] * 24
    for node, coeff in zip(chain, a):
        full[node] = coeff
    square = vector(ZZ, full) * G * vector(ZZ, full)
    kac = sorted(CartanType([letter, rank, 1]).a().values())
    print(f"\n{name:9} {len(chain):2} nodes, extended node {extended:2}")
    print(f"  null vector on the chain: {a}")
    print(f"  square in the presentation: {square}   Kac marks of the type: {kac}"
          f"   same multiset: {sorted(a) == kac}")
    nulls[name] = (chain, full)

print("\nThe four cusps, and Lemma 4.7 (the two components' nulls agree as classes in N):")
for cusp, left, right in [("D~10 E~7", "D~10", "E~7"),
                          ("E~8^2 A~1", "E~8^(1)", "E~8^(2)"),
                          ("E~8^2 A~1 (again)", "E~8^(1)", "A~1"),
                          ("D~16 A~1", "D~16", "A~1*")]:
    d = [x - y for x, y in zip(nulls[left][1], nulls[right][1])]
    rel = G * vector(ZZ, d)
    print(f"  {cusp:18}: n({left}) - n({right}) is a relation: {all(x == 0 for x in rel)}")
print("\nA~17 is a subdiagram by itself: its null vector is the sum of the eighteen rim roots.")
