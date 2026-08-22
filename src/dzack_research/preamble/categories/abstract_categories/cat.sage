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
    from collections.abc import Iterable
    from sage.structure.parent import MembershipInput

# Sage's ``Category``, not the owned base.  An owned base makes its category an
# object of ``Cat()``, and ``Cat()`` is not an object of itself.
from sage.categories.category import Category
from sage.categories.objects import Objects

from dzack_research.preamble.owned_category import (
    OwnedCategoryMixin,
    declared_implementation_types,
    object_of,
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
    HomCategoryOf,
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
        return isinstance(candidate, Category)

    def _hom_object(
        self,
        source: Category,
        target: Category,
        hom_category: Category,
    ) -> Category:
        r"""Construct \(\operatorname{Hom}_{\mathbf{Cat}}(C,D)=[C,D]\)."""
        return source.FunctorCategory(target)

    class _HomCategory(HomCategoryOf):
        r"""Functor categories as the hom objects of \(\mathbf{Cat}\)."""

        @property
        def ObjectType(self) -> type:
            from dzack_research.preamble.categories.abstract_categories.functors import (
                FunctorCategory,
            )

            return FunctorCategory

        def Of(self, source: Category, target: Category) -> Category:
            return source.FunctorCategory(target)

        def _object(
            self,
            source: Category,
            target: Category,
            placement: Category,
        ) -> Category:
            return source.FunctorCategory(target)

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

        def HomCategory(self) -> Category:
            r"""Return the category of hom objects of \(\mathbf{C}\)."""
            construction, _ = declared_implementation_types(
                type(self), ("_HomCategory",)
            )
            if construction is None:
                return HomCategoryOf(self)
            return construction(self)

        def EndCategory(self) -> Category:
            r"""Return the category of endomorphism objects of \(\mathbf{C}\)."""
            construction, _ = declared_implementation_types(
                type(self), ("_EndCategory",)
            )
            if construction is None:
                return EndCategoryOf(self)
            return construction(self)

        def AutCategory(self) -> Category:
            r"""Return the category of automorphism objects of \(\mathbf{C}\)."""
            construction, _ = declared_implementation_types(
                type(self), ("_AutCategory",)
            )
            if construction is None:
                return AutCategoryOf(self)
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
        def ArrowType(self) -> type:
            return self.HomCatType.ElementType

        @property
        def EndArrowType(self) -> type:
            return self.EndCatType.ElementType

        @property
        def AutArrowType(self) -> type:
            return self.AutCatType.ElementType

        def ArrowCategory(self) -> Category:
            r"""Return \(\operatorname{Ar}(\mathbf{C})\), whose objects are the arrows of \(\mathbf{C}\)."""
            arrows: Category = ArrowCategoryOf(self)
            return arrows

        def EndArrowCategory(self) -> Category:
            r"""Return the full subcategory of \(\operatorname{Ar}(\mathbf{C})\) on endomorphisms."""
            endomorphisms: Category = EndArrowCategoryOf(self)
            return endomorphisms

        def IsomorphismArrowCategory(self) -> Category:
            r"""Return the subcategory of \(\operatorname{Ar}(\mathbf{C})\) whose objects are the isomorphisms."""
            isomorphisms: Category = IsoArrowCategory(self)
            return isomorphisms

        def AutArrowCategory(self) -> Category:
            r"""Return the full subcategory of \(\operatorname{Ar}(\mathbf{C})\) on automorphisms."""
            automorphisms: Category = AutomorphismArrowCategoryOf(self)
            return automorphisms

        def core(self) -> Category:
            r"""Return \(\operatorname{core}(\mathbf{C})\): the same objects, the isomorphisms as the only arrows."""
            core_category: Category = Core(self)
            return core_category

        def Diagram(self, index_category: Category) -> Category:
            r"""Return the functor category \([J,\mathbf{C}]\) of diagrams of shape \(J\)."""
            return index_category.FunctorCategory(self)

        def FunctorCategory(self, codomain: Category) -> Category:
            r"""Return the functor category \(\operatorname{Fun}(\mathbf{C},\mathbf{D})\)."""
            from dzack_research.preamble.categories.abstract_categories.functors import FunctorCategory

            functors: Category = FunctorCategory(self, codomain)
            return functors

        def Hom(self, source: Parent, target: Parent) -> Parent:
            r"""Return \(\operatorname{Hom}_{\mathbf{C}}(X,Y)\)."""
            assert source in self and target in self
            return self.HomCategory().Of(source, target)

        def End(self, obj: Parent) -> Parent:
            r"""Return \(\operatorname{End}_{\mathbf{C}}(X)\)."""
            assert obj in self
            return self.EndCategory().Of(obj)

        def Aut(self, obj: Parent) -> Parent:
            r"""Return \(\operatorname{Aut}_{\mathbf{C}}(X)\)."""
            assert obj in self
            return self.AutCategory().Of(obj)

        def _hom_object(
            self,
            source: Parent,
            target: Parent,
            hom_category: Category,
        ) -> Parent:
            r"""Construct a hom object through its category-owned type."""
            return object_of(
                hom_category,
                source=source,
                target=target,
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
            the homset of \(\mathbf{Cat}\) is the functor space rather than
            the generic id-equality fallback.
            """
            return self.FunctorCategory(codomain)
