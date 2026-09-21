from dzack_research.preamble.all import ZZ, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/integrallattice/lattice_isometries.sage",
    "live_owner": "src/dzack_research/preamble/categories/lattice_morphisms.py",
    "owner_overrides": {
        "LatticeIsometries.ParentMethods.special_orthogonal_subgroup": "src/dzack_research/preamble/categories/lattices.py",
        "LatticeIsometries.ParentMethods.spinor_kernel_subgroup": "src/dzack_research/preamble/categories/lattices.py",
        "LatticeIsometries.ElementMethods.centralizer_discriminant_image": "src/dzack_research/preamble/categories/lattice_morphisms.py",
        "LatticeIsometries.ElementMethods.cyclic_subgroup": "src/dzack_research/preamble/categories/lattice_morphisms.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_orthogonal_group_owns_acted_lattice_generators_and_matrix_elements() -> None:
    lattice = Lattices(ZZ)("A1")
    group = lattice.O()
    identity = group.one()

    assert group.ambient_lattice() is lattice
    assert group.group_generators().cardinality() >= 1
    assert group.contains(identity)
    assert group.element(identity.matrix()) == identity


def test_discriminant_and_stable_group_vocabulary_uses_the_existing_representation() -> None:
    lattice = Lattices(ZZ)("A1")
    group = lattice.O()

    assert group.discriminant_representation() is lattice.discriminant_representation()
    assert group.stable_subgroup() is lattice.stable_orthogonal_group()
    assert lattice.O_plus() is lattice.stable_orthogonal_group()


def test_vector_and_sublattice_stabilizers_are_predicate_subgroups_of_one_O_L() -> None:
    lattice = Lattices(ZZ)("U")
    group = lattice.O()
    e = lattice.basis_vector(0)
    line = lattice.primitive_sublattice_from((e,))

    vector_stabilizer = group.stabilizer(e)
    setwise = group.stabilizer(line, action="setwise")
    pointwise = group.stabilizer(line, action="pointwise")

    assert group.one() in vector_stabilizer
    assert group.one() in setwise
    assert group.one() in pointwise
    assert group.intersection(setwise, pointwise).one() == group.one()


def test_component_character_kernel_and_vector_transporter_are_live_group_maps() -> None:
    lattice = Lattices(ZZ)("U")
    group = lattice.O()
    character = group.component_character()
    kernel = group.kernel(character)
    component = group.component_subgroup()
    e = lattice.basis_vector(0)

    assert lattice.O_component().one() == group.one()
    assert kernel.one() == group.one()
    assert component.one() == group.one()
    assert group.preimage(character, character.codomain().subgroup_on(())).one() == group.one()
    assert group.transporter(e, e)(e) == e


def test_centralizer_of_identity_is_the_whole_orthogonal_group_predicate() -> None:
    lattice = Lattices(ZZ)("A1")
    group = lattice.O()
    centralizer = group.centralizer(group.one())

    assert group.one() in centralizer
    assert all(generator in centralizer for generator in group.group_generators())
