r"""Ordinals, initial ordinals, and their natural semiring operations.

Ordinary ordinal addition is not commutative.  The operations ``+`` and ``*``
on :class:`Ordinal` are therefore the Hessenberg natural sum and product.
They form the commutative semiring of ordinals.  The noncommutative ordinal
operations remain available as :meth:`Ordinal.ordinal_sum` and
:meth:`Ordinal.ordinal_product`.

``omega(alpha)`` denotes the initial ordinal ``omega_alpha``.  Its cardinal
is ``aleph(alpha)``.  The expression model follows Mathlib's mature ordinal
and cardinal implementation in ``SetTheory/Ordinal/Arithmetic.lean`` and
``SetTheory/Cardinal/Defs.lean``.
"""

from __future__ import annotations

from dataclasses import dataclass

from sage.categories.semirings import Semirings
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
    index: Ordinal


@dataclass(frozen=True)
class _NaturalSum:
    terms: tuple[Ordinal, ...]


@dataclass(frozen=True)
class _NaturalProduct:
    factors: tuple[Ordinal, ...]


@dataclass(frozen=True)
class _OrdinalSum:
    left: Ordinal
    right: Ordinal


@dataclass(frozen=True)
class _OrdinalProduct:
    left: Ordinal
    right: Ordinal


@dataclass(frozen=True)
class _OrdinalPower:
    base: Ordinal
    exponent: Ordinal


type _OrdinalExpression = (
    _FiniteOrdinal
    | _InitialOrdinal
    | _NaturalSum
    | _NaturalProduct
    | _OrdinalSum
    | _OrdinalProduct
    | _OrdinalPower
)
type OrdinalInput = Ordinal | Integer | int


class Ordinals(UniqueRepresentation, Parent):
    r"""The Sage parent of ordinals with natural semiring arithmetic."""

    def __init__(self) -> None:
        Parent.__init__(self, category=Semirings().Commutative())

    def _repr_(self) -> str:
        return "Ordinal semiring"

    def _element_constructor_(self, value: OrdinalInput) -> Ordinal:
        if isinstance(value, Ordinal):
            return value
        integer = ZZ(value)
        if integer < 0:
            raise ValueError(f"an ordinal is nonnegative; found {integer}")
        return Ordinal(self, _FiniteOrdinal(integer))

    def zero(self) -> Ordinal:
        return self(0)

    def one(self) -> Ordinal:
        return self(1)

    def initial(self, index: OrdinalInput) -> Ordinal:
        r"""Return the initial ordinal ``omega_index``."""
        return Ordinal(self, _InitialOrdinal(self(index)))

    def natural_sum(self, *summands: OrdinalInput) -> Ordinal:
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
        return Ordinal(self, _NaturalSum(tuple(terms)))

    def natural_product(self, *factors: OrdinalInput) -> Ordinal:
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
        return Ordinal(self, _NaturalProduct(tuple(normalized)))

    def proves_le(self, left: OrdinalInput, right: OrdinalInput) -> bool:
        r"""Return whether the represented ordinal theory proves ``left <= right``."""
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


class Ordinal(Element):
    r"""An ordinal in the natural semiring."""

    def __init__(self, parent: Ordinals, expression: _OrdinalExpression) -> None:
        self._expression = expression
        Element.__init__(self, parent)

    def expression(self) -> _OrdinalExpression:
        return self._expression

    def __hash__(self) -> int:
        return hash(self.expression())

    def __eq__(self, other: OrdinalInput) -> bool:
        return self.expression() == Ordinals()(other).expression()

    def __ne__(self, other: OrdinalInput) -> bool:
        return not self == other

    def __le__(self, other: OrdinalInput) -> bool:
        return Ordinals().proves_le(self, other)

    def __lt__(self, other: OrdinalInput) -> bool:
        target = Ordinals()(other)
        return self != target and self <= target

    def __ge__(self, other: OrdinalInput) -> bool:
        return Ordinals().proves_le(other, self)

    def __gt__(self, other: OrdinalInput) -> bool:
        source = Ordinals()(other)
        return self != source and self >= source

    def __add__(self, other: OrdinalInput) -> Ordinal:
        return Ordinals().natural_sum(self, other)

    def __radd__(self, other: OrdinalInput) -> Ordinal:
        return Ordinals().natural_sum(other, self)

    def __mul__(self, other: OrdinalInput) -> Ordinal:
        return Ordinals().natural_product(self, other)

    def __rmul__(self, other: OrdinalInput) -> Ordinal:
        return Ordinals().natural_product(other, self)

    def ordinal_sum(self, other: OrdinalInput) -> Ordinal:
        r"""Return the ordinary ordinal sum."""
        right = Ordinals()(other)
        left_expression = self.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _FiniteOrdinal) and isinstance(
            right_expression, _FiniteOrdinal
        ):
            return Ordinals()(left_expression.value + right_expression.value)
        if right == 0:
            return self
        if self == 0:
            return right
        return Ordinal(Ordinals(), _OrdinalSum(self, right))

    def ordinal_product(self, other: OrdinalInput) -> Ordinal:
        r"""Return the ordinary ordinal product."""
        right = Ordinals()(other)
        left_expression = self.expression()
        right_expression = right.expression()
        if isinstance(left_expression, _FiniteOrdinal) and isinstance(
            right_expression, _FiniteOrdinal
        ):
            return Ordinals()(left_expression.value * right_expression.value)
        if self == 0 or right == 0:
            return Ordinals().zero()
        if right == 1:
            return self
        if self == 1:
            return right
        return Ordinal(Ordinals(), _OrdinalProduct(self, right))

    def ordinal_power(self, exponent: OrdinalInput) -> Ordinal:
        r"""Return ordinary ordinal exponentiation."""
        ordinal_exponent = Ordinals()(exponent)
        base_expression = self.expression()
        exponent_expression = ordinal_exponent.expression()
        if isinstance(base_expression, _FiniteOrdinal) and isinstance(
            exponent_expression, _FiniteOrdinal
        ):
            return Ordinals()(base_expression.value ** exponent_expression.value)
        if ordinal_exponent == 0:
            return Ordinals().one()
        if self == 0:
            return Ordinals().zero()
        if self == 1:
            return self
        return Ordinal(Ordinals(), _OrdinalPower(self, ordinal_exponent))

    def is_initial(self) -> bool:
        return isinstance(self.expression(), _InitialOrdinal)

    def initial_index(self) -> Ordinal:
        expression = self.expression()
        if not isinstance(expression, _InitialOrdinal):
            raise ValueError(f"{self} is not an initial ordinal")
        return expression.index

    def cardinality(self):
        r"""Return the cardinal of this ordinal."""
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
            return Cardinalities().product(
                *(factor.cardinality() for factor in factors)
            )
        return Cardinalities().power(
            expression.base.cardinality(),
            expression.exponent.cardinality(),
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


def ordinal(value: OrdinalInput) -> Ordinal:
    return Ordinals()(value)


def omega(index: OrdinalInput) -> Ordinal:
    r"""Return the initial ordinal ``omega_index``."""
    return Ordinals().initial(index)


omega0 = omega(0)
r"""The first infinite ordinal."""
