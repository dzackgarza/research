r"""Function spaces: \(C^k(X,Y)\), and \(L^p\), \(\ell^p\) as \(\mathbb R\)-modules of maps.

A function space is a set of maps \(X\to Y\) singled out by a condition on
the maps.  Function spaces form no category of their own: each is an object
of the category its structure places it in, realized by an engine class of
this module and built by one construction route.

- ``C``: the differentiability class \(C^k(X,Y)\) of maps \(X\to Y\) of
  class \(C^k\), a subset of \(\operatorname{Hom}_{\mathbf{Set}}(X,Y)\).
  ``C(k, X, Y)`` and ``(C^k)(X, Y)`` are the same space; ``C(k, X)`` is
  \(C^k(X,X)\).  The regularity \(k\) is the object's datum; \(\infty\) is a
  value of \(k\).  It is a set; when \(Y\) is an \(\mathbb R\)-vector space,
  pointwise operations make it an object of ``VectorSpaces(RR)``; when
  \(Y=\mathbb R\), pointwise product makes it a commutative unital
  \(\mathbb R\)-algebra.
- ``Lp``: \(\mathcal L^p(\mathbb R)\), the \(\mathbb R\)-vector space of
  \(p\)-integrable maps on \(\mathbb R\), whose quotient by the null maps is
  \(L^p(\mathbb R)\).
- ``ell``: \(\ell^p(\mathbb R)\), the \(\mathbb R\)-vector space of
  \(p\)-summable real sequences on \(\mathbb N\).

A map is constructed from the inductive class of formulas — polynomials,
named transcendentals, Laurent and power series, indefinite integrals, and
the pointwise operations and composition — when \(X=Y=\mathbb R\), or by
placing a callable.  Placement is the membership claim.

An admitted polynomial or formal power-series expression supplies a formula on \(\mathbb R\) in \(C^k\)
and \(L^p\), and is its coefficient sequence in \(\ell^p\).  A map in
\(C^\infty(\mathbb R)\) has a Maclaurin series and a Taylor series at any
point, as formal power series; a map in finite \(C^k\) has the jet of order
\(k\).  Hölder pairs \(L^p\) with \(L^{p'}\) and \(\ell^p\) with
\(\ell^{p'}\) when \(1/p+1/p'=1\); that pairing is the product of the two
spaces.  On the diagonal \(p=p'=2\), \(L^2\) and \(\ell^2\) are the formed
modules on the vector spaces \(L^2\) and \(\ell^2\), with
\(b(f,g)=\int_{\mathbb R}fg\) and \(b(a,c)=\sum_{n\in\mathbb N}a_n c_n\)
respectively.
"""

from functools import partial

from sage.categories.category import Category
from sage.functions.log import exp
from sage.functions.trig import cos, sin
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.rings.fraction_field import FractionField_generic
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ
from sage.rings.laurent_series_ring_element import LaurentSeries
from sage.rings.lazy_series import LazyPowerSeries
from sage.rings.lazy_series_ring import LazyPowerSeriesRing
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.power_series_ring import PowerSeriesRing
from sage.rings.power_series_ring_element import PowerSeries
from sage.rings.qqbar import AA
from sage.rings.rational_field import QQ
from sage.rings.semirings.non_negative_integer_semiring import NN
from sage.structure.element import Element, ModuleElement
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.symbolic.expression import Expression
from sage.symbolic.function import Function as SymbolicMap
from sage.symbolic.integration.integral import integrate
from sage.symbolic.operators import add_vararg, mul_vararg
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
)
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FormModules,
    PairedModules,
    SymmetricBilinearFormModules,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
from dzack_research.preamble.categories.modules.pure.modules import Modules, VectorSpaces
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.cardinals import continuum
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.rings.real import RR, ExactRealNumber


class _LebesgueIntegrationMorphism(ModuleMorphism):
    r"""Integration on ``L^1`` as the represented linear functional."""

    def __init__(self, parent, evaluate) -> None:
        super().__init__(parent, evaluate, elementwise=True)

    def _elementwise_linearity_derivation(self):
        # Additivity and scalar compatibility are the linearity theorem for the
        # Lebesgue integral on integrable real-valued functions.
        return True


def _regularity(k):
    if k is Infinity or k == Infinity:
        return Infinity
    integers = _own_ring(ZZ)
    k = integers(k)
    if k < integers.zero():
        raise ValueError("C^k is defined for k >= 0")
    return k


def _integrability(p):
    r"""Normalize the positive extended-real exponent supplied at map ingress.

    The symbolic field is the private expression realization of the owned
    exact real. Rational exponents retain their integer/rational spelling;
    irrational exponents are not replaced by rational approximations.
    """
    from dzack_research.preamble.logic import ask

    if p is Infinity:
        return Infinity
    real = RR(p)
    match ask(real > RR.zero()):
        case True:
            expression = real.expression()
            if expression in QQ:
                rational = _own_ring(QQ)._from_engine_element(QQ(expression))
                integers = _own_ring(ZZ)
                return integers(rational) if rational in integers else rational
            return real
        case False:
            raise ValueError("L^p and ell^p are defined for p > 0")
        case _:
            raise TypeError("positivity of the supplied exact exponent is undecided")


def _exponent_key(exponent):
    r"""Private expression key for a normalized, possibly irrational exponent."""
    return ("infinity",) if exponent is Infinity else ("finite", RR(exponent).expression())


def _l2_real_polynomial(expression, variable):
    r"""Return ``expression`` as an exact real-algebraic polynomial, or ``None``."""
    if not expression.is_polynomial(variable):
        return None
    coefficients = expression.coefficients(variable, sparse=False)
    if not all(coefficient in AA for coefficient in coefficients):
        return None
    return AA[str(variable)](coefficients)


def _l2_rational_function(expression, variable):
    r"""Return an exact reduced real rational function ``(p,q)``, or ``None``."""
    numerator = _l2_real_polynomial(expression.numerator(), variable)
    denominator = _l2_real_polynomial(expression.denominator(), variable)
    if numerator is None or denominator is None:
        return None
    common = numerator.gcd(denominator)
    return numerator // common, denominator // common


