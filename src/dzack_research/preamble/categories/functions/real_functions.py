r"""Mapping spaces \(C^k(X,Y)\), and \(L^p\), \(\ell^p\) as \(\mathbb R\)-modules of maps.

\(C(k,X,Y)\) is the space of maps \(X\to Y\) of class \(C^k\), a subset of
\(\operatorname{Hom}_{\mathbf{Set}}(X,Y)\).  The shorthand \(C(k,X)\) is
\(C(k,X,X)\).  The regularity \(k\) is a parameter; \(\infty\) is a value of
\(k\), not a separate constructor.  When the values are \(\mathbb R\),
pointwise product makes \(C^k(X,\mathbb R)\) a commutative
\(\mathbb R\)-algebra.

A map is constructed from the inductive class of formulas — polynomials,
named transcendentals, Laurent and power series, indefinite integrals, and
the pointwise operations and composition — when \(X=Y=\mathbb R\), or by
placing a callable.  Placement is the membership claim.

\(L^p(\mathbb R)\) is an \(\mathbb R\)-module of representatives on
\(\mathbb R\).  \(\ell^p(\mathbb R)\) is the same construction on
\(\mathbb N\): \(p\)-summable sequences.  A polynomial or formal power
series is a formula on \(\mathbb R\) in \(C^k\) and \(L^p\), and is its
coefficient sequence in \(\ell^p\).  A map in \(C^\infty(\mathbb R)\)
has a Maclaurin series and a Taylor series at any point, as formal
power series; a map in finite \(C^k\) has the jet of order \(k\).  Hölder pairs \(L^p\) with
\(L^{p'}\) and \(\ell^p\) with \(\ell^{p'}\) when \(1/p+1/p'=1\); that
pairing is the product of the two spaces.  On the diagonal \(p=p'=2\),
\(L^2\) and \(\ell^2\) are formed modules, with \(b(f,g)=\int_{\mathbb R}fg\)
and \(b(a,c)=\sum_{n\in\mathbb N}a_n c_n\) respectively.
"""

from sage.categories.category import Category
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.rings.fraction_field import FractionField_generic
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ
from sage.rings.polynomial.laurent_polynomial import LaurentPolynomial
from sage.rings.polynomial.polynomial_element import Polynomial
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.laurent_series_ring_element import LaurentSeries
from sage.rings.lazy_series import LazyPowerSeries
from sage.rings.lazy_series_ring import LazyPowerSeriesRing
from sage.rings.power_series_ring_element import PowerSeries
from sage.rings.power_series_ring import PowerSeriesRing
from sage.rings.rational_field import QQ
from sage.rings.semirings.non_negative_integer_semiring import NN
from sage.structure.element import Element, ModuleElement, parent as element_parent
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject
from sage.structure.unique_representation import UniqueRepresentation
from sage.symbolic.expression import Expression
from sage.symbolic.function import Function as SymbolicMap
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.sets.set_categories import Sets as OwnedSets
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    CommutativeAlgebras,
)
from dzack_research.preamble.categories.forms.forms import BilinearForms, Pairings
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    FormedModules,
    PairedModules,
    SymmetricBilinearFormModules,
)
from dzack_research.preamble.categories.modules.pure.modules import VectorSpaces
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.rings.real import RR, ExactRealNumber


def _regularity(k):
    if k is Infinity or k == Infinity:
        return Infinity
    integers = _own_ring(ZZ)
    k = integers(k)
    if k < integers.zero():
        raise ValueError("C^k is defined for k >= 0")
    return k


def _integrability(p):
    if p is Infinity or p == Infinity:
        return Infinity
    rationals = _own_ring(QQ)
    integers = _own_ring(ZZ)
    p = rationals(p)
    if p <= rationals.zero():
        raise ValueError("L^p and ell^p are defined for p > 0")
    try:
        integral = integers(p)
    except (TypeError, ValueError):
        return p
    return integral if rationals(integral) == p else p


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


