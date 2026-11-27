r"""Metric spaces."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, TypeVar, cast, final, override, TypeAlias

from sage.categories.metric_spaces import MetricSpaces as SageMetricSpaces
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ...sets import _SetElementMethods
from ...utils import with_axiom
from .. import TopologicalSpaces
from ..homsets import MetricSpaceHomCategory

_F = TypeVar("_F", bound=Callable[..., object])

if TYPE_CHECKING:
    from ...types import MetricBall, RealNumber, SetElement, SetMorphism


class _MetricSpaceObjectMethods:
    r"""Methods on metric spaces."""

    @override
    @final
    def is_metric(self) -> bool:
        r"""Return ``True`` because this object lies in metric spaces."""
        return True

    @abstractmethod
    def metric(self) -> SetMorphism:
        r"""Return the metric map ``d: X x X -> RR``."""
        ...

    @abstractmethod
    def ball(self, center: SetElement, radius: RealNumber) -> MetricBall:
        r"""Return the open metric ball with given ``center`` and ``radius``."""
        ...

    @abstractmethod
    def dist(self, x: SetElement, y: SetElement) -> RealNumber:
        r"""Return the metric distance between ``x`` and ``y``."""
        ...


class _MetricSpaceElementMethods(_SetElementMethods):
    r"""Methods on points of metric spaces."""

    @abstractmethod
    def parent(self) -> _MetricSpaceObjectMethods:
        r"""Return the metric space containing this point."""
        ...

    @final
    def dist(self, other: SetElement) -> RealNumber:
        r"""Return this point's distance to ``other`` in its parent metric space."""
        return self.parent().dist(self, other)


class MetricSpacesCategory(CategoryWithAxiom):
    r"""Category of metric spaces.

    Canonical chain: ``TopologicalSpaces().Metric()``.
    """

    _base_category_class_and_axiom = (TopologicalSpaces, "Metric")
    ParentMethods : TypeAlias = _MetricSpaceObjectMethods
    ElementMethods : TypeAlias = _MetricSpaceElementMethods
    HomCategory : TypeAlias = MetricSpaceHomCategory
    Complete = LazyImport(
        "category_specs.topological_spaces.subcategories.complete",
        "_CompleteMetricSpaces",
    )

    @override
    @final
    def _repr_object_names(self) -> str:
        return "metric spaces"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return Sage metric spaces and local topological spaces."""
        return [SageMetricSpaces(), TopologicalSpaces()]

    class SubcategoryMethods:
        @final
        def Complete(self) -> Category:
            r"""Return the complete metric-space subcategory."""
            return cast(Category, with_axiom(self, "Complete"))
