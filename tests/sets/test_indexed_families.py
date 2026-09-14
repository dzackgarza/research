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


def test_unhashable_labels_with_unknown_equality_do_not_alias_cache_entries() -> None:
    from sage.structure.parent import Parent

    class Label:
        __hash__ = None

        def __eq__(self, other):
            return True if self is other else Unknown

    class LabelSet(Parent):
        def __call__(self, label):
            return label

    indices = LabelSet()
    calls = []
    family = indexed_family(
        indices,
        lambda label: calls.append(label) or object(),
    )
    first = Label()
    second = Label()

    first_value = family.value(first)
    second_value = family.value(second)

    assert first_value is family.value(first)
    assert second_value is family.value(second)
    assert first_value is not second_value
    assert calls == [first, second]
