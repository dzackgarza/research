"""Complete linear systems and finite restriction maps on divisors."""

from sage.all import QQ, ProjectiveSpace


def test_complete_linear_system_image_and_base_locus():
    """Complete linear systems on bigrids have expected dimension and basepoint data."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    L = X.O(4, 4)

    system = L.complete_linear_system()
    morphism = system.morphism()

    assert system.dimension() == 24
    assert system.is_complete()
    assert system.is_basepoint_free()
    assert system.base_locus().defining_ideal().is_one()
    assert morphism.codomain().dimension_relative() == 24
    assert morphism.domain() is X
    assert morphism.codomain().O(1).pullback(morphism) == L


def test_restriction_map_has_expected_rank_and_cokernel():
    """Restriction to a complete-intersection curve has predictable linear-algebra size."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, y0, y1 = X.gens()

    P = X.O(2, 2)
    Z = X.subscheme([x0 * y0, x1 * y1])
    embedding = Z.embedding_morphism()
    P_on_Z = P.pullback(embedding)
    restriction = P.H(0).pullback(embedding)

    assert P_on_Z.source_line_bundle() is P
    assert restriction.base_morphism() is embedding
    assert restriction.domain() is P.H(0)
    assert restriction.codomain().dimension() == 4
    assert restriction.rank() == 4
    assert restriction.kernel().dimension() == 5
    assert restriction.cokernel().dimension() == 0
