r"""QQ ring subcategory spec."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast, final, overload, override

from sage.rings.integer import Integer

from ...cat import Category, Category_singleton
from .. import Rings
from ._lazy_subcategories import (
    _FractionFields,
    _NumberFields,
)

_F = TypeVar("_F", bound=Callable[..., object])

if TYPE_CHECKING:
    from ...types import (
        AbelianGroup,
        Field,
        Group,
        Ideal,
        NumberField,
        PrimeIdeal,
        Ring,
        RingElement,
        RingMorphism,
    )


class _QQ(Category_singleton):
    r"""Sage's rational field.

    Constructor target: ``Rings().Constructors().QQ()`` refines here.
    """

    @override
    @final
    def _repr_object_names(self) -> str:
        return "rational field"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [
            _FractionFields(),
            _NumberFields(),
            Rings().Characteristic(0),
        ]

    @override
    @final
    def __contains__(self, x: Any) -> bool:
        from sage.all import QQ

        return x is QQ

    @final
    def object(self) -> Ring:
        from sage.all import QQ

        return cast("Ring", QQ)

    class ParentMethods:
        @override
        @final
        def is_algebraically_closed(self) -> bool:
            return False

        @override
        @final
        def algebraic_closure(self) -> Field:
            from sage.all import QQbar

            return cast("Field", QQbar)
        @final
        def as_number_field(self) -> NumberField:
            from sage.all import ZZ, PolynomialRing
            from sage.all import NumberField as SageNumberField

            R = PolynomialRing(ZZ, "x")
            return cast("NumberField", SageNumberField(R.gen(), "a"))

        @override
        @final
        def is_quadratic(self) -> bool:
            return self.as_number_field().is_quadratic()

        @override
        @final
        def is_cyclotomic(self) -> bool:
            return self.as_number_field().is_cyclotomic()

        @override
        @final
        def degree(self) -> Integer:
            return self.as_number_field().degree()

        @override
        @final
        def absolute_degree(self) -> Integer:
            return self.as_number_field().absolute_degree()

        @override
        @final
        def signature(self) -> tuple[Integer, Integer]:
            return self.as_number_field().signature()

        @override
        @final
        def discriminant(self) -> Integer:
            return self.as_number_field().discriminant()

        @override
        @final
        def trace_pairing_discriminant(
            self, elements: Sequence[RingElement]
        ) -> RingElement:
            from sage.all import QQ, matrix

            trace_matrix = matrix(
                QQ,
                [[QQ(left) * QQ(right) for right in elements] for left in elements],
            )
            return cast("RingElement", trace_matrix.det())

        @override
        @final
        def absolute_discriminant(self) -> Integer:
            return self.as_number_field().absolute_discriminant()

        @override
        @final
        def galois_group(
            self,
            type: str | None = None,
            algorithm: str = "pari",
            names: str | None = None,
            gc_numbering: bool | None = None,
        ) -> Group:
            return self.as_number_field().galois_group(
                type=type, algorithm=algorithm, names=names, gc_numbering=gc_numbering
            )

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

        @override
        @final
        def galois_closure(
            self, names: str | None = None, map: bool = False
        ) -> Field | tuple[Field, RingMorphism]:
            return self.as_number_field().galois_closure(names=names, map=map)

        @override
        @final
        def automorphisms(self) -> list[RingMorphism]:
            return self.as_number_field().automorphisms()

        @override
        @final
        def class_number(self, proof: bool | None = None) -> Integer:
            return self.as_number_field().class_number(proof=proof)

        @override
        @final
        def class_group(
            self, proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup:
            return self.as_number_field().class_group(proof=proof, names=names)

        @override
        @final
        def integral_basis(self) -> tuple[RingElement, ...]:
            return self.as_number_field().integral_basis()

        @override
        @final
        def integral_basis_at_prime(self, prime: Integer) -> tuple[RingElement, ...]:
            from sage.all import QQ

            return (cast("RingElement", QQ(1)),)

        @override
        @final
        def integral_basis_at_primes(
            self, primes: Sequence[Integer]
        ) -> tuple[RingElement, ...]:
            from sage.all import QQ

            return (cast("RingElement", QQ(1)),)

        @override
        @final
        def power_basis(self) -> tuple[RingElement, ...]:
            return self.as_number_field().power_basis()

        @override
        @final
        def reduced_basis(self, prec: Integer | None = None) -> tuple[RingElement, ...]:
            return self.as_number_field().reduced_basis(prec=prec)

        @override
        @final
        def different(self) -> Ideal:
            return self.as_number_field().different()

        @override
        @final
        def places(
            self, all_complex: bool = False, prec: Integer | None = None
        ) -> tuple[RingMorphism, ...]:
            return self.as_number_field().places(all_complex=all_complex, prec=prec)

        @override
        @final
        def real_embeddings(self, prec: int = 53) -> tuple[RingMorphism, ...]:
            return self.as_number_field().real_embeddings(prec=prec)

        @override
        @final
        def complex_embeddings(self, prec: int = 53) -> tuple[RingMorphism, ...]:
            return self.as_number_field().complex_embeddings(prec=prec)

        @override
        @final
        def roots_of_unity(self) -> list[RingElement]:
            return self.as_number_field().roots_of_unity()

        @override
        @final
        def regulator(self, proof: bool | None = None) -> RingElement:
            return self.as_number_field().regulator(proof=proof)

        @override
        @final
        def units(self, proof: bool | None = None) -> list[RingElement]:
            return self.as_number_field().units(proof=proof)

        @override
        @final
        def unit_group(self, proof: bool | None = None) -> AbelianGroup:
            return self.as_number_field().unit_group(proof=proof)

        @override
        @final
        def conductor(self, check_abelian: bool = True) -> Integer:
            return self.as_number_field().conductor(check_abelian=check_abelian)

        @override
        @final
        def prime_above(
            self, x: RingElement, degree: Integer | None = None
        ) -> PrimeIdeal:
            return self.as_number_field().prime_above(x, degree=degree)

        @override
        @final
        def primes_above(
            self, x: RingElement, degree: Integer | None = None
        ) -> list[PrimeIdeal]:
            return self.as_number_field().primes_above(x, degree=degree)

        @override
        @final
        def S_units(
            self, S: Sequence[PrimeIdeal], proof: bool = True
        ) -> list[RingElement]:
            return self.as_number_field().S_units(S, proof=proof)

        @override
        @final
        def S_class_group(
            self, S: Sequence[PrimeIdeal], proof: bool | None = None, names: str = "c"
        ) -> AbelianGroup:
            return self.as_number_field().S_class_group(S, proof=proof, names=names)

        @override
        @final
        def ring_of_integers(
            self,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            from sage.all import ZZ

            return cast("Ring", ZZ)

        @override
        @final
        def ring_of_integers_at_prime(
            self,
            prime: Integer,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            from sage.all import ZZ

            return cast("Ring", ZZ)

        @override
        @final
        def ring_of_integers_at_primes(
            self,
            primes: Sequence[Integer],
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            from sage.all import ZZ

            return cast("Ring", ZZ)

        @override
        @final
        def maximal_order(
            self,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            from sage.all import ZZ

            return cast("Ring", ZZ)

        @override
        @final
        def maximal_order_at_prime(
            self,
            prime: Integer,
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            from sage.all import ZZ

            return cast("Ring", ZZ)

        @override
        @final
        def maximal_order_at_primes(
            self,
            primes: Sequence[Integer],
            assume_maximal: bool
            | None
            | Literal["non-maximal-non-unique"] = "non-maximal-non-unique",
        ) -> Ring:
            from sage.all import ZZ

            return cast("Ring", ZZ)

        @override
        @final
        def absolute_field(self, names: str) -> Field:
            return self.as_number_field().absolute_field(names)

    class ElementMethods: ...
