"""Archive reconciliation for finitely presented algebras."""

from dzack_research.preamble.all import QQ, Sets
from dzack_research.preamble.categories.algebras.algebras import (
    AlgebrasWithChosenFinitePresentation,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/algebras/finitely_presented_algebras.sage",
    "live_owner": "src/dzack_research/preamble/categories/algebras/algebras.py",
    "owner_overrides": {
        "FinitelyPresentedAlgebras.ParentMethods.framing_morphism": "src/dzack_research/preamble/categories/modules/module_morphisms/module_morphisms.py",
    },
    "disposition": "reconciled-live-owner",
}


def test_archived_finite_presentation_retains_ring_relations_and_generators() -> None:
    presentation = QQ.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    algebra = (presentation).quotient_by_relations((x * y,))

    assert algebra in AlgebrasWithChosenFinitePresentation(QQ)
    assert algebra.presentation_ring() is presentation
    relations = algebra.relations()
    assert relations.index_set() is Sets.Δ[0]
    assert relations.value(relations.index_set()[0]) == x * y

    projection = algebra.algebra_presentation_morphism()
    assert projection is algebra.algebra_presentation_morphism()
    assert projection.domain() is presentation
    assert projection.codomain() is algebra
    assert projection(x * y) == algebra.zero()

    generator_map = algebra.algebra_generator_morphism()
    assert generator_map("x") == algebra.algebra_generator("x")
    assert generator_map("y") == algebra.algebra_generator("y")


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


def test_selected_finite_presentation_constructor_is_owned_by_its_presentation() -> None:

    presentation = QQ.polynomial_ring(("x", "y"))
    x = presentation.algebra_generator("x")
    declared = AlgebrasWithChosenFinitePresentation(QQ)(
        presentation,
        (x**2,),
    )
    notation = (presentation).quotient_by_relations((x**2,))

    assert declared in AlgebrasWithChosenFinitePresentation(QQ)
    assert notation in AlgebrasWithChosenFinitePresentation(QQ)
    assert declared.presentation_ring() is presentation
    assert notation.presentation_ring() is presentation
    assert declared.relations() == notation.relations()
