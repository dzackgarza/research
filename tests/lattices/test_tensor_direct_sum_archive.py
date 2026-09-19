r"""Formed tensor/direct-sum mathematics retained from the archived lattice suite.

The specimens use non-unimodular root lattices so determinant formulas are not
vacuous.  They assert the actual bilinear form on pure tensors and its
compatibility with orthogonal direct sums, rather than only comparing ranks.
"""

from dzack_research.preamble.all import ZZ, BilinearMap, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_tensor_and_direct_sum.sage",
    "live_owner": "src/dzack_research/preamble/categories/lattices.py",
    "disposition": "reconciled-live-owner",
}


def test_sum_of_a_list_is_the_orthogonal_direct_sum() -> None:
    summed = sum((Lattices.U, Lattices.U, Lattices.E8))
    signature = summed.signature_pair()

    assert summed.module_rank() == 12
    assert signature.first() == 2
    assert signature.second() == 10


def test_orthogonal_sum_has_the_biproduct_inclusion_projection_identities() -> None:
    left = Lattices.A1
    right = Lattices.A2
    summed = left + right

    for source_index, source in enumerate((left, right)):
        for target_index, target in enumerate((left, right)):
            composite = summed.projection(target_index) * summed.injection(source_index)
            if source_index == target_index:
                assert composite == source.module_category().Mor(source, target).identity()
            else:
                assert composite == source.module_category().Mor(source, target).zero()


def test_orthogonal_sum_inclusions_preserve_each_form_and_cross_pairings_vanish() -> None:
    left = Lattices.A1
    right = Lattices.A2
    summed = left + right
    left_inclusion = summed.injection(0)
    right_inclusion = summed.injection(1)

    for x in left.module_generators():
        for y in left.module_generators():
            assert summed.b(left_inclusion(x), left_inclusion(y)) == left.b(x, y)
    for x in right.module_generators():
        for y in right.module_generators():
            assert summed.b(right_inclusion(x), right_inclusion(y)) == right.b(x, y)
    for x in left.module_generators():
        for y in right.module_generators():
            assert summed.b(left_inclusion(x), right_inclusion(y)) == ZZ.zero()


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


def test_tensor_universal_map_is_bilinear_and_factors_uniquely() -> None:
    left = Lattices.U
    right = Lattices.A2
    tensor = left @ right
    universal = tensor.universal_bilinear_map()

    assert universal.left_module() is left
    assert universal.right_module() is right
    assert universal.codomain() is tensor
    x1, x2 = left.module_generators()
    y = right.module_generator(0)
    assert universal(x1 + x2, y) == universal(x1, y) + universal(x2, y)
    assert universal(2 * x1, y) == 2 * universal(x1, y)
    assert universal(x1, 3 * y) == 3 * universal(x1, y)

    negated = BilinearMap(
        left,
        right,
        tensor,
        lambda left_label, right_label: -tensor.pure_tensor(
            left.module_generator(left_label), right.module_generator(right_label)
        ),
    )
    factored = negated
    direct = tensor.module_category().Mor(tensor, tensor)(
        {
            label: -tensor.module_generator(label)
            for label in tensor.module_generating_set()
        }
    )
    assert factored == direct


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
