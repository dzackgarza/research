from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.sets import NN, Sets
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def test_finite_indexed_family_equality_is_extensional() -> None:
    indices = Sets.Δ[2]
    left = indexed_family(indices, lambda index: int(index) ** 2)
    equal = indexed_family(indices, lambda index: int(index) * int(index))
    different = indexed_family(indices, lambda index: int(index))

    assert left == equal
    assert hash(left) == hash(equal)
    assert left != different
    assert left != indexed_family(Sets.Δ[1], lambda index: int(index) ** 2)


def test_infinite_indexed_family_equality_is_three_valued() -> None:
    left = indexed_family(NN, lambda index: index)
    equal_by_formula = indexed_family(NN, lambda index: index)

    assert left == left
    assert (left == equal_by_formula) is Unknown
    assert (left != equal_by_formula) is Unknown
