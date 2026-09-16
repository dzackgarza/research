r"""A product of schemes is asked of the objects, or taken over an index set.

``X.product_with(Y)`` is the operator spelling of the binary case, where one
argument is distinguished; a product whose index set is part of the
mathematics is taken over that set with ``Schemes(R).product(family)``.
Neither reads an arity.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    AffineSpaces,
    ProjectiveSpaces,
    Schemes,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def test_the_affine_plane_is_the_line_multiplied_by_the_line() -> None:
    line = AffineSpaces(ZZ)(1)
    plane = line.product_with(line)

    assert plane.relative_dimension() == 2
    assert plane.factors().cardinality() == 2
    assert plane.projection(0).codomain() is line
    assert plane.projection(1).codomain() is line


def test_the_quadric_surface_is_the_projective_line_multiplied_by_itself() -> None:
    line = ProjectiveSpaces(QQ)(1)
    quadric = line.product_with(line)

    assert quadric.relative_dimension() == 2
    assert quadric.projection(1).codomain() is line


def test_the_category_takes_the_product_over_a_family_of_three_factors() -> None:
    r"""The same word one level up, over the index set rather than an arity."""
    line = AffineSpaces(QQ)(1)
    space = Schemes(QQ).product((line, line, line))

    assert space.relative_dimension() == 3


def test_repeated_projective_factors_keep_their_named_projection_roles() -> None:
    labels = finite_ordered_set(("left", "right"))
    line = ProjectiveSpaces(QQ)(1)
    family = indexed_family(labels, lambda _label: line, name="Repeated projective factors")

    quadric = Schemes(QQ).product(family)

    assert quadric.factors().index_set() is labels
    assert quadric.projections().index_set() is labels
    assert quadric.factors()["left"] is line
    assert quadric.factors()["right"] is line
    assert quadric.projection("left").codomain() is line
    assert quadric.projection("right").codomain() is line
    assert quadric.projection_label(quadric.projection("left")) == "left"
    assert quadric.projection_label(quadric.projection("right")) == "right"

    point = quadric.point_morphism([1, 2, 3, 4])
    assert quadric.projection("left").evaluate_at(point) == line.point_morphism([1, 2])
    assert quadric.projection("right").evaluate_at(point) == line.point_morphism([3, 4])


def test_named_product_data_does_not_overwrite_an_earlier_product() -> None:
    first_labels = finite_ordered_set(("source", "target"))
    second_labels = finite_ordered_set(("domain", "codomain"))
    line = AffineSpaces(QQ)(1)
    first_family = indexed_family(first_labels, lambda _label: line)
    second_family = indexed_family(second_labels, lambda _label: line)

    first = Schemes(QQ).product(first_family)
    second = Schemes(QQ).product(second_family)

    assert first is not second
    assert first.factors().index_set() is first_labels
    assert second.factors().index_set() is second_labels
    assert first.projections().index_set() is first_labels
    assert second.projections().index_set() is second_labels


def test_projective_product_cone_recovers_both_repeated_factor_legs() -> None:
    labels = finite_ordered_set(("left", "right"))
    line = ProjectiveSpaces(QQ)(1)
    family = indexed_family(labels, lambda _label: line)
    product = Schemes(QQ).product(family)
    identity = line.categorical_identity_morphism()
    legs = indexed_family(labels, lambda _label: identity)

    diagonal = product.from_product_cone(legs)

    assert diagonal.domain() is line
    assert diagonal.codomain() is product
    assert product.projection("left") * diagonal is identity
    assert product.projection("right") * diagonal is identity
