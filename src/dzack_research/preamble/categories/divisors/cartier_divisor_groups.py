"""Cartier divisor groups."""

from sage.categories.category import Category

from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.refine import refine


class CartierDivisorGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "Cartier divisor groups"

    def super_categories(self):
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedModules(_own_ring(SageZZ))]


def CartierDivisorGroup(module):
    category = CartierDivisorGroups()
    if module not in category.super_categories()[0]:
        raise TypeError("a Cartier divisor group must carry a specified framing")
    return refine(module, category)
