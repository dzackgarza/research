r"""Topological and metric set subcategories."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.categories.category_with_axiom import CategoryWithAxiom
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method

if TYPE_CHECKING:
    from ...types import RealNumber, Set, SetElement

from .. import Sets


class _TopologicalSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (Sets, "Topological")

    def _repr_object_names(self) -> str:
        return "topological sets"

    def super_categories(self) -> list:
        return [SageSets().Topological(), Sets()]

    class SubcategoryMethods:
        @cached_method
        def Metric(self):
            return self._with_axiom("Metric")

    class ParentMethods:
        def is_topological(self) -> bool:
            return True

        @abstract_method
        def is_connected(self) -> bool: ...

        @abstract_method
        def closure(self) -> Set: ...

        @abstract_method
        def interior(self) -> Set: ...

        @abstract_method
        def boundary(self) -> Set: ...

        @abstract_method
        def is_open(self) -> bool: ...

        @abstract_method
        def is_closed(self) -> bool: ...

        @abstract_method
        def is_compact(self) -> bool: ...


class _MetricSets(CategoryWithAxiom):
    _base_category_class_and_axiom = (_TopologicalSets, "Metric")

    def _repr_object_names(self) -> str:
        return "metric sets"

    def super_categories(self) -> list:
        return [SageSets().Metric(), _TopologicalSets()]

    class ParentMethods:
        def is_metric(self) -> bool:
            return True

        @abstract_method
        def metric(self, x: SetElement, y: SetElement) -> RealNumber: ...

        @abstract_method
        def ball(self, center: SetElement, radius: RealNumber) -> Set: ...

        @abstract_method
        def dist(self, x: SetElement, y: SetElement) -> RealNumber: ...
