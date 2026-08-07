r"""Ideals and fractional ideals of a commutative ring, as \(R\)-modules.

An ideal \(I\subseteq R\) is an \(R\)-submodule of \(R\); a fractional ideal
is an \(R\)-submodule of \(\operatorname{Frac}(R)\) admitting a common
denominator.  Both are the same object with a different ambient, which is
why one class carries them: what changes is where the generators live.

The generating family is the ideal's own -- ``gens`` and
``module_generators`` are the same family read in the two vocabularies, and
this object exists so that reading is a fact rather than a coincidence.
"""

from sage.rings.ideal import Ideal_generic
from sage.structure.parent import Parent


class FractionalIdeal(Parent):
    r"""The \(R\)-submodule of \(\operatorname{Frac}(R)\) on a finite family."""

    def __init__(self, ring: "Ring", generators: "OrderedSet") -> None:
        self._ring = ring
        self._ambient = ring.fraction_field()
        # The generating family is kept as given.  An integral ideal's
        # generators are elements of R and a fractional ideal's are not;
        # moving them all into Frac(R) would replace the ideal's own family
        # with a copy of it, which is the one thing this object must not do.
        self._generators = finite_ordered_set(generators)
        Parent.__init__(self, base=ring, category=Modules(ring))

    def ring(self) -> "Ring":
        r"""Return \(R\), the ring this is an ideal of."""
        return self._ring

    def gens(self) -> "OrderedSet":
        return self._generators

    def module_generators(self) -> "OrderedSet":
        r"""Return the generating family, read as module generators.

        An ideal's generators generate it as an \(R\)-module: the two words
        name one family, and that is the content here.
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

    def _dividing_generator(self) -> "OrderedSet":
        r"""Return the generators that divide the whole family.

        A supplied family need not be minimal -- an order hands back a module
        basis of \((2)\), not the single ideal generator -- so a generator
        dividing the whole family generates the ideal by itself.
        """
        return finite_ordered_set(
            [
                candidate
                for candidate in self._generators
                if not candidate.is_zero()
                and all(
                    (generator / candidate) in self._ring
                    for generator in self._generators
                )
            ]
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

    def __eq__(self, other: object) -> bool:
        return (
            type(other) is type(self)
            and other._ring is self._ring
            and other._generators == self._generators
        )

    def _repr_(self) -> str:
        listed = ", ".join(str(g) for g in self._generators)
        return f"Fractional ideal ({listed}) of {self._ring}"


def own_ideal(ideal: "Ideal_generic") -> FractionalIdeal:
    r"""Return the owned fractional ideal a Sage ideal presents."""
    assert isinstance(ideal, Ideal_generic), (
        "an owned ideal is constructed from an actual ideal"
    )
    return FractionalIdeal(ideal.ring(), tuple(ideal.gens()))
