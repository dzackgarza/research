r"""Selected atlas presentations with boundary and corner local models."""

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
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.manifolds_with_boundary import (
    RealCkManifoldsWithBoundary,
    RealCkManifoldsWithCorners,
    TopologicalManifoldsWithBoundary,
    TopologicalManifoldsWithCorners,
)
from dzack_research.preamble.categories.real_ck_manifolds import _real_ck_degree
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


class _BoundaryAtlasAsCornerFunctor(Functor):
    r"""Retain boundary charts as corner charts with depth at most one."""

    def __init__(self):
        super().__init__(TopologicalBoundaryAtlases(), TopologicalCornerAtlases())

    def _apply_object(self, atlas):
        pass

    def _apply_morphism(self, morphism):
        pass


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

    @cached_method
    def as_corners(self):
        return _BoundaryAtlasAsCornerFunctor()

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


class RealCkStratifiedAtlasMor(CategoricalMor):
    r"""Fixed-degree chart maps preserving selected boundary or corner strata."""

    class ElementMethods:
        def __init__(self, parent, topological_map, chart_maps, stratum_maps):
            Morphism.__init__(self, parent)
            self._topological_map = topological_map
            self._chart_maps = chart_maps
            self._stratum_maps = stratum_maps

        def underlying_topological_stratified_morphism(self):
            return self._topological_map

        def chart_maps(self):
            return self._chart_maps

        def stratum_maps(self):
            return self._stratum_maps

        def real_ck_manifold_morphism(self):
            pass

        def topological_atlas_morphism(self):
            pass

        def __mul__(self, other):
            pass

    def _element_constructor_(self, topological_map, chart_maps, stratum_maps):
        if (
            topological_map.domain() is not self.domain().underlying_topological_stratified_manifold()
            or topological_map.codomain() is not self.codomain().underlying_topological_stratified_manifold()
        ):
            raise ValueError("the topological map must join the selected stratified manifolds")
        return self.element_class(self, topological_map, chart_maps, stratum_maps)

    @object_level
    def identity(self):
        pass


class RealCkStratifiedAtlasMorCategoryConstruction(MorCategoryConstruction):
    FixedCategoryClass = RealCkStratifiedAtlasMor


class _RealCkStratifiedAtlasTopologyFunctor(Functor):
    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, atlas):
        return atlas.underlying_topological_stratified_manifold()

    def _apply_morphism(self, morphism):
        return morphism.underlying_topological_stratified_morphism()


class _RealCkStratifiedAtlasMaximalizationFunctor(Functor):
    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, atlas):
        return atlas.real_ck_manifold()

    def _apply_morphism(self, morphism):
        return morphism.real_ck_manifold_morphism()


class _RealCkStratifiedAtlasForgetDegreeFunctor(Functor):
    def __init__(self, source, target):
        super().__init__(source, target)

    def _apply_object(self, atlas):
        pass

    def _apply_morphism(self, morphism):
        pass


class _RealCkStratifiedAtlasDataMethods(_StratifiedAtlasDataMethods):
    def __init__(self, topological_stratified_manifold, **rest):
        self._topological_stratified_manifold = topological_stratified_manifold
        super().__init__(**rest)

    def underlying_topological_stratified_manifold(self):
        return self._topological_stratified_manifold

    def real_ck_manifold(self):
        pass


class RealCkCornerAtlases(OwnedParameterizedCategory):
    r"""Selected C^k orthant charts over a topological corner manifold."""

    _MorCategory = RealCkStratifiedAtlasMorCategoryConstruction

    @staticmethod
    def __classcall__(cls, degree):
        return Category.__classcall__(cls, _real_ck_degree(degree))

    def degree(self):
        return self.parameter()

    def super_categories(self):
        return [Objects()]

    def _repr_object_names(self):
        return f"real C^{self.degree()} corner atlas presentations"

    def an_object(self):
        pass

    def on(
        self,
        topological_corner_manifold,
        chart_domains,
        chart_domain_inclusions,
        charts,
        overlap_inclusions,
        transition_maps,
    ):
        if topological_corner_manifold not in TopologicalManifoldsWithCorners():
            raise TypeError(f"{topological_corner_manifold} is not a topological corner manifold")
        return _object_of(
            self,
            topological_stratified_manifold=topological_corner_manifold,
            topological_space=topological_corner_manifold.underlying_topological_space(),
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
        return _RealCkStratifiedAtlasTopologyFunctor(self, TopologicalManifoldsWithCorners())

    @cached_method
    def maximalization(self):
        return _RealCkStratifiedAtlasMaximalizationFunctor(
            self, RealCkManifoldsWithCorners(self.degree())
        )

    @cached_method
    def forget_differentiability(self):
        return _RealCkStratifiedAtlasForgetDegreeFunctor(self, TopologicalCornerAtlases())

    @cached_method
    def forget_to(self, degree):
        degree = _real_ck_degree(degree)
        if degree > self.degree():
            raise ValueError(f"C^{self.degree()} can forget only to C^j with j <= {self.degree()}")
        return _RealCkStratifiedAtlasForgetDegreeFunctor(self, RealCkCornerAtlases(degree))

    class ParentMethods(_RealCkStratifiedAtlasDataMethods):
        def depth_strata(self):
            return self.underlying_topological_stratified_manifold().depth_strata()


class RealCkBoundaryAtlases(OwnedParameterizedCategory):
    r"""Selected C^k half-space charts over a topological boundary manifold."""

    _MorCategory = RealCkStratifiedAtlasMorCategoryConstruction

    @staticmethod
    def __classcall__(cls, degree):
        return Category.__classcall__(cls, _real_ck_degree(degree))

    def degree(self):
        return self.parameter()

    def super_categories(self):
        return [RealCkCornerAtlases(self.degree())]

    def _repr_object_names(self):
        return f"real C^{self.degree()} boundary atlas presentations"

    def an_object(self):
        pass

    def on(
        self,
        topological_boundary_manifold,
        chart_domains,
        chart_domain_inclusions,
        charts,
        overlap_inclusions,
        transition_maps,
    ):
        if topological_boundary_manifold not in TopologicalManifoldsWithBoundary():
            raise TypeError(f"{topological_boundary_manifold} is not a topological boundary manifold")
        return _object_of(
            self,
            topological_stratified_manifold=topological_boundary_manifold,
            topological_space=topological_boundary_manifold.underlying_topological_space(),
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
        return _RealCkStratifiedAtlasTopologyFunctor(self, TopologicalManifoldsWithBoundary())

    @cached_method
    def maximalization(self):
        return _RealCkStratifiedAtlasMaximalizationFunctor(
            self, RealCkManifoldsWithBoundary(self.degree())
        )

    @cached_method
    def forget_differentiability(self):
        return _RealCkStratifiedAtlasForgetDegreeFunctor(self, TopologicalBoundaryAtlases())

    @cached_method
    def forget_to(self, degree):
        degree = _real_ck_degree(degree)
        if degree > self.degree():
            raise ValueError(f"C^{self.degree()} can forget only to C^j with j <= {self.degree()}")
        return _RealCkStratifiedAtlasForgetDegreeFunctor(self, RealCkBoundaryAtlases(degree))

    class ParentMethods(_RealCkStratifiedAtlasDataMethods):
        def boundary_inclusion(self):
            return self.underlying_topological_stratified_manifold().boundary_inclusion()
