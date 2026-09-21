from sage.misc.unknown import Unknown
import pytest

from dzack_research.preamble.all import ZZ, Lattices


def test_isometry_to_returns_a_live_lattice_isometry_for_an_identical_lattice() -> None:
    lattice = Lattices(ZZ)("U")

    isometry = lattice.isometry_to(lattice)

    assert isometry.parent() is lattice.Isom(lattice)
    assert isometry.domain() is lattice
    assert isometry.codomain() is lattice
    assert isometry == lattice.O().one()


def test_isometry_to_returns_none_only_when_the_exact_homset_is_proved_empty() -> None:
    even = Lattices(ZZ)([[2]])
    odd = Lattices(ZZ)([[1]])

    assert even.is_isometric_to(odd) is False
    assert even.isometry_to(odd) is None


def test_is_isometric_to_refuses_when_only_the_three_valued_classifier_is_unknown() -> None:
    source = Lattices(ZZ)([[1, 0], [0, -1]])
    change = ZZ.matrix_space(2, 2).from_rows([[1, 2], [0, 1]])
    target = Lattices(ZZ)(source.gram_tensor().pullback(change))

    assert source.is_isometric(target) is Unknown
    with pytest.raises(AssertionError):
        source.is_isometric_to(target)
