from dzack_research.preamble.all import Lattices, ZZ


def test_full_orthogonal_isotropic_orbits_are_owned_finite_sets(monkeypatch) -> None:
    from py_polyhedral import binaries as polyhedral

    lattice = Lattices(ZZ)("U")
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_isotropic_k_stuff",
        lambda _gram, rank, nature: [[[1, 0]]] if rank == 1 and nature == "plane" else [],
    )

    representatives = lattice.O().isotropic_orbit_representatives(1)
    assert representatives.cardinality() == 1
    representative = representatives[0]
    assert representative.ambient_lattice() is lattice
    assert representative.module_rank() == 1


def test_finite_character_split_orbits_preserve_owned_collection_contract(monkeypatch) -> None:
    from py_polyhedral import binaries as polyhedral

    lattice = Lattices(ZZ)("U")
    swap = [[0, 1], [1, 0]]
    minus_identity = [[-1, 0], [0, -1]]
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_automorphism_group",
        lambda _gram: [swap, minus_identity],
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_isotropic_k_stuff",
        lambda _gram, rank, nature: [[[1, 0]]] if rank == 1 and nature == "plane" else [],
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_stabilizer_isotropic_subspace",
        lambda _gram, _basis, choice="plane": [minus_identity],
    )

    representatives = lattice.SO().isotropic_orbit_representatives(1)
    assert representatives.cardinality() == 2
    assert all(representative.ambient_lattice() is lattice for representative in representatives)

