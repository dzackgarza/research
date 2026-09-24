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

from __future__ import annotations

import operator

from sage.functions import generalized as _sage_generalized
from sage.functions import hyperbolic as _sage_hyperbolic
from sage.functions import log as _sage_log
from sage.functions import transcendental as _sage_transcendental
from sage.functions import trig as _sage_trig
from sage.misc import functional as _sage_functional
from sage.misc.latex import latex
from sage.misc.unknown import Unknown
from sage.categories.rings import Rings as SageRings
from sage.rings.integer_ring import ZZ
from sage.rings.qqbar import AA, QQbar
from sage.rings.rational_field import QQ
from sage.rings.real_arb import RealBallField
from sage.rings.real_lazy import CLF, RLF
from sage.rings.real_mpfr import (
    RealField,
)
from sage.rings.real_mpfr import (
    create_RealNumber as _create_real_approximation,
)
from sage.rings.ring import Field
from sage.structure.element import FieldElement, parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.expression import Expression
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedFields,
    OwnedRings,
    _OwnedRingBootstrapParent,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.sets.cardinals import continuum
from dzack_research.preamble.categories.sets.set_categories import UncountableSets
from dzack_research.preamble.logic import Predicate, Propositions, ask
from dzack_research.preamble.refine import realize_owned_category


def RealApproximation(value):
    r"""Return the owned finite-precision real represented by ``value``."""
    backend = _create_real_approximation(value)

    parent = _own_ring(backend.parent())
    return _owned_engine_element(parent, backend)


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

    atom_parent = parent(atom)
    if atom_parent in SageRings():
        return not bool(atom_parent.is_exact())
    # Symbolic constants and foreign Python atoms are not approximation rings.
    return False


def _closed_exact_real_expression(value) -> Expression:
    r"""Return the exact closed real symbolic expression represented by ``value``."""
    if isinstance(value, ExactRealNumber):
        return value.expression()

    value_parent = parent(value)
    if value_parent in OwnedRings():
        value = _engine_element(value_parent, value)
        value_parent = parent(value)

    if isinstance(value, float):
        raise TypeError(
            f"{value!r} is a floating-point number, not an exact real number; "
            "give the exact expression it approximates"
        )

    if value_parent is QQbar:
        if value.imag() != 0:
            raise TypeError(f"{value} is algebraic but not real")
        value = AA(value.real())
    elif value_parent in (RLF, CLF):
        raise TypeError(
            f"{value} is a numerical approximation in {value_parent}, not an exact real number; "
            "give the exact expression it approximates"
        )
    elif value_parent is not SR and value_parent in SageRings():
        if not value_parent.is_exact():
            raise TypeError(
                f"{value} lies in the inexact ring {value_parent}, so it is an approximation, not an exact real number"
            )

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
    if expression not in AA:
        return None
    value = AA(expression)
    if value == 0:
        return 0
    return -1 if value < 0 else 1


def _sign_from_ball(expression: Expression, precision: int):
    r"""Certify the sign using an Arb enclosure, or return ``None``."""
    field = RealBallField(precision)
    # ``expression in RealBallField`` is False even for pi^2 and sqrt(2),
    # which the field encloses; a closed real expression is what it
    # converts (TRAPS.md).
    if expression.variables() or not expression.is_real():
        return None
    ball = field(expression)
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
    raise TypeError(
        f"{relation} is not one of the order relations <, <=, >, >=, ==, != on the real numbers"
    )


def _decide_relation(
    left: Expression,
    right: Expression,
    relation,
    *,
    precision: int | None,
):
    r"""Decide a real relation: exact algebra, then Arb, then symbolic normalization.

    ``AA`` decides every algebraic difference exactly and an Arb enclosure
    certifies any nonzero sign, both without Maxima; ``simplify_full`` is
    reached only for a difference neither decides, and its result is then
    decided the same way.
    """
    for difference_of in (operator.sub, _simplified_difference):
        difference = difference_of(left, right)
        if difference.is_zero() is True:
            return _relation_from_sign(0, relation)
        sign = _sign_from_algebraic(difference)
        if sign is None and precision is not None:
            sign = _sign_from_ball(difference, precision)
        if sign is not None:
            return _relation_from_sign(sign, relation)
    return None


