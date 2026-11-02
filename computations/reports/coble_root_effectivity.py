"""Focused check: which root the marking singles out, and what its effectivity reduces to.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_root_effectivity.py

The report's tuple carries a root alpha with alpha^2 = -2, H.alpha = 0, fixed by I_Co, and a chamber in
which alpha is effective and H is nef and big (heegner report, sec-labeled-lattice-data).  An earlier
note here recorded only that h~_Co^perp has one root line (A_1).  This does the next step: it identifies
the two vectors of that line in the book's coordinates and reads off what their effectivity means
downstairs.

The dictionary is prop:coble-invariant-lattice's: S_Co = f^* Pic(S) with f^*D . f^*D' = 2 D.D', so a
class of S_Co has the *same coordinates* as its preimage in Pic(S) and half the square.  A root of S_Co
therefore corresponds to a class of square -1 in Pic(S) = I_{1,10}, i.e. to a (-1)-class.

What this decides and what it leaves.  It decides the coordinates: for the admissible marking
h~_Co = f^*(6H - 2(E_1+..+E_8) - E_9 - E_10) the two roots are +-(3 f^*H - Sum f^*E_i), whose preimage
in Pic(S) is +-(3H - Sum E_i) = +-(-K_S), a (-1)-class.  That is a coordinate statement under
prop:coble-invariant-lattice's dictionary and nothing more.

It does NOT decide that this class is effective, and an earlier version of this report said it did by
calling the ten-points-on-a-cubic condition "the classical Coble condition".  The repository's own
statement of the Coble condition is different: coble-surface-structure-and-classification.md line 39
(proposition on norms of rational negative curves, cited to DZ99 section 2) has a Coble surface satisfying
|-2K_S| = {D} with D a nonempty sum of (-4)-curves, so that -K_S = D/2 is NOT integral there and
2(-K_S) = D is effective.  That is a condition on |-2K_S|, not on |-K_S|, and in the ten-point blowup
model of prop:coble-invariant-lattice one has K_S = -3H + Sum E_i, so -2K_S = 2(3H - Sum E_i) and whether
|-2K_S| consists of a single reduced divisor depends on the configuration.  The two descriptions are not
interchangeable, and nothing here settles which one the retained Coble surface satisfies.

What does follow, and only this: because f: X -> S is finite, the pullback of an effective class is
effective, so alpha = f^*(-K_S) is effective IF -K_S is.  The converse is not claimed, and the book's
ten-point blowup set-up does not assert that -K_S is effective.

None of this touches H, which in the report's tuple is the degree-4 class H^2 = 4, i.e. h~_Co; the
plane-line class H of Pic(S), with H^2 = 1, is a different object and is not substituted for it.
"""
import sys

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'

print('provenance')
print('  sage-extensions provider pin: %s (.scratch/se-provider-c546/src, read-only export)' % PIN)
print('  Sage: %s' % sage_version)
print('  image rootfs: $HOME/sage-image/rootfs, read-only; repo bound at /repo')
print('')

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
S_Co = Lattices(ZZ)([list(row) for row in
                     block_diagonal_matrix(matrix(ZZ, [[2]]), -2 * matrix.identity(ZZ, 10)).rows()])
PicS = Lattices(ZZ)([list(row) for row in
                     block_diagonal_matrix(matrix(ZZ, [[1]]), -matrix.identity(ZZ, 10)).rows()])
p = [PicS.basis_vector(i) for i in range(11)]
print('Pic(S) = I_{1,10} = <H, E_1, ..., E_10> (prop:coble-invariant-lattice)')
K_S = -3 * p[0] + sum(p[1:], PicS.zero())
print('  K_S = -3H + Sum E_i: K_S^2 = %d' % K_S.q())

# the admissible marking: h_Co = F_1 + F_2 with F_i isotropic, orthogonal to K_S, F_1.F_2 = 1
F1 = 3 * p[0] - sum(p[1:10], PicS.zero())
F2 = 3 * p[0] - sum(p[1:9], PicS.zero()) - p[10]
h_Co = F1 + F2
print('  h_Co = F_1 + F_2 = 6H - 2(E_1+..+E_8) - E_9 - E_10: square %d, h_Co.K_S = %d'
      % (h_Co.q(), h_Co.b(K_S)))
coords = [int(h_Co.to_vector()(i)) for i in range(11)]
ring = S_Co.base_ring()
h_tilde = S_Co.linear_combination({i: ring(coords[i]) for i in range(11) if coords[i]})
print('  its pullback h~_Co in S_Co = f^*Pic(S): square %d' % h_tilde.q())

K = S_Co.orthogonal_complement(h_tilde.sublattice())
roots = [K.inclusion()(r) for r in K.roots()]
print('')
print('the root line of h~_Co^perp (%d vectors):' % len(roots))
assert len(roots) == 2
for alpha in roots:
    alpha_coords = [int(alpha.to_vector()(i)) for i in range(11)]
    minus_K_S = -K_S
    same = alpha_coords == [int(minus_K_S.to_vector()(i)) for i in range(11)]
    print('  alpha = %-38s square %2d, alpha.h~ = %d, equals -K_S by coordinates: %s'
          % (str(alpha_coords), alpha.q(), alpha.b(h_tilde), same))

minus_K_S = -K_S
print('')
print('  -K_S = 3H - Sum E_i: square %d (a (-1)-class), and the two roots are +- its pullback'
      % minus_K_S.q())
print('  so the pair of roots is {f^*(-K_S), -f^*(-K_S)} = {alpha, -alpha}, with alpha the anticanonical')
print('  class upstairs.')

print('')
print('SUMMARY')
print('  Decided, under prop:coble-invariant-lattice\'s dictionary only: the two roots are')
print('  +-(3f^*H - Sum f^*E_i), whose preimage classes in Pic(S) are +-(3H - Sum E_i) = -+K_S, a (-1)-class.')
print('  Not decided: that this class is effective.  The repository\'s Coble condition is |-2K_S| = {D}')
print('  with D a sum of (-4)-curves (coble-surface-structure-and-classification.md line 39, DZ99 sec. 2),')
print('  where -K_S is not integral; the ten-point model has K_S = -3H + Sum E_i and -2K_S = 2(3H-Sum E_i),')
print('  and whether |-2K_S| is a single reduced divisor depends on the configuration.  The two')
print('  descriptions are not interchangeable and are not interchanged here.')
print('  What does follow: alpha = f^*(-K_S) is effective if -K_S is, because a finite pullback of an')
print('  effective class is effective; the converse is not claimed.')
print('  H in the report\'s tuple is the degree-4 class h~_Co, not the plane-line class of Pic(S), and no')
print('  substitution between them is made.')
print('OK: coordinates identified; effectivity left open with its source conditions stated')
