r"""AlgebraicallyClosedFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .field import _Fields as _Fields

if TYPE_CHECKING:
    from ...types import (
        Field,
    )


class _AlgebraicallyClosedFields(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Field().AlgebraicallyClosed()``."""

    _base_category_class_and_axiom = (_Fields, "AlgebraicallyClosed")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "algebraically closed fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_Fields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_algebraically_closed()

    class ParentMethods:
        @final
        def is_algebraically_closed(self) -> bool:
            return True

        @final
        def algebraic_closure(self) -> Field:
            return self

    class ElementMethods: ...
