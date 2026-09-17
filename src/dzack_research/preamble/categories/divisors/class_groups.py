"""Weil divisor class groups."""

from dzack_research.preamble.categories.divisors.divisor_groups import _integers, _module_in_role
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.schemes.schemes import Schemes
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category_bases import Category


class ClassGroups(Category):
    r"""Weil divisor class groups \(\operatorname{Cl}(X)\) with a chosen framed presentation.

    An object is a framed \(\mathbb{Z}\)-module presenting the divisor class
    group of one scheme \(X\), its datum.
    """

    def an_object(self):
        r"""The trivial class group of the affine line, presented on no generator."""
        integers = _integers()
        return self(
            integers.free_module(finite_ordered_set(())),
            scheme=Schemes(integers).an_object(),
        )

    @classmethod
    def _repr_object_names(cls):
        return "class groups"

    def super_categories(self):
        return [FramedModules(_integers())]

    def _call_(self, module, scheme):
        assert module in FramedModules(_integers()), (
            "a class group is presented on a framed abelian group"
        )
        return _module_in_role(module, self, class_group_scheme=scheme)

    class ParentMethods:
        def __init__(self, class_group_scheme, **rest) -> None:
            self._class_group_scheme = class_group_scheme
            super().__init__(**rest)

        def class_group_scheme(self):
            r"""The scheme whose divisor classes this group presents."""
            return self._class_group_scheme
