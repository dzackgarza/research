"""Owned varieties, curves, and surfaces.

A variety over ``S`` is an integral separated scheme of finite type over
``S``; a curve and a surface are the varieties of relative dimension one and
two.  All three are full subcategories of ``Sch/S``: membership is the
conjunction of the stated hypotheses, each of which the scheme already
answers, so nothing is placed and no property is asserted twice.
"""

from dzack_research.preamble.categories.algebras.algebras import FramedAlgebras
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSpaces,
    ProjectiveSpaces,
    Schemes,
    _engine_projective_subscheme,
    _engine_scheme,
    _projective_closed_subscheme,
    _projective_equation_family,
)


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

    def from_equation(self, equation, ambient=None, placements=(), **level_data):
        r"""Return the integral curve over this base cut out by ``equation``.

        With an explicit ambient scheme this uses its closed-subscheme
        construction.  With no ambient, ``equation`` lies in a polynomial
        algebra over this category's base ring with chosen algebra generators;
        their labels determine the affine space in which the curve is cut out.
        A curve constructed with further data -- a chosen normalization --
        states those categories in ``placements``, with their level data.

        The closed subscheme is constructed once, as an object of this
        category.  Its two hypotheses are decided on the data that determine
        them: the ideal of the equation is prime, which makes ``V(f)``
        integral, and the relative dimension is one.  Separatedness and finite
        type come from the ambient.  A reducible or otherwise non-variety
        one-dimensional subscheme is rejected rather than being placed here
        merely because its dimension is one.
        """
        base = self.base_ring()
        match ambient:
            case None:
                source = equation.parent()
                assert source in FramedAlgebras(base), (
                    "Curves(R).from_equation(f) requires f in a polynomial algebra over R with "
                    "chosen algebra generators; otherwise supply the ambient scheme explicitly"
                )
                labels = tuple(source.algebra_generating_set())
                ambient = AffineSpaces(base)(
                    len(labels),
                    names=tuple(str(label) for label in labels),
                )
                target = ambient.coordinate_algebra()
                match source is target:
                    case True:
                        ambient_equation = equation
                    case False:
                        images = {label: target.algebra_generator(str(label)) for label in labels}
                        ambient_equation = source.Mor(target)(images)(equation)
            case _:
                assert ambient.scheme_base_ring() is base, (
                    f"the ambient scheme is over {ambient.scheme_base_ring()}, not the curve base {base}"
                )
                ambient_equation = equation
        assert ambient in Schemes(base).Separated() and ambient in Schemes(base).FiniteType(), (
            f"a curve over {base} is cut out of a separated scheme of finite type over {base}"
        )
        match ambient:
            case _ if ambient in Schemes(base).Affine():
                algebra = ambient.coordinate_algebra()
                ideal = algebra.ideal(ambient_equation)
                assert ideal.is_prime(), "the equation must define an integral curve"
                quotient_data = algebra._quotient_by_algebra_elements((ambient_equation,))
                quotient, _ = quotient_data
                assert quotient.krull_dimension() - base.krull_dimension() == 1, (
                    "the equation must define a curve of relative dimension one"
                )
                return ambient.closed_subscheme(
                    ambient_equation, placements=(self, *placements),
                    _quotient_data=quotient_data, **level_data,
                )
            case _:
                assert ambient in Schemes(base).Projective(), (
                    "the equation entry uses an affine or projective ambient scheme"
                )
                equations = _projective_equation_family((ambient_equation,))
                engine = _engine_projective_subscheme(_engine_scheme(ambient), equations)
                assert engine.defining_ideal().is_prime(), "the equation must define an integral curve"
                assert engine.dimension_relative() == 1, (
                    "the equation must define a curve of relative dimension one"
                )
                return _projective_closed_subscheme(
                    ambient, equations, placements=(self, *placements),
                    _engine=engine, **level_data,
                )

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
