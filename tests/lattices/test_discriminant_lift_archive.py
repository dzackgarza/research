r"""Archive reconciliation for lifting discriminant-form automorphisms."""

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_nontrivial_discriminant_action_has_a_live_lattice_isometry_lift() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)("A2")
    orthogonal_group = lattice.O()
    negation = orthogonal_group(
        {
            label: -lattice.module_generator(label)
            for label in lattice.module_generating_set()
        }
    )
    target_action = negation.discriminant_morphism()

    assert target_action != orthogonal_group.one().discriminant_morphism()

    lifted = orthogonal_group.discriminant_lift(target_action)

    assert lifted is not None
    assert lifted in orthogonal_group
    assert lifted.discriminant_morphism() == target_action
