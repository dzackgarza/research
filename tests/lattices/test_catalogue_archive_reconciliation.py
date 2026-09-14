r"""Reconcile ``archives/preamble/catalogue.sage`` with the live catalogue."""

from dzack_research.preamble.all import (
    Embeddings,
    Involutions,
    Lattices,
    NamedLattices,
    NegativeDefTwoElementary,
    TwoElementary,
    signature_orthogonal_sums,
    signature_pair,
    two_elementary_orthogonal_sums,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/catalogue.sage",
    "live_owner": "src/dzack_research/preamble/catalogue.py",
    "disposition": "reconciled-live-owner",
    "owner_overrides": {
        "Lattices": "src/dzack_research/preamble/categories/lattices.py",
    },
}


def test_two_elementary_catalogues_and_searches_retain_the_archive_mathematics() -> None:
    assert TwoElementary.cardinality() == 75
    assert NegativeDefTwoElementary.cardinality() == 51

    target = TwoElementary[(10, 0, 0)]
    candidates = two_elementary_orthogonal_sums(signature_pair(1, 9), 0, 0)
    assert candidates.cardinality() == 1
    candidate = candidates[0]
    assert candidate.gram_tensor().is_equal_tensor(target.gram_tensor())

    repeated = signature_orthogonal_sums(
        signature_pair(0, 2), (NamedLattices.A1,)
    )
    assert repeated.cardinality() == 1
    assert repeated[0].gram_tensor().is_equal_tensor(
        (NamedLattices.A1 + NamedLattices.A1).gram_tensor()
    )


def test_named_k3_involutions_retain_the_archived_block_actions() -> None:
    generators = NamedLattices.LK3.module_generators()
    identity = NamedLattices.LK3.Aut().one()

    assert Involutions.I_dP * Involutions.I_dP == identity
    assert Involutions.I_En * Involutions.I_En == identity
    assert Involutions.I_Nik * Involutions.I_Nik == identity

    assert Involutions.I_dP(generators[0]) == -generators[0]
    assert Involutions.I_dP(generators[2]) == generators[4]
    assert Involutions.I_dP(generators[6]) == -generators[6]

    assert Involutions.I_En(generators[0]) == -generators[0]
    assert Involutions.I_En(generators[2]) == generators[4]
    assert Involutions.I_En(generators[6]) == generators[14]
    assert Involutions.I_En(generators[14]) == generators[6]

    assert Involutions.I_Nik(generators[0]) == generators[0]
    assert Involutions.I_Nik(generators[6]) == -generators[14]
    assert Involutions.I_Nik(generators[14]) == -generators[6]


def test_primitive_embedding_chain_retains_the_archived_generator_maps() -> None:
    tco = NamedLattices.Tco.module_generators()
    ten = NamedLattices.TEn.module_generators()
    tdp = NamedLattices.TdP.module_generators()

    assert Embeddings.TCo_into_TEn(tco[0]) == ten[0] + ten[1]
    assert Embeddings.TCo_into_TEn(tco[1]) == ten[2]
    assert Embeddings.TCo_into_TEn(tco[2]) == ten[3]

    assert Embeddings.TEn_into_TdP(ten[0]) == tdp[0]
    assert Embeddings.TEn_into_TdP(ten[1]) == tdp[1]
    assert Embeddings.TEn_into_TdP(ten[2]) == tdp[2]
    assert Embeddings.TEn_into_TdP(ten[3]) == tdp[3]
    for index in range(8):
        assert Embeddings.TEn_into_TdP(ten[4 + index]) == (
            tdp[4 + index] + tdp[12 + index]
        )

    assert Embeddings.TEn_into_LK3 == Embeddings.TdP_into_LK3 * Embeddings.TEn_into_TdP
    for embedding in (
        Embeddings.TCo_into_TEn,
        Embeddings.TEn_into_TdP,
        Embeddings.TdP_into_LK3,
        Embeddings.U_E8_2_into_TEn,
    ):
        assert embedding.is_primitive()


def test_archived_lattices_reexport_is_the_live_owned_lattice_category() -> None:
    assert Lattices(Embeddings.TCo_into_TEn.domain().base_ring()) is Lattices(
        NamedLattices.Tco.base_ring()
    )
