import pytest

from dzack_research.preamble.all import (
    Modules,
    BasedFreeModule,
    DirectSumDecomposition,
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def test_direct_sum_decomposition_is_structure_on_the_existing_biproduct() -> None:
    left = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    right = BasedFreeModule(ZZ, finite_ordered_set(("y",)))
    direct_sum = Modules(left.base_ring()).biproduct([left, right])
    equipped = DirectSumDecomposition(direct_sum, (left, right))

    assert equipped is direct_sum
    assert equipped.summand(0) is left
    assert equipped.summand(1) is right
    assert equipped.summands().index_set() is equipped.summand_index_set()
    assert equipped.number_of_summands() == 2


def test_direct_sum_decomposition_rejects_post_construction_relabelling() -> None:
    left = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    right = BasedFreeModule(ZZ, finite_ordered_set(("y",)))
    direct_sum = Modules(left.base_ring()).biproduct([left, right])
    labels = finite_ordered_set(("left", "right"))
    family = indexed_family(
        labels,
        lambda label: left if label == "left" else right,
        name="Chosen summands",
    )

    with pytest.raises(ValueError, match="constructor-owned labels"):
        DirectSumDecomposition(direct_sum, family)

    assert direct_sum.summand(0) is left
    assert direct_sum.summand(1) is right


def test_direct_sum_decomposition_rejects_an_unverified_family() -> None:
    left = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    right = BasedFreeModule(ZZ, finite_ordered_set(("y",)))
    unrelated = BasedFreeModule(ZZ, finite_ordered_set(("z", "w")))
    with pytest.raises(ValueError):
        DirectSumDecomposition(unrelated, (left, right))
