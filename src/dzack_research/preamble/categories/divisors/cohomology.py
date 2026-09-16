r"""Owned coherent cohomology spaces for represented line bundles."""

from dzack_research.preamble.categories.modules.pure.modules import VectorSpaces
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set


class LineBundleCohomologySpaces(OwnedCategoryOverBaseRing):
    r"""Vector spaces represented as ``H^i(X,L)`` for one selected line bundle."""

    @classmethod
    def _repr_object_names(cls):
        return "line-bundle cohomology spaces"

    def super_categories(self):
        return [VectorSpaces(self.base_ring())]

    def _call_(self, scheme, divisor, degree, dimension):
        r"""Construct one represented ``H^degree(scheme, O(divisor))``."""
        degree = int(degree)
        dimension = int(dimension)
        if degree < 0:
            raise ValueError("cohomological degree is nonnegative")
        if dimension < 0:
            raise ValueError("a cohomology dimension is nonnegative")
        if scheme.scheme_base_ring() is not self.base_ring():
            raise ValueError("line-bundle cohomology is placed over this category's base ring")
        return self.base_ring()._fresh_free_module_on(
            finite_ordinal_set(dimension),
            _extra_categories=(self,),
            _extra_construction_data=(
                ("_preamble_cohomology_scheme", scheme),
                ("_preamble_cohomology_divisor", divisor),
                ("_preamble_cohomological_degree", degree),
            ),
        )

    class ParentMethods:
        def cohomology_scheme(self):
            return self._preamble_cohomology_scheme

        def cohomology_divisor(self):
            return self._preamble_cohomology_divisor

        def cohomological_degree(self):
            return self._preamble_cohomological_degree


__all__ = ["LineBundleCohomologySpaces"]
