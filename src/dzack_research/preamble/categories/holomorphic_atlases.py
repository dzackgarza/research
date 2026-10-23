r"""Selected holomorphic chart presentations on complex manifolds."""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method
from sage.rings.infinity import Infinity

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.manifolds import ComplexManifolds, TopologicalManifolds
from dzack_research.preamble.categories.real_ck_atlases import RealCkAtlases
from dzack_research.preamble.owned_category import _object_of


class HolomorphicAtlasMor(CategoricalMor):
    r"""Maps with a topological arrow and compatible holomorphic chart maps."""

    class ElementMethods:
        def __init__(self, parent, topological_map, chart_maps):
            Morphism.__init__(self, parent)
            self._topological_map = topological_map
            self._chart_maps = chart_maps

        def underlying_topological_morphism(self):
            return self._topological_map

        def chart_maps(self):
            return self._chart_maps

        def complex_manifold_morphism(self):
            pass

        def real_ck_atlas_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, topological_map, chart_maps):
        pass

    @object_level
    def identity(self):
        pass


class HolomorphicAtlasMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = HolomorphicAtlasMor


class _HolomorphicAtlasTopologyFunctor(Functor):
    def __init__(self):
        super().__init__(HolomorphicAtlases(), TopologicalManifolds())

    def _apply_object(self, atlas):
        return atlas.underlying_topological_manifold()

    def _apply_morphism(self, morphism):
        return morphism.underlying_topological_morphism()


class _HolomorphicAtlasMaximalizationFunctor(Functor):
    def __init__(self):
        super().__init__(HolomorphicAtlases(), ComplexManifolds())

    def _apply_object(self, atlas):
        pass

    def _apply_morphism(self, morphism):
        pass


class _HolomorphicAtlasRealificationFunctor(Functor):
    def __init__(self):
        super().__init__(HolomorphicAtlases(), RealCkAtlases(Infinity))

    def _apply_object(self, atlas):
        return atlas.real_ck_atlas()

    def _apply_morphism(self, morphism):
        return morphism.real_ck_atlas_morphism()


class HolomorphicAtlases(OwnedCategory):
    r"""Compatible holomorphic charts on a selected topological manifold."""

    _MorCategory = HolomorphicAtlasMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "holomorphic atlas presentations"

    def an_object(self):
        pass

    def on(
        self,
        topological_manifold,
        chart_domains,
        chart_domain_inclusions,
        charts,
        overlap_inclusions,
        transition_maps,
    ):
        if topological_manifold not in TopologicalManifolds():
            raise TypeError(f"{topological_manifold} is not a topological manifold")
        return _object_of(
            self,
            topological_manifold=topological_manifold,
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
        return _HolomorphicAtlasTopologyFunctor()

    @cached_method
    def maximalization(self):
        return _HolomorphicAtlasMaximalizationFunctor()

    @cached_method
    def realification(self):
        return _HolomorphicAtlasRealificationFunctor()

    class ParentMethods:
        def __init__(
            self,
            topological_manifold,
            chart_domains,
            chart_domain_inclusions,
            charts,
            overlap_inclusions,
            transition_maps,
            **rest,
        ):
            self._topological_manifold = topological_manifold
            self._chart_domains = chart_domains
            self._chart_domain_inclusions = chart_domain_inclusions
            self._charts = charts
            self._overlap_inclusions = overlap_inclusions
            self._transition_maps = transition_maps
            super().__init__(**rest)

        def underlying_topological_manifold(self):
            return self._topological_manifold

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

        def complex_manifold(self):
            pass

        def real_ck_atlas(self):
            pass
