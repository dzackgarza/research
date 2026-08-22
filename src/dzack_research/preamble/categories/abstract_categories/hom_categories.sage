r"""The Hom, End, and Aut type towers of a category.

For a category \(\mathbf C\), C.HomCategory() is the category whose objects
are the hom categories \(\operatorname{Hom}_{\mathbf C}(X,Y)\). Its object
type is C.HomCatType. A hom category's objects are the arrows of \(\mathbf C\),
so its object type is C.ArrowType:

    C.HomCatType = C.HomCategory().ObjectType
    C.ArrowType = C.HomCatType.ObjectType = C.HomCatType.ElementType

The End, Mono, Epi, Iso, and Aut towers are the corresponding restricted
families.  Nothing in this module assumes local smallness.  No hom category
is defined as a set.
"""

from typing import TYPE_CHECKING

from sage.categories.objects import Objects
from sage.categories.category import Category as SageCategory
from sage.structure.element import Element as SageElement

from dzack_research.preamble.owned_category_bases import Category

if TYPE_CHECKING:
    from sage.structure.parent import Parent

    type ObjectOfCategory = Parent | SageCategory | SageElement


class _OverACategory:
    def __init__(self, base_category: SageCategory) -> None:
        self._base_category = base_category
        super().__init__()

    def base_category(self) -> SageCategory:
        return self._base_category

    def inherited_base_categories(self) -> list[SageCategory]:
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        return [
            super_category
            for super_category in self._base_category.super_categories()
            if super_category.category() is Cat()
        ]

    def __contains__(self, candidate: "ObjectOfCategory") -> bool:
        match candidate:
            case HomCategoryOf.ParentMethods():
                family = candidate.hom_category()
                return family is self or family.is_subcategory(self)
            case _:
                return False


