r"""IntegrallyClosedDomains ring subcategory spec."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, final, override

from sage.misc.lazy_import import LazyImport

from ...cat import Category
from ...cat import CategoryWithAxiom_singleton as CategoryWithAxiom
from .integral_domain import _IntegralDomains as _IntegralDomains

if TYPE_CHECKING:
    from ...types import (
        Ring,
    )


class _IntegrallyClosedDomains(CategoryWithAxiom):
    r"""Canonical chain:
    ``Rings().Commutative().IntegralDomains().IntegrallyClosed()``.
    """

    _base_category_class_and_axiom = (_IntegralDomains, "IntegrallyClosed")

    @override
    @final
    def _repr_object_names(self) -> str:
        return "integrally closed domains"

    @override
    @final
    def super_categories(self) -> list[Category]:
        return [_IntegralDomains()]

    @override
    @final
    def __contains__(self, R: Any) -> bool:
        return R in self.base_category() and R.is_integrally_closed()

    Dedekind = LazyImport(
        "category_specs.rings.subcategories.dedekind_domain", "_DedekindDomains"
    )

    class SubcategoryMethods:
        @final
        def Dedekind(self) -> Category:
            return self._with_axiom("Dedekind")

    class ParentMethods:
        @final
        def is_integrally_closed(self) -> bool:
            return True

        @final
        def integral_closure(self: Ring) -> Ring:
            return self

    class ElementMethods: ...
