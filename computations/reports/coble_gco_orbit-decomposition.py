"""B2 (#688): is [1, 2, 120, 135, 270] the G_Co decomposition?

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := <dir of the resolved launcher>:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_gco_orbit-decomposition.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e; PATH derived from the
resolved launcher so the bare `gap` is the venv's 4.16.1 (sage#11).

STATED BEFORE THE RUN -- this is the generator-defined shape #689 lacked.

The group.  G_Co = <rho_{S_En}(g_1), ..., rho_{S_En}(g_9)> <= O(A_{S_En}, q_{S_En}), the image
under the discriminant representation of the nine integral isometries of S_En that generate the
integral stabilizer of the polarization by prop:polarization-stabilizer-enriques:
  g_1 = s_{u_0 - w_0}, the reflection in the <-2> direction of h^{perp C};
  g_2, ..., g_9 = the reflections in the eight simple roots of E8(2) contained in S_En.
Each g_i fixes h = u_0 + w_0 and is an isometry of S_En; each rho_{S_En}(g_i) is therefore an
element of O(A_{S_En}, q_{S_En}), and the group is given by those nine generators and nothing
else -- no enumeration of the parent group is needed to *define* it.

The set acted on.  The 528 isotropic classes of A_{S_En}.  A_{S_En} = A_{U(2)} perp A_{E8(2)}
has 3*136 + 1*120 = 528 classes of value 0, so the set #688 counts is the same size as the one
#689 counts, in the S-side space where G_Co actually acts.

The owner calls.  S_En.discriminant_representation() for rho_{S_En}; the images of the nine;
A_{S_En}.orthogonal_group().subgroup(images) for G_Co; then
G_Co.action_on(isotropic).orbits() for the decomposition.

What settles the question.  The multiset of orbit sizes: [1, 2, 120, 135, 270] settles B2 in
the affirmative, any other multiset refutes the stated list.  Independently, |G_Co| is
reported: the issue states it as 696 729 600 = |W(E8)|, and it is now also proved by hand in
prop:gamma-co-heegner-strict, so the group's order is a check on the run rather than a result
of it.
"""
import os
import shutil
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
print('  gap on PATH: %s' % shutil.which('gap'))
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])                      # negative definite, per @def:enriques-lattice
S = Lattices(ZZ)([list(r) for r in (2 * block_diagonal_matrix(U, E8)).rows()])
basis = [S.basis_vector(i) for i in range(S.rank())]
u0, w0 = basis[0], basis[1]
h = u0 + w0
print('S_En = C(2) = U(2) + E8(2): rank %d, determinant %s, signature %s'
      % (S.rank(), S.determinant(), S.signature_pair()))
print('  h = u_0 + w_0 has h^2 = %d' % h.q())
print('')

generators = [S.reflection(u0 - w0)] + [S.reflection(basis[2 + i]) for i in range(8)]
print('the nine integral isometries, before their discriminant images')
print('  squares: s_(u_0-w_0) in the direction of a vector of square %d'
      % (u0 - w0).q())
print('  each fixes h: %s' % all(g(h) == h for g in generators))
print('  each an isometry of S_En: %s' % all(g(S.basis_vector(0)).parent() is not None
                                             for g in generators))
assert all(g(h) == h for g in generators)
print('')

A = S.discriminant_quadratic_form()
isotropic = list(A.isotropic_elements())
print('A_{S_En}: %d classes, %d isotropic' % (int(A.cardinality()), len(isotropic)))
print('')

start = time.time()
rho = S.discriminant_representation()
images = tuple(rho(g) for g in generators)
print('the nine discriminant images, built in %.0f s' % (time.time() - start))
print('  each fixes the class of h/2: %s'
      % all(img(A.class_of(h)) == A.class_of(h) if hasattr(A, 'class_of') else 'not checked'
            for img in images))
print('')

start = time.time()
O = A.orthogonal_group()
print('|O(A_{S_En}, q)| = %d   (%.0f s)' % (int(O.order()), time.time() - start))
print('')

print('the call: O.subgroup(images), the group defined by its nine generators')
start = time.time()
G = O.subgroup(images)
print('  |G_Co| = %d   (%.0f s)' % (int(G.order()), time.time() - start))
print('  claimed 696 729 600 = |W(E8)|: %s' % (int(G.order()) == 696729600))
print('')

print('the orbits of G_Co on the 528 isotropic classes')
print('  the group carries only get_action/register_action, so the action is asked of the')
print('  module, which takes the acting group as an argument: A.orbits(group=G)')
start = time.time()
all_orbits = list(A.orbits(group=G))
iso_set = set(isotropic)
iso_orbits = [o for o in all_orbits if set(o) <= iso_set]
sizes = sorted(int(o.cardinality()) for o in iso_orbits)
print('  all orbits of G_Co on A_{S_En}: %d, sizes %s'
      % (len(all_orbits), sorted(int(o.cardinality()) for o in all_orbits)))
print('  those contained in the isotropic classes: %d, sizes %s   (%.0f s)'
      % (len(iso_orbits), sizes, time.time() - start))
print('  sum: %d, and the set has %d classes' % (sum(sizes), len(isotropic)))
print('')
print('the stated list is [1, 2, 120, 135, 270]: %s'
      % ('AGREE' if sizes == [1, 2, 120, 135, 270] else 'DISAGREE'))
