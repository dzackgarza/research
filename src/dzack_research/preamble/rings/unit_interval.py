r"""The monoid \(([0,1],\oplus)\) of Young's inequality.

The operation is \(s\oplus t=s+t-1\), defined when \(s+t\ge 1\), with
identity \(1\). This is the grading of convolution: if \(s=1/p\) and
\(t=1/q\), then \(L^p*L^q\subseteq L^r\) for \(1/r=s\oplus t\). The
identity degree is \(L^1\). Sage encodes this as a multiplicative
monoid (identity ``one()``, not ``zero()``).
"""

from sage.categories.monoids import Monoids as SageMonoids
from sage.rings.rational_field import QQ
from sage.structure.element import Element, parent as sage_parent
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.group.magmas import Monoids
from dzack_research.preamble.refine import refine
from dzack_research.preamble.rings.real import RR


class UnitIntervalElement(Element):
    r"""An element of \(([0,1],\oplus)\)."""

    def __init__(self, parent, value) -> None:
        self._value = value
        Element.__init__(self, parent)

    def _repr_(self) -> str:
        return repr(self._value)

    def _latex_(self) -> str:
        return self._value._latex_()

    def _mul_(self, other):
        total = self._value + other._value - RR.one()
        try:
            return self.parent()(total)
        except ValueError as error:
            raise ValueError(
                f"{self} ⊕ {other} = {total} is not in [0, 1]; "
                "Young's inequality does not supply a convolution degree"
            ) from error

    def as_extended_real(self):
        r"""This element as a real in \([0,1]\)."""
        return self._value

    def __hash__(self):
        try:
            return hash(QQ(self._value))
        except (TypeError, ValueError):
            return hash(str(self._value.expression()))

    def _richcmp_(self, other, op):
        return richcmp(self._value, other._value, op)


class UnitInterval(UniqueRepresentation, Parent):
    r"""The monoid \(([0,1],\oplus)\) with \(s\oplus t=s+t-1\) and identity \(1\)."""

    Element = UnitIntervalElement

    def __init__(self) -> None:
        Parent.__init__(self, category=SageMonoids().Commutative().Infinite())
        refine(self, Monoids())

    def _repr_(self) -> str:
        return "unit interval under s⊕t = s+t-1"

    def _latex_(self) -> str:
        return r"([0,1],\oplus)"

    def _element_constructor_(self, value):
        if sage_parent(value) is self:
            return value
        try:
            value = value.as_extended_real()
        except AttributeError:
            pass
        real = RR(value)
        nonnegative = real >= RR.zero()
        at_most_one = real <= RR.one()
        if nonnegative is False or at_most_one is False:
            raise ValueError(f"{value} is not in [0, 1]")
        if nonnegative is True and at_most_one is True:
            return self.element_class(self, real)
        raise TypeError(
            f"membership of {value} in [0, 1] is undecided; "
            f"use ask(0 <= {real} <= 1)"
        )

    def __contains__(self, value) -> bool:
        try:
            self(value)
        except (TypeError, ValueError):
            return False
        return True

    def one(self):
        return self(RR.one())

    def zero(self):
        r"""The degree of \(L^\infty\), not the monoid identity."""
        return self(RR.zero())

    def _an_element_(self):
        return self.one()

    def cardinality(self):
        from dzack_research.preamble.categories.sets.cardinals import continuum

        return continuum


UnitInterval = UnitInterval()
