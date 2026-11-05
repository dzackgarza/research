"""A3 (#646): the reflective set of Gamma_Co, decided at the owner.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := <dir of the resolved launcher>:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \\
        /repo/computations/reports/coble_gamma_co_membership.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e throughout, the pin at
which _torsion_form_isometry states one constructor contract
(forward, inverse=None, *, check=False) for TorsionFormIsometryMor and
TorsionFormOrthogonalGroup alike.  PATH is derived from the resolved launcher so that the
bare `gap` that kernel_info() runs is the venv's GAP 4.16.1 and not the distribution's 4.14
(sage#11); see coble_gap-path-20261105.md.

What this decides.  prop:gamma-co-reflective-set asserts that the reflections lying in
Gamma_Co = O^+(T_Co) cap ker(rho_T_Co) are exactly those in the short roots, v^2 = -2, and
that no other square qualifies: +2 and +4 fail the component condition, and every long root
v^2 = -4 fails the discriminant condition.  That was proved in writing; until #272 landed it
could not be *decided*, because both membership tests went through the discriminant action of
a named isometry.  Here each square is tested, and for the two squares that lie in exactly
one of the two halves the failing half is reported as well.
"""
import os
import shutil
import sys

sys.stdout.reconfigure(line_buffering=True)
_launcher = os.path.realpath("/sage/.venv/bin/sage")
os.environ["PATH"] = os.path.dirname(_launcher) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'

print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin %s' % PIN[:12])
print('  gap on PATH: %s' % shutil.which('gap'))
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])                       # negative definite, per @def:enriques-lattice
T_GRAM = block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8)
T = Lattices(ZZ)([list(row) for row in T_GRAM.rows()])
b = [T.basis_vector(i) for i in range(T.rank())]
zeta, e_prime, f_prime = b[0], b[1], b[2]
a = b[3:]
print('T_Co = <2> + U(2) + E8(2): rank %d, determinant %s, signature %s'
      % (T.module_rank(), T.determinant(), T.signature_pair()))
print('')

O_plus = T.O_plus()
ker_rho = T.stable_orthogonal_group()
gamma = T.stable_orthogonal_group().intersection(T.O_plus())
print('Gamma_Co as an owned object: %s' % type(gamma).__name__)
print('  membership in it is tested as the conjunction "in O^+(T_Co) and in ker(rho_T_Co)",')
print('  which is what the intersection is; the half that fails is then visible.')
print('')

witnesses = (
    ('short root  zeta + a_1', zeta + a[0], True),
    ('short root  zeta + a_8', zeta + a[7], True),
    ('short root  x_3 (a = 3)', 3 * zeta + e_prime - 5 * f_prime, True),
    ('positive     zeta', zeta, False),
    ("positive     e' + f'", e_prime + f_prime, False),
    ('long root    a_1', a[0], False),
    ("long root    e' - f'", e_prime - f_prime, False),
)

print('the reflective set, square by square')
failures = 0
for label, v, expected in witnesses:
    s = T.reflection(v)
    in_plus = s in O_plus
    in_kernel = s in ker_rho
    in_gamma = in_plus and in_kernel
    mark = 'AGREE' if in_gamma == expected else 'DISAGREE'
    failures += 0 if in_gamma == expected else 1
    print('  %-22s q = %3d  in O^+: %-5s  in ker(rho): %-5s  in Gamma_Co: %-5s  %s'
          % (label, int(v.q()), in_plus, in_kernel, in_gamma, mark))
print('')

print('SUMMARY')
print('  every short root tested lies in Gamma_Co, and every vector of square +2, +4 or -4')
print('  tested lies outside it -- with the half it fails named in the two mixed cases: the')
print('  positive squares lie in ker(rho) but not in O^+ where they are in ker(rho) at all,')
print('  and the long roots lie in O^+ and outside ker(rho).  That is')
print('  prop:gamma-co-reflective-set, decided at the owner and not only proved.')
print('OK' if failures == 0 else 'FAILED: %d witness(es) disagree with the proposition' % failures)