def _l2_rational_verdict(expression, variable):
    r"""Decide square-integrability of an exact real rational function.

    In lowest terms ``p/q`` belongs to ``L^2(RR)`` exactly when ``q`` has no
    real root and ``deg(q) >= deg(p)+1``.  A real root is a genuine pole and
    the degree inequality is precisely the ``p``-test at infinity.
    """
    fraction = _l2_rational_function(expression, variable)
    if fraction is None:
        return None
    numerator, denominator = fraction
    if denominator.roots(AA):
        return False
    return denominator.degree() >= numerator.degree() + 1


def _l2_gaussian(expression, variable) -> bool:
    if expression.operator() is not exp:
        return False
    exponent = expression.operands()[0]
    return (
        exponent.is_polynomial(variable)
        and exponent.degree(variable) == 2
        and bool(exponent.coefficient(variable, 2) < 0)
    )


def _l2_polynomially_bounded(expression, variable) -> bool:
    if expression.is_polynomial(variable):
        return True
    if expression.operator() in (sin, cos):
        return expression.operands()[0].is_polynomial(variable)
    return False


def _l2_schwartz(expression, variable) -> bool:
    factors = (
        expression.operands()
        if expression.operator() is mul_vararg
        else (expression,)
    )
    return any(_l2_gaussian(factor, variable) for factor in factors) and all(
        _l2_gaussian(factor, variable)
        or _l2_polynomially_bounded(factor, variable)
        for factor in factors
    )


def _l2_bounded(expression, variable) -> bool:
    if expression.operator() in (sin, cos):
        return True
    fraction = _l2_rational_function(expression, variable)
    if fraction is None:
        return False
    numerator, denominator = fraction
    return (
        not denominator.roots(AA)
        and denominator.degree() >= numerator.degree()
    )


def _engine_square_integral_verdict(expression, variable):
    r"""Decide \(\int_{\mathbb R} f^2<\infty\) by Sage's symbolic integration.

    Private engine adapter (`OWN-06`).  Its one owning caller is
    :func:`_l2_symbolic_verdict`, after the exact criteria there have not
    decided the formula.  The upstream operation is
    ``sage.symbolic.integration.integral.integrate`` on \(f^2\) over
    \((-\infty,\infty)\) with its default engine.  The engine reports that it
    reached no closed answer by raising ``RuntimeError``, ``TypeError`` or
    ``ValueError``; this adapter is the one site that reads those exceptions,
    and it reads each as *undecided* (``None``), never as nonmembership.  A
    returned ``+Infinity`` is divergence (``False``), a returned numeric value
    is convergence (``True``), and any other symbolic value is undecided.
    """
    try:
        integral = integrate(expression**2, variable, -Infinity, Infinity)
    except (RuntimeError, TypeError, ValueError):
        return None
    if integral is Infinity or integral == Infinity:
        return False
    if SR(integral).is_numeric():
        return True
    return None


def _l2_symbolic_verdict(expression, variable):
    r"""Return ``True``, ``False`` or ``None`` for membership in ``L^2(RR)``.

    ``None`` means that the supported exact criteria do not decide the
    formula; construction then remains an explicit placement claim.  In
    particular, failure of symbolic integration is never interpreted as a
    proof of nonmembership.
    """
    rational = _l2_rational_verdict(expression, variable)
    if rational is not None:
        return rational

    if expression.operator() in (sin, cos):
        argument = expression.operands()[0]
        if argument.is_polynomial(variable) and argument.degree(variable) == 1:
            return False

    if _l2_schwartz(expression, variable):
        return True

    if expression.operator() is add_vararg:
        verdicts = tuple(
            _l2_symbolic_verdict(summand, variable)
            for summand in expression.operands()
        )
        if all(verdict is True for verdict in verdicts):
            return True
        if verdicts.count(False) == 1 and verdicts.count(None) == 0:
            return False

    if expression.operator() is mul_vararg:
        factors = expression.operands()
        for position, factor in enumerate(factors):
            others = factors[:position] + factors[position + 1 :]
            if all(_l2_bounded(other, variable) for other in others):
                if _l2_symbolic_verdict(factor, variable) is True:
                    return True

    return _engine_square_integral_verdict(expression, variable)


def _parameter_name(value) -> str:
    if value is Infinity:
        return "Infinity"
    return str(value)


def _parameter_latex(value) -> str:
    if value is Infinity:
        return r"\infty"
    return str(latex(value))


def _space_name(space) -> str:
    if space is RR:
        return "RR"
    return repr(space)


def _space_latex(space) -> str:
    if space is RR:
        return r"\mathbb{R}"
    return str(latex(space))


def _conjugate_exponent(p):
    r"""The Hölder conjugate: \(1/p + 1/p' = 1\)."""
    if p is Infinity:
        return _own_ring(ZZ).one()
    if p == 1:
        return Infinity
    return _integrability(p / (p - 1))


def _are_holder_conjugates(p, q) -> bool:
    return _conjugate_exponent(p) == q


@cached_function
def _lebesgue_pairing_module(left, right):
    r"""The pairing \(\int fg\colon L^p\otimes L^{p'}\to\mathbb R\)."""
    if left is right:
        return left
    return PairedModules(RR)(left.pairings_with(right, RR)(_l2_pairing))


def _l2_pairing(left, right):
    r"""The pairing \(\int_{\mathbb R} fg\) on formulas in \(L^2(\mathbb R)\)."""
    formula = left.expression() * right.expression()
    return formula.integrate(left.parent().indeterminate(), -Infinity, Infinity)


@cached_function
def _sequence_pairing_module(left, right):
    r"""The pairing \(\sum a_n b_n\colon \ell^p\otimes\ell^{p'}\to\mathbb R\)."""
    if left is right:
        return left
    return PairedModules(RR)(left.pairings_with(right, RR)(_ell2_pairing))


