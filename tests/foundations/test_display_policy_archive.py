r"""Reconcile the archive's implicit formatter with object-owned rich display.

``archives/preamble/display.py`` installed one global IPython ``text/latex``
formatter for every object.  The live policy deliberately does not recreate
that global hook: mathematical objects that have a LaTeX representation own
it themselves, while other rich views are explicit object methods.
"""

from dzack_research.preamble.all import Lattices, ZZ


ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/display.py",
    "live_owner": "src/dzack_research/preamble/categories/_lattice.py",
    "disposition": "reconciled-live-owner",
}


def test_lattice_elements_own_their_latex_without_a_global_formatter() -> None:
    lattice = Lattices(ZZ)("A2")
    root = lattice.module_generator(0)

    rendered = root._latex_()
    assert isinstance(rendered, str)
    assert rendered
