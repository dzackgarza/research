r"""Archive reconciliation for function-valued modules with no finite framing."""

import pytest
from sage.all import RR, SR, exp, sin, var

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
