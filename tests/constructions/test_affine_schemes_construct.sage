r"""Spectra are affine schemes over their represented base rings."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_spec_of_every_commutative_ring_is_affine(commutative_ring) -> None:
    ring = commutative_ring
    spectrum = ring.affine_spectrum()

    assert spectrum in AffineSchemes(ring)
    assert spectrum in Schemes(ring)
    assert spectrum in Schemes(ZZ)
    assert spectrum.is_affine()
    assert spectrum.coordinate_ring() is ring
    assert spectrum.relative_dimension() == 0
