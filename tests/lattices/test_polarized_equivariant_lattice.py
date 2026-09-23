r"""The polarized Enriques arithmetic group as an owned intersection."""

from dzack_research.preamble.all import Involutions, NamedLattices, Set
from dzack_research.preamble.categories.lattice_centralizers import (
    PolarizedEquivariantLattice,
)


def test_enriques_polarization_retains_invariant_lift_and_group_maps() -> None:
    lattice = NamedLattices.LK3
    involution = Involutions.I_En
    extension = involution.primitive_extension()
    invariant = extension.invariant
    inclusion = invariant.inclusion()
    labels = invariant.module_generating_set()
    polarization = (
        inclusion(invariant.module_generator(labels[0]))
        + inclusion(invariant.module_generator(labels[1]))
    )

    polarized = involution.polarized(polarization)
    assert isinstance(polarized, PolarizedEquivariantLattice)
    assert polarized.lattice() is lattice
    assert polarized.isometry() == involution
    assert polarized.polarization() == polarization
    assert inclusion(polarized.invariant_polarization()) == polarization

    centralizer = polarized.centralizer_group()
    stabilizer = polarized.polarization_stabilizer()
    group = polarized.polarized_group()
    assert group.supergroup() is lattice.O()
    assert involution in centralizer
    assert involution in stabilizer
    assert involution in group
    assert lattice.O().one() in group

    negation = lattice.O()(
        {label: -lattice.module_generator(label) for label in lattice.module_generating_set()}
    )
    assert negation in centralizer
    assert negation not in stabilizer
    assert negation not in group
    assert group.intersected_subgroups() == Set((centralizer, stabilizer))
