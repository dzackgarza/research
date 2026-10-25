r"""The integers expose the foundational owned-ring constructions."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_integer_ring_exposes_fraction_module_polynomial_and_matrix_constructions() -> None:
    polynomials = ZZ.polynomial_ring("x")
    x = polynomials.algebra_generator("x")
    laurent = ZZ.laurent_polynomial_ring("t")
    t = laurent.algebra_generator("t")
    series = ZZ.power_series_ring("q")
    q = series.power_series_variable()
    matrices = ZZ.matrix_space(2)
    module = ZZ.free_module(2)

    assert ZZ in OwnedRings()
    assert ZZ.cardinality() == aleph0
    assert ZZ.fraction_field() is QQ
    assert module.module_rank() == 2
    assert x in polynomials
    assert t * t**-1 == laurent.one()
    assert q.coefficient(1) == ZZ.one()
    assert matrices.identity_matrix().determinant() == ZZ.one()
    assert ZZ.is_central(ZZ(2))
    assert ZZ.regular_module().module_rank() == 1
    assert ZZ.unit_group().order() == 2
    assert ZZ.Mor(QQ).cardinality() == cardinal(1)


def test_native_ring_and_extension_constructions_retain_the_additive_group_spine() -> None:
    r"""Ring, polynomial, quotient and fraction-field owners construct additive groups."""
    polynomials = QQ.polynomial_ring("x")
    quotient = polynomials.quotient_ring(polynomials.ideal(polynomials.algebra_generator("x") ** 2 - 2))
    fraction_field = polynomials.fraction_field()

    additive_groups = AdditiveGroups().AdditiveCommutative()
    assert OwnedRings().is_subcategory(additive_groups)
    assert OwnedRings().Commutative().is_subcategory(additive_groups)
    assert ZZ in additive_groups
    assert polynomials in additive_groups
    assert polynomials in OwnedRings().Commutative()
    assert polynomials in OwnedIntegralDomains()
    assert polynomials in OwnedRings().Noetherian()
    assert quotient in additive_groups
    assert quotient in OwnedRings().Commutative()
    assert fraction_field in additive_groups
    assert fraction_field in OwnedRings().Division().Commutative()


def test_cyclic_double_cover_presentation_has_square_equal_to_branch_coefficient() -> None:
    cover = QQ.cyclic_cover_presentation(QQ.one(), 2)
    z = cover.algebra_generator("z")

    assert z**2 == cover.one()


def test_predicate_subring_constructor_recovers_integers_inside_rationals() -> None:
    integers = QQ.predicate_subring(
        lambda element: element.denominator() == 1,
        "the denominator is one",
    )

    assert QQ(3) in integers
    assert QQ(1) / 2 not in integers

