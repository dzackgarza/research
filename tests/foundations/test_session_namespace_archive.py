

ARCHIVE_RECONCILIATIONS = (
    {
        "archive_module": "preamble/tests/test_session_namespace.sage",
        "live_owner": "src/dzack_research/preamble/all.py",
        "disposition": "reconciled-live-owner",
    },
    {
        "archive_module": "preamble/all.py",
        "live_owner": "src/dzack_research/preamble/all.py",
        "disposition": "reconciled-live-owner",
    },
)


def _session() -> dict:
    scope: dict = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope








def test_session_lattice_retains_owned_base_ring_and_form_data() -> None:
    session = _session()
    integers = session["ZZ"]
    lattice = session["Lattices"](integers)("A2")
    first, second = tuple(lattice.module_generators())

    assert lattice.module_rank() == 2
    assert lattice.base_ring() is integers
    assert lattice.is_even()
    assert lattice.is_nondegenerate()
    assert lattice.gram_matrix().determinant() == 3
    assert abs(lattice.b(first, second)) == 1
