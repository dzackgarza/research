"""The two-elementary type of v^perp/Zv for the five 0-cusps of F_{En,2}.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/enriques_cusp_boundary_labels.py

Library sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee.  Lattice L_- = H + H(2) +
E8(-2), Gram block_diagonal(H, [[0,2],[2,0]], -2*Cartan(E8)), as in
computations/scripts/sterk-enriques-cusps/sterk_cusp_diagrams.sage.  The five representatives of
Sterk's isotropic orbits are e, e', e' + f' + abar_8, 2e' + f' + abar_1, 2e + 2f + abar_1.

The route is the retained one: K = v.isotropic_reduction() gives v^perp/Zv as a lattice (the
vector-level call the API exposes; section 3.3 of the timing certificate shows it takes under a
second, while the subobject wrapper is the call that stalled), and the invariants are read off the
maintained two-elementary object, EvenTwoElementaryLattices(K.base_ring())(K).  No Gram complement
and no hand-built quotient is used.
"""
import time

from sage.all import CartanMatrix, QQ, ZZ, block_diagonal_matrix, matrix
from sage_extensions.all import EvenTwoElementaryLattices, Lattices

C = CartanMatrix(['E', 8])
GRAM = block_diagonal_matrix(matrix(ZZ, [[0, 1], [1, 0]]), matrix(ZZ, [[0, 2], [2, 0]]), -2 * C)
V = ZZ ** 12
e, f, ep, fp = (V.gen(i) for i in range(4))
alpha = [V.gen(4 + i) for i in range(8)]
Cinv = C.inverse()
abar = [V(sum(QQ(-Cinv[k, i]) * alpha[k] for k in range(8))) for i in range(8)]
L = Lattices(ZZ)([list(row) for row in GRAM.rows()])
ring = L.base_ring()


def element(vector):
    return L.linear_combination({i: ring(int(vector[i])) for i in range(12) if vector[i] != 0})


def ip(x, y):
    return x * GRAM * y


REPRESENTATIVES = [
    ('e', e),
    ("e'", ep),
    ("e' + f' + abar_8", ep + fp + abar[7]),
    ("2e' + f' + abar_1", 2 * ep + fp + abar[0]),
    ("2e + 2f + abar_1", 2 * e + 2 * f + abar[0]),
]
EXPECTED = [(10, 10, 0), (10, 8, 0), (10, 8, 0), (10, 8, 0), (10, 8, 0)]

for (name, vector), expected in zip(REPRESENTATIVES, EXPECTED):
    assert ip(vector, vector) == 0, (name, 'not isotropic')
    v = element(vector)
    start = time.time()
    K = v.isotropic_reduction()
    invariants = EvenTwoElementaryLattices(K.base_ring())(K).two_elementary_invariants()
    elapsed = time.time() - start
    computed = tuple(int(value) for value in invariants)   # two_elementary_invariants gives (r, a, delta)
    print('%-20s K = v^perp/Zv: rank %2d, det %7s, signature %s'
          % (name, K.module_rank(), K.determinant(), K.signature_pair()))
    print('%-20s two_elementary_invariants: %s   (%.2fs)'
          % ('', invariants, elapsed))
    assert computed == expected, (name, computed, expected)
    print('%-20s chapter says (r, a, delta) = %s   AGREE' % ('', expected))
