r"""ADE log pairs: the integral polygon, its toric base, and the blue divisor.

The polygon table is the one recorded in the archived preamble, whose stated
source is Table 1 of Alexeev--Thompson, *ADE surfaces and their moduli*.  The
assertions below are about what the table then produces: which toric surface
the normal fan gives, how the toric boundary splits at the distinguished
point, and whether the pyramid over the polygon is integral.
"""

from dzack_research.preamble.all import (
    ADELogPairs,
    LogPairs,
    QQ,
    ToricLogPairs,
)


def test_the_a_one_polygon_has_the_projective_plane_as_its_toric_base() -> None:
    r"""``Q`` is the triangle on ``(0,2)``, ``(0,0)``, ``(2,0)``, whose inner
    normal fan has rays ``e_1``, ``e_2`` and ``-e_1-e_2``."""
    pair = ADELogPairs(QQ)("A", 1)

    assert pair in ADELogPairs(QQ)
    assert pair in ToricLogPairs(QQ)
    assert pair in LogPairs(QQ)
    assert pair.dynkin_letter() == "A"
    assert pair.dynkin_rank() == 1
    assert not pair.is_affine_type()
    assert pair.polygon().vertices().cardinality() == 3
    assert pair.log_scheme().is_projective_space()
    assert pair.is_log_calabi_yau()




def test_the_d_four_polygon_has_a_quadric_surface_as_its_toric_base() -> None:
    r"""``Q`` is the square ``[0,2]^2``, whose normal fan is the fan of
    ``P^1 x P^1``, the Hirzebruch surface ``F_0``."""
    pair = ADELogPairs(QQ)("D", 4)

    assert pair.polygon().vertices().cardinality() == 4
    assert pair.log_scheme().is_hirzebruch_surface(0)
    assert not pair.log_scheme().is_projective_space()
    assert pair.log_scheme().torus_invariant_divisor_group().module_generating_set().cardinality() == 4