def _is_rr_module(space) -> bool:
    if space is RR:
        return True
    try:
        return space in VectorSpaces(RR)
    except TypeError:
        return False


def _mapping_space_category(codomain):
    r"""Vector spaces when \(Y\) is an \(\mathbb R\)-module; the function algebra when \(Y=\mathbb R\)."""
    if codomain is RR:
        return VectorSpaces(RR) & CommutativeAlgebras(RR)
    if _is_rr_module(codomain):
        return VectorSpaces(RR)
    return Sets()


def _is_mapping_space(space) -> bool:
    try:
        return space is C(space.differentiability(), space.domain(), space.codomain())
    except (TypeError, AttributeError):
        return False


def _is_lebesgue_space(space) -> bool:
    try:
        return space is Lp(space.integrability_exponent())
    except (TypeError, AttributeError, ValueError):
        return False


def _is_sequence_space(space) -> bool:
    try:
        return space is ell(space.integrability_exponent(), space.codomain())
    except (TypeError, AttributeError, ValueError):
        return False


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
    return PairedModules(RR)(Pairings(left, right, RR)(_l2_pairing))


def _l2_pairing(left, right):
    r"""The pairing \(\int_{\mathbb R} fg\) on formulas in \(L^2(\mathbb R)\)."""
    formula = left.expression() * right.expression()
    return formula.integrate(left.parent().indeterminate(), -Infinity, Infinity)


@cached_function
def _sequence_pairing_module(left, right):
    r"""The pairing \(\sum a_n b_n\colon \ell^p\otimes\ell^{p'}\to\mathbb R\)."""
    if left is right:
        return left
    return PairedModules(RR)(Pairings(left, right, RR)(_ell2_pairing))


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
    r"""Coefficients of a univariate polynomial or truncated formal series, or none."""
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
    r"""Return an \(\mathrm{SR}\) formula for a recognized primitive, if any."""
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
    try:
        return RR(value).expression()
    except (TypeError, ValueError):
        return None


