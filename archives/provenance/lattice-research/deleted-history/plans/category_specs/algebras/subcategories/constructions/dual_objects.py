r"""Dual objects of algebras."""

from __future__ import annotations

from typing import final, override

from ....cat import Category, DualObjectsCategory


class _DualObjects(DualObjectsCategory):
    r"""Dual objects in a category of algebras.

    Canonical chain: ``Algebras(R).DualObjects()``.
    """

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Return extra algebra categories carried by algebra duals."""
        return []

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
