r"""The exact real field.

Sage's global ``RR`` is MPFR: an approximation field.  It cannot be the
mathematical real field because its arithmetic is rounded; for example the
MPFR image of ``sqrt(2)`` need not square to exactly ``2``.

This module represents constructible exact real numbers by closed exact Sage
symbolic expressions.  Algebraic subproblems are delegated to ``AA`` and
inequalities/non-equality can be certified by Arb balls without ever storing
an approximation as the value.  Approximation is explicit through ``.n()``.

Equality and order are necessarily partial algorithms on a language rich
enough to contain transcendental expressions.  A relation that is not decided
immediately is returned as a predicate and can be evaluated by ``ask(...)``.
"""

import operator

from sage.categories.fields import Fields
from sage.misc.latex import latex
from sage.misc.unknown import Unknown
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ
from sage.rings.qqbar import AA, QQbar
from sage.rings.rational_field import QQ
from sage.rings.real_arb import RealBallField
from sage.rings.real_lazy import CLF, RLF
from sage.rings.real_mpfr import (
    RealField,
    RealNumber as _RealApproximationNumber,
    create_RealNumber as RealApproximation,
)
from sage.rings.ring import Field
from sage.structure.element import FieldElement, parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.expression import Expression
from sage.symbolic.ring import SR

from dzack_research.preamble.logic import Predicate


_RELATION_SYMBOL = {
    operator.eq: "==",
    operator.ne: "!=",
    operator.lt: "<",
    operator.le: "<=",
    operator.gt: ">",
    operator.ge: ">=",
}


def _contains_approximation(expression: Expression) -> bool:
    r"""Return whether a symbolic expression contains an inexact numeric atom."""
    operands = expression.operands()
    if operands:
        return any(_contains_approximation(SR(operand)) for operand in operands)

    try:
        atom = expression.pyobject()
    except TypeError:
        return False

    if isinstance(atom, (float, complex)):
        return True

    try:
        atom_parent = parent(atom)
        is_exact = atom_parent.is_exact()
    except (AttributeError, TypeError):
        # Symbolic constants such as pi are not approximate Sage ring elements.
        return False
    return not bool(is_exact)


def _closed_exact_real_expression(value) -> Expression:
    r"""Return the exact closed real symbolic expression represented by ``value``."""
    if isinstance(value, ExactRealNumber):
        return value.expression()

    if isinstance(value, float):
        raise TypeError("a floating-point approximation is not an exact real")

    value_parent = None
    try:
        value_parent = parent(value)
    except TypeError:
        pass

    if value_parent is QQbar:
        if value.imag() != 0:
            raise TypeError(f"{value} is algebraic but not real")
        value = AA(value.real())
    elif value_parent in (RLF, CLF):
        raise TypeError(
            "a lazy numerical real/complex value is not an exact real expression; "
            "coerce its original exact expression instead"
        )
    elif value_parent is not None and value_parent is not SR:
        try:
            if not value_parent.is_exact():
                raise TypeError(f"{value} is an approximation, not an exact real")
        except AttributeError:
            pass

    expression = SR(value)
    if expression.variables():
        raise TypeError(
            f"{expression} contains symbolic variables and does not name one real number"
        )
    if _contains_approximation(expression):
        raise TypeError(f"{expression} contains an inexact numeric approximation")
    if expression.is_real() is not True:
        raise TypeError(f"{expression} is not known to be a real number")
    return expression


def _simplified_difference(left: Expression, right: Expression) -> Expression:
    return (left - right).simplify_full()


def _sign_from_algebraic(expression: Expression):
    r"""Return ``-1,0,1`` when ``expression`` is algebraic, else ``None``."""
    try:
        value = AA(expression)
    except (TypeError, ValueError, NotImplementedError):
        return None
    if value == 0:
        return 0
    return -1 if value < 0 else 1


def _sign_from_ball(expression: Expression, precision: int):
    r"""Certify the sign using an Arb enclosure, or return ``None``."""
    try:
        ball = RealBallField(precision)(expression)
    except (TypeError, ValueError, NotImplementedError):
        return None
    if ball == 0:
        return 0
    if ball.contains_zero():
        return None
    return 1 if ball > 0 else -1


def _relation_from_sign(sign: int, relation) -> bool:
    if relation is operator.eq:
        return sign == 0
    if relation is operator.ne:
        return sign != 0
    if relation is operator.lt:
        return sign < 0
    if relation is operator.le:
        return sign <= 0
    if relation is operator.gt:
        return sign > 0
    if relation is operator.ge:
        return sign >= 0
    raise TypeError(f"unsupported real relation {relation}")


