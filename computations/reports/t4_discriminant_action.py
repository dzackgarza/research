"""What three reflections do to the discriminant modules of T_4 and Lambda_19, measured.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-main/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
        /repo/computations/reports/t4_discriminant_action.py

Why this is measured rather than argued.  A reflection in a vector r of square -4 that pairs
evenly with the lattice is integral, and it is tempting to read divisibility as membership in
the discriminant kernel, and from that the coset of the spinor kernel.  Neither follows.  The
first case below is the one the manuscript's lattice supplies: r the generator of the <-4>
summand of T_4 = <-4> + U^2 + E8^2, whose pairing with every other generator is 0 and with
itself is -4, hence even.  Its reflection is integral -- the library constructs it and refuses
any vector for which 2 b(x, r)/b(r, r) fails to be integral -- and its action on A_{T_4} = Z/4
is measured here through the maintained dual lattice and discriminant projection.

How the action is measured.  With (w_i, e_k) = delta_ik on the dual basis, an isometry g of L
with matrix H on the chosen basis moves w_i to sum_j (H^T)_{ji} w_j when g is an involution
(contragredient in general).  g lies in the discriminant kernel exactly when g(w_i) and w_i
have the same image under L.discriminant_projection(), and that is the test applied below; the
coset is then read off from the class of g(w_0) for w_0 the dual generator of the summand that
carries the discriminant.

The three cases, in the two lattices of the comparison:
  T_4        the generator of the <-4> summand;
  Lambda_19  -1 on the first hyperbolic summand, and the reflection in the sum of the last two
             D_17 simple roots, both of which fix the primitive isotropic plane <e_1, e_2>;
  Lambda_19  a (-2)-root of the D_17 summand, for contrast.
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


def matrix_of(lattice, gram, isometry):
    n = gram.nrows()
    basis = [lattice.basis_vector(i) for i in range(n)]
    P = matrix(ZZ, n, n, lambda k, j: isometry(basis[j]).b(basis[k]))
    H = gram.inverse() * P
    assert all(entry in ZZ for entry in H.list()), 'the isometry is not integral'
    H = matrix(ZZ, H)
    assert H.transpose() * gram * H == gram, 'not an isometry'
    return H


def discriminant_action(lattice, gram, isometry):
    """The action of ``isometry`` on A_L, as (trivial?, where the dual generator goes)."""
    n = gram.nrows()
    H = matrix_of(lattice, gram, isometry)
    involution = H * H == matrix.identity(ZZ, n)
    dual = lattice.dual_lattice()
    projection = lattice.discriminant_projection()
    ring = dual.base_ring()
    generators = tuple(dual.module_generators())

    def image(index):
        assert involution, 'only involutions are measured here'
        column = [int(H[j, index]) for j in range(n)]
        coefficients = {j: ring(column[j]) for j in range(n) if column[j] != 0}
        return projection(dual.linear_combination(coefficients))

    fixed = [image(i) == projection(generators[i]) for i in range(n)]
    return all(fixed), image(0), projection(generators[0])


def report(label, lattice, gram, isometry, expect):
    trivial, moved, original = discriminant_action(lattice, gram, isometry)
    where = 'fixed' if moved == original else 'moved to another class'
    print('%-52s in the kernel: %-5s   class of w_0: %s'
          % (label, trivial, where))
    if expect is not None:
        assert trivial is expect, (label, trivial, expect)
    return trivial


# ---------------------------------------------------------------- T_4
root = T4.basis_vector(0)
pairings = [root.b(T4.basis_vector(i)) for i in range(21)]
print('T_4: r the generator of <-4>, q(r) = %s, pairing with itself %s, with the rest %s'
      % (root.q(), pairings[0], set(pairings[1:])))
print('     divisibility of r in T_4: %s' % gcd(pairings))
t4_reflection = T4.reflection(root)
print('     the reflection exists (the library checks 2 b(x, r)/b(r, r) integrality)')
report('T_4: reflection in the <-4> generator', T4, T4_GRAM, t4_reflection, False)

# ---------------------------------------------------------------- Lambda_19
basis19 = [L19.basis_vector(i) for i in range(21)]
e1, f1, e2 = basis19[0], basis19[1], basis19[2]
minus_first_plane = L19.Aut()(
    lambda label: ((-1 if label in (0, 1) else 1) * L19.module_generator(label))
)
assert minus_first_plane(e1) == -e1 and minus_first_plane(e2) == e2
report('Lambda_19: -1 on the first hyperbolic summand', L19, L19_GRAM,
       minus_first_plane, True)

long_root = basis19[19] + basis19[20]
long_root_reflection = L19.reflection(long_root)
assert long_root.q() == -4 and long_root.b(e1) == 0 and long_root.b(e2) == 0
report('Lambda_19: reflection in the last two D_17 roots', L19, L19_GRAM,
       long_root_reflection, True)

short_root = basis19[4]
short_root_reflection = L19.reflection(short_root)
assert short_root.q() == -2
report('Lambda_19: reflection in the (-2)-root a_1', L19, L19_GRAM,
       short_root_reflection, False)

print()
print('Membership is decided by all n classes; the w_0 column is one sample of the action.')
print('So the (-4)-summand reflection of T_4 is integral and has even divisibility, and it is')
print('not in the discriminant kernel: divisibility does not decide membership, and the coset')
print('has to be measured.  In Lambda_19 the two plane-fixing elements used in the comparison')
print('were measured through the same projection map and do lie in the kernel; the (-2)-root')
print('does not, which is why it was never a witness.')
