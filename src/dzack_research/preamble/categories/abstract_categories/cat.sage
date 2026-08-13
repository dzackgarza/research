r"""``Cat``: the category whose objects are categories.

The constructions in this directory -- slices, arrows, diagrams, limits --
each take a category as their argument, so a category is the *object* they
are performed on and \(\mathbf{Cat}\) is where they are declared.  That is
what this module is: ``Cat.ParentMethods`` holds all twenty-one of them as
the methods an object of \(\mathbf{Cat}\) has, and each one delegates to the
owned class that already builds the construction.

Sage seats an object of a category in a ``Parent``, and a Sage category is
not one -- it is an instance of Sage's ``Category``.  So a session reaches
these constructions through that class, and the bottom of this file is the
one place where they are attached to it.  The declaration home is
``Cat.ParentMethods``; the attachment is a single loop over what is declared
there, and nothing is written on Sage's class that was not declared here
first.
"""

from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    ArrowCategory,
    Core,
    IsoArrowCategory,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    BiproductCategory,
    CoconeCategory,
    ConeCategory,
    CoproductCategory,
    DiagramCategory,
    DirectSumCategory,
    DirectedSystem,
    InverseSystem,
    ProductCategory,
    TensorProductCategory,
)
from dzack_research.preamble.categories.abstract_categories.slice_categories import (
    CokernelCategory,
    CosliceUnderCategory,
    CoveredObjectCategory,
    CoveringObjectCategory,
    KernelCategory,
    SliceOverCategory,
    SubobjectCategory,
    SuperobjectCategory,
)

if TYPE_CHECKING:
    from collections.abc import Iterable

    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet


class Cat(Category):
    r"""The category \(\mathbf{Cat}\), whose objects are categories."""

    def _repr_(self) -> str:
        return "Category of categories"

    def super_categories(self) -> list[Category]:
        # A category is not a set, so nothing above this holds its objects.
        return []

    def __contains__(self, candidate: object) -> bool:
        r"""Return whether ``candidate`` is a category, hence an object here."""
        return isinstance(candidate, Category)

    class ParentMethods:
        r"""What a category \(\mathbf{C}\) can do because it is an object of
        \(\mathbf{Cat}\): construct the categories built out of it."""

        def Arrow(self: Category) -> Category:
            r"""Return \(\operatorname{Ar}(\mathbf{C})\), whose objects are the arrows of \(\mathbf{C}\)."""
            return ArrowCategory(self)

        def IsoArrow(self: Category) -> Category:
            r"""Return the subcategory of \(\operatorname{Ar}(\mathbf{C})\) whose objects are the isomorphisms."""
            return IsoArrowCategory(self)

        def core(self: Category) -> Category:
            r"""Return \(\operatorname{core}(\mathbf{C})\): the same objects, the isomorphisms as the only arrows."""
            return Core(self)

        def Diagram(
            self: Category,
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of diagrams \(F:J\to\mathbf{C}\) on these objects and morphisms."""
            return DiagramCategory(self, objects, morphisms)

        def DirectedSystem(
            self: Category,
            index_set: "OrderedSet",
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of directed systems \((X_i)_{i\in I}\) with morphisms \(X_i\to X_j\)."""
            return DirectedSystem(self, index_set, objects, morphisms)

        def InverseSystem(
            self: Category,
            index_set: "OrderedSet",
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of inverse systems \((X_i)_{i\in I}\) with morphisms \(X_j\to X_i\)."""
            return InverseSystem(self, index_set, objects, morphisms)

        def Cone(
            self: Category,
            index_set: "OrderedSet",
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of cones: an apex \(A\) with projections \(\pi_i:A\to X_i\)."""
            return ConeCategory(self, index_set, objects, morphisms)

        def Cocone(
            self: Category,
            index_set: "OrderedSet",
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of cocones: a coapex \(A\) with injections \(\iota_i:X_i\to A\)."""
            return CoconeCategory(self, index_set, objects, morphisms)

        def Product(self: Category, factors: "Iterable[Parent]") -> Category:
            r"""Return the category of products \(\prod_i X_i\) of these factors."""
            return ProductCategory(self, factors)

        def Coproduct(self: Category, cofactors: "Iterable[Parent]") -> Category:
            r"""Return the category of coproducts \(\coprod_i X_i\) of these cofactors."""
            return CoproductCategory(self, cofactors)

        def Biproduct(self: Category, factors: "Iterable[Parent]") -> Category:
            r"""Return the category of biproducts of these factors: product and coproduct at once."""
            return BiproductCategory(self, factors)

        def DirectSum(self: Category, factors: "Iterable[Parent]") -> Category:
            r"""Return the category of direct sums \(\bigoplus_i X_i\), the additive name for the biproduct."""
            return DirectSumCategory(self, factors)

        def TensorProduct(self: Category, factors: "Iterable[Parent]") -> Category:
            r"""Return the category of tensor products \(X_1\otimes\cdots\otimes X_n\) of these factors."""
            return TensorProductCategory(self, factors)

        def SliceOver(self: Category, X: "Parent | Morphism") -> Category:
            r"""Return the slice category \(\mathbf{C}/X\), whose objects are the arrows \(A\to X\)."""
            return SliceOverCategory(self, X)

        def CosliceUnder(self: Category, X: "Parent | Morphism") -> Category:
            r"""Return the coslice category \(X\setminus\mathbf{C}\), whose objects are the arrows \(X\to A\)."""
            return CosliceUnderCategory(self, X)

        def SubObject(self: Category, X: "Parent | Morphism") -> Category:
            r"""Return the category of subobjects of \(X\): the monomorphisms \(A\hookrightarrow X\)."""
            return SubobjectCategory(self, X)

        def SuperObject(self: Category, X: "Parent | Morphism") -> Category:
            r"""Return the category of superobjects of \(X\): the monomorphisms \(X\hookrightarrow B\)."""
            return SuperobjectCategory(self, X)

        def CoveringObject(self: Category, X: "Parent | Morphism") -> Category:
            r"""Return the category of covering objects of \(X\): the epimorphisms \(A\twoheadrightarrow X\)."""
            return CoveringObjectCategory(self, X)

        def CoveredObject(self: Category, X: "Parent | Morphism") -> Category:
            r"""Return the category of covered objects of \(X\): the epimorphisms \(X\twoheadrightarrow B\)."""
            return CoveredObjectCategory(self, X)

        def Kernel(self: Category, f: Morphism) -> Category:
            r"""Return the category of kernels of \(f\): the subobject \(\ker f\hookrightarrow\operatorname{dom}f\)."""
            return KernelCategory(self, f)

        def Cokernel(self: Category, f: Morphism) -> Category:
            r"""Return the category of cokernels of \(f\): the covered object \(\operatorname{cod}f\twoheadrightarrow\operatorname{coker}f\)."""
            return CokernelCategory(self, f)


# The one crossing of the Sage boundary.  Every construction above is declared
# in ``Cat.ParentMethods``, which is its home; a session reaches a category
# through Sage's ``Category``, so what is declared there is attached to that
# class here, exactly once, and nowhere else.
for _construction_name, _construction in vars(Cat.ParentMethods).items():
    if not _construction_name.startswith("_"):
        setattr(Category, _construction_name, _construction)
