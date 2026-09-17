r"""Cyclic subgroups use the owned categorical meet for their placement."""

from dzack_research.preamble.categories.group.cyclic_subgroups import (
    CyclicGroups,
)
from dzack_research.preamble.categories.group.groups import (
    FiniteAbelianGroups,
    OwnedGroups,
    Subgroups,
)


def test_finite_cyclic_subgroup_retains_ambient_group_and_selected_generator() -> None:
    ambient = OwnedGroups().C(4)
    generator = ambient.group_generators()[0]
    subgroup = generator.cyclic_subgroup()
    declared = CyclicGroups()(generator)

    assert subgroup in CyclicGroups()
    assert declared in CyclicGroups()
    assert declared.supergroup() is ambient
    assert declared.group_generator() == generator
    assert declared.inclusion()(generator) == generator
    assert subgroup in Subgroups(ambient)
    assert subgroup in FiniteAbelianGroups()
    assert subgroup.supergroup() is ambient
    assert subgroup.group_generator() == generator
    assert subgroup.group_generators()[0] == generator
    assert subgroup.cardinality() == ambient.cardinality()
