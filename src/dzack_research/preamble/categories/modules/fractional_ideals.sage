r"""Ideals and fractional ideals of a commutative ring, as \(R\)-modules.

An ideal \(I\subseteq R\) is an \(R\)-submodule of \(R\); a fractional ideal
is an \(R\)-submodule of \(\operatorname{Frac}(R)\) admitting a common
denominator.  Both are the same object with a different ambient, which is
why one class carries them: what changes is where the generators live.

The generating family is the ideal's own -- ``gens`` and
``module_generators`` are the same family read in the two vocabularies, and
this object exists so that reading is a fact rather than a coincidence.
"""

from typing import Protocol, TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput
if TYPE_CHECKING:
    from dzack_research.preamble.lexicon import Element
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import OrderedSet

from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import BasedFreeModule
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.sets.owned_sets import Sets
from dzack_research.preamble.categories.rings.rings import engine_ring
if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.rings.ring import Ring
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobject

from dzack_research.preamble.categories.rings.rings import OwnedCategoryOverBaseRing
from dzack_research.preamble.categories.rings.rings import OwnedBaseRing
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings
from sage.rings.ideal import Ideal_generic
from sage.structure.parent import Parent


_RING_AS_MODULE: dict = {}


def ring_as_module(ring: "Ring") -> "Module":
    r"""Return \(R\) as a module over itself: free of rank one on \(\{1\}\).

    One object per ring, and that is the point rather than an optimisation.
    A framed free module carries value equality, so two separately built
    copies of \(R\) compare equal while being distinct -- and a morphism
    checks that its images belong to *its* codomain, which the copy is not.
    Every submodule of \(R\) is taken inside this one.
    """
    # One object per ring means per ring, not per name for it: the owned view
    # and the engine's copy are the same \(R\), and keying them apart would
    # build the second copy this function exists to prevent.
    ring = engine_ring(ring)
    module = _RING_AS_MODULE.get(ring)
    if module is None:
        module = BasedFreeModule(ring, Sets.Δ[0])
        _RING_AS_MODULE[ring] = module
    return module


class FractionalIdeal(OwnedBaseRing, Parent):
    r"""The \(R\)-submodule of \(\operatorname{Frac}(R)\) on a finite family."""

    def __init__(self, ring: "Ring", generators: "OrderedSet") -> None:
        ring = engine_ring(ring)
        self._ring = ring
        self._ambient = ring.fraction_field()
        # The generating family is kept as given, and kept as a tuple.  An
        # integral ideal's generators are elements of R and a fractional
        # ideal's are not; moving them all into Frac(R) would replace the
        # ideal's own family with a copy of it, which is the one thing this
        # object must not do -- and an ordered *set* does exactly that, since
        # its parent is cached by the values it holds, so \(1\in R\) is served
        # back as whichever equal \(1\) built that set first.  A family of
        # ring elements is carried by the ring, not by a set of numbers.
        self._generators = tuple(generators)
        # Placed as what it is: a submodule of R, so the category says
        # module and the object answers ``as_submodule`` with the
        # inclusion that carries it.
        Parent.__init__(self, base=ring, category=OwnedIdeals(ring))

    def ring(self) -> "Ring":
        r"""Return \(R\), the ring this is an ideal of."""
        return self._ring

    def _ring_morphism_defining_module_action(self) -> "Morphism":
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

    def module_generators(self) -> tuple:
        r"""Return the generating family, read as module generators.

        An ideal's generators generate it as an \(R\)-module: the two words
        name one family, and that is the content here.  The family is the
        one supplied, its members still elements of \(R\).
        """
        return self._generators

    def inverse(self) -> "FractionalIdeal":
        r"""Return \(I^{-1}=\{x\in\operatorname{Frac}(R):xI\subseteq R\}\).

        For \(I=(g)\) this is \((g^{-1})\), which is the whole of the
        computation.  A non-principal ideal's inverse needs the Dedekind
        arithmetic of \(R\), which this object does not carry.
        """
        generator = self.principal_generator()
        assert not generator.is_zero(), "the zero ideal is not invertible"
        return FractionalIdeal(self._ring, (~self._ambient(generator),))

    def _dividing_generator(self) -> tuple:
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

    def is_principal(self) -> bool:
        r"""Return whether the generating family exhibits \(I=(g)\)."""
        return bool(self._dividing_generator())

    def principal_generator(self) -> "Element":
        r"""Return \(g\) with \(I=(g)\)."""
        dividing = self._dividing_generator()
        assert dividing, (
            "this ideal's generating family exhibits no single generator; "
            "deciding principality needs the arithmetic of the ring"
        )
        return dividing[0]

    def __contains__(self, element: "Element") -> bool:
        return element in self._ambient and any(
            (self._ambient(element) / generator) in self._ring
            for generator in self._generators
        )

    def __hash__(self) -> int:
        return hash((type(self), self._ring, self._generators))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and other._ring is self._ring
            and other._generators == self._generators
        )

    def _repr_(self) -> str:
        listed = ", ".join(str(g) for g in self._generators)
        return f"Fractional ideal ({listed}) of {self._ring}"


if TYPE_CHECKING:
    class IdealParent(Protocol):
        r"""What a parent placed in ``OwnedIdeals(R)`` supplies."""

        def ring(self) -> "Ring": ...
        def module_generators(self) -> "OrderedSet": ...


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

    class ParentMethods:
        def as_submodule(self: "IdealParent") -> "Subobject":
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


def own_ideal(ideal: "Ideal_generic") -> FractionalIdeal:
    r"""Return the owned ideal a Sage ideal presents.

    The Sage ideal crosses the boundary once, here, and is asked in its own
    word: it is not a ``Parent`` and cannot be refined into a category, so
    what is owned is the object built from its generators.
    """
    assert isinstance(ideal, Ideal_generic), (
        "an owned ideal is constructed from an actual ideal"
    )
    return FractionalIdeal(ideal.ring(), tuple(ideal.gens()))
