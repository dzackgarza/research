r"""Arrow categories of a category \(\mathbf C\).

- ``ArrowCategory(C)`` -- \(\operatorname{Ar}(\mathbf{C})\): its objects are
  the *morphisms* of \(\mathbf{C}\) and its morphisms are commuting squares.
- ``EndArrowCategory(C)`` -- the full subcategory on endomorphisms.
- ``AutomorphismArrowCategory(C)`` -- the full subcategory on automorphisms.
- ``IsoArrowCategory(C)`` -- the full subcategory on isomorphisms.
- ``Isomorphism(f, g)`` -- the construction: declare \(f\) invertible with
  inverse \(g\).
- ``C.core()`` -- \(\operatorname{core}(\mathbf{C})\): the same objects, and
  the isomorphisms as the only arrows.  A functor defined only on
  isomorphisms declares this as its source.

``Ar(C).ObjectType`` is ``C.ArrowType``.  Its Hom categories have commuting
squares as objects.  No part of this construction assumes that a Hom category
is a set.
"""

from collections.abc import Iterable
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    HomCategoryConstruction,
)
from dzack_research.preamble.owned_category_bases import Category
from sage.categories.category import Category as SageCategory
from sage.categories.objects import Objects
from sage.structure.element import Element as SageElement
from sage.structure.parent import Parent

def common_category(objects: Iterable[Parent | SageCategory]) -> SageCategory:
    r"""Return the most specific category containing all given objects."""
    return SageCategory.meet([obj.category() for obj in objects])


class _OnACategory:
    r"""The one parameter these categories take: the base category
    \(\mathbf{C}\) they are built out of.

    This is not a category.  Each category below states its place with
    ``super_categories()``.  A category class that inherits another states the
    class graph by hand instead, and then its methods class arrives twice in
    one set of bases, which no method resolution order can satisfy.
    """

    def __init__(self, base_category: SageCategory) -> None:
        self._base_category = base_category
        super().__init__()

    def base_category(self) -> SageCategory:
        return self._base_category


class ArrowCategory(_OnACategory, Category):
    r"""\(\operatorname{Ar}(\mathbf{C})\): the morphisms of \(\mathbf{C}\) as objects."""

    def _repr_(self) -> str:
        return f"Category of arrows in {self._base_category}"

    @property
    def ObjectType(self) -> type:
        return self._base_category.ArrowType

    def super_categories(self) -> list[Category]:
        # Not the base category: an arrow of C is not an object of C.  What
        # relates the two are the functors dom, cod: Ar(C) -> C, and neither is
        # an inclusion, so there is nothing above this but Objects.
        return [Objects()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        match candidate:
            case SageElement():
                return (
                    candidate.parent() in self._base_category.HomCategory()
                    and candidate.domain() in self._base_category
                    and candidate.codomain() in self._base_category
                )
            case _:
                return False

    def __call__(self, arrow: SageElement) -> SageElement:
        r"""Place ``arrow`` as an object of \(\operatorname{Ar}(\mathbf{C})\)."""
        assert arrow in self
        return arrow

    class _HomCategory(HomCategoryConstruction):
        r"""Categories of commuting squares between arrows."""

        class ParentMethods:
            def __call__(
                self,
                left: SageElement,
                right: SageElement,
            ) -> "ArrowCategory.ArrowType":
                return self.ObjectType(
                    hom_category=self,
                    left=left,
                    right=right,
                )

            def identity(self) -> "ArrowCategory.EndArrowType":
                source = self.domain()
                assert source is self.codomain(), (
                    "an identity square belongs to an endomorphism category"
                )
                category = self.base_category().base_category()
                return self(
                    category.identity(source.domain()),
                    category.identity(source.codomain()),
                )

            def compose(
                self,
                second: "ArrowCategory.ArrowType",
                first: "ArrowCategory.ArrowType",
            ) -> "ArrowCategory.ArrowType":
                assert first.codomain() is second.domain()
                category = self.base_category().base_category()
                return self(
                    category.compose(second.left(), first.left()),
                    category.compose(second.right(), first.right()),
                )

        class ElementMethods:
            r"""A commuting square, with commutativity declared at construction."""

            def __init__(
                self,
                hom_category: Category,
                left: SageElement,
                right: SageElement,
            ) -> None:
                source = hom_category.domain()
                target = hom_category.codomain()
                category = hom_category.base_category().base_category()
                assert left in category.ArrowCategory()
                assert right in category.ArrowCategory()
                assert left.domain() is source.domain()
                assert left.codomain() is target.domain()
                assert right.domain() is source.codomain()
                assert right.codomain() is target.codomain()
                self._left = left
                self._right = right
                super().__init__(hom_category=hom_category)

            def left(self) -> SageElement:
                return self._left

            def right(self) -> SageElement:
                return self._right


class IsoArrowCategory(_OnACategory, Category):
    r"""The subcategory of \(\operatorname{Ar}(\mathbf{C})\) of isomorphisms."""

    def _repr_(self) -> str:
        return f"Category of isomorphisms in {self._base_category}"

    @property
    def ObjectType(self) -> type:
        return self._base_category.IsoArrowType

    def super_categories(self) -> list[Category]:
        return [ArrowCategory(self._base_category)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in ArrowCategory(self._base_category)
            and candidate.parent() in self._base_category.IsoCategory()
        )

    def __call__(self, arrow: SageElement) -> SageElement:
        assert arrow in self
        return arrow


class EndArrowCategory(_OnACategory, Category):
    r"""The full subcategory of \(\operatorname{Ar}(\mathbf{C})\) on endomorphisms."""

    def _repr_(self) -> str:
        return f"Category of endomorphisms in {self._base_category}"

    @property
    def ObjectType(self) -> type:
        return self._base_category.EndArrowType

    def super_categories(self) -> list[Category]:
        return [ArrowCategory(self._base_category)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in ArrowCategory(self._base_category)
            and candidate.domain() is candidate.codomain()
        )

    def __call__(self, arrow: SageElement) -> SageElement:
        assert arrow in self
        return arrow


class AutomorphismArrowCategory(_OnACategory, Category):
    r"""The full subcategory of \(\operatorname{Ar}(\mathbf{C})\) on automorphisms."""

    def _repr_(self) -> str:
        return f"Category of automorphisms in {self._base_category}"

    @property
    def ObjectType(self) -> type:
        return self._base_category.AutArrowType

    def super_categories(self) -> list[Category]:
        return [
            EndArrowCategory(self._base_category),
            IsoArrowCategory(self._base_category),
        ]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in ArrowCategory(self._base_category)
            and candidate.parent() in self._base_category.AutCategory()
        )

    def __call__(self, arrow: SageElement) -> SageElement:
        assert arrow in self
        return arrow


