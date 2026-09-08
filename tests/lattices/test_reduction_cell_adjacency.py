from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.categories.reduction_complexes import (
    ReductionCellAdjacency,
    rational_reduction_cell,
)


def test_adjacent_cell_record_retains_face_and_oriented_transporter() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    source = rational_reduction_cell(lattice, ((1, 0), (0, 1)))
    target = rational_reduction_cell(lattice, ((-1, 0), (0, 1)))

    adjacency = source.adjacency_to(target, lattice.O())
    assert isinstance(adjacency, ReductionCellAdjacency)
    assert adjacency.source() is source
    assert adjacency.target() is target
    assert adjacency.common_face().is_equal_to(source.intersection(target))
    assert source.transported_by(adjacency.transporter()).is_equal_to(target)

    reverse = adjacency.reversed()
    assert reverse.source() is target
    assert reverse.target() is source
    assert reverse.common_face().is_equal_to(adjacency.common_face())
    assert target.transported_by(reverse.transporter()).is_equal_to(source)
    assert reverse.transporter() == ~adjacency.transporter()


def test_nonadjacent_cells_do_not_acquire_an_adjacency_record() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    first = rational_reduction_cell(lattice, ((1, 0), (0, 1)))
    opposite = rational_reduction_cell(lattice, ((-1, 0), (0, -1)))

    assert not first.is_adjacent_to(opposite)
    assert first.adjacency_to(opposite, lattice.O()) is None
