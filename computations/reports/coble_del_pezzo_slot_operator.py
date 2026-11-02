"""The del Pezzo slot of the Coble tuple, as an operator on S_Co, through the owner's operations.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_del_pezzo_slot_operator.py

The obligation.  The Coble tuple of the book carries a del Pezzo slot.  The candidate
considered is the operator phi on S_Co = <2> + <-2>^10 which is +1 on the primitive
U(2) spanned by f^*F_1 = 3e_0 - (e_1+...+e_9) and f^*F_2 = 3e_0 - (e_1+...+e_8) - e_10,
and -1 on its orthogonal complement N inside S_Co.  What has to be certified, and is
certified below by the owner's own operations, is:

  * that phi is an integral isometry of S_Co -- built by ``S.O()`` from its images on the
    eleven basis vectors, so that the isometry property is the owner's, not an assertion;
  * that it is an involution, that it fixes H = f^*F_1 + f^*F_2, and that it reverses
    alpha = 3e_0 - (e_1+...+e_10), all as equalities of lattice elements;
  * that phi acts on the discriminant group A_{S_Co} as the identity, checked as equality
    of discriminant elements on the owner's generating set -- not inferred from q(-x) = q(x);
  * that S_Co = <f^*F_1,f^*F_2> perp N is an orthogonal direct sum of index 1, through the
    owner's primitive-sublattice and orthogonal-complement operations and determinants;
  * that A_{T_Co} has exponent 2 -- the stated 2-elementarity of T_Co -- and that the
    discriminant morphism of -id_{T_Co} is the identity there, which is what makes
    -id_{T_Co} an identity on discriminant elements rather than merely a form-preserving map.

What is *not* done here.  No L_K3 object and no gluing S_Co + T_Co -> L_K3 is built; the
extension over L_K3 in the book is the cited criterion @thm:automorphism-lifting-criterion
applied to the two trivial-discriminant facts above, and it is recorded as a theorem
application with its hypotheses named, not as a computation.  Nothing here says anything
about automorphisms of the Coble surface, about Kaehler cones, or about chambers: the
corollary in the manuscript is about the marking of the construction, and the residual
geometric question remains open.

Provenance.  sage-extensions at the provider pin c546077dce79a76eb32e92d080aa9c44e4c67552
(the pin this project records for ``.scratch/se-provider-c546``, exported read-only and
carrying no git metadata of its own), Sage 11.0.beta5, the shared image rootfs mounted
read-only, the repository bound at /repo.  Printed before anything is computed.

Construction, not certification.  The images of the eleven basis vectors are obtained
inside this script from the defining projection, with Sage's own linear algebra on the Gram
matrix; the resulting combinations are handed to ``S.O()``, which accepts the images only
if they define an isometry of S_Co.  No pairing, dual basis, discriminant representative or
group membership is computed by hand anywhere below.
"""
import sys

from sage.all import QQ, ZZ, diagonal_matrix, identity_matrix, matrix
from sage.version import version as sage_version

from sage_extensions.all import Lattices

sys.stdout.reconfigure(line_buffering=True)

PIN = 'c546077dce79a76eb32e92d080aa9c44e4c67552'

print('provenance')
print('  sage-extensions provider pin: %s (.scratch/se-provider-c546/src, read-only export)' % PIN)
print('  Sage: %s' % sage_version)
print('  image rootfs: $HOME/sage-image/rootfs, mounted read-only; repo bound at /repo')
print('')

# ---------------------------------------------------------------- S_Co = <2> + <-2>^10
GRAM_S = diagonal_matrix(ZZ, [2] + [-2] * 10)
S = Lattices(ZZ)([list(row) for row in GRAM_S.rows()])
assert S.module_rank() == 11
ring = S.base_ring()

basis = [S.basis_vector(i) for i in range(11)]
e0 = basis[0]


def sparse(d):
    return S.linear_combination({i: ring(c) for i, c in d.items() if c})


a = sparse({0: 3, **{i: -1 for i in range(1, 10)}})          # f^*F_1
b = sparse({0: 3, **{i: -1 for i in range(1, 9)}, 10: -1})    # f^*F_2
H = a + b
alpha = sparse({0: 3, **{i: -1 for i in range(1, 11)}})

print('S_Co = <2> + <-2>^10;  basis e_0..e_10;  a = f^*F_1, b = f^*F_2, H = a+b, alpha')
print('  |det S_Co| = %d, |A_{S_Co}| = %d'
      % (abs(int(S.determinant())), S.discriminant_group().cardinality()))
print('  q(a) = %d, q(b) = %d, b(a,b) = %d, q(H) = %d, q(alpha) = %d'
      % (int(a.q()), int(b.q()), int(S.b(a, b)), int(H.q()), int(alpha.q())))
assert int(a.q()) == 0 and int(b.q()) == 0 and int(S.b(a, b)) == 2
assert int(H.q()) == 4 and int(alpha.q()) == -2
assert int(S.b(alpha, a)) == 0 and int(S.b(alpha, b)) == 0 and int(S.b(alpha, H)) == 0
print('  alpha is orthogonal to a, b and H: True')

# ---------------------------------------------------------------- the decomposition, by the owner
U2 = S.primitive_sublattice_from([a, b])
print('  <a,b> as a primitive sublattice: rank %d, determinant %d'
      % (U2.module_rank(), int(U2.determinant())))
assert U2.module_rank() == 2 and int(U2.determinant()) == -4

N = S.orthogonal_complement(U2)
print('  N = <a,b>^perp in S_Co:      rank %d, determinant %d'
      % (N.module_rank(), int(N.determinant())))
assert N.module_rank() == 9 and int(N.determinant()) == -512
print('  det<a,b> * det N == det S_Co (index 1): %s'
      % (int(U2.determinant()) * int(N.determinant()) == int(S.determinant())))