class HomCategoryOf(_OverACategory, Category):
    r"""The category of hom categories of \(\mathbf C\)."""

    def _repr_(self) -> str:
        return f"Category of hom categories of {self._base_category}"

    def inherited_hom_category_families(self) -> list[Category]:
        r"""Return the Hom families inherited through super_categories."""
        return [
            super_category.HomCategory()
            for super_category in self.inherited_base_categories()
        ]

    def super_categories(self) -> list[Category]:
        inherited = self.inherited_hom_category_families()
        if inherited:
            return inherited
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        return [Cat()]

    def _object_type_of_object_type(self) -> type:
        r"""A hom category's objects are arrows."""
        return self.ElementType

    def Of(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        r"""Return \(\operatorname{Hom}_{\mathbf C}(X,Y)\)."""
        assert domain in self._base_category
        assert codomain in self._base_category
        return self.ObjectType(
            domain=domain,
            codomain=codomain,
            hom_category=self,
        )

    def Between(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        return self.Of(domain, codomain)

    class ParentMethods(Category):
        r"""The implementation of one category \(\operatorname{Hom}(X,Y)\)."""

        def __init__(
            self,
            domain: "ObjectOfCategory",
            codomain: "ObjectOfCategory",
            hom_category: "HomCategoryOf | EndCategoryOf | IsoCategoryOf | AutCategoryOf",
        ) -> None:
            self._domain = domain
            self._codomain = codomain
            self._hom_category = hom_category
            Category.__init__(self)

        def domain(self) -> "ObjectOfCategory":
            return self._domain

        def codomain(self) -> "ObjectOfCategory":
            return self._codomain

        def hom_category(
            self,
        ) -> "HomCategoryOf | EndCategoryOf | IsoCategoryOf | AutCategoryOf":
            return self._hom_category

        def base_category(self) -> SageCategory:
            return self._hom_category.base_category()

        def super_categories(self) -> list[Category]:
            inherited = self._hom_category.inherited_hom_category_families()
            if not inherited:
                return [Objects()]
            return [
                hom_category.Between(self._domain, self._codomain)
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

        def domain(self) -> "ObjectOfCategory":
            return self.hom_category().domain()

        def codomain(self) -> "ObjectOfCategory":
            return self.hom_category().codomain()

        def source(self) -> "ObjectOfCategory":
            return self.domain()

        def target(self) -> "ObjectOfCategory":
            return self.codomain()

        def __mul__(
            self,
            first: "HomCategoryOf.ElementMethods",
        ) -> "HomCategoryOf.ElementMethods":
            return self.base_category().compose(self, first)

        def is_endomorphism(self) -> bool:
            return self in self.base_category().EndArrowCategory()

        def is_isomorphism(self) -> bool:
            return self in self.base_category().IsomorphismArrowCategory()

        def is_automorphism(self) -> bool:
            return self in self.base_category().AutArrowCategory()

        def is_monomorphism(self) -> bool:
            return self in self.base_category().MonomorphismArrowCategory()

        def is_epimorphism(self) -> bool:
            return self in self.base_category().EpimorphismArrowCategory()


class HomCategoryConstruction(HomCategoryOf):
    r"""A category-specific Hom-family specialization."""

    def extra_super_categories(self) -> list[Category]:
        return []

    def inherited_hom_category_families(self) -> list[Category]:
        return [
            HomCategoryOf(self._base_category),
            *HomCategoryOf.inherited_hom_category_families(self),
        ]

    def super_categories(self) -> list[Category]:
        return [HomCategoryOf(self._base_category), *self.extra_super_categories()]


class EndCategoryOf(_OverACategory, Category):
    r"""The category of endomorphism categories of \(\mathbf C\)."""

    def _repr_(self) -> str:
        return f"Category of endomorphism categories of {self._base_category}"

    def super_categories(self) -> list[Category]:
        return self.inherited_hom_category_families()

    def inherited_hom_category_families(self) -> list[Category]:
        return [
            self._base_category.HomCategory(),
            *(
                category.EndCategory()
                for category in self.inherited_base_categories()
            ),
        ]

    def _object_type_of_object_type(self) -> type:
        return self.ElementType

    def Of(self, obj: "ObjectOfCategory") -> Category:
        r"""Return \(\operatorname{End}_{\mathbf C}(X)\)."""
        assert obj in self._base_category
        return self.ObjectType(
            domain=obj,
            codomain=obj,
            hom_category=self,
        )

    def Between(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        assert domain is codomain
        return self.Of(domain)

    class ElementMethods:
        def is_endomorphism(self) -> bool:
            return True


class MonoCategoryOf(_OverACategory, Category):
    r"""The category of monomorphism categories of \(\mathbf C\)."""

    def _repr_(self) -> str:
        return f"Category of monomorphism categories of {self._base_category}"

    def inherited_hom_category_families(self) -> list[Category]:
        return [
            self._base_category.HomCategory(),
            *(
                category.MonoCategory()
                for category in self.inherited_base_categories()
            ),
        ]

    def super_categories(self) -> list[Category]:
        return self.inherited_hom_category_families()

    def _object_type_of_object_type(self) -> type:
        return self.ElementType

    def Of(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        assert domain in self._base_category and codomain in self._base_category
        return self.ObjectType(
            domain=domain,
            codomain=codomain,
            hom_category=self,
        )

    def Between(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        return self.Of(domain, codomain)

    class ParentMethods:
        def __call__(
            self,
            underlying_arrow: "HomCategoryOf.ElementMethods",
        ) -> "MonoCategoryOf.ElementMethods":
            assert underlying_arrow in self.base_category().Hom(
                self.domain(),
                self.codomain(),
            )
            return self.ObjectType(
                hom_category=self,
                underlying_arrow=underlying_arrow,
            )

        def identity(self) -> "MonoCategoryOf.ElementMethods":
            assert self.domain() is self.codomain()
            return self(
                self.base_category().Hom(self.domain(), self.codomain()).identity()
            )

        def compose(
            self,
            second: "MonoCategoryOf.ElementMethods",
            first: "MonoCategoryOf.ElementMethods",
        ) -> "MonoCategoryOf.ElementMethods":
            assert first.codomain() is second.domain()
            return self(
                self.base_category().compose(
                    second.underlying_arrow(),
                    first.underlying_arrow(),
                )
            )

    class ElementMethods:
        def __init__(
            self,
            hom_category: Category,
            underlying_arrow: "HomCategoryOf.ElementMethods",
        ) -> None:
            self._underlying_arrow = underlying_arrow
            super().__init__(hom_category=hom_category)

        def underlying_arrow(self) -> "HomCategoryOf.ElementMethods":
            return self._underlying_arrow

        def is_monomorphism(self) -> bool:
            return True


class EpiCategoryOf(_OverACategory, Category):
    r"""The category of epimorphism categories of \(\mathbf C\)."""

    def _repr_(self) -> str:
        return f"Category of epimorphism categories of {self._base_category}"

    def inherited_hom_category_families(self) -> list[Category]:
        return [
            self._base_category.HomCategory(),
            *(
                category.EpiCategory()
                for category in self.inherited_base_categories()
            ),
        ]

    def super_categories(self) -> list[Category]:
        return self.inherited_hom_category_families()

    def _object_type_of_object_type(self) -> type:
        return self.ElementType

    def Of(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        assert domain in self._base_category and codomain in self._base_category
        return self.ObjectType(
            domain=domain,
            codomain=codomain,
            hom_category=self,
        )

    def Between(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        return self.Of(domain, codomain)

    class ParentMethods:
        def __call__(
            self,
            underlying_arrow: "HomCategoryOf.ElementMethods",
        ) -> "EpiCategoryOf.ElementMethods":
            assert underlying_arrow in self.base_category().Hom(
                self.domain(),
                self.codomain(),
            )
            return self.ObjectType(
                hom_category=self,
                underlying_arrow=underlying_arrow,
            )

        def identity(self) -> "EpiCategoryOf.ElementMethods":
            assert self.domain() is self.codomain()
            return self(
                self.base_category().Hom(self.domain(), self.codomain()).identity()
            )

        def compose(
            self,
            second: "EpiCategoryOf.ElementMethods",
            first: "EpiCategoryOf.ElementMethods",
        ) -> "EpiCategoryOf.ElementMethods":
            assert first.codomain() is second.domain()
            return self(
                self.base_category().compose(
                    second.underlying_arrow(),
                    first.underlying_arrow(),
                )
            )

    class ElementMethods:
        def __init__(
            self,
            hom_category: Category,
            underlying_arrow: "HomCategoryOf.ElementMethods",
        ) -> None:
            self._underlying_arrow = underlying_arrow
            super().__init__(hom_category=hom_category)

        def underlying_arrow(self) -> "HomCategoryOf.ElementMethods":
            return self._underlying_arrow

        def is_epimorphism(self) -> bool:
            return True


class IsoCategoryOf(_OverACategory, Category):
    r"""The category of isomorphism categories of \(\mathbf C\)."""

    def _repr_(self) -> str:
        return f"Category of isomorphism categories of {self._base_category}"

    def super_categories(self) -> list[Category]:
        return self.inherited_hom_category_families()

    def inherited_hom_category_families(self) -> list[Category]:
        return [
            self._base_category.HomCategory(),
            self._base_category.MonoCategory(),
            self._base_category.EpiCategory(),
            *(
                category.IsoCategory()
                for category in self.inherited_base_categories()
            ),
        ]

    def _object_type_of_object_type(self) -> type:
        return self.ElementType

    def Of(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        r"""Return the isomorphisms \(X\mathrel{\cong}Y\)."""
        assert domain in self._base_category
        assert codomain in self._base_category
        return self.ObjectType(
            domain=domain,
            codomain=codomain,
            hom_category=self,
        )

    def Between(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        return self.Of(domain, codomain)

    class ParentMethods:
        def __call__(
            self,
            forward: "HomCategoryOf.ElementMethods",
            backward: "HomCategoryOf.ElementMethods",
        ) -> "IsoCategoryOf.ElementMethods":
            category = self.base_category()
            assert forward in category.Hom(self.domain(), self.codomain())
            assert backward in category.Hom(self.codomain(), self.domain())
            return self.ObjectType(
                hom_category=self,
                forward=forward,
                backward=backward,
            )

        def identity(self) -> "IsoCategoryOf.ElementMethods":
            assert self.domain() is self.codomain(), (
                "an identity belongs to an endomorphism category"
            )
            identity_arrow = self.base_category().Hom(
                self.domain(), self.codomain()
            ).identity()
            return self(identity_arrow, identity_arrow)

        def compose(
            self,
            second: "IsoCategoryOf.ElementMethods",
            first: "IsoCategoryOf.ElementMethods",
        ) -> "IsoCategoryOf.ElementMethods":
            assert first.codomain() is second.domain()
            category = self.base_category()
            return self(
                category.compose(second.forward(), first.forward()),
                category.compose(
                    first.inverse().forward(),
                    second.inverse().forward(),
                ),
            )

    class ElementMethods:
        def __init__(
            self,
            hom_category: Category,
            forward: "HomCategoryOf.ElementMethods",
            backward: "HomCategoryOf.ElementMethods",
        ) -> None:
            self._forward_arrow = forward
            self._backward_arrow = backward
            super().__init__(hom_category=hom_category)

        def forward(self) -> "HomCategoryOf.ElementMethods":
            return self._forward_arrow

        def inverse(self) -> "IsoCategoryOf.ElementMethods":
            r"""Return the inverse isomorphism."""
            return self.base_category().Iso(self.codomain(), self.domain())(
                self._backward_arrow,
                self._forward_arrow,
            )

        def is_endomorphism(self) -> bool:
            return self.domain() is self.codomain()

        def is_isomorphism(self) -> bool:
            return True

        def is_automorphism(self) -> bool:
            return self.domain() is self.codomain()

        def is_monomorphism(self) -> bool:
            return True

        def is_epimorphism(self) -> bool:
            return True


class AutCategoryOf(_OverACategory, Category):
    r"""The category of automorphism categories of \(\mathbf C\)."""

    def _repr_(self) -> str:
        return f"Category of automorphism categories of {self._base_category}"

    def super_categories(self) -> list[Category]:
        return self.inherited_hom_category_families()

    def inherited_hom_category_families(self) -> list[Category]:
        return [
            self._base_category.EndCategory(),
            self._base_category.IsoCategory(),
            *(
                category.AutCategory()
                for category in self.inherited_base_categories()
            ),
        ]

    def _object_type_of_object_type(self) -> type:
        return self.ElementType

    def Of(self, obj: "ObjectOfCategory") -> Category:
        r"""Return \(\operatorname{Aut}_{\mathbf C}(X)\)."""
        assert obj in self._base_category
        return self.ObjectType(
            domain=obj,
            codomain=obj,
            hom_category=self,
        )

    def Between(
        self,
        domain: "ObjectOfCategory",
        codomain: "ObjectOfCategory",
    ) -> Category:
        assert domain is codomain
        return self.Of(domain)

    class ParentMethods:
        def identity(self) -> "AutCategoryOf.ElementMethods":
            identity_arrow = self.base_category().Hom(
                self.domain(), self.codomain()
            ).identity()
            return self(identity_arrow, identity_arrow)

        def compose(
            self,
            second: "AutCategoryOf.ElementMethods",
            first: "AutCategoryOf.ElementMethods",
        ) -> "AutCategoryOf.ElementMethods":
            return IsoCategoryOf.ParentMethods.compose(self, second, first)

    class ElementMethods:
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

    def inherited_hom_category_families(self) -> list[Category]:
        return [EndCategoryOf(self._base_category), *self.extra_super_categories()]

    def super_categories(self) -> list[Category]:
        return [EndCategoryOf(self._base_category), *self.extra_super_categories()]


class MonoCategoryConstruction(MonoCategoryOf):
    r"""A category-specific monomorphism-family specialization."""

    def extra_super_categories(self) -> list[Category]:
        return []

    def inherited_hom_category_families(self) -> list[Category]:
        return [MonoCategoryOf(self._base_category), *self.extra_super_categories()]

    def super_categories(self) -> list[Category]:
        return [MonoCategoryOf(self._base_category), *self.extra_super_categories()]


class EpiCategoryConstruction(EpiCategoryOf):
    r"""A category-specific epimorphism-family specialization."""

    def extra_super_categories(self) -> list[Category]:
        return []

    def inherited_hom_category_families(self) -> list[Category]:
        return [EpiCategoryOf(self._base_category), *self.extra_super_categories()]

    def super_categories(self) -> list[Category]:
        return [EpiCategoryOf(self._base_category), *self.extra_super_categories()]


class IsoCategoryConstruction(IsoCategoryOf):
    r"""A category-specific Iso-family specialization."""

    def extra_super_categories(self) -> list[Category]:
        return []

    def inherited_hom_category_families(self) -> list[Category]:
        return [IsoCategoryOf(self._base_category), *self.extra_super_categories()]

    def super_categories(self) -> list[Category]:
        return [IsoCategoryOf(self._base_category), *self.extra_super_categories()]


class AutCategoryConstruction(AutCategoryOf):
    r"""A category-specific Aut-family specialization."""

    def extra_super_categories(self) -> list[Category]:
        return []

    def inherited_hom_category_families(self) -> list[Category]:
        return [AutCategoryOf(self._base_category), *self.extra_super_categories()]

    def super_categories(self) -> list[Category]:
        return [AutCategoryOf(self._base_category), *self.extra_super_categories()]
