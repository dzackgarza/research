r"""Cell, polytopal, simplicial, Delta, and simplicial-set categories."""

from sage.categories.category_with_axiom import all_axioms
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom


for _axiom in ("RegularCW", "PLManifold", "Kan"):
    if _axiom not in all_axioms:
        all_axioms.add(_axiom)


class _ComplexMapMethods:
    def underlying_map(self):
        raise NotImplementedError("the complex-map constructor must retain its map of cells")

    def __mul__(self, other):
        raise NotImplementedError("composition needs the selected maps of cells and their faces")

    def realization_map(self):
        raise NotImplementedError("the complex-map constructor must retain its continuous realization")

    def cellular_realization_map(self):
        raise NotImplementedError("the complex-map constructor must retain its cellular realization")


class _ComplexMor(CategoricalMor):
    ElementMethods = _ComplexMapMethods

    def _element_constructor_(self, cell_map):
        raise NotImplementedError("a complex map needs its cell maps and attaching-map squares")

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a complex identity requires the same source and target")
        raise NotImplementedError("the complex identity needs its face and attaching maps")


class CellComplexMor(_ComplexMor):
    r"""Cellular maps respecting characteristic and attaching maps."""


class PolytopalComplexMor(_ComplexMor):
    r"""Cellular maps respecting selected polytope face placements."""


class SimplicialComplexMor(_ComplexMor):
    r"""Simplicial maps respecting every face inclusion."""


class DeltaComplexMor(_ComplexMor):
    r"""Maps commuting with the face identifications of a Delta-complex."""


class SimplicialSetMor(_ComplexMor):
    r"""Maps commuting with faces and degeneracies in every degree."""


class CellComplexMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = CellComplexMor


class PolytopalComplexMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = PolytopalComplexMor


class SimplicialComplexMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SimplicialComplexMor


class DeltaComplexMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = DeltaComplexMor


class SimplicialSetMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SimplicialSetMor


class _ComplexRealizationFunctor(Functor):
    r"""Send a represented complex and map to their selected realizations."""

    def __init__(self, source_category, target_category):
        super().__init__(source_category, target_category)

    def _apply_object(self, complex_):
        if self.codomain() is CellComplexes():
            return complex_.cellular_realization()
        return complex_.realization()

    def _apply_morphism(self, morphism):
        if self.codomain() is CellComplexes():
            return morphism.cellular_realization_map()
        return morphism.realization_map()


class CellComplexes(OwnedCategory):
    r"""CW complexes with selected cells and attaching maps."""

    _MorCategory = CellComplexMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "cell complexes"

    def an_object(self):
        raise NotImplementedError("a cell complex needs its cells and attaching maps")

    def from_attaching_maps(self, cells, attaching_maps):
        raise NotImplementedError("constructing a cell complex needs characteristic maps and skeleta")

    @cached_method
    def realization(self):
        return _ComplexRealizationFunctor(self, TopologicalSpaces())

    class ParentMethods:
        def cells(self, dimension):
            raise NotImplementedError("the constructor must retain the cells and their dimensions")

        def face_poset(self):
            raise NotImplementedError("the constructor must retain face incidence")

        def star(self, cell):
            raise NotImplementedError("the star needs its selected cell inclusions")

        def link(self, cell):
            raise NotImplementedError("the link needs its selected cell inclusions")

        def subdivision(self):
            raise NotImplementedError("a subdivision needs its realization comparison map")

        def realization(self):
            raise NotImplementedError("the constructor must retain characteristic maps")

    class RegularCW(CategoryWithAxiom):
        r"""Cell complexes with embedded closed cells."""

    class PLManifold(CategoryWithAxiom):
        r"""Cell complexes with the required PL sphere and ball links."""


class PolytopalComplexes(OwnedCategory):
    r"""Complexes built from placed polytopes and their face maps."""

    _MorCategory = PolytopalComplexMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "polytopal complexes"

    def an_object(self):
        raise NotImplementedError("a polytopal complex needs its placed cells and face maps")

    def from_cells(self, polytopes, face_maps):
        raise NotImplementedError("constructing a polytopal complex needs its face diagram")

    @cached_method
    def cellular_realization(self):
        return _ComplexRealizationFunctor(self, CellComplexes())

    class ParentMethods:
        def cells(self, dimension):
            raise NotImplementedError("the constructor must retain the placed polytope cells")

        def face_maps(self):
            raise NotImplementedError("the constructor must retain the selected face arrows")

        def cellular_realization(self):
            raise NotImplementedError("the polytopal diagram must determine its cell complex")


class SimplicialComplexes(OwnedCategory):
    r"""Complexes of simplices closed under faces, with simplicial maps."""

    _MorCategory = SimplicialComplexMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "simplicial complexes"

    def an_object(self):
        raise NotImplementedError("a simplicial complex needs a selected simplex family")

    def from_simplices(self, vertices, simplices):
        raise NotImplementedError("constructing a simplicial complex needs its face inclusions")

    @cached_method
    def cellular_realization(self):
        return _ComplexRealizationFunctor(self, CellComplexes())

    class ParentMethods:
        def simplices(self, dimension):
            raise NotImplementedError("the constructor must retain simplices by dimension")

        def link(self, simplex):
            raise NotImplementedError("the link needs its subcomplex inclusion")

        def star(self, simplex):
            raise NotImplementedError("the star needs its subcomplex inclusion")

        def cellular_realization(self):
            raise NotImplementedError("the simplex gluing must determine its cell complex")


class DeltaComplexes(OwnedCategory):
    r"""Delta-complexes with selected face identifications."""

    _MorCategory = DeltaComplexMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "Delta-complexes"

    def an_object(self):
        raise NotImplementedError("a Delta-complex needs its face identifications")

    def from_faces(self, simplices, face_maps):
        raise NotImplementedError("constructing a Delta-complex needs all face maps")

    @cached_method
    def cellular_realization(self):
        return _ComplexRealizationFunctor(self, CellComplexes())

    class ParentMethods:
        def face_maps(self):
            raise NotImplementedError("the constructor must retain every face identification")

        def cellular_realization(self):
            raise NotImplementedError("the face diagram must determine its cell complex")


class SimplicialSets(OwnedCategory):
    r"""Graded simplices with face and degeneracy operators."""

    _MorCategory = SimplicialSetMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "simplicial sets"

    def an_object(self):
        raise NotImplementedError("a simplicial set needs its face and degeneracy maps")

    def from_face_degeneracy_maps(self, simplices, faces, degeneracies):
        raise NotImplementedError("constructing a simplicial set needs the simplicial identities")

    @cached_method
    def realization(self):
        return _ComplexRealizationFunctor(self, TopologicalSpaces())

    class ParentMethods:
        def simplices(self, dimension):
            raise NotImplementedError("the constructor must retain each graded simplex set")

        def face_map(self, dimension, index):
            raise NotImplementedError("the constructor must retain each face map")

        def degeneracy_map(self, dimension, index):
            raise NotImplementedError("the constructor must retain each degeneracy map")

        def realization(self):
            raise NotImplementedError("the simplex diagram must determine its topological realization")

    class Kan(CategoryWithAxiom):
        r"""Simplicial sets satisfying the horn-filling condition."""
