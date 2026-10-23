r"""Selected presentations of integral-affine atlases on smooth manifolds."""

from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.integral_affine_manifolds import IntegralAffineManifolds
from dzack_research.preamble.categories.manifolds import SmoothManifolds
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom


class IntegralAffineAtlasMor(CategoricalMor):
    r"""Smooth maps with compatible chartwise integral-affine maps."""

    class ElementMethods:
        def underlying_smooth_morphism(self):
            pass

        def chartwise_affine_maps(self):
            pass

        def integral_affine_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, smooth_map, chartwise_affine_maps):
        pass

    @object_level
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("an atlas identity requires the same source and target")
        pass


class IntegralAffineAtlasMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = IntegralAffineAtlasMor


class _AtlasUnderlyingManifoldFunctor(Functor):
    r"""Forget the atlas presentation on objects and maps."""

    def __init__(self):
        super().__init__(IntegralAffineAtlases(), SmoothManifolds())

    def _apply_object(self, atlas):
        return atlas.underlying_smooth_manifold()

    def _apply_morphism(self, morphism):
        return morphism.underlying_smooth_morphism()


class _AtlasMaximalizationFunctor(Functor):
    r"""Pass from a compatible atlas to its selected maximal structure."""

    def __init__(self):
        super().__init__(IntegralAffineAtlases(), IntegralAffineManifolds())

    def _apply_object(self, atlas):
        return atlas.integral_affine_manifold()

    def _apply_morphism(self, morphism):
        return morphism.integral_affine_morphism()


class IntegralAffineAtlases(OwnedCategory):
    r"""Compatible charts into one selected real affine lattice model."""

    _MorCategory = IntegralAffineAtlasMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "integral-affine atlas presentations"

    def an_object(self):
        pass

    def on(self, smooth_manifold, affine_model, chart_domains, affine_charts, transition_maps):
        r"""Select charts and affine transitions on the exact smooth manifold."""
        pass

    @cached_method
    def forget(self):
        return _AtlasUnderlyingManifoldFunctor()

    @cached_method
    def maximalization(self):
        return _AtlasMaximalizationFunctor()

    class ParentMethods:
        def underlying_smooth_manifold(self):
            pass

        def affine_model(self):
            pass

        def chart_domains(self):
            pass

        def chart_domain_inclusion(self, chart):
            r"""Return the selected open inclusion of a chart domain."""
            pass

        def affine_charts(self):
            pass

        def affine_chart(self, chart):
            r"""Return the affine map from its exact open domain to the model."""
            pass

        def transition_maps(self):
            pass

        def overlap_inclusion(self, source_chart, target_chart):
            r"""Return the overlap's inclusion into the source chart domain."""
            pass

        def transition_map(self, source_chart, target_chart):
            r"""Return the integral-affine map on the specified overlap."""
            pass

        def transition_linear_part(self, source_chart, target_chart):
            r"""Return the transition's induced map of the selected lattice."""
            pass

        def maximal_atlas(self):
            pass

        def integral_affine_manifold(self):
            pass

    class Oriented(CategoryWithAxiom):
        r"""Atlases with determinant-one integral linear transitions."""

    class StrictLatticePointAtlas(CategoryWithAxiom):
        r"""Atlases whose transitions preserve selected lattice points."""
