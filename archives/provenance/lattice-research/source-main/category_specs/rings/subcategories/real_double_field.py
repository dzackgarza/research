r"""RealDoubleFields ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.rings.abc import RealDoubleField as SageRealDoubleField

from ...cat import Category, Category_singleton
from ._lazy_subcategories import _RealPrecisionFields

if TYPE_CHECKING:
    pass


class _RealDoubleFields(Category_singleton):
    r"""Category of Sage real double fields ``RDF``.

    Constructor target: ``Rings().Constructors().RDF()`` refines here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "real double fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_RealPrecisionFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return isinstance(R, SageRealDoubleField)

    class ParentMethods: ...

    class ElementMethods: ...
