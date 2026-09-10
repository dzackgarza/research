r"""Formed tensor/direct-sum arithmetic retained from the archived lattice suite.

The specimens use non-unimodular root lattices so determinant formulas are not
vacuous.  They assert the actual bilinear form on pure tensors and its
compatibility with orthogonal direct sums, rather than only comparing ranks.
"""

from dzack_research.preamble.all import Lattices


def test_orthogonal_sum_multiplies_nonunimodular_determinants() -> None:
    left = Lattices.A1
    right = Lattices.A2
    summed = left + right

    assert left.gram_matrix().determinant() == -2
    assert right.gram_matrix().determinant() == 3
    assert summed.gram_matrix().determinant() == -6


def test_lattice_tensor_has_product_rank_form_and_determinant() -> None:
    left = Lattices.A1
    right = Lattices.A2
    tensor = left @ right

    assert tensor.module_rank() == 2
    for x1 in left.module_generators():
        for y1 in right.module_generators():
            for x2 in left.module_generators():
                for y2 in right.module_generators():
                    assert tensor.b(
                        tensor.pure_tensor(x1, y1),
                        tensor.pure_tensor(x2, y2),
                    ) == left.b(x1, x2) * right.b(y1, y2)

    assert tensor.gram_matrix().determinant() == (
        left.gram_matrix().determinant() ** int(right.module_rank())
        * right.gram_matrix().determinant() ** int(left.module_rank())
    )
    assert tensor.gram_matrix().determinant() == 12


def test_triple_tensor_form_is_product_of_all_three_pairings() -> None:
    left = Lattices.A1
    middle = Lattices.U
    right = Lattices.A2
    left_middle = left @ middle
    middle_right = middle @ right
    first = left_middle @ right
    second = left @ middle_right

    for x1 in left.module_generators():
        for y1 in middle.module_generators():
            for z1 in right.module_generators():
                for x2 in left.module_generators():
                    for y2 in middle.module_generators():
                        for z2 in right.module_generators():
                            expected = (
                                left.b(x1, x2)
                                * middle.b(y1, y2)
                                * right.b(z1, z2)
                            )
                            assert first.b(
                                first.pure_tensor(
                                    left_middle.pure_tensor(x1, y1), z1
                                ),
                                first.pure_tensor(
                                    left_middle.pure_tensor(x2, y2), z2
                                ),
                            ) == expected
                            assert second.b(
                                second.pure_tensor(
                                    x1, middle_right.pure_tensor(y1, z1)
                                ),
                                second.pure_tensor(
                                    x2, middle_right.pure_tensor(y2, z2)
                                ),
                            ) == expected


def test_tensor_distributes_over_orthogonal_sum_at_the_level_of_forms() -> None:
    left = Lattices.A1
    middle = Lattices.A2
    right = Lattices.U

    distributed_source = (left + middle) @ right
    distributed_target = (left @ right) + (middle @ right)

    assert distributed_source.module_rank() == distributed_target.module_rank() == 6
    assert distributed_source.gram_matrix() == distributed_target.gram_matrix()
