r"""The Young-admissible family of convolution pairings on Lebesgue classes.

For p,q,r>=1 and 1/p+1/q=1+1/r, Young gives Lp tensor Lq -> Lr.
For finite r the proof is Holder on
 (|f|^p |g|^q)^(1/r) |f|^(1-p/r) |g|^(1-q/r), followed by Tonelli;
raising to r and integrating gives ||f*g||_r^r <= ||f||_p^r ||g||_q^r.
The conjugate (r=infinity) case is Holder directly, and p=q=r=1 is
Tonelli. Null changes do not affect convolution (Mathlib Analysis/Convolution,
convolution_congr). Thus these are well-defined bilinear maps on the quotients.
They are not one total product on the sum of every Lp.
"""

from sage.misc.cachefunc import cached_function
from sage.misc.unknown import Unknown
from sage.rings.infinity import Infinity
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.algebras.algebras import Algebras, _algebra_on_module
from dzack_research.preamble.categories.functions.real_functions import Lp
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.rings.real import RR
from dzack_research.preamble.rings.unit_interval import UnitInterval


def _holder_degree(space):
    exponent = space.integrability_exponent()
    return UnitInterval.zero() if exponent is Infinity else UnitInterval(RR.one() / RR(exponent))


def _space_at_degree(degree):
    value = degree.as_extended_real()
    exponent = Infinity if (value == RR.zero()) is True else RR.one() / value
    return Lp(exponent).quotient_by_null_functions()


@cached_function(key=lambda left, right: (id(left), id(right)))
def _symbolic_convolution(left, right):
    r"""Private SymPy integral of the existing representative formulas.

    Uses integrate over the full real line, not quadrature or finite samples.
    A remaining Integral is retained as an unevaluated exact expression.
    Opaque callable representatives keep their integral definition but have
    no symbolic evaluator in this adapter.
    """
    import sympy

    f, g = left._formula(), right._formula()
    if f is None or g is None:
        return None
    x = sympy.Symbol("x", real=True)
    t = sympy.Dummy("t", real=True)
    f = f._sympy_().subs(left.parent().indeterminate()._sympy_(), t)
    g = g._sympy_().subs(right.parent().indeterminate()._sympy_(), x - t)
    integrand = sympy.piecewise_fold((f * g).rewrite(sympy.Piecewise))
    try:
        expression = sympy.integrate(integrand, (t, -sympy.oo, sympy.oo))
    except (NotImplementedError, ValueError):
        expression = sympy.Integral(integrand, (t, -sympy.oo, sympy.oo))
    return expression, x


def _convolution_representative(space, left, right):
    r"""The integral representative, zero at exceptional nonintegrable points.

    Young's hypotheses guarantee those exceptions form a null set. This
    convention never supplies a product for an inadmissible exponent pair.
    The symbolic adapter may leave exact evaluations undecided; that is not
    evidence of divergence and must not be turned into zero.
    """
    import sympy
    from sympy.calculus.util import continuous_domain

    symbolic = _symbolic_convolution(left, right)
    formula = None
    if symbolic is not None:
        expression, variable = symbolic
        assert expression not in (sympy.oo, -sympy.oo, sympy.zoo, sympy.nan), (
            "the supplied representatives violate their stated Young integrability hypotheses"
        )
        try:
            if not expression.has(sympy.Integral) and continuous_domain(expression, variable, sympy.S.Reals) == sympy.S.Reals:
                formula = SR(expression).subs({SR(str(variable)): space.indeterminate()})
        except (NotImplementedError, TypeError, ValueError):
            formula = None

    def evaluate(point):
        assert symbolic is not None, "this integral evaluator requires formulas for the two supplied measurable maps"
        expression, variable = symbolic
        value = expression.subs(variable, RR(point).expression()._sympy_()).doit()
        if value in (sympy.oo, -sympy.oo, sympy.zoo, sympy.nan):
            return RR.zero()
        assert not value.has(sympy.Integral), "the exact convolution integral is not evaluated by the selected symbolic engine"
        return RR._from_engine_expression(SR(value))

    return space.element_class(space, evaluate=evaluate, expression=formula)


@cached_function(key=lambda left, right: (id(left), id(right)))
def _convolution_pairing(left, right):
    r"""The linear classifier Lp tensor_R Lq -> Lr on a Young-admissible pair."""
    s, t = _holder_degree(left), _holder_degree(right)
    pair = UnitInterval.degree_pairs()(lambda index: s if int(index) == 0 else t)
    degree = UnitInterval.young_degree_map()(pair)
    target = _space_at_degree(degree)
    tensor = Modules(RR).tensor_product((left, right))

    def product(f, g):
        f, g = left(f), right(g)
        return target(_convolution_representative(target.map_space(), f.representative(), g.representative()))

    return tensor.from_bilinear_map(target, product)


@cached_function
def _convolution_pairing_family():
    return indexed_family(UnitInterval.young_pairs(), lambda pair:
        _convolution_pairing(_space_at_degree(pair.component(0)), _space_at_degree(pair.component(1))))


@cached_function
def _convolution_algebra():
    r"""The total L1 convolution algebra, within the full Young family.

    Fubini gives associativity and integral(f*g)=integral(f)integral(g).
    Substitution gives commutativity. The family for other exponents remains
    separately available; L-infinity is not silently included in this algebra.
    """
    module = Lp(1).quotient_by_null_functions()
    multiplication = module.convolution_pairing(module)
    return _algebra_on_module(module, multiplication,
        placement=(Algebras(RR).Associative(), Algebras(RR).Commutative()))
