r"""Tensor and symmetric algebras on the torsion module Z/2 + Z/3."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_degree_two_of_the_tensor_and_symmetric_algebra_on_z2_plus_z3_has_order_six() -> None:
    r"""Mixed products vanish because Z/2 (x) Z/3 = 0, so T^2 = Sym^2 = Z/2 + Z/3.

    Derivation: (Z/m) (x) (Z/n) = Z/gcd(m, n); Sym^2(Z/m) = Z/m; Sym^2(A + B) =
    Sym^2 A + A (x) B + Sym^2 B.
    """
    module = Modules(ZZ).direct_sum_of_cyclics((2, 3))
    for algebra in (module.tensor_algebra(), module.symmetric_algebra()):
        a = algebra.algebra_generator(0)
        b = algebra.algebra_generator(1)
        assert a * b == algebra.zero()
        assert b * a == algebra.zero()
        assert a * a != algebra.zero()
        assert 2 * (a * a) == algebra.zero()
        assert b * b != algebra.zero()
        assert 3 * (b * b) == algebra.zero()
        assert algebra.graded_piece(2).cardinality() == 6
