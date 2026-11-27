r"""IntegralDomains ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .commutative import _CommutativeRings as _CommutativeRings

if TYPE_CHECKING:
    from ...types import (
        Field,
        LocalRing,
        RingElement,
    )


class _IntegralDomains(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().IntegralDomains()``."""

    _base_category_class_and_axiom = (_CommutativeRings, "IntegralDomains")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "integral domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageIntegralDomains(), _CommutativeRings()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageIntegralDomains() or (
            R in self.base_category() and R.is_integral_domain()
        )

    Gcd = LazyImport("category_specs.rings.subcategories.gcd_domain", "_GcdDomains")
    IntegrallyClosed = LazyImport(
        "category_specs.rings.subcategories.integrally_closed_domain",
        "_IntegrallyClosedDomains",
    )

    class SubcategoryMethods:
        @final
        def Gcd(self) -> Category:
            return self._with_axiom("Gcd")
        @final
        def UniqueFactorization(self) -> Category:
            return self.Gcd().UniqueFactorization()
        @final
        def PrincipalIdeal(self) -> Category:
            return self.Gcd().UniqueFactorization().PrincipalIdeal()
        @final
        def Euclidean(self) -> Category:
            return self.Gcd().UniqueFactorization().PrincipalIdeal().Euclidean()
        @final
        def IntegrallyClosed(self) -> Category:
            return self._with_axiom("IntegrallyClosed")
        @final
        def Dedekind(self) -> Category:
            return self.IntegrallyClosed().Dedekind()

    class ParentMethods:
        @abstractmethod
        def fraction_field(self) -> Field: ...

        @abstractmethod
        def localization(
            self,
            additional_units: RingElement | Sequence[RingElement],
            names: str | Sequence[str] | None = None,
            normalize: bool = True,
            category: Category | None = None,
        ) -> LocalRing: ...

    class ElementMethods:
        @abstractmethod
        def divides(self, other: RingElement) -> bool: ...
