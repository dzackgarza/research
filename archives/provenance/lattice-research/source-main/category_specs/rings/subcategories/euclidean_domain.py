r"""EuclideanDomains ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.categories.euclidean_domains import EuclideanDomains as SageEuclideanDomains
from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .principal_ideal_domain import _PrincipalIdealDomains as _PrincipalIdealDomains

if TYPE_CHECKING:
    pass


class _EuclideanDomains(CategoryWithAxiom):
    r"""Canonical chain:
    ``Rings().Commutative().IntegralDomains().Gcd().UniqueFactorization().PrincipalIdeal().Euclidean()``.
    """

    _base_category_class_and_axiom = (_PrincipalIdealDomains, "Euclidean")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "euclidean domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [SageEuclideanDomains(), _PrincipalIdealDomains()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in SageEuclideanDomains() or (
            R in self.base_category() and R.is_euclidean_domain()
        )

    Field = LazyImport("category_specs.rings.subcategories.field", "_Fields")

    class SubcategoryMethods:
        @final
        def Field(self) -> Category:
            return self._with_axiom("Field")

    class ParentMethods: ...

    class ElementMethods: ...
