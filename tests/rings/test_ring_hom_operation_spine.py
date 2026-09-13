r"""The ring Hom family refines both multiplicative-additive operation spines."""

from dzack_research.preamble.all import QQ, ZZ, PolynomialRing
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    category_packet,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    OwnedRngs,
    OwnedSemirings,
    ring_homset,
)


def test_ring_hom_is_owned_after_semiring_and_rng_hom_specialization() -> None:
    semiring_homs = category_packet(OwnedSemirings()).Homs()
    rng_homs = category_packet(OwnedRngs()).Homs()
    ring_homs = category_packet(OwnedRings()).Homs()

    assert semiring_homs.base_category() is OwnedSemirings()
    assert rng_homs.base_category() is OwnedRngs()
    assert ring_homs.base_category() is OwnedRings()
    identity = ring_homs.Of(ZZ, ZZ).identity()
    assert identity.domain() is ZZ
    assert identity.codomain() is ZZ
    assert identity(ZZ(3)) == ZZ(3)


def test_framed_polynomial_ring_map_uses_owned_generator_images() -> None:
    polynomials = PolynomialRing(QQ, "x")
    x = polynomials.algebra_generator("x")
    translate = ring_homset(polynomials, polynomials)({"x": x + polynomials.one()})

    assert translate.domain() is polynomials
    assert translate.codomain() is polynomials
    assert translate(x) == x + polynomials.one()
    assert translate(x**2) == (x + polynomials.one()) ** 2
    assert translate(x).parent() is polynomials
