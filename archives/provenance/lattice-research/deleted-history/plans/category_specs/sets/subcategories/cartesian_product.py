r"""One-object subcategory for Sage Cartesian products of sets."""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.category_singleton import Category_singleton
from sage.misc.abstract_method import abstract_method

if TYPE_CHECKING:
    from ...types import CartesianProductFunctor, Integer, Set, SetElement, SetMorphism, SympySet

from ...cat import Category
from .. import Sets


class _CartesianProductSets(Category_singleton):
    r"""Cartesian products of sets and their tuple-like elements.

    Constructor target:
    ``Sets().Constructors().CartesianProduct(factors)`` and
    ``Sets().Constructors().cartesian_product(factors)`` refine here after
    Sage constructs the product parent.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().CartesianProducts()]

    class ParentMethods:
        @override
        @abstract_method
        def _element_constructor_(self, x: SetElement) -> SetElement: ...

        @override
        @abstract_method
        def __contains__(self, x: Any) -> bool: ...

        @abstract_method
        def cartesian_factors(self) -> Sequence[Set]:
            r"""Return the factor sets of this Cartesian product."""
            ...

        @abstract_method
        def _sets_keys(self) -> Sequence[Set]: ...

        @abstract_method
        def cartesian_projection(self, i: Integer) -> Set:
            r"""Return the ``i``-th factor projection of this product set."""
            ...

        @abstract_method
        def _cartesian_product_of_elements(self, elements: Sequence[SetElement]) -> SetElement: ...

        @override
        @abstract_method
        def construction(self) -> tuple[CartesianProductFunctor, Sequence[Set]]: ...

        @abstract_method
        def _coerce_map_from_(self, S: Set) -> bool | SetMorphism | None: ...

        @override
        @abstract_method
        def _sympy_(self) -> SympySet: ...

    class ElementMethods:
        @abstract_method
        def cartesian_projection(self, i: Integer) -> SetElement:
            r"""Return the ``i``-th coordinate of this product element."""
            ...

        @abstract_method
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstract_method
        def __len__(self) -> Integer: ...

        @abstract_method
        def cartesian_factors(self) -> Sequence[SetElement]:
            r"""Return this Cartesian product element as ordered coordinates."""
            ...

    class MorphismMethods: ...
