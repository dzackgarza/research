r"""Sections of O(1) on P^2 split into three one-dimensional toric weights."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_sections_of_o_one_on_projective_plane() -> None:
    plane = RationalPolyhedralFans(ZZ.free_module(2)).projective_space_fan().toric_variety(QQ)
    cohomology = plane.line_bundle_cohomology(plane.hyperplane_divisor(), 0)

    assert cohomology in ToricGeometricLineBundleCohomologySpaces(QQ)
    assert cohomology.dimension() == 3
    assert cohomology.cohomology_weight_support().cardinality() == cardinal(3)
    assert all(
        cohomology.cohomology_weight_piece(weight).dimension() == 1
        for weight in cohomology.cohomology_weight_support()
    )
    for weight in cohomology.cohomology_weight_support():
        piece = cohomology.cohomology_weight_piece(weight)
        inclusion = cohomology.cohomology_weight_inclusion(weight)
        projection = cohomology.cohomology_weight_projection(weight)
        assert inclusion.domain() is piece
        assert inclusion.codomain() is cohomology
        assert projection.domain() is cohomology
        assert projection.codomain() is piece
        assert projection * inclusion == piece.Mor(piece).identity()
