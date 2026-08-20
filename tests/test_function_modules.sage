r"""Modules whose elements are functions, and a form given by an integral.

$C^\infty(\RR)$ and $L^2(\RR)$ have no finite generating set, no coordinates
and no Gram matrix.  What they do have is the module structure and, for
$L^2$, a bilinear form $\langle f,g\rangle=\int fg$.  So they exercise the
parts of the preamble that are about being a module rather than about being a
finitely generated one, and a construction that quietly assumed coordinates
fails here rather than years later.

Membership is decided where a theorem decides it: a proposed element that is
a symbolic expression is certified, refused, or admitted on trust, and the
tests below assert which of the three a specimen gets.  The bilinearity of
the pairing is still not checked, and is not decidable here.  The rest of the
mathematics asserted below is the module axioms on specimens, and the values
of an integral computed two ways.
"""


# Sage's namespace first, and the preamble's over it: these tests name
# ``MatrixSpace``, ``RR`` and their fellows, which the preamble does not
# export and a lowered module is not given.
from sage.all import *  # noqa: F401,F403

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

    from sage.symbolic.expression import Expression

    from dzack_research.preamble.categories.modules.pure.function_modules import (
        FunctionModule,
        FunctionModuleElement,
    )


def _ensure_preamble() -> None:
    if "Lattices" in globals():
        return
    from dzack_research.preamble.install import install_preamble

    install_preamble(globals())
    Lattices.install(globals())


def _smooth() -> "FunctionModule":
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.pure.function_modules import smooth_functions

    return smooth_functions(RR)


def _square_integrable() -> "FunctionModule":
    _ensure_preamble()
    from dzack_research.preamble.categories.modules.pure.function_modules import (
        square_integrable_functions,
    )

    return square_integrable_functions(RR)


def _integral_pairing() -> "Callable[[FunctionModuleElement, FunctionModuleElement], Expression]":
    r"""Return $\langle f,g\rangle=\int_{-1}^{1}fg$, on the symbolic variable."""
    t = var("t")
    return lambda f, g: (f(t) * g(t)).integrate(t, -1, 1)


def test_functions_form_a_module_over_the_reals() -> None:
    r"""Addition is pointwise and scaling is pointwise, on functions."""
    C = _smooth()
    f = C(lambda x: x**2)
    g = C(lambda x: x)

    assert (f + g)(3) == 12, "(x^2 + x)(3) = 12"
    assert (2 * f)(3) == 18, "(2x^2)(3) = 18"
    assert (f - f)(3) == 0
    assert (f + C.zero())(3) == f(3)


def test_the_module_action_needs_no_generating_set() -> None:
    r"""$\rho(r)$ is scaling, read off nothing.

    The obligation is about being a module, and this module has no generators
    to read an action off -- so it supplies one directly, which is what a
    module that is not finitely generated has to be able to do.
    """
    C = _smooth()
    f = C(lambda x: x**2)

    action = C._ring_morphism_defining_module_action()

    assert action(RR(2))(f)(3) == 18
    assert action(RR(1))(f)(3) == f(3), "the identity scalar acts as the identity"
    assert action(RR(0))(f)(3) == 0


def test_a_form_can_be_given_by_its_pairing_rather_than_a_matrix() -> None:
    r"""$\langle f,g\rangle=\int_{-1}^1 fg$ is a form on a module with no basis.

    A Gram matrix is how a finitely generated form is written down.  $L^2$ has
    no finite generating family to run over, so the form is stated as the
    pairing it is.
    """
    from dzack_research.preamble.categories.forms.forms import BilinearForms

    L2 = _square_integrable()
    form = BilinearForms(L2, RR)(_integral_pairing())
    x = L2(lambda t: t)
    x_squared = L2(lambda t: t**2)

    assert abs(form(x, x) - RR(2) / 3) < 1e-9, "int_{-1}^{1} t^2 = 2/3"
    assert abs(form(x, x_squared)) < 1e-9, "int_{-1}^{1} t^3 = 0, by parity"
    assert abs(form(x_squared, x_squared) - RR(2) / 5) < 1e-9, "int_{-1}^{1} t^4 = 2/5"


