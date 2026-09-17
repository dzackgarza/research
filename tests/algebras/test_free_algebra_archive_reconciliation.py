r"""Archive reconciliation for the graded basis of the four free constructions."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    AlternatingAlgebras,
    DividedPowerAlgebras,
    FreeAlgebras,
    GradedFreeAlgebras,
    SymmetricAlgebras,
    TensorAlgebras,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/categories/algebras/free_algebras.sage",
        "live_owner": "src/dzack_research/preamble/categories/algebras/free_algebras.py",
        "owner_overrides": {
            "TensorAlgebras.ParentMethods.center_embedding": "src/dzack_research/preamble/categories/algebras/free_algebras.py",
        },
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/test_free_constructions.sage",
        "live_owner": "tests/algebras/test_free_algebra_archive_reconciliation.py",
        "owner_overrides": {
            "test_tensor_and_divided_squares_respect_a_module_presentation": "tests/algebras/test_power_algebras.py",
            "test_the_divided_square_classifies_quadratic_maps": "tests/forms/test_classifier_vocabulary.py",
            "test_divided_squares_are_symmetric_tensor_invariants": "tests/algebras/test_tensor_symmetric_adjunctions.py",
            "test_higher_divided_powers_are_symmetric_tensor_invariants": "tests/algebras/test_tensor_symmetric_adjunctions.py",
            "test_the_free_constructions_are_related_by_the_canonical_maps": "tests/algebras/test_power_algebra_extensions_archive.py",
            "test_tensor_and_symmetric_freeness_are_homset_bijections": "tests/algebras/test_tensor_symmetric_adjunctions.py",
            "test_the_four_free_algebra_functors_preserve_identities_and_composition": "tests/algebras/test_functor_adjunctions.py",
            "test_the_free_algebra_units_are_natural_on_presented_modules": "tests/algebras/test_functor_adjunctions.py",
            "test_free_algebra_functors_preserve_their_characteristic_operations": "tests/algebras/test_power_algebra_extensions_archive.py",
        },
        "disposition": "reconciled-live-owner",
    },
)


def _two_labels():
    return finite_ordered_set(("x", "y"))


def test_archive_graded_piece_monomials_are_the_live_piece_basis() -> None:
    labels = _two_labels()
    algebras = (
        QQ.free_module(labels).tensor_algebra(),
        QQ.free_module(labels).symmetric_algebra(),
        QQ.free_module(labels).exterior_algebra(),
        QQ.free_module(labels).divided_power_algebra(),
    )
    expected_degree_two = (4, 3, 1, 3)

    for algebra, expected in zip(algebras, expected_degree_two, strict=True):
        monomials = algebra.graded_piece_monomials(2)
        assert monomials.index_set() is algebra.graded_piece(2).module_generating_set()
        assert int(monomials.cardinality()) == expected
        assert all(algebra.degree_on_module_generator(value) == 2 for value in monomials)


def test_archive_exterior_degree_above_rank_has_empty_basis() -> None:
    exterior = QQ.free_module(_two_labels()).exterior_algebra()
    assert exterior.graded_piece_monomials(3).cardinality() == 0


def test_archive_divided_and_symmetric_bases_agree_but_products_do_not() -> None:
    labels = _two_labels()
    divided = ZZ.free_module(labels).divided_power_algebra()
    symmetric = ZZ.free_module(labels).symmetric_algebra()

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
    divided = ZZ.free_module(finite_ordered_set(("x",))).divided_power_algebra()
    x = divided.algebra_generator("x")
    degree_three = divided.ideal_generators_in_degree((2 * x,), 3)

    divided_relation = divided.divided_power(2 * x, 3)
    assert any(generator == divided_relation for generator in degree_three)


def test_archive_free_algebra_retains_its_selected_generating_set() -> None:

    labels = finite_ordered_set(("a", "b", "c"))
    algebra = QQ.free_module(labels).symmetric_algebra()

    assert algebra.algebra_generating_set() is labels
    assert tuple(algebra.algebra_generators()) == tuple(
        algebra.algebra_generator(label) for label in labels
    )
    assert algebra.algebra_generator_morphism().domain() is labels


def test_archive_free_algebra_map_is_determined_on_generators_and_extends_multiplicatively() -> None:

    source_labels = finite_ordered_set(("x", "y"))
    target_labels = finite_ordered_set(("u", "v", "w"))
    source = QQ.free_module(source_labels).symmetric_algebra()
    target = QQ.free_module(target_labels).symmetric_algebra()
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

    source = QQ.free_module(finite_ordered_set(("x", "y"))).symmetric_algebra()
    middle = QQ.free_module(finite_ordered_set(("u", "v"))).symmetric_algebra()
    target = QQ.free_module(finite_ordered_set(("s", "t"))).symmetric_algebra()

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
    exterior = QQ.free_module(labels).exterior_algebra()
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
        QQ.free_module(labels).tensor_algebra(),
        QQ.free_module(labels).symmetric_algebra(),
        QQ.free_module(labels).exterior_algebra(),
        QQ.free_module(labels).divided_power_algebra(),
    ):
        structure = algebra.algebra_structure_morphism()
        x = algebra.algebra_generator("x")

        assert structure.domain() is QQ
        assert structure(QQ(3)) == QQ(3) * algebra.one()
        assert structure(QQ(3)) * x == QQ(3) * x
        assert x * structure(QQ(3)) == QQ(3) * x


def test_archive_graded_piece_is_a_submodule_with_its_actual_inclusion() -> None:
    algebra = QQ.free_module(_two_labels()).tensor_algebra()
    piece = algebra.graded_piece(2)
    inclusion = piece.inclusion()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")

    assert inclusion.codomain() is algebra
    assert piece.module_rank() == 4
    assert x * y in piece
    assert x not in piece


def test_archive_degree_two_pieces_remain_countable_on_countably_many_generators() -> None:
    from dzack_research.preamble.all import Sets, aleph0

    labels = Sets.Δ[aleph0]
    for algebra in (
        QQ.free_module(labels).tensor_algebra(),
        QQ.free_module(labels).symmetric_algebra(),
        QQ.free_module(labels).exterior_algebra(),
        QQ.free_module(labels).divided_power_algebra(),
    ):
        piece = algebra.graded_piece(2)
        assert piece.module_generating_set() in Sets().Countable().Infinite()
        generator = next(iter(piece.module_generators()))
        image = piece.inclusion()(generator)
        assert image in algebra
        assert image.degree() == 2


def test_archive_free_algebra_categories_are_the_live_four_flavor_placements() -> None:
    labels = _two_labels()
    symmetric = QQ.free_module(labels).symmetric_algebra()
    specimens = (
        (QQ.free_module(labels).tensor_algebra(), TensorAlgebras(QQ)),
        (symmetric, SymmetricAlgebras(QQ)),
        (QQ.free_module(labels).exterior_algebra(), AlternatingAlgebras(QQ)),
        (QQ.free_module(labels).divided_power_algebra(), DividedPowerAlgebras(QQ)),
    )

    assert QQ.free_module(labels).symmetric_algebra() is symmetric
    for algebra, flavor in specimens:
        assert algebra in FreeAlgebras(QQ)
        assert algebra in GradedFreeAlgebras(QQ)
        assert algebra in flavor
        assert algebra.is_free()

def test_tensor_algebra_homogeneous_degree_is_free_word_length() -> None:
    import pytest

    from dzack_research.preamble.all import ZZ
    from dzack_research.preamble.categories.sets.finite_ordered_sets import (
        finite_ordered_set,
    )

    module = ZZ.free_module(finite_ordered_set(("x", "y")))
    algebra = module.tensor_algebra()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")

    assert algebra.homogeneous_degree(x) == 1
    assert algebra.homogeneous_degree(x + y) == 1
    assert algebra.homogeneous_degree(x * y) == 2
    with pytest.raises(ValueError, match="not homogeneous"):
        algebra.homogeneous_degree(x + x * y)
