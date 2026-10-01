"""The invariants that `arithmetic` computes from a Gram tensor agree with the values that the definitions give by hand."""

from fractions import Fraction

import pytest
from latticedb import arithmetic
from latticedb.arithmetic import GramTensor


def gram(rows: list[list[int]]) -> GramTensor:
    return tuple(tuple(Fraction(value) for value in row) for row in rows)


D4 = [[2, -1, 0, 0], [-1, 2, -1, -1], [0, -1, 2, 0], [0, -1, 0, 2]]


@pytest.mark.parametrize(
    ("rows", "expected"),
    [
        # U is unimodular: L^* = L, and M = L is the one lattice.
        ([[0, 1], [1, 0]], 1),
        # A2: the discriminant group has order 3 and a nondegenerate form, so the form vanishes on the trivial subgroup only.
        ([[2, -1], [-1, 2]], 1),
        # <16>: the discriminant group is Z/16 with generator g = e/16 and b(kg, kg) = k^2/16, an integer for k = 4 and k = 8 and not for k = 1, 2.
        ([[16]], 3),
        # <2> + <2>: x = e_1/2 and y = e_2/2 have b(x, x) = b(y, y) = 1/2 and b(x + y, x + y) = 1, so the subgroups are 0 and <x + y>; the lattice M is I_2.
        ([[2, 0], [0, 2]], 2),
        # U(2): x = e/2 and y = f/2 have b(x, x) = b(y, y) = 0, b(x + y, x + y) = 1 and b(x, y) = 1/2: 0 and the three subgroups of order 2.
        ([[0, 2], [2, 0]], 4),
        # A3: the discriminant group is Z/4 with b(g, g) = 3/4, so b(2g, 2g) = 3: 0 and <2g>; the lattice M is I_3.
        ([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], 2),
        # D4: each of the three nonzero classes of D4^*/D4 has b(x, x) = 1 and two distinct ones have b(x, y) = 1/2: D4 and three lattices isometric to I_4.
        (D4, 4),
    ],
)
def test_overlattice_count_is_the_number_of_subgroups_on_which_the_discriminant_form_vanishes(rows: list[list[int]], expected: int) -> None:
    assert arithmetic.overlattice_count(gram(rows)) == expected


def test_overlattice_count_is_not_decided_above_the_subgroup_bound() -> None:
    # The discriminant group of <2>^8 is (Z/2)^8, which has more than `SUBGROUP_BOUND` subgroups.
    assert arithmetic.overlattice_count(gram([[2 if i == j else 0 for j in range(8)] for i in range(8)])) is None
