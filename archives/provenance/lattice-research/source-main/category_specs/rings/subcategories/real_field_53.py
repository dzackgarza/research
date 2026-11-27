r"""RR ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast, final, override

from ...cat import Category, Category_singleton
from ._lazy_subcategories import (
    _RealFields,
)

if TYPE_CHECKING:
    from ...types import Ring

    pass


class _RR(Category_singleton):
    r"""Sage's precision-53 real field.

    Constructor target: ``Rings().Constructors().RR()`` and
    ``Rings().Constructors().RealField(53)`` refine here when Sage returns the
    canonical ``RR`` object.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "real field with 53 bits of precision"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_RealFields()]

    @override
    @final
    def __contains__(self, x: Any) -> bool:
        from sage.all import RR

        return x is RR

    @final
    def object(self) -> Ring:
        from sage.all import RR

        return cast("Ring", RR)

    class ParentMethods: ...

    class ElementMethods: ...
