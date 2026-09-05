"""Weil divisor class groups."""

from sage.categories.category import Category

from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.divisors.divisor_groups import _module_in_role
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


class ClassGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "class groups"

    def super_categories(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedModules(_own_ring(SageZZ))]


def ClassGroup(module):
    category = ClassGroups()
    if module not in category.super_categories()[0]:
        raise TypeError("a class group must carry its quotient framing")
    return _module_in_role(
        module,
        category,
        "a class group requires a represented framed-module presentation",
    )
