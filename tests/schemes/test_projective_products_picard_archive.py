r"""Archive reconciliation for Picard arithmetic on a product of projective lines."""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    ProjectiveSpaces,
    RationalPolyhedralFans,
    Schemes,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import indexed_family

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/tests/framework/test_projective_products_picard.sage",
    "live_owner": "tests/schemes/test_projective_products_picard_archive.py",
    "disposition": "reconciled-live-owner",
}


def _product_of_lines():
    labels = finite_ordered_set(("left", "right"))
    line = ProjectiveSpaces(QQ)(1)
    return labels, Schemes(QQ).product(indexed_family(labels, lambda _label: line))


def test_picard_arithmetic_of_a_product_of_lines_is_componentwise() -> None:
    labels, product = _product_of_lines()
    positive = product.O(2, 1)
    negative = product.O(-2, -1)
    trivial = positive.tensor_product(negative)

    assert tuple(trivial.multidegree()[label] for label in labels) == (0, 0)
    assert tuple(product.canonical_line_bundle().multidegree()[label] for label in labels) == (-2, -2)
    anticanonical = product.anticanonical_line_bundle()
    assert tuple(anticanonical.multidegree()[label] for label in labels) == (2, 2)
    assert anticanonical.is_ample()


def test_picard_pairing_of_P1_times_P1_is_the_hyperbolic_plane() -> None:
    fans = RationalPolyhedralFans(ZZ.free_module(2))
    surface = fans.hirzebruch_surface_fan(0).toric_variety(QQ)
    picard = surface.picard_group()
    pairing = surface.picard_intersection_pairing()
    classes = tuple(
        surface.torus_invariant_cartier_class_projection()(
            surface.torus_invariant_prime_divisor(ray)
        )
        for ray in surface.fan().cones(1)
    )

    assert picard.module_rank() == 2
    assert any(
        pairing(left, left) == 0
        and pairing(right, right) == 0
        and pairing(left, right) == 1
        and pairing(right, left) == 1
        for left in classes
        for right in classes
    )
