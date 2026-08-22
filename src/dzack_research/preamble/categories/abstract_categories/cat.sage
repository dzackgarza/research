r"""``Cat``: the category whose objects are categories.

The constructions in this directory -- slices, arrows, diagrams, limits --
each take a category as their argument, so a category is the *object* they
are performed on and \(\mathbf{Cat}\) is where they are declared.  That is
what this module is: ``Cat.ObjectType`` holds the constructions that every
category supports.  Each method delegates to the categorical owner.

A category reaches them by inheritance, through its own
``subcategory_class``: Sage sets a category's class to ``dynamic_class(name,
(cls, self.subcategory_class))`` and builds that from the super categories'
``subcategory_class``es, so ``dzack_research.preamble.owned_category`` ties
``Cat.ObjectType`` in once at each owned root and every category below --
axiom categories, functorial constructions, and the ``JoinCategory``
instances Sage builds internally, which is what most owned categories
actually are -- inherits it.  Nothing is written on a Sage class, so a
Sage-native category correctly has none of this.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from collections.abc import Callable, Iterable
    from sage.structure.element import Element as SageElement
    from sage.structure.parent import MembershipInput

    type ObjectOfCategory = Parent | Category | SageElement

# Sage's ``Category``, not the owned base.  An owned base makes its category an
# object of ``Cat()``, and ``Cat()`` is not an object of itself.
from sage.categories.category import Category
from sage.categories.objects import Objects
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.owned_category import (
    OwnedCategoryMixin,
    declared_implementation_types,
)
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    ArrowCategory as ArrowCategoryOf,
    AutomorphismArrowCategory as AutomorphismArrowCategoryOf,
    Core,
    EndArrowCategory as EndArrowCategoryOf,
    IsoArrowCategory,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    AutCategoryOf,
    EndCategoryOf,
    HomCategoryConstruction,
    HomCategoryOf,
    IsoCategoryConstruction,
    IsoCategoryOf,
)
from dzack_research.preamble.categories.abstract_categories.slice_categories import (
    CosliceUnderCategory,
    CoveredObjectCategory,
    CoveringObjectCategory,
    SliceOverCategory,
    SubobjectCategory,
    SuperobjectCategory,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    CoproductCategory,
    ProductCategory,
)


class Cat(OwnedCategoryMixin, Category):
    r"""The category \(\mathbf{Cat}\), whose objects are categories.

    Not an :class:`OwnedCategory`: \(\mathbf{Cat}\) is not an object of itself,
    so it takes the hook that ties it to its implementation classes without the
    Cat-object half that every category below it carries.
    """

    def _repr_(self) -> str:
        return "Category of categories"

    def super_categories(self) -> list[Category]:
        # A category is an object.  Hom, End, Aut, and arrow categories are
        # Cat-level constructions declared below, not consequences of this
        # Sage runtime edge.
        return [Objects()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        r"""Return whether ``candidate`` is a category, hence an object here."""
        match candidate:
            case Category():
                return True
            case _:
                return False

    class _HomCategory(HomCategoryOf):
        r"""The functor categories \([\mathbf C,\mathbf D]\).

        This declaration specializes the arrows of :math:`\mathbf{Cat}`.
        The generic Hom-family still constructs each functor category through
        ``HomCatType`` and makes its objects instances of ``ArrowType``.
        """

        class ParentMethods:
            def identity(self) -> "Cat.ArrowType":
                assert self.domain() is self.codomain(), (
                    "an identity functor belongs to an endomorphism category"
                )
                from dzack_research.preamble.categories.abstract_categories.functors import (
                    IdentityFunctor,
                )

                return IdentityFunctor(self.domain(), hom_category=self)

            def compose(
                self,
                second: "Cat.ArrowType",
                first: "Cat.ArrowType",
            ) -> "Cat.ArrowType":
                from dzack_research.preamble.categories.abstract_categories.functors import (
                    compose_functors,
                )

                assert first.codomain() is second.domain()
                assert self.domain() is first.domain()
                assert self.codomain() is second.codomain()
                return compose_functors(second, first, hom_category=self)

            class _HomCategory(HomCategoryConstruction):
                r"""Categories of natural transformations between functors."""

                class ParentMethods:
                    def __call__(
                        self,
                        components: "Callable[[ObjectOfCategory], HomCategoryOf.ElementMethods]",
                    ) -> "HomCategoryOf.ElementMethods":
                        return self.ObjectType(
                            hom_category=self,
                            components=components,
                        )

                    def identity(self) -> "HomCategoryOf.ElementMethods":
                        source = self.domain()
                        assert source is self.codomain(), (
                            "an identity transformation belongs to an endomorphism category"
                        )
                        return self(
                            lambda obj: source.codomain().identity(source(obj))
                        )

                    def compose(
                        self,
                        second: "HomCategoryOf.ElementMethods",
                        first: "HomCategoryOf.ElementMethods",
                    ) -> "HomCategoryOf.ElementMethods":
                        assert first.codomain() is second.domain()
                        return self(
                            lambda obj: second.component(obj)
                            * first.component(obj)
                        )

                class ElementMethods:
                    def __init__(
                        self,
                        hom_category: Category,
                        components: "Callable[[ObjectOfCategory], HomCategoryOf.ElementMethods]",
                    ) -> None:
                        self._components = components
                        super().__init__(hom_category=hom_category)

                    def component(
                        self,
                        obj: "ObjectOfCategory",
                    ) -> "HomCategoryOf.ElementMethods":
                        source = self.domain()
                        target = self.codomain()
                        assert obj in source.domain()
                        component = self._components(obj)
                        assert component in source.codomain().Hom(
                            source(obj), target(obj)
                        )
                        return component

            class _IsoCategory(IsoCategoryConstruction):
                r"""Natural isomorphisms as inverse natural transformations."""

                class ElementMethods:
                    def component(
                        self,
                        obj: "ObjectOfCategory",
                    ) -> "HomCategoryOf.ElementMethods":
                        return self.forward().component(obj)

        class ElementMethods:
            r"""The implementation common to functors."""

            _faithful: bool = False

            def __call__(
                self,
                value: "ObjectOfCategory | HomCategoryOf.ElementMethods",
            ) -> "ObjectOfCategory | HomCategoryOf.ElementMethods":
                if value in self.domain().ArrowCategory():
                    image = self._apply_functor_to_morphism(value)
                    assert image in self.codomain().ArrowCategory()
                    return image
                assert value in self.domain()
                image = self._apply_functor(value)
                assert image in self.codomain()
                return image

            def is_faithful(self) -> bool:
                return self._faithful

            def factors(self) -> tuple["Cat.ArrowType", ...]:
                return (self,)

            def _repr_(self) -> str:
                return f"Functor from {self.domain()} to {self.codomain()}"

    class _IsoCategory(IsoCategoryConstruction):
        r"""Invertible functors, represented by mutually inverse functors."""

        class ElementMethods:
            def __call__(
                self,
                value: "ObjectOfCategory | HomCategoryOf.ElementMethods",
            ) -> "ObjectOfCategory | HomCategoryOf.ElementMethods":
                return self.forward()(value)

            def factors(self) -> tuple["Cat.ArrowType", ...]:
                return self.forward().factors()

            def is_faithful(self) -> bool:
                return self.forward().is_faithful()

    class ParentMethods:
        r"""What a category \(\mathbf{C}\) can do because it is an object of
        \(\mathbf{Cat}\): construct the categories built out of it.

        ``self`` is a category here, which is what being an object of
        \(\mathbf{Cat}\) means; each construction is named for what it
        returns and hands the work to the class that already builds it.
        """

        @property
        def ObjectType(self) -> type:
            r"""Return the complete implementation type for objects of \(\mathbf{C}\)."""
            return self.parent_class

        @property
        def ElementType(self) -> type:
            r"""Return the complete implementation type for their elements."""
            return self.element_class

        @cached_method
        def HomCategory(self) -> Category:
            r"""Return the category of hom objects of \(\mathbf{C}\)."""
            construction, _ = declared_implementation_types(
                type(self), ("_HomCategory",)
            )
            if construction is None:
                return HomCategoryOf(self)
            return construction(self)

        @cached_method
        def EndCategory(self) -> Category:
            r"""Return the category of endomorphism objects of \(\mathbf{C}\)."""
            construction, _ = declared_implementation_types(
                type(self), ("_EndCategory",)
            )
            if construction is None:
                return EndCategoryOf(self)
            return construction(self)

        @cached_method
        def AutCategory(self) -> Category:
            r"""Return the category of automorphism objects of \(\mathbf{C}\)."""
            construction, _ = declared_implementation_types(
                type(self), ("_AutCategory",)
            )
            if construction is None:
                return AutCategoryOf(self)
            return construction(self)

        @cached_method
        def IsoCategory(self) -> Category:
            r"""Return the category of isomorphism categories of \(\mathbf{C}\)."""
            construction, _ = declared_implementation_types(
                type(self), ("_IsoCategory",)
            )
            if construction is None:
                return IsoCategoryOf(self)
            return construction(self)

        @property
        def HomCatType(self) -> type:
            return self.HomCategory().ObjectType

        @property
        def EndCatType(self) -> type:
            return self.EndCategory().ObjectType

        @property
        def AutCatType(self) -> type:
            return self.AutCategory().ObjectType

        @property
        def IsoCatType(self) -> type:
            return self.IsoCategory().ObjectType

        @property
        def ArrowType(self) -> type:
            return self.HomCatType.ObjectType

        @property
        def EndArrowType(self) -> type:
            return self.EndCatType.ObjectType

        @property
        def AutArrowType(self) -> type:
            return self.AutCatType.ObjectType

        @property
        def IsoArrowType(self) -> type:
            return self.IsoCatType.ObjectType

        @cached_method
        def ArrowCategory(self) -> Category:
            r"""Return \(\operatorname{Ar}(\mathbf{C})\), whose objects are the arrows of \(\mathbf{C}\)."""
            arrows: Category = ArrowCategoryOf(self)
            return arrows

        @cached_method
        def EndArrowCategory(self) -> Category:
            r"""Return the full subcategory of \(\operatorname{Ar}(\mathbf{C})\) on endomorphisms."""
            endomorphisms: Category = EndArrowCategoryOf(self)
            return endomorphisms

        @cached_method
        def IsomorphismArrowCategory(self) -> Category:
            r"""Return the subcategory of \(\operatorname{Ar}(\mathbf{C})\) whose objects are the isomorphisms."""
            isomorphisms: Category = IsoArrowCategory(self)
            return isomorphisms

        @cached_method
        def AutArrowCategory(self) -> Category:
            r"""Return the full subcategory of \(\operatorname{Ar}(\mathbf{C})\) on automorphisms."""
            automorphisms: Category = AutomorphismArrowCategoryOf(self)
            return automorphisms

        @cached_method
        def core(self) -> Category:
            r"""Return \(\operatorname{core}(\mathbf{C})\): the same objects, the isomorphisms as the only arrows."""
            core_category: Category = Core(self)
            return core_category

        def Diagram(self, index_category: Category) -> Category:
            r"""Return the functor category \([J,\mathbf{C}]\) of diagrams of shape \(J\)."""
            return index_category.FunctorCategory(self)

        @cached_method
        def DiagonalFunctor(self, index_category: Category) -> "Cat.ArrowType":
            r"""Return \(\Delta:\mathbf C\to[J,\mathbf C]\)."""
            from dzack_research.preamble.categories.abstract_categories.functors import (
                DiagonalFunctor,
            )

            return DiagonalFunctor(self, index_category)

        def FunctorCategory(self, codomain: Category) -> Category:
            r"""Return the functor category \(\operatorname{Fun}(\mathbf{C},\mathbf{D})\)."""
            return Cat().Hom(self, codomain)

        def ImageOf(self, functor: "Cat.ArrowType") -> Category:
            r"""Return the image category of a functor with codomain ``self``."""
            assert functor in Cat().ArrowCategory()
            assert functor.codomain() is self
            return functor.Image()

        @cached_method
        def Hom(
            self,
            source: "ObjectOfCategory",
            target: "ObjectOfCategory",
        ) -> Category:
            r"""Return \(\operatorname{Hom}_{\mathbf{C}}(X,Y)\)."""
            assert source in self and target in self
            return self.HomCategory().Of(source, target)

        @cached_method
        def End(self, obj: "ObjectOfCategory") -> Category:
            r"""Return \(\operatorname{End}_{\mathbf{C}}(X)\)."""
            assert obj in self
            return self.EndCategory().Of(obj)

        @cached_method
        def Aut(self, obj: "ObjectOfCategory") -> Category:
            r"""Return \(\operatorname{Aut}_{\mathbf{C}}(X)\)."""
            assert obj in self
            return self.AutCategory().Of(obj)

        @cached_method
        def Iso(
            self,
            source: "ObjectOfCategory",
            target: "ObjectOfCategory",
        ) -> Category:
            r"""Return the isomorphism category from ``source`` to ``target``."""
            assert source in self and target in self
            return self.IsoCategory().Of(source, target)

        def identity(
            self,
            obj: "ObjectOfCategory",
        ) -> "HomCategoryOf.ElementMethods":
            r"""Return the identity arrow of ``obj``."""
            return self.Aut(obj).identity()

        def compose(
            self,
            second: "HomCategoryOf.ElementMethods",
            first: "HomCategoryOf.ElementMethods",
        ) -> "HomCategoryOf.ElementMethods":
            r"""Return ``second`` after ``first`` through their Hom category."""
            assert first in self.ArrowCategory()
            assert second in self.ArrowCategory()
            assert first.codomain() is second.domain(), (
                "arrows compose only when their middle object agrees"
            )
            return self.Hom(first.domain(), second.codomain()).compose(
                second,
                first,
            )

        def Product(self, factors: "Iterable[Parent]") -> Category:
            r"""Return the category of product cones on the given objects."""
            products: Category = ProductCategory(self, factors)
            return products

        def Coproduct(self, cofactors: "Iterable[Parent]") -> Category:
            r"""Return the category of coproduct cocones on the given objects."""
            coproducts: Category = CoproductCategory(self, cofactors)
            return coproducts

        def SliceOver(self, X: "Parent | Morphism") -> Category:
            r"""Return the slice category \(\mathbf{C}/X\), whose objects are the arrows \(A\to X\)."""
            slices: Category = SliceOverCategory(self, X)
            return slices

        def CosliceUnder(self, X: "Parent | Morphism") -> Category:
            r"""Return the coslice category \(X\setminus\mathbf{C}\), whose objects are the arrows \(X\to A\)."""
            coslices: Category = CosliceUnderCategory(self, X)
            return coslices

        def SubObject(self, X: "Parent | Morphism") -> Category:
            r"""Return the category of subobjects of \(X\): the monomorphisms \(A\hookrightarrow X\)."""
            subobjects: Category = SubobjectCategory(self, X)
            return subobjects

        def SuperObject(self, X: "Parent | Morphism") -> Category:
            r"""Return the category of superobjects of \(X\): the monomorphisms \(X\hookrightarrow B\)."""
            superobjects: Category = SuperobjectCategory(self, X)
            return superobjects

        def CoveringObject(self, X: "Parent | Morphism") -> Category:
            r"""Return the category of covering objects of \(X\): the epimorphisms \(A\twoheadrightarrow X\)."""
            coverings: Category = CoveringObjectCategory(self, X)
            return coverings

        def CoveredObject(self, X: "Parent | Morphism") -> Category:
            r"""Return the category of covered objects of \(X\): the epimorphisms \(X\twoheadrightarrow B\)."""
            covereds: Category = CoveredObjectCategory(self, X)
            return covereds

        def _Hom_(self, codomain: Category, category: "Category | None" = None) -> "Parent":
            r"""Return \(\operatorname{Hom}_{\mathbf{Cat}}(\mathbf{C},\mathbf{D})=\operatorname{Fun}(\mathbf{C},\mathbf{D})\).

            Sage's ``Hom(C, D)`` between two categories dispatches here, so
            the Hom category of \(\mathbf{Cat}\) is the functor category, not
            the generic id-equality fallback.
            """
            return Cat().Hom(self, codomain)
