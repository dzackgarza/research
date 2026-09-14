from pathlib import Path

from sage.rings.integer_ring import ZZ as SageZZ

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


def test_session_ZZ_is_owned_and_builds_the_owned_free_module() -> None:
    session = _session()
    integers = session["ZZ"]

    assert integers is not SageZZ
    module = integers**3
    assert module.base_ring() is integers
    assert module.module_generating_set().cardinality() == 3
    assert module is not SageZZ**3


def test_session_integer_literals_land_back_in_the_owned_integer_ring() -> None:
    session = _session()
    integers = session["ZZ"]
    integer = session["Integer"](7)

    assert integer.parent() is integers
    assert integer == integers(7)


def test_session_load_restores_owned_ring_bindings_after_sage_import(tmp_path: Path) -> None:
    session = _session()
    integers = session["ZZ"]
    before = integers**3
    script = tmp_path / "imports_sage.sage"
    script.write_text("from sage.all import *\narchive_session_marker = 1\n")

    session["load"](str(script), session)

    assert session["archive_session_marker"] == 1
    assert session["ZZ"] is integers
    assert session["ZZ"]**3 is before
    assert session["ZZ"] is not SageZZ


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
