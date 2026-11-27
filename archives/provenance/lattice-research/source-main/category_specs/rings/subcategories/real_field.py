r"""RealFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.rings.abc import RealField as SageRealField

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _RealPrecisionFields,
    _ScientificNotationFields,
)

if TYPE_CHECKING:
    pass


class _RealFields(Category_singleton):
    r"""Category of Sage real floating point fields ``RealField(prec)``.

    Constructor target: ``Rings().Constructors().RealField(prec)`` refines
    here; the precision-53 singleton also refines into ``_RR``.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "real fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_RealPrecisionFields(), _ScientificNotationFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(R, SageRealField)

    class ParentMethods: ...

    class ElementMethods: ...
