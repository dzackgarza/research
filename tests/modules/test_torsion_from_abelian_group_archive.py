r"""Archive reconciliation for finite abelian groups as torsion modules."""

from sage.groups.abelian_gps.abelian_group import AbelianGroup

from dzack_research.preamble.all import ZZ, FinitelyPresentedTorsionModules


def test_crossing_preserves_the_selected_two_generator_presentation() -> None:
    group = AbelianGroup([2, 3], names=("a", "b"))
    generators = tuple(group.gens())
    module = FinitelyPresentedTorsionModules(ZZ).from_abelian_group(group)

    assert tuple(module.module_generating_set()) == generators
    assert module.module_rank() == 0
    assert tuple(module.invariant_factors()) == (2, 3)
    assert module.cardinality() == 6


def test_crossing_discovers_a_relation_between_redundant_generators() -> None:
    cyclic = AbelianGroup([6], names=("g",))
    generator = cyclic.gen(0)
    subgroup_with_redundant_generators = cyclic.subgroup((generator**2, generator**3))
    selected = tuple(subgroup_with_redundant_generators.gens())
    module = FinitelyPresentedTorsionModules(ZZ).from_abelian_group(
        subgroup_with_redundant_generators
    )

    assert tuple(module.module_generating_set()) == selected
    assert module.cardinality() == 6
    assert tuple(module.invariant_factors()) == (6,)
