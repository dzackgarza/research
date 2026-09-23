"""Semirings and rngs, and the ring Mor family.

These categories sit below the cardinal and ordinal semirings, which are
objects of ``OwnedSemirings``, and below ``ring_foundation``, whose rings refine
both.  Keeping them free of ``ring_foundation`` at import time is what lets the
cardinals be constructed while the ring categories are still loading.
"""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups,
    AdditiveMonoids,
    Monoids,
    Semigroups,
)


class RingMorCategoryConstruction(MorCategoryConstruction):
    r"""The owned family ``(A,B) |-> Hom_Ring(A,B)``."""

    def fixed_category_class(self):
        from dzack_research.preamble.categories.rings.ring_foundation import RingMor

        return RingMor


class OwnedSemirings(OwnedCategory):
    """Semirings on the owned operation spine."""

    _MorCategory = RingMorCategoryConstruction

    def an_object(self):
        r"""The integers, which are in particular a semiring."""
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)

    def super_categories(self):
        return [Monoids(), AdditiveMonoids()]


class OwnedRngs(OwnedCategory):
    """Rngs on the owned operation spine."""

    _MorCategory = RingMorCategoryConstruction

    def an_object(self):
        r"""The integers, which happen to be unital."""
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ)

    def super_categories(self):
        return [Semigroups(), AdditiveGroups()]


__all__ = ["OwnedRngs", "OwnedSemirings", "RingMorCategoryConstruction"]
