from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .types import Lattice


def test_the_rational_curve_semifan_needs_a_stable_limit_over_a_cone():
    """method: stable_limit_over_cone

    Semifan-workflow contract (research#679; the page's @rmk:missing-stable-limit).

    At a 0-cusp of ``F_{2d}``, given the boundary lattice, a cone of the Coxeter fan
    (equivalently a monodromy invariant in its relative interior) and the rational-curve
    divisor, the interface returns the combinatorial type of the KSBA stable limit of
    ``(X, eps R_rc)``: the dual graph of the central fibre with the genera of its
    components, the multiplicities with which the limit divisor meets them, and the
    contraction that defines the stable model.  That value is the stratum function of
    AE23 Thm. 9.3 (printed p. 30).

    The obligation is not academic: the census record
    ``computations/reports/coble_679-cusp-census-run.txt`` names the 14 classes of cusps
    with ``p_* > 1`` and ``k in {1,2}`` at which no printed restriction theorem applies,
    and every statement about them is conditional on this operation.
    """
    assert hasattr(Lattice, "stable_limit_over_cone"), (
        "the operation @rmk:missing-stable-limit records is absent: no module of the "
        "library computes the stable limit of a pair over a cone, which is what the "
        "survivor classes of the rational-curve semifan wait on"
    )
