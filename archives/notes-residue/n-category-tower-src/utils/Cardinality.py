# Origin: gitclones/integral_lattice/cat/src/utils/Cardinality.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

from __future__ import annotations

from src.local_typing import *
from src._sage_types import SageType, SageTypeChecks

# Convenience aliases
Infinity = SageType.Infinity
NN_U_infty = SageType.NN_U_infty


@dataclass
class CardinalityClass:
    """
    A class representing the cardinality of a set, which can be finite or infinite (countable or uncountable).
    EXAMPLES::
        sage: from cat.implementations.Cardinality import Cardinality
        sage: c1 = cardinality(5)
        sage: c2 = cardinality(Infinity, is_countable=True)
        sage: c3 = cardinality(Infinity, is_countable=False)
        sage: c1.is_finite()
        True
        sage: c2.is_countably_infinite()
        True
        sage: c3.is_uncountably_infinite()
        True
        sage: c1 + c2
        ℵ_0
        sage: c2 + c3
        2^{ℵ_0}
        sage: c1 * c2
        ℵ_0
        sage: c2 * c3
        2^{ℵ_0}
        sage: c1 < c2 and c2 < c3 and c1 < c3 and c2 != c3
        True
        sage: c2 * c2 == c2 and c1 + c2 == c2 and c2^(10) == c2 and c2^c2 == c2
        True
        sage: c3 * c3 == c3 and c1 + c3 == c3 and c3^(10) == c3 and c3^c3 == c3
        True
        sage: c4 = cardinality(Infinity, is_countable=False)
        sage: c3 == c4 and c3 + c4 == c4 and c3 * c4 == c4
        True
    """

    value: NN_U_infty
    countable: bool = True

    def __lt__(self, other: object) -> bool:
        return self.__richcmp__(other, SageType.op_LT)

    def __le__(self, other: object) -> bool:
        return self.__richcmp__(other, SageType.op_LE)

    def __gt__(self, other: object) -> bool:
        return self.__richcmp__(other, SageType.op_GT)

    def __ge__(self, other: object) -> bool:
        return self.__richcmp__(other, SageType.op_GE)

    def __eq__(self, other: object) -> bool:
        return self.__richcmp__(other, SageType.op_EQ)

    def __ne__(self, other: object) -> bool:
        return self.__richcmp__(other, SageType.op_NE)

    def is_finite(self: Self) -> bool:
        return self.value < Infinity

    def is_infinite(self) -> bool:
        return self.value == Infinity

    def is_countable(self) -> bool:
        return self.countable

    def is_uncountable(self) -> bool:
        return self.value == Infinity and not self.is_countable()

    def is_countably_infinite(self) -> bool:
        return self.is_infinite() and self.is_countable()

    def is_uncountably_infinite(self) -> bool:
        return self.is_infinite() and self.is_uncountable()

    def __richcmp__(self, other: object, op: int) -> bool:
        other_card = cardinality(other)
        match op:
            case _ if op == SageType.op_LT:
                return self.lt(other_card)
            case _ if op == SageType.op_LE:
                return self.lt(other_card) or self.eq(other_card)
            case _ if op == SageType.op_EQ:
                return self.eq(other_card)
            case _ if op == SageType.op_NE:
                return not self.eq(other_card)
            case _ if op == SageType.op_GT:
                return not self.lt(other_card) and not self.eq(other_card)
            case _ if op == SageType.op_GE:
                return not self.lt(other_card)
            case _:
                assert_never(cast("Never", op))

    def eq(self, other: object) -> bool:
        other_card = cardinality(other)
        if self.is_countable() and other_card.is_countable():
            assert SageTypeChecks.is_natural_number_or_infinity(self.value), "Coding error."
            return self.value == other_card.value
        else:
            assert self.is_uncountable() or other_card.is_uncountable(), "Coding error."
            return self.is_uncountably_infinite() == other_card.is_uncountably_infinite()

    def lt(self, other: object) -> bool:
        other_card = cardinality(other)
        if self.is_countable() and other_card.is_countable():
            return bool(self.value < other_card.value)
        assert (
            self.is_uncountably_infinite() or other_card.is_uncountably_infinite()
        ), "Coding error."
        if self.is_uncountably_infinite() and other_card.is_uncountably_infinite():
            # self == other
            return False
        assert self != other_card, "Coding error."
        return bool(other_card.is_uncountably_infinite())

    def __add__(self, other: object) -> CardinalityClass:
        other_card = cardinality(other)
        if self.is_countable() and other_card.is_countable():
            return cardinality(self.value + other_card.value, countable=True)
        else:
            assert (
                self.is_uncountably_infinite() or other_card.is_uncountably_infinite()
            ), "Coding error."
            return max(self, other_card)

    def __mul__(self, other: object) -> CardinalityClass:
        other_card = cardinality(other)
        if self.is_countable() and other_card.is_countable():
            return cardinality(self.value * other_card.value)
        else:
            assert (
                self.is_uncountably_infinite() or other_card.is_uncountably_infinite()
            ), "Coding error."
            return max(self, other_card)

    def __pow__(self, n: Any) -> CardinalityClass:
        """
        Conventions:
        - 0^0 = 1
        - 0^n = 0 for any cardinality n >= 1
        - c^0 = 1 for any cardinality c >= 1
        - c^1 = c for any cardinality c >= 0
        - For finite n >= 2, c^n = c*c*.....*c (n times)
        - If c is finite and n is infinite, the result is uncountably infinite.
        - If both c and n are infinite, the result is uncountably infinite.
        """
        n = cardinality(n)
        if self == 0:
            return cardinality(0) if n != 0 else cardinality(1)
        elif self == 1:
            return self
        else:
            match n.value:
                case 0:
                    return cardinality(1)
                case 1:
                    return self
                case n if n in SageType.NN:
                    return reduce(lambda a, b: a * b, [self] * int(n))
                case n if n == Infinity:
                    return cardinality(Infinity, countable=False)
                case _:
                    assert_never(cast("Never", n))

    def __repr__(self) -> str:
        val: str = ""
        match self.value:
            case v if v in SageType.NN:
                val = f"{v}"
            case v if v == Infinity:
                val = "ℵ_0" if self.is_countable() else "2^{ℵ_0}"
            case _:
                assert_never(cast("Never", self.value))
        return f"{val}"