def _ell2_pairing(left, right):
    r"""The pairing \(\sum_{n\in\mathbb N} a_n b_n\) on sequences in \(\ell^p\)."""
    left_family = left._coefficient_family()
    right_family = right._coefficient_family()
    if left_family is not None and right_family is not None:
        indices = left_family.keys() | right_family.keys()
        return RR(
            sum(
                left_family.get(index, 0) * right_family.get(index, 0) for index in indices
            )
        )
    if left_family is not None:
        return RR(
            sum(
                coefficient * right.evaluate_at(index)
                for index, coefficient in left_family.items()
            )
        )
    if right_family is not None:
        return RR(
            sum(
                coefficient * left.evaluate_at(index)
                for index, coefficient in right_family.items()
            )
        )
    formula = left.expression() * right.expression()
    return RR(formula.sum(left.parent().indeterminate(), ZZ.zero(), Infinity))


def _univariate_coefficient_family(value):
    r"""Coefficients of a univariate polynomial or truncated formal series, or none.

    Element-constructor ingress (`OWN-06`): called only by
    ``_FunctionSpace._element_constructor_``, it inspects the
    foreign Sage representation of the supplied datum and returns its
    coefficients as a finite family on \(\mathbb N\).
    """
    if isinstance(value, Polynomial):
        if value.parent().ngens() != 1:
            return None
        return {ZZ(exponent): coefficient for exponent, coefficient in value.dict().items()}
    if isinstance(value, PowerSeries):
        return {ZZ(exponent): coefficient for exponent, coefficient in value.dict().items()}
    if isinstance(value, LaurentPolynomial):
        family = {
            ZZ(exponent): coefficient for exponent, coefficient in value.dict().items()
        }
        if any(exponent < 0 for exponent in family):
            raise TypeError(
                "a Laurent series is a two-sided sequence; ell^p is indexed by NN"
            )
        return family
    if isinstance(value, LaurentSeries):
        return _univariate_coefficient_family(value.laurent_polynomial())
    return None


def _is_placed_callable(value) -> bool:
    r"""Whether ``value`` is a bare callable placed as a map.

    Element-constructor ingress (`OWN-06`): called only by
    ``_FunctionSpace._element_constructor_``.  A parent, an
    element, a type, a symbolic function or a category is callable without
    being a map to place.
    """
    if isinstance(value, (Parent, Element, type, SymbolicMap, Category)):
        return False
    return callable(value)


def _univariate_expression(formula, indeterminate):
    expression = SR(formula)
    variables = expression.variables()
    if not variables:
        return expression
    if len(variables) != 1:
        raise TypeError(f"{formula} is not a univariate formula")
    return expression.subs({variables[0]: indeterminate})


def _expression_from_value(value, indeterminate):
    r"""Return an \(\mathrm{SR}\) formula for a recognized primitive, if any.

    Element-constructor ingress (`OWN-06`): called only by
    ``_FunctionSpace._element_constructor_`` (and by itself on a
    Laurent series), it inspects the foreign Sage representation of the
    supplied datum and crosses it into one symbolic formula.
    """
    if isinstance(value, Expression):
        return _univariate_expression(value, indeterminate)
    if isinstance(value, SymbolicMap):
        return value(indeterminate)
    if isinstance(value, ExactRealNumber):
        return value.expression()
    if isinstance(value, Polynomial):
        return _univariate_expression(value, indeterminate)
    if isinstance(value, LaurentPolynomial):
        return sum(
            coefficient * indeterminate**exponent
            for exponent, coefficient in value.dict().items()
        )
    if isinstance(value, PowerSeries):
        return _univariate_expression(value.polynomial(), indeterminate)
    if isinstance(value, LaurentSeries):
        return _expression_from_value(value.laurent_polynomial(), indeterminate)
    value_parent = element_parent(value)
    if isinstance(value_parent, FractionField_generic) and isinstance(
        value_parent.base(), PolynomialRing_generic
    ):
        return _univariate_expression(value.numerator(), indeterminate) / _univariate_expression(
            value.denominator(), indeterminate
        )
    if value in RR:
        return RR(value).expression()
    return None


