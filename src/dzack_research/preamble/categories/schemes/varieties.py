"""Owned varieties, curves, and surfaces.

A variety over ``S`` is an integral separated scheme of finite type over
``S``; a curve and a surface are the varieties of relative dimension one and
two.  All three are full subcategories of ``Sch/S``: membership is the
conjunction of the stated hypotheses, each of which the scheme already
answers, so nothing is placed and no property is asserted twice.
"""

from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSpaces,
    ProjectiveSpaces,
    Schemes,
)
from dzack_research.preamble.refine import refine


class Varieties(OwnedCategoryOverBaseRing):
    r"""Integral separated schemes of finite type over the stated base."""

    def an_object(self):
        r"""The affine line over the base ring."""
        return AffineSpaces(self.base_ring())(1)

    def _repr_object_names(self):
        return f"varieties over {self.base_ring()}"

    def super_categories(self):
        return [Schemes(self.base_ring()).Integral().Separated().FiniteType()]

    def __contains__(self, candidate) -> bool:
        r"""Membership is the three hypotheses, each read off the scheme itself."""
        base = self.base_ring()
        return (
            candidate in Schemes(base).Integral()
            and candidate in Schemes(base).Separated()
            and candidate in Schemes(base).FiniteType()
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
        return ProjectiveSpaces(self.base_ring())(1)

    def _repr_object_names(self):
        return f"curves over {self.base_ring()}"

    def from_equation(self, equation, ambient=None):
        r"""Return the integral curve over this base cut out by ``equation``.

        With an explicit ambient scheme this uses its closed-subscheme
        construction and then verifies membership in this curve category.  With
        no ambient, ``equation`` must belong to a represented polynomial
        algebra over this category's base ring; its selected algebra-generator
        labels determine the affine space in which the curve is cut out.

        A reducible or otherwise non-variety one-dimensional subscheme is
        rejected rather than being placed here merely because its dimension is
        one.
        """
        base = self.base_ring()
        match ambient:
            case None:
                source = equation.parent()
                try:
                    source_base = source.base_ring()
                    labels = tuple(source.algebra_generating_set())
                except AttributeError as error:
                    raise TypeError(
                        "Curves(R).from_equation(f) requires f in a represented "
                        "polynomial algebra over R; otherwise supply the ambient "
                        "scheme explicitly"
                    ) from error
                match source_base is base:
                    case False:
                        raise ValueError(
                            f"the equation is over {source_base}, not the curve base {base}"
                        )
                    case True:
                        pass
                ambient = AffineSpaces(base)(
                    len(labels),
                    names=tuple(str(label) for label in labels),
                )
                target = ambient.coordinate_algebra()
                match source is target:
                    case True:
                        ambient_equation = equation
                    case False:
                        images = {
                            label: target.algebra_generator(str(label))
                            for label in labels
                        }
                        ambient_equation = source.Mor(target)(images)(equation)
            case _:
                ambient_base = ambient.scheme_base_ring()
                match ambient_base is base:
                    case False:
                        raise ValueError(
                            f"the ambient scheme is over {ambient_base}, not the curve base {base}"
                        )
                    case True:
                        pass
                ambient_equation = equation

        curve = ambient.closed_subscheme(ambient_equation)
        match curve in self:
            case False:
                raise ValueError(
                    f"the closed subscheme cut out by {equation} in {ambient} "
                    f"is not an integral curve over {base}"
                )
            case True:
                pass
        return refine(curve, self)

    class ParentMethods:
        def arithmetic_genus(self):
            r"""Return the arithmetic genus ``p_a(C)=1-P_C(0)``.

            For a projective curve the Hilbert polynomial is the defining
            projective invariant whose constant term gives ``1-p_a``.  The
            computation therefore belongs to the projective presentation and
            remains distinct from normalization/geometric-genus algorithms.
            """
            base = self.scheme_base_ring()
            assert self in Schemes(base).Projective(), (
                "arithmetic genus here requires a represented projective curve"
            )
            if self in ProjectiveSpaces(base):
                return 0
            defining_ideal = self.defining_ideal_owned()
            polynomial = defining_ideal._engine_ideal().hilbert_polynomial()
            return int(1 - polynomial(0))

        def normalization_data(self):
            data = getattr(self, "_preamble_curve_normalization_data", None)
            if data is None:
                raise ValueError("this projective curve has no selected normalization map")
            return data

        def normalization_morphism(self):
            return self.normalization_data().normalization_morphism()

        def normalization_curve(self):
            return self.normalization_data().normalization_curve()

        def local_delta_contributions(self):
            return self.normalization_data().local_contributions()

        def genus_comparison(self):
            return self.normalization_data().genus_comparison()

        def geometric_genus(self):
            r"""Return geometric genus from a selected normalization, or smoothness.

            A smooth projective integral curve has no normalization defect, so
            its geometric and arithmetic genera agree.  For singular curves
            they need not agree; this method deliberately refuses to route
            those curves through Sage's unchecked generic ``genus()``.  Their
            geometric genus must instead come from an explicitly represented
            normalization/geometric-integrality construction.
            """
            base = self.scheme_base_ring()
            assert self in Schemes(base).Projective(), (
                "geometric genus here requires a represented projective curve"
            )
            normalization = getattr(self, "_preamble_curve_normalization_data", None)
            if normalization is not None:
                return normalization.geometric_genus()
            assert self in Schemes(base).Smooth(), (
                "geometric genus of a singular curve requires selected normalization data, not the arithmetic genus"
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
        return ProjectiveSpaces(self.base_ring())(2)

    def _repr_object_names(self):
        return f"surfaces over {self.base_ring()}"


__all__ = ["Curves", "Surfaces", "Varieties"]
