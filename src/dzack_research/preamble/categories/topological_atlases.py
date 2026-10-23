r"""Selected chart presentations of finite-dimensional topological manifolds."""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.manifolds import TopologicalManifolds
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.owned_category import _object_of


class TopologicalAtlasMor(CategoricalMor):
    r"""Continuous maps with compatible maps in selected charts."""

    class ElementMethods:
        def __init__(self, parent, continuous_map, chart_maps):
            Morphism.__init__(self, parent)
            self._continuous_map = continuous_map
            self._chart_maps = chart_maps

        def underlying_continuous_morphism(self):
            return self._continuous_map

        def chart_maps(self):
            return self._chart_maps

        def topological_manifold_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, continuous_map, chart_maps):
        if (
            continuous_map.domain() is not self.domain().underlying_topological_space()
            or continuous_map.codomain() is not self.codomain().underlying_topological_space()
        ):
            raise ValueError("the continuous map must join the selected atlas spaces")
        return self.element_class(self, continuous_map, chart_maps)

    @object_level
    def identity(self):
        pass


class TopologicalAtlasMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = TopologicalAtlasMor


class _AtlasUnderlyingSpaceFunctor(Functor):
    def __init__(self):
        super().__init__(TopologicalAtlases(), TopologicalSpaces())

    def _apply_object(self, atlas):
        return atlas.underlying_topological_space()

    def _apply_morphism(self, morphism):
        return morphism.underlying_continuous_morphism()


class _AtlasTopologicalManifoldFunctor(Functor):
    def __init__(self):
        super().__init__(TopologicalAtlases(), TopologicalManifolds())

    def _apply_object(self, atlas):
        pass

    def _apply_morphism(self, morphism):
        pass


class TopologicalAtlases(OwnedCategory):
    r"""Compatible homeomorphic charts on one selected topological space."""

    _MorCategory = TopologicalAtlasMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "topological atlas presentations"

    def an_object(self):
        pass

    def on(
        self,
        topological_space,
        chart_domains,
        chart_domain_inclusions,
        charts,
        overlap_inclusions,
        transition_maps,
    ):
        if topological_space not in TopologicalSpaces():
            raise TypeError(f"{topological_space} is not a topological space")
        return _object_of(
            self,
            topological_space=topological_space,
            chart_domains=chart_domains,
            chart_domain_inclusions=chart_domain_inclusions,
            charts=charts,
            overlap_inclusions=overlap_inclusions,
            transition_maps=transition_maps,
        )

    def refinement(self, finer_atlas, coarser_atlas, chartwise_maps):
        pass

    @cached_method
    def forget(self):
        return _AtlasUnderlyingSpaceFunctor()

    @cached_method
    def maximalization(self):
        return _AtlasTopologicalManifoldFunctor()

    class ParentMethods:
        def __init__(
            self,
            topological_space,
            chart_domains,
            chart_domain_inclusions,
            charts,
            overlap_inclusions,
            transition_maps,
            **rest,
        ):
            self._topological_space = topological_space
            self._chart_domains = chart_domains
            self._chart_domain_inclusions = chart_domain_inclusions
            self._charts = charts
            self._overlap_inclusions = overlap_inclusions
            self._transition_maps = transition_maps
            super().__init__(**rest)

        def underlying_topological_space(self):
            return self._topological_space

        def chart_domains(self):
            return self._chart_domains

        def chart_domain_inclusion(self, chart):
            return self._chart_domain_inclusions[chart]

        def charts(self):
            return self._charts

        def chart(self, chart):
            return self._charts[chart]

        def overlap_inclusion(self, source_chart, target_chart):
            return self._overlap_inclusions[source_chart, target_chart]

        def transition_map(self, source_chart, target_chart):
            return self._transition_maps[source_chart, target_chart]

        def transition_cocycle_holds(self):
            pass

        def restrict(self, open_inclusion):
            pass

        def restriction_morphism(self, restricted_atlas):
            pass

        def maximal_atlas(self):
            pass

        def topological_manifold(self):
            pass
