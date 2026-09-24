r"""The toric ADE pairs ``(Y, C)`` of pure shape and the decomposition of their boundary.

Source: Alexeev--Thompson, *ADE surfaces and their moduli* (2017), Lemma 3.4 and Definitions
3.5--3.6.  ``Y`` is the toric surface of a lattice polygon ``P`` with a distinguished vertex
``p_*``; ``C`` is the invariant divisor of the sides through ``p_*`` and ``C'`` that of the other
sides, so ``C + C'`` is the whole toric boundary and ``K_Y + C + C' ~ 0``; the sides not through
``p_*`` are at lattice distance 2 from it, whence ``L = -2(K_Y + C) ~ 2 C'``.  In type III (the
ADE shapes) ``C`` has exactly two components.
"""

from dzack_research.preamble.all import *


def _blue_component_count(pair):
    surface = pair.log_scheme()
    blue = pair.blue_divisor()
    return sum(surface.weil_multiplicity(blue, ray) for ray in surface.fan().cones(1))


def test_the_sides_through_the_distinguished_vertex_and_the_rest_make_up_the_boundary() -> None:
    r"""``C + C' = sum_rho D_rho`` for the ``A_1``, ``A_2``, ``D_4`` and ``E_6`` pairs."""
    for letter, rank in (("A", 1), ("A", 2), ("D", 4), ("E", 6)):
        pair = ADELogPairs(QQ)(letter, rank)
        surface = pair.log_scheme()

        assert pair.blue_divisor() + pair.complementary_divisor() == surface.toric_boundary_divisor()
        assert pair.blue_divisor() + pair.complementary_divisor() == -surface.canonical_divisor()


def test_an_ade_pair_has_two_sides() -> None:
    r"""In type III the divisor ``C`` has two components, the left and right sides (Def. 3.6)."""
    for letter, rank in (("A", 1), ("D", 4), ("E", 6)):
        assert _blue_component_count(ADELogPairs(QQ)(letter, rank)) == 2


def test_the_distinguished_point_is_a_vertex_of_the_polygon() -> None:
    r"""``p_*`` is a distinguished vertex of ``P`` (Lemma 3.4)."""
    for letter, rank in (("A", 2), ("D", 4), ("E", 6)):
        pair = ADELogPairs(QQ)(letter, rank)

        assert pair.distinguished_point() in pair.polygon().vertices()


def test_the_pair_records_its_dynkin_type() -> None:
    r"""The pair of type ``X_n`` has letter ``X``, rank ``n``, and is not of affine type unless asked."""
    pair = ADELogPairs(QQ)("E", 6)

    assert pair.dynkin_letter() == "E"
    assert pair.dynkin_rank() == 6
    assert not pair.is_affine_type()
    assert ADELogPairs(QQ)("A", 3, affine=True).is_affine_type()
    assert pair.is_base()
    assert not pair.is_cover()
    assert pair.codimension_in_toric_scheme() == 0


def test_the_toric_surface_is_the_one_of_the_normal_fan_of_the_polygon() -> None:
    r"""``Y`` is the polarized toric surface of ``P``, so its fan is the normal fan of ``P``."""
    pair = ADELogPairs(QQ)("D", 4)

    assert pair.log_scheme().fan().is_isomorphic(pair.polygon().normal_fan())


def test_the_pyramid_over_the_polygon_is_a_three_dimensional_cone_over_it() -> None:
    r"""The cone over ``P`` with apex ``(p_*, 2)`` is three-dimensional with one more vertex than ``P``."""
    for letter, rank in (("A", 1), ("D", 4)):
        pair = ADELogPairs(QQ)(letter, rank)
        pyramid = pair.pyramid()

        assert pyramid.dimension() == 3
        assert pyramid.n_vertices() == pair.polygon().n_vertices() + 1
        assert pyramid.is_lattice_polytope()


def test_the_branch_divisor_is_linearly_equivalent_to_twice_the_other_sides() -> None:
    r"""``-2(K_Y + C) ~ 2 C'`` in ``Cl(Y)`` (Lemma 3.4)."""
    pair = ADELogPairs(QQ)("A", 1)
    surface = pair.log_scheme()
    branch = -2 * (surface.canonical_divisor() + pair.blue_divisor())

    assert surface.divisor_class(branch) == surface.divisor_class(2 * pair.complementary_divisor())


def test_the_at21_enhancement_of_a1_is_a_log_pair_on_the_same_surface() -> None:
    r"""The enhancement keeps ``(Y, C)`` and adds the branch data of Lemma 3.4."""
    enhanced = ADELogPairs(QQ).at21("A", 1)

    assert enhanced in ToricLogPairs(QQ)