def cardinality(data: Any, countable: bool = True) -> CardinalityClass:
    """
    Factory function to create CardinalityClass instances.
    """
    match data:
        case v if isinstance(v, CardinalityClass):
            return v
        case v if SageTypeChecks.is_natural_number(v):
            # Assume Cardinality(Infinity) is countable unless specified otherwise
            return CardinalityClass(v, countable=True)
        case v if v == Infinity:
            return CardinalityClass(v, countable=countable)
        case v if SageTypeChecks.has_cardinality(v) and v.cardinality() < Infinity:
            return CardinalityClass(v.cardinality(), countable=True)
        # Handle infinite rings and sets with known cardinalities
        case v if v == SageType.Primes:
            return CardinalityClass(Infinity, countable=True)
        case v if SageTypeChecks.is_number_field(v) and SageTypeChecks.has_degree(v):
            return CardinalityClass(Infinity, countable=SageTypeChecks.is_natural_number(v.degree()))
        case v if SageTypeChecks.is_padic_ring(v):
            return CardinalityClass(Infinity, countable=False)
        case v if SageTypeChecks.is_ring(v):
            return _get_ring_cardinality(v, countable=countable)
        case v if SageTypeChecks.is_matrix_group(v):
            return _get_ring_cardinality(v, countable=countable)
        case v if SageTypeChecks.is_power_set(v):
            # If v is the powerset of a set and is infinite, then the original set must
            # have been countably infinite, and so the powerset is uncountably infinite.
            return CardinalityClass(v.cardinality(), countable=bool(v.cardinality() in SageType.NN))
        # Trust finite order methods (e.g. for Graphs, Groups)
        case v if SageTypeChecks.has_order(v) and v.order() < Infinity:
            return CardinalityClass(v.order(), countable=True)
        case v if SageTypeChecks.has_cardinality(v) and v.cardinality() == Infinity:
            # This handles is_set, since all sets have cardinality()
            print("Warning: only an infinite set structure detected; assuming countable cardinality.")
            return CardinalityClass(v.cardinality(), countable=countable)
        case v if SageTypeChecks.has_order(v) and v.order() == Infinity:
            # This handles e.g. monoids, which have order() but not cardinality()
            print("Warning: only an infinite set structure detected; assuming countable cardinality.")
            return CardinalityClass(v.order(), countable=countable)
        case _:
            assert_never(cast("Never", data))


def _get_ring_cardinality(v: Any, countable: bool = True) -> CardinalityClass:
    match v:
        case v if v in [SageType.NN, SageType.ZZ, SageType.QQ, SageType.QQbar]:
            return CardinalityClass(Infinity, countable=True)
        case v if v in [
            SageType.RR,
            SageType.CC,
            SageType.Subsets(SageType.NN),
            SageType.Subsets(SageType.ZZ),
            SageType.Subsets(SageType.QQ),
            SageType.Subsets(SageType.QQbar),
            SageType.AA,
        ]:
            return CardinalityClass(Infinity, countable=False)
        case v if (
            SageTypeChecks.is_power_series_ring(v)
            or SageTypeChecks.is_matrix_ring(v)
            or SageTypeChecks.is_polynomial_ring(v)
            or SageTypeChecks.is_multivariate_polynomial_ring(v)
            or SageTypeChecks.is_matrix_group(v)
        ) and SageTypeChecks.has_base_ring(v):
            # A polynomial, power series, or matrix ring over a countable base ring is countable
            # and uncountable over an uncountable base ring.
            base_ring_val = v.base_ring()
            # Recursively get the cardinality of the base ring.
            # We don't use has_cardinality() because sage rings don't implement
            # our Protocol - we handle them directly in get_ring_cardinality.
            return _get_ring_cardinality(base_ring_val, countable=countable)
        case _:
            assert_never(cast("Never", v))
