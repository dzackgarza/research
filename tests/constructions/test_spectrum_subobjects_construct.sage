r"""D(5) and V(10) in Spec Z retain their defining function and ideal."""

from dzack_research.preamble.all import *  # noqa: F401,F403


def test_distinguished_open_d_five_has_coordinate_ring_z_with_five_inverted() -> None:
    spectrum = ZZ.spectrum()
    open_set = spectrum.distinguished_open(ZZ(5))
    coordinate_ring = open_set.coordinate_ring()

    assert open_set.function() == ZZ(5)
    assert coordinate_ring(ZZ(5)).is_unit()
    assert not coordinate_ring(ZZ(3)).is_unit()


def test_closed_set_v_ten_retains_the_defining_ideal() -> None:
    spectrum = ZZ.spectrum()
    closed = spectrum.closed_set(ZZ.ideal(10))

    assert closed.defining_ideal() == ZZ.ideal(10)
    assert spectrum(ZZ.ideal(2)) in closed
    assert spectrum(ZZ.ideal(5)) in closed

