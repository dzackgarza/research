r"""Ordinals and the Hessenberg natural semiring operations."""

from __future__ import annotations

from dataclasses import dataclass

from sage.categories.category import Category
from sage.categories.semirings import Semirings
from sage.categories.sets_cat import Sets as SageSets
from sage.misc.cachefunc import cached_function
from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation


@dataclass(frozen=True)
class _FiniteOrdinal:
    value: Integer


@dataclass(frozen=True)
class _InitialOrdinal:
    index: "Ordinal"


@dataclass(frozen=True)
class _NaturalSum:
    terms: tuple["Ordinal", ...]


@dataclass(frozen=True)
class _NaturalProduct:
    factors: tuple["Ordinal", ...]


@dataclass(frozen=True)
class _OrdinalSum:
    left: "Ordinal"
    right: "Ordinal"


@dataclass(frozen=True)
class _OrdinalProduct:
    left: "Ordinal"
    right: "Ordinal"


@dataclass(frozen=True)
class _OrdinalPower:
    base: "Ordinal"
    exponent: "Ordinal"


class OrdinalSemirings(Category):
    r"""The category containing the ordinal semiring under natural operations."""

    def super_categories(self):
        return [SageSets(), Semirings().Commutative()]


class Ordinal(Element):
    r"""An ordinal represented by a symbolic arithmetic expression."""

    def __init__(self, parent, expression) -> None:
        Element.__init__(self, parent)
        self._expression = expression

    def expression(self):
        return self._expression

    def __hash__(self) -> int:
        return hash(self.expression())

    def __eq__(self, other) -> bool:
        try:
            other_ordinal = self.parent()(other)
        except (TypeError, ValueError):
            return False
        return self.expression() == other_ordinal.expression()

    def __ne__(self, other) -> bool:
        return not self == other

    def __le__(self, other) -> bool:
        return self.parent().proves_le(self, other)

    def __lt__(self, other) -> bool:
        target = self.parent()(other)
        return self != target and self <= target

    def __ge__(self, other) -> bool:
        return self.parent().proves_le(other, self)

    def __gt__(self, other) -> bool:
        source = self.parent()(other)
        return self != source and self >= source

    def _add_(self, other):
        return self.parent().natural_sum(self, other)

    def _mul_(self, other):
        return self.parent().natural_product(self, other)

    def __radd__(self, other):
        return self.parent().natural_sum(other, self)

    def __rmul__(self, other):
        return self.parent().natural_product(other, self)

    def ordinal_sum(self, other):
        right = self.parent()(other)
        left_expression = self.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _FiniteOrdinal) and isinstance(
            right_expression, _FiniteOrdinal
        ):
            return self.parent()(left_expression.value + right_expression.value)
        if right == 0:
            return self
        if self == 0:
            return right
        return self.parent().from_expression(_OrdinalSum(self, right))

    def ordinal_product(self, other):
        right = self.parent()(other)
        left_expression = self.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _FiniteOrdinal) and isinstance(
            right_expression, _FiniteOrdinal
        ):
            return self.parent()(left_expression.value * right_expression.value)
        if self == 0 or right == 0:
            return self.parent().zero()
        if right == 1:
            return self
        if self == 1:
            return right
        return self.parent().from_expression(_OrdinalProduct(self, right))

    def ordinal_power(self, exponent):
        power = self.parent()(exponent)
        base_expression = self.expression()
        exponent_expression = power.expression()
        if isinstance(base_expression, _FiniteOrdinal) and isinstance(
            exponent_expression, _FiniteOrdinal
        ):
            return self.parent()(base_expression.value ** exponent_expression.value)
        if power == 0:
            return self.parent().one()
        if self == 0:
            return self.parent().zero()
        if self == 1:
            return self
        return self.parent().from_expression(_OrdinalPower(self, power))

    def is_initial(self) -> bool:
        return isinstance(self.expression(), _InitialOrdinal)

    def initial_index(self):
        expression = self.expression()
        if not isinstance(expression, _InitialOrdinal):
            raise ValueError(f"{self} is not an initial ordinal")
        return expression.index

    def cardinality(self):
        from dzack_research.preamble.categories.sets.cardinals import (
            Cardinalities,
            aleph,
            cardinal,
        )

        expression = self.expression()
        if isinstance(expression, _FiniteOrdinal):
            return cardinal(expression.value)
        if isinstance(expression, _InitialOrdinal):
            return aleph(expression.index)
        if isinstance(expression, (_NaturalSum, _OrdinalSum)):
            terms = (
                expression.terms
                if isinstance(expression, _NaturalSum)
                else (expression.left, expression.right)
            )
            return Cardinalities().sum(*(term.cardinality() for term in terms))
        if isinstance(expression, (_NaturalProduct, _OrdinalProduct)):
            factors = (
                expression.factors
                if isinstance(expression, _NaturalProduct)
                else (expression.left, expression.right)
            )
            return Cardinalities().product(*(factor.cardinality() for factor in factors))
        return Cardinalities().power(
            expression.base.cardinality(), expression.exponent.cardinality()
        )

    def _repr_(self) -> str:
        expression = self.expression()
        if isinstance(expression, _FiniteOrdinal):
            return repr(expression.value)
        if isinstance(expression, _InitialOrdinal):
            return f"ω_{expression.index}"
        if isinstance(expression, _NaturalSum):
            return " # ".join(map(repr, expression.terms))
        if isinstance(expression, _NaturalProduct):
            return " ⊗ ".join(map(repr, expression.factors))
        if isinstance(expression, _OrdinalSum):
            return f"({expression.left} +o {expression.right})"
        if isinstance(expression, _OrdinalProduct):
            return f"({expression.left} *o {expression.right})"
        return f"({expression.base} ^o {expression.exponent})"


