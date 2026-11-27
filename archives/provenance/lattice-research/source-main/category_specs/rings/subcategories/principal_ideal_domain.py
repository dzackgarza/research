r"""PrincipalIdealDomains ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.principal_ideal_domains import (
    PrincipalIdealDomains as SagePrincipalIdealDomains,
)
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .unique_factorization_domain import (
    _UniqueFactorizationDomains as _UniqueFactorizationDomains,
)

if TYPE_CHECKING:
    from ...types import (
        Ideal,
        RingElement,
    )


class _PrincipalIdealDomains(CategoryWithAxiom):
    r"""Canonical chain:
    ``Rings().Commutative().IntegralDomains().Gcd().UniqueFactorization().PrincipalIdeal()``.
    """

    _base_category_class_and_axiom = (_UniqueFactorizationDomains, "PrincipalIdeal")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "principal ideal domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SagePrincipalIdealDomains(), _UniqueFactorizationDomains()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SagePrincipalIdealDomains() or (
            R in self.base_category() and R.is_pid()
        )

    Euclidean = LazyImport(
        "category_specs.rings.subcategories.euclidean_domain", "_EuclideanDomains"
    )

    class SubcategoryMethods:
        @final
        def Euclidean(self) -> Category:
            return self._with_axiom("Euclidean")

    class ParentMethods:
        @override
        @final
        def is_pid(self) -> bool:
            return True

        @final
        def ideal_generator(self, ideal: Ideal) -> RingElement:
            return ideal.gen()

        @override
        @final
        def gcd(self, r: RingElement, s: RingElement) -> RingElement:
            return self.ideal_generator(self.ideal([r, s]))

    class ElementMethods: ...
