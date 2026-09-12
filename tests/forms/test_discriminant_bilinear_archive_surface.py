r"""Archive reconciliation for discriminant bilinear modules.

The archived category has been absorbed into the live discriminant-module
owner.  The live object keeps the source/dual lattice and finite pairing, and
its normalization, orthogonal-group, Pontryagin-duality and quadratic-refinement
operations remain operations of that same mathematical object.
"""

from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.modules.framed.formed.discriminant_modules import (
    DiscriminantBilinearModules,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/torsionform/discriminant_bilinear_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_bilinear_discriminant_surface_is_the_live_lattice_discriminant() -> None:
    lattice = Lattices(ZZ)("A2")
    form = lattice.discriminant_bilinear_form()

    assert form in DiscriminantBilinearModules(ZZ)
    assert form.source_lattice() is lattice
    assert form.dual_lattice() is lattice.dual_lattice()
    assert form.cardinality() == 3
    assert form.associated_quadratic_form() is lattice.discriminant_quadratic_form()
    assert form.O() is form.orthogonal_group()


def test_archived_normalizations_and_pontryagin_identification_retain_maps() -> None:
    form = Lattices(ZZ)("D4").discriminant_bilinear_form()
    invariant = form.invariant_factor_form()
    jordan = form.p_adic_jordan_form()
    duality = form.pontryagin_dual_identification()

    assert invariant.domain() is form
    assert tuple(invariant.codomain().invariants()) == tuple(form.invariants())
    assert jordan.domain() is form
    assert tuple(jordan.codomain().invariants()) == tuple(form.invariants())
    assert duality.domain() is form
