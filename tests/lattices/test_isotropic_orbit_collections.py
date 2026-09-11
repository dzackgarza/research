r"""Archive reconciliation for integral isotropic and character-split orbits.

The archived monolithic orbit module is now split by mathematical ownership:
full-orthogonal isotropic geometry, structured predicate subgroups, and finite
character-quotient splitting/transporters.
"""

from dzack_research.preamble.all import Lattices, ZZ

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/integrallattice/isotropic_orbits.sage",
    "live_owner": "src/dzack_research/preamble/categories/isotropic_orbits.py",
    "owner_overrides": {
        "OrthogonalPredicateSubgroups": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.super_categories": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.domain": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.contains_character_kernel": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.intersection": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.isotropic_line_orbit_representatives": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.isotropic_plane_orbit_representatives": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.isotropic_flag_orbit_representatives": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.isotropic_lines_are_equivalent": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.isotropic_planes_are_equivalent": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.isotropic_flags_are_equivalent": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.vector_orbit_representatives": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.vectors_are_equivalent": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "OrthogonalPredicateSubgroups.ParentMethods.vector_equivalence_witness": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
        "orthogonal_predicate_subgroup": "src/dzack_research/preamble/categories/group/predicate_subgroups.py",
    },
    "disposition": "reconciled-live-owner",
}


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

