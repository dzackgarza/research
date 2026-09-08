"""Owned varieties, curves, and surfaces.

A variety over ``S`` is an integral separated scheme of finite type over
``S``; a curve and a surface are the varieties of relative dimension one and
two.  All three are full subcategories of ``Sch/S``: membership is the
conjunction of the stated hypotheses, each of which the scheme already
answers, so nothing is placed and no property is asserted twice.
"""

from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSpace,
    FiniteTypeSchemes,
    IntegralSchemes,
    ProjectiveSchemes,
    ProjectiveSpace,
    ProjectiveSpaces,
    Schemes,
    SeparatedSchemes,
    SmoothSchemes,
)


class Varieties(OwnedCategoryOverBaseRing):
    r"""Integral separated schemes of finite type over the stated base."""

    def an_object(self):
        r"""The affine line over the base ring."""
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

    def __contains__(self, candidate) -> bool:
        r"""Membership is the three hypotheses, each read off the scheme itself."""
        base = self.base_ring()
        return (
            candidate in IntegralSchemes(base)
            and candidate in SeparatedSchemes(base)
            and candidate in FiniteTypeSchemes(base)
        )


class _DimensionSubcategoryOfVarieties(OwnedCategoryOverBaseRing):
    r"""The varieties over ``S`` of one relative dimension.

    Relative dimension is the invariant that separates a curve from a
    surface, so the two categories differ only in the number they compare
    against and share every other statement.
    """

    relative_dimension = None

    def super_categories(self):
        return [Varieties(self.base_ring())]

    def __contains__(self, candidate) -> bool:
        return (
            candidate in Varieties(self.base_ring())
            and candidate.relative_dimension() == self.relative_dimension
        )


class Curves(_DimensionSubcategoryOfVarieties):
    r"""Varieties of relative dimension one over the stated base."""

    relative_dimension = 1

    def an_object(self):
        r"""The projective line, of relative dimension one."""
        return ProjectiveSpace(1, self.base_ring())

    def _repr_object_names(self):
        return f"curves over {self.base_ring()}"

    class ParentMethods:
        def arithmetic_genus(self):
            r"""Return the arithmetic genus ``p_a(C)=1-P_C(0)``.

            For a projective curve the Hilbert polynomial is the defining
            projective invariant whose constant term gives ``1-p_a``.  The
            computation therefore belongs to the projective presentation and
            remains distinct from normalization/geometric-genus algorithms.
            """
            base = self.scheme_base_ring()
            if self not in ProjectiveSchemes(base):
                raise NotImplementedError(
                    "arithmetic genus here requires a represented projective curve"
                )
            if self in ProjectiveSpaces(base):
                return 0
            defining_ideal = self.defining_ideal_owned()
            polynomial = defining_ideal._engine_ideal().hilbert_polynomial()
            return int(1 - polynomial(0))

        def geometric_genus(self):
            r"""Return geometric genus where smoothness identifies it with ``p_a``.

            A smooth projective integral curve has no normalization defect, so
            its geometric and arithmetic genera agree.  For singular curves
            they need not agree; this method deliberately refuses to route
            those curves through Sage's unchecked generic ``genus()``.  Their
            geometric genus must instead come from an explicitly represented
            normalization/geometric-integrality construction.
            """
            base = self.scheme_base_ring()
            if self not in ProjectiveSchemes(base):
                raise NotImplementedError(
                    "geometric genus here requires a represented projective curve"
                )
            if self not in SmoothSchemes(base):
                raise NotImplementedError(
                    "geometric genus of a singular curve requires its normalization, not the arithmetic genus"
                )
            return self.arithmetic_genus()

        def genus(self):
            r"""Return geometric genus, never arithmetic genus by convention."""
            return self.geometric_genus()


class Surfaces(_DimensionSubcategoryOfVarieties):
    r"""Varieties of relative dimension two over the stated base."""

    relative_dimension = 2

    def an_object(self):
        r"""The projective plane, of relative dimension two."""
        return ProjectiveSpace(2, self.base_ring())

    def _repr_object_names(self):
        return f"surfaces over {self.base_ring()}"


__all__ = ["Curves", "Surfaces", "Varieties"]
