r"""Archived standard-cardinality facts not already covered by live catalogues."""

from dzack_research.preamble.all import (
    QQ,
    RR,
    MatrixSpace,
    PolynomialRing,
    PowerSeriesRing,
    aleph0,
    continuum,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/sets/cardinals.py",
    "live_owner": "src/dzack_research/preamble/categories/sets/cardinals.py",
    "disposition": "reconciled-live-owner",
}


def test_matrix_ring_cardinality_tracks_the_coefficient_ring() -> None:
    rational_matrices = MatrixSpace(QQ, 2)
    real_matrices = MatrixSpace(RR, 2)

    assert rational_matrices.cardinality() == aleph0
    assert real_matrices.cardinality() == continuum


def test_rational_power_series_have_continuum_cardinality() -> None:
    power_series = PowerSeriesRing(QQ, "t")

    assert power_series.cardinality() == continuum


def test_rational_polynomial_ring_is_countable() -> None:
    polynomial = PolynomialRing(QQ, "x")

    assert polynomial.cardinality() == aleph0
