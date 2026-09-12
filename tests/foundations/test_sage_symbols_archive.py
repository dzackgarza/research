r"""Archive reconciliation for exact algebra through the public session symbols."""

from dzack_research.preamble.all import QQ, PolynomialRing, matrix

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/test_sage_symbols.py",
    "live_owner": "src/dzack_research/preamble/all.py",
    "disposition": "reconciled-live-owner",
}


def test_public_session_symbols_support_the_archived_polynomial_matrix_identity() -> None:
    ring = PolynomialRing(QQ, "x")
    x = ring.gen()
    square = matrix([[x, ring.one()], [ring.zero(), x]])

    assert square.det() == x**2
