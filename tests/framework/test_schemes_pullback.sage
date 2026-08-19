"""Categorical pullbacks, diagonals, graph morphisms, and fixed loci."""

from sage.all import QQ, ProjectiveSpace


def test_graph_and_fixed_subscheme_for_involution() -> None:
    P1x = ProjectiveSpace(QQ, 1, names=("tx0", "tx1"))
    P1y = ProjectiveSpace(QQ, 1, names=("ty0", "ty1"))
    X = P1x * P1y
    tx0, tx1, ty0, ty1 = X.gens()

    diagonal = X.diagonal_morphism()
    assert diagonal.codomain().dimension() == 2
    assert diagonal.image() == diagonal.codomain()

    involution = X.hom([tx0, -tx1, ty0, -ty1], X)
    graph = involution.graph_morphism()
    fixed = involution.fixed_subscheme()

    assert involution.is_automorphism()
    assert graph.image() == graph.codomain()
    assert graph.image().dimension() == 2
    assert fixed.dimension() == 0
    assert len(fixed.rational_points()) == 4


def test_fiber_pullback_from_projection_is_one_dimensional() -> None:
    P1x = ProjectiveSpace(QQ, 1, names=("px0", "px1"))
    P1y = ProjectiveSpace(QQ, 1, names=("py0", "py1"))
    X = P1x * P1y
    x0, x1, y0, y1 = X.gens()

    projection = X.hom([x0, x1], P1x)
    point = P1x.subscheme([P1x.gens()[1]])
    point_embedding = point.embedding_morphism()
    fiber_square = projection.pullback(point_embedding)

    assert fiber_square.commutes()
    assert fiber_square.left_projection().image().dimension() == 1
