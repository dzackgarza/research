r"""Archive reconciliation for formed isotypic sublattices of a group lattice."""

from dzack_research.preamble.all import Groups, Lattices, ZZ


def _acted_a2():
    lattice = Lattices(ZZ)("A2")
    group = Groups.C(2)
    first, second = lattice.module_generators()
    swap = lattice.Aut()({0: second, 1: first})
    return Lattices(ZZ[group])(
        lattice,
        lambda element, vector: vector if element == group.one() else swap(vector),
    )


def test_archive_isotypic_lattice_retains_form_action_and_embedding() -> None:
    acted = _acted_a2()
    characters = acted.group_module().isotypic_characters()
    nontrivial = next(character for character in characters if not character.is_trivial())

    component = acted.isotypic_lattice(nontrivial)
    assert component.module_rank() == 1
    assert component.ambient_lattice() is acted
    assert component in Lattices(ZZ[acted.group()])

    generator = component.module_generators()[0]
    group_generator = acted.group().group_generators()[0]
    inclusion = component.inclusion()
    assert inclusion(component.action_of(group_generator)(generator)) == acted.action_of(
        group_generator
    )(inclusion(generator))
    assert component.determinant() == 2


def test_equipping_an_existing_sublattice_preserves_its_ambient_inclusion() -> None:
    acted = _acted_a2()
    invariant = acted.invariant_lattice()
    group = acted.group()
    equipped = Lattices(ZZ[group])(
        invariant,
        lambda _element, vector: vector,
    )

    assert equipped.ambient_lattice() is acted
    assert equipped.inclusion().codomain() is acted
    assert equipped.inclusion()(equipped.module_generators()[0]) == invariant.inclusion()(
        invariant.module_generators()[0]
    )
