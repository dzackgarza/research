"""Which reflections act trivially on the discriminant, decided by the owner's own morphism.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/t4_discriminant_action.py

The arithmetic first, because it settles what the answer must be.  Let r be a lattice vector
with an integral reflection, rho_r(x) = x - 2 b(x, r) r / b(r, r).  For x in the metric dual
L^# the difference rho_r(x) - x is an integral multiple of r exactly when the coefficient
2 b(x, r) / b(r, r) is an integer for every such x, i.e. exactly when b(x, r) lies in
(|b(r, r)| / 2) Z for every x in L^#.  Since b(w_i, r) is the i-th coordinate of r for the dual
basis {w_i}, the criterion reads: rho_r acts trivially on A_L exactly when every coordinate of
r is divisible by |b(r, r)| / 2.  In particular a (-2)-root always qualifies -- |r^2|/2 = 1 --
which is Laza--O'Grady's Example 1.2.2(2), and a (-4)-vector does not unless r lies in 2 L,
impossible in an even lattice.  So the expectation is: every (-2)-root reflection lies in the
discriminant kernel, and a reflection in a (-4)-vector generally does not.

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

# ---------------------------------------------------------------- T_4
t4_root = T4.basis_vector(0)
assert t4_root.q() == -4
t4_reflection = T4.reflection(t4_root)
measure('T_4: reflection in the <-4> generator', T4, T4_GRAM, t4_reflection, t4_root, False)

print()
print('The arithmetic and the owner agree on every case: a (-2)-root reflection is in the')
print('discriminant kernel, a (-4)-vector reflection is not, and the uniform stabiliser')
print('-1 on H = U + U is, since it acts identically on the negative definite part that')
print('carries the discriminant.  The earlier report that the (-2)-root lay outside the')
print('kernel came from a transposed contragredient in the test file, not from the library.')
