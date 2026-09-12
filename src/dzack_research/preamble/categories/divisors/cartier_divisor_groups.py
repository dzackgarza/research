"""Cartier divisor groups."""

from sage.categories.category import Category

from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.divisors.divisor_groups import _module_in_role
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


class CartierDivisorGroups(Category):
    @classmethod
    def _repr_object_names(cls):
        return "Cartier divisor groups"

    def super_categories(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedModules(_own_ring(SageZZ))]

    class ParentMethods:
        def divisor_scheme(self):
            scheme = getattr(self, "_preamble_divisor_scheme", None)
            if scheme is None:
                raise TypeError("this Cartier-divisor role has no selected scheme")
            return scheme


def CartierDivisorGroup(module, scheme=None):
    category = CartierDivisorGroups()
    if module not in category.super_categories()[0]:
        raise TypeError("a Cartier divisor group must carry a specified framing")
    return _module_in_role(
        module,
        category,
        "a Cartier divisor group requires a represented framed-module presentation",
        construction_data=None if scheme is None else {"divisor_scheme": scheme},
    )
