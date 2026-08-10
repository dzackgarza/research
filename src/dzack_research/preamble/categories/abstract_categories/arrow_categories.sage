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

Sage seats an object of a category in a ``Parent`` and an arrow in an element
of a homset.  An object of \(\operatorname{Ar}(\mathbf{C})\) is an arrow of
\(\mathbf{C}\), so its methods are ``MorphismMethods`` and it enters the
category by :func:`refine` of the arrow -- not of the arrow's parent.  That is
the whole reason this construction is worth having: a normal form can be
*returned* as the arrow \(M\to M'\), and the new object recovered from it as
``target()``, instead of the caller being handed a reduced matrix and left to
track \(M'\) separately.
"""

from sage.categories.sets_cat import Sets
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.homset import Homset

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.objects import Objects
from sage.structure.parent import Parent


class ArrowCategory(Category):
    r"""\(\operatorname{Ar}(\mathbf{C})\): the morphisms of \(\mathbf{C}\) as objects."""

    @staticmethod
    def __classcall_private__(cls, ambient_category: Category) -> "ArrowCategory":
        return super().__classcall__(cls, ambient_category)

    def __init__(self, ambient_category: Category) -> None:
        self._ambient_category = ambient_category
        Category.__init__(self)

    def _repr_(self) -> str:
        return f"Category of arrows in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        # Not the ambient category: an arrow of C is not an object of C.  What
        # relates the two are the functors dom, cod: Ar(C) -> C, and neither is
        # an inclusion, so there is nothing above this but Objects.
        return [Objects()]

    def ambient_category(self) -> Category:
        return self._ambient_category

    class MorphismMethods:
        r"""The methods of an *object* of \(\operatorname{Ar}(\mathbf{C})\)."""

        def source(self) -> Parent:
            r"""Return \(X\), for this object \(f:X\to Y\)."""
            return self.domain()

        def target(self) -> Parent:
            r"""Return \(Y\), for this object \(f:X\to Y\)."""
            return self.codomain()

        def is_commuting_square(
            self,
            other: Morphism,
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
                left.domain() is self.source()
                and left.codomain() is other.source()
            ), "the left edge of the square runs between the two sources"
            assert (
                right.domain() is self.target()
                and right.codomain() is other.target()
            ), "the right edge of the square runs between the two targets"
            return all(
                other(left(generator)) == right(self(generator))
                for generator in sole_structure_generators(self.source())
            )


class IsoArrowCategory(ArrowCategory):
    r"""The subcategory of \(\operatorname{Ar}(\mathbf{C})\) of isomorphisms."""

    def _repr_(self) -> str:
        return f"Category of isomorphisms in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [ArrowCategory(self._ambient_category)]

    class MorphismMethods(ArrowCategory.MorphismMethods):
        def inverse(self) -> Morphism:
            r"""Return the inverse arrow \(f^{-1}:Y\to X\)."""
            return self._inverse_morphism

        def is_isomorphism(self) -> bool:
            return True


Category.Arrow = lambda self: ArrowCategory(self)
Category.IsoArrow = lambda self: IsoArrowCategory(self)


def Ar(source: Parent, target: Parent) -> "Homset":
    r"""Return \(\operatorname{Ar}(X,Y)\), the arrows \(X\to Y\), as one object.

    This is the canonical hom-set and not a wrapper of it.  A morphism's
    identity in this repo *is* its parent -- ``ModuleHomset.__contains__`` is
    ``parent() is self``, ``module_homset`` caches one homset per pair, and
    every morphism is manufactured by that parent -- so a second parent
    holding the same arrows would make two copies of one arrow fail to be the
    same arrow.  There is nothing to add: the hom-set already *is* the object
    whose elements are the arrows.
    """
    return source.Hom(target)


class IsomorphismSet(Parent):
    r"""\(\operatorname{IsoAr}(X,Y)\subseteq\operatorname{Ar}(X,Y)\).

    A *subset* of the arrow set, cut out by invertibility -- the same kind of
    thing ``CartesianProductOfSets`` is, a parent whose members live in other
    parents.  It is nonempty exactly when \(X\) and \(Y\) are isomorphic, and
    when nonempty it is a torsor under \(\operatorname{Aut}(X)\) acting by
    precomposition; \(\operatorname{IsoAr}(X,X)\) is \(\operatorname{Aut}(X)\).
    """

    def __init__(self, source: Parent, target: Parent) -> None:
        self._source = source
        self._target = target
        Parent.__init__(self, category=Sets())

    def source(self) -> Parent:
        return self._source

    def target(self) -> Parent:
        return self._target

    def arrow_set(self) -> "Homset":
        r"""Return \(\operatorname{Ar}(X,Y)\), the arrow set this sits inside."""
        return Ar(self._source, self._target)

    def __contains__(self, arrow: Morphism) -> bool:
        match arrow:
            case IsoArrowCategory.MorphismMethods():
                return (
                    arrow.source() is self._source
                    and arrow.target() is self._target
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


IsoAr = IsomorphismSet


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
    forward._inverse_morphism = backward
    backward._inverse_morphism = forward
    iso_arrows = forward.domain().category().IsoArrow()
    refine(backward, iso_arrows)
    return refine(forward, iso_arrows)
