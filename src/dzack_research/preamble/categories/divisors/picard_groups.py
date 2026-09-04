"""Picard groups."""

from sage.categories.category import Category

from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.refine import refine


class PicardGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "Picard groups"

    def super_categories(self):
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedModules(_own_ring(SageZZ))]


def PicardGroup(module):
    category = PicardGroups()
    if module not in category.super_categories()[0]:
        raise TypeError("a Picard group must carry its quotient framing")
    return refine(module, category)
