r"""Arrow categories: \(\operatorname{Ar}(\mathbf{C})\), its hom-sets, and the isomorphisms.

- ``ArrowCategory(C)`` -- \(\operatorname{Ar}(\mathbf{C})\): its objects are
  the *morphisms* of \(\mathbf{C}\) and its morphisms are commuting squares.
- ``EndArrowCategory(C)`` -- the full subcategory on endomorphisms.
- ``AutomorphismArrowCategory(C)`` -- the full subcategory on automorphisms.
- ``IsoArrowCategory(C)`` -- the subcategory whose objects are the
  isomorphisms.  Invertibility is a declared datum, exactly as surjectivity is
  for a framing: the inverse is supplied and checked at construction, never
  searched for afterwards.
- ``HomSet(X, Y)`` -- the arrows \(X\to Y\) as one set object.
- ``IsoAr(X, Y)`` -- the isomorphisms inside \(\operatorname{Ar}(X,Y)\).
- ``Isomorphism(f, g)`` -- the construction: declare \(f\) invertible with
  inverse \(g\), and get back \(f\) as an object of
  \(\operatorname{Ar}(\mathbf{C})\).
- ``C.core()`` -- \(\operatorname{core}(\mathbf{C})\): the same objects, and
  the isomorphisms as the only arrows.  A functor defined only on
  isomorphisms declares this as its source.

Sage seats an object of a category in a ``Parent`` and an arrow in an element
of a homset.  An object of \(\operatorname{Ar}(\mathbf{C})\) is an arrow of
\(\mathbf{C}\), so its methods are ``MorphismMethods`` and it enters the
category by :func:`refine` of the arrow -- not of the arrow's parent.  That is
the whole reason this construction is worth having: a normal form can be
*returned* as the arrow \(M\to M'\), and the new object recovered from it as
``target()``, instead of the caller being handed a reduced matrix and left to
track \(M'\) separately.
"""

from collections.abc import Iterable
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.structure.parent import MembershipInput
# The owned root, not Sage's: the preamble places every set in it, and a set
# left in Sage's ``Sets()`` is not in the owned one.
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category
from sage.categories.category import Category as SageCategory
from sage.categories.morphism import IdentityMorphism
from sage.categories.morphism import Morphism
from sage.categories.objects import Objects
from sage.structure.element import Element as SageElement
from sage.structure.parent import Parent

if TYPE_CHECKING:
    from sage.categories.homset import Homset


def common_category(objects: Iterable[Parent]) -> SageCategory:
    r"""Return the most specific category containing all given objects."""
    return SageCategory.meet([obj.category() for obj in objects])


class _OnACategory:
    r"""The one parameter these categories take: the ambient category
    \(\mathbf{C}\) they are built out of.

    This is not a category.  Each category below states its place with
    ``super_categories()``.  A category class that inherits another states the
    class graph by hand instead, and then its methods class arrives twice in
    one set of bases, which no method resolution order can satisfy.
    """

    def __init__(self, ambient_category: Category) -> None:
        self._ambient_category = ambient_category
        super().__init__()

    def ambient_category(self) -> Category:
        return self._ambient_category


class ArrowCategory(_OnACategory, Category):
    r"""\(\operatorname{Ar}(\mathbf{C})\): the morphisms of \(\mathbf{C}\) as objects."""

    def _repr_(self) -> str:
        return f"Category of arrows in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        # Not the ambient category: an arrow of C is not an object of C.  What
        # relates the two are the functors dom, cod: Ar(C) -> C, and neither is
        # an inclusion, so there is nothing above this but Objects.
        return [Objects()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            isinstance(candidate, Morphism)
            and candidate.domain() in self._ambient_category
            and candidate.codomain() in self._ambient_category
        )

    def __call__(self, arrow: Morphism) -> Morphism:
        r"""Place ``arrow`` as an object of \(\operatorname{Ar}(\mathbf{C})\)."""
        from dzack_research.preamble.refine import refine

        assert arrow in self
        placed: Morphism = refine(arrow, self)
        return placed

    def homset(self, source: Morphism, target: Morphism) -> Parent:
        r"""Return the commuting squares from ``source`` to ``target``."""
        assert source.domain() in self._ambient_category
        assert source.codomain() in self._ambient_category
        assert target.domain() in self._ambient_category
        assert target.codomain() in self._ambient_category
        return ArrowHomset(source, target)


class ArrowHomsets(Category):
    r"""Sets of morphisms in arrow categories."""

    def _repr_object_names(self) -> str:
        return "arrow-category homsets"

    def super_categories(self) -> list[Category]:
        return [Sets()]

    class ParentMethods:
        def __init__(
            self,
            source: Morphism,
            target: Morphism,
            **rest: "ConstructionData",
        ) -> None:
            self._source = source
            self._target = target
            super().__init__(**rest)

        def domain(self) -> Morphism:
            return self._source

        def codomain(self) -> Morphism:
            return self._target

        def __contains__(self, square: "CommutativeSquare") -> bool:
            return isinstance(square, CommutativeSquare) and square.parent() is self

        def _element_constructor_(
            self,
            left: Morphism,
            right: Morphism,
        ) -> "CommutativeSquare":
            return CommutativeSquare(self, left, right)

        def identity(self) -> "CommutativeSquare":
            source = self._source
            assert source is self._target, (
                "only an endomorphism set has an identity square"
            )
            left = source.domain().Hom(source.domain()).identity()
            right = source.codomain().Hom(source.codomain()).identity()
            return CommutativeSquare(self, left, right)

        def _repr_(self) -> str:
            return f"Commuting squares from {self._source} to {self._target}"


