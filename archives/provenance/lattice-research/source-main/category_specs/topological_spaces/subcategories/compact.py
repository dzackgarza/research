r"""Compact topological spaces."""

from __future__ import annotations

from typing import final, override

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import TopologicalSpaces, _TopologicalSpaceObjectMethods


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
        r"""Return local topological spaces."""
        return [self.base_category()]

    class ParentMethods(_TopologicalSpaceObjectMethods):
        @override
        @final
        def is_compact(self) -> bool:
            r"""Return ``True`` because this object lies in compact spaces."""
            return True

    class ElementMethods: ...
