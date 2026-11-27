r"""Compact topological spaces."""

from __future__ import annotations

from typing import final, override

from sage.categories.sets_cat import Sets as SageSets

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import TopologicalSpaces


class _CompactTopologicalSpaces(CategoryWithAxiom):
    r"""Category of compact topological spaces.

    Canonical chain: ``TopologicalSpaces().Compact()``.
    """

    _base_category_class_and_axiom = (TopologicalSpaces, "Compact")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "compact topological spaces"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return Sage compact spaces and local topological spaces."""
        return [SageSets().Topological().Compact(), TopologicalSpaces()]

    class ParentMethods:
        @override
        @final
        def is_compact(self) -> bool:
            r"""Return ``True`` because this object lies in compact spaces."""
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
