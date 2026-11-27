r"""Aut categories and automorphism method surfaces."""

from __future__ import annotations

from typing import TYPE_CHECKING, final, override

from sage.sets.condition_set import ConditionSet as SageConditionSet

from ..cat import Cat, Category, CategoryWithAxiom, CategoryWithAxiom_singleton
from .endsets import EndCategory, EndCategoryConstruction, EndCategoryOf
from .homsets import HomCategory

if TYPE_CHECKING:
    from ..types import Aut, Automorphism, CategoryObject, End, Endomorphism, Subset


def _aut_categories_of(category: Category) -> Category:
    if category.is_subcategory(EndCategory()):
        end_category = category
    elif category.is_subcategory(HomCategory()):
        end_category = category.EndCategory()
    else:
        end_category = category.HomCategory().EndCategory()
    return end_category.AutCategory()


def _is_invertible_endomorphism(endomorphism: Endomorphism) -> bool:
    r"""Return whether an endomorphism lies in the corresponding aut category."""
    return endomorphism.is_invertible()


class UniversalAutObjectMethods:
    r"""Methods on objects ``Aut_C(A)`` of an aut category."""

    def condition_set(self) -> Subset:
        r"""Return the condition-set object backing this automorphism object."""
        return self

    def end_category(self) -> End:
        r"""Return the ambient endomorphism object whose units form this object."""
        return self.condition_set().ambient()

    def domain(self) -> CategoryObject:
        r"""Return the domain object of this automorphism object."""
        return self.end_category().domain()

    def codomain(self) -> CategoryObject:
        r"""Return the codomain object of this automorphism object."""
        return self.end_category().codomain()

    def identity(self) -> Automorphism:
        r"""Return the identity automorphism."""
        return self.end_category().identity()


class UniversalAutElementMethods:
    r"""Methods on elements of aut categories."""

    @override
    @final
    def is_invertible(self) -> bool:
        r"""Return ``True`` because automorphisms are invertible."""
        return True

    @override
    @final
    def is_isomorphism(self) -> bool:
        r"""Return ``True`` because automorphisms are isomorphisms."""
        return True

    @override
    @final
    def is_automorphism(self) -> bool:
        r"""Return ``True`` because these elements lie in an automorphism object."""
        return True


class AutCategory(CategoryWithAxiom_singleton):
    r"""Category of all automorphism categories.

    Canonical chain: ``AutCategory()``.
    """

    _base_category_class_and_axiom = (EndCategory, "Autset")

    @override
    def extra_super_categories(self) -> list[Category]:
        r"""Return the end-category layer refined by automorphism objects."""
        return [EndCategory()]

    def from_end_category(self, end_category: End) -> Aut:
        r"""Return the unit subobject of an endomorphism object."""
        return SageConditionSet(end_category, _is_invertible_endomorphism, category=self)

    ParentMethods = UniversalAutObjectMethods
    ElementMethods = UniversalAutElementMethods
    class MorphismMethods: ...


class AutCategoryConstruction(EndCategoryConstruction):
    r"""Functorial construction category for ``C.AutCategory()``.

    Canonical chain: ``C.AutCategory()``.
    """

    _functor_category = "AutCategory"

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

    @final
    def from_end_category(self, end_category: End) -> Aut:
        r"""Return the unit subobject of ``end_category`` for this construction."""
        return SageConditionSet(end_category, _is_invertible_endomorphism, category=self)

    @final
    def Of(self, domain: CategoryObject) -> Aut:
        r"""Return ``Aut_C(domain)`` for ``C = self.base_category()``."""
        end_category = self.base_category().EndCategory().Of(domain)
        return self.from_end_category(end_category)

    @override
    @classmethod
    def default_super_categories(cls, category: Category) -> Category:
        r"""Lift category supercategories through the automorphism construction."""
        if cls is AutCategoryOf:
            return AutCategory()
        super_categories = category.super_categories()
        if not super_categories:
            return AutCategory()
        return Category.join([_aut_categories_of(super_category) for super_category in super_categories])


class AutCategoryOf(CategoryWithAxiom):
    r"""Generic category whose objects are ``Aut_C(A)``.

    Canonical chain: ``C.AutCategory()``.
    """

    _base_category_class_and_axiom = (EndCategoryOf, "Autset")

    # Category-level construction: C.AutCategory() has objects Aut_C(A).
    # Its Of(A) constructor evaluates the construction at A.

    @override
    def extra_super_categories(self) -> list[Category]:
        r"""Return automorphism categories inherited from supercategories of the base."""
        aut_supercategories = [
            super_category.AutCategory()
            for super_category in self.base_category().super_categories()
            if super_category in Cat() and super_category.is_subcategory(EndCategory())
        ]
        return [AutCategory(), *aut_supercategories]

    def from_end_category(self, end_category: End) -> Aut:
        r"""Return the automorphism subobject of ``end_category`` in this category."""
        return SageConditionSet(end_category, _is_invertible_endomorphism, category=self)

    @final
    def Of(self, domain: CategoryObject) -> Aut:
        r"""Return ``Aut_C(domain)`` for ``C = self.base_category()``."""
        end_category = self.base_category().Of(domain)
        return self.from_end_category(end_category)

    ParentMethods = UniversalAutObjectMethods
    ElementMethods = UniversalAutElementMethods
    class MorphismMethods: ...
