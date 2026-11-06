"""B3 (#689): are [1, 255, 272] the orbits of the stated stabilizer?

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := <dir of the resolved launcher>:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_discriminant-stabilizer-orbits.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e; PATH derived from
the resolved launcher so the bare `gap` is the venv's 4.16.1 (sage#11).

STATED BEFORE THE RUN.

The group.  G = Stab_{O(A_{T_Co}, q)}(c), the stabilizer in the finite orthogonal group of the
discriminant form of T_Co of the class c of (1/2)h~_Co.  The class has q(c) = 1, so it lies in
the q = 1 fibre, of 496 classes; |O(A_{T_Co}, q)| = 46 998 591 897 600 and 46 998 591 897 600 /
496 = 94 755 225 600, the order GAPS.md 1068-1069 records for this stabilizer.  It is NOT the
stabilizer of the class of zeta/2: that one is all of O(A_{T_Co}, q), because every isometry
of the form fixes zeta/2 (prop:coble-discriminant-group), so its orbits are the two of
thm:coble-isotropic-class-orbits, [1, 527].

The generators.  None are written down here, and that is the point of this record: the
generator description of G is what the route below lacks.  What is available is the whole
group O(A_{T_Co}, q), built by the owner in about a minute, and the class c.

The set acted on.  The 528 isotropic classes of A_{T_Co}, q = 0, of which 527 are nonzero.

The owner call.  O.stabilizer_of_element(c) to get G, then the action of G on those 528
points, S.action_on(points).orbits().  The first of the two is the call that has not
returned before (1800 s), and this record measures it again under a hard cap.

What would settle the question.  The multiset of orbit sizes of G on the 528 isotropic
classes: [1, 255, 272] settles B3 in the affirmative, any other multiset refutes the stated
list, and either way the certificate is the orbit partition itself, which is a partition of a
finite set that the record prints.
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
E8 = -CartanMatrix(['E', 8])
T = Lattices(ZZ)([list(r) for r in
                  block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8).rows()])
A = T.discriminant_quadratic_form()
isotropic = list(A.isotropic_elements())
print('A = A_{T_Co}: %d classes, %d isotropic' % (int(A.cardinality()), len(isotropic)))
print('')

print('the class c of (1/2)h~_Co: taken in the q = 1 fibre')
c = None
for x in A:
    if A.q(x) == A.q(x).parent()(1):
        c = x
        break
print('  c = %s, q(c) = %s' % (c, A.q(c)))
assert A.q(c) == A.q(c).parent()(1)
print('')

start = time.time()
O = A.orthogonal_group()
print('|O(A, q)| = %d   (%.0f s)' % (int(O.order()), time.time() - start))
print('  |O| / 496 = %d, the order GAPS.md records for the stabilizer'
      % (int(O.order()) // 496))
print('')

print('the call: O.stabilizer_of_element(c)')
start = time.time()
G = O.stabilizer_of_element(c)
elapsed = time.time() - start
print('  returned in %.0f s; |G| = %d' % (elapsed, int(G.order())))
print('')

print('and the orbits of G on the 528 isotropic classes')
orbits = G.action_on(isotropic).orbits()
sizes = sorted(int(o.cardinality()) for o in orbits)
print('  orbit sizes: %s' % sizes)
print('  sum: %d' % sum(sizes))
print('')
print('the stated list is [1, 255, 272]: %s' % ('AGREE' if sizes == [1, 255, 272] else 'DISAGREE'))

# Nothing below runs: the call above does not return, so this file is the measurement of that
# and the statement of what would have to exist.  What the run does establish is printed above:
# A_{T_Co} has 2048 classes and 528 isotropic ones, |O(A,q)| = 46 998 591 897 600 in 83 s, and
# 46 998 591 897 600 / 496 = 94 755 225 600, the order GAPS.md records for this stabilizer.
#
# THE OPERATION THAT IS MISSING, stated as a contract for the owner.
#
#   stabilizer_generators(action, point) -> generating set of isometries
#
# in:  a finite torsion quadratic module A over Z/2 with its orthogonal group acting on itself
#      (here |A| = 2048, exponent 2), and a point c in A (here a class of value 1);
# out: a generating set of Stab_{O(A,q)}(c) as explicit isometries of A, i.e. as elements whose
#      forward maps are module Mors, so that each one is checkable and so that a subgroup can
#      be built from them without enumerating O(A,q);
# certifies: (i) every returned generator fixes c and preserves q, which the existing
#      form-preservation validator decides; and (ii) completeness, by the order identity
#      |<generators>| = |O(A,q)|/|O(A,q).c|, which here is 46 998 591 897 600/496 =
#      94 755 225 600 -- computable from the orbit of c alone, so the check does not require
#      the parent group's enumeration either.
#
# With that in hand the orbit question is the one line of code above and nothing else.  The two
# calls that exist instead are O.stabilizer_of_element(c), which does not return (1800 s once,
# 900 s here), and nothing that presents the stabilizer by generators.
