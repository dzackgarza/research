r"""The Hom, End, and Aut type towers of a category.

For a category \(\mathbf C\), C.HomCategory() is the category whose objects
are the hom categories \(\operatorname{Hom}_{\mathbf C}(X,Y)\). Its object
type is C.HomCatType. A hom category's objects are the arrows of \(\mathbf C\),
so its object type is C.ArrowType:

    C.HomCatType = C.HomCategory().ObjectType
    C.ArrowType = C.HomCatType.ObjectType

The End and Aut towers are the corresponding restricted families. Nothing
in this module assumes local smallness. No hom category is defined as a set.
"""

from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING

from sage.categories.objects import Objects
from sage.structure.element import Element as SageElement

from dzack_research.preamble.owned_category_bases import Category

if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.structure.parent import Parent


class _OverACategory:
    def __init__(self, base_category: Category) -> None:
        self._base_category = base_category
        super().__init__()

    def base_category(self) -> Category:
        return self._base_category


class HomCategoryOf(_OverACategory, Category):
    r"""The category of hom categories of \(\mathbf C\)."""

    def _repr_(self) -> str:
        return f"Category of hom categories of {self._base_category}"

    def inherited_hom_categories(self) -> list[Category]:
        r"""Return the Hom families inherited through super_categories."""
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        return [
            super_category.HomCategory()
            for super_category in self._base_category.super_categories()
            if super_category.category() is Cat()
        ]

    def super_categories(self) -> list[Category]:
        inherited = self.inherited_hom_categories()
        return inherited if inherited else [Objects()]

    def _object_type_of_object_type(self) -> type:
        r"""A hom category's objects are arrows."""
        return self.ElementType

    def Of(self, domain: "Parent", codomain: "Parent") -> Category:
        r"""Return \(\operatorname{Hom}_{\mathbf C}(X,Y)\)."""
        assert domain in self._base_category
        assert codomain in self._base_category
        return self.ObjectType(
            domain=domain,
            codomain=codomain,
            hom_category=self,
        )

    class ParentMethods(Category):
        r"""The implementation of one category \(\operatorname{Hom}(X,Y)\)."""

        def __init__(
            self,
            domain: "Parent",
            codomain: "Parent",
            hom_category: HomCategoryOf,
            **rest: "ConstructionData",
        ) -> None:
            self._domain = domain
            self._codomain = codomain
            self._hom_category = hom_category
            Category.__init__(self)

        def domain(self) -> "Parent":
            return self._domain

        def codomain(self) -> "Parent":
            return self._codomain

        def hom_category(self) -> HomCategoryOf:
            return self._hom_category

        def base_category(self) -> Category:
            return self._hom_category.base_category()

        def super_categories(self) -> list[Category]:
            inherited = self._hom_category.inherited_hom_categories()
            if not inherited:
                return [Objects()]
            return [
                hom_category.Of(self._domain, self._codomain)
                for hom_category in inherited
            ]

        def __contains__(self, arrow: "HomCategoryOf.ElementMethods") -> bool:
            return arrow.parent() is self

        def __call__(
            self,
            arrow: "HomCategoryOf.ElementMethods",
        ) -> "HomCategoryOf.ElementMethods":
            assert arrow in self
            return arrow

        def _repr_(self) -> str:
            return (
                f"Hom category from {self._domain} to {self._codomain} "
                f"in {self.base_category()}"
            )

    class ElementMethods(SageElement):
        r"""The implementation common to every arrow."""

        def __init__(self, hom_category: Category) -> None:
            SageElement.__init__(self, hom_category)

        def hom_category(self) -> Category:
            return self.parent()

        def base_category(self) -> Category:
            return self.hom_category().base_category()

        def domain(self) -> "Parent":
            return self.hom_category().domain()

        def codomain(self) -> "Parent":
            return self.hom_category().codomain()

        def is_endomorphism(self) -> bool:
            return self in self.base_category().EndArrowCategory()

        def is_isomorphism(self) -> bool:
            return self in self.base_category().IsomorphismArrowCategory()

        def is_automorphism(self) -> bool:
            return self in self.base_category().AutArrowCategory()


class EndCategoryOf(_OverACategory, Category):
    r"""The category of endomorphism categories of \(\mathbf C\)."""

    def _repr_(self) -> str:
        return f"Category of endomorphism categories of {self._base_category}"

    def super_categories(self) -> list[Category]:
        return [self._base_category.HomCategory()]

    def _object_type_of_object_type(self) -> type:
        return self.ElementType

    def Of(self, obj: "Parent") -> Category:
        r"""Return \(\operatorname{End}_{\mathbf C}(X)\)."""
        assert obj in self._base_category
        return self.ObjectType(
            domain=obj,
            codomain=obj,
            hom_category=self,
        )

    class ElementMethods:
        def is_endomorphism(self) -> bool:
            return True


class AutCategoryOf(_OverACategory, Category):
    r"""The category of automorphism categories of \(\mathbf C\)."""

    def _repr_(self) -> str:
        return f"Category of automorphism categories of {self._base_category}"

    def super_categories(self) -> list[Category]:
        return [self._base_category.EndCategory()]

    def _object_type_of_object_type(self) -> type:
        return self.ElementType

    def Of(self, obj: "Parent") -> Category:
        r"""Return \(\operatorname{Aut}_{\mathbf C}(X)\)."""
        assert obj in self._base_category
        return self.ObjectType(
            domain=obj,
            codomain=obj,
            hom_category=self,
        )

    class ElementMethods(metaclass=ABCMeta):
        @abstractmethod
        def inverse(self) -> "AutCategoryOf.ElementMethods":
            r"""Return the inverse automorphism."""

        def is_endomorphism(self) -> bool:
            return True

        def is_isomorphism(self) -> bool:
            return True

        def is_automorphism(self) -> bool:
            return True


class EndCategoryConstruction(EndCategoryOf):
    r"""A category-specific End-family specialization."""

    def extra_super_categories(self) -> list[Category]:
        return []

    def super_categories(self) -> list[Category]:
        return [EndCategoryOf(self._base_category), *self.extra_super_categories()]


class AutCategoryConstruction(AutCategoryOf):
    r"""A category-specific Aut-family specialization."""

    def extra_super_categories(self) -> list[Category]:
        return []

    def super_categories(self) -> list[Category]:
        return [AutCategoryOf(self._base_category), *self.extra_super_categories()]
