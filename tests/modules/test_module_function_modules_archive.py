r"""Archive reconciliation for function-valued modules with no finite framing."""

import pytest
from sage.all import RR, SR, cosh, exp, sech, sin, tanh, var

from dzack_research.preamble.categories.modules.pure.function_modules import (
    FunctionModules,
    _MEMBER,
    _NOT_MEMBER,
    _square_integrability,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_function_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/pure/function_modules.py",
    "disposition": "reconciled-live-owner",
}




def _square_integrable_functions():
    return FunctionModules(RR).square_integrable()




def test_l2_membership_distinguishes_theorem_proofs_from_refutations() -> None:
    x = var("x")
    l2 = _square_integrable_functions()

    assert l2(exp(-x**2))(0) == 1
    assert l2(x / (1 + x**2))(1) == SR(1) / 2
    assert _square_integrability(exp(-x**2), x) == _MEMBER
    assert _square_integrability(x**2, x) == _NOT_MEMBER
    with pytest.raises(AssertionError):
        l2(x**2)
    with pytest.raises(AssertionError):
        l2(sin(x))




def test_callable_bilinear_form_on_l2_needs_no_gram_matrix() -> None:
    t = var("t")
    l2 = _square_integrable_functions()
    form = l2.bilinear_forms(RR)(lambda f, g: (f(t) * g(t)).integrate(t, -1, 1))
    x = l2(lambda point: point)
    x2 = l2(lambda point: point**2)

    assert abs(form(x, x) - RR(2) / 3) < 1e-9
    assert abs(form(x, x2)) < 1e-9
    with pytest.raises(AssertionError, match="no finite generating set"):
        form.gram_matrix()


def test_l2_rational_function_membership_has_the_exact_degree_and_pole_boundary() -> None:
    x = var("x")
    l2 = _square_integrable_functions()

    assert l2(1 / (1 + x**2))(0) == 1
    assert l2(x / (1 + x**2))(1) == SR(1) / 2
    with pytest.raises(AssertionError):
        l2(1 / x)
    with pytest.raises(AssertionError):
        l2(x**2 / (1 + x**2))


def test_l2_bounded_multiple_and_vanishing_tail_criteria_retain_their_verdicts() -> None:
    x = var("x")
    l2 = _square_integrable_functions()

    assert l2(sin(x) / (1 + x**2))(0) == 0
    assert _square_integrability(sech(x**2), x) == _MEMBER
    assert _square_integrability(exp(-cosh(x)), x) == _MEMBER
    assert _square_integrability(tanh(x), x) == _NOT_MEMBER


def test_l2_integral_fallback_certifies_integrable_and_divergent_exponentials() -> None:
    x = var("x")
    l2 = _square_integrable_functions()

    assert l2(exp(-abs(x)))(0) == 1
    with pytest.raises(AssertionError):
        l2(exp(-x))








def test_l2_certifies_zero_and_polynomial_multiples_of_a_gaussian() -> None:
    x = var("x")
    l2 = _square_integrable_functions()

    zero = l2(SR(0))
    weighted_gaussian = l2(x * exp(-x**2))

    assert zero(7) == 0
    assert weighted_gaussian(2) == 2 * exp(-4)
    assert _square_integrability(x * exp(-x**2), x) == _MEMBER


