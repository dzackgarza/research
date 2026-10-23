r"""Selected chart presentations of real manifolds of fixed differentiability degree."""

from sage.categories.category import Category
from sage.categories.morphism import Morphism
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
from dzack_research.preamble.categories.topological_atlases import TopologicalAtlases
from dzack_research.preamble.categories.real_ck_manifolds import RealCkManifolds, _real_ck_degree
from dzack_research.preamble.owned_category import _object_of


class RealCkAtlasMor(CategoricalMor):
    r"""Maps presented by a topological map and compatible chart maps."""

    class ElementMethods:
        def __init__(self, parent, topological_map, chart_maps):
            Morphism.__init__(self, parent)
            self._topological_map = topological_map
            self._chart_maps = chart_maps

        def underlying_topological_morphism(self):
            return self._topological_map

        def chart_maps(self):
            return self._chart_maps

        def real_ck_morphism(self, source, target):
            pass

        def topological_atlas_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, topological_map, chart_maps):
        if (
            topological_map.domain() is not self.domain().underlying_topological_manifold()
            or topological_map.codomain() is not self.codomain().underlying_topological_manifold()
        ):
            raise ValueError("the topological map must join the selected C^k atlas manifolds")
        return self.element_class(self, topological_map, chart_maps)

    @object_level
    def identity(self):
        pass


class RealCkAtlasMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = RealCkAtlasMor


class _AtlasUnderlyingTopologicalManifoldFunctor(Functor):
    def __init__(self, degree):
        super().__init__(RealCkAtlases(degree), TopologicalManifolds())

    def _apply_object(self, atlas):
        return atlas.underlying_topological_manifold()

    def _apply_morphism(self, morphism):
        return morphism.underlying_topological_morphism()


class _AtlasRealCkManifoldFunctor(Functor):
    def __init__(self, degree):
        super().__init__(RealCkAtlases(degree), RealCkManifolds(degree))

    def _apply_object(self, atlas):
        pass

    def _apply_morphism(self, morphism):
        pass


class _AtlasUnderlyingTopologicalAtlasFunctor(Functor):
    def __init__(self, degree):
        super().__init__(RealCkAtlases(degree), TopologicalAtlases())

    def _apply_object(self, atlas):
        return atlas.topological_atlas()

    def _apply_morphism(self, morphism):
        return morphism.topological_atlas_morphism()


class _WeakenAtlasDifferentiabilityFunctor(Functor):
    r"""Forget higher atlas regularity on objects and chartwise maps."""

    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, atlas):
        pass

    def _apply_morphism(self, morphism):
        pass


class RealCkAtlases(OwnedParameterizedCategory):
    r"""Compatible ``C^k`` charts on a selected topological manifold."""

    _MorCategory = RealCkAtlasMorCategoryConstruction

    @staticmethod
    def __classcall__(cls, degree):
        return Category.__classcall__(cls, _real_ck_degree(degree))

    def degree(self):
        return self.parameter()

    def super_categories(self):
        return [Objects()]

    def _repr_object_names(self):
        return f"real C^{self.degree()} atlas presentations"

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
        return _AtlasUnderlyingTopologicalManifoldFunctor(self.degree())

    @cached_method
    def maximalization(self):
        return _AtlasRealCkManifoldFunctor(self.degree())

    @cached_method
    def forget_differentiability(self):
        return _AtlasUnderlyingTopologicalAtlasFunctor(self.degree())

    @cached_method
    def forget_to(self, degree):
        degree = _real_ck_degree(degree)
        if degree > self.degree():
            raise ValueError(f"C^{self.degree()} can forget only to C^j with j <= {self.degree()}")
        return _WeakenAtlasDifferentiabilityFunctor(self, RealCkAtlases(degree))

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

        @cached_method
        def real_ck_manifold(self):
            pass

        def topological_atlas(self):
            pass