class CommutativeSquare(SageElement):
    r"""A morphism in an arrow category.

    For ``source: X -> Y`` and ``target: X' -> Y'``, the left and right
    edges have boundaries ``X -> X'`` and ``Y -> Y'``.  Commutativity is
    declared structure.  This general layer does not decide morphism equality.
    """

    def __init__(self, parent: Parent, left: Morphism, right: Morphism) -> None:
        source = parent.domain()
        target = parent.codomain()
        assert left.domain() is source.domain()
        assert left.codomain() is target.domain()
        assert right.domain() is source.codomain()
        assert right.codomain() is target.codomain()
        self._left = left
        self._right = right
        SageElement.__init__(self, parent)

    def domain(self) -> Morphism:
        return self.parent().domain()

    def codomain(self) -> Morphism:
        return self.parent().codomain()

    def left(self) -> Morphism:
        return self._left

    def right(self) -> Morphism:
        return self._right

    def __mul__(self, first: "CommutativeSquare") -> "CommutativeSquare":
        r"""Compose two commuting squares componentwise."""
        assert first.codomain() is self.domain(), (
            "commuting squares compose only when their middle arrow agrees"
        )
        return ArrowHomset(first.domain(), self.codomain())(
            self._left * first.left(),
            self._right * first.right(),
        )

    def _repr_(self) -> str:
        return f"Commuting square from {self.domain()} to {self.codomain()}"


def ArrowHomset(source: Morphism, target: Morphism) -> Parent:
    r"""Return the homset of commuting squares from ``source`` to ``target``."""
    endpoints = (
        source.domain(),
        source.codomain(),
        target.domain(),
        target.codomain(),
    )
    arrow_category = common_category(endpoints).Ar()
    assert source.domain() in arrow_category.ambient_category()
    assert source.codomain() in arrow_category.ambient_category()
    assert target.domain() in arrow_category.ambient_category()
    assert target.codomain() in arrow_category.ambient_category()
    return object_of(ArrowHomsets(), source=source, target=target)

class IsoArrowCategory(_OnACategory, Category):
    r"""The subcategory of \(\operatorname{Ar}(\mathbf{C})\) of isomorphisms."""

    def _repr_(self) -> str:
        return f"Category of isomorphisms in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [ArrowCategory(self._ambient_category)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in ArrowCategory(self._ambient_category)
            and isinstance(getattr(candidate, "_inverse_morphism", None), Morphism)
        )

    def __call__(self, arrow: Morphism) -> Morphism:
        from dzack_research.preamble.refine import refine

        assert arrow in self
        placed: Morphism = refine(arrow, self)
        return placed

    class MorphismMethods:
        # Installed on the arrow by ``Isomorphism`` below.
        _inverse_morphism: Morphism

        def inverse(self) -> Morphism:
            r"""Return the inverse arrow \(f^{-1}:Y\to X\)."""
            return self._inverse_morphism

        def is_isomorphism(self) -> bool:
            return True


class EndArrowCategory(_OnACategory, Category):
    r"""The full subcategory of \(\operatorname{Ar}(\mathbf{C})\) on endomorphisms."""

    def _repr_(self) -> str:
        return f"Category of endomorphisms in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [ArrowCategory(self._ambient_category)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in ArrowCategory(self._ambient_category)
            and candidate.domain() is candidate.codomain()
        )

    def __call__(self, arrow: Morphism) -> Morphism:
        from dzack_research.preamble.refine import refine

        assert arrow in self
        placed: Morphism = refine(arrow, self)
        return placed

    class MorphismMethods:
        def is_endomorphism(self) -> bool:
            return True


class AutomorphismArrowCategory(_OnACategory, Category):
    r"""The full subcategory of \(\operatorname{Ar}(\mathbf{C})\) on automorphisms."""

    def _repr_(self) -> str:
        return f"Category of automorphisms in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [
            EndArrowCategory(self._ambient_category),
            IsoArrowCategory(self._ambient_category),
        ]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in EndArrowCategory(self._ambient_category)
            and candidate in IsoArrowCategory(self._ambient_category)
        )

    def __call__(self, arrow: Morphism) -> Morphism:
        from dzack_research.preamble.refine import refine

        assert arrow in self
        placed: Morphism = refine(arrow, self)
        return placed

    class MorphismMethods:
        def is_automorphism(self) -> bool:
            return True


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
        return f"Core of {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        # Objects, for ArrowCategory's reason read the other way round: what
        # separates the core from C is which *arrows* it has, and Sage's
        # subcategory relation is about objects satisfying more.  Naming C
        # here would say the core has fewer objects, which is the one thing
        # it does not.
        return [Objects()]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        r"""Return whether ``candidate`` is an object of \(\mathbf{C}\): the core keeps them all."""
        return candidate in self._ambient_category

    def admits(self, morphism: Morphism) -> bool:
        r"""Return whether ``morphism`` is an arrow of the core, i.e. invertible."""
        match morphism:
            case IdentityMorphism():
                return True
            case IsoArrowCategory.MorphismMethods():
                return morphism.is_isomorphism()
            case _:
                return False

    def arrow(self, morphism: Morphism) -> Morphism:
        r"""Return ``morphism`` as an arrow of the core, refusing one that is not.

        The gate a functor out of the core passes its argument through.
        """
        assert self.admits(morphism), (
            f"{morphism} is not a declared isomorphism, so it is not an arrow "
            f"of {self}"
        )
        return morphism


