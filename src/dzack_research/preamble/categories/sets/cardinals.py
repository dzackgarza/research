r"""Cardinal numbers, cardinal arithmetic, and the thin cardinal-order category."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from typing import TYPE_CHECKING

from sage.categories.category import Category
from sage.categories.homset import Homset
from sage.categories.morphism import Morphism
from sage.categories.objects import Objects
from sage.misc.cachefunc import cached_function
from sage.rings.infinity import Infinity
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ
from sage.structure.parent import Parent

if TYPE_CHECKING:
    from dzack_research.preamble.categories.sets.ordinals import Ordinal


@dataclass(frozen=True)
class _FiniteCardinal:
    value: Integer


@dataclass(frozen=True)
class _AlephCardinal:
    index: "Ordinal"


@dataclass(frozen=True)
class _PowerCardinal:
    base: "Cardinal"
    exponent: "Cardinal"


@dataclass(frozen=True)
class _SupremumCardinal:
    terms: tuple["Cardinal", ...]


@dataclass(frozen=True)
class _IndexedSumCardinal:
    index_set: Parent
    summands: Callable


@dataclass(frozen=True)
class _IndexedProductCardinal:
    index_set: Parent
    factors: Callable


class CardinalComparison(Enum):
    LESS = -1
    EQUAL = 0
    GREATER = 1
    LESS_OR_EQUAL = 2
    GREATER_OR_EQUAL = 3
    INCOMPARABLE = 4


class CardinalityMorphism(Morphism):
    def __init__(self, parent) -> None:
        Morphism.__init__(self, parent)

    def _repr_(self) -> str:
        return f"{self.domain()} <= {self.codomain()}"


class CardinalityHomset(Homset):
    Element = CardinalityMorphism

    def __init__(self, domain, codomain) -> None:
        Homset.__init__(self, domain, codomain, category=Objects())

    def cardinality(self):
        return ZZ.one() if Cardinalities().le(self.domain(), self.codomain()) else ZZ.zero()

    def unique_morphism(self):
        if not Cardinalities().le(self.domain(), self.codomain()):
            raise ValueError(f"there is no cardinality morphism {self.domain()} -> {self.codomain()}")
        return self.element_class(self)

    def _element_constructor_(self, morphism=None):
        if morphism is not None and morphism.parent() is not self:
            raise ValueError(f"{morphism} is not in {self}")
        return self.unique_morphism()

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism homset")
        return self.unique_morphism()


class Cardinalities(Category):
    r"""The thin category associated to the represented cardinal order."""

    def super_categories(self):
        return [Objects()]

    def _repr_(self) -> str:
        return "Category of cardinalities"

    def hom(self, domain, codomain) -> CardinalityHomset:
        return CardinalityHomset(cardinal(domain), cardinal(codomain))

    Hom = hom

    def zero(self):
        return cardinal(0)

    def one(self):
        return cardinal(1)

    def sum(self, *summands):
        result = self.zero()
        for summand in map(cardinal, summands):
            if result.is_finite() and summand.is_finite():
                result = cardinal(result.finite_value() + summand.finite_value())
            elif result.is_finite():
                result = summand
            elif summand.is_infinite():
                result = self.supremum(result, summand)
        return result

    def product(self, *factors):
        result = self.one()
        for factor in map(cardinal, factors):
            if result == 0 or factor == 0:
                return cardinal(0)
            if result.is_finite() and factor.is_finite():
                result = cardinal(result.finite_value() * factor.finite_value())
            elif result.is_finite():
                result = factor
            elif factor.is_infinite():
                result = self.supremum(result, factor)
        return result

    def indexed_sum(self, index_set: Parent, summands: Callable):
        size = cardinal(index_set.cardinality())
        if size.is_finite():
            return self.sum(*(summands(index) for index in index_set))
        return _cardinal_with_expression(_IndexedSumCardinal(index_set, summands))

    def indexed_product(self, index_set: Parent, factors: Callable):
        size = cardinal(index_set.cardinality())
        if size.is_finite():
            return self.product(*(factors(index) for index in index_set))
        return _cardinal_with_expression(_IndexedProductCardinal(index_set, factors))

    def power(self, base, exponent):
        cardinal_base = cardinal(base)
        cardinal_exponent = cardinal(exponent)
        if cardinal_exponent == 0:
            return cardinal(1)
        if cardinal_base == 0:
            return cardinal(0)
        if cardinal_base == 1:
            return cardinal(1)
        if cardinal_exponent.is_finite():
            if cardinal_base.is_finite():
                return cardinal(cardinal_base.finite_value() ** cardinal_exponent.finite_value())
            return cardinal_base
        if cardinal_base.is_finite() or self.le(cardinal_base, cardinal_exponent):
            cardinal_base = cardinal(2)
        exponent_expression = cardinal_exponent.expression()
        if isinstance(exponent_expression, _SupremumCardinal):
            return self.supremum(
                *(self.power(cardinal_base, term) for term in exponent_expression.terms)
            )
        base_expression = cardinal_base.expression()
        if isinstance(base_expression, _SupremumCardinal):
            return self.supremum(
                *(self.power(term, cardinal_exponent) for term in base_expression.terms)
            )
        if isinstance(base_expression, _PowerCardinal):
            return self.power(
                base_expression.base,
                self.product(base_expression.exponent, cardinal_exponent),
            )
        return _cardinal_with_expression(_PowerCardinal(cardinal_base, cardinal_exponent))

    def supremum(self, *cardinal_numbers):
        terms: list[Cardinal] = []
        for cardinal_number in map(cardinal, cardinal_numbers):
            expression = cardinal_number.expression()
            if isinstance(expression, _SupremumCardinal):
                terms.extend(expression.terms)
            else:
                terms.append(cardinal_number)
        if not terms:
            raise ValueError("a finite supremum needs at least one cardinal")
        maximal_terms: list[Cardinal] = []
        for candidate in sorted(set(terms), key=Cardinal.sort_key):
            if any(self.le(candidate, term) for term in maximal_terms):
                continue
            maximal_terms = [term for term in maximal_terms if not self.le(term, candidate)]
            maximal_terms.append(candidate)
        maximal_terms.sort(key=Cardinal.sort_key)
        if len(maximal_terms) == 1:
            return maximal_terms[0]
        return _cardinal_with_expression(_SupremumCardinal(tuple(maximal_terms)))

    def le(self, source, target) -> bool:
        left = cardinal(source)
        right = cardinal(target)
        if left == right:
            return True
        left_expression = left.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _SupremumCardinal):
            return all(self.le(term, right) for term in left_expression.terms)
        if isinstance(right_expression, _SupremumCardinal):
            return any(self.le(left, term) for term in right_expression.terms)
        if isinstance(left_expression, (_IndexedSumCardinal, _IndexedProductCardinal)) or isinstance(
            right_expression, (_IndexedSumCardinal, _IndexedProductCardinal)
        ):
            return False
        if left.is_finite():
            if right.is_finite():
                return left.finite_value() <= right.finite_value()
            return True
        if right.is_finite():
            return False
        if left.is_aleph() and right.is_aleph():
            return left.aleph_index() <= right.aleph_index()
        if left.is_countably_infinite():
            return True
        if left.is_aleph() and left.aleph_index() == 1 and right.is_uncountable():
            return True
        if isinstance(right_expression, _PowerCardinal):
            if self.le(left, right_expression.base):
                return True
            if self.le(cardinal(2), right_expression.base) and self.le(
                left, right_expression.exponent
            ):
                return True
            if isinstance(left_expression, _PowerCardinal):
                return self.le(left_expression.base, right_expression.base) and self.le(
                    left_expression.exponent, right_expression.exponent
                )
        return False

    def lt(self, source, target) -> bool:
        left = cardinal(source)
        right = cardinal(target)
        if left == right:
            return False
        left_expression = left.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _SupremumCardinal):
            return all(self.lt(term, right) for term in left_expression.terms)
        if isinstance(right_expression, _SupremumCardinal):
            return any(self.lt(left, term) for term in right_expression.terms)
        if isinstance(left_expression, (_IndexedSumCardinal, _IndexedProductCardinal)) or isinstance(
            right_expression, (_IndexedSumCardinal, _IndexedProductCardinal)
        ):
            return False
        if left.is_finite():
            if right.is_finite():
                return left.finite_value() < right.finite_value()
            return True
        if right.is_finite():
            return False
        if left.is_aleph() and right.is_aleph():
            return left.aleph_index() < right.aleph_index()
        if left.is_countably_infinite() and right.is_uncountable():
            return True
        if isinstance(right_expression, _PowerCardinal):
            return self.le(cardinal(2), right_expression.base) and self.le(
                left, right_expression.exponent
            )
        return False

    def ge(self, source, target) -> bool:
        return self.le(target, source)

    def gt(self, source, target) -> bool:
        return self.lt(target, source)

    def compare(self, source, target) -> CardinalComparison:
        left = cardinal(source)
        right = cardinal(target)
        if left == right:
            return CardinalComparison.EQUAL
        if self.lt(left, right):
            return CardinalComparison.LESS
        if self.lt(right, left):
            return CardinalComparison.GREATER
        if self.le(left, right):
            return CardinalComparison.LESS_OR_EQUAL
        if self.le(right, left):
            return CardinalComparison.GREATER_OR_EQUAL
        return CardinalComparison.INCOMPARABLE

    def are_incomparable(self, source, target) -> bool:
        return not self.le(source, target) and not self.le(target, source)


class Cardinal(Parent):
    r"""A cardinal number as an object of the thin cardinal-order category."""

    def __init__(self, expression) -> None:
        self._expression = expression
        Parent.__init__(self, category=Cardinalities())

    def expression(self):
        return self._expression

    def cardinality(self):
        return self

    def sort_key(self) -> tuple[int, str]:
        expression = self.expression()
        if isinstance(expression, _FiniteCardinal):
            return (0, str(expression.value))
        if isinstance(expression, _AlephCardinal):
            return (1, str(expression.index))
        if isinstance(expression, _PowerCardinal):
            return (2, repr(self))
        if isinstance(expression, _SupremumCardinal):
            return (3, repr(self))
        return (4, repr(self))

    def _repr_(self) -> str:
        expression = self.expression()
        if isinstance(expression, _FiniteCardinal):
            return repr(expression.value)
        if isinstance(expression, _AlephCardinal):
            return f"ℵ_{expression.index}"
        if isinstance(expression, _PowerCardinal):
            return f"({expression.base})^({expression.exponent})"
        if isinstance(expression, _SupremumCardinal):
            return "sup(" + ", ".join(map(str, expression.terms)) + ")"
        if isinstance(expression, _IndexedSumCardinal):
            return f"sum_{{i in {expression.index_set}}} kappa_i"
        return f"prod_{{i in {expression.index_set}}} kappa_i"

    def __hash__(self) -> int:
        if self.is_finite():
            return hash(self.finite_value())
        if self.is_countably_infinite():
            return hash(Infinity)
        return hash(self.expression())

    def __eq__(self, other) -> bool:
        try:
            return self.expression() == cardinal(other).expression()
        except (TypeError, ValueError):
            return False

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        return Cardinalities().lt(self, other)

    def __le__(self, other) -> bool:
        return Cardinalities().le(self, other)

    def __gt__(self, other) -> bool:
        return Cardinalities().gt(self, other)

    def __ge__(self, other) -> bool:
        return Cardinalities().ge(self, other)

    def __add__(self, other):
        return Cardinalities().sum(self, other)

    __radd__ = __add__

    def __mul__(self, other):
        return Cardinalities().product(self, other)

    __rmul__ = __mul__

    def __pow__(self, exponent):
        return Cardinalities().power(self, exponent)

    def __rpow__(self, base):
        return Cardinalities().power(base, self)

    def is_finite(self) -> bool:
        expression = self.expression()
        if isinstance(expression, (_IndexedSumCardinal, _IndexedProductCardinal)):
            raise NotImplementedError(
                "finiteness of an arbitrary indexed cardinal family is not decidable"
            )
        return isinstance(expression, _FiniteCardinal)

    def is_infinite(self) -> bool:
        return not self.is_finite()

    def is_aleph(self) -> bool:
        return isinstance(self.expression(), _AlephCardinal)

    def is_continuum(self) -> bool:
        expression = self.expression()
        return bool(
            isinstance(expression, _PowerCardinal)
            and expression.base == 2
            and expression.exponent.is_countably_infinite()
        )

    def is_countable(self) -> bool:
        return self.is_finite() or self.is_countably_infinite()

    def is_uncountable(self) -> bool:
        expression = self.expression()
        if isinstance(expression, (_IndexedSumCardinal, _IndexedProductCardinal)):
            raise NotImplementedError(
                "countability of an arbitrary indexed cardinal family is not decidable"
            )
        if self.is_finite() or self.is_countably_infinite():
            return False
        if isinstance(expression, _SupremumCardinal):
            return any(term.is_uncountable() for term in expression.terms)
        return True

    def is_countably_infinite(self) -> bool:
        expression = self.expression()
        return isinstance(expression, _AlephCardinal) and expression.index == 0

    def is_uncountably_infinite(self) -> bool:
        return self.is_infinite() and self.is_uncountable()

    def aleph_index(self):
        expression = self.expression()
        if not isinstance(expression, _AlephCardinal):
            raise ValueError(f"{self} is not an aleph cardinal")
        return expression.index

    def initial_ordinal(self):
        from dzack_research.preamble.categories.sets.ordinals import omega
        return omega(self.aleph_index())

    def finite_value(self) -> Integer:
        expression = self.expression()
        if not isinstance(expression, _FiniteCardinal):
            raise ValueError(f"{self} is not a finite cardinal")
        return expression.value

    def __int__(self) -> int:
        if not self.is_finite():
            raise TypeError(f"cannot convert infinite cardinal {self} to integer")
        return int(self.finite_value())

    def __index__(self) -> int:
        return int(self)

    def _integer_(self, ring=None) -> Integer:
        if not self.is_finite():
            raise TypeError(f"cannot convert infinite cardinal {self} to Sage Integer")
        return self.finite_value()

    def _rational_(self):
        if not self.is_finite():
            raise TypeError(f"cannot convert infinite cardinal {self} to Sage Rational")
        return QQ(self.finite_value())


@cached_function
def _cardinal_with_expression(expression) -> Cardinal:
    return Cardinal(expression)


def cardinal(value) -> Cardinal:
    if isinstance(value, Cardinal):
        return value
    if value == Infinity:
        return aleph(0)
    integer = ZZ(value)
    if integer < 0:
        raise ValueError(f"a cardinal is nonnegative; found {integer}")
    return _cardinal_with_expression(_FiniteCardinal(integer))


def aleph(index) -> Cardinal:
    from dzack_research.preamble.categories.sets.ordinals import ordinal
    return _cardinal_with_expression(_AlephCardinal(ordinal(index)))


aleph0 = aleph(0)
continuum = cardinal(2) ** aleph0


__all__ = [
    "Cardinal",
    "CardinalComparison",
    "Cardinalities",
    "CardinalityHomset",
    "CardinalityMorphism",
    "aleph",
    "aleph0",
    "cardinal",
    "continuum",
]
