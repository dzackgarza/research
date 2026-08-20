r"""``Cat``: the category whose objects are categories.

The constructions in this directory -- slices, arrows, diagrams, limits --
each take a category as their argument, so a category is the *object* they
are performed on and \(\mathbf{Cat}\) is where they are declared.  That is
what this module is: ``Cat.ParentMethods`` holds all twenty-one of them as
the methods an object of \(\mathbf{Cat}\) has, and each one delegates to the
owned class that already builds the construction.

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

from sage.categories.category import Category

from dzack_research.preamble.owned_category import OwnedCategoryMixin
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


class Cat(OwnedCategoryMixin, Category):
    r"""The category \(\mathbf{Cat}\), whose objects are categories.

    Not an :class:`OwnedCategory`: \(\mathbf{Cat}\) is not an object of itself,
    so it takes the hook that ties it to its implementation classes without the
    Cat-object half that every category below it carries.
    """

    def _repr_(self) -> str:
        return "Category of categories"

    def super_categories(self) -> list[Category]:
        # A category is not a set, so nothing above this holds its objects.
        return []

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

        def Diagram(
            self,
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of diagrams \(F:J\to\mathbf{C}\) on these objects and morphisms."""
            diagrams: Category = DiagramCategory(self, objects, morphisms)
            return diagrams

        def DirectedSystem(
            self,
            index_set: "OrderedSet",
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of directed systems \((X_i)_{i\in I}\) with morphisms \(X_i\to X_j\)."""
            systems: Category = DirectedSystem(self, index_set, objects, morphisms)
            return systems

        def InverseSystem(
            self,
            index_set: "OrderedSet",
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of inverse systems \((X_i)_{i\in I}\) with morphisms \(X_j\to X_i\)."""
            systems: Category = InverseSystem(self, index_set, objects, morphisms)
            return systems

        def Cone(
            self,
            index_set: "OrderedSet",
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of cones: an apex \(A\) with projections \(\pi_i:A\to X_i\)."""
            cones: Category = ConeCategory(self, index_set, objects, morphisms)
            return cones

        def Cocone(
            self,
            index_set: "OrderedSet",
            objects: "Iterable[Parent]",
            morphisms: "Iterable[Morphism]" = (),
        ) -> Category:
            r"""Return the category of cocones: a coapex \(A\) with injections \(\iota_i:X_i\to A\)."""
            cocones: Category = CoconeCategory(self, index_set, objects, morphisms)
            return cocones

        def Product(self, factors: "Iterable[Parent]") -> Category:
            r"""Return the category of products \(\prod_i X_i\) of these factors."""
            products: Category = ProductCategory(self, factors)
            return products

        def Coproduct(self, cofactors: "Iterable[Parent]") -> Category:
            r"""Return the category of coproducts \(\coprod_i X_i\) of these cofactors."""
            coproducts: Category = CoproductCategory(self, cofactors)
            return coproducts

        def Biproduct(self, factors: "Iterable[Parent]") -> Category:
            r"""Return the category of biproducts of these factors: product and coproduct at once."""
            biproducts: Category = BiproductCategory(self, factors)
            return biproducts

        def DirectSum(self, factors: "Iterable[Parent]") -> Category:
            r"""Return the category of direct sums \(\bigoplus_i X_i\), the additive name for the biproduct."""
            direct_sums: Category = DirectSumCategory(self, factors)
            return direct_sums

        def TensorProduct(self, factors: "Iterable[Parent]") -> Category:
            r"""Return the category of tensor products \(X_1\otimes\cdots\otimes X_n\) of these factors."""
            tensor_products: Category = TensorProductCategory(self, factors)
            return tensor_products

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

        def Kernel(self, f: Morphism) -> Category:
            r"""Return the category of kernels of \(f\): the subobject \(\ker f\hookrightarrow\operatorname{dom}f\)."""
            kernels: Category = KernelCategory(self, f)
            return kernels

        def Cokernel(self, f: Morphism) -> Category:
            r"""Return the category of cokernels of \(f\): the covered object \(\operatorname{cod}f\twoheadrightarrow\operatorname{coker}f\)."""
            cokernels: Category = CokernelCategory(self, f)
            return cokernels

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
