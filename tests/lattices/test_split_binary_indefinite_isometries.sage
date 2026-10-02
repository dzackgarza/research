from dzack_research.preamble.all import *
from pytest import raises
from sage.matrix.constructor import matrix as engine_matrix
from sage.rings.rational_field import QQ as SageQQ


def test_split_binary_indefinite_isometry_returns_an_actual_witness() -> None:
    source = Lattices(ZZ)([[0, 2], [2, 0]])
    target = Lattices(ZZ)([[0, 2], [2, 4]])

    assert source.discriminant() == target.discriminant()
    assert source.gram_matrix().determinant() < 0
    assert source.Isom(target).is_empty() is False

    isometry = source.Isom(target).an_element()
    assert isometry.domain() is source
    assert isometry.codomain() is target
    assert (~isometry) * isometry == source.Aut().one()
    for left in source.module_generators():
        for right in source.module_generators():
            assert target.b(isometry(left), isometry(right)) == source.b(left, right)


def test_split_binary_indefinite_nonequivalence_is_decided_exactly() -> None:
    source = Lattices(ZZ)([[0, 2], [2, 0]])
    target = Lattices(ZZ)([[2, 2], [2, 0]])

    assert source.discriminant() == target.discriminant()
    assert source.Isom(target).is_empty() is True


def test_private_matrix_lift_rejects_an_invertible_nonisometry() -> None:
    lattice = Lattices(QQ)([[0, 1], [1, 0]])
    nonisometry = engine_matrix(SageQQ, [[1, 1], [0, 1]])

    with raises(ValueError, match="does not preserve the lattice form"):
        lattice.Aut()._isometry_from_column_matrix(nonisometry)
