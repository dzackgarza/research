r"""Arrow categories: \(\operatorname{Ar}(\mathbf{C})\), its hom-sets, and the isomorphisms.

- ``ArrowCategory(C)`` -- \(\operatorname{Ar}(\mathbf{C})\): its objects are
  the *morphisms* of \(\mathbf{C}\) and its morphisms are commuting squares.
- ``IsoArrowCategory(C)`` -- the subcategory whose objects are the
  isomorphisms.  Invertibility is a declared datum, exactly as surjectivity is
  for a framing: the inverse is supplied and checked at construction, never
  searched for afterwards.
- ``Ar(X, Y)`` -- the arrows \(X\to Y\) as one object.
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

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.structure.parent import MembershipInput
# The owned root, not Sage's: the preamble places every set in it, and a set
# left in Sage's ``Sets()`` is not in the owned one.
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category
from sage.categories.morphism import IdentityMorphism
from sage.categories.morphism import Morphism
from sage.categories.objects import Objects
from sage.structure.parent import Parent

if TYPE_CHECKING:
    from sage.categories.homset import Homset

    from typing import Protocol

    class ArrowObject(Protocol):
        r"""An object of \(\operatorname{Ar}(\mathbf{C})\): an arrow of
        \(\mathbf{C}\), applied to elements and asked for its two ends."""

        def __call__(self, x: Element) -> Element: ...
        def domain(self) -> Parent: ...
        def codomain(self) -> Parent: ...


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

    class MorphismMethods:
        r"""The methods of an *object* of \(\operatorname{Ar}(\mathbf{C})\)."""

        def is_commuting_square(
            self: "ArrowObject",
            other: "ArrowObject",
            left: Morphism,
            right: Morphism,
        ) -> bool:
            r"""Return whether \((\ell,r)\) is a morphism \(f\to g\) of \(\operatorname{Ar}(\mathbf{C})\).

            A morphism of the arrow category from \(f:X\to Y\) to
            \(g:X'\to Y'\) is a pair \(\ell:X\to X'\), \(r:Y\to Y'\) with
            \(g\circ\ell=r\circ f\).  The two composites are compared where
            two morphisms out of \(X\) are decided -- on \(X\)'s distinguished
            generators -- and not by building a formal composite whose
            equality nothing defines.
            """
            # Local: slice_categories reaches the algebra node, so a
            # module-level import would close that cycle.
            from dzack_research.preamble.categories.abstract_categories.slice_categories import sole_structure_generators

            assert (
                left.domain() is self.domain()
                and left.codomain() is other.domain()
            ), "the left edge of the square runs between the two sources"
            assert (
                right.domain() is self.codomain()
                and right.codomain() is other.codomain()
            ), "the right edge of the square runs between the two targets"
            return all(
                other(left(generator)) == right(self(generator))
                for generator in sole_structure_generators(self.domain())
            )


class IsoArrowCategory(_OnACategory, Category):
    r"""The subcategory of \(\operatorname{Ar}(\mathbf{C})\) of isomorphisms."""

    def _repr_(self) -> str:
        return f"Category of isomorphisms in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [ArrowCategory(self._ambient_category)]

    class MorphismMethods:
        # Installed on the arrow by ``Isomorphism`` below.
        _inverse_morphism: Morphism

        def inverse(self) -> Morphism:
            r"""Return the inverse arrow \(f^{-1}:Y\to X\)."""
            return self._inverse_morphism

        def is_isomorphism(self) -> bool:
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


def Ar(source: Parent, target: Parent) -> "Homset":
    r"""Return \(\operatorname{Ar}(X,Y)\), the arrows \(X\to Y\), as one object.

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
            return Ar(self._source, self._target)

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

    Both round trips are checked on the distinguished generators, which is
    what makes the declaration falsifiable: a wrong transformation matrix
    fails here rather than silently naming an unrelated object.
    """
    # Local: slice_categories reaches the algebra node, so module-level
    # imports would close that cycle; both are built by call time.
    from dzack_research.preamble.categories.abstract_categories.slice_categories import sole_structure_generators
    from dzack_research.preamble.refine import refine

    assert isinstance(forward, Morphism) and isinstance(backward, Morphism), (
        "an isomorphism is declared by an arrow and its inverse"
    )
    assert (
        backward.domain() is forward.codomain()
        and backward.codomain() is forward.domain()
    ), "the inverse of an arrow X -> Y is an arrow Y -> X"
    assert all(
        backward(forward(generator)) == generator
        for generator in sole_structure_generators(forward.domain())
    ), "the declared inverse does not recover the source's generators"
    assert all(
        forward(backward(generator)) == generator
        for generator in sole_structure_generators(forward.codomain())
    ), "the declared inverse does not recover the target's generators"
    # Installed on the arrows themselves: ``Morphism`` is a cython class and
    # the inverse is declared here, not held by any Sage class.
    setattr(forward, "_inverse_morphism", backward)
    setattr(backward, "_inverse_morphism", forward)
    iso_arrows = forward.domain().category().IsoArrow()
    refine(backward, iso_arrows)
    isomorphism: Morphism = refine(forward, iso_arrows)
    return isomorphism
