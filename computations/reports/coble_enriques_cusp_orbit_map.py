"""The Coble-to-Enriques cusp-orbit map: its fibres, and why it is not onto.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_enriques_cusp_orbit_map.py

Library sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee on this project's bind.

The setting.  eta: T_Co -> T_En is the primitive embedding of thm:normalization, T_En = U + U(2) + E8(2)
with the book's negative-definite E8, and T_Co = <2> + U(2) + E8(2) sitting inside it as the orthogonal
complement of k = e~ - f~, so that h = e~ + f~ is the <2> generator and e~ = (h + k)/2.  By the
stabilizer step of thm:normalization every phi in Gamma_Co = Orth^+(T_Co)^* extends to Gamma_En, and the
object map v |-> eta(v) therefore descends to

    Phi: Gamma_Co \\ I(T_Co) -> Gamma_En \\ I(T_En),      I = primitive isotropic vectors,

which is the map of 0-cusp sets; the 1-cusp version replaces vectors by primitive isotropic planes.
This file decides whether Phi is onto.

The fibre, stated before anything is computed, and for the 0-cusp map only: v and v' are isotropic
*vectors*, i.e. rank-1 isotropic lines, and the rank-2 (plane, 1-cusp) fibre is a separate question not
treated here.  Over a primitive isotropic w~ in T_En, Phi^{-1}([w~]) consists of the Gamma_Co-orbits of
those v with eta(v) in Gamma_En w~, that is of the v for which gamma^{-1}(w~) lies in eta(T_Co) for some
gamma in Gamma_En.  With the left action convention gamma.x = gamma x, put

    Y = {gamma in Gamma_En : gamma^{-1}w~ in eta(T_Co)},   v_gamma = eta^{-1}(gamma^{-1}w~),

so that the fibre is the double-coset set

    Phi^{-1}([w~])  =  Stab_{Gamma_En}(w~) \\ Y / Ext(Gamma_Co),

with the stabilizer acting on the LEFT and Ext(Gamma_Co) on the RIGHT.  Both actions preserve Y: on the
left, (h gamma)^{-1}w~ = gamma^{-1}w~ because h fixes w~, so the left action leaves v_gamma unchanged;
on the right, (gamma Ext(phi))^{-1}w~ = Ext(phi)^{-1} eta(v_gamma) = eta(phi^{-1} v_gamma), so the right
action moves the source vector inside its Gamma_Co-orbit, which is the ambiguity to quotient out.  The
reversed expression Gamma_Co \\ Y / Stab is not an action of a subgroup in the written order and is not
used.  The set is nonempty exactly when the Gamma_En-orbit of w~ meets eta(T_Co).  None of it is
enumerated below; what decides surjectivity, and then separability, are invariants of the target orbit
that every image vector is forced to take.

The groups are the stable ones throughout: Gamma_Co = Orth^+(T_Co)^* and Gamma_En = Orth^+(T_En)^*.  The
discriminant argument for separability uses Gamma_En inside the discriminant kernel, which holds for the
stable group by definition and fails for AEGS25's Gamma^K_En = Orth(T_En); nothing here is claimed for
the latter.

The obstruction.  Divisibility is invariant under isometries, hence constant on Gamma_En-orbits, and
AEGS25 §2 distinguish the two 0-cusps of the Enriques diagram by it.  Every primitive isotropic v in
T_Co has eta(v) of even divisibility in T_En, hence -- the target being 2-elementary, where a primitive
vector has divisibility 1 or 2 -- equal to 2.  So the divisibility-1 cusp is not in the image, and Phi
is not surjective.

Two identities carry that, and both are checked here on the representatives and structurally:

  (i)  div_En(eta(v)) = gcd(div_Co(v), beta_Co(v,h)/2).
       Reason: T_En = eta(T_Co) + Z e~, and beta_En(eta(v), e~) = beta_Co(v,h)/2.
  (ii) both entries are even.  div_Co is even because the Gram of T_Co is even entrywise (the corrected
       lem:divisibilityAlwaysTwoTco, whose content is exactly this).  beta_Co(v,h)/2 = a is even for
       every isotropic v = a h + y: the block of U(2) + E8(2) is twice an even lattice, so y^2 is
       divisible by 4, and v^2 = 2a^2 + y^2 = 0 then forces a^2 even.

Injectivity is not decided here and is not claimed: the fibre above is a genuine double-coset set and
nothing computed below separates its elements.
"""
from sage.all import CartanMatrix, QQ, ZZ, block_diagonal_matrix, matrix

