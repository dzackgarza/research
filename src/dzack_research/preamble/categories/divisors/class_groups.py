"""Weil divisor class groups."""

from sage.categories.category import Category

from dzack_research.preamble.categories.modules import FramedModules
from dzack_research.preamble.refine import refine


class ClassGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "class groups"

    def super_categories(self):
        from dzack_research.preamble.categories.rings import own_ring
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedModules(own_ring(SageZZ))]


def ClassGroup(module):
    category = ClassGroups()
    if module not in category.super_categories()[0]:
        raise TypeError("a class group must carry its quotient framing")
    return refine(module, category)
