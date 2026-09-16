"""Cartier divisor groups."""

from dzack_research.preamble.categories.divisors.divisor_groups import _divisor_role_specimen, _module_in_role
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.owned_category_bases import Category


class _CartierDivisorConstruction:
    r"""The selected scheme defining one represented Cartier-divisor role."""

    def __init__(self, scheme) -> None:
        self._scheme = scheme

    def scheme(self):
        return self._scheme


class CartierDivisorGroups(Category):
    def an_object(self):
        return _divisor_role_specimen(self)

    @classmethod
    def _repr_object_names(cls):
        return "Cartier divisor groups"

    def super_categories(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedModules(_own_ring(SageZZ))]

    def _call_(self, module, scheme=None):
        if module not in self.super_categories()[0]:
            raise TypeError("a Cartier divisor group must carry a specified framing")
        return _module_in_role(
            module,
            self,
            "a Cartier divisor group requires a represented framed-module presentation",
            construction_data=(
                None
                if scheme is None
                else {"_cartier_divisor_construction": _CartierDivisorConstruction(scheme)}
            ),
        )

    class ParentMethods:
        def cartier_divisor_construction(self):
            construction = getattr(self, "_cartier_divisor_construction", None)
            if construction is None:
                raise TypeError("this Cartier-divisor role has no selected scheme")
            return construction

        def divisor_scheme(self):
            return self.cartier_divisor_construction().scheme()
