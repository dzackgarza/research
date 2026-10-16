r"""The exact complex field.

Sage's global ``CC`` is MPFR: a 53-bit approximation field.  Its arithmetic
is rounded, so it is not the field \(\mathbb C\).  This module presents
\(\mathbb C = \mathbb R[i]/(i^2+1)\) over the exact real field ``RR`` of
:mod:`dzack_research.preamble.rings.real`, with the same representation: a
complex number is a closed exact Sage symbolic expression.  Algebraic
subproblems are decided in ``QQbar``; Arb enclosures of the real and
imaginary parts certify that a difference is nonzero without storing an
approximation as the value.  Approximation is explicit: ``z.n(prec)`` is the
image of ``z`` in the owned ``ComplexField(prec)``.

Equality is a partial algorithm on a language that contains transcendental
expressions.  An equality that is not decided at once is returned as a
predicate, which ``ask(...)`` evaluates.  The field is not ordered, so it has
no order relations.

The session's elementary functions live here because they choose between the
two fields: on a real argument whose value is real they are the operations of
``RR``, and otherwise the principal-branch operations of ``CC``.
"""

from __future__ import annotations

import operator

from sage.arith.numerical_approx import digits_to_bits
from sage.functions import generalized as _sage_generalized
from sage.functions import hyperbolic as _sage_hyperbolic
from sage.functions import log as _sage_log
from sage.functions import transcendental as _sage_transcendental
from sage.functions import trig as _sage_trig
from sage.misc import functional as _sage_functional
from sage.misc.cachefunc import cached_method
from sage.misc.latex import latex
from sage.misc.unknown import Unknown
from sage.rings.complex_mpfr import ComplexField as _SageComplexField
from sage.rings.integer_ring import ZZ
from sage.rings.qqbar import QQbar
from sage.rings.ring import Field
from sage.structure.element import FieldElement, parent
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.expression import Expression
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedFields,
    OwnedRings,
    _OwnedRingBootstrapParent,
    _engine_element,
    _engine_ring,
    _owned_complex_field_of_precision,
    _owned_engine_element,
    _owned_integers,
)
from dzack_research.preamble.categories.sets.cardinals import continuum
from dzack_research.preamble.categories.sets.set_categories import UncountableSets
from dzack_research.preamble.logic import Predicate, Propositions, ask
from dzack_research.preamble.refine import realize_owned_category
from dzack_research.preamble.rings.real import (
    RR,
    ExactRealNumber,
    _contains_approximation,
    _sign_from_ball,
    _simplified_difference,
)


def _exact_complex_expression(value) -> Expression | None:
    r"""The closed exact symbolic expression of the complex number ``value``, or ``None``.

    The values that name an exact complex number are the elements of this
    field and of ``RR``, the closed symbolic expressions with no inexact atom,
    and the elements of the exact rings that coerce into ``QQbar`` (``ZZ``,
    ``QQ``, ``AA``, ``QQbar``, embedded number fields).  An element of an
    approximation ring -- MPFR, double precision, a lazy field, a Python
    float -- names no exact number and gives ``None``.
    """
    source = parent(value)
    if source in OwnedRings():
        value = _engine_element(source, value)
        source = parent(value)
    match source:
        case _ if source is SR or source is RR:
            pass
        case _ if QQbar.has_coerce_map_from(source):
            pass
        case _ if source is CC:
            pass
        case _:
            return None
    expression = SR(value)
    if expression.variables() or expression.is_infinity():
        return None
    if _contains_approximation(expression):
        return None
    return expression


def _closed_exact_complex_expression(value) -> Expression:
    r"""The closed exact symbolic expression of ``value``; ``TypeError`` if it names no complex number."""
    expression = _exact_complex_expression(value)
    if expression is None:
        raise TypeError(
            f"{value!r} does not name an exact complex number: give a closed exact expression, "
            "an element of RR, or an element of an exact ring that embeds in QQbar, "
            "not a numerical approximation, a symbolic variable or an infinity"
        )
    return expression


