"""Archive reconciliation for scheme points as morphisms in Sch/S."""

from dzack_research.preamble.all import QQ, AffineSpaces, ProjectiveSpaces, Schemes

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/schemes/scheme_points.sage",
    "live_owner": "src/dzack_research/preamble/categories/schemes/schemes.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_scheme_point_is_an_actual_scheme_morphism() -> None:
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    point = plane.point_morphism([1, 2])
    residue_scheme = (QQ).affine_spectrum()

    assert point.domain() is residue_scheme
    assert point.codomain() is plane
    assert point in Schemes(QQ).Mor(residue_scheme, plane)


def test_scheme_point_composes_with_the_structure_map_over_the_same_base() -> None:
    line = AffineSpaces(QQ)(1, names=("t",))
    point = line.point_morphism([3])
    base = (QQ).affine_spectrum()

    structural_value = line.structure_morphism().evaluate_at(point)
    assert structural_value.domain() is point.domain()
    assert structural_value.codomain() is base
    assert structural_value in Schemes(QQ).Mor(point.domain(), base)


def test_projective_point_retains_owned_noncoordinate_homogeneous_coordinates() -> None:
    plane = ProjectiveSpaces(QQ)(2)
    point = plane.point_morphism((1, 2, 3))
    coordinates = point.point_coordinates()

    assert coordinates.cardinality() == 3
    assert tuple(coordinates) == (QQ(1), QQ(2), QQ(3))
    assert all(coordinate.parent() is QQ for coordinate in coordinates)
    assert point.codomain() is plane
