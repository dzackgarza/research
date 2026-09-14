r"""Analysis grading monoids use only the owned mathematical category graph."""

from dzack_research.preamble.categories.group.magmas import AdditiveMonoids, Monoids
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.rings.nonnegative_reals import NonNegativeReals
from dzack_research.preamble.rings.unit_interval import UnitInterval


def test_nonnegative_extended_reals_have_owned_commutative_additive_monoid_placement() -> None:
    assert NonNegativeReals in AdditiveMonoids().AdditiveCommutative()
    assert NonNegativeReals in Sets().Infinite()
    assert NonNegativeReals.monoidal_unit() == NonNegativeReals.zero()

    one = NonNegativeReals(1)
    infinity = ~NonNegativeReals.zero()
    assert (one + one).parent() is NonNegativeReals
    assert infinity.parent() is NonNegativeReals
    assert one + infinity == infinity


def test_unit_interval_has_owned_commutative_monoid_placement() -> None:
    assert UnitInterval in Monoids().Commutative()
    assert UnitInterval in Sets().Infinite()

    half = UnitInterval("1/2")
    assert UnitInterval.one().parent() is UnitInterval
    assert half.parent() is UnitInterval
    assert half * half == UnitInterval.zero()
