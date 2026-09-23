r"""Limits and colimits of a discrete diagram of finite sets."""

from dzack_research.preamble.all import *  # noqa: F401,F403


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
