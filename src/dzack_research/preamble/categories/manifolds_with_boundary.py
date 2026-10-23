r"""Manifolds with half-space and quadrant local models."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.manifolds import (
    SmoothManifolds,
    TopologicalManifolds,
)


class _StratifiedManifoldMapMethods:
    def underlying_continuous_map(self):
        pass

    def interior_map(self):
        pass

    def underlying_topological_stratified_map(self):
        pass

    def __mul__(self, other):
        pass


class _StratifiedManifoldMor(CategoricalMor):
    ElementMethods = _StratifiedManifoldMapMethods

    def _element_constructor_(self, map_on_points, stratum_maps):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("a stratified identity requires the same source and target")
        pass


class TopologicalBoundaryMor(_StratifiedManifoldMor):
    r"""Continuous maps preserving the specified boundary stratum."""


class SmoothBoundaryMor(_StratifiedManifoldMor):
    r"""Smooth maps preserving the specified boundary stratum."""


class TopologicalCornerMor(_StratifiedManifoldMor):
    r"""Continuous maps preserving the specified corner-depth strata."""


class SmoothCornerMor(_StratifiedManifoldMor):
    r"""Smooth maps preserving the specified corner-depth strata."""


class TopologicalBoundaryMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = TopologicalBoundaryMor


class SmoothBoundaryMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SmoothBoundaryMor


class TopologicalCornerMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = TopologicalCornerMor


class SmoothCornerMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = SmoothCornerMor


class _InteriorFunctor(Functor):
    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, manifold):
        return manifold.interior()

    def _apply_morphism(self, morphism):
        return morphism.interior_map()


class _UnderlyingTopologicalStrataFunctor(Functor):
    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, manifold):
        return manifold.underlying_topological_stratified_manifold()

    def _apply_morphism(self, morphism):
        return morphism.underlying_topological_stratified_map()


class _StratifiedManifoldMethods:
    def dimension(self):
        pass

    def atlas(self):
        pass

    def interior(self):
        pass

    def interior_inclusion(self):
        pass

    def depth_stratum(self, depth):
        pass


class TopologicalManifoldsWithBoundary(OwnedCategory):
    r"""Manifolds modelled on closed half-spaces, with boundary-preserving maps."""

    _MorCategory = TopologicalBoundaryMorCategoryConstruction

    def super_categories(self):
        return [TopologicalManifoldsWithCorners()]

    @classmethod
    def _repr_object_names(cls):
        return "topological manifolds with boundary"

    def an_object(self):
        pass

    def on(self, space, atlas, boundary_inclusion):
        pass

    @cached_method
    def interior(self):
        return _InteriorFunctor(self, TopologicalManifolds())

    class ParentMethods(_StratifiedManifoldMethods):
        def boundary(self):
            pass


class SmoothManifoldsWithBoundary(OwnedCategory):
    r"""Smooth half-space manifolds with smooth boundary-preserving maps."""

    _MorCategory = SmoothBoundaryMorCategoryConstruction

    def super_categories(self):
        return [SmoothManifoldsWithCorners()]

    @classmethod
    def _repr_object_names(cls):
        return "smooth manifolds with boundary"

    def an_object(self):
        pass

    def on(self, space, atlas, boundary_inclusion):
        pass

    @cached_method
    def interior(self):
        return _InteriorFunctor(self, SmoothManifolds())

    @cached_method
    def forget_smoothness(self):
        return _UnderlyingTopologicalStrataFunctor(self, TopologicalManifoldsWithBoundary())

    class ParentMethods(_StratifiedManifoldMethods):
        def boundary(self):
            pass

        def underlying_topological_stratified_manifold(self):
            pass


class TopologicalManifoldsWithCorners(OwnedCategory):
    r"""Manifolds modelled on orthants, with maps preserving corner depth."""

    _MorCategory = TopologicalCornerMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "topological manifolds with corners"

    def an_object(self):
        pass

    def on(self, space, atlas, depth_strata):
        pass

    @cached_method
    def interior(self):
        return _InteriorFunctor(self, TopologicalManifolds())

    class ParentMethods(_StratifiedManifoldMethods):
        pass


class SmoothManifoldsWithCorners(OwnedCategory):
    r"""Smooth orthant manifolds with smooth maps preserving corner depth."""

    _MorCategory = SmoothCornerMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "smooth manifolds with corners"

    def an_object(self):
        pass

    def on(self, space, atlas, depth_strata):
        pass

    @cached_method
    def interior(self):
        return _InteriorFunctor(self, SmoothManifolds())

    @cached_method
    def forget_smoothness(self):
        return _UnderlyingTopologicalStrataFunctor(self, TopologicalManifoldsWithCorners())

    class ParentMethods(_StratifiedManifoldMethods):
        def underlying_topological_stratified_manifold(self):
            pass
