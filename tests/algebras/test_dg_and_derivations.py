from dzack_research.preamble.all import QQ


def test_de_rham_differential_is_a_degree_one_graded_derivation() -> None:
    algebra = QQ.free_module(("x", "y")).symmetric_algebra()
    dga = algebra.de_rham_algebra()
    differential = dga.differential()

    x, y = algebra.algebra_generators()
    assert differential.degree_shift() == 1
    assert differential(x * y) == differential(x) * y + x * differential(y)
    assert differential(differential(x)) == dga.zero()


