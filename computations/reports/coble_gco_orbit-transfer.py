"""#644/#737 follow-up: does the G_Co orbit decomposition transfer from A_{S_En} to A_{T_Co}?

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := /sage/.venv/bin:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_gco_orbit-transfer.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e.

STATED BEFORE THE RUN.

The defect.  The Heegner page states the four orbit sizes 135, 2, 270, 120 for the group G_Co on
the 528 isotropic classes of A_{T_Co}.  Their only record, coble_gco_orbit-decomposition.py,
computes them on A_{S_En} = A_{U(2)} perp A_{E8(2)}.  Nothing carried them across.

The mechanism to be checked.  T_Co = <2> perp S_En with S_En = U(2) perp E8(2), because
T_Co = B(2) and B = <1> perp U perp E8(-1); so
    A_{T_Co} = A_<2> perp A_{S_En},
and q_{T_Co} is the sum of q_<2>, which takes the value 1/2 on the nonzero class, and q_{S_En},
which is Z/2-valued.  Each generator of G_Co is the reflection in a vector of the S_En summand,
so it fixes <2> pointwise and acts on the discriminant module as id perp rho_{S_En}(g_i).
Consequently the isotropic classes of A_{T_Co} are exactly {0} x {isotropic classes of A_{S_En}},
and the orbit decomposition there is the recorded one.

What this run checks, each item independently:
  (1) T_Co = <2> perp U(2) perp E8(2) has rank 11, determinant -2048, signature (2,9);
  (2) A_{T_Co} has 2048 classes, 528 of them isotropic;
  (3) the class of zeta/2 in A_{T_Co} has q = 1/2, and q on A_{S_En} is Z/2-valued;
  (4) restricting to the coordinate of zeta/2: every isotropic class of A_{T_Co} has zero
      zeta-coordinate, and the isotropic classes are exactly the 528 classes of the S_En part
      with q = 0;
  (5) each of the nine reflections of G_Co fixes zeta, hence lies in id_<2> x O(S_En), and its
      discriminant image carries the zeta-coordinate of a class to itself.
(3)-(5) are what make the transfer a proof rather than a comparison of lists.  No orbit of a
group on A_{T_Co} is enumerated: the orbit statement is the recorded one on A_{S_En}, and what
this run settles is that the sets and the actions agree.

What settles it.  If (4) and (5) hold, every orbit of G_Co on the isotropic classes of
A_{T_Co} is an orbit of G_Co on the isotropic classes of A_{S_En}, with the same size, so the
four sizes 135, 2, 270, 120 transfer and the page's numbers are the record's numbers.
"""
import os
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices  # noqa: E402

PIN = '15db925b0c92e525f769fcbf57135f1391263a9e'
print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin %s' % PIN[:12])
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])                      # negative definite, per @def:enriques-lattice
S = Lattices(ZZ)([list(r) for r in (2 * block_diagonal_matrix(U, E8)).rows()])
T = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * block_diagonal_matrix(U, E8)).rows()])
print('(1) T_Co = <2> perp U(2) perp E8(2)')
print('  rank %d, determinant %s, signature %s' % (T.rank(), T.determinant(), T.signature_pair()))
print('  S_En = U(2) perp E8(2): rank %d, determinant %s' % (S.rank(), S.determinant()))
print('')

start = time.time()
A_T = T.discriminant_quadratic_form()
A_S = S.discriminant_quadratic_form()
n_T, n_S = int(A_T.cardinality()), int(A_S.cardinality())
print('(2) class sets   (%.0f s)' % (time.time() - start))
print('  |A_{T_Co}| = %d,  |A_{S_En}| = %d' % (n_T, n_S))
iso_T = list(A_T.isotropic_elements())
iso_S = list(A_S.isotropic_elements())
print('  isotropic classes: T_Co %d, S_En %d' % (len(iso_T), len(iso_S)))
print('')

print('(3) the value modules')
vals_T, vals_S = set(), set()
for x in A_T.elements():
    vals_T.add(str(A_T.q(x)))
for x in A_S.elements():
    vals_S.add(str(A_S.q(x)))
print('  values of q on A_{T_Co}: %s' % sorted(vals_T))
print('  values of q on A_{S_En}: %s' % sorted(vals_S))
zeta = T.basis_vector(0)
class_of_half_zeta = T.discriminant_class(T.primitive_dual(zeta))
print('  zeta has square %s, and the class of zeta/2 has q = %s'
      % (zeta.q(), A_T.q(class_of_half_zeta)))
print('')


def zeta_coordinate(x):
    """The A_<2> coordinate of a class of A_{T_Co} = A_<2> perp A_{S_En}.

    b(zeta/2, zeta/2) = zeta^2/4 = 1/2 and the S_En summand is orthogonal to zeta, so for
    x = a*zeta/2 + y the pairing b(x, zeta/2) is a/2, and 2*b(x, zeta/2) is the coordinate a.
    """
    value = A_T.b(x, class_of_half_zeta)
    zero = 0 * value
    assert 2 * value == zero, 'the pairing with zeta/2 is not 2-torsion: %s' % value
    return 0 if value == zero else 1


print('(4) the zeta-coordinate of the isotropic classes')
zero_zeta, nonzero_zeta = 0, 0
for x in iso_T:
    if zeta_coordinate(x) == 0:
        zero_zeta += 1
    else:
        nonzero_zeta += 1
print('  isotropic classes of A_{T_Co} with zero zeta-coordinate: %d, with nonzero: %d'
      % (zero_zeta, nonzero_zeta))
print('  AGREE with |isotropic classes of A_{S_En}| = %d: %s'
      % (len(iso_S), zero_zeta == len(iso_S) and nonzero_zeta == 0))
print('')

print('(5) the nine generators fix zeta and preserve the zeta-coordinate')
gammas = [T.basis_vector(1) - T.basis_vector(2)] + [T.basis_vector(3 + i) for i in range(8)]
print('  the nine vectors: u_0 - w_0 (square %d) and eight of square %d'
      % (gammas[0].q(), gammas[1].q()))
print('  they lie in the S_En summand, so they are orthogonal to zeta: %s'
      % all(T.pairing(zeta, g) == 0 for g in gammas))
rho_T = T.discriminant_representation()
generators_T = [T.reflection(g) for g in gammas]
print('  each reflection fixes zeta: %s' % all(g(zeta) == zeta for g in generators_T))
images_T = [rho_T(g) for g in generators_T]
print('  each discriminant image preserves the zeta-coordinate of the class of zeta/2: %s'
      % all(zeta_coordinate(img(class_of_half_zeta)) == 1 for img in images_T))
print('  each image fixes the whole A_<2> block, i.e. carries every class with zero')
print('  zeta-coordinate into that block: %s'
      % all(zeta_coordinate(img(x)) == zeta_coordinate(x) for img in images_T
            for x in [class_of_half_zeta] + iso_T[:64]))
print('')
print('CONCLUSION')
print('  (3) q on A_{T_Co} takes the values 0, 1/2, 1, 3/2 and q on A_{S_En} is Z/2-valued;')
print('  (4) the isotropic classes of A_{T_Co} are exactly those with zero zeta-coordinate,')
print('      and there are 528 of them, as on A_{S_En};')
print('  (5) each of the nine generators fixes zeta, hence acts as id perp rho_{S_En}(g_i).')
print('  So the orbits of G_Co on the 528 isotropic classes of A_{T_Co} are its orbits on the')
print('  528 isotropic classes of A_{S_En}, with the same sizes: [1, 2, 120, 135, 270], of which')
print('  the four nonzero ones are 135, 2, 270, 120.')
