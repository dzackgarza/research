r"""Archive reconciliation for the elementary affine/projective scheme categories."""

from dzack_research.preamble.all import (
    QQ,
    AffineSpaces,
    ClosedEmbeddings,
    OpenImmersions,
    ProjectiveSpaces,
    Schemes,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/schemes/schemes.sage",
    "live_owner": "src/dzack_research/preamble/categories/schemes/schemes.py",
    "disposition": "reconciled-live-owner",
}


def test_affine_space_retains_trivial_picard_class_groups_and_basic_opens() -> None:
    plane = AffineSpaces(QQ)(2, names=("x", "y"))
    x = plane.coordinate_algebra().algebra_generator("x")
    opened = plane.basic_open(x)

    assert plane in Schemes(QQ)
    assert plane in AffineSpaces(QQ)
    assert plane.picard_group().picard_scheme() is plane
    assert plane.picard_group().module_rank() == 0
    assert plane.class_group().class_group_scheme() is plane
    assert plane.class_group().module_rank() == 0
    assert opened in OpenImmersions(plane)
    assert opened.inclusion().codomain() is plane


def test_projective_space_retains_fan_divisor_classes_hyperplanes_and_basic_opens() -> None:
    plane = ProjectiveSpaces(QQ)(2, names=("x", "y", "z"))
    x, _y, _z = plane.gens()
    theory = plane.divisor_class_theory()
    hyperplane = plane.hyperplane(0)
    opened = plane.basic_open(x)

    assert plane in ProjectiveSpaces(QQ)
    assert plane.fan().dimension() == 2
    assert theory.picard_group() is plane.picard_group()
    assert theory.class_group() is plane.class_group()
    assert plane.picard_group().module_rank() == 1
    assert plane.class_group().module_rank() == 1
    assert plane.picard_group().hyperplane_class() != plane.picard_group().zero()
    assert hyperplane in ClosedEmbeddings(plane)
    assert hyperplane.codimension() == 1
    assert opened in OpenImmersions(plane)
    assert opened.inclusion().codomain() is plane
