r"""PolynomialRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings
from ._sage_ring_classes import _SAGE_POLYNOMIAL_RING_CLASSES

if TYPE_CHECKING:
    from ...types import (
        CompleteRing,
        Ideal,
        Polynomial,
        Ring,
        RingElement,
        RingMorphism,
    )


class _PolynomialRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Polynomial()``."""

    _base_category_class_and_axiom = (Rings, "Polynomial")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "polynomial rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and (
            isinstance(R, _SAGE_POLYNOMIAL_RING_CLASSES)
            or isinstance(R, self.parent_class)
        )

    class ParentMethods:
        @override
        @final
        def is_polynomial_ring(self) -> bool:
            return True

        @override
        @final
        def extension(
            self,
            poly: RingElement,
            name: str | None = None,
            names: str | Sequence[str] | None = None,
            *,
            latex_name: str | None = None,
            latex_names: str | Sequence[str] | None = None,
            map: bool = False,
            embedding: RingMorphism | None = None,
        ) -> Ring:
            base_ext = self.base_ring().extension(
                poly,
                name=name,
                names=names,
                latex_name=latex_name,
                latex_names=latex_names,
                map=map,
                embedding=embedding,
            )
            return self.change_ring(base_ext)

        @override
        @final
        def completion(self, ideal: Ideal) -> CompleteRing:
            from sage.rings.infinity import infinity

            assert ideal.is_principal(), (
                "polynomial ring completion expects a principal ideal"
            )
            p: Polynomial = ideal.gen()
            assert p.is_irreducible(), (
                "polynomial ring completion expects an irreducible generator"
            )
            completion: CompleteRing = super().completion(p, prec=infinity)
            return completion

        @abstractmethod
        def gen(self, n: Integer = 0) -> RingElement: ...

        @abstractmethod
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstractmethod
        def change_ring(self, R: Ring) -> Ring: ...

        @abstractmethod
        def change_var(self, var: str) -> Ring: ...

        @abstractmethod
        def monomials_of_degree(self, n: Integer) -> tuple[RingElement, ...]: ...

        @abstractmethod
        def monics(
            self,
            of_degree: Integer | None = None,
            max_degree: Integer | None = None,
        ) -> Iterable[RingElement]:
            ...

        @abstractmethod
        def cyclotomic_polynomial(self, n: Integer) -> RingElement: ...

        @abstractmethod
        def weil_polynomials(
            self,
            d: Integer,
            q: Integer,
            sign: Integer = Integer(1),
            lead: RingElement | Sequence[RingElement] = Integer(1),
        ) -> Sequence[RingElement]:
            ...

    class ElementMethods: ...
