r"""Archive reconciliation for the graded basis of the four free constructions."""

from dzack_research.preamble.all import (
    AlternatingAlgebraOn,
    DividedPowerAlgebraOn,
    QQ,
    SymmetricAlgebraOn,
    TensorAlgebraOn,
    ZZ,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set


def _two_labels():
    return finite_ordered_set(("x", "y"))


def test_archive_graded_piece_monomials_are_the_live_piece_basis() -> None:
    labels = _two_labels()
    algebras = (
        TensorAlgebraOn(QQ, labels),
        SymmetricAlgebraOn(QQ, labels),
        AlternatingAlgebraOn(QQ, labels),
        DividedPowerAlgebraOn(QQ, labels),
    )
    expected_degree_two = (4, 3, 1, 3)

    for algebra, expected in zip(algebras, expected_degree_two, strict=True):
        monomials = algebra.graded_piece_monomials(2)
        assert monomials.index_set() is algebra.graded_piece(2).module_generating_set()
        assert int(monomials.cardinality()) == expected
        assert all(algebra.degree_on_module_generator(value) == 2 for value in monomials)


def test_archive_exterior_degree_above_rank_has_empty_basis() -> None:
    exterior = AlternatingAlgebraOn(QQ, _two_labels())
    assert exterior.graded_piece_monomials(3).cardinality() == 0


def test_archive_divided_and_symmetric_bases_agree_but_products_do_not() -> None:
    labels = _two_labels()
    divided = DividedPowerAlgebraOn(ZZ, labels)
    symmetric = SymmetricAlgebraOn(ZZ, labels)

    for degree in range(4):
        assert divided.graded_piece_monomials(degree).cardinality() == symmetric.graded_piece_monomials(degree).cardinality()

    divided_x = divided.algebra_generator("x")
    symmetric_x = symmetric.algebra_generator("x")
    gamma_two = divided.divided_power(divided_x, 2)
    divided_basis = tuple(divided.graded_piece_monomials(2))
    symmetric_basis = tuple(symmetric.graded_piece_monomials(2))
    assert gamma_two in divided_basis
    assert symmetric_x * symmetric_x in symmetric_basis
    assert divided_x * divided_x == 2 * gamma_two


def test_archive_divided_ideal_degree_includes_divided_relations() -> None:
    divided = DividedPowerAlgebraOn(ZZ, finite_ordered_set(("x",)))
    x = divided.algebra_generator("x")
    degree_three = divided.ideal_generators_in_degree((2 * x,), 3)

    divided_relation = divided.divided_power(2 * x, 3)
    assert any(generator == divided_relation for generator in degree_three)
