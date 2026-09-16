r"""Archive reconciliation for graded sections on a product of projective lines."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    CoxRings,
    ProjectiveSpaces,
    RationalPolyhedralFans,
    Schemes,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_graded_algebra_sections.sage",
    "live_owner": "tests/schemes/test_framework_graded_sections_archive.py",
    "disposition": "reconciled-live-owner",
}


def test_bidegree_four_section_ring_has_the_expected_first_two_graded_pieces() -> None:
    labels = finite_ordered_set(("left", "right"))
    line = ProjectiveSpaces(QQ)(1)
    product = Schemes(QQ).product(indexed_family(labels, lambda _label: line))
    bundle = product.O(4, 4)
    section_ring = bundle.section_ring()

    assert section_ring.graded_piece(1) is bundle.global_sections()
    assert section_ring.graded_piece(1).module_rank() == 25
    assert section_ring.graded_piece(2).module_rank() == 81
    assert section_ring.algebra_generating_set().cardinality() == 25


def test_P1_times_P1_cox_ring_has_four_homogeneous_coordinate_generators() -> None:
    fans = RationalPolyhedralFans(ZZ.free_module(2))
    surface = fans.hirzebruch_surface_fan(0).toric_variety(QQ)
    cox = surface.cox_ring()
    labels = tuple(cox.algebra_generating_set())

    assert cox in CoxRings(surface)
    assert len(labels) == 4
    degrees = tuple(cox.generator_degree(label) for label in labels)
    assert cox.homogeneous_degree(
        cox.algebra_generator(labels[0]) * cox.algebra_generator(labels[1])
    ) == degrees[0] + degrees[1]
