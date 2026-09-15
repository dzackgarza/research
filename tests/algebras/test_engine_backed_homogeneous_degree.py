import pytest

from dzack_research.preamble.all import QQ


def test_engine_backed_polynomial_degree_survives_unrepresented_module_coordinates() -> None:
    ring = QQ.polynomial_ring(("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")

    assert ring.homogeneous_degree(x - y) == 1
    assert ring.homogeneous_degree(x * y) == 2

    with pytest.raises(ValueError, match="not homogeneous"):
        ring.homogeneous_degree(x + y**2)
