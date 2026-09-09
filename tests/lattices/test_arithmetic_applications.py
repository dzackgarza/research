r"""The three arithmetic research constructions retain their actual maps."""

from dzack_research.preamble.catalogue import NamedLattices
from dzack_research.preamble.categories.arithmetic_applications import (
    enriques_equivariant_k3_application,
    enriques_higher_witt_application,
    lorentzian_e10_application,
)


def test_lorentzian_application_retains_the_cusp_reduction_and_levi_map() -> None:
    application = lorentzian_e10_application()
    line = application.isotropic_line()
    reduction = application.reduction_lattice()
    levi = application.levi_action()

    assert application.lattice() is NamedLattices.E10
    assert application.orthogonal_group() is application.lattice().O()
    assert application.positive_cone_subgroup().supergroup() is application.orthogonal_group()
    assert line.ambient_lattice() is application.lattice()
    assert reduction.module_rank() == 8
    assert reduction.is_isometric(NamedLattices.E8)
    assert levi.domain() is application.parabolic_subgroup()
    assert levi.codomain() is reduction.Aut()

    lifted_identity = application.lift_reduction_isometry(reduction.Aut().one())
    assert lifted_identity in application.parabolic_subgroup()
    assert levi(lifted_identity) == reduction.Aut().one()


def test_higher_witt_application_uses_the_glue_compatible_enriques_group() -> None:
    application = enriques_higher_witt_application()
    group = application.arithmetic_group()

    assert application.lattice().is_isometric(NamedLattices.TEn)
    assert group.supergroup() is application.lattice().O()
    assert group.contains_character_kernel()
    assert group.character_data_is_complete()
    assert application.line_cusps().cardinality() > 0
    assert application.plane_cusps().cardinality() > 0
    assert application.full_orthogonal_tits_building_incidence().cardinality() > 0
    assert application.tits_building_incidence().cardinality() > 0

    incidence = application.tits_building_incidence()[0]
    assert incidence.line_transporter() in group
    assert incidence.plane_transporter() in group


def test_equivariant_application_retains_gluing_centralizer_and_polarization_group() -> None:
    application = enriques_equivariant_k3_application()
    extension = application.primitive_extension()
    polarization = application.polarization()
    polarized_group = application.polarized_group()

    assert application.lattice() is NamedLattices.LK3
    assert extension.index() > 1
    assert application.involution()(polarization) == polarization
    assert polarization.q() != 0
    assert polarized_group.supergroup() is application.lattice().O()
    assert polarized_group.one() in polarized_group
    assert application.anti_invariant_lattice().is_isometric(NamedLattices.TEn)
    assert application.anti_invariant_arithmetic_group().character_data_is_complete()
    assert application.anti_invariant_line_cusps().cardinality() > 0
