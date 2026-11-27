r"""End categories and endomorphism method surfaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport

from ..cat import Cat, Category, CategoryWithAxiom, CategoryWithAxiom_singleton
from .homsets import HomCategory, HomCategoryConstruction, HomCategoryOf

if TYPE_CHECKING:
    from ..types import CategoryObject, End, Endomorphism


def _end_categories_of(category: Category) -> Category:
    if category.is_subcategory(HomCategory()):
        return category.EndCategory()
    return category.HomCategory().EndCategory()


class UniversalEndObjectMethods:
    r"""Methods on objects ``End_C(A)`` of an end category."""

    @override
    @final
    def is_endomorphism_set(self) -> bool:
        r"""Return ``True`` because objects of this category are endomorphism objects."""
        return True

    @abstract_method
    def identity(self) -> Endomorphism:
        r"""Return the identity endomorphism of this end object."""
        ...


class UniversalEndElementMethods:
    r"""Methods on elements of end categories."""

    @override
    @final
    def is_endomorphism(self) -> bool:
        r"""Return ``True`` because elements of this category are endomorphisms."""
        return True


class EndCategory(CategoryWithAxiom_singleton):
    r"""Category of all endomorphism categories.

    Canonical chain: ``EndCategory()``.
    """

    _base_category_class_and_axiom = (HomCategory, "Endset")

    @override
    def extra_super_categories(self) -> list[Category]:
        r"""Return Sage's endset axiom category refined by this spec."""
        from sage.categories.homsets import Homsets as SageHomsets

        return [SageHomsets().Endset()]

    ParentMethods = UniversalEndObjectMethods
    ElementMethods = UniversalEndElementMethods
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport("category_specs.homsets.autsets", "AutCategory")


class EndCategoryConstruction(HomCategoryConstruction):
    r"""Functorial construction category for ``C.EndCategory()``.

    Canonical chain: ``C.EndCategory()``.
    """

    _functor_category = "EndCategory"

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

    @final
    def Of(self, domain: CategoryObject) -> End:
        r"""Return ``End_C(domain)`` for ``C = self.base_category()``."""
        return self.base_category().HomCategory().Of(domain, domain)

    @override
    @classmethod
    def default_super_categories(cls, category: Category) -> Category:
        r"""Lift category supercategories through the end-category construction."""
        if cls is EndCategoryOf:
            return EndCategory()
        super_categories = category.super_categories()
        if not super_categories:
            return EndCategory()
        return Category.join([_end_categories_of(super_category) for super_category in super_categories])


class EndCategoryOf(CategoryWithAxiom):
    r"""Generic category whose objects are ``End_C(A)``.

    Canonical chain: ``C.EndCategory()``.
    """

    _base_category_class_and_axiom = (HomCategoryOf, "Endset")

    # Category-level construction: C.EndCategory() has objects End_C(A).
    # Its Of(A) constructor evaluates the construction at A.

    @override
    def extra_super_categories(self) -> list[Category]:
        r"""Return the end categories inherited from supercategories of the base."""
        end_supercategories = [
            _end_categories_of(super_category)
            for super_category in self.base_category().super_categories()
            if super_category in Cat() and super_category.is_subcategory(HomCategory())
        ]
        return [EndCategory(), *end_supercategories]

    @final
    def Of(self, domain: CategoryObject) -> End:
        r"""Return ``End_C(domain)`` for ``C = self.base_category()``."""
        return self.base_category().Of(domain, domain)

    ParentMethods = UniversalEndObjectMethods
    ElementMethods = UniversalEndElementMethods
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport("category_specs.homsets.autsets", "AutCategoryOf")