assert int(U2.determinant()) * int(N.determinant()) == int(S.determinant())

# ---------------------------------------------------------------- the operator, by its definition
# phi = +1 on span(a,b), -1 on its complement: the projection is taken with Sage's linear algebra
# on the Gram matrix, and the images are handed to S.O(), which accepts them only as an isometry.
G = matrix(QQ, [list(row) for row in GRAM_S.rows()])
ca = [int(x) for x in a.to_vector()]
cb = [int(x) for x in b.to_vector()]
At = matrix(QQ, 11, 2, lambda i, j: ca[i] if j == 0 else cb[i])   # columns a, b in e-coordinates
Gram2 = matrix(QQ, [[int(S.b(a, a)), int(S.b(a, b))], [int(S.b(b, a)), int(S.b(b, b))]])
assert Gram2 == At.transpose() * G * At
# the orthogonal projection onto span(a,b) inside the formed space (S_Co, G)
proj = At * Gram2.inverse() * At.transpose() * G
phi_matrix = 2 * proj - identity_matrix(QQ, 11)

integral = all(QQ(phi_matrix[j, i]).denominator() == 1 for i in range(11) for j in range(11))
print('  the defining matrix has integer entries on the e-basis: %s' % integral)

images = {}
for i in range(11):
    images[i] = S.linear_combination(
        {j: ring(int(QQ(phi_matrix[j, i]))) for j in range(11) if QQ(phi_matrix[j, i])})
phi = S.O()(lambda label: images[int(label)])
print('  phi built by S.O() from its images on the basis: accepted as an isometry of S_Co')

# ---------------------------------------------------------------- its properties
basis_ok = all(S.b(phi(x), phi(y)) == S.b(x, y) for x in basis for y in basis)
print('  phi preserves the pairing on the basis: %s' % basis_ok)
assert basis_ok

square_ok = all(phi(phi(v)) == v for v in basis)
print('  phi is an involution:                   %s' % square_ok)
assert square_ok

print('  phi(a) == a, phi(b) == b:               %s'
      % (phi(a) == a and phi(b) == b))
print('  phi(H) == H:                            %s' % (phi(H) == H))
print('  phi(alpha) == -alpha:                   %s' % (phi(alpha) == -alpha))
assert phi(a) == a and phi(b) == b and phi(H) == H and phi(alpha) == -alpha

# the eigenspaces, as statements about the owner's sublattices
inc_U2, inc_N = U2.inclusion(), N.inclusion()
print('  the (+1)-eigenspace contains <a,b>:     %s'
      % all(phi(inc_U2(v)) == inc_U2(v) for v in U2.module_generators()))
fixed_N = [v for v in N.module_generators() if phi(inc_N(v)) == -inc_N(v)]
print('  phi acts as -1 on a basis of N:         %s' % (len(fixed_N) == N.module_rank()))
assert all(phi(inc_U2(v)) == inc_U2(v) for v in U2.module_generators())
assert len(fixed_N) == N.module_rank()

# ---------------------------------------------------------------- the discriminant action
D = S.discriminant_group()
classes = [S.discriminant_class(S.primitive_dual(v)) for v in basis]
action = phi.discriminant_morphism()
trivial = all(action(c) == c for c in classes)
print('  rho(phi) fixes all %d discriminant generators: %s' % (len(classes), trivial))
assert trivial, 'phi does not act trivially on A_{S_Co}'
print('  A_{S_Co} has exponent 2:                %s'
      % all(2 * c == D.zero() for c in classes))

print('')
print('T_Co = <2> + U(2) + E8(2);  the -id factor')
from sage.all import CartanMatrix, block_diagonal_matrix  # noqa: E402

E8 = -CartanMatrix(['E', 8])
U = matrix(ZZ, [[0, 1], [1, 0]])
GRAM_T = block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8)
T = Lattices(ZZ)([list(row) for row in GRAM_T.rows()])
assert T.module_rank() == 11 and abs(int(T.determinant())) == 2048

basis_T = [T.basis_vector(i) for i in range(11)]
minus_id = T.O()(lambda label: -basis_T[int(label)])
assert all(minus_id(minus_id(v)) == v for v in basis_T)

DT = T.discriminant_group()
classes_T = [T.discriminant_class(T.primitive_dual(v)) for v in basis_T]
exponent_two = all(2 * c == DT.zero() for c in classes_T)
print('  A_{T_Co} has exponent 2 (T_Co is 2-elementary): %s' % exponent_two)
assert exponent_two, 'T_Co is not 2-elementary at this construction'

action_T = minus_id.discriminant_morphism()
trivial_T = all(action_T(c) == c for c in classes_T)
print('  rho(-id_{T_Co}) fixes all %d discriminant generators: %s'
      % (len(classes_T), trivial_T))
assert trivial_T, '-id does not act trivially on A_{T_Co}'
print('  (form preservation alone would not give this; the exponent 2 above is the premise)')

print('')
print('CONCLUSION')
print('  phi is an integral isometry of S_Co, an involution, it fixes H, it reverses alpha,')
print('  it acts trivially on A_{S_Co}; A_{T_Co} has exponent 2 and -id acts trivially on it.')
print('  Those are exactly the hypotheses of @thm:automorphism-lifting-criterion for the pair')
print('  (phi|_{S_Co}, -id_{T_Co}) over S_Co + T_Co -> L_K3.  L_K3 and its gluing are NOT built')
print('  in this run: the extension is that theorem applied to the two verified facts, and the')
print('  geometric statements about automorphisms, Kaehler cones and chambers are not touched.')
print('')
print('OK: the del Pezzo slot candidate is certified on S_Co and T_Co by the owner\'s operations')