def test_that_form_is_symmetric_and_bilinear_on_specimens() -> None:
    r"""Bilinearity cannot be checked in general, so it is checked on cases.

    The pairing is trusted -- nothing here can decide bilinearity of an
    arbitrary callable -- but a form that failed it on these specimens would
    not be one, and the integral is the reason it holds.
    """
    from dzack_research.preamble.categories.forms.forms import BilinearForms

    L2 = _square_integrable()
    form = BilinearForms(L2, RR)(_integral_pairing())
    x = L2(lambda t: t)
    x_squared = L2(lambda t: t**2)

    assert abs(form(x, x_squared) - form(x_squared, x)) < 1e-9, "symmetric"
    assert abs(form(2 * x, x_squared) - 2 * form(x, x_squared)) < 1e-9, "linear in the first slot"
    assert abs(
        form(x + x_squared, x) - form(x, x) - form(x_squared, x)
    ) < 1e-9, "additive in the first slot"


def test_a_polynomial_is_refused_by_square_integrable_functions_on_the_line() -> None:
    r"""$\int_\RR p^2$ diverges for $p\neq 0$, so $p\notin L^2(\RR)$.

    A refusal, not a warning: the leading term of a nonzero polynomial
    dominates, so the integral of its square over the whole line is infinite.
    That is a theorem about the proposed element, and the module states it.
    A nonconstant sine is refused for the other reason -- it is periodic and
    not identically zero, so each period contributes the same positive amount.
    """
    import pytest

    x = var("x")
    L2 = _square_integrable()

    with pytest.raises(AssertionError):
        L2(x**2)
    with pytest.raises(AssertionError):
        L2(SR(1))
    with pytest.raises(AssertionError):
        L2(sin(x))


def test_a_gaussian_and_its_polynomial_multiples_are_certified_for_l2() -> None:
    r"""$p(x)e^{-ax^2+bx+c}$ with $a>0$ is Schwartz, hence in $L^2(\RR)$.

    The zero polynomial is the one polynomial that is square-integrable, so
    the refusal above must not reach it.
    """
    x = var("x")
    L2 = _square_integrable()

    assert L2(exp(-x**2))(0) == 1
    assert L2(x * exp(-x**2))(2) == 2 * exp(-4)
    assert L2(SR(0))(7) == 0, "the zero function is square-integrable"


def test_an_elementary_expression_is_certified_smooth() -> None:
    r"""Sums, products, powers and compositions of polynomials, $\exp$, $\sin$
    and $\cos$ are $C^\infty$, so $\sin(x)e^x+x^3$ is admitted on a theorem.
    """
    x = var("x")
    C = _smooth()

    assert C(sin(x) * exp(x) + x**3).parent() is C


def test_rational_functions_are_decided_completely_by_the_p_test() -> None:
    r"""$p/q\in L^2(\RR)$ exactly when $q$ has no real root and $\deg q\ge\deg p+1$.

    Both halves of the theorem are asserted, and the degree condition is
    asserted at its boundary: $x/(1+x^2)$ decays like $1/x$, whose square is
    the convergent $1/x^2$, so a gap of exactly one is enough, while
    $x^2/(1+x^2)$ tends to $1$ and cannot be.
    """
    import pytest

    x = var("x")
    L2 = _square_integrable()

    assert L2(1/(1+x**2))(0) == 1
    assert L2(x/(1+x**2))(1) == 1/2, "a degree gap of one is enough"

    with pytest.raises(AssertionError):
        L2(1/x)  # a pole at the origin
    with pytest.raises(AssertionError):
        L2(x**2/(1+x**2))  # no decay at all


def test_a_linear_combination_of_members_is_a_member() -> None:
    r"""$L^2$ is a vector space, so Minkowski decides a sum from its summands.

    Neither summand is decided by the same tier as the other -- the Gaussian
    by decay, the rational one by the $p$-test -- and the sum needs no tier of
    its own beyond the inequality.
    """
    x = var("x")
    L2 = _square_integrable()

    assert L2(3*exp(-x**2) - 2/(1+x**2))(0) == 1


