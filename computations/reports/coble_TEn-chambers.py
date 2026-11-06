"""#654 known-family check, step (i): Vinberg on the two T_En cusp lattices.

    .scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \
        /repo/computations/reports/coble_TEn-chambers.py

K(L_1) = U(2) + E8(2), det -1024, type (10,10,0), the cusp of the div-1 class (e_1 in U);
K(L_2) = U   + E8(2), det  -256, type (10,8,0),  the cusp of the div-2 class (e_3 in U(2)).
The rings are sage-extensions' own (ZZ, Lattices, HyperbolicLattices from sage_extensions.all);
sage.all supplies only matrix/CartanMatrix.  Walls are printed in the coordinates of the Gram matrix
passed, so the dictionary of step (ii) is the identity on them.
"""
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import ZZ, HyperbolicLattices, Lattices  # noqa: E402

print('provenance\n  Sage: %s\n  sage-extensions pin 15db925b\n' % SAGE_VERSION)
U = matrix([[0, 1], [1, 0]])
E8 = [[2 if i == j else (-1 if abs(i - j) == 1 else (-4 if (i, j) in ((2, 6), (6, 2)) else 0))
       for j in range(8)] for i in range(8)]
# the E8 Cartan matrix, negative definite
C = [[int(x) for x in row] for row in CartanMatrix(['E', 8])]
E8n = [[-2 * C[i][j] for j in range(8)] for i in range(8)]


def block(blocks):
    rows = []
    for Bi in blocks:
        for r in Bi:
            rows.append(list(r) + [0] * (sum(len(x) for x in blocks) - len(r)))
    out = []
    for Bi, i0 in zip(blocks, [sum(len(x) for x in blocks[:k]) for k in range(len(blocks))]):
        pass
    return rows


def diag_blocks(*blocks):
    n = sum(len(B) for B in blocks)
    M = [[0] * n for _ in range(n)]
    off = 0
    for B in blocks:
        for i in range(len(B)):
            for j in range(len(B)):
                M[off + i][off + j] = B[i][j]
        off += len(B)
    return M


U2 = [[0, 2], [2, 0]]
cases = (('K(L_1) = U(2) + E8(2)', diag_blocks(U2, E8n)),
         ('K(L_2) = U    + E8(2)', diag_blocks([list(r) for r in U.rows()], E8n)))
for name, rows in cases:
    L = Lattices(ZZ)(rows)
    H = HyperbolicLattices(ZZ)(L)
    print('%s: rank %s, det %s, signature %s'
          % (name, H.rank(), H.determinant(), H.signature_pair()))
    start = time.time()
    try:
        walls = list(H.vinberg_simple_roots(max_roots=20, max_decompositions=2000))
        print('  vinberg_simple_roots: %d walls   (%.0f s)' % (len(walls), time.time() - start))
        for w in walls:
            print('    %s' % (list(w),))
        G = [[int(L.pairing(a, b)) for b in walls] for a in walls]
        print('  Gram matrix of the walls:')
        for row in G:
            print('    %s' % row)
        print('  norms: %s' % [int(L.pairing(w, w)) for w in walls])
    except Exception as exc:                                    # noqa: BLE001
        print('  FAILED: %s: %s' % (type(exc).__name__, exc))
    print('')
