r"""Archive reconciliation for the function-module mathematics.

The historical ``smooth_functions`` and ``square_integrable_functions``
parents were replaced by the general mapping-space and Lebesgue-space owners.
These specimens retain the independent mathematical assertions from that
archive without reinstating its separate module hierarchy.
"""

import pytest
from sage.all import SR, exp, sin
from sage.rings.infinity import Infinity

from dzack_research.preamble.all import RR, C, Lp

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/pure/function_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/functions/real_functions.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_function_modules_are_the_live_mapping_and_lebesgue_spaces() -> None:
    smooth = C(Infinity, RR)
    square_integrable = Lp(2)
    x = smooth.indeterminate()

    f = smooth(x**2)
    g = smooth(x)
    assert (f + g)(3) == 12
    assert (2 * f)(3) == 18

    gaussian = square_integrable(smooth(exp(-(x**2))))
    assert gaussian(0) == 1
    assert square_integrable.b(gaussian, gaussian) == square_integrable.q(gaussian)


def test_symbolic_l2_membership_retains_the_archived_exact_rational_boundary() -> None:
    space = Lp(2)
    x = SR.var("x")

    assert space(1 / (1 + x**2))(0) == 1
    assert space(x / (1 + x**2))(1) == RR(1) / 2

    with pytest.raises(ValueError, match="not square-integrable"):
        space(x**2)
    with pytest.raises(ValueError, match="not square-integrable"):
        space(1 / x)
    with pytest.raises(ValueError, match="not square-integrable"):
        space(x**2 / (1 + x**2))


def test_symbolic_l2_membership_retains_schwartz_sum_and_bounded_product_cases() -> None:
    space = Lp(2)
    x = SR.var("x")

    assert space(x * exp(-(x**2)))(2) == 2 * exp(-4)
    assert space(3 * exp(-(x**2)) - 2 / (1 + x**2))(0) == 1
    assert space(sin(x) / (1 + x**2))(0) == 0

    with pytest.raises(ValueError, match="not square-integrable"):
        space(sin(x))


def test_opaque_callable_remains_an_explicit_placement_claim() -> None:
    space = Lp(2)

    placed = space(lambda point: point**2)
    assert placed(3) == 9
    assert (placed + space.zero())(3) == 9


def test_archived_smooth_elementary_expression_is_owned_by_C_infinity() -> None:
    smooth = C(Infinity, RR)
    x = smooth.indeterminate()

    element = smooth(sin(x) * exp(x) + x**3)
    assert element.parent() is smooth


def test_archived_l2_form_is_the_live_integral_pairing_without_a_finite_framing() -> None:
    space = Lp(2)
    x = space.indeterminate()
    linear = space(x * exp(-(x**2)))
    quadratic = space((x**2) * exp(-(x**2)))

    assert space.b(linear, quadratic) == space.b(quadratic, linear)
    assert space.q(linear) == space.b(linear, linear)
    assert not hasattr(space, "module_generating_set")


def test_archived_integral_fallback_decides_two_nonstructural_symbolic_cases() -> None:
    space = Lp(2)
    x = SR.var("x")

    assert space(exp(-abs(x)))(0) == 1
    with pytest.raises(ValueError, match="not square-integrable"):
        space(exp(-x))


def test_archived_finite_formed_module_still_has_a_gram_matrix() -> None:
    from dzack_research.preamble.all import ZZ, Lattices

    root_lattice = Lattices(ZZ)("A2")
    gram = root_lattice.gram_matrix()
    assert tuple(
        gram[row, column]
        for row in range(2)
        for column in range(2)
    ) == (-2, 1, 1, -2)


def test_function_algebra_retains_root_multiplication_and_scalar_structure() -> None:
    smooth = C(Infinity, RR)
    x = smooth.coordinate()
    multiplication = smooth.multiplication()
    assert multiplication(smooth(2), x)(3) == 6
    assert smooth.algebra_structure_morphism()(RR(4))(2) == 4


def test_formed_function_engines_cross_to_their_original_vector_space() -> None:
    from dzack_research.preamble.all import ell

    for space in (Lp(2), ell(2)):
        zero = space.zero()
        module = space.unformed_module()
        assert module is not space
        assert module(zero)(0) == 0
        assert space(module(zero))(0) == 0
        assert space.b(zero, zero) == RR.zero()
