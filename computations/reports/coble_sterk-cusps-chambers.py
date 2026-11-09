"""#654: chambers of Sterk's five cusps under the subgroups G_v (written, NOT run).

    .scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \
        /repo/computations/reports/coble_sterk-cusps-chambers.py

For each j = 1..5 of Sterk Prop. 4.2.3 (p. 16), with K_j as in Lemma 4.3.4 (p. 17):
  j = 1: K_1 = U(2) + E8(2) = K(L_1), type (10,10,0)
  j = 2..5: K_j = U + E8(2) = K(L_2), type (10,8,0)
the chamber Sterk draws is that of the subgroup G_v = rho(Stab_Gamma(v)) <= O(K_j) (Sterk 4.3.1,
p. 17), not of the full orthogonal group.  The full-group chambers are already records:
ten walls each, one and two ideal vertices (coble_TEn-chambers.py); the subgroups are
rho(S_eta_j) of coble_TEn-sandwich.py.

What this script does once the chamber-under-a-subgroup operation exists (sage-extensions, filed
under #281 after #285): build K_j, build G_v by the sandwich, ask for the chamber of G_v, print its
wall count beside Sterk's 12, 10, 12, 11, 14.  Until then it stops at the full-group chamber and
prints the index [O(K_j) : G_v], which is the datum the wall count refines.
"""
import os
import sys

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage_extensions.all import ZZ as SEZZ, HyperbolicLattices, Lattices  # noqa: E402

C = [[int(x) for x in row] for row in CartanMatrix(['E', 8])]
E8n = [[-2 * C[i][j] for j in range(8)] for i in range(8)]
U2 = [[0, 2], [2, 0]]
U1 = [[0, 1], [1, 0]]


def diag(*blocks):
    n = sum(len(B) for B in blocks)
    M = [[0] * n for _ in range(n)]
    off = 0
    for B in blocks:
        for i in range(len(B)):
            for j in range(len(B)):
                M[off + i][off + j] = B[i][j]
        off += len(B)
    return M


CASES = (('j = 1, v = e          K = U(2) + E8(2)', diag(U2, E8n), 12),
         ("j = 2, v = e'         K = U    + E8(2)", diag(U1, E8n), 10),
         ('j = 3, v = e\'+f\'+w   K = U    + E8(2)', diag(U1, E8n), 12),
         ("j = 4, v = e'+2f'+a   K = U    + E8(2)", diag(U1, E8n), 11),
         ('j = 5, v = 2e+2f+a    K = U    + E8(2)', diag(U1, E8n), 14))
for name, rows, stern in CASES:
    L = Lattices(SEZZ)(rows)
    H = HyperbolicLattices(SEZZ)(L)
    walls = list(H.vinberg_simple_roots(max_roots=20, max_decompositions=2000))
    print('%s' % name)
    print('  full-group chamber: %d walls   (Sterk: %d)' % (len(walls), stern))
    print('  the subgroup G_v is rho(S_eta_j) of coble_TEn-sandwich.py;')
    print('  the chamber under G_v needs the subgroup-chamber operation (sage-extensions, #281 after #285).')
    print('')