def HomSet(source: Parent, target: Parent) -> "Homset":
    r"""Return \(\operatorname{Hom}_{\mathbf{C}}(X,Y)\), the arrows \(X\to Y\), as one set.

    This is the canonical hom-set and not a wrapper of it.  A morphism's
    identity in this repo *is* its parent -- the module homsets' ``__contains__`` is
    ``parent() is self``, ``module_homset`` caches one homset per pair, and
    every morphism is manufactured by that parent -- so a second parent
    holding the same arrows would make two copies of one arrow fail to be the
    same arrow.  There is nothing to add: the hom-set already *is* the object
    whose elements are the arrows.
    """
    arrows: "Homset" = source.Hom(target)
    return arrows


class IsomorphismSets(Category):
    r"""\(\operatorname{IsoAr}(X,Y)\subseteq\operatorname{Ar}(X,Y)\).

    An object is a *subset* of the arrow set, cut out by invertibility.  It is
    the same kind of thing ``CartesianProductOfSets`` is: a parent whose
    members live in other parents.  It is nonempty exactly when \(X\) and
    \(Y\) are isomorphic, and when nonempty it is a torsor under
    \(\operatorname{Aut}(X)\) acting by precomposition;
    \(\operatorname{IsoAr}(X,X)\) is \(\operatorname{Aut}(X)\).

    The two ends are the datum this level introduces, so they are the two
    arguments its ``__init__`` consumes.
    """

    def _repr_object_names(self) -> str:
        return "isomorphism sets"

    def super_categories(self) -> list[Category]:
        return [Sets()]

    class ParentMethods:
        def __init__(
            self,
            source: Parent,
            target: Parent,
            **rest: "ConstructionData",
        ) -> None:
            self._source = source
            self._target = target
            super().__init__(**rest)

        def source(self) -> Parent:
            return self._source

        def target(self) -> Parent:
            return self._target

        def arrow_set(self) -> "Homset":
            r"""Return \(\operatorname{Ar}(X,Y)\), the arrow set this sits inside."""
            return HomSet(self._source, self._target)

        def __contains__(self, arrow: "MembershipInput") -> bool:
            match arrow:
                case IsoArrowCategory.MorphismMethods():
                    # An object of Ar(C) is an arrow of C, and its source and
                    # target are that arrow's two ends.
                    assert isinstance(arrow, Morphism)
                    return (
                        arrow.domain() is self._source
                        and arrow.codomain() is self._target
                    )
                case _:
                    return False

        def _element_constructor_(self, arrow: Morphism) -> Morphism:
            assert arrow in self, (
                f"{arrow} is not a declared isomorphism from {self._source} to "
                f"{self._target}"
            )
            return arrow

        def _repr_(self) -> str:
            return f"Isomorphisms from {self._source} to {self._target}"


def IsoAr(source: Parent, target: Parent) -> Parent:
    r"""Return \(\operatorname{IsoAr}(X,Y)\), the isomorphisms \(X\to Y\).

    The construction is the category: what an isomorphism set *is* is declared
    once on ``IsomorphismSets.ParentMethods``, and the object is that
    category's parent class carrying the two ends.
    """
    return object_of(IsomorphismSets(), source=source, target=target)


def Isomorphism(forward: Morphism, backward: Morphism) -> Morphism:
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
    from dzack_research.preamble.refine import refine

    assert isinstance(forward, Morphism) and isinstance(backward, Morphism), (
        "an isomorphism is declared by an arrow and its inverse"
    )
    assert (
        backward.domain() is forward.codomain()
        and backward.codomain() is forward.domain()
    ), "the inverse of an arrow X -> Y is an arrow Y -> X"
    # Installed on the arrows themselves: ``Morphism`` is a cython class and
    # the inverse is declared here, not held by any Sage class.
    setattr(forward, "_inverse_morphism", backward)
    setattr(backward, "_inverse_morphism", forward)
    category = common_category((forward.domain(), forward.codomain()))
    iso_arrows = (
        category.AutAr()
        if forward.domain() is forward.codomain()
        else category.IsoAr()
    )
    iso_arrows(backward)
    isomorphism: Morphism = iso_arrows(forward)
    return isomorphism
