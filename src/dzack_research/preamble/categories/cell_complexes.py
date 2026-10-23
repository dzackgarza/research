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
        pass

    def __mul__(self, other):
        pass

    def realization_map(self):
        pass

    def cellular_realization_map(self):
        pass


class _ComplexMor(CategoricalMor):
    ElementMethods = _ComplexMapMethods

    def _element_constructor_(self, cell_map):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a complex identity requires the same source and target")
        pass


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
        pass

    def from_attaching_maps(self, cells, attaching_maps):
        pass

    def from_intersection_strata(self, component_inclusions, intersection_strata):
        r"""Select the dual complex of connected component intersections."""
        pass

    def colimit(self, diagram):
        r"""Select a complex colimit with its universal cocone."""
        pass

    def face_gluing_diagram(self, pieces, paired_faces, face_isomorphisms):
        r"""Present the finite face-pairing data as a diagram in this category."""
        pass

    def from_face_gluing_diagram(self, diagram, colimit_cocone):
        r"""Select the quotient complex with every piece-to-quotient arrow."""
        pass

    def surgery(self, region_inclusion, replacement, boundary_isomorphism):
        r"""Select the pushout of a region complement and a boundary-matched replacement."""
        pass

    def boundary_surgery_span(self, region_inclusion, replacement, boundary_isomorphism):
        r"""Select the boundary-matched span of the complement and replacement."""
        pass

    @cached_method
    def realization(self):
        return _ComplexRealizationFunctor(self, TopologicalSpaces())

    class ParentMethods:
        def cells(self, dimension):
            pass

        def face_poset(self):
            pass

        def star(self, cell):
            pass

        def star_inclusion(self, cell):
            pass

        def link(self, cell):
            pass

        def link_inclusion(self, cell):
            pass

        def subdivision(self):
            pass

        def subdivision_comparison(self, subdivision):
            pass

        def face_inclusion(self, face, cell):
            pass

        def face_gluing_diagram(self):
            pass

        def gluing_cocone(self):
            pass

        def piece_inclusion(self, piece):
            pass

        def surgery_span(self):
            pass

        def surgery_cocone(self):
            pass

        def realization(self):
            pass

    class RegularCW(CategoryWithAxiom):
        r"""Cell complexes with embedded closed cells."""

    class PLManifold(CategoryWithAxiom):
        r"""Cell complexes with the required PL sphere and ball links."""

        class ParentMethods:
            def boundary(self):
                pass

            def boundary_inclusion(self):
                pass


class PolytopalComplexes(OwnedCategory):
    r"""Complexes built from placed polytopes and their face maps."""

    _MorCategory = PolytopalComplexMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "polytopal complexes"

    def an_object(self):
        pass

    def from_cells(self, polytopes, face_maps):
        pass

    @cached_method
    def cellular_realization(self):
        return _ComplexRealizationFunctor(self, CellComplexes())

    class ParentMethods:
        def cells(self, dimension):
            pass

        def face_maps(self):
            pass

        def face_poset(self):
            pass

        def face_inclusion(self, face, cell):
            pass

        def cellular_realization(self):
            pass


class SimplicialComplexes(OwnedCategory):
    r"""Complexes of simplices closed under faces, with simplicial maps."""

    _MorCategory = SimplicialComplexMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "simplicial complexes"

    def an_object(self):
        pass

    def from_simplices(self, vertices, simplices):
        pass

    @cached_method
    def cellular_realization(self):
        return _ComplexRealizationFunctor(self, CellComplexes())

    class ParentMethods:
        def simplices(self, dimension):
            pass

        def face_poset(self):
            pass

        def link(self, simplex):
            pass

        def link_inclusion(self, simplex):
            pass

        def star(self, simplex):
            pass

        def star_inclusion(self, simplex):
            pass

        def simplex_inclusion(self, face, simplex):
            pass

        def cellular_realization(self):
            pass


class DeltaComplexes(OwnedCategory):
    r"""Delta-complexes with selected face identifications."""

    _MorCategory = DeltaComplexMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "Delta-complexes"

    def an_object(self):
        pass

    def from_faces(self, simplices, face_maps):
        pass

    @cached_method
    def cellular_realization(self):
        return _ComplexRealizationFunctor(self, CellComplexes())

    class ParentMethods:
        def face_maps(self):
            pass

        def face_poset(self):
            pass

        def cellular_realization(self):
            pass


class SimplicialSets(OwnedCategory):
    r"""Graded simplices with face and degeneracy operators."""

    _MorCategory = SimplicialSetMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "simplicial sets"

    def an_object(self):
        pass

    def from_face_degeneracy_maps(self, simplices, faces, degeneracies):
        pass

    @cached_method
    def realization(self):
        return _ComplexRealizationFunctor(self, TopologicalSpaces())

    class ParentMethods:
        def simplices(self, dimension):
            pass

        def simplex_category(self):
            pass

        def face_map(self, dimension, index):
            pass

        def degeneracy_map(self, dimension, index):
            pass

        def realization(self):
            pass

    class Kan(CategoryWithAxiom):
        r"""Simplicial sets satisfying the horn-filling condition."""
