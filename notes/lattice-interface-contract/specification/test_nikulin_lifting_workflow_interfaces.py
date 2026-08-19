from __future__ import annotations

import pytest

pytestmark = pytest.mark.tdd_red

from .conftest import assert_equal
from .types import (
    DiscriminantFormIsometry,
    DiscriminantOrthogonalGroup,
    Lattice,
    LatticeGlueData,
    LatticeOrthogonalSubgroup,
    LatticePrimitiveEmbedding,
    LatticeAutomorphism,
)


def test_lattice_direct_sum_and_glued_construction_interfaces():
    """
    method: direct_sum

    Gluing-workflow contract:
    interface exposes direct-sum construction and glued-model recognition.
    """
    u: Lattice = Lattice.A(2)
    two_u: Lattice = u.direct_sum(u)
    disc_u = u.discriminant()
    glue: LatticeGlueData = disc_u.isotropic_subgroups()[0]

    assert_equal(two_u.rank(), 4, f"Expected rank(A2⊕A2)=4 in contract example: rank={two_u.rank()}")
    assert_equal(
        two_u.is_glued_from(u, u, glue),
        True,
        f"Expected direct sum model to be recognized as glue realization in nontrivial A2 case: lattice={two_u}",
    )


def test_lattice_primitive_complement_and_embedding_glue_isometry_interfaces():
    """
    method: primitive_complement_in

    Embedding-workflow contract:
    primitive embeddings expose complements and their discriminant-form glue isometries.
    """
    u: Lattice = Lattice.A(2)
    target: Lattice = Lattice.D(4)
    embeddings: tuple[LatticePrimitiveEmbedding, ...] = u.primitive_embeddings(target)
    emb: LatticePrimitiveEmbedding = embeddings[0]
    comp: Lattice = u.primitive_complement_in(target, embedding=emb)
    glue_iso: DiscriminantFormIsometry = emb.glue_isometry()

    assert_equal(comp.rank(), 2, f"Expected rank-2 primitive complement for A2 in D4 contract example: comp={comp}")
    assert_equal(
        glue_iso.is_anti_isometry(),
        True,
        "Expected primitive-embedding glue map to be represented as anti-isometry in contract interface",
    )


def test_lattice_discriminant_automorphism_image_interface():
    """
    method: automorphism_group_on_discriminant

    Automorphism-workflow contract:
    image of lattice isometries in O(A_L) is explicitly queryable.
    """
    u: Lattice = Lattice.hyperbolic(rank=3)
    root = u.vinberg().simple_roots()[0]
    nontrivial_isometry: LatticeAutomorphism = u.reflection(root)
    image_default: DiscriminantOrthogonalGroup = u.automorphism_group_on_discriminant()
    subgroup: LatticeOrthogonalSubgroup = u.orthogonal_set_stabilizer([u.element((1, 0, 0))])
    image_subgroup: DiscriminantOrthogonalGroup = u.automorphism_group_on_discriminant(subgroup=subgroup)

    assert_equal(
        image_default.contains(nontrivial_isometry),
        True,
        "Image of O(L) in O(A_L) should contain nontrivial reflection witness",
    )
    assert_equal(
        image_subgroup.contains(nontrivial_isometry),
        True,
        "Image of subgroup in O(A_L) should contain nontrivial reflection witness",
    )


def test_lattice_glue_compatibility_and_lift_decision_interfaces():
    """
    method: automorphism_lifts_to_overlattice

    Lifting-workflow contract:
    liftability decision is exposed independently for a fixed gluing context.
    """
    u: Lattice = Lattice.hyperbolic(rank=3)
    root = u.vinberg().simple_roots()[1]
    nontrivial_isometry: LatticeAutomorphism = u.reflection(root)
    glue: LatticeGlueData = Lattice.A(2).discriminant().isotropic_subgroups()[0]

    assert_equal(
        u.automorphism_lifts_to_overlattice(nontrivial_isometry, Lattice.D(4), glue),
        True,
        "Nontrivial reflection automorphism should be liftable in contract case",
    )


def test_lattice_lift_construction_and_liftable_subgroup_interfaces():
    """
    method: extend_automorphism_to_overlattice

    Lifting-workflow contract:
    interface provides both explicit lift construction and subgroup-level liftability filter.
    """
    u: Lattice = Lattice.hyperbolic(rank=3)
    root = u.vinberg().simple_roots()[0]
    nontrivial_isometry: LatticeAutomorphism = u.reflection(root)
    glue: LatticeGlueData = Lattice.A(2).discriminant().isotropic_subgroups()[0]

    lifted: LatticeAutomorphism = u.extend_automorphism_to_overlattice(nontrivial_isometry, Lattice.D(4), glue)
    liftable: LatticeOrthogonalSubgroup = u.liftable_automorphisms(Lattice.D(4), glue)

    assert_equal(lifted in liftable, True, "Lifted automorphism should belong to liftable subgroup")


def test_lattice_glue_compatibility_nontrivial_pair():
    """
    method: glue_compatibility

    Lifting-workflow contract:
    nontrivial automorphisms on summands can satisfy glue compatibility.
    """
    u: Lattice = Lattice.hyperbolic(rank=3)
    root = u.vinberg().simple_roots()[1]
    nontrivial_isometry: LatticeAutomorphism = u.reflection(root)
    glue: LatticeGlueData = Lattice.A(2).discriminant().isotropic_subgroups()[0]
    assert_equal(
        u.glue_compatibility(nontrivial_isometry, nontrivial_isometry, glue),
        True,
        "Nontrivial summand automorphisms should satisfy glue compatibility in contract example",
    )


def test_lattice_structured_automorphism_lifting_result_interface():
    """
    method: automorphism_lifting_result

    Lifting-workflow contract:
    theorem decision can be returned as structured data with boolean, witness, and obstruction.
    """
    u: Lattice = Lattice.hyperbolic(rank=3)
    root = u.vinberg().simple_roots()[0]
    nontrivial_isometry: LatticeAutomorphism = u.reflection(root)
    glue: LatticeGlueData = Lattice.A(2).discriminant().isotropic_subgroups()[0]

    result: tuple[bool, LatticeAutomorphism | None, str | None] = u.automorphism_lifting_result(
        nontrivial_isometry,
        Lattice.D(4),
        glue,
    )
    lifts, witness, obstruction = result
    liftable: LatticeOrthogonalSubgroup = u.liftable_automorphisms(Lattice.D(4), glue)
    assert_equal(lifts, True, f"Expected nontrivial reflection to be liftable in contract example: result={result}")
    assert_equal(obstruction, None, f"Expected no obstruction for nontrivial liftable example: result={result}")
    assert_equal(
        witness in liftable,
        True,
        f"Expected witness to be an element of the liftable subgroup: result={result}",
    )
