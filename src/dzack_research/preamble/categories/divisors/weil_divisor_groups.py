"""Weil divisor groups."""

from sage.categories.category import Category

from dzack_research.preamble.categories.divisors.divisor_groups import DivisorGroups
from dzack_research.preamble.categories.modules.framed.framed_free_modules import FramedFreeModules
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


class WeilDivisorGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "Weil divisor groups"

    def super_categories(self):
        return [DivisorGroups()]


def WeilDivisorGroup(module):
    from sage.rings.integer_ring import ZZ as SageZZ

    if module not in FramedFreeModules(_own_ring(SageZZ)):
        raise TypeError("Weil divisors are free on specified codimension-one subvarieties")
    return refine(module, WeilDivisorGroups())
