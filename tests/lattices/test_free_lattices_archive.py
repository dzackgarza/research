r"""Archive reconciliation for the finite-rank free-lattice construction."""

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.lattices import FiniteRankLattices, Lattices
from dzack_research.preamble.categories.modules.framed.formed.form_modules import (
    SymmetricBilinearFormModules,
)


ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/free_lattices.sage",
    "live_owner": "src/dzack_research/preamble/categories/lattices.py",
    "disposition": "reconciled-live-owner",
}


def test_gram_constructor_is_the_live_finite_rank_free_lattice() -> None:
    gram = ((ZZ(2), ZZ(1)), (ZZ(1), ZZ(-2)))
    lattice = Lattices(ZZ)(gram)

    assert lattice in Lattices(ZZ)
    assert lattice in FiniteRankLattices(ZZ)
    assert lattice in SymmetricBilinearFormModules(ZZ)
    assert lattice.module_rank() == 2
    assert lattice.gram_matrix()[0, 0] == 2
    assert lattice.gram_matrix()[0, 1] == 1
    assert lattice.gram_matrix()[1, 0] == 1
    assert lattice.gram_matrix()[1, 1] == -2


def test_lattice_form_and_underlying_module_are_the_same_represented_object() -> None:
    lattice = Lattices(ZZ)(((0, 1), (1, 0)))
    form = lattice.form()
    first, second = tuple(lattice.module_generators())

    assert lattice.unformed_module() is lattice
    assert form.module() is lattice
    assert first.parent() is lattice
    assert second.parent() is lattice
    assert form(first, first) == 0
    assert form(first, second) == 1
    assert form(second, second) == 0
