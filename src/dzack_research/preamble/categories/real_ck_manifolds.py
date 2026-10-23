r"""Real manifolds of one selected differentiability degree."""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.manifolds import TopologicalManifolds
from dzack_research.preamble.categories.rings.ring_foundation import _owned_integers


class RealCkManifoldMor(CategoricalMor):
    r"""Maps with the selected finite differentiability degree."""

    class ElementMethods:
        def underlying_topological_morphism(self):
            raise NotImplementedError("the C^k-map constructor must retain its continuous map")

        def weaken_to(self, degree):
            raise NotImplementedError("the C^k-map constructor must retain chart representations")

        def __mul__(self, other):
            raise NotImplementedError("C^k-map composition needs the chart representations")

    def _element_constructor_(self, chart_maps):
        raise NotImplementedError("a C^k map needs chart representations and overlap agreement")

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a C^k identity requires the same source and target")
        raise NotImplementedError("the C^k identity needs its selected charts")


class RealCkManifoldMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = RealCkManifoldMor


class _WeakenDifferentiabilityFunctor(Functor):
    r"""Retain the exact manifold and maps while forgetting higher regularity."""

    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, manifold):
        if self.codomain() is TopologicalManifolds():
            return manifold.underlying_topological_manifold()
        return manifold.weaken_to(self.codomain().degree())

    def _apply_morphism(self, morphism):
        if self.codomain() is TopologicalManifolds():
            return morphism.underlying_topological_morphism()
        return morphism.weaken_to(self.codomain().degree())


class RealCkManifolds(OwnedParameterizedCategory):
    r"""Real manifolds equipped with a selected compatible ``C^k`` atlas."""

    _MorCategory = RealCkManifoldMorCategoryConstruction

    @staticmethod
    def __classcall__(cls, degree):
        degree = _owned_integers()(degree)
        if degree < 1:
            raise ValueError(f"a finite C^k degree must be positive, but {degree} is not")
        return Category.__classcall__(cls, degree)

    def degree(self):
        return self.parameter()

    def super_categories(self):
        return [Objects()]

    def _repr_object_names(self):
        return f"real C^{self.degree()} manifolds"

    def an_object(self):
        raise NotImplementedError("a C^k manifold needs an atlas on its exact topological manifold")

    def on(self, topological_manifold, atlas):
        r"""Select a compatible ``C^k`` atlas on the exact topological manifold."""
        raise NotImplementedError("construction needs chart domains, transitions, and their cocycle")

    @cached_method
    def forget_to(self, degree):
        degree = _owned_integers()(degree)
        if degree < 1 or degree > self.degree():
            raise ValueError(f"C^{self.degree()} can forget only to C^j with 1 <= j <= {self.degree()}")
        return _WeakenDifferentiabilityFunctor(self, RealCkManifolds(degree))

    @cached_method
    def forget_topology(self):
        return _WeakenDifferentiabilityFunctor(self, TopologicalManifolds())

    class ParentMethods:
        def underlying_topological_manifold(self):
            raise NotImplementedError("the constructor must retain the exact topological manifold")

        def atlas(self):
            raise NotImplementedError("the constructor must retain the selected C^k atlas")

        def weaken_to(self, degree):
            raise NotImplementedError("weakening must retain the same manifold with its C^j atlas")
