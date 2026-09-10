r"""Archive reconciliation for the independent lattice property refinements."""

from dzack_research.preamble.all import (
    EvenLattices,
    FiniteRankLattices,
    Lattices,
    NondegenerateLattices,
    ZZ,
)


def test_integral_valued_is_the_base_lattice_contract() -> None:
    lattice = Lattices(ZZ)([[1, 2], [2, 3]])
    first, second = tuple(lattice.module_generators())

    assert lattice.b(first, first) in ZZ
    assert lattice.b(first, second) in ZZ
    assert lattice.b(second, second) in ZZ


def test_finite_nondegenerate_and_even_are_independent_refinements() -> None:
    even_nondegenerate = Lattices(ZZ)([[0, 1], [1, 0]])
    odd_nondegenerate = Lattices(ZZ)([[1]])
    even_degenerate = Lattices(ZZ)([[0]])

    assert even_nondegenerate in FiniteRankLattices(ZZ)
    assert even_nondegenerate in NondegenerateLattices(ZZ)
    assert even_nondegenerate in EvenLattices(ZZ)

    assert odd_nondegenerate in FiniteRankLattices(ZZ)
    assert odd_nondegenerate in NondegenerateLattices(ZZ)
    assert odd_nondegenerate not in EvenLattices(ZZ)

    assert even_degenerate in FiniteRankLattices(ZZ)
    assert even_degenerate not in NondegenerateLattices(ZZ)
    assert even_degenerate in EvenLattices(ZZ)
