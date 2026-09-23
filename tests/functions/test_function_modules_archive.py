r"""Archive reconciliation for the function-module mathematics.

The historical ``smooth_functions`` and ``square_integrable_functions``
parents were replaced by the general mapping-space and Lebesgue-space owners.
These specimens retain the independent mathematical assertions from that
archive without reinstating its separate module hierarchy.
"""

import pytest
from sage.all import SR, exp, sin

from dzack_research.preamble.all import RR, Lp

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/pure/function_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/functions/real_functions.py",
    "disposition": "reconciled-live-owner",
}




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








def test_archived_integral_fallback_decides_two_nonstructural_symbolic_cases() -> None:
    space = Lp(2)
    x = SR.var("x")

    assert space(exp(-abs(x)))(0) == 1
    with pytest.raises(ValueError, match="not square-integrable"):
        space(exp(-x))






