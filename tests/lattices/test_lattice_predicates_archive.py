r"""Archive reconciliation for exact lattice and element predicates."""

from dzack_research.preamble.catalogue import NamedLattices


def test_elliptic_and_parabolic_are_distinct_lattice_predicates() -> None:
    assert NamedLattices.E8.is_elliptic()
    assert not NamedLattices.E8.is_parabolic()
    assert not NamedLattices.U.is_elliptic()


def test_isotropy_in_the_hyperbolic_plane_is_exactly_zero_norm() -> None:
    e, f = tuple(NamedLattices.U.module_generators())

    assert e.norm() == 0
    assert f.norm() == 0
    assert e.is_isotropic()
    assert f.is_isotropic()
    assert e.b(f) == 1

    diagonal = e + f
    assert diagonal.norm() == 2
    assert not diagonal.is_isotropic()
