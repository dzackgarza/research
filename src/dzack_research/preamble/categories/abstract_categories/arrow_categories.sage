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
from dzack_research.preamble.owned_category_bases import Category, CategoryWithParameters
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

        def extra_super_categories(self) -> list[SageCategory]:
            if not self.base_category().base_category().is_locally_discrete():
                return []
            from dzack_research.preamble.categories.abstract_categories.functors import (
                DiscreteCategories,
            )

            return [DiscreteCategories()]

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
        return [
            MonomorphismArrowCategory(self._base_category),
            EpimorphismArrowCategory(self._base_category),
        ]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in ArrowCategory(self._base_category)
            and candidate.parent() in self._base_category.IsoCategory()
        )

    def __call__(self, arrow: SageElement) -> SageElement:
        assert arrow in self
        return arrow


class MonomorphismArrowCategory(_OnACategory, Category):
    r"""The subcategory of \(\operatorname{Ar}(\mathbf C)\) on monomorphisms."""

    def _repr_(self) -> str:
        return f"Category of monomorphisms in {self._base_category}"

    @property
    def ObjectType(self) -> type:
        return self._base_category.MonoArrowType

    def super_categories(self) -> list[Category]:
        return [ArrowCategory(self._base_category)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return candidate in ArrowCategory(self._base_category) and (
            candidate.parent() in self._base_category.MonoCategory()
            or candidate.parent() in self._base_category.IsoCategory()
        )

    def __call__(self, arrow: SageElement) -> SageElement:
        assert arrow in self
        return arrow


class EpimorphismArrowCategory(_OnACategory, Category):
    r"""The subcategory of \(\operatorname{Ar}(\mathbf C)\) on epimorphisms."""

    def _repr_(self) -> str:
        return f"Category of epimorphisms in {self._base_category}"

    @property
    def ObjectType(self) -> type:
        return self._base_category.EpiArrowType

    def super_categories(self) -> list[Category]:
        return [ArrowCategory(self._base_category)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return candidate in ArrowCategory(self._base_category) and (
            candidate.parent() in self._base_category.EpiCategory()
            or candidate.parent() in self._base_category.IsoCategory()
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


class _WithArrows:
    def __init__(
        self,
        base_category: SageCategory,
        arrows: Category,
    ) -> None:
        assert arrows.is_subcategory(base_category.ArrowCategory())
        self._base_category = base_category
        self._arrows = arrows
        super().__init__()

    def base_category(self) -> SageCategory:
        return self._base_category

    def arrows(self) -> Category:
        return self._arrows

    def _make_named_class_key(
        self,
        name: str,
    ) -> tuple[SageCategory, Category]:
        return self._base_category, self._arrows


class WideSubcategory(_WithArrows, CategoryWithParameters):
    r"""The objects of \(\mathbf C\) with a chosen subcategory of its arrows."""

    @property
    def ObjectType(self) -> type:
        return self._base_category.ObjectType

    @property
    def ElementType(self) -> type:
        return self._base_category.ElementType

    def super_categories(self) -> list[Category]:
        return [self._base_category]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return candidate in self._base_category

    def admits(self, arrow: SageElement) -> bool:
        return arrow in self._arrows

    def arrow(self, arrow: SageElement) -> SageElement:
        assert self.admits(arrow)
        return arrow

    def _repr_(self) -> str:
        if self._arrows is self._base_category.IsomorphismArrowCategory():
            return f"Core of {self._base_category}"
        return f"Wide subcategory of {self._base_category} with arrows in {self._arrows}"

    class _HomCategory(HomCategoryConstruction):
        def _object_type_of_object_type(self) -> type:
            return self.base_category().base_category().ArrowType

        class ParentMethods:
            def __contains__(self, arrow: SageElement) -> bool:
                wide = self.base_category()
                return (
                    arrow in wide.base_category().Hom(
                        self.domain(),
                        self.codomain(),
                    )
                    and wide.admits(arrow)
                )

            def __call__(self, arrow: SageElement) -> SageElement:
                assert arrow in self
                return arrow

            def identity(self) -> SageElement:
                wide = self.base_category()
                identity = wide.base_category().identity(self.domain())
                assert identity in self
                return identity

            def compose(self, second: SageElement, first: SageElement) -> SageElement:
                wide = self.base_category()
                composite = wide.base_category().compose(second, first)
                assert composite in self
                return composite


def Core(base_category: SageCategory) -> WideSubcategory:
    r"""Return the maximal subgroupoid of ``base_category``."""
    return WideSubcategory(
        base_category,
        base_category.IsomorphismArrowCategory(),
    )


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
