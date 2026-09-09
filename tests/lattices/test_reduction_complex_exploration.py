from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.categories.reduction_complexes import (
    rational_reduction_cell,
    rational_reduction_complex_exploration,
)


def _quadrants():
    lattice = Lattices(ZZ)(ZZ**2)
    cells = (
        rational_reduction_cell(lattice, ((1, 0), (0, 1))),
        rational_reduction_cell(lattice, ((-1, 0), (0, 1))),
        rational_reduction_cell(lattice, ((-1, 0), (0, -1))),
        rational_reduction_cell(lattice, ((1, 0), (0, -1))),
    )
    group = lattice.O()
    adjacencies = []
    for position, cell in enumerate(cells):
        target = cells[(position + 1) % len(cells)]
        adjacency = cell.adjacency_to(target, group)
        assert adjacency is not None
        adjacencies.append(adjacency)
    return lattice, cells, tuple(adjacencies)


def test_complete_quadrant_exploration_pairs_every_facet_and_generates_o_i2() -> None:
    lattice, cells, adjacencies = _quadrants()
    exploration = rational_reduction_complex_exploration(
        lattice,
        cells,
        adjacencies,
        complete=True,
    )

    assert exploration.is_complete()
    assert exploration.unpaired_facets().cardinality() == 0
    assert exploration.adjacencies().cardinality() == 4
    assert exploration.adjacency_transporters().cardinality() == 4
    assert exploration.generation_is_full(lattice.O())


def test_finite_prefix_is_not_promoted_to_a_complete_reduction_domain() -> None:
    lattice, cells, adjacencies = _quadrants()
    prefix = rational_reduction_complex_exploration(
        lattice,
        cells[:2],
        adjacencies[:1],
        complete=False,
    )

    assert not prefix.is_complete()
    assert prefix.unpaired_facets().cardinality() > 0
    try:
        prefix.generation_subgroup(lattice.O())
    except ValueError:
        pass
    else:
        raise AssertionError("a finite exploration prefix is not a group-generation proof")


def test_incomplete_facet_data_cannot_be_declared_complete() -> None:
    lattice, cells, adjacencies = _quadrants()
    try:
        rational_reduction_complex_exploration(
            lattice,
            cells[:2],
            adjacencies[:1],
            complete=True,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("completeness requires an adjacency for every retained facet")
