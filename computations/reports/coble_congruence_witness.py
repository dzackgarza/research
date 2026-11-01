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
verified here is that one is, so that Gamma_Co is a proper subgroup of Gamma^cong.

The witness.  sigma = the transposition of the two isotropic generators e', f' of the U(2) summand of

    T_Co = <2> + U(2) + E8(2),   basis zeta; e', f'; a_1..a_8,

which is the reflection in e' - f'.  It is proposed as the witness; what the owner's operations
verify is each property the argument needs, and they are verified or the run fails:

  * sigma is built as L.reflection(e' - f'), not as a matrix, and it transposes e' and f' and fixes
    zeta and the eight E8(2) roots (equality of lattice elements);
  * sigma in L.O_plus(), the owner's O^+(L) = O(L) cap ker(sn_RR) (Gritsenko-Hulek-Sankaran §1),
    which is the book's Orth^+(L) = Theta_R(L) of `def:spinor-norm`;
  * sigma not in L.stable_orthogonal_group(), so rho(sigma) is nontrivial and sigma is not in
    Gamma_Co; sigma is also not in L.special_orthogonal_group(), which is consistent and is the
    reason O^+ is not SO here;
  * the discriminant classes of the three blocks, got as L.discriminant_class(L.primitive_dual(v)),
    are nonzero and satisfy q([e'/2]) = q([f'/2]) = 0 (isotropic), q([zeta/2]) = 1/2 (the value the
    book's `prop:coble-discriminant-group` records), and b([e'/2],[f'/2]) = 1/2 with the U(2)-block
    orthogonal to the <2>- and E8(2)-blocks; and |A_{T_Co}| = |det T_Co| = 2048;
  * sigma.discriminant_morphism() transposes [e'/2] and [f'/2] and fixes [zeta/2] and all eight
    [a_i/2], so rho(sigma) lies in P and is not the identity.

Conclusion.  sigma in Orth^+(T_Co) cap rho^{-1}(P) with rho(sigma) != 1, hence Gamma_Co <
Gamma^cong strictly, and [Gamma^cong : Gamma_Co] >= 2.

How this is done, and how it is not.  Every step above is an owner call: Lattices, reflection,
O_plus, stable_orthogonal_group, special_orthogonal_group, primitive_dual, discriminant_class,
discriminant_morphism.  No determinant, Gram pairing, dual basis, contragredient or isometry test is
reimplemented here.  That is deliberate and is the lesson recorded in
`computations/reports/t4_discriminant_action.py`: an earlier version of that report built the
coordinate contragredient by hand, transposed it, and reported a (-2)-root as outside the
discriminant kernel — wrong arithmetic that was a defect of the report, not of the library.  The
same objection applies to a hand-built action on the discriminant group: transcribing classes into
coordinates and permuting them re-derives the very morphism the owner provides.

Not claimed: strictness for the Heegner group Gamma^Hdg.  That needs an element of Gamma_{En,2}
fixing the Heegner line and acting nontrivially on A_{T_Co}; no such element is proposed here, and
the manuscript records that question as open.
"""
import sys

from sage.all import CartanMatrix, QQ, ZZ, block_diagonal_matrix, matrix

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

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
def klass(vector):
    """The discriminant class of v/div(v), through the owner's projection."""
    return L.discriminant_class(L.primitive_dual(vector))


D = L.discriminant_group()
zero = D.zero()
c_zeta, c_e, c_f = klass(zeta), klass(e_prime), klass(f_prime)
c_roots = [klass(r) for r in roots]

# The values of q and b live in quotient rings of Frac(ZZ), and comparing one of them with a plain
# integer is silently False rather than an error: q([e'/2]) == 0 is False although the class is
# isotropic, because the zero of that parent is not ZZ(0).  Every value is therefore lifted to QQ
# before it is compared here.
ZERO, HALF = QQ(0), QQ(1) / QQ(2)


def qval(cls):
    return cls.q().lift()


def pair(cls1, cls2):
    return cls1.b(cls2).lift()


print('  classes nonzero: zeta/2 %s, e\'/2 %s, f\'/2 %s'
      % (c_zeta != zero, c_e != zero, c_f != zero))
assert c_zeta != zero and c_e != zero and c_f != zero
print('  q(zeta/2) = %s, q(e\'/2) = %s, q(f\'/2) = %s' % (qval(c_zeta), qval(c_e), qval(c_f)))
assert qval(c_e) == ZERO and qval(c_f) == ZERO, 'the two U(2) classes are not isotropic'
assert qval(c_zeta) == HALF, 'q(zeta/2) should be 1/2, as prop:coble-discriminant-group records'
print('  b(e\'/2, f\'/2) = %s' % pair(c_e, c_f))
assert pair(c_e, c_f) == HALF
orthogonal = all(pair(c_e, c) == ZERO and pair(c_f, c) == ZERO for c in [c_zeta] + c_roots)
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
print('  Every step is an owner call; no contragredient, dual basis or pairing is built here.')
print('OK: the congruence group strictly contains the stable group, witnessed by an owner-built isometry')
