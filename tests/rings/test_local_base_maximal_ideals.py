r"""The maximal ideal of a ring built on a local base.

For a local base ``(R, m)`` the ring ``R[[t_1, ..., t_n]]`` is local with
maximal ideal ``m A + (t_1, ..., t_n)``, and so is ``R[e]/(e^2)`` with maximal
ideal ``m A + (e)``.  Both parts are needed: over ``Z_3`` the scalar ``3`` is a
non-unit of the power-series ring, and in two variables both variables are.
"""

from dzack_research.preamble.all import (
    CommutativeIdeals,
    GF,
    QQ,
    Zp,
)


def test_a_fields_maximal_ideal_is_the_owned_zero_ideal() -> None:
    ideal = QQ.maximal_ideal()

    assert ideal in CommutativeIdeals(QQ)
    assert tuple(ideal.ideal_generators()) == (QQ.zero(),)
    assert QQ.residue_field() is QQ


def test_power_series_in_two_variables_are_local_at_both_variables() -> None:
    ring = QQ.power_series_ring("x,y")

    assert tuple(ring.maximal_ideal().ideal_generators()) == (
        ring.algebra_generator("x"),
        ring.algebra_generator("y"),
    )


def test_power_series_over_a_local_base_retain_the_base_maximal_ideal() -> None:
    base = Zp(3)
    (base_uniformizer,) = base.maximal_ideal().ideal_generators()
    ring = base.power_series_ring("t")

    assert tuple(ring.maximal_ideal().ideal_generators()) == (
        ring(base_uniformizer),
        ring.algebra_generator("t"),
    )
    assert ring.residue_field() is base.residue_field()
    assert int(ring.residue_field().cardinality()) == 3


def test_dual_numbers_over_a_local_base_retain_the_base_maximal_ideal() -> None:
    base = Zp(3)
    (base_uniformizer,) = base.maximal_ideal().ideal_generators()
    ring = base.dual_numbers()

    generators = ring.maximal_ideal().ideal_generators()

    assert tuple(generators) == (ring(base_uniformizer), ring.algebra_generator("epsilon"))
    assert ring.residue_field() is base.residue_field()


def test_dual_numbers_over_a_field_are_local_at_the_nilpotent_alone() -> None:
    ring = GF(7).dual_numbers()

    assert tuple(ring.maximal_ideal().ideal_generators()) == (ring.algebra_generator("epsilon"),)


def test_padic_principal_quotient_cardinality_is_residue_size_to_valuation() -> None:
    ring = Zp(2)
    quotient = ring.quotient_ring(ring.ideal(ring(6)))

    assert quotient.cardinality() == 2