class _RealMap(ModuleElement):
    r"""A map \(X\to Y\), as an element of a function space."""

    def __init__(self, parent, evaluate, expression=None, coefficients=None) -> None:
        ModuleElement.__init__(self, parent)
        self._evaluate = evaluate
        self._expression = expression
        self._coefficients = coefficients

    def expression(self):
        r"""Return the symbolic formula from which this map was constructed."""
        if self._expression is None:
            raise ValueError(f"{self} is a placed callable; it has no symbolic formula")
        return self._expression

    def _formula(self):
        r"""The formula this map was constructed from, or ``None`` for a placed callable.

        Protected contract of the function-space element: the pointwise
        operations and the calculus of maps of class \(C^k\) read it to
        decide whether a result is computed on formulas or pointwise.
        """
        return self._expression

    def _coefficient_family(self):
        return self._coefficients

    def generating_series(self, series_ring=None):
        r"""The ordinary generating series \(\sum a_n t^n\).

        A finitely supported sequence, constructed from a polynomial or
        truncated series, returns a truncated power series.  A formula
        in the index returns the closed sum \(\sum a_n t^n\) when Sage
        can evaluate it.
        """
        family = self._coefficient_family()
        if family is not None:
            if series_ring is None:
                series_ring = PowerSeriesRing(QQ, "t")
            if not family:
                return series_ring.zero()
            degree = max(family)
            terms = [family.get(ZZ(index), 0) for index in range(degree + 1)]
            return series_ring(terms)
        formula = self.expression()
        index = self.parent().indeterminate()
        indeterminate = series_ring.gen() if series_ring is not None else SR.var("t")
        return (formula * indeterminate**index).sum(index, ZZ.zero(), Infinity)

    def evaluate_at(self, point):
        r"""Evaluate this map at a point of its domain."""
        value = self._evaluate(self.parent().domain()(point))
        return self.parent().codomain()(value)

    def as_set_morphism(self):
        r"""This map as an element of \(\operatorname{Hom}_{\mathbf{Set}}(X,Y)\)."""
        return self.parent().set_homset()(self.evaluate_at)

    def __call__(self, argument):
        r"""Evaluate at a point, or compose with a map landing in the domain.

        Composition is the operation of differentiability classes: a map
        of class \(C^k\) applied to a map of class \(C^\ell\) into its
        domain is their composite.
        """
        source = element_parent(argument)
        space = self.parent()
        match source:
            case _ if (
                _is_differentiability_class(source)
                and _is_differentiability_class(space)
                and source.codomain() is space.domain()
            ):
                return self.compose(argument)
            case _:
                return self.evaluate_at(argument)

    def _add_(self, other):
        left_family = self._coefficient_family()
        right_family = other._coefficient_family()
        if left_family is not None and right_family is not None:
            family = dict(left_family)
            for index, coefficient in right_family.items():
                family[index] = family.get(index, 0) + coefficient
            return self.parent()._sequence_from_coefficients(family)
        if self._formula() is None or other._formula() is None:
            return self.parent()._placed(
                lambda point: self.evaluate_at(point) + other.evaluate_at(point)
            )
        return self.parent()(self._formula() + other._formula())

    def _neg_(self):
        family = self._coefficient_family()
        if family is not None:
            return self.parent()._sequence_from_coefficients(
                {index: -coefficient for index, coefficient in family.items()}
            )
        if self._formula() is None:
            return self.parent()._placed(lambda point: -self.evaluate_at(point))
        return self.parent()(-self._formula())

    def _lmul_(self, scalar):
        coefficient = RR(scalar)
        family = self._coefficient_family()
        if family is not None:
            return self.parent()._sequence_from_coefficients(
                {index: coefficient * value for index, value in family.items()}
            )
        if self._formula() is None:
            return self.parent()._placed(lambda point: coefficient * self.evaluate_at(point))
        return self.parent()(coefficient.expression() * self._formula())

    def _mul_(self, other):
        left_family = self._coefficient_family()
        right_family = other._coefficient_family()
        if left_family is not None and right_family is not None:
            return self.parent()._sequence_from_coefficients(
                {
                    index: left_family[index] * right_family[index]
                    for index in left_family.keys() & right_family.keys()
                }
            )
        if self._formula() is None or other._formula() is None:
            return self.parent()._placed(
                lambda point: self.evaluate_at(point) * other.evaluate_at(point)
            )
        return self.parent()(self._formula() * other._formula())

    def _div_(self, other):
        if self._formula() is None or other._formula() is None:
            return self.parent()._placed(
                lambda point: self.evaluate_at(point) / other.evaluate_at(point)
            )
        return self.parent()(self._formula() / other._formula())

    def __mul__(self, other):
        other = self.parent()(other)
        return self._mul_(other)

    def __truediv__(self, other):
        other = self.parent()(other)
        return self._div_(other)

    def _repr_(self) -> str:
        if self._expression is not None:
            return repr(self._expression)
        if self._coefficients is not None:
            return repr(self.generating_series())
        return f"Map {self.parent().domain()} -> {self.parent().codomain()} defined pointwise"

    def _latex_(self) -> str:
        if self._expression is not None:
            return str(latex(self._expression))
        if self._coefficients is not None:
            return str(latex(self.generating_series()))
        return (
            r"\text{pointwise-defined map }"
            + str(latex(self.parent().domain()))
            + r"\to "
            + str(latex(self.parent().codomain()))
        )


class _DifferentiableMap(_RealMap):
    r"""A map of class \(C^k\), with its calculus."""

    def compose(self, other):
        r"""Return \(f\circ g\), in \(C^{\min(k,\ell)}(W,Y)\)."""
        outer = self.parent()
        if not _is_differentiability_class(element_parent(other)):
            other = outer(other)
        inner = other.parent()
        if inner.codomain() is not outer.domain():
            raise TypeError(
                f"cannot compose {self} after {other}: "
                f"codomain {inner.codomain()} is not domain {outer.domain()}"
            )
        k = min(outer.differentiability(), inner.differentiability())
        target = C(k, inner.domain(), outer.codomain())
        if self._formula() is None or other._formula() is None:
            return target._placed(lambda point: self.evaluate_at(other.evaluate_at(point)))
        return target(self._formula().subs({outer.indeterminate(): other._formula()}))

    def derivative(self):
        r"""Return \(f'\), in \(C^{k-1}(X,Y)\) when \(k\) is finite."""
        space = self.parent()
        k = space.differentiability()
        if k == 0:
            raise ValueError(f"{self} is merely continuous; it has no C^k derivative")
        target = space if k is Infinity else C(k - 1, space.domain(), space.codomain())
        return target(self.expression().diff(space.indeterminate()))

    def integral_from(self, lower):
        r"""Return \(x\mapsto\int_a^x f\), in \(C^{k+1}(\mathbb R,\mathbb R)\) when \(k\) is finite."""
        space = self.parent()
        a = RR(lower)
        x = space.indeterminate()
        antiderivative = self.expression().integral(x)
        k = space.differentiability()
        target = space if k is Infinity else C(k + 1, space.domain(), space.codomain())
        return target(antiderivative - antiderivative.subs({x: a.expression()}))

    def taylor_series(self, centre):
        r"""The Taylor series of this map at ``centre``, as a formal power series in \(t = x - a\).

        For \(C^\infty(\mathbb R)\) this is the untruncated series
        \(\sum_{n\ge 0} f^{(n)}(a)\, t^n / n!\).  For finite regularity
        \(k\) it is the jet of order \(k\).
        """
        space = self.parent()
        k = space.differentiability()
        if space.domain() is not RR or space.codomain() is not RR:
            raise TypeError(f"Taylor series is defined for maps RR -> RR, not {space}")
        formula = self.expression()
        x = space.indeterminate()
        shifted = formula.subs({x: RR(centre).expression() + x})
        if k is Infinity:
            return LazyPowerSeriesRing(SR, "t").taylor(shifted)
        jet = shifted.taylor(x, ZZ.zero(), k)
        t = SR.var("t")
        return PowerSeriesRing(SR, "t")(jet.subs({x: t}))

    def maclaurin_series(self):
        r"""The Maclaurin series of this map: the Taylor series at \(0\)."""
        return self.taylor_series(ZZ.zero())


