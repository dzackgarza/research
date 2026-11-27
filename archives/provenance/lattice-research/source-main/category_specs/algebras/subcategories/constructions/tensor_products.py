r"""Tensor products of algebras."""

from __future__ import annotations

from typing import final, override

from ....cat import Category, TensorProductsCategory


class _TensorProducts(TensorProductsCategory):
    r"""Tensor products in a category of algebras.

    Canonical chain: ``Algebras(R).TensorProducts()``.
    """

    @override
    @final
    def extra_super_categories(self) -> list[Category]:
        r"""Return the algebra category inherited by tensor products."""
        return [self.base_category()]

    class ParentMethods: ...

    class ElementMethods: ...
