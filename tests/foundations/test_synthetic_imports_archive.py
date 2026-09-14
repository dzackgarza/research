r"""Retire the archive's synthetic Sage-import cache at the live session boundary.

``archives/preamble/symbols.py`` was editor/tooling infrastructure: it asked Sage
which import statement would bind a global name, cached that string in sqlite,
and assembled synthetic import blocks for lowered Python.  It did not own a
mathematical object.  The live preamble exposes the mathematical session names
directly through :mod:`dzack_research.preamble.all`, so archive reconciliation
keeps the public mathematical consumer and does not recreate the synthetic-import
cache.
"""

from dzack_research.preamble.all import QQ, PolynomialRing, matrix

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/symbols.py",
    "live_owner": "src/dzack_research/preamble/all.py",
    "disposition": "reconciled-live-owner",
}


def test_public_session_names_need_no_synthetic_import_block() -> None:
    ring = PolynomialRing(QQ, "u")
    u = ring.gen()
    operator = matrix([[u, ring.one()], [ring.zero(), u + 1]])

    assert operator.trace() == 2 * u + 1
    assert operator.det() == u * (u + 1)