class _FunctionSpace:
    r"""A function space: a set of maps \(X\to Y\) between two fixed sets.

    An engine realizing objects of ``Sets()``, and the shared construction of
    the differentiability classes, Lebesgue spaces and sequence spaces below.
    A function space is singled out inside the exponential
    \(Y^X=\operatorname{Hom}_{\mathbf{Set}}(X,Y)\) by a condition on its maps
    -- a differentiability class, an integrability exponent, a summability
    exponent -- so it is a subset of that exponential and not the exponential
    itself.

    The datum is the domain \(X\), the codomain \(Y\), and the indeterminate
    in which a map given by a formula is written.  An element is a map, given
    by a formula, by a finitely supported coefficient family on
    \(\mathbb N\), or by a placed callable; the pointwise operations are
    computed on formulas and families where both operands have them, and
    pointwise otherwise.
    """

    Element = _RealMap

    def __init__(self, domain, codomain, indeterminate, **rest) -> None:
        self._map_domain = domain
        self._map_codomain = codomain
        self._indeterminate = SR(indeterminate)
        super().__init__(**rest)

    def __call__(self, value):
        r"""Admit a formula or placed map at the function-space engine boundary."""
        return self._element_constructor_(value)

    def _element_of_unformed_module(self, element):
        return self.unformed_module()._reparent(element)

    def _element_from_unformed_module(self, element):
        return self._reparent(element)

    def domain(self):
        return self._map_domain

    def codomain(self):
        return self._map_codomain

    def indeterminate(self):
        return self._indeterminate

    def set_homset(self):
        r"""\(\operatorname{Hom}_{\mathbf{Set}}(X,Y)\)."""
        return Sets().Mor(self.domain(), self.codomain())

    def zero(self):
        return self._element_constructor_(ZZ.zero())

    def one(self):
        return self._element_constructor_(ZZ.one())

    def _an_element_(self):
        return self.zero()

    def _placed(self, evaluate):
        return self.element_class(self, evaluate=evaluate)

    def _map_from_expression(self, expression):
        formula = _univariate_expression(expression, self.indeterminate())
        on_reals = self.domain() is RR

        def evaluate(point, formula=formula, on_reals=on_reals):
            variables = formula.variables()
            if not variables:
                return RR(formula)
            symbol = point.expression() if on_reals else SR(point)
            return RR(formula.subs({variables[0]: symbol}))

        return self.element_class(self, evaluate=evaluate, expression=formula)

    def _map_from_callable(self, placed):
        def evaluate(point, placed=placed):
            return placed(point)

        return self.element_class(self, evaluate=evaluate)

    def _reparent(self, value):
        r"""The map ``value`` of another space on the same domain and codomain, read here."""
        coefficients = value._coefficient_family()
        if coefficients is not None:
            return self._sequence_from_coefficients(coefficients)
        formula = value._formula()
        if formula is None:
            return self.element_class(
                self,
                evaluate=lambda point, source=value: source.evaluate_at(point),
            )
        return self._map_from_expression(formula)

    def _sequence_from_coefficients(self, coefficients):
        r"""The sequence whose ordinary generating series has these coefficients."""
        family = {
            ZZ(index): self.codomain()(coefficient)
            for index, coefficient in coefficients.items()
            if coefficient
        }
        zero = self.codomain().zero()

        def evaluate(point, family=family, zero=zero):
            return family.get(ZZ(point), zero)

        return self.element_class(self, evaluate=evaluate, coefficients=family)

    def _sequence_from_lazy_series(self, series):
        r"""The coefficient sequence of an untruncated formal power series."""

        def evaluate(point, series=series):
            return self.codomain()(series[ZZ(point)])

        return self.element_class(self, evaluate=evaluate)

    def _element_constructor_(self, value):
        source = element_parent(value)
        if source is self:
            return value
        if self.codomain() is RR and source in Modules(RR) and source.unformed_module() is self:
            return source._element_of_unformed_module(value)
        if (
            _is_function_space(source)
            and source.domain() is self.domain()
            and source.codomain() is self.codomain()
        ):
            return self._reparent(value)
        if self.domain() is NN:
            if isinstance(value, LazyPowerSeries):
                return self._sequence_from_lazy_series(value)
            family = _univariate_coefficient_family(value)
            if family is not None:
                return self._sequence_from_coefficients(family)
        if self.codomain() is RR:
            formula = _expression_from_value(value, self.indeterminate())
            if formula is not None:
                return self._map_from_expression(formula)
        if _is_placed_callable(value):
            return self._map_from_callable(value)
        raise TypeError(f"{value!r} does not name a map {self.domain()} -> {self.codomain()}")


def _is_function_space(space) -> bool:
    r"""Whether ``space`` is a function space realized by :class:`_FunctionSpace`.

    Declared engine adapter (`OWN-06`).  Function spaces form no category of
    their own: each is an object of ``Sets()`` or of a vector-space or algebra
    category, realized by the engine classes of this module.  Recognizing a
    space that engine realized is a question about the engine, and this is
    its one site.  Its callers are the element constructor, which reparents a
    map of another function space, and :func:`_is_differentiability_class`,
    :func:`_is_lebesgue_space` and :func:`_is_sequence_space`.
    """
    return isinstance(space, _FunctionSpace)


def _is_differentiability_class(space) -> bool:
    r"""Whether ``space`` is a differentiability class \(C^k(X,Y)\) realized by :class:`_DifferentiabilityClass`.

    Declared engine adapter (`OWN-06`), for the reason
    :func:`_is_function_space` states: composition, coercion and membership
    between differentiability classes recognize one here.
    """
    return isinstance(space, _DifferentiabilityClass)


def _is_lebesgue_space(space) -> bool:
    r"""Whether ``space`` is a Lebesgue space \(\mathcal L^p(\mathbb R)\) realized by :class:`_LebesgueSpace`.

    Declared engine adapter (`OWN-06`), for the reason
    :func:`_is_function_space` states: the Hölder product and the graded
    Lebesgue modules recognize one here.
    """
    return isinstance(space, _LebesgueSpace)


def _is_sequence_space(space) -> bool:
    r"""Whether ``space`` is a sequence space \(\ell^p(\mathbb R)\) realized by :class:`_SequenceSpace`.

    Declared engine adapter (`OWN-06`), for the reason
    :func:`_is_function_space` states: the Hölder product recognizes one here.
    """
    return isinstance(space, _SequenceSpace)


