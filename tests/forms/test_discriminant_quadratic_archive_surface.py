r"""Archive reconciliation for discriminant quadratic modules.

The live discriminant-module owner keeps quadratic forms separate from their
bilinear polarizations, while retaining normal forms, Brown invariants,
metabolizers and orthogonal automorphisms on the same finite quadratic object.
"""

from dzack_research.preamble.all import ZZ, Lattices

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/torsionform/discriminant_quadratic_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py",
    "disposition": "reconciled-live-owner",
}




def test_archived_quadratic_normalization_and_brown_invariant_remain_form_data() -> None:
    form = Lattices(ZZ)("D4").discriminant_quadratic_form()
    invariant = form.invariant_factor_form()
    jordan = form.p_adic_jordan_form()

    assert invariant.domain() is form
    assert tuple(invariant.codomain().invariants()) == tuple(form.invariants())
    assert jordan.domain() is form
    assert tuple(jordan.codomain().invariants()) == tuple(form.invariants())
    positive, negative = Lattices(ZZ)("D4").signature_pair()
    assert form.brown_invariant() == (int(positive) - int(negative)) % 8