def _decide_relation(
    left: Expression,
    right: Expression,
    relation,
    *,
    precision: int | None,
):
    r"""Decide a real relation by exact normalization/algebra, then Arb."""
    difference = _simplified_difference(left, right)
    if difference.is_zero() is True:
        return _relation_from_sign(0, relation)

    sign = _sign_from_algebraic(difference)
    if sign is not None:
        return _relation_from_sign(sign, relation)

    if precision is not None:
        sign = _sign_from_ball(difference, precision)
        if sign is not None:
            return _relation_from_sign(sign, relation)
    return None


class RealRelation(Predicate):
    r"""An exact relation between two real numbers awaiting evaluation."""

    __slots__ = ("_left", "_right", "_relation")

    def __init__(self, left: "ExactRealNumber", right: "ExactRealNumber", relation):
        self._left = left
        self._right = right
        self._relation = relation

    def left(self) -> "ExactRealNumber":
        return self._left

    def right(self) -> "ExactRealNumber":
        return self._right

    def operator(self):
        return self._relation

    def _ask_(self, *, max_prec: int = 4096):
        precision = 128
        while precision <= max_prec:
            answer = _decide_relation(
                self._left.expression(),
                self._right.expression(),
                self._relation,
                precision=precision,
            )
            if answer is not None:
                return answer
            precision *= 2
        return Unknown

    def _repr_(self) -> str:
        symbol = _RELATION_SYMBOL[self._relation]
        return f"{self._left} {symbol} {self._right}"

    def _latex_(self) -> str:
        symbol = {
            operator.eq: "=",
            operator.ne: r"\ne",
            operator.lt: "<",
            operator.le: r"\le",
            operator.gt: ">",
            operator.ge: r"\ge",
        }[self._relation]
        return rf"{latex(self._left)} {symbol} {latex(self._right)}"


class ExactRealNumber(FieldElement):
    r"""An exact, explicitly real number."""

    __hash__ = None

    def __init__(self, parent: "ExactRealField", expression: Expression) -> None:
        self._expression = expression
        FieldElement.__init__(self, parent)

    def expression(self) -> Expression:
        r"""Return the exact symbolic expression representing this real."""
        return self._expression

    def is_real(self) -> bool:
        return True

    def _repr_(self) -> str:
        return repr(self._expression)

    def __reduce__(self):
        return (_restore_exact_real, (self._expression,))

    def _latex_(self) -> str:
        return str(latex(self._expression))

    def _symbolic_(self, symbolic_ring):
        return symbolic_ring(self._expression)

    def _sympy_(self):
        return self._expression._sympy_()

    def _integer_(self, integer_ring):
        return integer_ring(self._expression)

    def _rational_(self):
        return QQ(self._expression)

    def _algebraic_(self, algebraic_field):
        return algebraic_field(self._expression)

    def _mpfr_(self, field):
        return field(self._expression)

    def _real_double_(self, field):
        return field(self._expression)

    def n(self, prec: int = 53, digits: int | None = None, **kwds):
        r"""Return an explicit floating-point approximation of ``self``."""
        if digits is not None:
            return self._expression.n(digits=digits, **kwds)
        return RealField(prec)(self._expression)

    numerical_approx = n

    def __float__(self) -> float:
        return float(self.n())

    def _add_(self, other):
        return self.parent()(self._expression + other._expression)

    def _sub_(self, other):
        return self.parent()(self._expression - other._expression)

    def _mul_(self, other):
        return self.parent()(self._expression * other._expression)

    def _div_(self, other):
        nonzero = self.parent().relation(other, self.parent().zero(), operator.ne)
        from dzack_research.preamble.logic import ask

        decision = ask(nonzero) if isinstance(nonzero, Predicate) else nonzero
        if decision is False:
            raise ZeroDivisionError("division by zero")
        if decision is Unknown:
            raise ValueError("the denominator's zero predicate is undecided")
        return self.parent()(self._expression / other._expression)

    def _neg_(self):
        return self.parent()(-self._expression)

    def __invert__(self):
        return self.parent().one() / self

    def __pow__(self, exponent, modulus=None):
        if modulus is not None:
            raise TypeError("modular exponentiation is not defined in the real field")
        if isinstance(exponent, ExactRealNumber):
            exponent = exponent.expression()
        return self.parent()(self._expression**exponent)

    def __rpow__(self, base):
        base_expression = _closed_exact_real_expression(base)
        return self.parent()(base_expression**self._expression)

    def sqrt(self):
        return self.parent()(self._expression.sqrt())

    def exp(self):
        return self.parent()(self._expression.exp())

    def log(self, base=None):
        if base is None:
            return self.parent()(self._expression.log())
        base = self.parent()(base)
        return self.parent()(self._expression.log() / base.expression().log())

    def sin(self):
        return self.parent()(self._expression.sin())

    def cos(self):
        return self.parent()(self._expression.cos())

    def tan(self):
        return self.parent()(self._expression.tan())

    def __abs__(self):
        return self.parent()(abs(self._expression))

    def _coerce_for_relation(self, other):
        try:
            return self.parent()(other)
        except (TypeError, ValueError):
            return None

    def __eq__(self, other):
        other = self._coerce_for_relation(other)
        if other is None:
            return False
        return self.parent().relation(self, other, operator.eq)

    def __ne__(self, other):
        other = self._coerce_for_relation(other)
        if other is None:
            return True
        return self.parent().relation(self, other, operator.ne)

    def __lt__(self, other):
        other = self._coerce_for_relation(other)
        if other is None:
            raise TypeError(f"{other!r} is not a real number")
        return self.parent().relation(self, other, operator.lt)

    def __le__(self, other):
        other = self._coerce_for_relation(other)
        if other is None:
            raise TypeError(f"{other!r} is not a real number")
        return self.parent().relation(self, other, operator.le)

    def __gt__(self, other):
        other = self._coerce_for_relation(other)
        if other is None:
            raise TypeError(f"{other!r} is not a real number")
        return self.parent().relation(self, other, operator.gt)

    def __ge__(self, other):
        other = self._coerce_for_relation(other)
        if other is None:
            raise TypeError(f"{other!r} is not a real number")
        return self.parent().relation(self, other, operator.ge)

    def is_zero(self):
        return self == self.parent().zero()

    def is_one(self):
        return self == self.parent().one()

    def is_positive(self):
        return self > self.parent().zero()

    def is_negative(self):
        return self < self.parent().zero()

    def __bool__(self):
        relation = self != self.parent().zero()
        if relation is True or relation is False:
            return relation
        raise TypeError("nonzeroness is undecided; use ask(x != 0)")


