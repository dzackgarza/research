r"""The Enriques anti-invariant arithmetic group from primitive gluing."""

from dzack_research.preamble.all import Involutions, NamedLattices


def test_enriques_coinvariant_group_is_the_glue_compatible_discriminant_preimage() -> None:
    extension = Involutions.I_En.primitive_extension()
    anti = extension.orthogonal_complement_inclusion().domain()
    group = extension.coinvariant_extension_subgroup()

    assert anti.is_isometric(NamedLattices.TEn)
    assert group.supergroup() is anti.O()
    assert group.contains_character_kernel()
    assert group.character_data_is_complete()


def test_enriques_anti_invariant_line_and_plane_orbits_have_actual_transporters() -> None:
    extension = Involutions.I_En.primitive_extension()
    group = extension.coinvariant_extension_subgroup()

    line_representatives = group.isotropic_orbit_representatives(1)
    plane_representatives = group.isotropic_orbit_representatives(2)
    assert line_representatives.cardinality() > 0
    assert plane_representatives.cardinality() > 0

    line = line_representatives[0]
    plane = plane_representatives[0]
    line_witness = group.isotropic_equivalence_witness(line, line)
    plane_witness = group.isotropic_equivalence_witness(plane, plane)
    assert line_witness in group
    assert plane_witness in group