class _RealMap(ModuleElement):
    r"""A map \(X\to Y\), as an element of \(C^k(X,Y)\), \(L^p\), or \(\ell^p\)."""

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

    def compose(self, other):
        r"""Return \(f\circ g\), in \(C^{\min(k,\ell)}(W,Y)\)."""
        other = other if _is_mapping_space(element_parent(other)) else self.parent()(other)
        if other.parent().codomain() is not self.parent().domain():
            raise TypeError(
                f"cannot compose {self} after {other}: "
                f"codomain {other.parent().codomain()} is not domain {self.parent().domain()}"
            )
        k = min(self.parent().differentiability(), other.parent().differentiability())
        target = C(k, other.parent().domain(), self.parent().codomain())
        try:
            return target(
                self.expression().subs({self.parent().indeterminate(): other.expression()})
            )
        except (ValueError, TypeError):
            return target._placed(lambda point: self.evaluate_at(other.evaluate_at(point)))

    def derivative(self):
        r"""Return \(f'\), in \(C^{k-1}(X,Y)\) when \(k\) is finite."""
        k = self.parent().differentiability()
        if k == 0:
            raise ValueError(f"{self} is merely continuous; it has no C^k derivative")
        target = self.parent() if k is Infinity else C(k - 1, self.parent().domain(), self.parent().codomain())
        return target(self.expression().diff(self.parent().indeterminate()))

    def integral_from(self, lower):
        r"""Return \(x\mapsto\int_a^x f\), in \(C^{k+1}(\mathbb R,\mathbb R)\) when \(k\) is finite."""
        a = RR(lower)
        x = self.parent().indeterminate()
        antiderivative = self.expression().integral(x)
        k = self.parent().differentiability()
        target = (
            self.parent()
            if k is Infinity
            else C(k + 1, self.parent().domain(), self.parent().codomain())
        )
        return target(antiderivative - antiderivative.subs({x: a.expression()}))

    def taylor_series(self, centre):
        r"""The Taylor series of this map at ``centre``, as a formal power series in \(t = x - a\).

        For \(C^\infty(\mathbb R)\) this is the untruncated series
        \(\sum_{n\ge 0} f^{(n)}(a)\, t^n / n!\).  For finite regularity
        \(k\) it is the jet of order \(k\).
        """
        k = self.parent().differentiability()
        if self.parent().domain() is not RR or self.parent().codomain() is not RR:
            raise TypeError(
                f"Taylor series is defined for maps RR -> RR, not {self.parent()}"
            )
        formula = self.expression()
        x = self.parent().indeterminate()
        shifted = formula.subs({x: RR(centre).expression() + x})
        if k is Infinity:
            return LazyPowerSeriesRing(SR, "t").taylor(shifted)
        jet = shifted.taylor(x, ZZ.zero(), k)
        t = SR.var("t")
        return PowerSeriesRing(SR, "t")(jet.subs({x: t}))

    def maclaurin_series(self):
        r"""The Maclaurin series of this map: the Taylor series at \(0\)."""
        return self.taylor_series(ZZ.zero())

    def as_set_morphism(self):
        r"""This map as an element of \(\operatorname{Hom}_{\mathbf{Set}}(X,Y)\)."""
        return SetMorphism(self.parent().set_homset(), self.evaluate_at)

    def __call__(self, argument):
        argument_parent = element_parent(argument)
        if _is_mapping_space(argument_parent) and argument_parent.codomain() is self.parent().domain():
            return self.compose(argument)
        return self.evaluate_at(argument)

    def _add_(self, other):
        left_family = self._coefficient_family()
        right_family = other._coefficient_family()
        if left_family is not None and right_family is not None:
            family = dict(left_family)
            for index, coefficient in right_family.items():
                family[index] = family.get(index, 0) + coefficient
            return self.parent()._sequence_from_coefficients(family)
        try:
            return self.parent()(self.expression() + other.expression())
        except ValueError:
            return self.parent()._placed(
                lambda point: self.evaluate_at(point) + other.evaluate_at(point)
            )

    def _neg_(self):
        family = self._coefficient_family()
        if family is not None:
            return self.parent()._sequence_from_coefficients(
                {index: -coefficient for index, coefficient in family.items()}
            )
        try:
            return self.parent()(-self.expression())
        except ValueError:
            return self.parent()._placed(lambda point: -self.evaluate_at(point))

    def _lmul_(self, scalar):
        coefficient = RR(scalar)
        family = self._coefficient_family()
        if family is not None:
            return self.parent()._sequence_from_coefficients(
                {index: coefficient * value for index, value in family.items()}
            )
        try:
            return self.parent()(coefficient.expression() * self.expression())
        except ValueError:
            return self.parent()._placed(lambda point: coefficient * self.evaluate_at(point))

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
        try:
            return self.parent()(self.expression() * other.expression())
        except ValueError:
            return self.parent()._placed(
                lambda point: self.evaluate_at(point) * other.evaluate_at(point)
            )

    def _div_(self, other):
        try:
            return self.parent()(self.expression() / other.expression())
        except ValueError:
            return self.parent()._placed(
                lambda point: self.evaluate_at(point) / other.evaluate_at(point)
            )

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
        return "placed map"

    def _latex_(self) -> str:
        if self._expression is not None:
            return str(latex(self._expression))
        if self._coefficients is not None:
            return str(latex(self.generating_series()))
        return r"\text{placed map}"


