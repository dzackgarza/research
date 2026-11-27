r"""One-object subcategory for Sage Cartesian products of sets."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterator, Sequence
from typing import TYPE_CHECKING, Any, cast, final, override

from sage.categories.category_singleton import Category_singleton
from sage.categories.sets_cat import Sets as SageSets
from sage.sets.cartesian_product import CartesianProduct as SageCartesianProduct

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        CartesianProductFunctor,
        Integer,
        Set,
        SetElement,
        SetMorphism,
        SympySet,
    )

from ...cat import Category
from .. import Sets


class _CartesianProductSets(Category_singleton):
    r"""Cartesian products of sets and their tuple-like elements.

    Constructor target:
    ``Sets().Constructors().CartesianProduct(factors=factors)`` refines Sage's
    finite-factor product parent here after the original Sage constructor builds it.
    The lowercase ``Sets().Constructors().cartesian_product(factors)`` compatibility
    path refines into the same one-object category.
    """

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Sets().CartesianProducts()]

    class ParentMethods:
        @override
        @final
        def cardinality(self) -> Cardinality:
            r"""Return the product cardinality of the factor sets."""
            return cast(
                "Cardinality",
                SageSets.CartesianProducts.ParentMethods.cardinality(self),
            )

        @override
        @final
        def is_finite(self) -> bool:
            r"""Return whether this product set is finite."""
            return cast(bool, SageSets.CartesianProducts.ParentMethods.is_finite(self))

        @override
        @abstractmethod
        def _element_constructor_(self, x: SetElement) -> SetElement: ...

        @override
        @abstractmethod
        def __contains__(self, x: Any) -> bool: ...

        @abstractmethod
        def cartesian_factors(self) -> Sequence[Set]:
            r"""Return the factor sets of this Cartesian product."""
            ...

        @abstractmethod
        def _sets_keys(self) -> Sequence[Set]: ...

        @abstractmethod
        def cartesian_projection(self, i: Integer) -> Set:
            r"""Return the ``i``-th factor projection of this product set."""
            ...

        @abstractmethod
        def _cartesian_product_of_elements(
            self, elements: Sequence[SetElement]
        ) -> SetElement: ...

        @override
        @abstractmethod
        def construction(self) -> tuple[CartesianProductFunctor, Sequence[Set]]: ...

        @override
        @final
        def _coerce_map_from_(self, S: Set) -> bool | SetMorphism | None:
            r"""Return whether ``S`` coerces into this Cartesian product."""
            if isinstance(S, SageCartesianProduct):
                source_factors = S.cartesian_factors()
                target_factors = self.cartesian_factors()
                if len(source_factors) == len(target_factors) and all(
                    target.has_coerce_map_from(source)
                    for target, source in zip(target_factors, source_factors)
                ):
                    return True
            return None

        @override
        @final
        def _sympy_(self) -> SympySet:
            return SageSets.CartesianProducts.ParentMethods._sympy_(self)

    class ElementMethods:
        @abstractmethod
        def cartesian_projection(self, i: Integer) -> SetElement:
            r"""Return the ``i``-th coordinate of this product element."""
            ...

        @abstractmethod
        def __iter__(self) -> Iterator[SetElement]: ...

        @abstractmethod
        def __len__(self) -> Integer: ...

        @abstractmethod
        def cartesian_factors(self) -> Sequence[SetElement]:
            r"""Return this Cartesian product element as ordered coordinates."""
            ...
