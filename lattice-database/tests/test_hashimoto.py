"""Fast source-intake checks on the Hashimoto comparator that need no corpus."""

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.rings import session_ring_objects

from latticedb import hashimoto

ZZ = session_ring_objects()["ZZ"]


def test_the_group_of_a_genus_symbol_is_the_sum_of_its_cyclic_factors() -> None:
    assert hashimoto.symbol_group("2_II^{-2}, 8_1^{+1}, 5^{-1}") == [2, 2, 5, 8]


def test_a_change_of_basis_is_an_isometry_when_it_preserves_the_forms_and_is_bijective() -> None:
    a2 = Lattices(ZZ)([[2, -1], [-1, 2]])
    assert hashimoto.basis_gives_isometry(a2, a2, ((1, 0), (0, 1)))
    # x -> 2x takes b(x, x) = 4 on Z(4) to b(2x, 2x) = 4 on Z, and misses the generator of Z.
    assert not hashimoto.basis_gives_isometry(
        Lattices(ZZ)([[4]]), Lattices(ZZ)([[1]]), ((2,),)
    )
