r"""Metric spaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import TopologicalSpaces
from ..homsets import MetricSpaceHomCategory

if TYPE_CHECKING:
    from ...types import MetricBall, RealNumber, SetElement, SetMorphism


class _MetricSpaceObjectMethods:
    r"""Methods on metric spaces."""

    @override
    @final
    def is_metric(self) -> bool:
        r"""Return ``True`` because this object lies in metric spaces."""
        return True

    @abstract_method
    def metric(self) -> SetMorphism:
        r"""Return the metric map ``d: X x X -> RR``."""
        ...

    @abstract_method
    def ball(self, center: SetElement, radius: RealNumber) -> MetricBall:
        r"""Return the open metric ball with given ``center`` and ``radius``."""
        ...

    @abstract_method
    def dist(self, x: SetElement, y: SetElement) -> RealNumber:
        r"""Return the metric distance between ``x`` and ``y``."""
        ...


class _MetricSpaceElementMethods:
    r"""Methods on points of metric spaces."""

    @final
    def dist(self, other: SetElement) -> RealNumber:
        r"""Return this point's distance to ``other`` in its parent metric space."""
        return self.parent().dist(self, other)


class MetricSpacesCategory(CategoryWithAxiom):
    r"""Category of metric spaces.

    Canonical chain: ``TopologicalSpaces().Metric()``.
    """

    _base_category_class_and_axiom = (TopologicalSpaces, "Metric")
    ParentMethods = _MetricSpaceObjectMethods
    ElementMethods = _MetricSpaceElementMethods
    HomCategory = MetricSpaceHomCategory
    Complete = LazyImport("category_specs.topological_spaces.subcategories.complete", "_CompleteMetricSpaces")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "metric spaces"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return Sage metric spaces and local topological spaces."""
        return [SageSets().Metric(), TopologicalSpaces()]

    class SubcategoryMethods:
        @cached_method
        @final
        def Complete(self) -> Category:
            r"""Return the complete metric-space subcategory."""
            return self._with_axiom("Complete")

    class MorphismMethods: ...
