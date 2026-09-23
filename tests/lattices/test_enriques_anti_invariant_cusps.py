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


