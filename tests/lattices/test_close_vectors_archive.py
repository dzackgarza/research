r"""Archive reconciliation for exact vectors close to a rational target."""

from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.definite_lattices import close_vectors


def test_close_vectors_retains_every_exact_point_in_a_rational_ball() -> None:
    lattice = Lattices(ZZ)([[2]])
    target = (SageQQ(1) / 2,)
    close = close_vectors(lattice, target, ZZ(1))

    assert close.cardinality() == 2
    vectors = tuple(close.index_set())
    assert {tuple(vector.to_tuple()) for vector in vectors} == {(ZZ(0),), (ZZ(1),)}
    assert all(close[vector] == SageQQ(1) / 2 for vector in vectors)
    assert lattice.closest_vector(target) in close.index_set()


def test_close_vectors_preserves_the_negative_definite_sign_convention() -> None:
    lattice = Lattices(ZZ)([[-2]])
    target = (SageQQ(1) / 2,)
    close = close_vectors(lattice, target, ZZ(-1))

    assert close.cardinality() == 2
    assert all(close[vector] == -SageQQ(1) / 2 for vector in close.index_set())
