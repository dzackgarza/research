r"""Archived Cantor and iterated-power-set facts on the live owned set surface."""

from dzack_research.preamble.all import PowerSet, Sets, aleph0, cardinal


def test_cantor_strict_inequality_for_live_finite_countable_and_power_set_specimens() -> None:
    finite = Sets.Δ[2]
    naturals = Sets.Δ[aleph0]
    subsets = PowerSet(naturals)

    for source in (finite, naturals, subsets):
        assert cardinal(source.cardinality()) < PowerSet(source).cardinality()


def test_iterated_power_set_contains_families_of_subsets() -> None:
    naturals = Sets.Δ[aleph0]
    subsets = PowerSet(naturals)
    families = PowerSet(subsets)
    small_primes = subsets({2, 3, 5, 7})
    small_squares = subsets({1, 4, 9, 16})
    family = families((small_primes, small_squares))

    assert family in families
    assert small_primes in family
    assert small_squares in family
    assert subsets.top() in families.top()
    assert families.cardinality() == cardinal(2) ** subsets.cardinality()
