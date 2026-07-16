r"""Cardinals: exact cardinal arithmetic for the owned category of sets.

Sage has no cardinal arithmetic — ``cardinality()`` conflates ``aleph_0``
with ``2^aleph_0`` as ``+Infinity``, erasing exactly the distinction the
owned ``Countable``/``Uncountable`` axioms encode — and sympy owns only
ORDINAL arithmetic (probed 2026-07-16: no aleph/cardinal surface). The
graph therefore owns this vocabulary, adapted from the ``integral_lattice``
spike reference implementation.

The representable cardinals are the ones realized by objects of the owned
graph: exact naturals, ``aleph_0`` (countably infinite), and ``2^aleph_0``
(the continuum). Every uncountable object constructible here (``RR``-like
facades and their finite products and disjoint unions) has continuum
cardinality, so identifying "uncountable" with ``2^aleph_0`` is exact for
this graph, not an approximation; a cardinal beyond the continuum fails
loudly instead of being misrepresented.

Arithmetic is standard cardinal arithmetic: exact on the naturals, with
absorption ``kappa + lam == kappa * lam == max(kappa, lam)`` once an
infinite cardinal is involved (and ``0 * kappa == 0`` always), and powers
following ``kappa ^ aleph_0 == 2^aleph_0`` for ``2 <= kappa <= 2^aleph_0``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ

from ..lexicon import Integer

if TYPE_CHECKING:
    from sage.rings.infinity import PlusInfinity


class Cardinal:
    r"""A cardinal number: an exact natural, ``aleph_0``, or the continuum.

    Immutable value object. Equality and order are cardinal comparisons and
    accept plain naturals and ``+Infinity`` on the other side (``+Infinity``
    normalizes to ``aleph_0``, Sage's countable-blind infinity being read in
    its weakest sense)."""

    __slots__ = ("_value", "_countable")

    _value: Integer | PlusInfinity
    _countable: bool

    def __init__(self, value: object, countable: bool = True) -> None:
        if value == Infinity:
            self._value = Infinity
            self._countable = countable
            return
        exact = ZZ(value)
        assert exact >= 0, f"a cardinal is a nonnegative count; found {exact}"
        self._value = exact
        self._countable = True

    def is_finite(self) -> bool:
        return self._value != Infinity

    def is_infinite(self) -> bool:
        return self._value == Infinity

    def is_countable(self) -> bool:
        return self._countable

    def is_uncountable(self) -> bool:
        return not self._countable

    def is_countably_infinite(self) -> bool:
        return self.is_infinite() and self._countable

    def is_uncountably_infinite(self) -> bool:
        return self.is_infinite() and not self._countable

    def finite_value(self) -> Integer:
        assert self.is_finite(), f"{self} is not a finite cardinal"
        return ZZ(self._value)

    def __repr__(self) -> str:
        if self.is_finite():
            return repr(self._value)
        return "\N{HEBREW LETTER ALEF}_0" if self._countable else "2^\N{HEBREW LETTER ALEF}_0"

    def __hash__(self) -> int:
        # The Python hash law: equality normalizes through cardinal(), so
        # aleph_0 == oo and finite cardinals equal their exact values —
        # hashes must follow (the uncountable cardinal equals neither).
        if self.is_finite():
            return hash(self._value)
        return hash(Infinity) if self._countable else hash(("continuum",))

    def __eq__(self, other: object) -> bool:
        other_cardinal = cardinal(other)
        if self._countable and other_cardinal._countable:
            return bool(self._value == other_cardinal._value)
        return self.is_uncountably_infinite() == other_cardinal.is_uncountably_infinite()

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __lt__(self, other: object) -> bool:
        other_cardinal = cardinal(other)
        if self._countable and other_cardinal._countable:
            return bool(self._value < other_cardinal._value)
        if self.is_uncountably_infinite():
            return False
        return other_cardinal.is_uncountably_infinite()

    def __le__(self, other: object) -> bool:
        return self < other or self == other

    def __gt__(self, other: object) -> bool:
        return not self <= other

    def __ge__(self, other: object) -> bool:
        return not self < other

    @staticmethod
    def _as_cardinal_operand(other: object, operation: str) -> Cardinal:
        r"""Cardinal arithmetic is CLOSED over counts: the operand must be
        a Cardinal, an integer, or the two-valued infinity (read as
        ``aleph_0``). There is no scalar action of a larger ring on the
        cardinals — a rational times a cardinal does not typecheck
        mathematically, so it fails loudly here. Formulas that mix a
        finite-or-infinite count into scalar arithmetic (the determinant
        law ``|det L| = |det O| * [O : L]^2``) live in the EXTENDED
        scalars ``ZZ u {oo}`` and consume the extended-scalar spelling
        (``index()``), never a Cardinal."""
        if isinstance(other, Cardinal):
            return other
        assert other == Infinity or other in ZZ, (
            f"cardinal {operation} takes a count (a Cardinal, an integer, or oo); "
            f"found the non-count scalar {other!r} — extended-scalar formulas consume the extended-scalar spelling instead"
        )
        return cardinal(other)

    def __add__(self, other: object) -> Cardinal:
        other_cardinal = self._as_cardinal_operand(other, "addition")
        if self.is_finite() and other_cardinal.is_finite():
            return Cardinal(self.finite_value() + other_cardinal.finite_value())
        return max(self, other_cardinal)

    def __radd__(self, other: object) -> Cardinal:
        return self + other

    def __mul__(self, other: object) -> Cardinal:
        other_cardinal = self._as_cardinal_operand(other, "multiplication")
        if self == 0 or other_cardinal == 0:
            return Cardinal(ZZ(0))
        if self.is_finite() and other_cardinal.is_finite():
            return Cardinal(self.finite_value() * other_cardinal.finite_value())
        return max(self, other_cardinal)

    def __rmul__(self, other: object) -> Cardinal:
        return self * other

    def __pow__(self, exponent: object) -> Cardinal:
        r"""Cardinal exponentiation within the representable range.

        ``0^0 == 1``; ``0^n == 0`` for ``n >= 1``; ``1^kappa == 1``;
        exact on naturals; ``kappa^n == kappa`` for infinite ``kappa`` and
        finite ``n >= 1``; ``kappa^aleph_0 == 2^aleph_0`` for
        ``2 <= kappa <= 2^aleph_0``. A continuum exponent on a base ``>= 2``
        exceeds the continuum and is refused rather than misrepresented."""
        exponent_cardinal = cardinal(exponent)
        if self == 0:
            return Cardinal(ZZ(1)) if exponent_cardinal == 0 else Cardinal(ZZ(0))
        if self == 1:
            return self
        if exponent_cardinal == 0:
            return Cardinal(ZZ(1))
        if exponent_cardinal.is_finite():
            if self.is_finite():
                return Cardinal(self.finite_value() ** exponent_cardinal.finite_value())
            return self
        assert not exponent_cardinal.is_uncountably_infinite(), f"{self}^{exponent_cardinal} exceeds the continuum and is not representable in this graph"
        return continuum


def cardinal(value: object) -> Cardinal:
    r"""Normalize a cardinal-like value: a ``Cardinal``, a nonnegative
    integer, or ``+Infinity`` (read as ``aleph_0``, its weakest sense)."""
    if isinstance(value, Cardinal):
        return value
    return Cardinal(value)


aleph0 = Cardinal(Infinity, countable=True)
r"""The first infinite cardinal: the cardinality of every countably
infinite set."""

continuum = Cardinal(Infinity, countable=False)
r"""``2^aleph_0``: the cardinality of every uncountable object
constructible in the owned graph."""
