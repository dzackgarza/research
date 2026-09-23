r"""Archive reconciliation for exact vectors close to a rational target."""

from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.all import Set, ZZ, Lattices


def test_close_vectors_retains_every_exact_point_in_a_rational_ball() -> None:
    lattice = Lattices(ZZ)([[2]])
    target = (SageQQ(1) / 2,)
    close = lattice.close_vectors(target, ZZ(1))

    assert close.cardinality() == 2
    vectors = close.index_set()
    assert Set(vectors) == Set((lattice.zero(), lattice.basis_vector(0)))
    assert all(close[vector] == SageQQ(1) / 2 for vector in vectors)
    assert lattice.closest_vector(target) in close.index_set()


