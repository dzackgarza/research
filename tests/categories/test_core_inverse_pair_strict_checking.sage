r"""The identity cannot invert a constant map on two distinct points.

Conversely, the transposition is its own inverse. These two equations
separate unchecked inverse-pair data from the session's strict validator.
"""

import pytest

from dzack_research.preamble.all import *


def test_the_global_strict_flag_controls_inverse_pair_validation():
    points = Sets.Δ[1]
    maps = Sets().Mor(points, points)
    core = Sets().Core().Mor(points, points)
    constant = maps(lambda _point: points(0))
    identity = maps.identity()
    swap = maps(lambda point: points(1 - int(point)))
    previous = strict_checking()
    try:
        strict_checking(False)
        declared = core(constant, identity)
        assert declared.forward() is constant
        with pytest.raises(ValueError):
            declared.validate_inverse_pair()

        strict_checking(True)
        with pytest.raises(ValueError):
            core(constant, identity)
        transposition = core(swap, swap)
        assert transposition.inverse() * transposition == core.identity()
    finally:
        strict_checking(previous)
