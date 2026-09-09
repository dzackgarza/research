r"""Archive reconciliation for elementary discriminant predicates."""

from dzack_research.preamble.catalogue import NamedLattices


def test_p_elementary_predicate_separates_prime_exponent_from_prime_power_order() -> None:
    assert NamedLattices.U_2.is_p_elementary(2)
    assert NamedLattices.E8.is_p_elementary(2)

    assert not NamedLattices.A2.is_p_elementary(2)
    assert NamedLattices.A2.discriminant_group().is_p_elementary(3)

    # <4> has discriminant group C4.  Its order is a power of two, but its
    # exponent is four, so it is not 2-elementary.
    assert not NamedLattices.Z.twist(4).is_p_elementary(2)


def test_two_elementary_coeven_predicate_is_the_delta_zero_condition() -> None:
    for lattice in (
        NamedLattices.U,
        NamedLattices.U_2,
        NamedLattices.E8,
        NamedLattices.E8_2,
        NamedLattices.E10_2,
        NamedLattices.TEn,
    ):
        assert lattice.delta() in (0, 1)
        assert lattice.is_coeven() == (lattice.delta() == 0)
