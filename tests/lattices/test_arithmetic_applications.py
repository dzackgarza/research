r"""The three arithmetic research constructions retain their actual maps."""

from dzack_research.preamble.catalogue import NamedLattices
from dzack_research.preamble.categories.arithmetic_applications import (
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






