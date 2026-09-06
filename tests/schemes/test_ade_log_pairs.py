r"""ADE log pairs: the integral polygon, its toric base, and the blue divisor.

The polygon table is the one recorded in the archived preamble, whose stated
source is Table 1 of Alexeev--Thompson, *ADE surfaces and their moduli*.  The
assertions below are about what the table then produces: which toric surface
the normal fan gives, how the toric boundary splits at the distinguished
point, and whether the pyramid over the polygon is integral.
"""

from dzack_research.preamble.all import (
    ADELogPair,
    ADELogPairs,
    LogPairs,
    QQ,
    ToricLogPairs,
)


def test_the_a_one_polygon_has_the_projective_plane_as_its_toric_base() -> None:
    r"""``Q`` is the triangle on ``(0,2)``, ``(0,0)``, ``(2,0)``, whose inner
    normal fan has rays ``e_1``, ``e_2`` and ``-e_1-e_2``."""
    pair = ADELogPair("A", 1, QQ)

    assert pair in ADELogPairs(QQ)
    assert pair in ToricLogPairs(QQ)
    assert pair in LogPairs(QQ)
    assert pair.dynkin_letter() == "A"
    assert pair.dynkin_rank() == 1
    assert not pair.is_affine_type()
    assert pair.polygon().vertices().cardinality() == 3
    assert pair.log_scheme().is_projective_space()
    assert pair.is_log_calabi_yau()


def test_the_boundary_splits_into_the_blue_divisor_and_its_complement() -> None:
    r"""``p* = (0,2)`` is a vertex of the ``A_1`` triangle, so it lies on two of
    the three sides and exactly two of the three invariant divisors are blue."""
    pair = ADELogPair("A", 1, QQ)
    blue = pair.blue_divisor()
    complementary = pair.complementary_divisor()
    group = pair.boundary_divisor_group()

    assert blue + complementary == pair.boundary_divisor()
    assert blue != group.zero()
    assert complementary != group.zero()
    assert blue != pair.boundary_divisor()


def test_the_d_four_polygon_has_a_quadric_surface_as_its_toric_base() -> None:
    r"""``Q`` is the square ``[0,2]^2``, whose normal fan is the fan of
    ``P^1 x P^1``, the Hirzebruch surface ``F_0``."""
    pair = ADELogPair("D", 4, QQ)

    assert pair.polygon().vertices().cardinality() == 4
    assert pair.log_scheme().is_hirzebruch_surface(0)
    assert not pair.log_scheme().is_projective_space()
    assert pair.log_scheme().torus_invariant_divisor_group().module_generating_set().cardinality() == 4


def test_the_unadorned_a_family_carries_two_long_white_sides() -> None:
    pair = ADELogPair("A", 3, QQ)
    decorations = pair.side_decorations()

    assert decorations.cardinality() == 2
    for position in decorations.index_set():
        assert decorations[position].length_class == "long"
        assert decorations[position].vertex_colour == "white"


def test_a_short_variant_decorates_one_side_differently() -> None:
    plain = ADELogPair("A", 3, QQ)
    right_short = ADELogPair("A", 3, QQ, variant=("long", "short"))
    decorations = right_short.side_decorations()

    assert decorations.cardinality() == 2
    assert decorations[1].length_class == "short"
    assert decorations[1].vertex_colour == "black"
    assert plain.polygon().normalized_volume() == 8
    assert right_short.polygon().normalized_volume() == 6


def test_the_pyramid_over_a_finite_type_polygon_is_a_lattice_polytope() -> None:
    r"""The apex is ``(p*, 2)``, integral exactly when ``p*`` is."""
    pair = ADELogPair("A", 1, QQ)
    pyramid = pair.pyramid()

    assert pyramid.dimension() == 3
    assert pyramid.is_lattice_polytope()
    assert pair.cover_toric_threefold().dimension() == 3


def test_the_affine_a_family_places_the_apex_at_a_half_integral_point() -> None:
    r"""``p* = (n/2, 1)`` for the affine ``A`` family, so the pyramid over the
    polygon is rational rather than integral and carries no toric threefold."""
    pair = ADELogPair("A", 3, QQ, affine=True)

    assert pair.is_affine_type()
    assert pair.polygon().vertices().cardinality() == 4
    assert not pair.pyramid().is_lattice_polytope()


def test_the_coxeter_diagram_of_a_finite_type_has_one_vertex_per_rank() -> None:
    assert ADELogPair("A", 3, QQ).coxeter_diagram().cardinality() == 3
    assert ADELogPair("E", 6, QQ).coxeter_diagram().cardinality() == 6


def test_the_polarizing_polytope_of_the_toric_base_is_the_ade_polygon() -> None:
    pair = ADELogPair("E", 6, QQ)

    assert pair.log_scheme().is_polarized()
    assert pair.log_scheme().polarizing_polytope() is pair.polygon()
    assert pair.polygon().normalized_volume() > 0