def _ball_excludes_zero(expression: Expression, precision: int) -> bool:
    r"""Whether Arb enclosures of the real or imaginary part of ``expression`` exclude zero."""
    signs = (
        _sign_from_ball(expression.real_part(), precision),
        _sign_from_ball(expression.imag_part(), precision),
    )
    return any(sign is not None and sign != 0 for sign in signs)


def _decide_equality(left: Expression, right: Expression, *, precision: int | None):
    r"""Decide ``left == right``: symbolic zero, then ``QQbar``, then Arb; ``None`` if undecided.

    ``QQbar`` decides every algebraic difference exactly.  A nonzero
    difference is certified by an Arb ball for its real or imaginary part.
    ``simplify_full`` is reached only for a difference that neither decides.
    """
    for difference_of in (operator.sub, _simplified_difference):
        difference = difference_of(left, right)
        if difference.is_zero() is True:
            return True
        if difference in QQbar:
            return QQbar(difference).is_zero()
        if precision is not None and _ball_excludes_zero(difference, precision):
            return False
    return None


def _relation_answer(equal: bool, relation) -> bool:
    match relation:
        case operator.eq:
            return equal
        case operator.ne:
            return not equal
    raise TypeError(
        f"{relation} is not == or !=: the complex field is not ordered, so equality and "
        "inequality are its only relations"
    )


class ComplexRelation(Predicate):
    r"""An exact equality or inequality of two complex numbers awaiting evaluation."""

    __slots__ = ("_left", "_right", "_relation")

    def __init__(self, left: ExactComplexNumber, right: ExactComplexNumber, relation):
        self._left = left
        self._right = right
        self._relation = relation
        super().__init__()

    def left(self) -> ExactComplexNumber:
        return self._left

    def right(self) -> ExactComplexNumber:
        return self._right

    def operator(self):
        return self._relation

    def _ask_(self, *, max_prec: int = 4096):
        precision = 128
        while precision <= max_prec:
            equal = _decide_equality(
                self._left.expression(),
                self._right.expression(),
                precision=precision,
            )
            if equal is not None:
                return _relation_answer(equal, self._relation)
            precision *= 2
        return Unknown

    def _repr_(self) -> str:
        symbol = {operator.eq: "==", operator.ne: "!="}[self._relation]
        return f"{self._left} {symbol} {self._right}"

    def _latex_(self) -> str:
        symbol = {operator.eq: "=", operator.ne: r"\ne"}[self._relation]
        return rf"{latex(self._left)} {symbol} {latex(self._right)}"


