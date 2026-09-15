r"""A commutative owned ring becomes its own commutative algebra after initialization."""

from dzack_research.preamble.all import ZZ, Algebras


def test_integer_ring_self_algebra_uses_the_finished_owned_parent() -> None:
    category = Algebras(ZZ).Associative().Unital().Commutative()

    assert ZZ in category
    assert ZZ.algebra_base_ring() is ZZ
    structure = ZZ.algebra_structure_morphism()
    assert structure.domain() is ZZ
    assert structure.codomain() is ZZ.ring_center()
    assert structure(ZZ(7)) == ZZ(7)
