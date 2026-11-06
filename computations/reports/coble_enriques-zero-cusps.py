"""A41 (#684): the discriminant side of the 0-cusp count of F_En.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := /sage/.venv/bin:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_enriques-zero-cusps.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e; `gap` is taken from the
venv so that it is the GAP 4.16.1 matching libgap.so.11.

STATED BEFORE THE RUN.

The question.  The section `sec:fen-unpolarized-cusps` of the Scattone chapter asserted a bijection
T_En/O(T_En) = K/O(K) and, "pulling back" through it, that T_En has exactly two O(T_En)-orbits of
primitive isotropic lines.  A41 records that the transport is asserted without proof across two
different discriminant groups.  What replaces it is Alexeev-Engel [@AE22, Prop. 5.5]: for an even
indefinite 2-elementary lattice T with invariants (r, a, delta), a primitive isotropic vector is of
exactly one of three types, and an isotropic vector of a given type exists iff a 2-elementary
lattice of signature (n_+ - 1, n_- - 1) with the corresponding invariants exists, and is then
unique up to O(T).  So the 0-cusp count is the number of admissible types, and the three types are
separated by (divisibility, discriminant class): delta_T = 0 kills the third one.

The objects.  T_En = U + U(2) + E8(2), rank 12, determinant -2^10, signature (2, 10), even
2-elementary; E8 is the negative definite E8 of @def:enriques-lattice, so E8(2) is negative
definite and the signature is (2, 10).

The set acted on and the calls.  Only the discriminant module is needed here: A =
T_En.discriminant_quadratic_form(), its cardinality, the multiset of values of q, and
A.isotropic_elements().  Two representative vectors of T_En are tested for divisibility by
T_En.divisibility_ideal.  No group is constructed and no orbit is enumerated; the orbit statement
used in the writing is Nikulin's lemma on isotropic vectors of a 2-elementary discriminant form,
quoted in the chapter as [@AE22, Lem. 5.4] / [@Nik80, Lem. 3.9.1], and the per-type uniqueness of
[@AE22, Prop. 5.5], which is a statement about the lattice and is not something this run can
enumerate.

What settles it, each item independently checkable:
  (1) |A| = 1024 with A = (Z/2)^10, i.e. a_T = 10;
  (2) every value of q lies in Z (not merely in Q/2Z): then delta_T = 0, the functional q mod Z is
      zero, and a characteristic class -- one satisfying b(x, y) = q(y) mod Z for all y -- cannot
      be nonzero.  Hence the third type of [@AE22, Prop. 5.5] does not occur for T_En;
  (3) the number of isotropic classes, so that with (2) and Nikulin's lemma the ordinary nonzero
      isotropic classes are a single O(q)-orbit;
  (4) div(e) = 1 for e the isotropic generator of the U summand and div(e') = 2 for e' the
      isotropic generator of the U(2) summand, so the two representatives realize types (1) and
      (2) of the proposition, i.e. the two orbits it produces are non-empty.
A result contradicting any of (1)-(4) refutes the count in the writing as well, since the count is
derived from exactly these inputs.
"""
import os
import shutil
import sys
import time

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from collections import Counter  # noqa: E402

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
E8 = -CartanMatrix(['E', 8])                        # negative definite, per @def:enriques-lattice
T = Lattices(ZZ)([list(r) for r in block_diagonal_matrix(U, 2 * U, 2 * E8).rows()])
print('T_En = U + U(2) + E8(2)')
print('  rank %d, determinant %s, signature %s' % (T.rank(), T.determinant(), T.signature_pair()))
print('')

start = time.time()
A = T.discriminant_quadratic_form()
n = int(A.cardinality())
print('A_{T_En}: %d classes   (%.0f s)' % (n, time.time() - start))

start = time.time()
elements = list(A.elements())
values = Counter()
for x in elements:
    values[A.q(x)] += 1
order_two = all((2 * x) == A.zero() for x in elements)
print('  A is 2-elementary, i.e. (Z/2)^10: |A| = %d and every element has order 2: %s   (%.0f s)'
      % (n, order_two, time.time() - start))
print('  the multiset of values of q, over all %d classes   (%.0f s)'
      % (n, time.time() - start))
for v, c in sorted(values.items(), key=lambda t: str(t[0])):
    lift = v.lift()
    print('    q = %-8s (lift %-6s)  %d classes   the lift is an integer: %s'
          % (v, lift, c, lift.denominator() == 1))
print('  every value of q has an integral lift, i.e. q maps into Z/2Z in Q/2Z'
      ' (delta_T = 0): %s' % all(v.lift().denominator() == 1 for v in values))
print('  hence q mod Z is the zero functional, and a characteristic class -- a nonzero x with')
print('  b(x, y) = q(y) mod Z for every y -- would lie in the radical of the nondegenerate')
print('  bilinear form.  There is none, so type (3) of [@AE22, Prop. 5.5] does not occur.')
print('')

start = time.time()
isotropic = list(A.isotropic_elements())
print('  isotropic classes (q = 0): %d, of which nonzero: %d   (%.0f s)'
      % (len(isotropic), len([x for x in isotropic if x != A.zero()]), time.time() - start))
print('')
basis = [T.basis_vector(i) for i in range(T.rank())]
e, ep = basis[0], basis[2]
print('the two representatives')
for name, v in (('e  (the isotropic generator of U)', e), ("e' (the isotropic generator of U(2))", ep)):
    print('  %s: square %s, divisibility %s'
          % (name, v.q(), T.divisibility_ideal(v)))
print('')
print('types realized: e is of type (1) odd/simple iff div = 1,')
print("                e' is of type (2) even ordinary iff div = 2 and its class is not")
print('                characteristic, which is implied by the vanishing of q mod Z above.')
