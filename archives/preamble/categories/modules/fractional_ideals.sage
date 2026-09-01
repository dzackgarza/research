r"""Ideals and fractional ideals of a commutative ring, as \(R\)-modules.

An ideal \(I\subseteq R\) is an \(R\)-submodule of \(R\); a fractional ideal
is an \(R\)-submodule of \(\operatorname{Frac}(R)\) admitting a common
denominator.  One category carries both, because each is the pair
\((I,\iota)\) for an inclusion \(\iota\): what changes between them is the
codomain of \(\iota\) -- \(R\) for an integral ideal,
\(\operatorname{Frac}(R)\) for a fractional one -- read off the ring on
demand, never stored beside it.

The generating family is the ideal's own -- ``gens`` and
``module_generators`` are the same family read in the two vocabularies, and
this category exists so that reading is a fact rather than a coincidence.
"""

from typing import Self, TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from dzack_research.preamble.lexicon import OrderedSet
    from dzack_research.preamble.owned_category import ConstructionData

from dzack_research.preamble.categories.modules.framed.finitely_generated.ring_as_module import ring_as_module
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings.rings import engine_ring
if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.rings.ring import Ring
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.rings.rings import OwnedBaseRing
from dzack_research.preamble.owned_category import object_of
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.rings.ideal import Ideal_generic
from sage.structure.parent import Parent


