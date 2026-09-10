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


def test_archive_free_algebra_retains_its_selected_generating_set() -> None:
    from dzack_research.preamble.all import FreeAlgebraOn

    labels = finite_ordered_set(("a", "b", "c"))
    algebra = FreeAlgebraOn(QQ, labels)

    assert algebra.algebra_generating_set() is labels
    assert tuple(algebra.algebra_generators()) == tuple(
        algebra.algebra_generator(label) for label in labels
    )
    assert algebra.algebra_generator_morphism().domain() is labels


def test_archive_free_algebra_map_is_determined_on_generators_and_extends_multiplicatively() -> None:
    from dzack_research.preamble.all import FreeAlgebraOn

    source_labels = finite_ordered_set(("x", "y"))
    target_labels = finite_ordered_set(("u", "v", "w"))
    source = FreeAlgebraOn(QQ, source_labels)
    target = FreeAlgebraOn(QQ, target_labels)
    morphism = source.Mor(target)(
        {
            "x": target.algebra_generator("v"),
            "y": target.algebra_generator("w"),
        }
    )

    assert morphism.domain() is source
    assert morphism.codomain() is target
    assert morphism.algebra_generator_morphism()("x") == target.algebra_generator("v")
    assert morphism.algebra_generator_morphism()("y") == target.algebra_generator("w")
    assert morphism(source.algebra_generator("x") * source.algebra_generator("y")) == (
        target.algebra_generator("v") * target.algebra_generator("w")
    )


def test_archive_free_algebra_morphisms_compose_and_have_the_expected_identity() -> None:
    from dzack_research.preamble.all import FreeAlgebraOn

    source = FreeAlgebraOn(QQ, finite_ordered_set(("x", "y")))
    middle = FreeAlgebraOn(QQ, finite_ordered_set(("u", "v")))
    target = FreeAlgebraOn(QQ, finite_ordered_set(("s", "t")))

    first = source.Mor(middle)(
        {
            "x": middle.algebra_generator("v"),
            "y": middle.algebra_generator("u"),
        }
    )
    second = middle.Mor(target)(
        {
            "u": target.algebra_generator("s"),
            "v": target.algebra_generator("t"),
        }
    )
    composite = second * first
    identity = source.Mor(source).identity()

    assert composite(source.algebra_generator("x")) == target.algebra_generator("t")
    assert composite(source.algebra_generator("y")) == target.algebra_generator("s")
    assert identity.is_identity()
    assert identity(source.algebra_generator("x")) == source.algebra_generator("x")
    assert first * identity == first


def test_archive_exterior_shuffle_parity_is_retained() -> None:
    labels = finite_ordered_set(("x", "y", "z"))
    exterior = AlternatingAlgebraOn(QQ, labels)
    x = exterior.algebra_generator("x")
    y = exterior.algebra_generator("y")
    z = exterior.algebra_generator("z")

    assert (x * y) * z == x * (y * z)
    assert z * x * y == x * y * z
    assert y * x * z == -(x * y * z)
    assert x * y * z != exterior.zero()


def test_archive_scalars_enter_each_free_construction_through_its_unit() -> None:
    labels = _two_labels()
    for algebra in (
        TensorAlgebraOn(QQ, labels),
        SymmetricAlgebraOn(QQ, labels),
        AlternatingAlgebraOn(QQ, labels),
        DividedPowerAlgebraOn(QQ, labels),
    ):
        structure = algebra._ring_morphism_defining_algebra_structure()
        x = algebra.algebra_generator("x")

        assert structure.domain() is QQ
        assert structure(QQ(3)) == QQ(3) * algebra.one()
        assert structure(QQ(3)) * x == QQ(3) * x
        assert x * structure(QQ(3)) == QQ(3) * x
