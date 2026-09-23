"""Archive reconciliation for finitely presented algebras."""

from dzack_research.preamble.all import QQ

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/algebras/finitely_presented_algebras.sage",
    "live_owner": "src/dzack_research/preamble/categories/algebras/algebras.py",
    "owner_overrides": {
        "FinitelyPresentedAlgebras.ParentMethods.framing_morphism": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
    },
    "disposition": "reconciled-live-owner",
}




def test_archived_presented_algebra_morphism_is_determined_by_generator_images() -> None:
    presentation = QQ.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    algebra = (presentation).quotient_by_relations((x * y,))
    xbar = algebra.algebra_generator("x")
    ybar = algebra.algebra_generator("y")

    swap = algebra.Mor(algebra)({"x": ybar, "y": xbar})
    assert swap(xbar) == ybar
    assert swap(ybar) == xbar
    assert swap(xbar * ybar) == algebra.zero()