class ExactComplexNumber(FieldElement):
    r"""An exact complex number, given by a closed exact symbolic expression."""

    def __init__(self, parent: ExactComplexField, expression: Expression) -> None:
        self._expression = expression
        FieldElement.__init__(self, parent)

    def expression(self) -> Expression:
        r"""Return the exact symbolic expression representing this complex number."""
        return self._expression

    def __hash__(self) -> int:
        r"""The hash of this number as an element of ``QQbar``.

        Equality is decided on ``QQbar``, so an algebraic number has a hash
        consistent with ``==``.  Equality of other exact complex numbers is
        not decided in general, so they have none.
        """
        if self._expression not in QQbar:
            raise TypeError(
                f"the complex number {self} is not known to be algebraic, so equality with it is "
                "not decided and it has no hash"
            )
        return hash(QQbar(self._expression))

    def _repr_(self) -> str:
        return repr(self._expression)

    def __reduce__(self):
        return (_restore_exact_complex, (self._expression,))

    def _latex_(self) -> str:
        return str(latex(self._expression))

    def _symbolic_(self, symbolic_ring):
        return symbolic_ring(self._expression)

    def _sympy_(self):
        return self._expression._sympy_()

    def _algebraic_(self, algebraic_field):
        return algebraic_field(self._expression)

    def _complex_mpfr_field_(self, field):
        return field(self._expression)

    def _complex_double_(self, field):
        return field(self._expression)

    def n(self, prec: int = 53, digits: int | None = None):
        r"""The image of this number in the owned approximation field ``ComplexField(prec)``."""
        precision = int(prec) if digits is None else int(digits_to_bits(digits))
        approximation = _SageComplexField(precision)(self._expression)
        return _owned_engine_element(_owned_complex_field_of_precision(precision), approximation)

    numerical_approx = n

    def real_part(self) -> ExactRealNumber:
        r"""The real part \(\operatorname{Re} z\), an element of ``RR``."""
        return RR(self._expression.real_part())

    def imaginary_part(self) -> ExactRealNumber:
        r"""The imaginary part \(\operatorname{Im} z\), an element of ``RR``."""
        return RR(self._expression.imag_part())

    def conjugate(self) -> ExactComplexNumber:
        r"""The complex conjugate \(\bar z\); the map \(z\mapsto\bar z\) is ``CC.complex_conjugation()``."""
        return self.parent()(self._expression.conjugate())

    def __abs__(self) -> ExactRealNumber:
        r"""The absolute value \(|z| = \sqrt{z\bar z}\), an element of ``RR``."""
        return RR(abs(self._expression))

    def _add_(self, other):
        return self.parent()(self._expression + other._expression)

    def _sub_(self, other):
        return self.parent()(self._expression - other._expression)

    def _mul_(self, other):
        return self.parent()(self._expression * other._expression)

    def __mul__(self, other):
        r"""Use the exact scalar product, or the action on an owned module.

        The coefficient product cannot call the algebra tensor classifier
        whose own linear evaluation uses these coefficients.
        """
        ring = self.parent()
        source = parent(other)
        if source is ring:
            return ExactComplexNumber._mul_(self, other)
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        if source in Modules(ring):
            return source.scalar_multiple(self, other)
        if ring.has_coerce_map_from(source):
            return ExactComplexNumber._mul_(self, ring(other))
        return NotImplemented

    def __rmul__(self, other):
        return ExactComplexNumber.__mul__(self, other)

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

    def _unit_inverse_decision(self):
        r"""``z^{-1}``: every nonzero complex number is a unit."""
        return ~self

    def __pow__(self, exponent, modulus=None):
        r"""The principal power \(z^w = \exp(w \log z)\); an integer power is the iterated product."""
        if modulus is not None:
            raise TypeError(
                f"cannot compute {self}^{exponent} mod {modulus}: modular exponentiation is not defined "
                "on the complex numbers"
            )
        return self.parent()(self._expression ** _closed_exact_complex_expression(exponent))

    def __rpow__(self, base):
        return self.parent()(_closed_exact_complex_expression(base) ** self._expression)

    def sqrt(self):
        r"""The principal square root, \(\exp(\tfrac12 \log z)\) with \(-\pi < \arg z \le \pi\)."""
        return self.parent()(self._expression.sqrt())

    def exp(self):
        return self.parent()(self._expression.exp())

    def log(self, base=None):
        r"""The principal logarithm, with imaginary part in \((-\pi, \pi]\); defined for \(z \ne 0\)."""
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
        return self.parent()(_sage_hyperbolic.sech(self._expression))

    def __eq__(self, other):
        expression = _exact_complex_expression(other)
        if expression is None:
            return False
        return self.parent().relation(self, self.parent()(expression), operator.eq)

    def __ne__(self, other):
        expression = _exact_complex_expression(other)
        if expression is None:
            return True
        return self.parent().relation(self, self.parent()(expression), operator.ne)

    def _unordered(self, symbol: str):
        raise TypeError(
            f"cannot compare the complex number {self} by {symbol}: the complex field is not ordered"
        )

    def __lt__(self, other):
        self._unordered("<")

    def __le__(self, other):
        self._unordered("<=")

    def __gt__(self, other):
        self._unordered(">")

    def __ge__(self, other):
        self._unordered(">=")

    def is_zero(self):
        return self == self.parent().zero()

    def is_one(self):
        return self == self.parent().one()

    def _squareness_decision(self):
        r"""Every complex number is a square: \(z = (\sqrt z)^2\) for the principal root."""
        return True

    def __bool__(self):
        relation = self != self.parent().zero()
        if relation is True or relation is False:
            return relation
        raise TypeError(
            f"the truth value of {self} is undecided: it is not decided whether {self} != 0; "
            "use ask(z != 0)"
        )


ComplexNumber = ExactComplexNumber


