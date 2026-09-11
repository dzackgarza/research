r"""Archive reconciliation for the graded-algebra category and its product grading."""

from dzack_research.preamble.all import (
    Algebras,
    GradedAlgebras,
    GradedModules,
    QQ,
    TensorAlgebraOn,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/algebras/graded_algebras.sage",
    "live_owner": "src/dzack_research/preamble/categories/algebras/graded_algebras.py",
    "disposition": "reconciled-live-owner",
}


def _tensor_algebra(labels=("x", "y")):
    return TensorAlgebraOn(QQ, finite_ordered_set(labels))


def test_archive_graded_algebras_are_both_algebras_and_graded_modules() -> None:
    category = GradedAlgebras(QQ)

    assert category.is_subcategory(GradedModules(QQ))
    assert category.is_subcategory(Algebras(QQ).Associative().Unital())

    algebra = _tensor_algebra()
    assert algebra in category
    assert algebra.grading_monoid() is category.grading_monoid()


def test_archive_product_adds_degrees() -> None:
    algebra = _tensor_algebra()
    x = algebra.algebra_generator("x")
    y = algebra.algebra_generator("y")

    assert algebra.homogeneous_degree(x) == 1
    assert algebra.homogeneous_degree(y) == 1
    assert algebra.homogeneous_degree(x * y) == algebra.combine_degrees(1, 1)
    assert algebra.homogeneous_degree(x * y) == 2


def test_archive_graded_morphism_preserves_the_product_grading() -> None:
    source = _tensor_algebra(("x", "y"))
    target = _tensor_algebra(("u", "v"))
    morphism = GradedAlgebras(QQ).Mor(source, target)(
        {
            "x": target.algebra_generator("v"),
            "y": target.algebra_generator("u"),
        }
    )

    x = source.algebra_generator("x")
    y = source.algebra_generator("y")
    image = morphism(x * y)
    assert image == target.algebra_generator("v") * target.algebra_generator("u")
    assert target.homogeneous_degree(image) == source.homogeneous_degree(x * y)