RealNumber = ExactRealNumber


class ExactRealField(UniqueRepresentation, Field):
    r"""The exact field of real numbers represented by closed exact expressions."""

    Element = ExactRealNumber

    def __init__(self) -> None:
        from sage.categories.category import Category
        from dzack_research.preamble.categories.sets import UncountableSets

        Field.__init__(
            self,
            base=self,
            category=Category.join((Fields().Infinite(), UncountableSets())),
        )

    def _repr_(self) -> str:
        return "Real Field"

    def _latex_(self) -> str:
        return r"\mathbb{R}"

    def _element_constructor_(self, value) -> ExactRealNumber:
        if isinstance(value, ExactRealNumber) and value.parent() is self:
            return value
        return self.element_class(self, _closed_exact_real_expression(value))

    def __contains__(self, value) -> bool:
        r"""Return whether ``value`` canonically names an exact real number."""
        try:
            self(value)
        except (TypeError, ValueError):
            return False
        return True

    def _coerce_map_from_(self, source):
        from dzack_research.preamble.categories.rings import engine_ring

        computation_source = engine_ring(source)
        if computation_source in (ZZ, QQ, AA):
            return True
        try:
            if AA.has_coerce_map_from(computation_source):
                return True
        except TypeError:
            pass
        return None

    def relation(self, left: ExactRealNumber, right: ExactRealNumber, relation):
        r"""Return a decided Boolean or an exact real relation predicate."""
        answer = _decide_relation(
            left.expression(),
            right.expression(),
            relation,
            precision=128,
        )
        if answer is not None:
            return answer
        return RealRelation(left, right, relation)

    def zero(self) -> ExactRealNumber:
        return self(ZZ.zero())

    def one(self) -> ExactRealNumber:
        return self(ZZ.one())

    def characteristic(self):
        return ZZ.zero()

    def is_exact(self) -> bool:
        return True

    def is_finite(self) -> bool:
        return False

    def cardinality(self):
        from dzack_research.preamble.categories.sets import continuum

        return continuum

    def fraction_field(self):
        return self

    def _an_element_(self):
        from sage.symbolic.constants import pi

        return self(pi)

    def pi(self) -> ExactRealNumber:
        from sage.symbolic.constants import pi

        return self(pi)

    def e(self) -> ExactRealNumber:
        from sage.symbolic.constants import e

        return self(e)


RR = ExactRealField()


def _restore_exact_real(expression: Expression) -> ExactRealNumber:
    return RR(expression)


__all__ = [
    "ExactRealField",
    "ExactRealNumber",
    "RR",
    "RealApproximation",
    "RealNumber",
    "RealRelation",
]
