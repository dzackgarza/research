r"""Distinct semantic category parameters receive distinct deterministic order keys."""

from dzack_research.preamble.categories.group.magmas import (
    AdditiveSemigroups,
    Semigroups,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    RingMorCategoryConstruction,
)


def test_additive_and_multiplicative_mor_families_do_not_collapse_in_c3_ordering() -> None:
    multiplicative = Semigroups().MorCategory()
    additive = AdditiveSemigroups().MorCategory()

    assert multiplicative._cmp_key != additive._cmp_key
    family = RingMorCategoryConstruction(OwnedRings())
    assert family.base_category() is OwnedRings()
    assert multiplicative in family.all_super_categories()
    assert additive in family.all_super_categories()
