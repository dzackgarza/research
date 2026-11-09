"""#654 step (ii): the walls of both T_En cusp chambers lifted into T_En, with the Gram identity.

T_En = U + U(2) + E8(2) in the coordinates e_1, f_1 (U, indices 0-1), e_3, f_3 (U(2), 2-3), and the
E8(2) basis (4-11).  The walls printed by coble_TEn-chambers.py are coordinates in the Gram matrix
passed for K(L_j); since K(L_j) IS the sublattice eta^perp/<eta> with the inherited form, the lift is
the insertion of those coordinates into the corresponding slots of T_En, and the Gram identity to
check is equality of the two Gram matrices.
"""
import os
import sys

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, matrix  # noqa: E402
from sage_extensions.all import ZZ, HyperbolicLattices, Lattices  # noqa: E402

C = [[int(x) for x in row] for row in CartanMatrix(['E', 8])]
E8n = [[-2 * C[i][j] for j in range(8)] for i in range(8)]
G = [[0] * 12 for _ in range(12)]
G[0][1] = G[1][0] = 1                      # U
G[2][3] = G[3][2] = 2                      # U(2)
for i in range(8):
    for j in range(8):
        G[4 + i][4 + j] = E8n[i][j]        # E8(2), negative definite


def b(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(12) for j in range(12))


U2 = [[0, 2], [2, 0]]
U1 = [[0, 1], [1, 0]]
cases = (('K(L_1) = U(2) + E8(2), eta = e_1 (div 1)', [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], U2),
         ('K(L_2) = U    + E8(2), eta = e_3 (div 2)', [0, 1, 4, 5, 6, 7, 8, 9, 10, 11], U1))
for name, idx, H2 in cases:
    rows = [[0] * 10 for _ in range(10)]
    for i in range(2):
        for j in range(2):
            rows[i][j] = H2[i][j]
    for i in range(8):
        for j in range(8):
            rows[2 + i][2 + j] = E8n[i][j]
    K = Lattices(ZZ)(rows)
    HK = HyperbolicLattices(ZZ)(K)
    walls = list(HK.vinberg_simple_roots(max_roots=20, max_decompositions=2000))
    gram_provider = [[int(K.pairing(a, b)) for b in walls] for a in walls]
    lifted = []
    for w in walls:
        v = [0] * 12
        for a, i in zip(list(w), idx):
            v[i] = int(a)
        lifted.append(v)
    gram_T = [[b(x, y) for y in lifted] for x in lifted]
    print(name)
    print('  walls returned by vinberg_simple_roots: %d' % len(walls))
    print('  Gram matrix of those walls in K(L_j):')
    for row in gram_provider:
        print('    %s' % row)
    print('  Gram matrix of the lifted walls in T_En:')
    for row in gram_T:
        print('    %s' % row)
    print('  THE TWO ARE EQUAL: %s' % (gram_provider == gram_T))
    print('')
