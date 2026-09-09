r"""Archived discrete-category and constant-functor semantics."""

from dzack_research.preamble.all import ConstantDiagram, DiscreteCategory, Sets
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def test_discrete_category_has_only_identity_arrows_and_retains_unhashable_labels() -> None:
    labels = finite_ordered_set(([0], [1]))
    category = DiscreteCategory(labels)
    first = category([0])
    second = category([1])

    assert category.object_set() is labels
    assert category([0]) is first
    assert category.objects().value([0]) is first
    assert category.Mor(first, second).cardinality() == cardinal(0)
    assert category.Mor(first, first).cardinality() == cardinal(1)
    identity = category.identity(first)
    assert identity * identity == identity

    equal_labels = finite_ordered_set(([0], [1]))
    assert equal_labels == labels
    assert equal_labels is not labels
    assert DiscreteCategory(equal_labels) is not category
    assert DiscreteCategory(equal_labels).object_set() is equal_labels


def test_constant_diagram_sends_every_index_arrow_to_the_codomain_identity() -> None:
    index = DiscreteCategory(Sets.Δ[1])
    value = finite_ordered_set(("x", "y"))
    diagram = ConstantDiagram(index, Sets(), value)
    first = index(index.object_set()[0])
    identity = index.identity(first)

    assert diagram(first) is value
    carried = diagram(identity)
    assert carried == Sets().Mor(value, value).identity()
    assert carried.domain() is value
    assert carried.codomain() is value
