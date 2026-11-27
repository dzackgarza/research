r"""Dual modules."""

from __future__ import annotations

from typing import final, override

from sage.categories.category import Category

from ....cat import DualObjectsCategory


class _DualObjects(DualObjectsCategory):
    r"""Dual modules M^* := Hom_R(M, R) viewed as integral linear forms.

    Canonical chain: ``Modules(R).DualObjects()``.
    """

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""The dual M^* is an integral linear form."""
        return [self.base_category().HomCategory().Forms().Linear().Integral()]

    class ParentMethods: ...

    class ElementMethods: ...
