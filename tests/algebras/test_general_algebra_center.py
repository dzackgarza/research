r"""The centre of an associative algebra is returned with its algebra structure."""

from dzack_research.preamble.all import Algebras, MatrixSpace, QQ


def test_matrix_center_is_a_commutative_associative_algebra_on_the_central_submodule() -> None:
    matrices = MatrixSpace(QQ, 2)
    center = matrices.center()
    module = center.underlying_module()
    inclusion = center._preamble_center_inclusion

    assert center in Algebras(QQ).Associative()
    assert center in Algebras(QQ).Commutative()
    assert inclusion.domain() is module
    identity = matrices.identity()
    central_identity = inclusion.lift(identity)
    assert center.product(central_identity, central_identity) == center(central_identity)