class RealRelation(Predicate):
    r"""An exact relation between two real numbers awaiting evaluation."""

    __slots__ = ("_left", "_right", "_relation")

    def __init__(self, left: ExactRealNumber, right: ExactRealNumber, relation):
        self._left = left
        self._right = right
        self._relation = relation
        super().__init__()

    def left(self) -> ExactRealNumber:
        return self._left

    def right(self) -> ExactRealNumber:
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

    def __init__(self, parent: ExactRealField, expression: Expression) -> None:
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

    def __mul__(self, other):
        r"""Use the exact scalar engine, or the action on an owned module.

        The coefficient product cannot call the algebra tensor classifier
        whose own linear evaluation uses these coefficients.
        """
        ring = self.parent()
        source = parent(other)
        if source is ring:
            return ExactRealNumber._mul_(self, other)
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        if source in Modules(ring):
            return source.scalar_multiple(self, other)
        try:
            return ExactRealNumber._mul_(self, ring(other))
        except (TypeError, ValueError):
            return NotImplemented

    def __rmul__(self, other):
        return ExactRealNumber.__mul__(self, other)

    def _div_(self, other):
        nonzero = self.parent().relation(other, self.parent().zero(), operator.ne)

        decision = ask(nonzero) if nonzero in Propositions else nonzero
        if decision is False:
            raise ZeroDivisionError(f"cannot divide {self} by {other}: the denominator is zero")
        if decision is Unknown:
            raise ValueError(
                f"cannot divide {self} by {other}: it is undecided whether {other} is zero"
            )
        return self.parent()(self._expression / other._expression)

    def _neg_(self):
        return self.parent()(-self._expression)

    def __invert__(self):
        return self.parent().one() / self

    def inverse_of_unit(self):
        r"""``x^{-1}``: every nonzero real number is a unit."""
        assert not self.is_zero(), f"0 is not a unit of {self.parent()}"
        return ~self

    def __pow__(self, exponent, modulus=None):
        if modulus is not None:
            raise TypeError(
                f"cannot compute {self}^{exponent} mod {modulus}: modular exponentiation is not defined "
                "on the real numbers"
            )
        return self.parent()(self._expression ** _closed_exact_real_expression(exponent))

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

    def sinh(self):
        return self.parent()(self._expression.sinh())

    def cosh(self):
        return self.parent()(self._expression.cosh())

    def tanh(self):
        return self.parent()(self._expression.tanh())

    def sech(self):
        from sage.functions.hyperbolic import sech

        return self.parent()(sech(self._expression))

    def zeta(self):
        r"""The Riemann zeta function at this real number, which must exceed 1."""
        from sage.functions.transcendental import zeta

        assert self > 1, f"zeta(s) is computed here only for real s > 1, but s = {self} is not > 1"
        return self.parent()(zeta(self._expression))

    def sgn(self):
        r"""The sign of this real number, in the integers: \(1\), \(0\) or \(-1\)."""
        integers = _own_ring(ZZ)
        if self.is_zero() is True:
            return integers(0)
        positive = self.is_positive()
        assert positive is True or positive is False, (
            f"the sign of the real number {self} is undecided: it is not decided whether {self} > 0"
        )
        return integers(1 if positive else -1)

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
            raise TypeError(
                f"cannot compare the real number {self} by <: the other argument is not a real number"
            )
        return self.parent().relation(self, other, operator.lt)

    def __le__(self, other):
        other = self._coerce_for_relation(other)
        if other is None:
            raise TypeError(
                f"cannot compare the real number {self} by <=: the other argument is not a real number"
            )
        return self.parent().relation(self, other, operator.le)

    def __gt__(self, other):
        other = self._coerce_for_relation(other)
        if other is None:
            raise TypeError(
                f"cannot compare the real number {self} by >: the other argument is not a real number"
            )
        return self.parent().relation(self, other, operator.gt)

    def __ge__(self, other):
        other = self._coerce_for_relation(other)
        if other is None:
            raise TypeError(
                f"cannot compare the real number {self} by >=: the other argument is not a real number"
            )
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
        raise TypeError(
            f"the truth value of {self} is undecided: it is not decided whether {self} != 0; "
            "use ask(x != 0)"
        )


RealNumber = ExactRealNumber


