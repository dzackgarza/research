from sage.misc.unknown import Unknown

from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.sets import NN, Sets
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def test_finite_indexed_family_equality_is_extensional() -> None:
    indices = Sets.Δ[2]
    left = indexed_family(indices, lambda index: int(index) ** 2)
    equal = indexed_family(indices, lambda index: int(index) * int(index))
    different = indexed_family(indices, lambda index: int(index))

    assert left in Objects()
    assert left not in Sets()
    assert left == equal
    assert hash(left) == hash(equal)
    assert left != different
    assert left != indexed_family(Sets.Δ[1], lambda index: int(index) ** 2)


def test_equal_values_at_distinct_indices_remain_distinct_family_slots() -> None:
    indices = Sets.Δ[1]
    repeated = object()
    family = indexed_family(indices, lambda _index: repeated)

    assert family.cardinality() == 2
    assert family[0] is family[1] is repeated
    assert tuple(family.index_set()) == (0, 1)


def test_finite_indexed_family_display_exposes_indexed_values() -> None:
    indices = Sets.Δ[2]
    family = indexed_family(
        indices,
        lambda index: int(index) ** 2,
        name="Squares",
    )

    assert repr(family) == "Squares: [0 ↦ 0, 1 ↦ 1, 2 ↦ 4]"


def test_infinite_indexed_family_equality_is_three_valued() -> None:
    left = indexed_family(NN, lambda index: index)
    equal_by_formula = indexed_family(NN, lambda index: index)

    assert left == left
    assert (left == equal_by_formula) is Unknown
    assert (left != equal_by_formula) is Unknown
    assert repr(left) == "Indexed family over NN = {0, 1, 2, ...}"


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


def test_large_finite_family_display_is_bounded() -> None:
    indices = Sets.Δ[20]
    family = indexed_family(indices, lambda index: index, name="Identity")

    display = repr(family)
    assert display.startswith("Identity: [0 ↦ 0, 1 ↦ 1")
    assert "..." in display
    assert "21 entries" in display
