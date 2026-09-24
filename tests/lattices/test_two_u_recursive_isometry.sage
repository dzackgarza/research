from dzack_research.preamble.all import *


def test_isometric_complements_give_isometric_eichler_models_fixing_the_hyperbolic_basis() -> None:
    r"""An isometry \(K \to K'\) extends by the identity on \(2U\) to
    \(2U \oplus K \to 2U \oplus K'\); here \(K = A_2\) and \(K'\) is \(A_2\) given by
    its Gram matrix."""
    source = Lattices(ZZ)("A2").two_u_eichler_model()
    target = Lattices(ZZ)([[-2, 1], [1, -2]]).two_u_eichler_model()

    assert source.is_isometric_to(target)
    witness = source.isometry_to(target)
    for left, right in zip(source.hyperbolic_basis(), target.hyperbolic_basis(), strict=True):
        assert witness(left) == right


def test_2U_plus_A2_is_not_isometric_to_2U_plus_2A1() -> None:
    r"""The determinants differ: \(\det(2U \oplus A_2) = 3\) while
    \(\det(2U \oplus A_1^2) = 4\)."""
    source = Lattices(ZZ)("A2").two_u_eichler_model()
    target = (Lattices(ZZ)("A1") + Lattices(ZZ)("A1")).two_u_eichler_model()

    assert not source.is_isometric_to(target)
    assert source.isometry_to(target) is None
