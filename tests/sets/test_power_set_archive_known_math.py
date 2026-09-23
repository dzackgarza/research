r"""Archived Cantor and iterated-power-set facts on the live owned set surface."""

from dzack_research.preamble.all import (
    Sets,
    aleph0,
    cardinal,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_power_sets.sage",
    "live_owner": "src/dzack_research/preamble/categories/sets/set_categories.py",
    "disposition": "reconciled-live-owner",
}


def test_cantor_strict_inequality_for_live_finite_countable_and_power_set_specimens() -> None:
    finite = Sets.Δ[2]
    naturals = Sets.Δ[aleph0]
    subsets = naturals.power_set()
    families = subsets.power_set()

    assert families is not subsets
    assert families.base_set() is subsets
    for source in (finite, naturals, subsets):
        assert cardinal(source.cardinality()) < source.power_set().cardinality()


