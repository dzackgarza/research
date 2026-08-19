from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import assert_equal
from .types import (
    Lattice,
    LatticeDiscriminantGroup,
    LatticeGlueData,
    LatticePrimitiveEmbedding,
)


def test_lattice_is_isometric_small_known_examples():
    """
    method: is_isometric

    Practical classification contract:
    isometry query distinguishes equal-model hyperbolic aliases from non-isometric signatures.
    """
    u: Lattice = Lattice.U()
    h: Lattice = Lattice.H()
    e8: Lattice = Lattice.E(8)

    assert_equal(u.is_isometric(h), True, f"Expected U and H to be isometric in contract model: U={u}, H={h}")
    assert_equal(
        u.is_isometric(e8),
        False,
        f"Expected non-isometry for different signatures: U.sig={u.signature()}, E8.sig={e8.signature()}",
    )


def test_lattice_primitive_embedding_queries_for_a2_into_d4_case():
    """
    method: primitive_embedding_exists

    Practical classification contract:
    nontrivial embedding existence check on a classical pair A2 -> D4.
    """
    u: Lattice = Lattice.A(2)
    target: Lattice = Lattice.D(4)
    assert_equal(
        u.primitive_embedding_exists(target),
        True,
        f"Expected primitive embedding existence for A2 into D4 in contract example: source={u}, target={target}",
    )


def test_lattice_primitive_embeddings_returns_typed_embedding_objects():
    """
    method: primitive_embeddings

    Practical classification contract:
    primitive embedding enumeration returns typed embedding records for A2 -> D4.
    """
    u: Lattice = Lattice.A(2)
    target: Lattice = Lattice.D(4)
    embeddings: tuple[LatticePrimitiveEmbedding, ...] = u.primitive_embeddings(target)
    assert_equal(len(embeddings), 1, f"Expected one primitive embedding witness in contract model: {embeddings}")
    emb = embeddings[0]
    assert_equal(emb.source().is_isometric(u), True, f"Embedding source mismatch for A2->D4 case: emb={emb}")
    assert_equal(emb.target().is_isometric(target), True, f"Embedding target mismatch for A2->D4 case: emb={emb}")


def test_lattice_orthogonal_complement_in_for_a2_into_d4_embedding():
    """
    method: orthogonal_complement_in

    Practical classification contract:
    orthogonal complement for a nontrivial embedding A2 -> D4 has positive rank.
    """
    source: Lattice = Lattice.A(2)
    target: Lattice = Lattice.D(4)
    comp: Lattice = source.orthogonal_complement_in(target)
    assert_equal(comp.rank(), 2, f"Expected rank-2 orthogonal complement for A2 in D4 contract example: comp={comp}")


def test_discriminant_form_isotropic_subgroups_returns_glue_data():
    """
    method: isotropic_subgroups

    Practical classification contract:
    isotropic-subgroup enumeration on discriminant form returns typed glue data.
    """
    disc_u: LatticeDiscriminantGroup = Lattice.A(2).discriminant()
    glue_candidates: tuple[LatticeGlueData, ...] = disc_u.isotropic_subgroups()
    assert_equal(len(glue_candidates), 1, f"Expected one isotropic-subgroup datum in contract model: {glue_candidates}")
    glue0 = glue_candidates[0]
    gens = glue0.subgroup_generators()
    assert_equal(glue0.is_isotropic(), True, f"Contract glue datum should be isotropic: glue={glue0}")
    assert_equal(len(gens), 1, f"Expected one nontrivial isotropic-subgroup generator in contract model: glue={glue0}")
    assert_equal(gens[0].order(), 3, f"Expected order-3 generator in contract model: generator={gens[0]}")


def test_lattice_overlattice_from_glue_roundtrip_on_nontrivial_glue():
    """
    method: overlattice_from_glue

    Practical classification contract:
    applying nontrivial glue datum over A2 returns a contract overlattice witness.
    """
    u: Lattice = Lattice.A(2)
    disc_u: LatticeDiscriminantGroup = u.discriminant()
    nontrivial_glue: LatticeGlueData = disc_u.isotropic_subgroups()[0]
    over_u: Lattice = u.overlattice_from_glue(nontrivial_glue)

    assert_equal(over_u.is_isometric(Lattice.D(4)), True, f"Expected contract glued lattice to match D4 witness: over={over_u}")


def test_lattice_glue_data_inverse_direction_contract():
    """
    method: glue_data

    Practical classification contract:
    glue-data extraction from an overlattice produces isotropic glue compatible with base discriminant form.
    """
    u: Lattice = Lattice.A(2)
    disc_u: LatticeDiscriminantGroup = u.discriminant()
    nontrivial_glue: LatticeGlueData = disc_u.isotropic_subgroups()[0]
    over_u: Lattice = u.overlattice_from_glue(nontrivial_glue)
    recovered: LatticeGlueData = u.glue_data(over_u)

    assert_equal(recovered.is_isotropic(), True, f"Recovered glue should be isotropic: recovered={recovered}")
    assert_equal(
        recovered.base_discriminant_form().is_isomorphic(disc_u),
        True,
        "Recovered glue must reference base discriminant form isomorphic to the starting one",
    )


def test_lattice_overlattices_lists_concrete_small_candidates():
    """
    method: overlattices

    Practical classification contract:
    overlattice enumeration contains expected nontrivial candidate for A2 contract data.
    """
    u: Lattice = Lattice.A(2)
    candidates: tuple[Lattice, ...] = u.overlattices()
    assert_equal(len(candidates), 2, f"Expected two overlattice candidates in nontrivial contract model: {candidates}")
    n_d4 = sum(1 for c in candidates if c.is_isometric(Lattice.D(4)))
    assert_equal(n_d4, 1, f"Expected exactly one D4-type overlattice witness: candidates={candidates}")
