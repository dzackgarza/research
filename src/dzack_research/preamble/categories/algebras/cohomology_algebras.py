r"""Graded cohomology algebras of represented differential graded algebras.

The cohomology computation is deliberately the common owned cochain-complex
construction: each homogeneous piece is literally ``dga.cohomology(p)``, so
its cycle inclusion, boundary-in-cycles map, quotient projection and selected
representatives remain available to multiplication and induced maps.  Sage's
``CommutativeDifferentialGradedAlgebra`` backend is not a replacement for this
boundary: in its supported field regime ``cocycles`` and ``coboundaries`` are
coordinate vector subspaces and ``cohomology`` is an abstract free module,
which does not retain those comparison maps.  The maintained module backends
used by the cochain-complex owner therefore remain the private computation authority for
both commutative and noncommutative source DGAs.
"""

from sage.categories.morphism import Morphism

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
    DifferentialGradedAlgebras,
    StrictlyCommutativeDifferentialGradedAlgebras,
)
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.graded_commutative_algebras import (
    StrictlyGradedCommutativeAlgebras,
)
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)


class _CohomologyAlgebraConstruction:
    r"""The selected differential graded algebra defining one cohomology algebra."""

    def __init__(self, source_dga) -> None:
        self._source_dga = source_dga

    def source_dga(self):
        return self._source_dga


class CohomologyAlgebraHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return CohomologyAlgebraHomset


class CohomologyAlgebras(OwnedCategoryOverBaseRing):
    r"""Graded algebras ``H^*(B)`` represented from a DGA ``B``."""

    def an_object(self):
        r"""The cohomology of the de Rham algebra of the polynomial algebra."""
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebras

        return self(DeRhamAlgebras(self.base_ring()).an_object())

    def _call_(self, dga):
        r"""Construct ``H^*(dga)`` with its descended graded multiplication.

        The source DGA is the defining datum.  This category constructor owns
        both identity caching and the private graded-direct-sum realization;
        DGA objects and the cohomology-algebra functor both land here through
        this one category-owned construction path.
        """
        dgas = DifferentialGradedAlgebras(self.base_ring())
        if dga not in dgas:
            raise TypeError(
                "a cohomology algebra is constructed from a differential graded algebra over the same base ring"
            )
        cached = _COHOMOLOGY_ALGEBRA_CACHE.get(id(dga))
        if cached is not None and cached.source_dga() is dga:
            return cached
        result = _CohomologyAlgebra(dga)
        _COHOMOLOGY_ALGEBRA_CACHE[id(dga)] = result
        return result

    @classmethod
    def _repr_object_names(cls):
        return "cohomology algebras"

    def super_categories(self):
        return [GradedAlgebras(self.base_ring())]

    _HomCategory = CohomologyAlgebraHomCategoryConstruction

    class ParentMethods:
        def cohomology_construction(self):
            return self._cohomology_construction

        def source_dga(self):
            return self.cohomology_construction().source_dga()


class CohomologyAlgebraElement(GradedDirectSumElement):
    def _mul_(self, other):
        return self.parent().multiply(self, other)