class _DifferentiabilityClass(_FunctionSpace):
    r"""The differentiability class \(C^k(X,Y)\) of maps \(X\to Y\) of class \(C^k\).

    An engine realizing objects of ``Sets()``; the datum this level adds is
    the regularity \(k\in\mathbb N\cup\{\infty\}\).  The placement of an
    object is a theorem about its codomain: pointwise operations make
    \(C^k(X,Y)\) an \(\mathbb R\)-vector space when \(Y\) is one, realized by
    :class:`_VectorSpaceDifferentiabilityClass`, and when \(Y=\mathbb R\)
    pointwise product makes it a commutative unital \(\mathbb R\)-algebra,
    realized by :class:`_FunctionAlgebraDifferentiabilityClass`.
    ``C(k, X, Y)`` is the construction route.
    """

    Element = _DifferentiableMap

    def __init__(self, regularity, **rest) -> None:
        self._regularity = regularity
        super().__init__(**rest)

    def differentiability(self):
        return self._regularity

    def cardinality(self):
        r"""\(|C^k(\mathbb R,\mathbb R)| = 2^{\aleph_0}\); any other space answers as a set.

        The theorem: a continuous map \(\mathbb R\to\mathbb R\) is
        determined by its values on \(\mathbb Q\), so
        \(|C^k(\mathbb R,\mathbb R)|\le|\mathbb R^{\mathbb Q}|
        =(2^{\aleph_0})^{\aleph_0}=2^{\aleph_0}\), and the constant maps
        give the reverse inequality.  Every other represented space has
        the cardinality its underlying set supplies.
        """
        if self.domain() is RR and self.codomain() is RR:
            return continuum
        return super().cardinality()

    def is_integral_domain(self, proof=True):
        r"""Pointwise product has zero-divisors: bump functions."""
        return False

    def is_field(self, proof=True):
        return False

    def fraction_field(self):
        raise TypeError(f"{self} is not an integral domain")

    def coordinate(self):
        r"""The identity map, an element of \(C^k(X,X)\)."""
        if self.domain() is not self.codomain():
            raise TypeError("the identity map lives in C(k, X) = C(k, X, X)")
        if self.domain() is RR:
            return self(self.indeterminate())
        return self._placed(lambda point: point)

    def integral(self, integrand, lower):
        r"""The map \(x\mapsto\int_a^x f(t)\,dt\)."""
        return integrand.integral_from(lower)

    def _coerce_map_from_(self, source):
        r"""Sage's coercion hook: the constants, and \(C^\ell(X,Y)\to C^k(X,Y)\) for \(\ell\ge k\)."""
        if source is RR or source is ZZ or source is QQ:
            return True
        if not _is_differentiability_class(source):
            return None
        if source.domain() is not self.domain() or source.codomain() is not self.codomain():
            return None
        if source.differentiability() >= self.differentiability():
            return True
        return None

    def __contains__(self, value) -> bool:
        source = element_parent(value)
        if source is self:
            return True
        if not _is_differentiability_class(source):
            return False
        return (
            source.domain() is self.domain()
            and source.codomain() is self.codomain()
            and source.differentiability() >= self.differentiability()
        )

    def _repr_(self) -> str:
        k = _parameter_name(self.differentiability())
        source = _space_name(self.domain())
        if self.domain() is self.codomain():
            return f"C({k}, {source})"
        return f"C({k}, {source}, {_space_name(self.codomain())})"

    def _latex_(self) -> str:
        k = _parameter_latex(self.differentiability())
        source = _space_latex(self.domain())
        if self.domain() is self.codomain():
            return rf"C^{{{k}}}({source})"
        return rf"C^{{{k}}}({source}, {_space_latex(self.codomain())})"


class _VectorSpaceDifferentiabilityClass(_DifferentiabilityClass):
    r"""\(C^k(X,Y)\) for a real vector space \(Y\): an object of ``VectorSpaces(RR)`` under pointwise operations."""


class _FunctionAlgebraDifferentiabilityClass(_DifferentiabilityClass):
    r"""\(C^k(X,\mathbb R)\): a commutative unital \(\mathbb R\)-algebra under pointwise operations."""


@cached_function
def _differentiability_class(regularity, domain, codomain):
    r"""Build \(C^k(X,Y)\) in the category its codomain places it in."""
    data = {
        "regularity": regularity,
        "domain": domain,
        "codomain": codomain,
        "indeterminate": SR.var("x"),
    }
    match codomain:
        case _ if codomain is RR:
            algebras = Algebras(RR).Associative().Unital().Commutative()
            return _object_of(
                Cat().meet((VectorSpaces(RR), algebras)),
                _engine=(Algebras(RR), _FunctionAlgebraDifferentiabilityClass, _DifferentiableMap),
                base_ring=RR,
                _engine_product=lambda left, right: _RealMap._mul_(left, right),
                _engine_scalar_action=lambda scalar, element: _RealMap._lmul_(element, scalar),
                _engine_unit=lambda algebra: algebra._element_constructor_(1),
                **data,
            )
        case _ if codomain in VectorSpaces(RR):
            modules = VectorSpaces(RR)
            return _object_of(
                modules,
                _engine=(modules, _VectorSpaceDifferentiabilityClass, _DifferentiableMap),
                base_ring=RR,
                **data,
            )
        case _:
            return _object_of(
                Sets(), _engine=(Sets(), _DifferentiabilityClass, _DifferentiableMap), **data
            )


class _DifferentiabilityClassNotation:
    r"""The notation ``C`` for differentiability classes.

    ``C(k, X, Y)`` and ``(C^k)(X, Y)`` are \(C^k(X,Y)\), and ``C(k, X)`` is
    \(C^k(X,X)\).  The regularity \(k\) is a parameter; \(\infty\) is a value
    of \(k\), not a separate constructor.

    EXAMPLES::

        sage: from dzack_research.preamble.all import Algebras, C, RR, VectorSpaces, exp
        sage: (C^Infinity)(RR) is C(Infinity, RR, RR)
        True
        sage: (C^2)(RR, RR) is C(2, RR)
        True
        sage: (C^Infinity)(RR) in VectorSpaces(RR)
        True
        sage: (C^Infinity)(RR) in Algebras(RR)
        True
        sage: x = (C^Infinity)(RR).coordinate()
        sage: x(3)
        3
        sage: f = (C^Infinity)(RR)(exp)
        sage: f(0)
        1
        sage: (f * x)(0)
        0
        sage: f(x * x)(0)
        1
        sage: (C^Infinity)(RR).integral(x, 0)(2)
        2
    """

    def __call__(self, k, domain, codomain=None):
        return _differentiability_class(
            _regularity(k), domain, domain if codomain is None else codomain
        )

    def __pow__(self, k):
        r"""``C^k``: the construction \((X, Y)\mapsto C^k(X,Y)\) for one regularity."""
        return partial(self, _regularity(k))

    __xor__ = __pow__

    def __repr__(self) -> str:
        return "C"

    def _latex_(self) -> str:
        return "C"


