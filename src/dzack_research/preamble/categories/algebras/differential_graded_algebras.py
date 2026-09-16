r"""Differential graded algebra categories and their morphisms."""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.algebras.derivations import GradedDerivation
from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.graded_commutative_algebras import (
    StrictlyGradedCommutativeAlgebras,
)
from dzack_research.preamble.categories.modules.cochain_complexes import CochainComplexes
from dzack_research.preamble.categories.modules.pure.modules import FramedModules
from dzack_research.preamble.categories.rings.ring_foundation import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets


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

        source = self.domain()
        target = self.codomain()
        ring = source.base_ring()
        assert source in FramedModules(ring) and target in FramedModules(ring), (
            "materializing a differential component as a module morphism requires selected framings on both endpoints"
        )
        labels = source.module_generating_set()
        assert labels.cardinality().is_finite(), (
            "materializing a differential component as a module morphism requires a finite selected source framing"
        )
        return source.module_category().Mor(source, target)(
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
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebras

        ring = self.base_ring()
        return DeRhamAlgebras(ring).an_object()

    @classmethod
    def _repr_object_names(cls):
        return "differential graded algebras"

    def super_categories(self):

        return [GradedAlgebras(self.base_ring()), CochainComplexes(self.base_ring())]

    _HomCategory = None

    def degree_zero_algebra(self):
        r"""Return the functor taking a DGA to its degree-zero algebra."""
        from dzack_research.preamble.categories.functors.de_rham import (
            _degree_zero_dga_functor,
        )

        return _degree_zero_dga_functor(self.base_ring())

    def cohomology_algebra(self):
        r"""Return the graded cohomology-algebra functor ``H^*`` on this category."""
        from dzack_research.preamble.categories.functors.cohomology import (
            _cohomology_algebra_functor,
        )

        return _cohomology_algebra_functor(self.base_ring())

    class ParentMethods:
        def cohomology_algebra(self):
            r"""Return the represented graded cohomology algebra ``H^*(self)``."""
            from dzack_research.preamble.categories.algebras.cohomology_algebras import (
                CohomologyAlgebras,
            )

            return CohomologyAlgebras(self.base_ring())(self)

        def degree_index_set(self):
            r"""Return the grading object as the inherited cochain degree set."""
            return self.grading_monoid()

        def graded_algebra(self):
            return self

        def dga(self):
            return self

        def regular_dg_module(self):
            r"""Read this DGA as its canonical right DG-module over itself."""
            return self

        def right_action(self):
            return lambda module_element, algebra_element: module_element * algebra_element

        def act(self, module_element, algebra_element):
            return module_element * algebra_element

        def is_differential_graded_module(self) -> bool:
            return True

        def _Hom_(self, codomain, category=None):
            dgas = DifferentialGradedAlgebras(self.base_ring())
            if codomain in dgas and (
                category is None or category.is_subcategory(dgas)
            ):
                return dgas.Mor(self, codomain)
            return super()._Hom_(codomain, category=category)

        def differential(self):
            return self._preamble_differential

        def d(self, element):
            return self.differential()(element)

        @cached_method
        def _negative_cochain_zero_module(self):
            r"""The represented zero module used by the inherited cochain complex."""
            return self.base_ring().free_module(finite_ordered_set(()))

        def differential_component(self, degree):
            degree = int(degree)
            if degree < 0:
                source = self._negative_cochain_zero_module()
                if degree == -1:
                    target = self.graded_piece(0)
                else:
                    target = source
                return DifferentialComponentMorphism(
                    source,
                    target,
                    lambda _element: target.zero(),
                )
            source = self.graded_piece(degree)
            target = self.graded_piece(degree + 1)

            def component(element):
                source_element = self.from_graded_piece(degree, element)
                image = self.d(source_element)
                return image.homogeneous_component(degree + 1)

            return DifferentialComponentMorphism(source, target, component)


class StrictlyCommutativeDifferentialGradedAlgebras(OwnedCategoryOverBaseRing):
    r"""Supercommutative DGAs whose odd elements square to zero.

    The supercommutative DGAs themselves are the computed join
    ``DifferentialGradedAlgebras(R).Supercommutative()``.
    """

    def an_object(self):
        r"""That de Rham algebra, strictly graded-commutative."""
        from dzack_research.preamble.categories.algebras.de_rham_algebras import DeRhamAlgebras

        ring = self.base_ring()
        return DeRhamAlgebras(ring).an_object()

    @classmethod
    def _repr_object_names(cls):
        return "strictly commutative differential graded algebras"

    def super_categories(self):
        return [
            DifferentialGradedAlgebras(self.base_ring()).Supercommutative(),
            StrictlyGradedCommutativeAlgebras(self.base_ring()),
        ]


class Differential(GradedDerivation):
    r"""A represented degree-one square-zero graded derivation."""

    def __init__(self, algebra, function) -> None:
        GradedDerivation.__init__(
            self,
            algebra.graded_derivations(algebra, shift=1),
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
            if generator != source.zero():
                try:
                    generator_degree = source.homogeneous_degree(generator)
                except (ValueError, NotImplementedError) as error:
                    raise ValueError(
                        "a selected DGA generator must be homogeneous"
                    ) from error
                if image != target.zero():
                    try:
                        image_degree = target.homogeneous_degree(image)
                    except (ValueError, NotImplementedError) as error:
                        raise ValueError(
                            "a DGA morphism must preserve homogeneous degree"
                        ) from error
                    if image_degree != generator_degree:
                        raise ValueError(
                            "a DGA morphism must preserve homogeneous degree"
                        )
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
            source = self.domain()._negative_cochain_zero_module()
            target = self.codomain()._negative_cochain_zero_module()
            return DegreewiseLinearMorphism(
                source,
                target,
                lambda _element: target.zero(),
            )
        source = self.domain().graded_piece(degree)
        target = self.codomain().graded_piece(degree)

        def image(element):
            source_element = self.domain().from_graded_piece(degree, element)
            return self(source_element).homogeneous_component(degree)

        return DegreewiseLinearMorphism(source, target, image)

    def __mul__(self, other):
        if not isinstance(other, DGAMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        source = other.domain()
        return DifferentialGradedAlgebras(source.base_ring()).Mor(source, self.codomain())(
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


__all__ = [
    "DGAHomset",
    "DGAHomCategoryConstruction",
    "DGAMorphism",
    "DegreewiseLinearMorphism",
    "Differential",
    "DifferentialComponentMorphism",
    "DifferentialGradedAlgebras",
    "StrictlyCommutativeDifferentialGradedAlgebras",
]
