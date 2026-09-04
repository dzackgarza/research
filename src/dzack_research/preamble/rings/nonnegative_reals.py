r"""The additive monoid of nonnegative extended real numbers.

This is \(([0,\infty],+)\): the nonnegative reals together with
\(+\infty\), under addition, with identity \(0\). Addition with
\(\infty\) is absorbing. This is the arithmetic of the nonnegative
part of the extended real line; Hölder degree \(1/p\) of \(L^p\)
takes values in \([0,\infty)\).

The additive monoid \((\mathbb{N},+)\) is the discrete submonoid.
"""

from sage.categories.commutative_additive_monoids import CommutativeAdditiveMonoids
from sage.rings.infinity import Infinity, minus_infinity
from sage.rings.rational_field import QQ
from sage.rings.semirings.non_negative_integer_semiring import NN
from sage.structure.element import Element, parent as sage_parent
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.group.magmas import AdditiveMonoids
from dzack_research.preamble.refine import refine
from dzack_research.preamble.rings.real import RR
from dzack_research.preamble.categories.sets.cardinals import continuum


class NonNegativeReal(Element):
    r"""An element of \(([0,\infty],+)\)."""

    def __init__(self, parent, value) -> None:
        self._value = value
        Element.__init__(self, parent)

    def _repr_(self) -> str:
        return repr(self._value)

    def _latex_(self) -> str:
        if self._value is Infinity:
            return r"\infty"
        return self._value._latex_()

    def _add_(self, other):
        if self._value is Infinity or other._value is Infinity:
            return self.parent()(Infinity)
        return self.parent()(self._value + other._value)

    def __invert__(self):
        r"""The extended-real reciprocal: \(0\leftrightarrow\infty\)."""
        parent = self.parent()
        if self._value is Infinity:
            return parent.zero()
        if self == parent.zero():
            return parent(Infinity)
        return parent(RR.one() / self._value)

    def as_extended_real(self):
        r"""This element as a finite real, or \(+\infty\)."""
        return self._value

    def __hash__(self):
        value = self._value
        if value is Infinity:
            return hash(Infinity)
        try:
            return hash(QQ(value))
        except (TypeError, ValueError):
            return hash(str(value.expression()))

    def _richcmp_(self, other, op):
        if self._value is Infinity and other._value is Infinity:
            return richcmp(0, 0, op)
        if self._value is Infinity:
            return richcmp(1, 0, op)
        if other._value is Infinity:
            return richcmp(0, 1, op)
        return richcmp(self._value, other._value, op)


class NonNegativeReals(UniqueRepresentation, Parent):
    r"""The additive monoid \(([0,\infty],+)\)."""

    Element = NonNegativeReal

    def __init__(self) -> None:
        Parent.__init__(self, category=CommutativeAdditiveMonoids().Infinite())
        refine(self, AdditiveMonoids())

    def _repr_(self) -> str:
        return "Nonnegative extended real numbers"

    def _latex_(self) -> str:
        return r"[0,\infty]"

    def _element_constructor_(self, value):
        if value is Infinity:
            return self.element_class(self, Infinity)
        if value is minus_infinity:
            raise ValueError(f"{value} is negative")
        if sage_parent(value) is self:
            return value
        real = RR(value)
        try:
            atom = real.expression().pyobject()
        except TypeError:
            atom = None
        if atom is Infinity:
            return self.element_class(self, Infinity)
        if atom is minus_infinity:
            raise ValueError(f"{value} is negative")
        nonnegative = real >= RR.zero()
        if nonnegative is True:
            return self.element_class(self, real)
        if nonnegative is False:
            raise ValueError(f"{value} is negative")
        raise TypeError(
            f"nonnegativity of {value} is undecided; use ask({real} >= 0)"
        )

    def __contains__(self, value) -> bool:
        try:
            self(value)
        except ValueError:
            return False
        return True

    def zero(self):
        return self(RR.zero())

    def _an_element_(self):
        return self.zero()

    def cardinality(self):

        return continuum

    def _coerce_map_from_(self, source):
        if source is NN:
            return True
        return None


NonNegativeReals = NonNegativeReals()
