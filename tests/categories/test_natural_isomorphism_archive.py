r"""Archive reconciliation for natural isomorphisms as morphisms in ``Cat``."""

from dzack_research.preamble.all import Cat, Sets
from dzack_research.preamble.categories.abstract_categories.functors import (
    DiscreteCategory,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_natural_isomorphism_is_an_actual_isomorphism_in_the_functor_category() -> None:
    index_labels = finite_ordered_set(("stage",))
    index = DiscreteCategory(index_labels)
    points = finite_ordered_set(("left", "right"))
    constant = Cat().Mor(index, Sets()).constant_functor(points)
    swap = Sets().Mor(points, points)(
        lambda point: points("right") if point == points("left") else points("left")
    )

    natural_iso = constant.natural_isomorphism_to(
        constant,
        lambda _stage: swap,
        lambda _stage: swap,
    )
    stage = index("stage")

    assert natural_iso.forward().component(stage) is swap
    assert natural_iso.inverse().component(stage) is swap
    assert natural_iso.domain().arrow().functor() is constant
    assert natural_iso.codomain().arrow().functor() is constant
    assert natural_iso.inverse().component(stage) * natural_iso.forward().component(stage) == Sets().Mor(points, points).identity()
