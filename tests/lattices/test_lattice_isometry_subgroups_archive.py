r"""Archive reconciliation for subgroups of integral lattice isometry groups.

The archive used a dedicated ``LatticeIsometrySubgroups`` category.  The live
owner uses the general subgroup construction on the actual orthogonal-group
parent: a subgroup still consists of lattice isometries, while its ambient
``O(L)`` and selected generators are retained by ``Subgroups(O(L))`` and the
more specific generated-subgroup category.
"""

from dzack_research.preamble.all import ZZ, Lattices, finite_ordered_set
from dzack_research.preamble.categories.group.groups import (
    GeneratedSubgroups,
    Subgroups,
)


def test_generated_lattice_isometry_subgroup_keeps_the_actual_orthogonal_group() -> None:
    lattice = Lattices(ZZ)("A1")
    root = lattice.basis_vector(0)
    reflection = lattice.reflection(root)
    orthogonal = lattice.O()

    subgroup = orthogonal.subgroup((reflection,))

    assert subgroup in Subgroups(orthogonal)
    assert subgroup in GeneratedSubgroups(orthogonal)
    assert subgroup.supergroup() is orthogonal
    assert subgroup.selected_subgroup_generators() == finite_ordered_set((reflection,))
    assert reflection in subgroup
    assert subgroup.one() in subgroup


def test_subgroup_elements_remain_actual_lattice_isometries_not_detached_matrices() -> None:
    lattice = Lattices(ZZ)("A1")
    root = lattice.basis_vector(0)
    reflection = lattice.reflection(root)
    subgroup = lattice.O().subgroup((reflection,))

    held = subgroup(reflection)
    assert held is reflection
    assert held.domain() is lattice
    assert held.codomain() is lattice
    assert held(root) == -root
    assert held(root).q() == root.q()
    assert held * held == subgroup.one()
