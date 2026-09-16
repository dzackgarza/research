"""Weil divisor class groups."""

from dzack_research.preamble.categories.divisors.divisor_groups import _divisor_role_specimen, _module_in_role
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.owned_category_bases import Category


class _ClassGroupConstruction:
    r"""The selected scheme defining one represented Weil divisor class group."""

    def __init__(self, scheme) -> None:
        self._scheme = scheme

    def scheme(self):
        return self._scheme


class ClassGroups(Category):
    def an_object(self):
        return _divisor_role_specimen(self)

    @classmethod
    def _repr_object_names(cls):
        return "class groups"

    def super_categories(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        return [FramedModules(_own_ring(SageZZ))]

    def _call_(self, module, scheme=None):
        if module not in self.super_categories()[0]:
            raise TypeError("a class group must carry its quotient framing")
        return _module_in_role(
            module,
            self,
            "a class group requires a represented framed-module presentation",
            construction_data=(
                None
                if scheme is None
                else {"_class_group_construction": _ClassGroupConstruction(scheme)}
            ),
        )

    class ParentMethods:
        def class_group_construction(self):
            construction = getattr(self, "_class_group_construction", None)
            if construction is None:
                raise TypeError("this class-group role has no selected scheme")
            return construction

        def class_group_scheme(self):
            return self.class_group_construction().scheme()
