r"""Differential graded algebra categories and their morphisms."""

from sage.categories.morphism import Morphism
from dzack_research.preamble.categories.sets.set_categories import Sets

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.derivations import (
    GradedDerivation,
    GradedDerivations,
)
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.graded_commutative_algebras import (
    GradedCommutativeAlgebras,
    StrictlyGradedCommutativeAlgebras,
)
from dzack_research.preamble.categories.modules.cochain_complexes import CochainComplexes
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset
from dzack_research.preamble.categories.modules.pure.modules import FramedModules


class DegreewiseLinearMorphism(Morphism):
    r"""An ``R``-linear map between two represented homogeneous pieces.

    This is deliberately independent of a selected finite framing. When the
    source and target pieces admit the finite module-morphism backend,
    :meth:`represented_module_morphism` exposes it and therefore enables the
    usual kernel/image algorithms; otherwise the component remains a genuine
    morphism with exact evaluation but no fabricated finite presentation.
    """

    def __init__(self, domain, codomain, function) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("a differential component requires one base ring")
        self._function = function
        Morphism.__init__(
            self,
            Sets().Mor(domain, codomain),
        )

    def _call_(self, element):
        if element.parent() is not self.domain():
            element = self.domain()(element)
        image = self._function(element)
        return image if image.parent() is self.codomain() else self.codomain()(image)

    def __call__(self, element):
        return self._call_(element)

    def represented_module_morphism(self):
        from sage.rings.integer_ring import ZZ as SageZZ

        source = self.domain()
        target = self.codomain()
        ring = source.base_ring()
        if source not in FramedModules(ring) or target not in FramedModules(ring):
            raise NotImplementedError(
                "this differential component has no selected framed-module backend"
            )
        labels = source.module_generating_set()
        if not labels.cardinality().is_finite():
            raise NotImplementedError(
                "this differential component has no finite framed-module backend"
            )
        return module_homset(source, target)(
            {label: self(source.module_generator(label)) for label in labels}
        )

    def kernel(self):
        return self.represented_module_morphism().kernel()

    def image(self):
        return self.represented_module_morphism().image()


class DifferentialComponentMorphism(DegreewiseLinearMorphism):
    r"""A degreewise component of a represented DGA differential."""


class DifferentialGradedAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""That de Rham algebra, whose differential makes it a DGA."""
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebra

        ring = self.base_ring()
        return DeRhamAlgebra(CommutativeAlgebras(ring).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "differential graded algebras"

    def super_categories(self):

        return [GradedAlgebras(self.base_ring()), CochainComplexes(self.base_ring())]

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a DGA Hom requires two differential graded algebras")
        return dga_homset(domain, codomain)

    _HomCategory = None

    class ParentMethods:
        def _Hom_(self, codomain, category=None):
            dgas = DifferentialGradedAlgebras(self.base_ring())
            if codomain in dgas and (
                category is None or category.is_subcategory(dgas)
            ):
                return dga_homset(self, codomain)
            return super()._Hom_(codomain, category=category)

        def differential(self):
            return self._preamble_differential

        def d(self, element):
            return self.differential()(element)

        def differential_component(self, degree):
            degree = int(degree)
            if degree < 0:
                raise ValueError("a nonnegative DGA has no negative differential component")
            source = self.graded_piece(degree)
            target = self.graded_piece(degree + 1)

            def component(element):
                source_element = self.from_component(degree, element)
                image = self.d(source_element)
                return image.homogeneous_component(degree + 1)

            return DifferentialComponentMorphism(source, target, component)


class CommutativeDifferentialGradedAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""That de Rham algebra, which is graded-commutative."""
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebra

        ring = self.base_ring()
        return DeRhamAlgebra(CommutativeAlgebras(ring).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "commutative differential graded algebras"

    def super_categories(self):

        return [
            DifferentialGradedAlgebras(self.base_ring()),
            GradedCommutativeAlgebras(self.base_ring()),
        ]


class StrictlyCommutativeDifferentialGradedAlgebras(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""That de Rham algebra, strictly graded-commutative."""
        from dzack_research.preamble.categories.algebras.algebras import CommutativeAlgebras
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebra

        ring = self.base_ring()
        return DeRhamAlgebra(CommutativeAlgebras(ring).an_object())

    @classmethod
    def _repr_object_names(cls):
        return "strictly commutative differential graded algebras"

    def super_categories(self):

        return [
            CommutativeDifferentialGradedAlgebras(self.base_ring()),
            StrictlyGradedCommutativeAlgebras(self.base_ring()),
        ]


class Differential(GradedDerivation):
    r"""A represented degree-one square-zero graded derivation."""

    def __init__(self, algebra, function) -> None:
        GradedDerivation.__init__(
            self,
            GradedDerivations(algebra, algebra, shift=1),
            function,
        )
        for label in algebra.algebra_generating_set():
            generator = algebra.algebra_generator(label)
            if self(self(generator)) != algebra.zero():
                raise ValueError("the proposed differential does not square to zero")


class DGAMorphism(Morphism):
    def __init__(self, parent, function) -> None:
        Morphism.__init__(self, parent)
        if not callable(function):
            raise TypeError("a represented DGA morphism is specified by its map on elements")
        self._function = function
        self._check_structured_laws()

    def _check_structured_laws(self) -> None:
        source = self.domain()
        target = self.codomain()
        if self(source.one()) != target.one():
            raise ValueError("a DGA morphism must preserve the unit")
        generators = tuple(
            source.algebra_generator(label) for label in source.algebra_generating_set()
        )
        for generator in generators:
            image = self(generator)
            if (
                generator.is_homogeneous()
                and image != target.zero()
                and (not image.is_homogeneous() or image.degree() != generator.degree())
            ):
                raise ValueError("a DGA morphism must preserve homogeneous degree")
            if self(source.d(generator)) != target.d(image):
                raise ValueError("a DGA morphism must commute with the differential")
        for left in generators:
            for right in generators:
                if self(left * right) != self(left) * self(right):
                    raise ValueError("a DGA morphism must preserve multiplication")

    def _call_(self, element):
        if element.parent() is not self.domain():
            element = self.domain()(element)
        image = self._function(element)
        return image if image.parent() is self.codomain() else self.codomain()(image)

    def __call__(self, element):
        return self._call_(element)

    def component(self, degree):
        r"""Return the degree-``degree`` linear component of this DGA map."""
        degree = int(degree)
        if degree < 0:
            raise ValueError("the represented DGA is nonnegative")
        source = self.domain().graded_piece(degree)
        target = self.codomain().graded_piece(degree)

        def image(element):
            source_element = self.domain().from_component(degree, element)
            return self(source_element).homogeneous_component(degree)

        return DegreewiseLinearMorphism(source, target, image)

    def __mul__(self, other):
        if not isinstance(other, DGAMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        return dga_homset(other.domain(), self.codomain())(
            lambda element: self(other(element))
        )


class DGAHomset(CategoricalHomset):
    Element = DGAMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("DGA morphisms require one common differential base ring")
        CategoricalHomset.__init__(
            self,
            hom_family,
            domain,
            codomain,
        )

    def _element_constructor_(self, function):
        return self.element_class(self, function)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a DGA endomorphism homset")
        return self(lambda element: element)


class DGAHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return DGAHomset


DifferentialGradedAlgebras._HomCategory = DGAHomCategoryConstruction


def dga_homset(domain, codomain):
    ring = domain.base_ring()
    if codomain.base_ring() is not ring:
        raise ValueError("DGA morphisms require one common differential base ring")
    category = DifferentialGradedAlgebras(ring)
    if domain not in category or codomain not in category:
        raise TypeError("DGA Hom endpoints must lie in one differential graded algebra category")
    return category.Mor(domain, codomain)


__all__ = [
    "CommutativeDifferentialGradedAlgebras",
    "DGAHomset",
    "DGAHomCategoryConstruction",
    "DGAMorphism",
    "DegreewiseLinearMorphism",
    "Differential",
    "DifferentialComponentMorphism",
    "DifferentialGradedAlgebras",
    "StrictlyCommutativeDifferentialGradedAlgebras",
    "dga_homset",
]
