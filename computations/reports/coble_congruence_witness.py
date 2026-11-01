"""The integral witness for the congruence group, through the owner's own operations.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_congruence_witness.py

The obligation.  The report's congruence group is Gamma^cong = rho^{-1}(P) with
P = O(q_{U(2)}) x O(q_{E8(2)}), and P is nontrivial.  That alone does not separate rho^{-1}(P) from
the stable group Gamma_Co = Orth^+(T_Co) cap ker(rho): a preimage of a subgroup is larger than the
kernel only when some element of the subgroup is realised by an isometry of the lattice.  The claim
verified below is that one is, so Gamma_Co is a proper subgroup of Gamma^cong.

The witness, proposed first and verified second.  sigma := the transposition of the two isotropic
generators e', f' of the U(2) summand of

    T_Co = <2> + U(2) + E8(2),   basis zeta; e', f'; a_1..a_8,

which is the reflection in e' - f'.  Every property the argument needs is an owner call, and the run
fails if one of them does not hold:

  * Lattices.reflection(e' - f') builds sigma; it is not supplied as a matrix, and the checks that it
    transposes e', f' and fixes zeta and the eight E8(2) roots are equalities of lattice elements;
  * sigma in L.O_plus(), the owner's O^+(L) = O(L) cap ker(sn_RR) (Gritsenko-Hulek-Sankaran
    arXiv:0810.1614 §1), which is the book's Orth^+(L) = Theta_R(L) of `def:spinor-norm`;
  * sigma not in L.stable_orthogonal_group(), so rho(sigma) != 1 and sigma is outside Gamma_Co;
    sigma not in L.special_orthogonal_group(), consistently, a reflection having determinant -1;
  * the classes are L.discriminant_class(L.primitive_dual(v)); the action is
    isometry.discriminant_morphism(); |A_{T_Co}| = |det T_Co| = 2048.

Discriminant values.  The values of q and b lie in the owner's value modules, where equality is
parent-sensitive by contract, so every comparison below is made in the value module itself:
q-values against D.quadratic_value_module().zero(), b-values against
D.bilinear_value_module().zero(), and the two half-values against a half constructed in the same
module from the lattice's own fraction field.  No representative is lifted and compared.

Provenance of this run.  sage-extensions at the provider pin c546077dce79a76eb32e92d080aa9c44e4c67552
(the pin this project records for `.scratch/se-provider-c546`, which is exported read-only and carries
no git metadata of its own; the same pin as `coble_heegner_stabilizer_orbits.py`), Sage 11.0.beta5, the
shared image rootfs mounted read-only, and the repository path bound at /repo.  The script prints these
before it computes.

Not claimed: strictness for the Heegner group Gamma^Hdg.  That needs an element of Gamma_{En,2} fixing
the Heegner line and acting nontrivially on A_{T_Co}; no such element is proposed here, and the
manuscript records that question, the theta-side question, the finite-image comparison and the period
statement as open.
"""
import sys

from sage.all import CartanMatrix, QQ, ZZ, block_diagonal_matrix, matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'

print('provenance')
print('  sage-extensions provider pin: %s (.scratch/se-provider-c546/src, read-only export)' % PIN)
print('  Sage: %s' % sage_version)
print('  image rootfs: $HOME/sage-image/rootfs, mounted read-only; repo bound at /repo')
print('')