class _CohomologyAlgebra(GradedDirectSumModule):
    Element = CohomologyAlgebraElement

    def __init__(self, dga) -> None:
        self._cohomology_construction = _CohomologyAlgebraConstruction(dga)
        self._preamble_algebra_base_ring = dga.base_ring()
        extra_categories = [CohomologyAlgebras(dga.base_ring())]
        if dga in DifferentialGradedAlgebras(dga.base_ring()).Supercommutative():
            extra_categories.append(GradedAlgebras(dga.base_ring()).Supercommutative())
        if dga in StrictlyCommutativeDifferentialGradedAlgebras(dga.base_ring()):
            extra_categories.append(StrictlyGradedCommutativeAlgebras(dga.base_ring()))
        GradedDirectSumModule.__init__(
            self,
            dga.base_ring(),
            lambda degree: dga.cohomology(degree),
            name=f"H^*({dga})",
            extra_categories=tuple(extra_categories),
        )

    def source_dga(self):
        return self._cohomology_construction.source_dga()

    def algebra_base_ring(self):
        return self.base_ring()

    def multiply(self, left, right):
        left = self(left)
        right = self(right)
        dga = self.source_dga()
        result = self.zero()
        for left_degree, left_class in left.homogeneous_components().items():
            left_piece = self.graded_piece(left_degree)
            left_cycle = left_piece.cycle_representative(left_class)
            left_element = dga.from_component(left_degree, left_cycle)
            for right_degree, right_class in right.homogeneous_components().items():
                right_piece = self.graded_piece(right_degree)
                right_cycle = right_piece.cycle_representative(right_class)
                right_element = dga.from_component(right_degree, right_cycle)
                product = left_element * right_element
                target_degree = left_degree + right_degree
                target_piece = self.graded_piece(target_degree)
                product_class = target_piece.class_of_cycle(
                    product.homogeneous_component(target_degree)
                )
                if product_class != target_piece.zero():
                    result += self.from_component(target_degree, product_class)
        return result

    def one(self):
        dga = self.source_dga()
        degree_zero = self.graded_piece(0)
        unit_class = degree_zero.class_of_cycle(
            dga.one().homogeneous_component(0)
        )
        return self.from_component(0, unit_class)

    def _element_constructor_(self, value):
        if isinstance(value, GradedDirectSumElement):
            return GradedDirectSumModule._element_constructor_(self, value)
        if isinstance(value, dict):
            return self.linear_combination(value)
        try:
            scalar = self.base_ring()(value)
        except (TypeError, ValueError):
            raise TypeError(f"{value!r} does not define a cohomology-algebra element") from None
        return self.scalar_multiple(scalar, self.one())

    def algebra_structure_morphism(self):
        return self.base_ring().Mor(self)(
            lambda scalar: self(scalar),
        )


class CohomologyAlgebraMorphism(Morphism):
    r"""The graded algebra morphism induced on cohomology by a DGA morphism."""

    def __init__(self, parent, dga_morphism) -> None:
        Morphism.__init__(self, parent)
        if dga_morphism.domain() is not self.domain().source_dga():
            raise ValueError("the DGA morphism has the wrong cohomology source")
        if dga_morphism.codomain() is not self.codomain().source_dga():
            raise ValueError("the DGA morphism has the wrong cohomology target")
        self._dga_morphism = dga_morphism

    def underlying_dga_morphism(self):
        return self._dga_morphism

    def _call_(self, element):
        source = self.domain()
        target = self.codomain()
        element = source(element)
        result = target.zero()
        for degree, cohomology_class in element.homogeneous_components().items():
            source_piece = source.graded_piece(degree)
            target_piece = target.graded_piece(degree)
            cycle = source_piece.cycle_representative(cohomology_class)
            image_cycle = self.underlying_dga_morphism().component(degree)(cycle)
            image_class = target_piece.class_of_cycle(image_cycle)
            if image_class != target_piece.zero():
                result += target.from_component(degree, image_class)
        return result

    def __call__(self, element):
        return self._call_(element)

    def __mul__(self, other):
        if not isinstance(other, CohomologyAlgebraMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        return CohomologyAlgebras(source.base_ring()).Mor(source, self.codomain())(
            self.underlying_dga_morphism() * other.underlying_dga_morphism()
        )


class CohomologyAlgebraHomset(CategoricalHomset):
    Element = CohomologyAlgebraMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def _element_constructor_(self, dga_morphism):
        return self.element_class(self, dga_morphism)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a cohomology-algebra endomorphism homset")

        source_dga = self.domain().source_dga()
        return self(
            DifferentialGradedAlgebras(source_dga.base_ring())
            .Mor(source_dga, source_dga)
            .identity()
        )


_COHOMOLOGY_ALGEBRA_CACHE = {}


__all__ = [
    "CohomologyAlgebraElement",
    "CohomologyAlgebraHomset",
    "CohomologyAlgebraMorphism",
    "CohomologyAlgebras",
]
