r"""The ring Mor family refines both multiplicative-additive operation spines."""

from dzack_research.preamble.all import QQ, ZZ
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedRings,
    OwnedRngs,
    OwnedSemirings,
)


def test_ring_mor_is_owned_after_semiring_and_rng_mor_specialization() -> None:
    semiring_homs = OwnedSemirings().category_packet().Mors()
    rng_homs = OwnedRngs().category_packet().Mors()
    ring_homs = OwnedRings().category_packet().Mors()

    assert semiring_homs.base_category() is OwnedSemirings()
    assert rng_homs.base_category() is OwnedRngs()
    assert ring_homs.base_category() is OwnedRings()
    identity = ring_homs.Of(ZZ, ZZ).identity()
    assert identity.domain() is ZZ
    assert identity.codomain() is ZZ
    assert identity(ZZ(3)) == ZZ(3)


def test_framed_polynomial_ring_map_uses_owned_generator_images() -> None:
    polynomials = QQ.polynomial_ring("x")
    x = polynomials.algebra_generator("x")
    translate = polynomials.Mor(polynomials)({"x": x + polynomials.one()})

    assert translate.domain() is polynomials
    assert translate.codomain() is polynomials
    assert translate(x) == x + polynomials.one()
    assert translate(x**2) == (x + polynomials.one()) ** 2
    assert translate(x).parent() is polynomials
