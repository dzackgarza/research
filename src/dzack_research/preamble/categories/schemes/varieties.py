"""Owned varieties, curves, and surfaces."""

from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import (
    FiniteTypeSchemes,
    IntegralSchemes,
    Schemes,
    SeparatedSchemes,
)


class Varieties(OwnedCategoryOverBaseRing):
    r"""Integral separated schemes of finite type over the stated base."""

    def _repr_object_names(self):
        return f"varieties over {self.base_ring()}"

    def super_categories(self):
        return [
            Schemes(self.base_ring()),
            IntegralSchemes(self.base_ring()),
            SeparatedSchemes(self.base_ring()),
            FiniteTypeSchemes(self.base_ring()),
        ]


class Curves(OwnedCategoryOverBaseRing):
    def _repr_object_names(self):
        return f"curves over {self.base_ring()}"

    def super_categories(self):
        return [Varieties(self.base_ring())]

    class ParentMethods:
        def dimension(self):
            return 1


class Surfaces(OwnedCategoryOverBaseRing):
    def _repr_object_names(self):
        return f"surfaces over {self.base_ring()}"

    def super_categories(self):
        return [Varieties(self.base_ring())]

    class ParentMethods:
        def dimension(self):
            return 2


__all__ = ["Curves", "Surfaces", "Varieties"]
