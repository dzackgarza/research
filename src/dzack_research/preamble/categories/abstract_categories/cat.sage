r"""``Cat``: the category whose objects are categories.

The constructions in this directory -- slices, arrows, diagrams, limits --
each take a category as their argument, so a category is the *object* they
are performed on and \(\mathbf{Cat}\) is where they are declared.  That is
what this module is: ``Cat.ParentMethods`` holds the constructions that every
category supports.  Each method delegates to the categorical owner.

A category reaches them by inheritance, through its own
``subcategory_class``: Sage sets a category's class to ``dynamic_class(name,
(cls, self.subcategory_class))`` and builds that from the super categories'
``subcategory_class``es, so ``dzack_research.preamble.owned_category`` ties
``Cat.ParentMethods`` in once at each owned root and every category below --
axiom categories, functorial constructions, and the ``JoinCategory``
instances Sage builds internally, which is what most owned categories
actually are -- inherits it.  Nothing is written on a Sage class, so a
Sage-native category correctly has none of this.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput

# Sage's ``Category``, not the owned base.  An owned base makes its category an
# object of ``Cat()``, and ``Cat()`` is not an object of itself.
from sage.categories.category import Category
from sage.categories.objects import Objects

from dzack_research.preamble.owned_category import OwnedCategoryMixin
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    ArrowCategory,
    Core,
    IsoArrowCategory,
)
from dzack_research.preamble.categories.abstract_categories.slice_categories import (
    CosliceUnderCategory,
    CoveredObjectCategory,
    CoveringObjectCategory,
    SliceOverCategory,
    SubobjectCategory,
    SuperobjectCategory,
)

if TYPE_CHECKING:
class Cat(OwnedCategoryMixin, Category):
    r"""The category \(\mathbf{Cat}\), whose objects are categories.

    Not an :class:`OwnedCategory`: \(\mathbf{Cat}\) is not an object of itself,
    so it takes the hook that ties it to its implementation classes without the
    Cat-object half that every category below it carries.
    """

    def _repr_(self) -> str:
        return "Category of categories"

    def super_categories(self) -> list[Category]:
        # A category is an object.  ``Objects()`` is where Sage declares
        # ``Homsets``/``Endsets``, which is how every ordinary category comes
        # by them -- so without this, ``Hom(C, D)`` between categories cannot
        # build its homset at all.
        return [Objects()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        r"""Return whether ``candidate`` is a category, hence an object here."""
        return isinstance(candidate, Category)

    class ParentMethods:
        r"""What a category \(\mathbf{C}\) can do because it is an object of
        \(\mathbf{Cat}\): construct the categories built out of it.

        ``self`` is a category here, which is what being an object of
        \(\mathbf{Cat}\) means; each construction is named for what it
        returns and hands the work to the class that already builds it.
        """

        def Arrow(self) -> Category:
            r"""Return \(\operatorname{Ar}(\mathbf{C})\), whose objects are the arrows of \(\mathbf{C}\)."""
            arrows: Category = ArrowCategory(self)
            return arrows

        def IsoArrow(self) -> Category:
            r"""Return the subcategory of \(\operatorname{Ar}(\mathbf{C})\) whose objects are the isomorphisms."""
            isomorphisms: Category = IsoArrowCategory(self)
            return isomorphisms

        def core(self) -> Category:
            r"""Return \(\operatorname{core}(\mathbf{C})\): the same objects, the isomorphisms as the only arrows."""
            core_category: Category = Core(self)
            return core_category

        def Diagram(self, index_category: Category) -> Category:
            r"""Return the functor category \([J,\mathbf{C}]\) of diagrams of shape \(J\)."""
            from dzack_research.preamble.categories.abstract_categories.functors import FunctorCategory

            diagrams: Category = FunctorCategory(index_category, self)
            return diagrams

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
            # Local: the functor-space module imports this one for ``Cat``,
            # so a module-level import here would close that cycle.
            from dzack_research.preamble.categories.abstract_categories.functors import FunctorSpace

            functor_space: "Parent" = FunctorSpace(self, codomain)
            return functor_space
