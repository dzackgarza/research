r"""UniqueFactorizationDomains ring subcategory spec."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.unique_factorization_domains import (
    UniqueFactorizationDomains as SageUniqueFactorizationDomains,
)
from sage.misc.lazy_import import LazyImport
from sage.structure.factorization import Factorization

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .gcd_domain import _GcdDomains as _GcdDomains

if TYPE_CHECKING:
    pass


class _UniqueFactorizationDomains(CategoryWithAxiom):
    r"""Canonical chain:
    ``Rings().Commutative().IntegralDomains().Gcd().UniqueFactorization()``.
    """

    _base_category_class_and_axiom = (_GcdDomains, "UniqueFactorization")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "unique factorization domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageUniqueFactorizationDomains(), _GcdDomains()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageUniqueFactorizationDomains() or (
            R in self.base_category() and R.is_unique_factorization_domain()
        )

    PrincipalIdeal = LazyImport(
        "category_specs.rings.subcategories.principal_ideal_domain",
        "_PrincipalIdealDomains",
    )

    class SubcategoryMethods:
        @final
        def PrincipalIdeal(self) -> Category:
            return self._with_axiom("PrincipalIdeal")

    class ElementMethods:
        @abstractmethod
        def factor(self) -> Factorization: ...

        @abstractmethod
        def is_irreducible(self) -> bool: ...

        @abstractmethod
        def is_prime(self) -> bool: ...

    class ParentMethods: ...
