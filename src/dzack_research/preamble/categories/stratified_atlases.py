r"""Selected atlas presentations with boundary and corner local models."""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.mor_foundation import object_level
from dzack_research.preamble.categories.abstract_categories.objects import Objects, OwnedCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.manifolds_with_boundary import (
    TopologicalManifoldsWithBoundary,
    TopologicalManifoldsWithCorners,
)
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.owned_category import _object_of


class StratifiedTopologicalAtlasMor(CategoricalMor):
    r"""Maps of selected atlases preserving their boundary or corner strata."""

    class ElementMethods:
        def __init__(self, parent, continuous_map, chart_maps, stratum_maps):
            Morphism.__init__(self, parent)
            self._continuous_map = continuous_map
            self._chart_maps = chart_maps
            self._stratum_maps = stratum_maps

        def underlying_continuous_morphism(self):
            return self._continuous_map

        def chart_maps(self):
            return self._chart_maps

        def stratum_maps(self):
            return self._stratum_maps

        def topological_manifold_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, continuous_map, chart_maps, stratum_maps):
        if (
            continuous_map.domain() is not self.domain().underlying_topological_space()
            or continuous_map.codomain() is not self.codomain().underlying_topological_space()
        ):
            raise ValueError("the continuous map must join the selected atlas spaces")
        return self.element_class(self, continuous_map, chart_maps, stratum_maps)

    @object_level
    def identity(self):
        pass


class StratifiedTopologicalAtlasMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = StratifiedTopologicalAtlasMor


class _UnderlyingStratifiedAtlasSpaceFunctor(Functor):
    def __init__(self, source):
        super().__init__(source, TopologicalSpaces())

    def _apply_object(self, atlas):
        return atlas.underlying_topological_space()

    def _apply_morphism(self, morphism):
        return morphism.underlying_continuous_morphism()


class _StratifiedAtlasMaximalizationFunctor(Functor):
    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, atlas):
        pass

    def _apply_morphism(self, morphism):
        return morphism.topological_manifold_morphism()


class _StratifiedAtlasDataMethods:
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


class TopologicalBoundaryAtlases(OwnedCategory):
    r"""Half-space charts with a selected boundary inclusion."""

    _MorCategory = StratifiedTopologicalAtlasMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "topological boundary atlas presentations"

    def an_object(self):
        pass

    def on(
        self,
        topological_space,
        boundary_inclusion,
        chart_domains,
        chart_domain_inclusions,
        charts,
        overlap_inclusions,
        transition_maps,
    ):
        if topological_space not in TopologicalSpaces():
            raise TypeError(f"{topological_space} is not a topological space")
        if boundary_inclusion.codomain() is not topological_space:
            raise ValueError("the boundary inclusion must land in the selected space")
        return _object_of(
            self,
            topological_space=topological_space,
            boundary_inclusion=boundary_inclusion,
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
        return _UnderlyingStratifiedAtlasSpaceFunctor(self)

    @cached_method
    def maximalization(self):
        return _StratifiedAtlasMaximalizationFunctor(self, TopologicalManifoldsWithBoundary())

    class ParentMethods(_StratifiedAtlasDataMethods):
        def __init__(self, boundary_inclusion, **rest):
            self._boundary_inclusion = boundary_inclusion
            super().__init__(**rest)

        def boundary_inclusion(self):
            return self._boundary_inclusion

        def topological_manifold(self):
            pass

        def maximal_atlas(self):
            pass


class TopologicalCornerAtlases(OwnedCategory):
    r"""Orthant charts with selected corner-depth strata."""

    _MorCategory = StratifiedTopologicalAtlasMorCategoryConstruction

    def super_categories(self):
        return [Objects()]

    @classmethod
    def _repr_object_names(cls):
        return "topological corner atlas presentations"

    def an_object(self):
        pass

    def on(
        self,
        topological_space,
        depth_strata,
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
            depth_strata=depth_strata,
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
        return _UnderlyingStratifiedAtlasSpaceFunctor(self)

    @cached_method
    def maximalization(self):
        return _StratifiedAtlasMaximalizationFunctor(self, TopologicalManifoldsWithCorners())

    class ParentMethods(_StratifiedAtlasDataMethods):
        def __init__(self, depth_strata, **rest):
            self._depth_strata = depth_strata
            super().__init__(**rest)

        def depth_strata(self):
            return self._depth_strata

        def depth_stratum(self, depth):
            return self._depth_strata[depth]

        def topological_manifold(self):
            pass

        def maximal_atlas(self):
            pass