class _FunctionSpace(UniqueRepresentation, Parent):
    r"""Shared construction for mapping spaces, \(L^p\), and \(\ell^p\)."""

    Element = _RealMap

    def __init__(self, domain, codomain, category, indeterminate=None) -> None:
        self._map_domain = domain
        self._map_codomain = codomain
        self._indeterminate = SR.var("x") if indeterminate is None else SR(indeterminate)
        Parent.__init__(self, base=RR, category=category)

    def __call__(self, value):
        r"""Construct a represented function without Sage coercion discovery."""
        return self._element_constructor_(value)

    def domain(self):
        return self._map_domain

    def codomain(self):
        return self._map_codomain

    def indeterminate(self):
        return self._indeterminate

    def set_homset(self):
        r"""\(\operatorname{Hom}_{\mathbf{Set}}(X,Y)\)."""
        return OwnedSets().hom(self.domain(), self.codomain())

    def zero(self):
        return self._element_constructor_(ZZ.zero())

    def one(self):
        return self._element_constructor_(ZZ.one())

    def _an_element_(self):
        return self.zero()

    def _placed(self, evaluate):
        return self.element_class(self, evaluate=evaluate)

    def _map_from_expression(self, expression):
        formula = _univariate_expression(expression, self._indeterminate)
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
        def evaluate(point, source=value):
            return source.evaluate_at(point)

        coefficients = value._coefficient_family()
        if coefficients is not None:
            return self._sequence_from_coefficients(coefficients)
        try:
            expression = value.expression()
        except ValueError:
            return self.element_class(self, evaluate=evaluate)
        return self._map_from_expression(expression)

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
        value_parent = element_parent(value)
        if value_parent is self:
            return value
        if (
            _is_mapping_space(value_parent)
            or _is_lebesgue_space(value_parent)
            or _is_sequence_space(value_parent)
        ):
            if value_parent.domain() is self.domain() and value_parent.codomain() is self.codomain():
                return self._reparent(value)
        if self.domain() is NN:
            if isinstance(value, LazyPowerSeries):
                return self._sequence_from_lazy_series(value)
            family = _univariate_coefficient_family(value)
            if family is not None:
                return self._sequence_from_coefficients(family)
        if self.codomain() is RR:
            formula = _expression_from_value(value, self._indeterminate)
            if formula is not None:
                return self._map_from_expression(formula)
        if _is_placed_callable(value):
            return self._map_from_callable(value)
        raise TypeError(f"{value!r} does not name a map {self.domain()} -> {self.codomain()}")


class _C(_FunctionSpace):
    r"""The mapping space \(C^k(X,Y)\subset\operatorname{Hom}_{\mathbf{Set}}(X,Y)\)."""

    @staticmethod
    def __classcall__(cls, k, domain, codomain=None):
        if codomain is None:
            codomain = domain
        return UniqueRepresentation.__classcall__(cls, _regularity(k), domain, codomain)

    def __init__(self, k, domain, codomain) -> None:
        self._regularity = k
        if codomain is RR:
            self._preamble_algebra_base_ring = RR
        _FunctionSpace.__init__(self, domain, codomain, _mapping_space_category(codomain))

    def differentiability(self):
        return self._regularity

    def cardinality(self):
        r"""The set of \(C^k\) maps \(X\to Y\) is infinite for \(Y=\mathbb R\)."""
        return Infinity

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
        if source is RR or source is ZZ or source is QQ:
            return True
        if not _is_mapping_space(source):
            return None
        if source.domain() is not self.domain() or source.codomain() is not self.codomain():
            return None
        if source.differentiability() >= self.differentiability():
            return True
        return None

    def __contains__(self, value) -> bool:
        value_parent = element_parent(value)
        if value_parent is self:
            return True
        if not _is_mapping_space(value_parent):
            return False
        return (
            value_parent.domain() is self.domain()
            and value_parent.codomain() is self.codomain()
            and value_parent.differentiability() >= self.differentiability()
        )

    def _repr_(self) -> str:
        k = _parameter_name(self._regularity)
        source = _space_name(self.domain())
        if self.domain() is self.codomain():
            return f"C({k}, {source})"
        return f"C({k}, {source}, {_space_name(self.codomain())})"

    def _latex_(self) -> str:
        k = _parameter_latex(self._regularity)
        source = _space_latex(self.domain())
        if self.domain() is self.codomain():
            return rf"C^{{{k}}}({source})"
        return rf"C^{{{k}}}({source}, {_space_latex(self.codomain())})"


