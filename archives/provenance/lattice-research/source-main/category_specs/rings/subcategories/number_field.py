r"""NumberFields ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast, final, overload, override

from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.misc.lazy_import import LazyImport
from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from ...utils import with_axiom
from .global_field import _GlobalFields as _GlobalFields

_F = TypeVar("_F", bound=Callable[..., object])

if TYPE_CHECKING:
    from ...types import (
        AbelianGroup,
        Field,
        Group,
        Ideal,
        PrimeIdeal,
        Ring,
        RingElement,
        RingMorphism,
    )


class _NumberFields(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().Field().GlobalFields().NumberFields()``."""

    _base_category_class_and_axiom = (_GlobalFields, "NumberFields")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "number fields"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageNumberFields(), _GlobalFields()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageNumberFields() or (
            R in self.base_category() and R.is_number_field()
        )

    QuadraticNumberField = LazyImport(
        "category_specs.rings.subcategories.quadratic_number_field",
        "_QuadraticNumberFields",
    )
    Quadratic = QuadraticNumberField
    Cyclotomic = LazyImport(
        "category_specs.rings.subcategories.cyclotomic_field", "_CyclotomicFields"
    )

    class SubcategoryMethods:
        @final
        def QuadraticNumberField(self) -> Category:
            return cast(Category, with_axiom(self, "QuadraticNumberField"))
        @final
        def Quadratic(self) -> Category:
            return self.QuadraticNumberField()
        @final
        def Cyclotomic(self) -> Category:
            return cast(Category, with_axiom(self, "Cyclotomic"))

    class ParentMethods:
        @override
        @final
        def is_number_field(self) -> bool:
            return True

        @abstractmethod
        def is_quadratic(self) -> bool: ...

        @abstractmethod
        def is_cyclotomic(self) -> bool: ...

        @abstractmethod
        def degree(self) -> Integer: ...

        @abstractmethod
        def absolute_degree(self) -> Integer: ...

        @abstractmethod
        def signature(self) -> tuple[Integer, Integer]: ...

        @abstractmethod
        def discriminant(self) -> Integer: ...

        @abstractmethod
        def trace_pairing_discriminant(
            self, elements: Sequence[RingElement]
        ) -> RingElement:
            r"""Return the determinant of the trace pairing on ``elements``."""
            ...

        @abstractmethod
        def absolute_discriminant(self) -> Integer: ...

        @abstractmethod
        def galois_group(
            self,
            type: str | None = None,
            algorithm: str = "pari",
            names: str | None = None,
            gc_numbering: bool | None = None,
        ) -> Group: ...

        @overload
        def galois_closure(
            self, names: str | None = None, map: Literal[False] = False
        ) -> Field: ...

        @overload
        def galois_closure(
            self, names: str | None = None, map: Literal[True] = True
        ) -> tuple[Field, RingMorphism]: ...

        @overload
        def galois_closure(
            self, names: str | None = None, map: bool = False
        ) -> Field | tuple[Field, RingMorphism]: ...

        @abstractmethod
        def galois_closure(
            self, names: str | None = None, map: bool = False
        ) -> Field | tuple[Field, RingMorphism]: ...

        @abstractmethod
        def automorphisms(self) -> list[RingMorphism]: ...

        @abstractmethod
        def class_number(self, proof: bool | None = None) -> Integer: ...

        @abstractmethod
        def class_group(
            self, proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup: ...

        @abstractmethod
        def integral_basis(self) -> tuple[RingElement, ...]: ...

        @abstractmethod
        def integral_basis_at_prime(self, prime: Integer) -> tuple[RingElement, ...]:
            r"""Return an integral basis for an order maximal at ``prime``."""
            ...

        @abstractmethod
        def integral_basis_at_primes(
            self, primes: Sequence[Integer]
        ) -> tuple[RingElement, ...]:
            r"""Return an integral basis for an order maximal at each listed prime."""
            ...

        @abstractmethod
        def power_basis(self) -> tuple[RingElement, ...]: ...

        @abstractmethod
        def reduced_basis(
            self, prec: Integer | None = None
        ) -> tuple[RingElement, ...]: ...

        @abstractmethod
        def different(self) -> Ideal: ...

        @abstractmethod
        def places(
            self, all_complex: bool = False, prec: Integer | None = None
        ) -> tuple[RingMorphism, ...]: ...

        @abstractmethod
        def real_embeddings(self, prec: int = 53) -> tuple[RingMorphism, ...]: ...

        @abstractmethod
        def complex_embeddings(self, prec: int = 53) -> tuple[RingMorphism, ...]: ...

        @abstractmethod
        def roots_of_unity(self) -> list[RingElement]: ...

        @abstractmethod
        def regulator(self, proof: bool | None = None) -> RingElement: ...

        @abstractmethod
        def units(self, proof: bool | None = None) -> list[RingElement]: ...

        @abstractmethod
        def unit_group(self, proof: bool | None = None) -> AbelianGroup: ...

        @abstractmethod
        def conductor(self, check_abelian: bool = True) -> Integer: ...

        @abstractmethod
        def prime_above(
            self, x: RingElement, degree: Integer | None = None
        ) -> PrimeIdeal: ...

        @abstractmethod
        def primes_above(
            self, x: RingElement, degree: Integer | None = None
        ) -> list[PrimeIdeal]: ...

        @abstractmethod
        def S_units(
            self, S: Sequence[PrimeIdeal], proof: bool = True
        ) -> list[RingElement]: ...

        @abstractmethod
        def S_class_group(
            self, S: Sequence[PrimeIdeal], proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup: ...

        @abstractmethod
        def ring_of_integers(
            self,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring: ...

        @abstractmethod
        def ring_of_integers_at_prime(
            self,
            prime: Integer,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            r"""Return an order of integers that is maximal at ``prime``."""
            ...

        @abstractmethod
        def ring_of_integers_at_primes(
            self,
            primes: Sequence[Integer],
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            r"""Return an order of integers maximal at each listed prime."""
            ...

        @abstractmethod
        def maximal_order(
            self,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring: ...

        @abstractmethod
        def maximal_order_at_prime(
            self,
            prime: Integer,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            r"""Return an order that is maximal at ``prime``."""
            ...

        @abstractmethod
        def maximal_order_at_primes(
            self,
            primes: Sequence[Integer],
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            r"""Return an order that is maximal at each listed prime."""
            ...

        @abstractmethod
        def absolute_field(self, names: str) -> Field: ...

    class ElementMethods:
        @abstractmethod
        def norm(self, K: Field | None = None) -> RingElement: ...

        @abstractmethod
        def trace(self, K: Field | None = None) -> RingElement: ...

        @abstractmethod
        def minpoly(
            self, var: str = "x", algorithm: str | None = None
        ) -> RingElement: ...

        @abstractmethod
        def charpoly(
            self, var: str = "x", algorithm: str | None = None
        ) -> RingElement: ...
