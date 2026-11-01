"""Which reflections act trivially on the discriminant, decided by the owner's own morphism.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/t4_discriminant_action.py

The arithmetic first, because it settles what the answer must be.  Let r be a *primitive* lattice
vector with an integral reflection, rho_r(x) = x - 2 b(x, r) r / b(r, r).  For x in the metric dual
L^# the difference rho_r(x) - x is an integral multiple of r exactly when the coefficient
2 b(x, r) / b(r, r) is an integer for every such x, i.e. exactly when b(x, r) lies in
(|b(r, r)| / 2) Z for every x in L^#.  For r primitive the values b(x, r), x in L^#, run over all
of Z -- that is what primitivity means for the functional b(., r) -- so the condition is
|b(r, r)| = 2 and nothing else: a reflection acts trivially on the discriminant exactly for the
primitive vectors of square +2 or -2, which is Laza--O'Grady's Example 1.2.2(2), and a primitive
(-4)-vector is never such a vector.  The primitivity cannot be dropped: r = 2 a with a^2 = -2 spans
the same line as a and gives the *same* reflection, rho_{2a} = rho_a, and yet |q(2a)|/2 = 4, so a
criterion phrased in the coordinates of r itself would call the same reflection trivial for a and
non-trivial for 2a.  The script below therefore tests the reflection of a primitive vector in each
case and records the non-primitive example separately, as the reason the hypothesis is there.

The measurement uses the owner's discriminant morphism, isometry.discriminant_morphism(),
the action of O(L) on O(A_L) that Lattices.discriminant_representation() packages, and
Lattices.stable_orthogonal_group() for the kernel itself.  No coordinate contragredient is
built by hand here: an earlier version of this file built one, transposed it, and reported the
(-2)-root as outside the kernel, which is wrong arithmetic and was a defect of that file, not
of the library.  If the owner's morphism disagrees with the criterion above, the disagreement
is reported as a library defect rather than absorbed into the arithmetic conclusion.
"""
from sage.all import ZZ, CartanMatrix, block_diagonal_matrix, gcd, matrix

from sage_extensions.all import Lattices

U = matrix(ZZ, [[0, 1], [1, 0]])
E8 = -CartanMatrix(['E', 8])
D17 = -CartanMatrix(['D', 17])
T4_GRAM = block_diagonal_matrix(matrix(ZZ, [[-4]]), U, U, E8, E8)
L19_GRAM = block_diagonal_matrix(U, U, D17)

T4 = Lattices(ZZ)([list(row) for row in T4_GRAM.rows()])
L19 = Lattices(ZZ)([list(row) for row in L19_GRAM.rows()])


def measure(label, lattice, gram, isometry, vector, expected):
    """Report the discriminant action through the owner's morphism, and the criterion."""
    action = isometry.discriminant_morphism()
    discriminant = lattice.discriminant_group()
    generators = tuple(discriminant.module_generators())
    trivial = all(action(g) == g for g in generators)
    kernel_membership = isometry in lattice.stable_orthogonal_group()
    print('%-46s q(r) = %3s   fixes A_L (morphism): %-5s   in stable group: %-5s'
          % (label, vector.q(), trivial, kernel_membership))
    assert trivial == kernel_membership, (label, 'the two owner answers disagree')
    assert trivial is expected, (label, 'the owner disagrees with the arithmetic', trivial, expected)
    return trivial


# ---------------------------------------------------------------- Lambda_19
basis19 = [L19.basis_vector(i) for i in range(21)]
e1, f1, e2 = basis19[0], basis19[1], basis19[2]

root = basis19[4]
assert root.q() == -2
root_reflection = L19.reflection(root)
assert all(root_reflection(root_reflection(v)) == v for v in basis19), 'not an involution'
measure('Lambda_19: reflection in the (-2)-root a_1', L19, L19_GRAM, root_reflection, root, True)

long_root = basis19[19] + basis19[20]
assert long_root.q() == -4
long_reflection = L19.reflection(long_root)
measure('Lambda_19: reflection in a_16 + a_17 of square -4', L19, L19_GRAM, long_reflection, long_root, False)

minus_h_plus = L19.Aut()(lambda label: ((-1 if label in (0, 1, 2, 3) else 1)
                                        * L19.module_generator(label)))
assert minus_h_plus(e1) == -e1 and minus_h_plus(e2) == -e2
measure('Lambda_19: -1 on H = U + U, +1 on L', L19, L19_GRAM, minus_h_plus, basis19[2], True)

