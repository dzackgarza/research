r"""Hom categories and morphism method surfaces."""

from __future__ import annotations

from abc import abstractmethod
from collections.abc import Callable
from typing import TYPE_CHECKING, final, override, TypeAlias

from sage.misc.lazy_import import LazyImport
from sage.structure.parent import Parent

from ..cat import Cat, Category, FunctorialConstructionCategory, _SageCategory
from ..cat import Homsets as SageHomsetsBase

if TYPE_CHECKING:
    from ..types import CategoryElement, CategoryObject, Hom, Morphism


def _category_class_declares_functor(category: Category, functor_name: str) -> bool:
    return any(functor_name in cls.__dict__ for cls in category.__class__.mro())


class UniversalHomObjectMethods:
    r"""Methods on objects ``Hom_C(A, B)`` of a hom category."""

    @abstractmethod
    def domain(self) -> CategoryObject:
        r"""Return the source object ``A`` of this hom object."""
        ...

    @abstractmethod
    def codomain(self) -> CategoryObject:
        r"""Return the target object ``B`` of this hom object."""
        ...

    def is_endomorphism_set(self) -> bool:
        r"""Return whether this hom object is an endomorphism object."""
        return bool(self.domain() == self.codomain())

    @abstractmethod
    def natural_map(self) -> Morphism:
        r"""Return the canonical coercion morphism carried by this hom object."""
        ...

    @abstractmethod
    def reversed(self) -> Hom:
        r"""Return ``Hom_C(B, A)`` for this ``Hom_C(A, B)`` object."""
        ...

    @abstractmethod
    def __call__(
        self, data: Morphism | Callable[[CategoryElement], CategoryElement]
    ) -> Morphism:
        r"""Coerce morphism data into this hom object."""
        ...


class UniversalHomElementMethods:
    r"""Methods on elements ``f`` of hom categories."""

    @abstractmethod
    def parent(self) -> UniversalHomObjectMethods:
        r"""Return the hom object containing this morphism."""
        ...

    @final
    def domain(self) -> CategoryObject:
        r"""Return the domain of this morphism."""
        return self.parent().domain()

    @final
    def codomain(self) -> CategoryObject:
        r"""Return the codomain of this morphism."""
        return self.parent().codomain()

    @abstractmethod
    def __call__(self, x: CategoryElement) -> CategoryElement:
        r"""Evaluate this morphism at ``x``."""
        ...

    @abstractmethod
    def image(self, domain_subset: CategoryObject | None = None) -> CategoryObject:
        r"""Return the image of ``domain_subset`` under this morphism."""
        ...

    @abstractmethod
    def pre_compose(self, other: Morphism) -> Morphism:
        r"""Return ``self`` after precomposition by ``other``."""
        ...

    @abstractmethod
    def post_compose(self, other: Morphism) -> Morphism:
        r"""Return ``self`` after postcomposition by ``other``."""
        ...

    def is_endomorphism(self) -> bool:
        r"""Return whether this morphism has equal domain and codomain."""
        return bool(self.domain() == self.codomain())

    @abstractmethod
    def is_identity(self) -> bool:
        r"""Return whether this morphism is an identity morphism."""
        ...

    @abstractmethod
    def equals_as_function(self, other: Morphism) -> bool:
        r"""Return whether this morphism and ``other`` agree extensionally."""
        ...

    @final
    def is_equal_function(self, other: Morphism) -> bool:
        r"""Sage-compatible spelling of extensional equality."""
        return self.equals_as_function(other)

    @abstractmethod
    def is_invertible(self) -> bool:
        r"""Return whether this morphism has a two-sided inverse."""
        ...

    @abstractmethod
    def is_isomorphism(self) -> bool:
        r"""Return whether this morphism is an isomorphism in its category."""
        ...

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
        super_categories: list[Category] = super().super_categories()
        return super_categories

    ParentMethods : TypeAlias = UniversalHomObjectMethods
    ElementMethods : TypeAlias = UniversalHomElementMethods

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

    ParentMethods : TypeAlias = UniversalHomObjectMethods
    ElementMethods : TypeAlias = UniversalHomElementMethods

    def Of(self, domain: CategoryObject, codomain: CategoryObject) -> Hom:
        r"""Return ``Hom_C(domain, codomain)`` for ``C = self.base_category()``."""
        category = self.base_category()
        assert domain in category, "domain must be an object of the base category"
        assert codomain in category, "codomain must be an object of the base category"
        hom: Hom = Parent.Hom(domain, codomain, category=category)
        return hom

    @classmethod
    def default_super_categories(cls, category: Category) -> Category:
        r"""Lift Cat-level supercategories through the hom-category construction."""
        hom_supercategories = [
            cls.category_of(super_category)
            for super_category in category.super_categories()
            if super_category in Cat()
            and _category_class_declares_functor(super_category, cls._functor_category)
        ]
        if not hom_supercategories:
            return HomCategory()
        return Cat().join(hom_supercategories)


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
            object_names = " and ".join(
                category._repr_object_names()
                for category in base_category.super_categories()
            )
        else:
            object_names = base_category._repr_object_names()
        return f"hom categories of {object_names}"

    ParentMethods : TypeAlias = UniversalHomObjectMethods
    ElementMethods : TypeAlias = UniversalHomElementMethods
