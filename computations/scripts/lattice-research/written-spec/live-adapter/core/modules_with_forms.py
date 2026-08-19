"""ModulesWithForms(R) category — paired module + form data.

Lightweight scaffolding over category_specs/forms/chain.py which defines
the full category hierarchy. This module provides minimal Sage-registerable
categories for Phase 2 implementation work.
"""

from __future__ import annotations

from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.category_with_axiom import CategoryWithAxiom_singleton

from category_specs.utils import with_axiom


class ModulesWithFormsCategory(Category_over_base_ring):
    """Category of R-modules equipped with a form."""

    def super_categories(self) -> list[Category]:
        from sage.categories.modules import Modules

        return [Modules(self.base_ring())]

    class ParentMethods:
        def form(self) -> object:
            raise NotImplementedError

    class SubcategoryMethods:
        def Bilinear(self) -> Category:
            return with_axiom(self, "Bilinear")

        def Quadratic(self) -> Category:
            return with_axiom(self, "Quadratic")


class BilinearModulesCategory(CategoryWithAxiom_singleton):
    """Bilinear formed modules."""

    _base_category_class_and_axiom = (ModulesWithFormsCategory, "Bilinear")


class QuadraticModulesCategory(CategoryWithAxiom_singleton):
    """Quadratic formed modules."""

    _base_category_class_and_axiom = (ModulesWithFormsCategory, "Quadratic")