class ExactComplexField(UniqueRepresentation, Field):
    r"""The field \(\mathbb C = \mathbb R[i]/(i^2+1)\) of exact complex numbers.

    An object of the owned fields, of characteristic zero and cardinality
    \(2^{\aleph_0}\), and the regular commutative algebra over itself.  It
    is an ``RR``-algebra along :meth:`real_field_inclusion`: that algebra is
    ``CC.restrict_scalars(CC.real_field_inclusion())``, the image under
    restriction of scalars, a functor (``CAT-16``).
    """

    Element = ExactComplexNumber
    _preamble_owned_ring_parent = True

    def __init__(self) -> None:
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.modules.pure.modules import (
            FinitelyGeneratedFreeModules,
        )

        regular_algebra = Algebras(self).Associative().Unital().Commutative()
        Field.__init__(
            self,
            self,
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

        _algebra_from_native_ring(
            self,
            lambda left, right: ExactComplexNumber._mul_(left, right),
            ExactComplexField.one(self),
            lambda scalar, element: ExactComplexNumber._mul_(self(scalar), self(element)),
        )

    def is_commutative(self) -> bool:
        r"""A field is commutative; answered by the class so ``Modules(CC)`` can place itself during construction."""
        return True

    def _refine_category_(self, category) -> None:
        r"""Keep the category fixed at construction.

        This field is its own computation model, so Sage algorithms that
        receive it ask Sage's ``_refine_category_`` to add Sage's ``Fields()``
        or ``Sets().Infinite()`` as a cached answer.  Placement comes only from
        construction: the field is already in the owned fields and the owned
        uncountable sets, and an engine's answer never changes the category
        or the operations it selects.
        """

    def _repr_(self) -> str:
        return "Complex Field"

    def _latex_(self) -> str:
        return r"\mathbb{C}"

    def _element_constructor_(self, value) -> ExactComplexNumber:
        if parent(value) is self:
            return value
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        source = parent(value)
        if source in Modules(self) and source.unformed_module() is self:
            return source._element_of_unformed_module(value)
        return self.element_class(self, _closed_exact_complex_expression(value))

    def _from_engine_expression(self, value) -> ExactComplexNumber:
        r"""Cross a private exact expression; implementation endpoint for the protected dispatcher."""
        return self.element_class(self, _closed_exact_complex_expression(value))

    def __contains__(self, value) -> bool:
        r"""Return whether ``value`` names an exact complex number."""
        return parent(value) is self or _exact_complex_expression(value) is not None

    def _coerce_map_from_(self, source):
        r"""``RR`` and the exact rings that embed in ``QQbar`` coerce into ``CC``."""
        match source:
            case _ if source is RR:
                return True
            case _ if source in OwnedRings():
                return QQbar.has_coerce_map_from(_engine_ring(source)) or None
            case _:
                return QQbar.has_coerce_map_from(source) or None

    def relation(self, left: ExactComplexNumber, right: ExactComplexNumber, relation):
        r"""Return a decided Boolean or an exact complex relation predicate."""
        left = self(left)
        right = self(right)
        equal = _decide_equality(left.expression(), right.expression(), precision=128)
        if equal is not None:
            return _relation_answer(equal, relation)
        return ComplexRelation(left, right, relation)

    def zero(self) -> ExactComplexNumber:
        return self(ZZ.zero())

    def one(self) -> ExactComplexNumber:
        return self(ZZ.one())

    def imaginary_unit(self) -> ExactComplexNumber:
        r"""The class \(i\) of the indeterminate in \(\mathbb R[i]/(i^2+1)\)."""
        return self(SR.I())

    def _characteristic_decision(self):
        return _owned_integers().zero()

    def is_exact(self) -> bool:
        return True

    def is_finite(self) -> bool:
        return False

    def _cardinality_decision(self):
        r"""Supply the cardinality of the complex numbers at the set owner."""
        return continuum

    def fraction_field(self):
        return self

    def _an_element_(self):
        return self.imaginary_unit()

    @cached_method
    def complex_conjugation(self):
        r"""The field automorphism \(z \mapsto \bar z\) of \(\mathbb C\), an element of ``Mor(CC, CC)``.

        It fixes ``RR`` and sends \(i\) to \(-i\); it is an involution.
        """
        return OwnedRings().Mor(self, self).elementwise(lambda element: self(element).conjugate())

    @cached_method
    def real_field_inclusion(self):
        r"""The ring morphism \(\mathbb R \hookrightarrow \mathbb C\), an element of ``Mor(RR, CC)``.

        It is the structure morphism of \(\mathbb C\) as an ``RR``-algebra.
        """
        return OwnedRings().Mor(RR, self).elementwise(lambda element: self(element))


_OwnedRingBootstrapParent.register(ExactComplexField)


CC = ExactComplexField()


I = CC.imaginary_unit()


# The elementary functions of a session.  On a real number whose value is
# real each is the operation of the real field; on any other complex number
# it is the principal-branch operation of the complex field.  Any other
# argument -- a power series, a matrix, a symbolic expression -- goes to
# Sage's function of the same name, which applies the argument's own method
# where it has one.


def _decided(proposition):
    return ask(proposition) if proposition in Propositions else proposition


def sqrt(x):
    r"""The square root of ``x``: of a real \(x \ge 0\) the nonnegative real root, else the principal root in ``CC``."""
    match x:
        case _ if x in RR:
            real = RR(x)
            match _decided(real >= RR.zero()):
                case True:
                    return real.sqrt()
                case False:
                    return CC(real).sqrt()
                case _:
                    assert False, (
                        f"the square root of the real number {real}: it is undecided whether {real} >= 0, "
                        "so it is not decided whether the root lies in RR"
                    )
        case _ if x in CC:
            return CC(x).sqrt()
        case _:
            return _sage_functional.sqrt(x)


def exp(x):
    r"""The exponential of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).exp()
        case _ if x in CC:
            return CC(x).exp()
        case _:
            return _sage_log.exp(x)


def log(x, base=None):
    r"""The logarithm of ``x``, natural unless ``base`` is given: of a real \(x > 0\) in ``RR``, else principal in ``CC``."""
    match x:
        case _ if x in RR:
            real = RR(x)
            match _decided(real > RR.zero()):
                case True:
                    return real.log(base)
                case False:
                    return CC(real).log(base)
                case _:
                    assert False, (
                        f"the logarithm of the real number {real}: it is undecided whether {real} > 0, "
                        "so it is not decided whether the logarithm lies in RR"
                    )
        case _ if x in CC:
            return CC(x).log(base)
        case _:
            return _sage_functional.log(x) if base is None else _sage_functional.log(x, base)


def sin(x):
    r"""The sine of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).sin()
        case _ if x in CC:
            return CC(x).sin()
        case _:
            return _sage_trig.sin(x)