class _CToThe(UniqueRepresentation, SageObject):
    r"""The family \(C^k\), for a fixed regularity \(k\)."""

    @staticmethod
    def __classcall__(cls, k):
        return UniqueRepresentation.__classcall__(cls, _regularity(k))

    def __init__(self, k) -> None:
        self._regularity = k

    def __call__(self, domain, codomain=None):
        return C(self._regularity, domain, codomain)

    def _repr_(self) -> str:
        return f"C^{_parameter_name(self._regularity)}"

    def _latex_(self) -> str:
        return rf"C^{{{_parameter_latex(self._regularity)}}}"


class _ContinuousMaps(SageObject):
    r"""The constructor \(C\).  \(C^k(X,Y)\) is the mapping space of class \(k\).

    ``C(k, X, Y)`` and ``C^k(X, Y)`` are the same space.  ``C(k, X)`` and
    ``C^k(X)`` are \(C^k(X,X)\).

    EXAMPLES::

        sage: from dzack_research.preamble.all import Algebras, C, RR, VectorSpaces, exp
        sage: (C^Infinity)(RR) is C(Infinity, RR, RR)
        True
        sage: (C^2)(RR, RR) is C(2, RR)
        True
        sage: (C^Infinity)(RR)
        C(Infinity, RR)
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
        return _C(k, domain, codomain)

    def __pow__(self, k):
        return _CToThe(k)

    __xor__ = __pow__

    def _repr_(self) -> str:
        return "C"

    def _latex_(self) -> str:
        return "C"


C = _ContinuousMaps()


class Lp(_FunctionSpace):
    r"""The \(\mathbb R\)-module \(L^p(\mathbb R)\), represented by functions.

    \(L^2(\mathbb R)\) is a module with the symmetric bilinear form
    \(b(f,g)=\int_{\mathbb R}fg\).  A general \(L^p\) is not: Hölder pairs it
    with \(L^{p'}\) as \(L^p * L^{p'}\).

    EXAMPLES::

        sage: from dzack_research.preamble.all import (
        ....:     C, FormModules, FormedModules, Lp, PairedModules, RR,
        ....:     SymmetricBilinearFormModules, VectorSpaces, exp,
        ....: )
        sage: L = Lp(2)
        sage: L
        L^2(RR)
        sage: L in VectorSpaces(RR)
        True
        sage: L in SymmetricBilinearFormModules(RR)
        True
        sage: L in FormedModules(RR)
        True
        sage: L in PairedModules(RR)
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
        sage: Lp(1) * Lp(Infinity) in FormedModules(RR)
        False
    """

    @staticmethod
    def __classcall__(cls, p):
        return UniqueRepresentation.__classcall__(cls, _integrability(p))

    def __init__(self, p) -> None:
        self._exponent = p
        category = VectorSpaces(RR)
        if p == 2:
            category = (
                category & SymmetricBilinearFormModules(RR) & FormedModules(RR)
            )
        _FunctionSpace.__init__(self, RR, RR, category)
        if p == 2:
            self._form = BilinearForms(self, RR)(_l2_pairing)
            self._pairing = self._form

    def integrability_exponent(self):
        return self._exponent

    def conjugate_lebesgue_space(self):
        r"""The space \(L^{p'}\) with \(1/p+1/p'=1\)."""
        return Lp(_conjugate_exponent(self.integrability_exponent()))

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

    def differentiability(self):
        r"""Lebesgue classes are not a \(C^k\) mapping space."""
        raise TypeError(f"{self} is not a C^k mapping space")

    def _repr_(self) -> str:
        return f"L^{_parameter_name(self._exponent)}(RR)"

    def _latex_(self) -> str:
        return rf"L^{{{_parameter_latex(self._exponent)}}}(\mathbb{{R}})"


class _ell(_FunctionSpace):
    r"""The \(\mathbb R\)-module \(\ell^p(\mathbb R)\) of sequences \(\mathbb N\to\mathbb R\)."""

    @staticmethod
    def __classcall__(cls, p, values=None):
        if values is None:
            values = RR
        if values is not RR:
            raise TypeError(f"ell^p is sequences of reals, not of {values}")
        return UniqueRepresentation.__classcall__(cls, _integrability(p), values)

    def __init__(self, p, values) -> None:
        self._exponent = p
        category = VectorSpaces(RR)
        if p == 2:
            category = (
                category & SymmetricBilinearFormModules(RR) & FormedModules(RR)
            )
        _FunctionSpace.__init__(self, NN, values, category, indeterminate=SR.var("n"))
        if p == 2:
            self._form = BilinearForms(self, RR)(_ell2_pairing)
            self._pairing = self._form

    def integrability_exponent(self):
        return self._exponent

    def conjugate_sequence_space(self):
        r"""The space \(\ell^{p'}\) with \(1/p+1/p'=1\)."""
        return ell(_conjugate_exponent(self.integrability_exponent()), self.codomain())

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

    def differentiability(self):
        r"""Sequence spaces are not a \(C^k\) mapping space."""
        raise TypeError(f"{self} is not a C^k mapping space")

    def _repr_(self) -> str:
        return f"ell^{_parameter_name(self._exponent)}(RR)"

    def _latex_(self) -> str:
        return rf"\ell^{{{_parameter_latex(self._exponent)}}}(\mathbb{{R}})"


class _EllToThe(UniqueRepresentation, SageObject):
    r"""The family \(\ell^p\), for a fixed exponent \(p\)."""

    @staticmethod
    def __classcall__(cls, p):
        return UniqueRepresentation.__classcall__(cls, _integrability(p))

    def __init__(self, p) -> None:
        self._exponent = p

    def __call__(self, values=None):
        return ell(self._exponent, values)

    def _repr_(self) -> str:
        return f"ell^{_parameter_name(self._exponent)}"

    def _latex_(self) -> str:
        return rf"\ell^{{{_parameter_latex(self._exponent)}}}"


class _SequenceSpaces(SageObject):
    r"""The constructor \(\ell\).  \(\ell^p(\mathbb R)\) is \(p\)-summable real sequences.

    ``ell(p)``, ``ell(p, RR)``, and ``ell^p(RR)`` are the same space.

    EXAMPLES::

        sage: from dzack_research.preamble.all import (
        ....:     FormedModules, PairedModules, QQ, RR, VectorSpaces, ell,
        ....: )
        sage: from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
        sage: ell(2) is ell(2, RR)
        True
        sage: ell(2) in VectorSpaces(RR)
        True
        sage: ell(2) in FormedModules(RR)
        True
        sage: ell(1) in FormedModules(RR)
        False
        sage: n = ell(2).indeterminate()
        sage: geometric = ell(2)(2 ** (-n))
        sage: geometric(3)
        1/8
        sage: ell(2).b(geometric, geometric)
        4/3
        sage: t = PolynomialRing(QQ, "t").gen()
        sage: truncated = ell(2)(1 + t + t**2)
        sage: truncated(3)
        0
        sage: ell(2).b(truncated, truncated)
        3
        sage: ell(2) * ell(2) is ell(2)
        True
        sage: ell(1) * ell(Infinity) in PairedModules(RR)
        True
        sage: ell(1) * ell(Infinity) in FormedModules(RR)
        False
    """

    def __call__(self, p, values=None):
        return _ell(p, values)

    def __pow__(self, p):
        return _EllToThe(p)

    __xor__ = __pow__

    def _repr_(self) -> str:
        return "ell"

    def _latex_(self) -> str:
        return r"\ell"


ell = _SequenceSpaces()
