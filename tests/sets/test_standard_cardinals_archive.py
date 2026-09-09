r"""Archived standard-cardinality facts not already covered by live catalogues."""

from dzack_research.preamble.all import MatrixSpace, QQ, RR, aleph0, continuum


def test_matrix_ring_cardinality_tracks_the_coefficient_ring() -> None:
    rational_matrices = MatrixSpace(QQ, 2)
    real_matrices = MatrixSpace(RR, 2)

    assert rational_matrices.cardinality() == aleph0
    assert real_matrices.cardinality() == continuum