from sage_extensions.all import EvenTwoElementaryLattices, Lattices

E8 = -CartanMatrix(['E', 8])            # the book's E8 is negative definite
U = matrix(ZZ, [[0, 1], [1, 0]])
U2, E82 = 2 * U, 2 * E8

TEN_GRAM = block_diagonal_matrix(U, U2, E82)
TCO_GRAM = block_diagonal_matrix(matrix(ZZ, [[2]]), U2, E82)

ten = Lattices(ZZ)([list(row) for row in TEN_GRAM.rows()])
co = Lattices(ZZ)([list(row) for row in TCO_GRAM.rows()])
print('T_En: rank %2d, signature %s, det %4s' % (ten.module_rank(),
      tuple(int(x) for x in ten.signature_pair()), int(ten.determinant())))
print('T_Co: rank %2d, signature %s, det %4s' % (co.module_rank(),
      tuple(int(x) for x in co.signature_pair()), int(co.determinant())))
assert int(ten.determinant()) == 2 ** 10 and int(co.determinant()) == -2 ** 11


def make(lattice, coefficients):
    ring = lattice.base_ring()
    return lattice.linear_combination({index: ring(int(value)) for index, value in coefficients.items()})


# T_En basis: e, f, e', f', a1..a8.   T_Co basis: h, e', f', a1..a8.
eta = {0: {0: 1, 1: 1}, 1: {2: 1}, 2: {3: 1}, **{3 + i: {4 + i: 1} for i in range(8)}}
for i in range(int(co.module_rank())):
    for j in range(int(co.module_rank())):
        left, right = make(co, {i: 1}), make(co, {j: 1})
        assert int(left.b(right)) == int(make(ten, eta[i]).b(make(ten, eta[j])))
print('eta is an isometry of the two Gram matrices   AGREE')

k = make(ten, {0: 1, 1: -1})
assert int(k.b(k)) == -2 and all(int(k.b(make(ten, eta[i]))) == 0 for i in eta)
print('k = e~ - f~: square -2 and orthogonal to eta(T_Co)   AGREE')

bill = make(ten, {0: 1})                       # e~
v1 = make(co, {1: 1})                          # e'
v2 = make(co, {0: 2, 3: 1, 4: 1})              # 2h + a_1 + a_2
w1 = make(ten, eta[1])                         # eta(v_1) = e~'
w2 = make(ten, {0: 2, 1: 2, 4: 1, 5: 1})       # eta(v_2)

print()
print('the representatives:')
for name, element, lattice in (('v_1 = e\'', v1, co), ('v_2 = 2h+a_1+a_2', v2, co),
                               ('eta(v_1)', w1, ten), ('e~ (target)', bill, ten)):
    print('   %-16s isotropic %-5s div %d' % (name, int(element.b(element)) == 0, int(lattice.div(element))))

# (i) the pairing identity and the divisibility formula, on both representatives.
print()
for name, v, image in (('v_1', v1, w1), ('v_2', v2, w2)):
    left = int(image.b(bill))
    right = QQ(int(v.b(make(co, {0: 1})))) / 2
    divisor = int(ten.div(image))
    formula = int(ZZ(int(co.div(v))).gcd(ZZ(int(right)))) if right.denominator() == 1 else None
    print('   %s: beta_En(eta(v), e~) = %d, beta_Co(v,h)/2 = %s   %s'
          % (name, left, right, 'AGREE' if left == right else '*** DIFFER'))
    print('       div_En(eta(v)) = %d, gcd(div_Co(v), beta_Co(v,h)/2) = %s   %s'
          % (divisor, formula, 'AGREE' if divisor == formula else '*** DIFFER'))
    assert left == right and divisor == formula

