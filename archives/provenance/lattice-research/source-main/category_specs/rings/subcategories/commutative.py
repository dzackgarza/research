r"""CommutativeRings ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.commutative_rings import CommutativeRings as SageCommutativeRings
from sage.misc.lazy_import import LazyImport
from sage.rings.integer import Integer

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .. import Rings

if TYPE_CHECKING:
    from ...types import (
        Cardinality,
        CompleteRing,
        Ideal,
        Integer,
        Ring,
        RingElement,
        RingMorphism,
    )


class _CommutativeRings(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative()``."""

    _base_category_class_and_axiom = (Rings, "Commutative")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "commutative rings"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageCommutativeRings(), Rings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageCommutativeRings() or (
            R in self.base_category() and R.is_commutative_ring()
        )

    IntegralDomains = LazyImport(
        "category_specs.rings.subcategories.integral_domain", "_IntegralDomains"
    )
    Noetherian = LazyImport(
        "category_specs.rings.subcategories.noetherian", "_NoetherianRings"
    )
    Local = LazyImport("category_specs.rings.subcategories.local", "_LocalRings")
    Reduced = LazyImport("category_specs.rings.subcategories.reduced", "_ReducedRings")

    class SubcategoryMethods:
        @final
        def IntegralDomains(self) -> Category:
            return self._with_axiom("IntegralDomains")
        @final
        def Field(self) -> Category:
            return (
                self.IntegralDomains()
                .Gcd()
                .UniqueFactorization()
                .PrincipalIdeal()
                .Euclidean()
                .Field()
            )
        @final
        def Noetherian(self) -> Category:
            return self._with_axiom("Noetherian")
        @final
        def Local(self) -> Category:
            return self._with_axiom("Local")
        @final
        def Reduced(self) -> Category:
            return self._with_axiom("Reduced")

    class ParentMethods:
        @override
        @final
        def is_commutative_ring(self) -> bool:
            return True

        @abstractmethod
        def completion(self, ideal: Ideal) -> CompleteRing: ...

        @abstractmethod
        # Computable via Macaulay2 (m2) backend.
        def gens(self) -> tuple[RingElement, ...]: ...

        @abstractmethod
        # Computable via Macaulay2 (m2) backend.
        def ngens(self) -> Integer: ...

        @abstractmethod
        # Computable via Macaulay2 (m2) backend.
        def characteristic(self) -> Integer: ...

        @abstractmethod
        # Computable via Macaulay2 (m2) backend.
        def krull_dimension(self) -> Cardinality: ...

        @abstractmethod
        # Computable via Macaulay2 (m2) backend.
        def hilbert_polynomial(self) -> RingElement: ...

        @abstractmethod
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
            implementation: str | None = None,
            prec: Integer | None = None,
            print_mode: str | None = None,
        ) -> Ring: ...

    class ElementMethods: ...
