"""The 528 isotropic classes of A_{T_Co}, counted at the discriminant form.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-api/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/coble_528_isotropic_classes.py

Library sage-extensions 2a1babbbc530430f1836707d6f2a4e8ad7a458ee on this project's bind.

What is checked.  prop:tco-as-twist of writing/coble/lattices-and-moduli/discriminant-orbits-of-the-
coble-lattice.md states T_Co = <2> + E_10(2) = B(2) with B = <1> + E_10 odd unimodular of signature
(2,9); prop:coble-q-fibers states that the four fibers of Q = beta_B mod 4 on B/2B -- the four
classes of the value of q_{T_Co} -- have sizes 528, 528, 496, 496, so that A_{T_Co} has exactly 528
isotropic classes, 527 of them nonzero.  Both are reproduced here from the lattice itself: B is
assembled from the Cartan matrix of E8 and the hyperbolic plane, the twist is the library's, and the
counts are read off the discriminant quadratic form the library computes for T_Co = B(2).  No Gram
complement, no hand-written Cartan arithmetic, and no separately constructed E8 discriminant form:
the withdrawn 88/87 count came from exactly that, its E8 Cartan matrix having had determinant 12,
so the lattice it counted was not E8.

The sign of E8, stated rather than assumed.  def:enriques-lattice declares E_10 = U + E_8 with E_8
*negative definite*, which is what makes U + E_8 be II_{1,9} of signature (1,9) and what makes B have
signature (2,9).  Written on the positive-definite root lattice E8 of CartanMatrix(['E',8]), the same
lattice is B = <1> + U + E8(-1) and T_Co = <2> + U(2) + E8(-2); the certificate builds it that way
and asserts the signature (2,9) and the two-elementary type (11,11,1) that the chapter states, so
the lattice counted here is the chapter's and not merely a lattice with the same rank.  Reversing
the sign of E8 changes the signature to (10,1) and leaves every count below unchanged, which is
checked at the end: the 528 is a mod-2 count and does not depend on that convention.

The value convention.  q_{T_Co} takes values in (1/2)Z/2Z; the four classes are the fibers of Q mod 4,
so q = 0, 1/2, 1, 3/2 are Q = 0, 1, 2, 3.  Isotropic means q = 0 in Q/2Z, which is the 528 fiber.
"""
from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix

from sage_extensions.all import EvenTwoElementaryLattices, Lattices

E8C = CartanMatrix(['E', 8])          # positive definite
U = matrix(ZZ, [[0, 1], [1, 0]])


def value_class(value):
    """The class of a q-value in (1/2)Z/2Z, named by its lift, which lies in [0, 2)."""
    return str(value.lift()).replace('(', '').replace(')', '')


def counted(lattice, label):
    """Print the value census of q on the discriminant form, and return the isotropic count."""
    D = lattice.discriminant_quadratic_form()
    counts = {}
    for element in D.elements():
        name = value_class(D.q(element))
        counts[name] = counts.get(name, 0) + 1
    print('%s: %d classes, q-fibers %s' % (label, D.cardinality(),
                                           dict(sorted(counts.items()))))
    return D, counts


def gram(lattice):
    n = int(lattice.module_rank())
    return matrix(ZZ, [[lattice.gram_tensor()[i, j] for j in range(n)] for i in range(n)])


B = Lattices(ZZ)([list(row) for row in
                  block_diagonal_matrix(matrix(ZZ, [[1]]), U, -E8C).rows()])
assert abs(B.determinant()) == 1, B.determinant()
assert not B.is_even()
print('B = <1> + U + E8(-1): rank %d, determinant %s, signature %s'
      % (B.module_rank(), B.determinant(), B.signature_pair()))
assert tuple(int(v) for v in B.signature_pair()) == (2, 9), B.signature_pair()

T = B.twist(2)
print('T_Co = B(2): rank %d, determinant %s, signature %s, even %s'
      % (T.module_rank(), T.determinant(), T.signature_pair(), T.is_even()))
assert T.module_rank() == 11
assert abs(T.determinant()) == 2 ** 11
assert tuple(int(v) for v in T.signature_pair()) == (2, 9), T.signature_pair()
assert T.is_even()
assert gram(T) == block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, -2 * E8C), \
    'the twist is not <2> + U(2) + E8(-2)'
print('   Gram: <2> + U(2) + E8(-2)   AGREE with prop:tco-as-twist')
invariants = EvenTwoElementaryLattices(T.base_ring())(T).two_elementary_invariants()
print('   two_elementary_invariants: %s' % (invariants,))
assert tuple(int(value) for value in invariants) == (11, 11, 1), invariants
print('   type (r, a, delta) = (11, 11, 1)   AGREE with the Coble lattice table and open-problems')

D, counts = counted(T, 'A_{T_Co}')
assert D.cardinality() == 2 ** 11
assert sum(counts.values()) == 2 ** 11
EXPECTED_FIBERS = {'0': 528, '1/2': 528, '1': 496, '3/2': 496}
for name in sorted(EXPECTED_FIBERS):
    computed, expected = counts.get(name, 0), EXPECTED_FIBERS[name]
    print('   # {q = %-3s} = %4d   prop:coble-q-fibers says %4d   %s'
          % (name, computed, expected, 'AGREE' if computed == expected else '*** DIFFER'))
    assert computed == expected, (name, computed, expected)

isotropic = int(D.isotropic_elements().cardinality())
assert isotropic == 528
assert isotropic - 1 == 527
print('isotropic classes (q = 0): %d, of which nonzero %d   AGREE' % (isotropic, isotropic - 1))

# The two summands, counted the same way, and the convolution the proposition's proof uses.
_, zeros_e8 = counted(Lattices(ZZ)([list(row) for row in (-2 * E8C).rows()]), 'E8(-2)')
_, zeros_u2 = counted(Lattices(ZZ)([list(row) for row in (2 * U).rows()]), 'U(2)')
n_e8, n_u2 = zeros_e8['0'], zeros_u2['0']
assert (n_e8, sum(zeros_e8.values())) == (136, 256)
assert (n_u2, sum(zeros_u2.values())) == (3, 4)
assert n_u2 * n_e8 + 1 * (256 - n_e8) == 528
print('3*136 + 1*120 = %d   AGREE with the proposition\'s N_0 = 2^9 + 2^4 = %d'
      % (n_u2 * n_e8 + 1 * (256 - n_e8), 2 ** 9 + 2 ** 4))

# The same counts with E8 taken positive definite: the sign convention does not enter the mod-2 count.
T_flipped = Lattices(ZZ)([list(row) for row in
                          block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8C).rows()])
print('with E8 positive definite instead: signature %s (the chapter\'s is (2, 9))'
      % (T_flipped.signature_pair(),))
D_flipped, counts_flipped = counted(T_flipped, 'A of <2> + U(2) + E8(2)')
assert counts_flipped == EXPECTED_FIBERS, counts_flipped
assert int(D_flipped.isotropic_elements().cardinality()) == 528
print('   the same four fibers and the same 528   the count is invariant under that sign')