class Core(_OnACategory, Category):
    r"""\(\operatorname{core}(\mathbf{C})\): the objects of \(\mathbf{C}\), its isomorphisms alone.

    The maximal subgroupoid.  A construction that is functorial only on
    isomorphisms names this as its source, and the naming is the point: the
    refusal of a non-invertible arrow becomes part of what the functor *is*,
    rather than a check each call site has to remember.  \(Z\) is such a
    construction -- an isomorphism \(A\to B\) restricts to \(Z(A)\to Z(B)\)
    and a general ring map does not.

    Invertibility is read off the arrow and never searched for, as
    :func:`Isomorphism` records it: an identity is invertible by itself, and
    every other arrow of the core is one that was declared with its inverse.
    """

    def _repr_(self) -> str:
        return f"Core of {self._base_category}"

    def super_categories(self) -> list[Category]:
        # Objects, for ArrowCategory's reason read the other way round: what
        # separates the core from C is which *arrows* it has, and Sage's
        # subcategory relation is about objects satisfying more.  Naming C
        # here would say the core has fewer objects, which is the one thing
        # it does not.
        return [Objects()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        r"""Return whether ``candidate`` is an object of \(\mathbf{C}\): the core keeps them all."""
        return candidate in self._base_category

    def admits(self, morphism: SageElement) -> bool:
        r"""Return whether ``morphism`` is an arrow of the core, i.e. invertible."""
        return morphism in self._base_category.IsomorphismArrowCategory()

    def arrow(self, morphism: SageElement) -> SageElement:
        r"""Return ``morphism`` as an arrow of the core, refusing one that is not.

        The gate a functor out of the core passes its argument through.
        """
        assert self.admits(morphism), (
            f"{morphism} is not a declared isomorphism, so it is not an arrow "
            f"of {self}"
        )
        return morphism


def Isomorphism(forward: SageElement, backward: SageElement) -> SageElement:
    r"""Declare ``forward`` invertible with inverse ``backward``, and return it.

    Two objects being isomorphic is not a property either of them carries; it
    is this arrow.  So what is constructed is the arrow, and both objects are
    read off it as ``source()`` and ``target()``.  A construction that produces
    a new object -- a normal form, a change of generators -- returns this and
    is complete; returning the object alone loses the only thing that relates
    it to the one it came from.

    The category records inverse data.  It does not decide equality of
    arbitrary morphisms.  A category with decidable morphism equality can
    validate the two inverse equations before it calls this constructor.
    """
    assert (
        backward.domain() is forward.codomain()
        and backward.codomain() is forward.domain()
    ), "the inverse of an arrow X -> Y is an arrow Y -> X"
    category = common_category((forward.domain(), forward.codomain()))
    isomorphisms = (
        category.Aut(forward.domain())
        if forward.domain() is forward.codomain()
        else category.Iso(forward.domain(), forward.codomain())
    )
    return isomorphisms(forward, backward)
