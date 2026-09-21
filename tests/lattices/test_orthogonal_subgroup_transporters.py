r"""Finite-character orbit decisions retain actual subgroup transporters."""

import pytest

from dzack_research.preamble.all import (
    ZZ,
    Lattices,
)


def test_special_orthogonal_vector_equivalence_returns_a_live_transporter() -> None:
    lattice = Lattices(ZZ)("A2")
    group = lattice.SO()
    root = lattice.basis_vector(0)

    witness = group.vector_equivalence_witness(root, root)
    assert witness == group.supergroup().one()
    assert witness in group
    assert witness(root) == root


def test_target_stabilizer_left_adjusts_an_O_transporter_into_SO() -> None:
    lattice = Lattices(ZZ)(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
        ]
    )
    first, second, _third = lattice.module_generators()
    special = lattice.SO()

    witness = special.vector_equivalence_witness(first, second)
    assert witness is not None
    assert witness in special
    assert witness.determinant() == 1
    assert witness(first) == second
    assert special.vectors_are_equivalent(first, second)


def test_special_orthogonal_isotropic_equivalence_returns_a_live_transporter(
    monkeypatch,
) -> None:
    from py_polyhedral import binaries as polyhedral

    lattice = Lattices(ZZ)("U")
    minus_identity = [[-1, 0], [0, -1]]

    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_automorphism_group",
        lambda _gram: [minus_identity],
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_stabilizer_isotropic_subspace",
        lambda _gram, _basis, choice="plane": [minus_identity],
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_test_equivalence_isotropic_k_plane",
        lambda _gram, _left, _right, choice="plane": [[1, 0], [0, 1]],
    )

    line = lattice.primitive_isotropic_subobject(lattice.basis_vector(0))
    special = lattice.SO()
    witness = special.isotropic_equivalence_witness(line, line)
    assert witness is not None
    assert witness in special
    assert special.isotropic_are_equivalent(line, line)


def test_mixed_predicate_intersection_does_not_claim_a_complete_character_quotient() -> None:
    lattice = Lattices(ZZ)("A2")
    special = lattice.SO()
    identity_only = lattice.O().predicate_subgroup(lambda isometry: isometry == lattice.O().one(), "g=1")
    mixed = special.intersection(identity_only)

    assert not mixed.character_data_is_complete()
    assert not mixed.contains_character_kernel()
    with pytest.raises(ValueError, match="do not define this whole subgroup"):
        mixed.finite_character_quotient()
