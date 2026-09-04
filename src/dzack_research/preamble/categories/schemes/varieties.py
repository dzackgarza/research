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

    def an_object(self):
        r"""The affine line over the base ring."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return AffineSpace(1, self.base_ring())

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
    def an_object(self):
        r"""The projective line, of relative dimension one."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return ProjectiveSpace(1, self.base_ring())

    def _repr_object_names(self):
        return f"curves over {self.base_ring()}"

    def super_categories(self):
        return [Varieties(self.base_ring())]

    class ParentMethods:
        def dimension(self):
            return 1


class Surfaces(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The projective plane, of relative dimension two."""
        from dzack_research.preamble.categories.schemes.schemes import AffineSpace, ProjectiveSpace, scheme_product

        return ProjectiveSpace(2, self.base_ring())

    def _repr_object_names(self):
        return f"surfaces over {self.base_ring()}"

    def super_categories(self):
        return [Varieties(self.base_ring())]

    class ParentMethods:
        def dimension(self):
            return 2


__all__ = ["Curves", "Surfaces", "Varieties"]
