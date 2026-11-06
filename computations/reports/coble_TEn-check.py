"""#654/#668 known-family check, part 1: the discriminant form of T_En and |O(q_{T_En})|.

    .scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \
        /repo/computations/reports/coble_TEn-check.py

T_En = U + U(2) + E8(2), rank 12, determinant -2^10, signature (2,10).  This part records the
discriminant form and the order of its orthogonal group, which the orbit counts of the check need.
The remainder of the check -- the two O(T_En)-orbit representatives, their cusp lattices' chambers,
S_v, rho(S_v), ker pi_v and the per-orbit counts -- is not in this run.
"""
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

print('provenance\n  Sage: %s\n  sage-extensions pin 15db925b\n' % SAGE_VERSION)
U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
G = block_diagonal_matrix(U, 2 * U, 2 * E8)
T = Lattices(ZZ)([list(r) for r in G.rows()])
print('T_En = U + U(2) + E8(2): rank %d, det %s, signature %s'
      % (T.rank(), T.determinant(), T.signature_pair()))
start = time.time()
A = T.discriminant_quadratic_form()
n = int(A.cardinality())
iso = len(list(A.isotropic_elements()))
values = {str(A.q(x)) for x in A.elements()}
print('  |A| = %d, isotropic classes %d, distinct values of q: %d   (%.0f s)'
      % (n, iso, len(values), time.time() - start))
start = time.time()
O = A.orthogonal_group()
print('  |O(q_{T_En})| = %d   (%.0f s)' % (int(O.order()), time.time() - start))
