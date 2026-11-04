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
h~_Co = f^*(6H - 2(E_1+..+E_8) - E_9 - E_10) the two roots are +-(3f^*H - Sum f^*E_i), whose preimage in
Pic(S) is +-(3H - Sum E_i) = +-(-K_S).  That is a coordinate statement under prop:coble-invariant-lattice's
dictionary and nothing more.

The definition, from the primary source in the repository.  references/literature/lattice-research/
dolgachev_kondo_2013.md, section 3 (the book's [@DK13]): "A Coble surface is a smooth rational projective
surface S such that |-K_S| = empty but |-2K_S| != empty", with the classical example the blow-up of the
plane at the ten *nodes of an irreducible plane sextic*.  Two consequences, both the opposite of what an
earlier version of this report said: -K_S is a perfectly integral *class* (the coefficients of D/2 are a
statement about a divisor representative, not about the class) but it is *ineffective* by definition; and
the model is ten nodes of a sextic, not ten points on a cubic.

What decides it, from the double-cover construction itself.  Two divisors must not be confused.  The
*branch* divisor is the plane sextic C inside S, of class [C] = 6H - 2 Sum E_i = -2K_S (DK13 section 3:
S is the blowup at the ten nodes of C, so the strict transform has those multiplicities).  The
*ramification* divisor is R = the reduced preimage f^{-1}(C) inside X, and it is R, not C, that lives on
X.  For a double cover branched along C the pullback relation is

    f^*[C] = 2[R],

the coefficient 2 being the ramification index along R (and the strict transform of C in S is smooth, so
R is reduced).  With [C] = -2K_S this gives

    [R] = f^*[C]/2 = f^*(-K_S) = alpha,

so alpha is the class of the *ramification curve*: an effective divisor, geometrically exhibited, not a
cohomological count.  That is a source-supported argument, using only DK13's model and the standard
f^*[C] = 2[R] of a double cover.

The three statements reconciled.  (i) 2 alpha = f^*[C] = 2[R] is effective, being twice the effective
divisor R.  (ii) Exactly one of +-alpha is effective, and it is +alpha, because alpha = [R] with R
nonempty: if -alpha were also effective, -alpha = [R'] for some effective R', so R + R' would be a
principal divisor with both terms effective and nonnegative, forcing R = R' = 0, a contradiction.  (iii)
The sign is therefore *not* unresolved: the retained effective root is +alpha = 3f^*H - Sum f^*E_i.  An
earlier version left it open and offered a cohomological count (h^0(X, alpha) = h^0(S,-K_S) +
h^0(S,O_S) = 1, from f_* O_X = O_S (+) O_S(K_S)); that count is correct but it is a count, and the
ramification divisor is the actual witness.

What remains open is separate: whether H = h~_Co = f^*h_Co is nef and big -- a property of the divisor,
not of its class -- and the identification of AEGS's I_dP with the del Pezzo involution of the cover.
The coordinate computation above (the two roots and their preimages) is what it is and certifies no
effectivity by itself.
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
print('  Coordinates: the two roots are +-(3f^*H - Sum f^*E_i), with preimages +-(3H - Sum E_i) = -+K_S.')
print('  Definition, [@DK13] section 3: |-K_S| = empty, |-2K_S| nonempty, S the blowup at the ten nodes of')
print('  the plane sextic C, so that [C] = 6H - 2 Sum E_i = -2K_S.')
print('  Branch downstairs, ramification upstairs: the branch divisor is C in S; the ramification divisor')
print('  is R = f^{-1}(C) in X, and f^*[C] = 2[R].  Hence [R] = f^*[C]/2 = f^*(-K_S) = alpha: alpha is')
print('  the class of the ramification curve, so it is effective with a geometric witness.')
print('  2alpha = f^*[C] = 2[R] is therefore effective as twice R; exactly one of +-alpha is effective,')
print('  and it is +alpha, since -alpha = [R\'] with R\' effective would make R + R\' principal with both')
print('  terms effective, forcing both to vanish.  The sign is resolved: the retained root is +alpha.')
print('  Still open, and separate: whether H = h~_Co = f^*h_Co is nef and big; and the identification of')
print('  I_dP with the del Pezzo involution of the cover.  The coordinate check above certifies neither.')
print('OK: the retained root identified and shown effective by its ramification divisor; sign resolved')
