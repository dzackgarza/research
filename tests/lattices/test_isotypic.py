from dzack_research.preamble.all import (
    ZZ,
    BasedFreeModule,
    FormedModules,
    GroupLattice,
    GroupModule,
    Groups,
    Lattices,
    Modules,
    tensor,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_c2_integral_isotypic_decomposition_is_the_plus_minus_underlattice() -> None:
    group = Groups.C(2)
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    x, y = module.module_generators()
    swap = module.Hom(module)({"x": y, "y": x})

    def action(group_element, vector):
        return vector if group_element == group.one() else swap(vector)

    acted = GroupModule(module, group, action)
    decomposition = acted.isotypic_decomposition()

    assert len(tuple(decomposition.isotypic_characters())) == 2
    assert decomposition.trivial_component().rank() == 1
    assert decomposition.nontrivial_components()[0].rank() == 1
    assert decomposition.index() == 2
    assert decomposition.trivial_component().inclusion().is_in_image(acted.linear_combination({"x": 1, "y": 1}))
    assert decomposition.nontrivial_components()[0].inclusion().is_in_image(acted.linear_combination({"x": 1, "y": -1}))


def test_c3_integral_characters_are_grouped_into_rational_orbits() -> None:
    group = Groups.C(3)
    module = BasedFreeModule(ZZ, finite_ordered_set(("x", "y", "z")))
    generator = next(iter(group.group_generators()))
    x, y, z = module.module_generators()
    cycle = module.Hom(module)({"x": y, "y": z, "z": x})

    def action(group_element, vector):
        exponent = next(i for i in range(3) if group_element == generator**i)
        moved = vector
        for _ in range(exponent):
            moved = cycle(moved)
        return moved

    acted = GroupModule(module, group, action)
    characters = acted.isotypic_characters()
    decomposition = acted.isotypic_decomposition()

    assert len(characters) == 2
    assert sorted(character.degree() for character in characters) == [1, 2]
    assert decomposition.trivial_component().rank() == 1
    assert decomposition.nontrivial_components()[0].rank() == 2
    assert decomposition.index() == 3


def test_group_lattice_invariants_and_formed_coinvariants_keep_the_form() -> None:
    group = Groups.C(2)
    lattice = Lattices(ZZ)("U")
    labels = tuple(lattice.module_generating_set())
    x, y = lattice.module_generators()
    swap = lattice.Aut()({labels[0]: y, labels[1]: x})

    def action(group_element, vector):
        return vector if group_element == group.one() else swap(vector)

    acted = GroupLattice(lattice, group, action)
    decomposition = acted.isotypic_decomposition()
    invariants = acted.invariant_lattice()
    formed_coinvariants = acted.formed_coinvariants()
    module_coinvariants = acted.module_coinvariants()

    assert decomposition.trivial_component().gram_tensor() == invariants.gram_tensor()
    assert decomposition.nontrivial_components()[0].gram_tensor() == formed_coinvariants.gram_tensor()
    assert decomposition.trivial_component().inclusion() == invariants.inclusion()
    assert decomposition.nontrivial_components()[0].inclusion() == formed_coinvariants.inclusion()
    assert invariants.gram_tensor() == tensor(ZZ, (), (1, 1), [[2]])
    assert formed_coinvariants.gram_tensor() == tensor(ZZ, (), (1, 1), [[-2]])
    assert module_coinvariants.rank() == 1
    assert module_coinvariants in Modules(ZZ)
    assert module_coinvariants not in FormedModules(ZZ)
    assert formed_coinvariants in FormedModules(ZZ)
