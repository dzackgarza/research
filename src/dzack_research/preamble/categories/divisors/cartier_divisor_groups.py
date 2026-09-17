"""Cartier divisor groups."""

from dzack_research.preamble.categories.divisors.divisor_groups import _integers, _module_in_role
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.schemes.schemes import Schemes
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.owned_category_bases import Category


class CartierDivisorGroups(Category):
    r"""Cartier divisor groups \(\operatorname{CDiv}(X)\) with a chosen framed presentation.

    An object is a framed \(\mathbb{Z}\)-module presenting Cartier divisors
    of one scheme \(X\), its datum.
    """

    def an_object(self):
        r"""The Cartier divisors of the affine line framed by one divisor."""
        integers = _integers()
        return self(
            integers.free_module(finite_ordered_set(("D",))),
            scheme=Schemes(integers).an_object(),
        )

    @classmethod
    def _repr_object_names(cls):
        return "Cartier divisor groups"

    def super_categories(self):
        return [FramedModules(_integers())]

    def _call_(self, module, scheme):
        assert module in FramedModules(_integers()), (
            "a Cartier divisor group is presented on a framed abelian group"
        )
        return _module_in_role(module, self, divisor_scheme=scheme)

    class ParentMethods:
        def __init__(self, divisor_scheme, **rest) -> None:
            self._divisor_scheme = divisor_scheme
            super().__init__(**rest)

        def divisor_scheme(self):
            r"""The scheme whose Cartier divisors this group presents."""
            return self._divisor_scheme
