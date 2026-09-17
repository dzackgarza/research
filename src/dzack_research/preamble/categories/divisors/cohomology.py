r"""Owned coherent cohomology spaces for represented line bundles."""

from dzack_research.preamble.categories.modules.pure.modules import VectorSpaces
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.sets.set_categories import finite_ordinal_set


class LineBundleCohomologySpaces(OwnedCategoryOverBaseRing):
    r"""Vector spaces represented as \(H^i(X, \mathcal{O}_X(D))\) for one divisor.

    An object is a finite free module over the base field together with the
    scheme \(X\), the divisor \(D\) and the degree \(i\) it represents.  The
    free-module level consumes the framing; this level adds \(X\), \(D\) and
    \(i\).
    """

    @classmethod
    def _repr_object_names(cls):
        return "line-bundle cohomology spaces"

    def super_categories(self):
        return [VectorSpaces(self.base_ring())]

    def _call_(self, scheme, divisor, degree, dimension):
        r"""The represented \(H^{\mathrm{degree}}(X, \mathcal{O}_X(D))\) of the stated dimension."""
        degree = int(degree)
        dimension = int(dimension)
        assert degree >= 0, "cohomological degree is nonnegative"
        assert dimension >= 0, "a cohomology dimension is nonnegative"
        assert scheme.scheme_base_ring() is self.base_ring(), (
            "line-bundle cohomology is placed over this category's base ring"
        )
        return self.base_ring()._fresh_free_module_on(
            finite_ordinal_set(dimension),
            _extra_categories=(self,),
            _extra_construction_data={
                "cohomology_scheme": scheme,
                "cohomology_divisor": divisor,
                "cohomological_degree": degree,
            },
        )

    class ParentMethods:
        def __init__(
            self,
            cohomology_scheme,
            cohomology_divisor,
            cohomological_degree,
            **rest,
        ) -> None:
            self._cohomology_scheme = cohomology_scheme
            self._cohomology_divisor = cohomology_divisor
            self._cohomological_degree = int(cohomological_degree)
            super().__init__(**rest)

        def cohomology_scheme(self):
            r"""The scheme \(X\) of \(H^i(X, \mathcal{O}_X(D))\)."""
            return self._cohomology_scheme

        def cohomology_divisor(self):
            r"""The divisor \(D\) of \(H^i(X, \mathcal{O}_X(D))\)."""
            return self._cohomology_divisor

        def cohomological_degree(self):
            r"""The degree \(i\) of \(H^i(X, \mathcal{O}_X(D))\)."""
            return self._cohomological_degree


__all__ = ["LineBundleCohomologySpaces"]
