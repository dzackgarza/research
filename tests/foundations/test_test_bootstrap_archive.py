r"""Reconcile archived pytest bootstrap modules with the live root harness.

The archived root conftest installed the preamble before test-module import, and
the archived framework conftest autoloaded a projective extension layer.  The
live suite has one root harness that imports the closed ``preamble.all`` surface;
framework tests use that public surface directly, so no subtree autoload hook
remains.
"""

from pathlib import Path


ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/tests/conftest.py",
        "live_owner": "tests/conftest.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/tests/framework/conftest.py",
        "live_owner": "tests/conftest.py",
        "disposition": "reconciled-live-owner",
    },
)


def test_live_root_harness_owns_session_bootstrap_without_framework_autoload() -> None:
    source = Path("tests/conftest.py").read_text()

    assert "from dzack_research.preamble.all import *" in source
    assert "projective_framework_loader" not in source
    assert "load_projective_framework" not in source