# ------------------------------------- the component character, on O(H) not on the centre
# Lemma A.10(1) of arXiv:1801.04845 supplies, for every J in I_2(U + U), an element of
# O(U + U) \ O^+(U + U) fixing J; extended by the identity on L it is an element of O(Lambda_19)
# outside O^+(Lambda_19) fixing J, and it is in the discriminant kernel because H is unimodular.
# The concrete candidate is -1 on ONE hyperbolic summand, +1 on the other and on L.  The central
# -id is *not* this element: on a type IV lattice with two positive directions it acts as -1 on
# the whole positive plane, hence with determinant (-1)^2 = +1, so it lies in O^+ -- and it is
# outside the discriminant kernel, since A_{Lambda_19} = Z/4 and -1 acts on it non-trivially.
import numpy as np

one_u_minus = L19.Aut()(lambda label: ((-1 if label in (0, 1) else 1)
                                       * L19.module_generator(label)))
assert one_u_minus(e1) == -e1 and one_u_minus(f1) == -f1
assert one_u_minus(e2) == e2 and one_u_minus(basis19[4]) == basis19[4]
# J = <e_1, e_2> is carried to itself as a sublattice: e_1 to -e_1 and e_2 to e_2.
measure('-1 on one U, +1 on the other U and on L', L19, L19_GRAM, one_u_minus, basis19[0], True)

central_minus = L19.Aut()(lambda label: -L19.module_generator(label))
measure('central -id on Lambda_19', L19, L19_GRAM, central_minus, basis19[0], False)


def orientation_on_positive(eigenspace_gram, label):
    """det of the isometry on the positive plane: (-1)^(number of positive -1-eigenspace lines)."""
    eigenvalues = np.linalg.eigvalsh(np.array([[float(entry) for entry in row]
                                               for row in eigenspace_gram.rows()]))
    positive = int((eigenvalues > 1e-8).sum())
    print('%-46s -1-eigenspace signature: (%d positive, %d negative) -> det on P = %+d'
          % (label, positive, int((eigenvalues < -1e-8).sum()), (-1) ** positive))
    return (-1) ** positive


ONE_U = matrix(ZZ, [[0, 1], [1, 0]])
WHOLE = L19_GRAM
for label, gram in (('-1 on one U', ONE_U), ('central -id', WHOLE)):
    determinant = orientation_on_positive(gram, label)
    if label == '-1 on one U':
        assert determinant == -1, 'the one-U element must reverse the positive orientation'
    else:
        assert determinant == 1, 'the central -id must preserve it'

# ---------------------------------------------------------------- T_4
t4_root = T4.basis_vector(0)
assert t4_root.q() == -4
t4_reflection = T4.reflection(t4_root)
measure('T_4: reflection in the <-4> generator', T4, T4_GRAM, t4_reflection, t4_root, False)

# ------------------------------------------------- the primitivity hypothesis, exhibited
# r = 2a with a^2 = -2 spans the line of a and defines the *same* reflection, since
# x - 2b(x,2a)/b(2a,2a) (2a) = x - (2b(x,a)/b(a,a)) a.  The pair is the reason the criterion is
# stated for primitive r: |q(2a)|/2 = 4 while |q(a)|/2 = 1, so a test reading the coordinates of r
# itself would call one and the same reflection trivial for a and non-trivial for 2a.
a = basis19[4]
twice = 2 * a
assert a.q() == -2 and twice.q() == -8 and twice.q() == 4 * a.q()
print('r = 2a with a^2 = -2: q(a) = %s, q(2a) = %s, and 2b(x,2a)/b(2a,2a) (2a) = 2b(x,a)/b(a,a) a,'
      % (a.q(), twice.q()))
print('so rho_{2a} and rho_a are the same map while their |q|/2 differ by a factor 4: the')
print('criterion is for primitive r only.')
# The library refuses to *build* rho_{2a}: it tests the scalar 2b(x,r)/b(r,r) for integrality,
# which is half-integral here for x with b(x,a) odd, although the image ... + b(x,a) a is integral.
# That is conservative for non-primitive vectors and is recorded rather than worked around.
try:
    L19.reflection(twice)
    built = True
except ValueError:
    built = False
print('the library builds rho_{2a}: %s  (False is its integrality test on the scalar coefficient,'
      % built)
print('not on the image; rho_a itself is built and measured above, and they are one map)')

print()
print('The arithmetic and the owner agree on every case: a (-2)-root reflection is in the')
print('discriminant kernel, a (-4)-vector reflection is not, and the uniform stabiliser')
print('-1 on H = U + U is, since it acts identically on the negative definite part that')
print('carries the discriminant.  The earlier report that the (-2)-root lay outside the')
print('kernel came from a transposed contragredient in the test file, not from the library.')
