r"""ComplexDoubleFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.rings.abc import ComplexDoubleField as SageComplexDoubleField

from ...cat import Category, Category_singleton
from ._lazy_subcategories import _ComplexPrecisionFields

if TYPE_CHECKING:
    pass


class _ComplexDoubleFields(Category_singleton):
    r"""Category of Sage complex double fields ``CDF``.

    Constructor target: ``Rings().Constructors().CDF()`` refines here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "complex double fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_ComplexPrecisionFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(R, SageComplexDoubleField)

    class ParentMethods: ...

    class ElementMethods: ...