def test_a_bounded_multiple_of_a_member_is_a_member() -> None:
    r"""The comparison test: $|h|\le C$ and $g\in L^2$ give $(hg)^2\le C^2g^2$."""
    x = var("x")
    L2 = _square_integrable()

    assert L2(sin(x)/(1+x**2))(0) == 0


def test_the_integral_decides_what_the_structural_tiers_cannot() -> None:
    r"""$\int_\RR f^2$ is the last tier, and it answers both ways.

    None of the structural tiers recognizes $e^{-|x|}$ or $e^{-x}$: neither is
    rational, periodic, Schwartz-shaped, a sum or a product.  Sage integrates
    the squares to $1$ and to $+\infty$ respectively, which is a certificate
    each way.
    """
    import pytest

    x = var("x")
    L2 = _square_integrable()

    assert L2(exp(-abs(x)))(0) == 1

    with pytest.raises(AssertionError):
        L2(exp(-x))


def test_a_vanishing_tail_certifies_what_the_integral_cannot_evaluate() -> None:
    r"""A continuous $f$ with $|x|f(x)\to0$ at both ends is in $L^2(\RR)$.

    Sage returns $\int\operatorname{sech}^2(x^2)$ and $\int e^{-2\cosh x}$
    unevaluated, so the integral tier declines both, while the limits are
    plainly zero and the $p$-test does the rest.  A tail that does not vanish
    settles nothing on its own, so $\tanh$ falls through to the integral,
    which diverges.

    This asserts the verdict rather than admission because certifying and
    trusting are both admission -- the module takes an undecided function on
    trust -- so the verdict is the only place the tier is observable.
    """
    from dzack_research.preamble.categories.modules.pure.function_modules import (
        _MEMBER,
        _NOT_MEMBER,
        _square_integrability,
    )

    x = var("x")

    assert _square_integrability(sech(x**2), x) == _MEMBER
    assert _square_integrability(exp(-cosh(x)), x) == _MEMBER
    assert _square_integrability(tanh(x), x) == _NOT_MEMBER


def test_module_arithmetic_stays_symbolic_and_needs_no_certificate() -> None:
    r"""A combination of members is a member because the module is a module.

    Nothing is re-decided: the sum goes around the certifier, which is what
    lets an element be built from an expression whose $\int f^2$ costs a call
    to the computer algebra system without paying for it again on every
    addition.  The combination is kept symbolically, so the result is still an
    expression that can be read rather than an opaque composition.
    """
    x = var("x")
    L2 = _square_integrable()
    gaussian = L2(exp(-x**2))
    lorentzian = L2(1/(1+x**2))

    assert (gaussian + lorentzian)(0) == 2
    assert (3 * gaussian - lorentzian)(0) == 2
    assert (gaussian - gaussian)(5) == 0
    assert (gaussian + L2.zero())(1) == exp(-1)


def test_an_opaque_callable_is_trusted_where_an_expression_is_refused() -> None:
    r"""The protocol is three-way, and the third way is honest trust.

    $x\mapsto x^2$ written as a Python function is the same function that is
    refused as a symbolic expression, and it is admitted -- nothing here can
    read a lambda, so $L^2$ takes it on trust and says so in the log.  What
    separates the two is the proof, not the function.
    """
    L2 = _square_integrable()

    assert L2(lambda point: point**2)(3) == 9


def test_such_a_form_has_no_gram_matrix_and_says_so() -> None:
    r"""Asking for coordinates of a module that has none is refused.

    Not an oversight to paper over: the entries of a Gram matrix are the
    pairings of a finite generating family, and there is no such family here.
    """
    import pytest

    from dzack_research.preamble.categories.forms.forms import BilinearForms

    L2 = _square_integrable()
    form = BilinearForms(L2, RR)(_integral_pairing())

    with pytest.raises(AssertionError, match="no finite generating set"):
        form.gram_matrix()


def test_a_finitely_generated_form_still_has_one() -> None:
    r"""The general case does not cost the finite one its Gram matrix."""
    assert Lattices.A2.form().gram_matrix() is not None
    assert Lattices.A2.gram_matrix().list() == [-2, 1, 1, -2]