class OwnedIdeals(OwnedCategoryOverBaseRing):
    r"""Ideals of \(R\), which are the \(R\)-submodules of \(R\).

    Not a resemblance: \(I\subseteq R\) is closed under addition and under
    multiplication by \(R\), and those two conditions *are* the submodule
    conditions, so an ideal is a submodule and its generating family is one
    family under one word.  (Over a Dedekind domain a nonzero ideal is
    moreover rank-1 projective; that is a theorem about this category, not
    what places a method on it.)
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "ideals"

    def super_categories(self) -> list:
        return [Modules(self.base_ring())]

    class ParentMethods(OwnedBaseRing):
        r"""One ideal: the ring it lies in, and the family that generates it."""

        def __init__(
            self: Self,
            ring: "Ring",
            generators: "OrderedSet",
            **rest: "ConstructionData",
        ) -> None:
            ring = engine_ring(ring)
            self._ring = ring
            # The generating family is kept as given, and kept as a tuple.  An
            # integral ideal's generators are elements of R and a fractional
            # ideal's are not; moving them all into Frac(R) would replace the
            # ideal's own family with a copy of it, which is the one thing this
            # object must not do -- and an ordered *set* does exactly that, since
            # its parent is cached by the values it holds, so \(1\in R\) is served
            # back as whichever equal \(1\) built that set first.  A family of
            # ring elements is carried by the ring, not by a set of numbers.
            self._generators = tuple(generators)
            super().__init__(**rest)

        def ring(self: Self) -> "Ring":
            r"""Return \(R\), the ring this is an ideal of."""
            return self._ring

        def _ring_morphism_defining_module_action(self: Self) -> "Morphism":
            r"""Return \(\rho:R\to\operatorname{End}(I)\), \(r\mapsto(x\mapsto rx)\).

            The action an ideal has from being an ideal: \(RI\subseteq I\) is one
            of the two conditions defining it, so multiplication in
            \(\operatorname{Frac}(R)\) already lands where it must.  No generating
            family is consulted -- being a module is not a statement about
            generators.
            """
            # Local: a module-level import here would close a cycle; the morphism
            # module is built by the time an ideal is asked for its action.
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import module_homset

            endomorphisms = module_homset(self, self)
            return SetMorphism(
                Hom(self._ring, endomorphisms, SageRings()),
                lambda scalar: SetMorphism(
                    endomorphisms, lambda element: scalar * element
                ),
            )

        def module_generators(self: Self) -> tuple:
            r"""Return the generating family, read as module generators.

            An ideal's generators generate it as an \(R\)-module: the two words
            name one family, and that is the content here.  The family is the
            one supplied, its members still elements of \(R\).
            """
            return self._generators

        def inverse(self: Self) -> Parent:
            r"""Return \(I^{-1}=\{x\in\operatorname{Frac}(R):xI\subseteq R\}\).

            For \(I=(g)\) this is \((g^{-1})\), which is the whole of the
            computation.  A non-principal ideal's inverse needs the Dedekind
            arithmetic of \(R\), which this object does not carry.
            """
            generator = self.principal_generator()
            assert not generator.is_zero(), "the zero ideal is not invertible"
            return FractionalIdeal(
                self._ring, (~self._ring.fraction_field()(generator),)
            )

        def _dividing_generator(self: Self) -> tuple:
            r"""Return the generators that divide the whole family.

            A supplied family need not be minimal -- an order hands back a module
            basis of \((2)\), not the single ideal generator -- so a generator
            dividing the whole family generates the ideal by itself.
            """
            return tuple(
                candidate
                for candidate in self._generators
                if not candidate.is_zero()
                and all(
                    (generator / candidate) in self._ring
                    for generator in self._generators
                )
            )

        def is_principal(self: Self) -> bool:
            r"""Return whether the generating family exhibits \(I=(g)\)."""
            return bool(self._dividing_generator())

        def principal_generator(self: Self) -> "Element":
            r"""Return \(g\) with \(I=(g)\)."""
            dividing = self._dividing_generator()
            assert dividing, (
                "this ideal's generating family exhibits no single generator; "
                "deciding principality needs the arithmetic of the ring"
            )
            return dividing[0]

        def as_submodule(self: Self) -> "Subobject":
            r"""Return \(I\hookrightarrow R\), the submodule with its inclusion.

            \(R\) as a module over itself is free of rank one on the framing
            \(\{1\}\), and this ideal is the submodule its generators span
            there -- carried, as every subobject is, by the inclusion rather
            than by membership.

            Integral only: a fractional ideal is an \(R\)-submodule of
            \(\operatorname{Frac}(R)\), and \(\operatorname{Frac}(R)\) is not a
            finitely generated \(R\)-module, so it has no framing here to be a
            subobject of.
            """
            ring = self.ring()
            generators = self.module_generators()
            assert all(generator in ring for generator in generators), (
                "a fractional ideal is a submodule of Frac(R), not of R; "
                "clear its denominator to ask this"
            )
            return ring_as_module(ring).subobject_on(
                [[ring(generator)] for generator in generators]
            )

        def __contains__(self: Self, element: "Element") -> bool:
            if all(generator in self._ring for generator in self._generators):
                return bool(
                    element in self._ring
                    and element in self._ring.ideal(self._generators)
                )

            fractional_ideal = getattr(self._ring, "fractional_ideal", None)
            assert fractional_ideal is not None, (
                f"{self._ring} supplies no fractional-ideal membership algorithm"
            )
            return bool(element in fractional_ideal(self._generators))

        def __hash__(self: Self) -> int:
            return hash((type(self), self._ring, self._generators))

        def __eq__(self: Self, other: "MembershipInput") -> bool:
            return (
                type(other) is type(self)
                and other._ring is self._ring
                and other._generators == self._generators
            )

        def _repr_(self: Self) -> str:
            listed = ", ".join(str(g) for g in self._generators)
            return f"Fractional ideal ({listed}) of {self._ring}"


def FractionalIdeal(ring: "Ring", generators: "OrderedSet") -> Parent:
    r"""Return the \(R\)-submodule of \(\operatorname{Frac}(R)\) on a family."""
    return object_of(OwnedIdeals(ring), ring=ring, generators=generators)


def own_ideal(ideal: "Ideal_generic") -> Parent:
    r"""Return the owned ideal a Sage ideal presents.

    The Sage ideal crosses the boundary once, here, and is asked in its own
    word: it is not a ``Parent`` and cannot be refined into a category, so
    what is owned is the object built from its generators.
    """
    assert isinstance(ideal, Ideal_generic), (
        "an owned ideal is constructed from an actual ideal"
    )
    return FractionalIdeal(ideal.ring(), tuple(ideal.gens()))