def cos(x):
    r"""The cosine of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).cos()
        case _ if x in CC:
            return CC(x).cos()
        case _:
            return _sage_trig.cos(x)


def tan(x):
    r"""The tangent of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).tan()
        case _ if x in CC:
            return CC(x).tan()
        case _:
            return _sage_trig.tan(x)


def sinh(x):
    r"""The hyperbolic sine of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).sinh()
        case _ if x in CC:
            return CC(x).sinh()
        case _:
            return _sage_hyperbolic.sinh(x)


def cosh(x):
    r"""The hyperbolic cosine of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).cosh()
        case _ if x in CC:
            return CC(x).cosh()
        case _:
            return _sage_hyperbolic.cosh(x)


def tanh(x):
    r"""The hyperbolic tangent of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).tanh()
        case _ if x in CC:
            return CC(x).tanh()
        case _:
            return _sage_hyperbolic.tanh(x)


def sech(x):
    r"""The hyperbolic secant of ``x``."""
    match x:
        case _ if x in RR:
            return RR(x).sech()
        case _ if x in CC:
            return CC(x).sech()
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


def _restore_exact_complex(expression: Expression) -> ExactComplexNumber:
    return CC(expression)


__all__ = [
    "CC",
    "I",
    "ComplexNumber",
    "ComplexRelation",
    "ExactComplexField",
    "ExactComplexNumber",
    "cos",
    "cosh",
    "exp",
    "log",
    "sech",
    "sgn",
    "sin",
    "sinh",
    "sqrt",
    "tan",
    "tanh",
    "zeta",
]
