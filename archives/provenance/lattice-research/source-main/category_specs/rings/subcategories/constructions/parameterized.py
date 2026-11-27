r"""Parameterized ring construction category helpers."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast, final, override

from sage.rings.integer import Integer

from ....cat import Category, CategoryWithParameters

if TYPE_CHECKING:
    from ....types import Ring


class _Category_over_base_integer(CategoryWithParameters):
    r"""Base class for categories indexed by an integer and a base category.

    Canonical endpoint family: ``Rings().<integer-indexed construction>()``.
    """

    parameter_name = "integer"

    @staticmethod
    def __classcall_private__(
        cls: type[_Category_over_base_integer],
        category: Category,
        base_integer: Integer,
    ) -> _Category_over_base_integer:
        return cast(
            _Category_over_base_integer,
            super().__classcall__(cls, category, Integer(base_integer)),
        )

    def __init__(self, category: Category, base_integer: Integer) -> None:
        self._base_category = category
        self._base_integer = Integer(base_integer)
        Category.__init__(self)

    @final
    def base_category(self) -> Category:
        return self._base_category

    @final
    def base_integer(self) -> Integer:
        return self._base_integer

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [self.base_category()]

    @override
    @final
    def _make_named_class_key(self, name: str) -> tuple[Category, Integer]:
        return (self.base_category(), self.base_integer())

    class ParentMethods: ...

    class ElementMethods: ...



class _Category_over_base_integer_pair(CategoryWithParameters):
    r"""Base class for categories indexed by a base ring and two integers.

    Canonical endpoint family:
    ``Rings().<base-ring-and-integer-indexed construction>()``.
    """

    parameter_name = "integer_pair"

    @staticmethod
    def __classcall_private__(
        cls: type[_Category_over_base_integer_pair],
        base_ring: Ring,
        n: Integer,
        m: Integer | None = None,
    ) -> _Category_over_base_integer_pair:
        if m is None:
            m = n
        return cast(
            _Category_over_base_integer_pair,
            super().__classcall__(cls, base_ring, Integer(n), Integer(m)),
        )

    def __init__(self, base_ring: Ring, n: Integer, m: Integer) -> None:
        self._base_ring = base_ring
        self._n = Integer(n)
        self._m = Integer(m)
        Category.__init__(self)

    @final
    def base_ring(self) -> Ring:
        return self._base_ring

    @final
    def nrows(self) -> Integer:
        return self._n

    @final
    def ncols(self) -> Integer:
        return self._m

    @override
    @final
    def _make_named_class_key(self, name: str) -> tuple[Ring, Integer, Integer]:
        return (self._base_ring, self._n, self._m)

    @override
    def super_categories(self) -> list[Category]:
        from ... import Rings

        return [Rings()]

    class ParentMethods: ...

    class ElementMethods: ...
