r"""Complete metric spaces."""

from __future__ import annotations

from typing import final, override

from sage.categories.sets_cat import Sets as SageSets

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .metric import MetricSpacesCategory


class _CompleteMetricSpaces(CategoryWithAxiom):
    r"""Category of complete metric spaces.

    Canonical chain: ``TopologicalSpaces().Metric().Complete()``.
    """

    _base_category_class_and_axiom = (MetricSpacesCategory, "Complete")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complete metric spaces"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return Sage complete metric spaces and local metric spaces."""
        return [SageSets().Metric().Complete(), MetricSpacesCategory()]

    class ParentMethods:
        @override
        @final
        def is_complete(self) -> bool:
            r"""Return ``True`` because this object lies in complete metric spaces."""
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
