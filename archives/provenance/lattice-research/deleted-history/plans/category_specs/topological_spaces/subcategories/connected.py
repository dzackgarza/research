r"""Connected topological spaces."""

from __future__ import annotations

from typing import final, override

from sage.categories.sets_cat import Sets as SageSets

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import TopologicalSpaces


class _ConnectedTopologicalSpaces(CategoryWithAxiom):
    r"""Category of connected topological spaces.

    Canonical chain: ``TopologicalSpaces().Connected()``.
    """

    _base_category_class_and_axiom = (TopologicalSpaces, "Connected")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "connected topological spaces"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return Sage connected spaces and local topological spaces."""
        return [SageSets().Topological().Connected(), TopologicalSpaces()]

    class ParentMethods:
        @override
        @final
        def is_connected(self) -> bool:
            r"""Return ``True`` because this object lies in connected spaces."""
            return True

    class ElementMethods: ...
    class MorphismMethods: ...
