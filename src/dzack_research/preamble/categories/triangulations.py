r"""Chosen triangulations over an exact cell-complex target."""

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
from dzack_research.preamble.categories.cell_complexes import CellComplexes, SimplicialComplexes
from dzack_research.preamble.categories.functors.core import Functor


class ChosenTriangulationMor(CategoricalMor):
    r"""Simplicial maps commuting with the two realization maps to the target."""

    class ElementMethods:
        def simplicial_map(self):
            raise NotImplementedError("a triangulation map must retain its simplicial arrow")

        def __mul__(self, other):
            raise NotImplementedError("triangulation-map composition needs its commuting triangle")

    def _element_constructor_(self, simplicial_map):
        raise NotImplementedError(
            "a map of chosen triangulations needs a simplicial arrow whose "
            "realization commutes over the exact target"
        )

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a triangulation identity requires the same source and target")
        raise NotImplementedError("the triangulation identity needs its simplicial identity arrow")


class ChosenTriangulationMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = ChosenTriangulationMor


class _TriangulationSourceFunctor(Functor):
    r"""Forget the chosen map to the target, on objects and arrows."""

    def __init__(self, target):
        super().__init__(ChosenTriangulations(target), SimplicialComplexes())

    def _apply_object(self, triangulation):
        return triangulation.simplicial_complex()

    def _apply_morphism(self, morphism):
        return morphism.simplicial_map()


class ChosenTriangulations(OwnedParameterizedCategory):
    r"""Pairs ``(T, |T| -> K)`` for one selected cell complex ``K``."""

    _MorCategory = ChosenTriangulationMorCategoryConstruction

    def parameter_category(self):
        return CellComplexes()

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "chosen triangulations"

    def an_object(self):
        raise NotImplementedError("a chosen triangulation needs a simplicial complex over its target")

    def on(self, simplicial_complex, realization_map):
        r"""Select ``T`` and the exact map ``|T| -> K`` to this category's target."""
        raise NotImplementedError(
            "constructing a chosen triangulation needs simplex inclusions, "
            "coverage, and the realization map to the exact target"
        )

    def target(self):
        return self.parameter()

    @cached_method
    def source(self):
        return _TriangulationSourceFunctor(self.target())

    class ParentMethods:
        def simplicial_complex(self):
            raise NotImplementedError("the constructor must retain the exact simplicial complex")

        def realization_map(self):
            raise NotImplementedError("the constructor must retain the map to the target")

        def simplices(self, dimension):
            raise NotImplementedError("the selected simplicial complex must supply its simplices")

        def simplex_inclusion(self, simplex):
            raise NotImplementedError("the constructor must retain the simplex inclusion")
