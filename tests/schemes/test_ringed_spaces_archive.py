"""Archive reconciliation for ringed and locally ringed spaces."""

from dzack_research.preamble.all import (
    QQ,
    AffineSpaces,
    LocallyRingedSpaces,
    LocalRings,
    RingedSpaces,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/schemes/ringed_spaces.sage",
    "live_owner": "src/dzack_research/preamble/categories/schemes/ringed_spaces.py",
    "disposition": "reconciled-live-owner",
}


def test_archived_ringed_space_structure_is_live_on_affine_schemes() -> None:
    line = AffineSpaces(QQ)(1, names=("x",))
    sheaf = line.structure_sheaf()

    assert line in RingedSpaces()
    assert line in LocallyRingedSpaces()
    assert line.underlying_space() is line.underlying_space()
    assert line.underlying_space() is line.coordinate_algebra().spectrum()
    assert sheaf.ringed_space() is line
    assert sheaf.global_sections() is line.coordinate_ring()


def test_archived_locally_ringed_stalk_is_the_actual_point_local_ring() -> None:
    line = AffineSpaces(QQ)(1, names=("x",))
    algebra = line.coordinate_ring()
    x = algebra.algebra_generator("x")
    point = line.underlying_space()(algebra.ideal(x))

    stalk = line.stalk(point)
    assert stalk is line.structure_sheaf().stalk(point)
    assert stalk is point.local_ring()
    assert stalk in LocalRings()