class OrdinalSemiring(UniqueRepresentation, Parent):
    Element = Ordinal

    def __init__(self) -> None:
        Parent.__init__(self, category=OrdinalSemirings())

    def _repr_(self) -> str:
        return "Ordinal semiring"

    def from_expression(self, expression) -> Ordinal:
        return self.element_class(self, expression)

    def _element_constructor_(self, value):
        if isinstance(value, Ordinal):
            if value.parent() is self:
                return value
            raise TypeError("an ordinal belongs to the canonical ordinal semiring")
        integer = ZZ(value)
        if integer < 0:
            raise ValueError(f"an ordinal is nonnegative; found {integer}")
        return self.from_expression(_FiniteOrdinal(integer))

    def zero(self) -> Ordinal:
        return self(0)

    def one(self) -> Ordinal:
        return self(1)

    def initial(self, index) -> Ordinal:
        return self.from_expression(_InitialOrdinal(self(index)))

    def natural_sum(self, *summands) -> Ordinal:
        terms: list[Ordinal] = []
        finite_part = ZZ.zero()
        for summand in map(self, summands):
            expression = summand.expression()
            if isinstance(expression, _FiniteOrdinal):
                finite_part += expression.value
            elif isinstance(expression, _NaturalSum):
                terms.extend(expression.terms)
            else:
                terms.append(summand)
        if finite_part:
            terms.append(self(finite_part))
        if not terms:
            return self.zero()
        terms.sort(key=repr)
        if len(terms) == 1:
            return terms[0]
        return self.from_expression(_NaturalSum(tuple(terms)))

    def natural_product(self, *factors) -> Ordinal:
        ordinal_factors = tuple(map(self, factors))
        for index, factor in enumerate(ordinal_factors):
            expression = factor.expression()
            if isinstance(expression, _NaturalSum):
                preceding = ordinal_factors[:index]
                following = ordinal_factors[index + 1 :]
                return self.natural_sum(
                    *(
                        self.natural_product(*preceding, term, *following)
                        for term in expression.terms
                    )
                )
        normalized: list[Ordinal] = []
        finite_part = ZZ.one()
        for factor in ordinal_factors:
            expression = factor.expression()
            if isinstance(expression, _FiniteOrdinal):
                if expression.value == 0:
                    return self.zero()
                finite_part *= expression.value
            elif isinstance(expression, _NaturalProduct):
                normalized.extend(expression.factors)
            else:
                normalized.append(factor)
        if finite_part != 1 or not normalized:
            normalized.append(self(finite_part))
        normalized.sort(key=repr)
        if len(normalized) == 1:
            return normalized[0]
        return self.from_expression(_NaturalProduct(tuple(normalized)))

    def proves_le(self, left, right) -> bool:
        source = self(left)
        target = self(right)
        if source == target:
            return True
        source_expression = source.expression()
        target_expression = target.expression()
        if isinstance(source_expression, _FiniteOrdinal):
            if isinstance(target_expression, _FiniteOrdinal):
                return source_expression.value <= target_expression.value
            return True
        if isinstance(target_expression, _FiniteOrdinal):
            return False
        if isinstance(source_expression, _InitialOrdinal) and isinstance(
            target_expression, _InitialOrdinal
        ):
            return self.proves_le(source_expression.index, target_expression.index)
        return False


@cached_function
def Ordinals() -> OrdinalSemiring:
    return OrdinalSemiring()


def ordinal(value) -> Ordinal:
    return Ordinals()(value)


def omega(index) -> Ordinal:
    return Ordinals().initial(index)


omega0 = omega(0)


__all__ = [
    "Ordinal",
    "OrdinalSemiring",
    "OrdinalSemirings",
    "Ordinals",
    "omega",
    "omega0",
    "ordinal",
]
