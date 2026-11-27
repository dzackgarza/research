r"""ZZ ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast, final, override

from ...cat import Category, Category_singleton
from .. import Rings
from ._lazy_subcategories import (
    _DedekindDomains,
    _EuclideanDomains,
)

if TYPE_CHECKING:
    from ...types import Ring
    pass


class _ZZ(Category_singleton):
    r"""Sage's integer ring.

    Constructor target: ``Rings().Constructors().ZZ()`` refines here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "integer ring"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [
            _EuclideanDomains(),
            _DedekindDomains(),
            Rings().Characteristic(0),
        ]

    @override
    @final
    def __contains__(self, x: Any) -> bool:
        from sage.all import ZZ

        return x is ZZ

    @final
    def object(self) -> Ring:
        from sage.all import ZZ

        return cast("Ring", ZZ)

    class ParentMethods: ...

    class ElementMethods: ...
