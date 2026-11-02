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

What that leaves.  alpha = f^*(-K_S) is the pullback of an ineffective class, and the pullback of an
ineffective class can still be effective, so nothing follows either way about whether alpha is effective
on X.  What the source does pin is 2 alpha: 2 alpha = 6f^*H - 2 Sum f^*E_i = f^*C, and f^*C is the branch
divisor of the double cover, hence effective.  Whether alpha itself is effective is a question about the
K3 cover, not about Pic(S), and it is left open here.  H is not involved: the report's H is the degree-4
class h~_Co, not the plane-line class of Pic(S).
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
print('  Decided, under prop:coble-invariant-lattice\'s dictionary: the two roots are')
print('  +-(3f^*H - Sum f^*E_i), whose preimages in Pic(S) are +-(3H - Sum E_i) = -+K_S.')
print('  Source definitions, from [@DK13] section 3 (references/literature/lattice-research/')
print('  dolgachev_kondo_2013.md): a Coble surface has |-K_S| = empty and |-2K_S| nonempty, and the')
print('  classical model is the blow-up at the ten nodes of an irreducible plane sextic.  So -K_S is an')
print('  integral class that is ineffective by definition, and the model is not ten points on a cubic.')
print('  Not decided, and not decidable from Pic(S): whether alpha = f^*(-K_S) is effective on the K3')
print('  cover.  2 alpha = f^*C is the branch divisor, hence effective; alpha itself is a (-2)-class on X')
print('  with either it or its negative effective, and which one is a property of the cover.')
print('  H in the report\'s tuple is the degree-4 class h~_Co, not the plane-line class of Pic(S).')
print('OK: coordinates identified; the definition applied as stated; effectivity of the upstairs root left open')
