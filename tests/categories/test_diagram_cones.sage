r"""Limits and colimits of a discrete diagram of finite sets."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_discrete_diagram_rejects_invalid_finite_object_images() -> None:
    from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
    from dzack_research.preamble.categories.sets.indexed_families import indexed_family

    labels = Sets.Δ[1]
    index = DiscreteCategory(labels)
    diagrams = Cat().Mor(index, Sets())
    valid = diagrams.discrete_diagram(lambda _point: labels)
    assert valid(index.object(labels(0))) is labels
    try:
        diagrams.discrete_diagram(lambda _point: object())
    except ValueError:
        pass
    else:
        raise AssertionError("an object outside Set was admitted to a set-valued diagram")

    different_labels = Sets.Δ[2]
    try:
        diagrams.discrete_diagram(indexed_family(different_labels, lambda _point: labels))
    except ValueError:
        pass
    else:
        raise AssertionError("a discrete diagram admitted an unrelated indexing set")


def test_limit_and_colimit_of_a_discrete_diagram_are_product_and_disjoint_union() -> None:
    r"""For the discrete diagram ``{0 ↦ [1], 1 ↦ [2]}`` (sets of 2 and 3 elements),
    the limit is the product, of cardinality ``2 · 3 = 6``, and the colimit is
    the disjoint union, of cardinality ``2 + 3 = 5``; cones from a point are
    pairs of elements, so there are 6 of them."""
    index = DiscreteCategory(Sets.Δ[1])
    two, three = Sets.Δ[1], Sets.Δ[2]
    diagram = Cat().Mor(index, Sets()).discrete_diagram(lambda position: two if position == 0 else three)

    assert diagram.limit().cardinality() == 6
    assert diagram.colimit().cardinality() == 5
    assert diagram.Cones().Mor(Sets.Δ[0]).cardinality() == 6
