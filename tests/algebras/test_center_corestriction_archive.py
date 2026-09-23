r"""Archive reconciliation for corestriction of algebra maps to the centre."""

from dzack_research.preamble.all import (
    QQ,
    OwnedRings,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


def test_exterior_algebra_center_is_the_archived_predicate_subring() -> None:
    exterior = QQ.free_module(finite_ordered_set(("e1", "e2"))).exterior_algebra()
    first = exterior.algebra_generator("e1")
    second = exterior.algebra_generator("e2")
    center = exterior.ring_center()

    assert first * second in center
    assert first not in center
    assert center.ambient_ring() is exterior
    assert center.inclusion()(first * second) == first * second
    assert center in OwnedRings().Commutative()


def test_archived_free_algebra_map_corestricts_to_the_exterior_center() -> None:
    exterior = QQ.free_module(finite_ordered_set(("e1", "e2"))).exterior_algebra()
    first = exterior.algebra_generator("e1")
    second = exterior.algebra_generator("e2")
    source = QQ.free_module(finite_ordered_set(("t",))).symmetric_algebra()
    morphism = source.Mor(exterior)({"t": first * second})

    factor = morphism.corestrict_to_center()
    center = exterior.ring_center()
    variable = source.algebra_generator("t")

    assert factor.domain() is source
    assert factor.codomain() is center
    assert factor(variable) == first * second
    assert center.inclusion()(factor(variable)) == morphism(variable)