E8 = -CartanMatrix(['E', 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
GRAM = block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8)
L = Lattices(ZZ)([list(row) for row in GRAM.rows()])

# basis: 0 = zeta, 1 = e', 2 = f', 3..10 = a_1..a_8
basis = [L.basis_vector(i) for i in range(L.rank())]
zeta, e_prime, f_prime = basis[0], basis[1], basis[2]
roots = basis[3:]

print('T_Co = <2> + U(2) + E8(2);  sigma := L.reflection(e\' - f\')')
print('  |det T_Co| = %d, |A_{T_Co}| = %d'
      % (abs(int(L.determinant())), L.discriminant_group().cardinality()))
assert abs(int(L.determinant())) == 2048

v = e_prime - f_prime
print('  q(e\' - f\') = %d' % int(v.q()))
sigma = L.reflection(v)

# ---------------------------------------------------------------- the witness on the lattice
print('  sigma(e\') == f\': %s;  sigma(f\') == e\': %s'
      % (sigma(e_prime) == f_prime, sigma(f_prime) == e_prime))
print('  sigma fixes zeta and all 8 E8(2) roots: %s'
      % (sigma(zeta) == zeta and all(sigma(r) == r for r in roots)))
assert sigma(e_prime) == f_prime and sigma(f_prime) == e_prime
assert sigma(zeta) == zeta and all(sigma(r) == r for r in roots)

in_plus = sigma in L.O_plus()
in_stable = sigma in L.stable_orthogonal_group()
in_special = sigma in L.special_orthogonal_group()
print('  sigma in O_plus (= Orth^+(T_Co), the spinor kernel over RR): %s' % in_plus)
print('  sigma in stable_orthogonal_group (= ker rho):                %s' % in_stable)
print('  sigma in special_orthogonal_group:                           %s' % in_special)
assert in_plus, 'the witness is not in Orth^+(T_Co)'
assert not in_stable, 'the witness acts trivially on the discriminant'
assert not in_special, 'the reflection would have determinant +1'

# ---------------------------------------------------------------- the discriminant blocks
D = L.discriminant_group()
QV, BV = D.quadratic_value_module(), D.bilinear_value_module()
zero_q, zero_b = QV.zero(), BV.zero()

# The half is built in the lattice's own fraction field and then in each value module, so that every
# comparison is an equality of values inside their own parent.
F = L.base_ring().fraction_field()
half = F(L.base_ring()(1)) / F(L.base_ring()(2))
half_q, half_b = QV(half), BV(half)


def klass(vector):
    """The discriminant class of v/div(v), through the owner's projection."""
    return L.discriminant_class(L.primitive_dual(vector))


c_zeta, c_e, c_f = klass(zeta), klass(e_prime), klass(f_prime)
c_roots = [klass(r) for r in roots]
print('  classes nonzero: zeta/2 %s, e\'/2 %s, f\'/2 %s'
      % (c_zeta != D.zero(), c_e != D.zero(), c_f != D.zero()))
assert c_zeta != D.zero() and c_e != D.zero() and c_f != D.zero()
print('  q(e\'/2) == q(f\'/2) == 0 in the quadratic value module: %s'
      % (c_e.q() == zero_q and c_f.q() == zero_q))
assert c_e.q() == zero_q and c_f.q() == zero_q, 'the two U(2) classes are not isotropic'
print('  q(zeta/2) == 1/2 in the quadratic value module: %s' % (c_zeta.q() == half_q))
assert c_zeta.q() == half_q, 'q(zeta/2) should be 1/2, as prop:coble-discriminant-group records'
print('  b(e\'/2, f\'/2) == 1/2 in the bilinear value module: %s' % (c_e.b(c_f) == half_b))
assert c_e.b(c_f) == half_b
orthogonal = all(c_e.b(c) == zero_b and c_f.b(c) == zero_b for c in [c_zeta] + c_roots)
print('  the U(2) block is orthogonal to the <2> and E8(2) blocks: %s' % orthogonal)
assert orthogonal

# ---------------------------------------------------------------- the induced action
action = sigma.discriminant_morphism()
print('  rho(sigma) transposes e\'/2 and f\'/2: %s'
      % (action(c_e) == c_f and action(c_f) == c_e))
print('  rho(sigma) fixes zeta/2 and all 8 root classes: %s'
      % (action(c_zeta) == c_zeta and all(action(c) == c for c in c_roots)))
assert action(c_e) == c_f and action(c_f) == c_e
assert action(c_zeta) == c_zeta and all(action(c) == c for c in c_roots)

print('')
print('CONCLUSION')
print('  sigma in Orth^+(T_Co) with rho(sigma) in O(q_{U(2)}) x O(q_{E8(2)}) and rho(sigma) != 1,')
print('  so sigma lies in the congruence preimage rho^{-1}(P) and not in')
print('  Gamma_Co = Orth^+(T_Co) cap ker(rho): the inclusion is strict, [rho^{-1}(P) : Gamma_Co] >= 2.')
print('  Every step is an owner call; no contragredient, dual basis, pairing or comparison is built here.')
print('OK: the congruence group strictly contains the stable group, witnessed by an owner-built isometry')
