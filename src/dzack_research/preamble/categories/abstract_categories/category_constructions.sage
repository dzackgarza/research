r"""Opposite categories and binary products of categories.

These are constructions in :math:`\mathbf{Cat}`.  They supply the domain
categories for contravariant functors and bifunctors.  Objects of
``ProductCategory(C, D)`` are pairs, and its arrows are pairs of arrows.
Objects of ``OppositeCategory(C)`` are the objects of ``C``.  Its arrows wrap
arrows of ``C`` with their direction reversed.

The representations follow the mature implementations in Mathlib,
``Mathlib/CategoryTheory/Opposites.lean`` and
``Mathlib/CategoryTheory/Products/Basic.lean``: opposite composition reverses
the underlying composition, while product identities and composition operate
componentwise.
"""

from typing import TYPE_CHECKING

from sage.categories.category import Category as SageCategory
from sage.categories.objects import Objects
from sage.structure.element import Element as SageElement

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
)
from dzack_research.preamble.owned_category_bases import CategoryWithParameters

if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput, Parent as SageParent

    from dzack_research.preamble.categories.abstract_categories.hom_categories import (
        HomCategoryOf,
    )

    type ObjectOfCategory = SageParent | SageCategory | SageElement


class _OnACategory:
    def __init__(self, base_category: SageCategory) -> None:
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        assert base_category in Cat()
        self._base_category = base_category
        super().__init__()

    def base_category(self) -> SageCategory:
        return self._base_category

    def _make_named_class_key(self, name: str) -> SageCategory:
        return self._base_category


class OppositeCategory(_OnACategory, CategoryWithParameters):
    r"""The category :math:`\mathbf C^{\mathrm{op}}`."""

    @property
    def ObjectType(self) -> type:
        return self._base_category.ObjectType

    @property
    def ElementType(self) -> type:
        return self._base_category.ElementType

    def super_categories(self) -> list[SageCategory]:
        inherited = [
            category.OppositeCategory()
            for category in self._base_category.super_categories()
            if category.category() is self.category()
        ]
        return inherited or [Objects()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return candidate in self._base_category

    def OppositeCategory(self) -> SageCategory:
        r"""Return :math:`(\mathbf C^{\mathrm{op}})^{\mathrm{op}}=\mathbf C`."""
        return self._base_category

    def _repr_(self) -> str:
        return f"Opposite of {self._base_category}"

    class _HomCategory(HomCategoryConstruction):
        class ElementMethods:
            def __init__(
                self,
                hom_category: SageCategory,
                underlying_arrow: "HomCategoryOf.ElementMethods",
            ) -> None:
                base_category = hom_category.base_category().base_category()
                assert underlying_arrow in base_category.Hom(
                    hom_category.codomain(),
                    hom_category.domain(),
                )
                self._underlying_arrow = underlying_arrow
                super().__init__(hom_category=hom_category)

            def underlying_arrow(self) -> "HomCategoryOf.ElementMethods":
                return self._underlying_arrow

        class ParentMethods:
            def __call__(
                self,
                underlying_arrow: "HomCategoryOf.ElementMethods",
            ) -> "HomCategoryOf.ElementMethods":
                base_category = self.base_category().base_category()
                assert underlying_arrow in base_category.Hom(
                    self.codomain(),
                    self.domain(),
                )
                return self.ObjectType(
                    hom_category=self,
                    underlying_arrow=underlying_arrow,
                )

            def identity(self) -> "HomCategoryOf.ElementMethods":
                assert self.domain() is self.codomain()
                base_category = self.base_category().base_category()
                return self(base_category.identity(self.domain()))

            def compose(
                self,
                second: "HomCategoryOf.ElementMethods",
                first: "HomCategoryOf.ElementMethods",
            ) -> "HomCategoryOf.ElementMethods":
                assert first.codomain() is second.domain()
                base_category = self.base_category().base_category()
                return self(
                    base_category.compose(
                        first.underlying_arrow(),
                        second.underlying_arrow(),
                    )
                )


class _OfTwoCategories:
    def __init__(
        self,
        first_category: SageCategory,
        second_category: SageCategory,
    ) -> None:
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        assert first_category in Cat() and second_category in Cat()
        self._first_category = first_category
        self._second_category = second_category
        super().__init__()

    def first_category(self) -> SageCategory:
        return self._first_category

    def second_category(self) -> SageCategory:
        return self._second_category

    def _make_named_class_key(self, name: str) -> tuple[SageCategory, SageCategory]:
        return self._first_category, self._second_category


class ProductCategory(_OfTwoCategories, CategoryWithParameters):
    r"""The product category :math:`\mathbf C\times\mathbf D`."""

    def super_categories(self) -> list[SageCategory]:
        return [Objects()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        try:
            return candidate.parent() is self
        except AttributeError:
            return False

    def pair(
        self,
        first: "ObjectOfCategory",
        second: "ObjectOfCategory",
    ) -> SageElement:
        assert first in self._first_category
        assert second in self._second_category
        return self.ObjectType(parent=self, first=first, second=second)

    def __call__(
        self,
        first: "ObjectOfCategory",
        second: "ObjectOfCategory",
    ) -> SageElement:
        return self.pair(first, second)

    def _repr_(self) -> str:
        return f"Product of {self._first_category} and {self._second_category}"

    class ParentMethods(SageElement):
        def __init__(
            self,
            parent: "ProductCategory",
            first: "ObjectOfCategory",
            second: "ObjectOfCategory",
        ) -> None:
            assert first in parent.first_category()
            assert second in parent.second_category()
            self._first = first
            self._second = second
            SageElement.__init__(self, parent)

        def first(self) -> "ObjectOfCategory":
            return self._first

        def second(self) -> "ObjectOfCategory":
            return self._second

        def _repr_(self) -> str:
            return f"({self._first}, {self._second})"

    class _HomCategory(HomCategoryConstruction):
        class ElementMethods:
            def __init__(
                self,
                hom_category: SageCategory,
                first: "HomCategoryOf.ElementMethods",
                second: "HomCategoryOf.ElementMethods",
            ) -> None:
                product = hom_category.base_category()
                assert first in product.first_category().Hom(
                    hom_category.domain().first(),
                    hom_category.codomain().first(),
                )
                assert second in product.second_category().Hom(
                    hom_category.domain().second(),
                    hom_category.codomain().second(),
                )
                self._first = first
                self._second = second
                super().__init__(hom_category=hom_category)

            def first(self) -> "HomCategoryOf.ElementMethods":
                return self._first

            def second(self) -> "HomCategoryOf.ElementMethods":
                return self._second

        class ParentMethods:
            def __call__(
                self,
                first: "HomCategoryOf.ElementMethods",
                second: "HomCategoryOf.ElementMethods",
            ) -> "HomCategoryOf.ElementMethods":
                return self.ObjectType(
                    hom_category=self,
                    first=first,
                    second=second,
                )

            def identity(self) -> "HomCategoryOf.ElementMethods":
                assert self.domain() is self.codomain()
                product = self.base_category()
                return self(
                    product.first_category().identity(self.domain().first()),
                    product.second_category().identity(self.domain().second()),
                )

            def compose(
                self,
                second: "HomCategoryOf.ElementMethods",
                first: "HomCategoryOf.ElementMethods",
            ) -> "HomCategoryOf.ElementMethods":
                assert first.codomain() is second.domain()
                product = self.base_category()
                return self(
                    product.first_category().compose(second.first(), first.first()),
                    product.second_category().compose(second.second(), first.second()),
                )
