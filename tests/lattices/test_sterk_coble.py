from dzack_research.preamble.all import Coble, Sterk, ZZ, tensor

_STERK_NORM_COUNTS = {
    "Sterk_1": {-4: 12, -2: 0},
    "Sterk_2": {-4: 9, -2: 1},
    "Sterk_3": {-4: 10, -2: 2},
    "Sterk_4": {-4: 9, -2: 2},
    "Sterk_5": {-4: 10, -2: 4},
}


def test_sterk_configurations_have_the_archived_root_counts_and_norms() -> None:
    configurations = Sterk.sterk_roots()
    assert {name: roots.cardinality() for name, roots in configurations.items()} == {
        "Sterk_1": 12,
        "Sterk_2": 10,
        "Sterk_3": 12,
        "Sterk_4": 11,
        "Sterk_5": 14,
    }
    assert all(root.q() in (-2, -4) for roots in configurations.values() for root in roots)
    assert {name: {norm: sum(root.q() == norm for root in roots) for norm in (-4, -2)} for name, roots in configurations.items()} == _STERK_NORM_COUNTS


def test_five_sterk_diagrams_retain_the_exact_root_pairings() -> None:
    configurations = Sterk.sterk_roots()
    diagrams = Sterk.diagrams()

    assert set(diagrams) == set(configurations)
    for name, roots in configurations.items():
        diagram = diagrams[name]
        assert diagram.is_rooted()
        assert diagram.cardinality() == roots.cardinality()
        expected = tensor(
            ZZ,
            (),
            (len(roots), len(roots)),
            [[left.b(right) for right in roots] for left in roots],
        )
        assert diagram.root_gram_tensor() == expected


def test_sterk_alternative_realizations_reproduce_the_archived_root_data() -> None:
    lattice, sterk_5 = Sterk.sterk5_in_U_E8_2()
    alternatives = Sterk.sterks_in_TEn()

    assert lattice.rank() == 10
    assert sterk_5.cardinality() == 14
    assert sum(root.q() == -4 for root in sterk_5) == _STERK_NORM_COUNTS["Sterk_5"][-4]
    assert sum(root.q() == -2 for root in sterk_5) == _STERK_NORM_COUNTS["Sterk_5"][-2]

    assert {name: roots.cardinality() for name, roots in alternatives.items()} == {
        "Sterk_1": 12,
        "Sterk_2": 10,
        "Sterk_3": 12,
    }
    assert all(root.q() in (-2, -4) for roots in alternatives.values() for root in roots)


def test_sterk_ten_realizations_preserve_the_two_archived_dual_scalings() -> None:
    from dzack_research.preamble.all import NamedLattices

    lattice = NamedLattices.TEn
    alternatives = Sterk.sterks_in_TEn()
    dual = tuple(lattice.dual_lattice().module_generators())
    b = {str(label): lattice.module_generator(label) for label in lattice.module_generating_set()}
    c = lattice.correlation()

    assert alternatives["Sterk_1"][9] == c.lift(c(2 * b["ep"]) + 2 * dual[11])
    assert c(alternatives["Sterk_1"][9]) != c(2 * b["ep"]) + dual[11]
    assert alternatives["Sterk_3"][8] == c.lift(c(2 * b["fp"]) + 2 * dual[11])


def test_sterk_diagram_layouts_are_exact_optional_presentation_data() -> None:
    layouts = Sterk.diagram_layouts()
    diagrams = Sterk.diagrams()

    assert layouts["Sterk_1"][9] == (13 / 4, -19 / 4)
    for name, diagram in diagrams.items():
        assert diagram.preferred_positions() == layouts[name]
        vertex = tuple(diagram.index_set())[0]
        assert diagram.induced_subdiagram((vertex,)).preferred_positions() == {vertex: layouts[name][vertex]}


def test_sterk_selected_vectors_are_the_five_isotropic_cusps() -> None:
    vectors = Sterk.selected_isotropic_vectors()
    assert vectors.cardinality() == 5
    assert all(vector.q() == 0 for vector in vectors.values())


def test_coble_has_seventeen_isotropic_candidates_and_embedding_chain_preserves_them() -> None:
    source = Coble.isotropic_vectors()
    ten = Coble.isotropic_vectors_in_TEn()
    tdp = Coble.isotropic_vectors_in_TdP()
    assert source.cardinality() == ten.cardinality() == tdp.cardinality() == 17
    assert all(vector.q() == 0 for vector in source.values())
    assert all(vector.q() == 0 for vector in ten.values())
    assert all(vector.q() == 0 for vector in tdp.values())


def test_coble_rank_ten_configuration_builds_a_rooted_coxeter_diagram() -> None:
    lattice, roots = Coble.rank_ten_coxeter_roots()
    diagram = Coble.rank_ten_diagram()
    assert lattice.rank() == 10
    assert roots.cardinality() == 11
    assert diagram.is_rooted()
    assert diagram.cardinality() == 11
