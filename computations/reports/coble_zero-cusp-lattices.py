"""#668: the 0-cusp lattices -- Enriques first (Sterk 1991), then Coble.

    .scratch/udocker_dir/bin/proot-x86_64 -R <rootfs> -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \
        /repo/computations/reports/coble_zero-cusp-lattices.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e.

For a primitive isotropic v of T, the cusp lattice is K = v^perp/<v>, of signature one less.
The two cases, both with v the isotropic generator of a hyperbolic summand:
  T_En = U + U(2) + E8(2), v = e of the U summand,  K = U(2) + E8(2)   (Sterk's cusp lattice);
  T_Co = B(2), B = U + U + I_{0,7}, v = e_1,       K = U(2) + I_{0,7}(2) = I_{1,8}(2).
This run builds each K directly, and prints its Gram matrix, determinant, signature, elementary
divisors, whether it is 2-elementary, the generator length a, the coparity delta read off the value
module of q, and the order of the discriminant group.  It does not decide reflectivity or produce a
Coxeter diagram: that needs Vinberg anchored at the chosen cusp, sage-extensions#285, which is
named in the page's report line.
"""
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402
from sage_extensions.all import Lattices  # noqa: E402

print('provenance\n  Sage: %s\n  sage-extensions: pin 15db925b0c92\n' % SAGE_VERSION)

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])          # negative definite, per @def:enriques-lattice
cases = [
    ('K_En = U(2) + E8(2)  (Sterk, the Enriques 0-cusp)', block_diagonal_matrix(2 * U, 2 * E8)),
    ('K_Co = U(2) + <-2>^7 = I_{1,8}(2)  (the Coble 0-cusp)', block_diagonal_matrix(2 * U, -2 * matrix.identity(ZZ, 7))),
]
for name, G in cases:
    start = time.time()
    L = Lattices(ZZ)([list(r) for r in G.rows()])
    print(name)
    print('  rank %d, determinant %s, signature %s, even %s'
          % (L.rank(), L.determinant(), L.signature_pair(), L.is_even()))
    A = L.discriminant_quadratic_form()
    print('  |A| = %d; the elementary divisors of the Gram matrix: %s'
          % (int(A.cardinality()), list(G.elementary_divisors())))
    values = {str(A.q(x)) for x in A.elements()}
    integral = all(A.q(x).lift().denominator() == 1 for x in A.elements())
    print('  the value module of q has %d element(s) after reduction mod Z; every value integral: %s'
          % (len(values), integral))
    print('  2-elementary iff every class has order 2... a = dim_{F_2}(A) = %s'
          % (int(A.cardinality()).bit_length() - 1 if int(A.cardinality()) & (int(A.cardinality()) - 1) == 0 else 'not a power of 2'))
    print('  delta: %d   (0 iff q is Z/2-valued, 1 otherwise)' % (0 if integral else 1))
    print('  (%.0f s)\n' % (time.time() - start))
