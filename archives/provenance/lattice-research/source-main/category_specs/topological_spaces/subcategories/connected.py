r"""Connected topological spaces."""

from __future__ import annotations

from typing import final, override

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import TopologicalSpaces, _TopologicalSpaceObjectMethods


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
        r"""Return local topological spaces."""
        return [self.base_category()]

    class ParentMethods(_TopologicalSpaceObjectMethods):
        @override
        @final
        def is_connected(self) -> bool:
            r"""Return ``True`` because this object lies in connected spaces."""
            return True

    class ElementMethods: ...
