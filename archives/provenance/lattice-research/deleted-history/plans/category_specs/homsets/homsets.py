r"""Hom categories and morphism method surfaces."""

from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, final, overload, override

from sage.misc.abstract_method import abstract_method
from sage.misc.lazy_import import LazyImport
from sage.structure.parent import Parent

from ..cat import Cat, Category, FunctorialConstructionCategory, _SageCategory
from ..cat import Homsets as SageHomsetsBase

if TYPE_CHECKING:
    from ..types import CategoryElement, CategoryObject, Hom, Morphism


class UniversalHomObjectMethods:
    r"""Methods on objects ``Hom_C(A, B)`` of a hom category."""

    @abstract_method
    def domain(self) -> CategoryObject:
        r"""Return the source object ``A`` of this hom object."""
        ...

    @abstract_method
    def codomain(self) -> CategoryObject:
        r"""Return the target object ``B`` of this hom object."""
        ...

    @override
    @final
    def is_endomorphism_set(self) -> bool:
        r"""Return whether this hom object is an endomorphism object."""
        return self.domain() == self.codomain()

    @overload
    def __call__(self, morphism: Morphism) -> Morphism: ...

    @overload
    def __call__(self, function: Callable[[CategoryElement], CategoryElement]) -> Morphism: ...

    @abstract_method
    def __call__(self, data: Morphism | Callable[[CategoryElement], CategoryElement]) -> Morphism:
        r"""Coerce morphism data into this hom object."""
        ...


class UniversalHomElementMethods:
    r"""Methods on elements ``f`` of hom categories."""

    @final
    def domain(self) -> CategoryObject:
        r"""Return the domain of this morphism."""
        return self.parent().domain()

    @final
    def codomain(self) -> CategoryObject:
        r"""Return the codomain of this morphism."""
        return self.parent().codomain()

    @abstract_method
    def __call__(self, x: CategoryElement) -> CategoryElement:
        r"""Evaluate this morphism at ``x``."""
        ...

    @abstract_method
    def image(self, domain_subset: CategoryObject | None = None) -> CategoryObject:
        r"""Return the image of ``domain_subset`` under this morphism."""
        ...

    @abstract_method
    def pre_compose(self, other: Morphism) -> Morphism:
        r"""Return ``self`` after precomposition by ``other``."""
        ...

    @abstract_method
    def post_compose(self, other: Morphism) -> Morphism:
        r"""Return ``self`` after postcomposition by ``other``."""
        ...

    @override
    @final
    def is_endomorphism(self) -> bool:
        r"""Return whether this morphism has equal domain and codomain."""
        return self.domain() == self.codomain()

    @override
    @final
    def is_identity(self) -> bool:
        r"""Return whether this morphism is the identity endomorphism."""
        return self.is_endomorphism() and self == self.parent().identity()

    @abstract_method
    def is_invertible(self) -> bool:
        r"""Return whether this morphism has a two-sided inverse."""
        ...

    @abstract_method
    def is_isomorphism(self) -> bool:
        r"""Return whether this morphism is an isomorphism in its category."""
        ...

    @override
    @final
    def is_automorphism(self) -> bool:
        r"""Return whether this morphism is an invertible endomorphism."""
        return self.is_endomorphism() and self.is_invertible()


class HomCategory(SageHomsetsBase):
    r"""Category of all hom categories.

    Canonical chain: ``HomCategory()``.
    """

    @override
    def super_categories(self) -> list[Category]:
        r"""Return Sage's base hom-category supercategories."""
        return super().super_categories()

    ParentMethods = UniversalHomObjectMethods
    ElementMethods = UniversalHomElementMethods
    class MorphismMethods: ...

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport("category_specs.homsets.endsets", "EndCategory")


class HomCategoryConstruction(FunctorialConstructionCategory):
    r"""Functorial construction category for ``C.HomCategory()``.

    Canonical chain: ``C.HomCategory()``.

    This is the project-owned functorial assignment ``Hom_*: Cat -> Cat``,
    sending ``C`` to ``Hom_C``.  Sage's ``HomsetsCategory`` is inventory
    and interop vocabulary here; it is not a source of mathematical method
    inheritance.  The Hom method surface is declared in this file and refined
    by subtree ``homsets.py`` files.
    """

    _functor_category = "HomCategory"
    _base_category_class = (_SageCategory,)

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...

    @final
    def Of(self, domain: CategoryObject, codomain: CategoryObject) -> Hom:
        r"""Return ``Hom_C(domain, codomain)`` for ``C = self.base_category()``."""
        category = self.base_category()
        assert domain in category, "domain must be an object of the base category"
        assert codomain in category, "codomain must be an object of the base category"
        return Parent.Hom(domain, codomain, category=category)

    @override
    @classmethod
    @final
    def default_super_categories(cls, category: Category) -> Category:
        r"""Lift Cat-level supercategories through the hom-category construction."""
        hom_supercategories = [
            super_category.HomCategory()
            for super_category in category.super_categories()
            if super_category in Cat()
        ]
        if not hom_supercategories:
            return HomCategory()
        return Category.join(hom_supercategories)

class HomCategoryOf(HomCategoryConstruction):
    r"""Generic category whose objects are ``Hom_C(A, B)``.

    Canonical chain: ``C.HomCategory()``.
    """

    # Sage axiom interop hook for _with_axiom("Endset").
    Endset = LazyImport("category_specs.homsets.endsets", "EndCategoryOf")

    # This is the category-level construction for a category C:
    # C.HomCategory() is the category whose objects are Hom_C(A, B).
    # Its Of(A, B) constructor evaluates the construction at objects A, B.
    # It does not define
    # set-map-only predicates such as injectivity.

    @override
    def _repr_object_names(self) -> str:
        base_category = self.base_category()
        if base_category in Cat().JoinCategories():
            object_names = " and ".join(category._repr_object_names() for category in base_category.super_categories())
        else:
            object_names = base_category._repr_object_names()
        return f"hom categories of {object_names}"

    class ParentMethods: ...
    class ElementMethods: ...
    class MorphismMethods: ...
