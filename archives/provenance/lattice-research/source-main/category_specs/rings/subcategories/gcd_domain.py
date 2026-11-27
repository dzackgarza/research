r"""GcdDomains ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.gcd_domains import GcdDomains as SageGcdDomains
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .integral_domain import _IntegralDomains as _IntegralDomains

if TYPE_CHECKING:
    from ...types import (
        RingElement,
    )


class _GcdDomains(CategoryWithAxiom):
    r"""Canonical chain: ``Rings().Commutative().IntegralDomains().Gcd()``."""

    _base_category_class_and_axiom = (_IntegralDomains, "Gcd")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "gcd domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageGcdDomains(), _IntegralDomains()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageGcdDomains() or (
            R in self.base_category() and R.is_gcd_domain()
        )

    UniqueFactorization = LazyImport(
        "category_specs.rings.subcategories.unique_factorization_domain",
        "_UniqueFactorizationDomains",
    )

    class SubcategoryMethods:
        @final
        def UniqueFactorization(self) -> Category:
            return self._with_axiom("UniqueFactorization")

    class ParentMethods:
        @override
        @final
        def is_gcd_domain(self) -> bool:
            return True

        @abstractmethod
        def gcd(self, r: RingElement, s: RingElement) -> RingElement: ...

    class ElementMethods:
        @abstractmethod
        def gcd(self, other: RingElement) -> RingElement: ...

        @abstractmethod
        def lcm(self, other: RingElement) -> RingElement: ...

        @abstractmethod
        def xgcd(
            self, other: RingElement
        ) -> tuple[RingElement, RingElement, RingElement]: ...
