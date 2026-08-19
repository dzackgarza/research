"""Line-bundle pullback and base-change compatibility for supported spaces."""

from sage.all import QQ, ProjectiveSpace


def test_projection_pullback_matches_multiindices() -> None:
    """Pulling back divisors along projections preserves multigrading."""
    P1_x = ProjectiveSpace(QQ, 1, names=("x0", "x1"))
    P1_y = ProjectiveSpace(QQ, 1, names=("y0", "y1"))
    X = P1_x * P1_y
    x0, x1, _, _ = X.gens()

    projection = X.hom((x0, x1), P1_x)
    pulled = P1_x.O(2).pullback(projection)

    assert pulled == X.O(2, 0)
    assert pulled.H(0).dimension() == 3

    pulled_sections = P1_x.O(2).H(0).pullback(projection)
    assert pulled_sections.domain() is P1_x.O(2).H(0)
    assert pulled_sections.codomain() == pulled.H(0)
    assert pulled_sections.rank() == 3


def test_identity_base_change_is_faithful_on_schemes_and_bundles() -> None:
    """Base-change along the base identity preserves dimension and bundle data."""
    P2 = ProjectiveSpace(QQ, 2, names=("z0", "z1", "z2"))
    scheme = P2
    base_change = scheme.base_scheme().identity_morphism()
    scheme_bc = scheme.base_change(base_change)
    line_bundle_bc = scheme.O(1).base_change(base_change)

    assert scheme_bc.dimension() == scheme.dimension()
    assert scheme_bc.dimension_relative() == scheme.dimension_relative()
    assert line_bundle_bc.bidegree() == (1,)
