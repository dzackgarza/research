from dzack_research.preamble.all import NamedLattices


def test_a2_discriminant_primary_part_is_the_whole_three_group() -> None:
    discriminant = NamedLattices.A2.discriminant_group()
    primary = discriminant.primary_part(3)

    assert primary.cardinality() == discriminant.cardinality() == 3
    assert all(element in primary for element in discriminant.elements())


def test_a2_discriminant_has_trivial_two_primary_part() -> None:
    discriminant = NamedLattices.A2.discriminant_group()
    primary = discriminant.primary_part(2)

    assert primary.cardinality() == 1
    assert primary.embedded_elements().cardinality() == 1
    assert primary.embedded_elements()[0] == discriminant.zero()
