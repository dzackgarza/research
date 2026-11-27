r"""End categories and endomorphism method surfaces."""

from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, ClassVar, final, override, TypeAlias

from sage.misc.lazy_import import LazyImport

from ..cat import Cat, Category, CategoryWithAxiom, CategoryWithAxiom_singleton
from .homsets import (
    HomCategory,
    HomCategoryConstruction,
    HomCategoryOf,
    UniversalHomElementMethods,
    UniversalHomObjectMethods,
)

if TYPE_CHECKING:
    from ..types import CategoryObject, End, Endomorphism


def _end_categories_of(category: Category) -> Category:
    if category.is_subcategory(HomCategory()):
        end_category: Category = category.EndCategory()
        return end_category
    hom_end_category: Category = category.HomCategory().EndCategory()
    return hom_end_category


class UniversalEndObjectMethods(UniversalHomObjectMethods):
    r"""Methods on objects ``End_C(A)`` of an end category."""

    @override
    @final
    def is_endomorphism_set(self) -> bool:
        r"""Return ``True`` because objects of this category are endomorphism
        objects.
        """
        return True

    @abstractmethod
    def identity(self) -> Endomorphism:
        r"""Return the identity endomorphism of this end object."""
        ...

    @final
    def one(self) -> Endomorphism:
        r"""Sage-compatible spelling for the identity endomorphism."""
        return self.identity()


class UniversalEndElementMethods(UniversalHomElementMethods):
    r"""Methods on elements of end categories."""

    @override
    @abstractmethod
    def parent(self) -> UniversalEndObjectMethods:
        r"""Return the end object containing this endomorphism."""
        ...

    @override
    @final
    def is_endomorphism(self) -> bool:
        r"""Return ``True`` because elements of this category are endomorphisms."""
        return True

    @override
    @final
    def is_identity(self) -> bool:
        r"""Return whether this endomorphism is the identity endomorphism."""
        return bool(self == self.parent().identity())


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

    ParentMethods : TypeAlias = UniversalEndObjectMethods
    ElementMethods : TypeAlias = UniversalEndElementMethods

    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport("category_specs.homsets.autsets", "AutCategory")


class EndCategoryConstruction(HomCategoryConstruction):
    r"""Functorial construction category for ``C.EndCategory()``.

    Canonical chain: ``C.EndCategory()``.
    """

    _functor_category = "EndCategory"

    class ParentMethods: ...

    class ElementMethods: ...

    def Of(self, domain: CategoryObject) -> End:  # type: ignore[override]
        r"""Return ``End_C(domain)`` for ``C = self.base_category()``."""
        end_object: End = self.base_category().HomCategory().Of(domain, domain)
        return end_object

    @override
    @classmethod
    def default_super_categories(cls, category: Category) -> Category:
        r"""Lift category supercategories through the end-category construction."""
        if cls is EndCategoryOf:
            return EndCategory()
        super_categories = category.super_categories()
        if not super_categories:
            return EndCategory()
        return Cat().join([_end_categories_of(super_category) for super_category in super_categories])


class EndCategoryOf(CategoryWithAxiom):
    r"""Generic category whose objects are ``End_C(A)``.

    Canonical chain: ``C.EndCategory()``.
    """

    _base_category_class_and_axiom: ClassVar[tuple[type[HomCategoryOf], str]] = (
        HomCategoryOf,
        "Endset",
    )

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
        end_object: End = self.base_category().Of(domain, domain)
        return end_object

    ParentMethods : TypeAlias = UniversalEndObjectMethods
    ElementMethods : TypeAlias = UniversalEndElementMethods

    # Sage axiom interop hook for _with_axiom("Autset").
    Autset = LazyImport("category_specs.homsets.autsets", "AutCategoryOf")
