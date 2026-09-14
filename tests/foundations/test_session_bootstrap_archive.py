r"""Reconcile the archived Sage startup/installer with the live session import.

``archives/preamble/install.sage`` existed to load the preamble once, cache the
exported objects, and re-export the same identities into later namespaces.
``archives/preamble/init.sage`` called that installer from Sage startup and also
carried session side effects (implicit display, Julia startup) that are no longer
part of the mathematical session contract.  The live entrypoint is the ordinary
Python import surface ``dzack_research.preamble.all``.
"""


ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/init.sage",
        "live_owner": "src/dzack_research/preamble/all.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/install.sage",
        "live_owner": "src/dzack_research/preamble/all.py",
        "disposition": "reconciled-live-owner",
    },
)


def test_repeated_session_imports_reuse_the_same_owned_objects() -> None:
    first: dict[str, object] = {}
    second: dict[str, object] = {}

    exec("from dzack_research.preamble.all import *", first)
    exec("from dzack_research.preamble.all import *", second)

    for name in ("Lattices", "ZZ", "QQ"):
        assert first[name] is second[name]
