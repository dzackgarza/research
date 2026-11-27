r"""ComplexFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.rings.abc import ComplexField as SageComplexField

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _ComplexPrecisionFields,
    _ScientificNotationFields,
)

if TYPE_CHECKING:
    pass


class _ComplexFields(Category_singleton):
    r"""Category of Sage complex floating point fields ``ComplexField(prec)``.

    Constructor target: ``Rings().Constructors().ComplexField(prec)`` refines
    here; the precision-53 singleton also refines into ``_CC``.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complex fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_ComplexPrecisionFields(), _ScientificNotationFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(R, SageComplexField)

    class ParentMethods: ...

    class ElementMethods: ...