# (ii) the parity facts, structurally rather than by sampling.
assert all(int(TCO_GRAM[i, j]) % 2 == 0 for i in range(TCO_GRAM.nrows()) for j in range(TCO_GRAM.ncols()))
print()
print('the Gram of T_Co is even entrywise, so div_Co is even for every vector   AGREE')

rest = block_diagonal_matrix(U2, E82)
halved = matrix(QQ, rest) / 2
assert all(entry in ZZ for entry in halved.list())
halved = matrix(ZZ, halved)
assert all(int(halved[i, i]) % 2 == 0 for i in range(halved.nrows()))
print('U(2) + E8(2) is twice an even lattice, so y^2 = 0 mod 4 for every y in that block   AGREE')

# The two target cusps, by the maintained two-elementary route.
print()
for name, element in (('e~ (div 1)', bill), ('eta(v_1) (div 2)', w1)):
    quotient = element.isotropic_reduction()
    invariants = EvenTwoElementaryLattices(quotient.base_ring())(quotient).two_elementary_invariants()
    print('   %-18s boundary lattice: rank %2d, det %5s, two_elementary (r,a,delta) = %s'
          % (name, quotient.module_rank(), int(quotient.determinant()),
             tuple(int(x) for x in invariants)))

# The image criterion, in closed form.  w~ lies in the image iff some gamma in Gamma_En carries it into
# k^perp, i.e. iff beta(w~, gamma^{-1}k) = 0: iff w~ is orthogonal to some (-2)-vector in the Gamma_En
# orbit of k.  The (-2)-vectors of T_En are the solutions of 2ab + y^2 = -2 with y in U(2) + E8(2), so
# the candidate set is finite and the criterion is decidable; but the necessary condition "orthogonal to
# SOME (-2)-vector" is not sufficient, and the following candidate shows how weakly it excludes.
candidate = make(ten, {0: 2, 2: 1})                 # 2e~ + e~'
witness = make(ten, {0: 1, 1: -1, 3: 1})            # e~ - f~ + f~'
print()
print('candidate w~ = 2e~ + e~\': isotropic %s, div %d' % (int(candidate.b(candidate)) == 0,
                                                          int(ten.div(candidate))))
assert int(candidate.b(candidate)) == 0 and int(ten.div(candidate)) == 2
print('   witness k\' = e~ - f~ + f~\': square %d, beta(k\', w~) = %d'
      % (int(witness.b(witness)), int(witness.b(candidate))))
assert int(witness.b(witness)) == -2 and int(witness.b(candidate)) == 0
quotient = candidate.isotropic_reduction()
invariants = EvenTwoElementaryLattices(quotient.base_ring())(quotient).two_elementary_invariants()
print('   so w~ passes the necessary condition; its boundary lattice is rank %2d, det %5s, (r,a,delta) %s'
      % (quotient.module_rank(), int(quotient.determinant()), tuple(int(x) for x in invariants)))
print('   nothing here decides whether k\' lies in the Gamma_En orbit of k, which is what the criterion needs')

# Separability: e' and f' are incongruent mod 2, so their target classes differ (proved separately;
# here the coordinate parity is read off the library's own coordinates).
ep_t, fp_t = make(ten, {2: 1}), make(ten, {3: 1})
difference = ep_t - fp_t
vector = difference.to_vector()
coefficients = vector.parent()._selected_module_coefficients(vector)
coordinates = [int(coefficients.get(index, 0)) for index in sorted(coefficients)]
print()
print('e~\' and f~\' both have divisibility %d in T_En' % (int(ten.div(ep_t)),))
assert int(ten.div(ep_t)) == 2 and int(ten.div(fp_t)) == 2
print('the coordinates of e~\' - f~\' are %s, so the difference is not in 2*T_En:' % coordinates)
print('   the two target classes are distinct, since Gamma_En acts trivially on the discriminant group')
assert any(value % 2 for value in coordinates)

print()
print('div_En(eta(v)) is even for every primitive isotropic v of T_Co, hence 2;')
print('div(e~) = 1, and divisibility is an isometry invariant, so no Gamma_En-translate of any eta(v)')
print('can be e~: the divisibility-1 cusp lies outside the image and Phi is NOT SURJECTIVE.')
