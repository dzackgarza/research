"""Archive reconciliation for finitely presented algebras."""

from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras.algebras import (
    AlgebrasWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/algebras/finitely_presented_algebras.sage",
    "live_owner": "src/dzack_research/preamble/categories/algebras/algebras.py",
    "owner_overrides": {
        "FinitelyPresentedAlgebra": "src/dzack_research/preamble/categories/algebras/free_algebras.py",
        "FinitelyPresentedAlgebras.ParentMethods.framing_morphism": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_archived_finite_presentation_retains_ring_relations_and_generators() -> None:
    presentation = PolynomialRing(QQ, ("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    algebra = FinitelyPresentedAlgebra(presentation, (x * y,))

    assert algebra in AlgebrasWithChosenFinitePresentation(QQ)
    assert algebra.presentation_ring() is presentation
    assert tuple(algebra.relations()) == (x * y,)

    projection = algebra.algebra_presentation_morphism()
    assert projection.domain() is presentation
    assert projection.codomain() is algebra
    assert projection(x * y) == algebra.zero()

    generator_map = algebra.algebra_generator_morphism()
    assert generator_map("x") == algebra.algebra_generator("x")
    assert generator_map("y") == algebra.algebra_generator("y")


def test_archived_presented_algebra_morphism_is_determined_by_generator_images() -> None:
    presentation = PolynomialRing(QQ, ("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    algebra = FinitelyPresentedAlgebra(presentation, (x * y,))
    xbar = algebra.algebra_generator("x")
    ybar = algebra.algebra_generator("y")

    swap = algebra.Mor(algebra)({"x": ybar, "y": xbar})
    assert swap(xbar) == ybar
    assert swap(ybar) == xbar
    assert swap(xbar * ybar) == algebra.zero()
