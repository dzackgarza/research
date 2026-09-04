from dzack_research.preamble.all import (
    NamedLattices,
    NegativeDefTwoElementary,
    nikulin_invariants,
    signature_pair,
    two_elementary_orthogonal_sums,
)


def test_delta_distinguishes_coeven_and_coodd_discriminant_forms() -> None:
    assert NamedLattices.U_2.two_elementary_invariants() == nikulin_invariants(2, 2, 0)
    assert NamedLattices.Z_2.two_elementary_invariants() == nikulin_invariants(1, 1, 1)
    assert NamedLattices.E10_2.two_elementary_invariants() == nikulin_invariants(10, 10, 0)


def test_block_search_recovers_the_hand_counted_rows() -> None:
    expected_counts = {
        (2, 2, 0): 1,
        (10, 10, 0): 1,
        (10, 10, 1): 3,
    }
    for (rank, length, delta), expected in expected_counts.items():
        candidates = two_elementary_orthogonal_sums(
            signature_pair(1, rank - 1), length, delta
        )
        assert candidates.cardinality() == expected
        expected_invariants = nikulin_invariants(rank, length, delta)
        assert all(
            candidate.two_elementary_invariants() == expected_invariants
            for candidate in candidates
        )


def test_the_negative_definite_table_has_fifty_one_rows() -> None:
    assert NegativeDefTwoElementary.cardinality() == 51


def test_starred_row_retains_its_live_gluing_inclusion() -> None:
    glued = NegativeDefTwoElementary[(8, 6, 0)][0]
    inclusion = glued._catalogue_glue_inclusion
    assert inclusion.domain().two_elementary_invariants() == nikulin_invariants(8, 8, 1)
    assert inclusion.codomain() is glued
    assert inclusion.index() == 2
