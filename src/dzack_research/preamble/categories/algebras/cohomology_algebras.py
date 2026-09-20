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
from sage.misc.cachefunc import cached_function
from sage.structure.element import parent as element_parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
    DGAMorphism,
    DifferentialGradedAlgebras,
)
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    _algebra_on_module,
    _root_algebra_law_decisions,
)
from dzack_research.preamble.categories.algebras.graded_algebras import (
    GradedAlgebras,
    _graded_multiplication_from_components,
)
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
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


class _CohomologyAlgebra:
    r"""The source DGA and scalar ingress of its cohomology algebra.

    The graded module and multiplication are supplied to their owners before
    this level is constructed.  Cycle quotients remain the actual summands.
    """

    def __init__(self, cohomology_construction, **rest) -> None:
        self._cohomology_construction = cohomology_construction
        super().__init__(**rest)

    def cohomology_construction(self):
        return self._cohomology_construction

    def source_dga(self):
        return self.cohomology_construction().source_dga()

    def _element_constructor_(self, value):
        match value:
            case _ if element_parent(value) is self:
                return value
            case dict():
                return super()._element_constructor_(value)
            case _ if value in self.base_ring():
                return self.scalar_multiple(self.base_ring()(value), self.one())
            case _:
                return super()._element_constructor_(value)

    def _repr_(self):
        return f"H^*({self.source_dga()})"


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
        return _cohomology_algebra_from_dga(dga)

    @classmethod
    def _repr_object_names(cls):
        return "cohomology algebras"

    def super_categories(self):
        return [GradedAlgebras(self.base_ring())]

    _HomCategory = CohomologyAlgebraHomCategoryConstruction

    ParentMethods = _CohomologyAlgebra


def CohomologyAlgebraElement(parent, components):
    r"""Read homogeneous cohomology classes in their constructed algebra."""
    return parent.from_components(components)



class CohomologyAlgebraMorphism(Morphism):
    r"""The graded algebra morphism induced on cohomology by a DGA morphism."""

    def __init__(self, parent, dga_morphism) -> None:
        Morphism.__init__(self, parent)
        if not isinstance(dga_morphism, DGAMorphism):
            raise TypeError("a cohomology-algebra morphism is induced by an actual DGA morphism")
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


@cached_function(key=lambda dga: id(dga))
def _cohomology_algebra_from_dga(dga):
    r"""Construct the graded cycle quotient, then its descended product.

    For cycles x,y, Leibniz gives d(xy)=0.  Replacing x by x+d(a)
    changes xy by d(ay); replacing y by y+d(b) changes xy by
    (-1)^deg(x) d(xb).  Thus the product is independent of representatives,
    bilinear, associative and unital.  See Stacks, Tag 061U, Definition 22.3.1.
    """
    ring = dga.base_ring()
    graded = GradedModules(ring)
    pieces = indexed_family(graded.grading_monoid(), dga.cohomology)
    module = graded(pieces, placements=(FramedModules(ring),))

    def component_product(s, x, t, y):
        left_cycle = module.graded_piece(s).cycle_representative(x)
        right_cycle = module.graded_piece(t).cycle_representative(y)
        product = dga.from_component(s, left_cycle) * dga.from_component(t, right_cycle)
        degree = module.combine_degrees(s, t)
        return module.graded_piece(degree).class_of_cycle(product.homogeneous_component(degree))

    multiplication = _graded_multiplication_from_components(module, component_product)
    law_decisions = _root_algebra_law_decisions(dga)
    law_decisions["grading"] = dga.grading_compatibility_decision()
    placements = (CohomologyAlgebras(ring), *(
        target
        for source, target in (
            (DifferentialGradedAlgebras(ring).Supercommutative(), GradedAlgebras(ring).Supercommutative()),
            (DifferentialGradedAlgebras(ring).Supercommutative().Alternating(), GradedAlgebras(ring).Supercommutative().Alternating()),
        )
        if dga in source
    ))
    match dga.is_commutative():
        case True:
            placements = (*placements, Algebras(ring).Commutative())
            law_decisions["commutativity"] = True
        case _:
            pass
    zero_degree = graded.grading_monoid().zero()
    unit = module.from_component(zero_degree, module.graded_piece(zero_degree).class_of_cycle(
        dga.one().homogeneous_component(zero_degree),
    ))
    return _algebra_on_module(
        module, multiplication, placement=placements, unit=unit,
        construction_data={"cohomology_construction": _CohomologyAlgebraConstruction(dga)},
        law_decisions=law_decisions,
    )


__all__ = [
    "CohomologyAlgebraElement",
    "CohomologyAlgebraHomset",
    "CohomologyAlgebraMorphism",
    "CohomologyAlgebras",
]
