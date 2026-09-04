from dzack_research.preamble.all import (
    NamedLattices,
    NegativeDefTwoElementary,
    TwoElementary,
    two_elementary_orthogonal_sums,
    validate_negative_def_two_elementary_table,
    validate_two_elementary_table,
)


def test_nikulin_table_has_all_75_rows_with_exact_invariants() -> None:
    assert len(TwoElementary) == 75
    assert validate_two_elementary_table()


def test_delta_distinguishes_coeven_and_coodd_discriminant_forms() -> None:
    assert NamedLattices.U_2.two_elementary_invariants() == (2, 2, 0)
    assert NamedLattices.Z_2.two_elementary_invariants() == (1, 1, 1)
    assert NamedLattices.E10_2.two_elementary_invariants() == (10, 10, 0)


def test_block_search_recovers_the_hand_counted_rows() -> None:
    expected_counts = {
        (2, 2, 0): 1,
        (10, 10, 0): 1,
        (10, 10, 1): 3,
    }
    for (rank, length, delta), expected in expected_counts.items():
        candidates = two_elementary_orthogonal_sums((1, rank - 1), length, delta)
        assert len(candidates) == expected
        assert all(candidate.two_elementary_invariants() == (rank, length, delta) for candidate in candidates)


def test_alexeev_engel_table_rows_have_exact_negative_definite_invariants() -> None:
    assert len(NegativeDefTwoElementary) == 51
    assert validate_negative_def_two_elementary_table()


def test_starred_row_retains_its_live_gluing_inclusion() -> None:
    glued = NegativeDefTwoElementary[(8, 6, 0)][0]
    inclusion = glued._catalogue_glue_inclusion
    assert inclusion.domain().two_elementary_invariants() == (8, 8, 1)
    assert inclusion.codomain() is glued
    assert inclusion.index() == 2
