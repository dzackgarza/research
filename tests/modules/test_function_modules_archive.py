r"""Archive reconciliation for function-valued modules with no finite framing."""

import pytest
from sage.all import RR, SR, cosh, exp, sech, sin, tanh, var

from dzack_research.preamble.categories.forms.forms import BilinearForms
from dzack_research.preamble.categories.modules.pure.function_modules import (
    _MEMBER,
    _NOT_MEMBER,
    _square_integrability,
    smooth_functions,
    square_integrable_functions,
)


def test_function_modules_use_pointwise_module_operations_without_generators() -> None:
    smooth = smooth_functions(RR)
    f = smooth(lambda x: x**2)
    g = smooth(lambda x: x)

    assert smooth.is_finitely_generated() is False
    assert (f + g)(3) == 12
    assert (2 * f)(3) == 18
    assert (f - f)(3) == 0
    assert smooth.scalar_action()(RR(2))(f)(3) == 18


def test_l2_membership_distinguishes_theorem_proofs_from_refutations() -> None:
    x = var("x")
    l2 = square_integrable_functions(RR)

    assert l2(exp(-x**2))(0) == 1
    assert l2(x / (1 + x**2))(1) == SR(1) / 2
    assert _square_integrability(exp(-x**2), x) == _MEMBER
    assert _square_integrability(x**2, x) == _NOT_MEMBER
    with pytest.raises(AssertionError):
        l2(x**2)
    with pytest.raises(AssertionError):
        l2(sin(x))


def test_l2_accepts_opaque_callable_but_module_arithmetic_needs_no_recertification() -> None:
    x = var("x")
    l2 = square_integrable_functions(RR)
    opaque = l2(lambda point: point**2)
    gaussian = l2(exp(-x**2))

    assert opaque(3) == 9
    assert (gaussian + gaussian)(0) == 2
    assert (3 * gaussian - gaussian)(1) == 2 * exp(-1)


def test_callable_bilinear_form_on_l2_needs_no_gram_matrix() -> None:
    t = var("t")
    l2 = square_integrable_functions(RR)
    form = BilinearForms(l2, RR)(lambda f, g: (f(t) * g(t)).integrate(t, -1, 1))
    x = l2(lambda point: point)
    x2 = l2(lambda point: point**2)

    assert abs(form(x, x) - RR(2) / 3) < 1e-9
    assert abs(form(x, x2)) < 1e-9
    with pytest.raises(AssertionError, match="no finite generating set"):
        form.gram_matrix()


def test_l2_rational_function_membership_has_the_exact_degree_and_pole_boundary() -> None:
    x = var("x")
    l2 = square_integrable_functions(RR)

    assert l2(1 / (1 + x**2))(0) == 1
    assert l2(x / (1 + x**2))(1) == SR(1) / 2
    with pytest.raises(AssertionError):
        l2(1 / x)
    with pytest.raises(AssertionError):
        l2(x**2 / (1 + x**2))


def test_l2_bounded_multiple_and_vanishing_tail_criteria_retain_their_verdicts() -> None:
    x = var("x")
    l2 = square_integrable_functions(RR)

    assert l2(sin(x) / (1 + x**2))(0) == 0
    assert _square_integrability(sech(x**2), x) == _MEMBER
    assert _square_integrability(exp(-cosh(x)), x) == _MEMBER
    assert _square_integrability(tanh(x), x) == _NOT_MEMBER


def test_l2_integral_fallback_certifies_integrable_and_divergent_exponentials() -> None:
    x = var("x")
    l2 = square_integrable_functions(RR)

    assert l2(exp(-abs(x)))(0) == 1
    with pytest.raises(AssertionError):
        l2(exp(-x))


def test_smooth_elementary_expression_is_certified_by_the_function_module() -> None:
    x = var("x")
    smooth = smooth_functions(RR)

    element = smooth(sin(x) * exp(x) + x**3)
    assert element.parent() is smooth


def test_l2_is_closed_under_sums_certified_by_different_membership_criteria() -> None:
    x = var("x")
    l2 = square_integrable_functions(RR)
    gaussian = l2(exp(-x**2))
    rational = l2(1 / (1 + x**2))

    combined = 3 * gaussian - 2 * rational
    assert combined.parent() is l2
    assert combined(0) == 1


def test_integral_pairing_is_symmetric_and_bilinear_on_archived_specimens() -> None:
    t = var("t")
    l2 = square_integrable_functions(RR)
    form = BilinearForms(l2, RR)(lambda f, g: (f(t) * g(t)).integrate(t, -1, 1))
    x = l2(lambda point: point)
    x2 = l2(lambda point: point**2)

    assert abs(form(x, x2) - form(x2, x)) < 1e-9
    assert abs(form(2 * x, x2) - 2 * form(x, x2)) < 1e-9
    assert abs(form(x + x2, x) - form(x, x) - form(x2, x)) < 1e-9


def test_l2_certifies_zero_and_polynomial_multiples_of_a_gaussian() -> None:
    x = var("x")
    l2 = square_integrable_functions(RR)

    zero = l2(SR(0))
    weighted_gaussian = l2(x * exp(-x**2))

    assert zero(7) == 0
    assert weighted_gaussian(2) == 2 * exp(-4)
    assert _square_integrability(x * exp(-x**2), x) == _MEMBER
