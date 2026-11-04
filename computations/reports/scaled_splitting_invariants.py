"""The scaled splitting of T_Co = B(2): the invariants of the two presentations agree.

    JULIA_DEPOT_PATH=/root/.julia:/opt/julia-depot: \
    PYTHONPATH=/repo/.scratch/se-provider-c546/src \
    $HOME/.udocker/bin/proot-x86_64 -R $HOME/sage-image/rootfs -b /proc -b /dev -b /sys \
        -b <repo>:/repo -w /repo /sage/.venv/bin/sage \
    /repo/computations/reports/scaled_splitting_invariants.py

Twisting the unimodular splitting B = I_{1,1} + I_{1,8} at a primitive isotropic line gives
T_Co = I_{1,1}(2) + I_{1,8}(2) = U(2) + I_{1,8}(2), and the manuscript writes T_Co = <2> + U(2) + E_8(2).
Both are rank 11, signature (2,9), determinant -2^11; this checks that they also agree in the two-elementary
invariants and in the discriminant quadratic form's cardinality, which is what the identification of the
factors uses.
"""
import sys

from sage.all import CartanMatrix, ZZ, block_diagonal_matrix, matrix

from sage_extensions.all import EvenTwoElementaryLattices, Lattices

sys.stdout.reconfigure(line_buffering=True)

E8 = -CartanMatrix(['E', 8])
U = matrix(ZZ, [[0, 1], [1, 0]])


def lattice(gram):
    return Lattices(ZZ)([list(row) for row in gram.rows()])


# <2> + U(2) + E8(2), the manuscript's presentation.
written = lattice(block_diagonal_matrix(matrix(ZZ, [[2]]), 2 * U, 2 * E8))
# The twist of the unimodular splitting I_{1,1} + I_{0,7} = I_{1,8}:  U(2) + I_{0,7}(2).
# I_{0,7} is diag(-1,..,-1), so I_{0,7}(2) has Gram -2*I_7; the odd hyperbolic plane is diag(1,-1).
odd_hyperbolic = matrix(ZZ, [[1, 0], [0, -1]])
# T_Co = I_{1,1}(2) + I_{1,8}(2), and I_{1,8} = I_{1,1} + I_{0,7}, so the second presentation is
# U(2) + U(2) + I_{0,7}(2):  rank 2 + 2 + 7 = 11.
splitting = lattice(block_diagonal_matrix(2 * odd_hyperbolic, 2 * odd_hyperbolic,
                                          -2 * matrix.identity(ZZ, 7)))

for name, L in (('written: <2> + U(2) + E8(2)', written),
                ('splitting: U(2) + U(2) + I_{0,7}(2)', splitting)):
    invariants = EvenTwoElementaryLattices(L.base_ring())(L).two_elementary_invariants()
    print('%-34s rank %2d  sig %s  det %6s  two_elementary %s  |A| %d'
          % (name, L.module_rank(), tuple(int(x) for x in L.signature_pair()), int(L.determinant()),
             tuple(int(x) for x in invariants), int(L.discriminant_quadratic_form().cardinality())))
    assert L.module_rank() == 11
    assert tuple(int(x) for x in L.signature_pair()) == (2, 9)
    assert int(L.determinant()) == -2 ** 11
    assert tuple(int(x) for x in invariants) == (11, 11, 1)
print()
print('the two presentations agree in rank, signature, determinant, two-elementary type and |A|')
print('(the identification of I_{1,7} with I_{1,1} + I_{0,7} is the book\'s indefinite classification,')
print(' and twisting distributes over the orthogonal sum, so no further check is needed for the split)')
