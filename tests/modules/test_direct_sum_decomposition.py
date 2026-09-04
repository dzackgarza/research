import pytest

from dzack_research.preamble.all import (
    Biproduct,
    BasedFreeModule,
    DirectSumDecomposition,
    ZZ,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_direct_sum_decomposition_is_structure_on_the_existing_biproduct() -> None:
    left = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    right = BasedFreeModule(ZZ, finite_ordered_set(("y",)))
    direct_sum = Biproduct(left, right)
    equipped = DirectSumDecomposition(direct_sum, (left, right))

    assert equipped is direct_sum
    assert equipped.summand(0) is left
    assert equipped.summand(1) is right
    assert equipped.summands().index_set() is equipped.summand_index_set()
    assert equipped.number_of_summands() == 2


def test_direct_sum_decomposition_rejects_an_unverified_family() -> None:
    left = BasedFreeModule(ZZ, finite_ordered_set(("x",)))
    right = BasedFreeModule(ZZ, finite_ordered_set(("y",)))
    unrelated = BasedFreeModule(ZZ, finite_ordered_set(("z", "w")))
    with pytest.raises(ValueError):
        DirectSumDecomposition(unrelated, (left, right))