C = _DifferentiabilityClassNotation()


class _LebesgueSpace(_FunctionSpace):
    r"""The space \(\mathcal L^p(\mathbb R)\) of \(p\)-integrable maps \(\mathbb R\to\mathbb R\).

    An engine realizing objects of ``VectorSpaces(RR)``: pointwise operations
    make the \(p\)-integrable maps a real vector space.  The datum this level
    adds is the exponent \(p\in(0,\infty]\).  The Lebesgue space
    \(L^p(\mathbb R)\) proper is the quotient of \(\mathcal L^p(\mathbb R)\)
    by the maps vanishing almost everywhere; its elements are classes, not
    maps; ``quotient_by_null_functions`` constructs that quotient.

    \(\mathcal L^2(\mathbb R)\) is the formed module on the vector space
    \(\mathcal L^2\) with the symmetric bilinear form
    \(b(f,g)=\int_{\mathbb R}fg\), which vanishes on the null maps, realized by
    :class:`_SquareIntegrableFormedSpace`.  A general \(\mathcal L^p\) is not:
    Hölder pairs it with \(\mathcal L^{p'}\) as ``Lp(p) * Lp(p')``.
    ``Lp(p)`` is the construction route.

    EXAMPLES::

        sage: from dzack_research.preamble.all import (
        ....:     C, FormModules, Lp, PairedModules, RR,
        ....:     SymmetricBilinearFormModules, VectorSpaces, exp,
        ....: )
        sage: L = Lp(2)
        sage: L
        L^2(RR)
        sage: L in VectorSpaces(RR)
        True
        sage: L in SymmetricBilinearFormModules(RR)
        True
        sage: L in FormModules(RR)
        True
        sage: Lp(1) in FormModules(RR)
        False
        sage: Maps = C(Infinity, RR)
        sage: gaussian = Maps(exp(-Maps.indeterminate() ** 2))
        sage: L(gaussian)(0)
        1
        sage: L.b(L(gaussian), L(gaussian))
        1/2*sqrt(2)*sqrt(pi)
        sage: L.q(L(gaussian))
        1/2*sqrt(2)*sqrt(pi)
        sage: L.pairing_module() is L
        True
        sage: Lp(1) * Lp(Infinity) in PairedModules(RR)
        True
        sage: Lp(1) * Lp(Infinity) in FormModules(RR)
        False
    """

    def __init__(self, exponent, **rest) -> None:
        self._exponent = exponent
        super().__init__(**rest)

    def _element_constructor_(self, value):
        element = super()._element_constructor_(value)
        exponent = self.integrability_exponent()
        formula = element._formula()
        if formula is not None and not formula.variables() and exponent is not Infinity:
            from dzack_research.preamble.logic import ask

            if ask(RR(formula) != RR.zero()) is True:
                raise ValueError("a nonzero constant on R has infinite finite-p integral")
        if (exponent == 2) is not True:
            return element
        formula = element._formula()
        if formula is None:
            return element
        verdict = _l2_symbolic_verdict(formula, self.indeterminate())
        if verdict is False:
            raise ValueError(f"{formula} is not square-integrable on RR")
        return element

    def quotient_by_null_functions(self):
        r"""The actual Lebesgue space, quotienting these maps by a.e. equality."""
        from dzack_research.preamble.categories.functions.lebesgue_quotients import _lebesgue_quotient

        return _lebesgue_quotient(self)

    def almost_everywhere_equal(self, left, right):
        r"""The proposition that the two integrable maps agree outside a null set."""
        from dzack_research.preamble.categories.functions.lebesgue_quotients import AlmostEverywhereEquality

        return AlmostEverywhereEquality(self(left), self(right))

    def integrability_exponent(self):
        return self._exponent

    def conjugate_lebesgue_space(self):
        r"""The space \(L^{p'}\) with \(1/p+1/p'=1\)."""
        return Lp(_conjugate_exponent(self.integrability_exponent()))

    def integration_morphism(self):
        r"""Integration \(\iota:L^1(\mathbb R)\to\mathbb R\)."""
        if self.integrability_exponent() != 1:
            raise TypeError("integration as a bounded linear functional is owned by L^1(RR)")

        def evaluate(function, space=self):
            function = space(function)
            if function == space.zero():
                return RR.zero()
            return RR(function.expression().integrate(space.indeterminate(), -Infinity, Infinity))

        return _LebesgueIntegrationMorphism(Modules(RR).Mor(self, RR), evaluate)

    @cached_method
    def pairing_module(self):
        r"""The Hölder pairing module \(L^p\otimes L^{p'}\to\mathbb R\).

        When \(p=2\) this is \(L^2\) itself, as a formed module.
        """
        return self * self.conjugate_lebesgue_space()

    def __mul__(self, other):
        if not _is_lebesgue_space(other):
            raise TypeError(
                f"{self} * {other} is a pairing module only when both factors are Lebesgue spaces"
            )
        if not _are_holder_conjugates(
            self.integrability_exponent(), other.integrability_exponent()
        ):
            raise TypeError(
                f"{self} ⊗ {other} → RR is a pairing when 1/p + 1/q = 1"
            )
        return _lebesgue_pairing_module(self, other)

    def _repr_(self) -> str:
        return f"L^{_parameter_name(self.integrability_exponent())}(RR)"

    def _latex_(self) -> str:
        return rf"L^{{{_parameter_latex(self.integrability_exponent())}}}(\mathbb{{R}})"


class _SquareIntegrableFormedSpace(_LebesgueSpace):
    r"""\(\mathcal L^2(\mathbb R)\) with \(b(f,g)=\int_{\mathbb R}fg\): the formed module on the vector space \(\mathcal L^2\)."""