class ExactRealField(UniqueRepresentation, Field):
    r"""The exact field of real numbers represented by closed exact expressions."""

    Element = ExactRealNumber
    _preamble_owned_ring_parent = True

    def __init__(self) -> None:
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.modules.pure.modules import (
            FinitelyGeneratedFreeModules,
        )

        regular_algebra = Algebras(self).Associative().Unital().Commutative()
        Field.__init__(
            self,
            base=self,
            category=Cat().meet(
                (
                    OwnedFields(),
                    UncountableSets(),
                    regular_algebra,
                    FinitelyGeneratedFreeModules(self),
                )
            ),
        )
        realize_owned_category(self)
        from dzack_research.preamble.categories.algebras.algebras import _algebra_from_native_ring

        _algebra_from_native_ring(self, lambda left, right: ExactRealNumber._mul_(left, right),
            ExactRealField.one(self), lambda scalar, element: ExactRealNumber._mul_(self(scalar), self(element)))


    def is_commutative(self) -> bool:
        r"""A field is commutative; answered by the class so ``Modules(RR)`` can place itself during construction."""
        return True

    def _repr_(self) -> str:
        return "Real Field"

    def _latex_(self) -> str:
        return r"\mathbb{R}"

    def _element_constructor_(self, value) -> ExactRealNumber:
        if isinstance(value, ExactRealNumber) and value.parent() is self:
            return value
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        source = parent(value)
        if source in Modules(self) and source.unformed_module() is self:
            return source._element_of_unformed_module(value)
        return self.element_class(self, _closed_exact_real_expression(value))

    def _from_engine_expression(self, value) -> ExactRealNumber:
        r"""Cross a private exact expression; implementation endpoint for the protected dispatcher."""
        return self.element_class(self, _closed_exact_real_expression(value))

    def __contains__(self, value) -> bool:
        r"""Return whether ``value`` canonically names an exact real number."""
        try:
            self(value)
        except (TypeError, ValueError):
            return False
        return True

    def _coerce_map_from_(self, source):

        computation_source = _engine_ring(source)
        if computation_source in (ZZ, QQ, AA):
            return True
        if computation_source not in SageRings():
            return None
        if AA.has_coerce_map_from(computation_source):
            return True
        return None

    def relation(self, left: ExactRealNumber, right: ExactRealNumber, relation):
        r"""Return a decided Boolean or an exact real relation predicate."""
        left = self(left)
        right = self(right)
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


_OwnedRingBootstrapParent.register(ExactRealField)


RR = ExactRealField()


pi = RR.pi()
e = RR.e()


# The elementary functions of a session.  On a real number each is the
# operation of the real field.  Any other argument -- a power series, a
# matrix, a symbolic expression -- goes to Sage's function of the same name,
# which applies the argument's own method where it has one.


def sqrt(x):
    r"""The square root of ``x``; of a real number, the nonnegative real root."""
    match x:
        case _ if x in RR:
            return RR(x).sqrt()
        case _:
            return _sage_functional.sqrt(x)


def exp(x):
    r"""The exponential of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).exp()
        case _:
            return _sage_log.exp(x)


def log(x, base=None):
    r"""The logarithm of ``x``, natural unless ``base`` is given."""
    match x:
        case _ if x in RR:
            return RR(x).log(base)
        case _:
            return _sage_functional.log(x) if base is None else _sage_functional.log(x, base)


def sin(x):
    r"""The sine of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).sin()
        case _:
            return _sage_trig.sin(x)


def cos(x):
    r"""The cosine of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).cos()
        case _:
            return _sage_trig.cos(x)


def tan(x):
    r"""The tangent of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).tan()
        case _:
            return _sage_trig.tan(x)


def sinh(x):
    r"""The hyperbolic sine of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).sinh()
        case _:
            return _sage_hyperbolic.sinh(x)


def cosh(x):
    r"""The hyperbolic cosine of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).cosh()
        case _:
            return _sage_hyperbolic.cosh(x)


def tanh(x):
    r"""The hyperbolic tangent of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).tanh()
        case _:
            return _sage_hyperbolic.tanh(x)


def sech(x):
    r"""The hyperbolic secant of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).sech()
        case _:
            return _sage_hyperbolic.sech(x)


def sgn(x):
    r"""The sign of ``x``: \(1\), \(0\) or \(-1\) for a real number."""
    match x:
        case _ if x in RR:
            return RR(x).sgn()
        case _:
            return _sage_generalized.sgn(x)


def zeta(x):
    r"""The Riemann zeta function at ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).zeta()
        case _:
            return _sage_transcendental.zeta(x)


def _owned_real_from_engine_expression(value) -> ExactRealNumber:
    r"""Raise a private exact symbolic expression into the owned real field.

    Protected exact-real contract (\`OWN-05\`--\`OWN-07\`).  Permitted
    callers are exact symbolic computation adapters for definite-lattice
    invariants and convolution evaluation.  They produce a closed exact
    expression and immediately raise it here; the symbolic engine value never
    becomes public mathematical storage.
    """
    return RR._from_engine_expression(value)


def _restore_exact_real(expression: Expression) -> ExactRealNumber:
    return RR(expression)


__all__ = [
    "cos",
    "cosh",
    "e",
    "exp",
    "log",
    "pi",
    "sech",
    "sgn",
    "sin",
    "sinh",
    "sqrt",
    "tan",
    "tanh",
    "zeta",
    "ExactRealField",
    "ExactRealNumber",
    "RR",
    "RealApproximation",
    "RealNumber",
    "RealRelation",
]