@cached_function(key=_exponent_key)
def _lebesgue_space(exponent):
    r"""Build \(L^p(\mathbb R)\); for \(p=2\), the formed module on the vector space \(L^2\).

    The form \(\int fg\) is a morphism out of the vector space, so the vector
    space is built first and retained as the formed module's unformed module
    (`CON-16`).
    """
    modules = VectorSpaces(RR)
    data = dict(exponent=exponent, base_ring=RR, domain=RR, codomain=RR, indeterminate=SR.var("x"))
    module = _object_of(modules, _engine=(modules, _LebesgueSpace, _RealMap), **data)
    if (exponent == 2) is not True:
        return module
    formed = SymmetricBilinearFormModules(RR)
    return _object_of(
        Cat().meet((modules, formed)),
        _engine=(FormModules(RR), _SquareIntegrableFormedSpace, _RealMap),
        source_form=module.bilinear_forms(RR)(_l2_pairing),
        **data,
    )


def Lp(p):
    r"""The real Lebesgue space \(L^p(\mathbb R)\), represented by its \(p\)-integrable maps."""
    return _lebesgue_space(_integrability(p))


class _SequenceSpace(_FunctionSpace):
    r"""The real sequence space \(\ell^p(\mathbb R)\) of \(p\)-summable maps \(\mathbb N\to\mathbb R\).

    An engine realizing objects of ``VectorSpaces(RR)``: pointwise operations
    make the \(p\)-summable sequences (the bounded ones for \(p=\infty\)) a
    real vector space.  The datum this level adds is the exponent
    \(p\in(0,\infty]\).  \(\ell^2(\mathbb R)\) is the formed module on the
    vector space \(\ell^2\) with \(b(a,c)=\sum_{n\in\mathbb N}a_n c_n\),
    realized by :class:`_SquareSummableFormedSpace`.  ``ell(p)`` is the
    construction route.
    """

    def __init__(self, exponent, **rest) -> None:
        self._exponent = exponent
        super().__init__(**rest)

    def integrability_exponent(self):
        return self._exponent

    def conjugate_sequence_space(self):
        r"""The space \(\ell^{p'}\) with \(1/p+1/p'=1\)."""
        return ell(_conjugate_exponent(self.integrability_exponent()))

    @cached_method
    def pairing_module(self):
        r"""The Hölder pairing module \(\ell^p\otimes\ell^{p'}\to\mathbb R\).

        When \(p=2\) this is \(\ell^2\) itself, as a formed module.
        """
        return self * self.conjugate_sequence_space()

    def __mul__(self, other):
        if not _is_sequence_space(other):
            raise TypeError(
                f"{self} * {other} is a pairing module only when both factors are sequence spaces"
            )
        if not _are_holder_conjugates(
            self.integrability_exponent(), other.integrability_exponent()
        ):
            raise TypeError(
                f"{self} ⊗ {other} → RR is a pairing when 1/p + 1/q = 1"
            )
        return _sequence_pairing_module(self, other)

    def _repr_(self) -> str:
        return f"ell^{_parameter_name(self.integrability_exponent())}(RR)"

    def _latex_(self) -> str:
        return rf"\ell^{{{_parameter_latex(self.integrability_exponent())}}}(\mathbb{{R}})"


class _SquareSummableFormedSpace(_SequenceSpace):
    r"""\(\ell^2(\mathbb R)\) with \(b(a,c)=\sum_n a_n c_n\): the formed module on the vector space \(\ell^2\)."""


@cached_function(key=_exponent_key)
def _sequence_space(exponent):
    r"""Build \(\ell^p(\mathbb R)\); for \(p=2\), the formed module on the vector space \(\ell^2\).

    The form \(\sum a_nb_n\) is a morphism out of the vector space, so the
    vector space is built first and retained as the formed module's unformed
    module (`CON-16`).
    """
    modules = VectorSpaces(RR)
    data = dict(exponent=exponent, base_ring=RR, domain=NN, codomain=RR, indeterminate=SR.var("n"))
    module = _object_of(modules, _engine=(modules, _SequenceSpace, _RealMap), **data)
    if (exponent == 2) is not True:
        return module
    formed = SymmetricBilinearFormModules(RR)
    return _object_of(
        Cat().meet((modules, formed)),
        _engine=(FormModules(RR), _SquareSummableFormedSpace, _RealMap),
        source_form=module.bilinear_forms(RR)(_ell2_pairing),
        **data,
    )


class _SequenceSpaceNotation:
    r"""The notation ``ell`` for sequence spaces.

    ``ell(p)``, ``ell(p, RR)`` and ``(ell^p)(RR)`` are \(\ell^p(\mathbb R)\).

    EXAMPLES::

        sage: from dzack_research.preamble.all import (
        ....:     FormModules, PairedModules, QQ, RR, VectorSpaces, ell,
        ....: )
        sage: ell(2) is ell(2, RR)
        True
        sage: ell(2) in FormModules(RR)
        True
        sage: ell(1) in FormModules(RR)
        False
        sage: n = ell(2).indeterminate()
        sage: geometric = ell(2)(2 ** (-n))
        sage: geometric(3)
        1/8
        sage: ell(2).b(geometric, geometric)
        4/3
        sage: t = QQ.polynomial_ring("t").gen()
        sage: truncated = ell(2)(1 + t + t**2)
        sage: truncated(3)
        0
        sage: ell(2).b(truncated, truncated)
        3
        sage: ell(2) * ell(2) is ell(2)
        True
        sage: ell(1) * ell(Infinity) in PairedModules(RR)
        True
        sage: ell(1) * ell(Infinity) in FormModules(RR)
        False
    """

    def __call__(self, p, values=None):
        assert values is None or values is RR, f"ell^p is sequences of reals, not of {values}"
        return _sequence_space(_integrability(p))

    def __pow__(self, p):
        r"""``ell^p``: the construction of \(\ell^p(\mathbb R)\) for one exponent."""
        return partial(self, _integrability(p))

    __xor__ = __pow__

    def __repr__(self) -> str:
        return "ell"

    def _latex_(self) -> str:
        return r"\ell"


ell = _SequenceSpaceNotation()
