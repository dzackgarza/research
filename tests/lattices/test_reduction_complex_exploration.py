from dzack_research.preamble.all import ZZ, Lattices, finite_ordered_set


def _quadrants():
    lattice = Lattices(ZZ)(ZZ**2)
    cells = finite_ordered_set(
        (
            lattice.reduction_cell(((1, 0), (0, 1))),
            lattice.reduction_cell(((-1, 0), (0, 1))),
            lattice.reduction_cell(((-1, 0), (0, -1))),
            lattice.reduction_cell(((1, 0), (0, -1))),
        )
    )
    group = lattice.O()
    adjacencies = []
    for position, cell in enumerate(cells):
        target = cells[(position + 1) % int(cells.cardinality())]
        adjacency = cell.adjacency_to(target, group)
        assert adjacency is not None
        adjacencies.append(adjacency)
    return lattice, cells, finite_ordered_set(adjacencies)


def test_complete_quadrant_exploration_pairs_every_facet_and_generates_o_i2() -> None:
    lattice, cells, adjacencies = _quadrants()
    exploration = lattice.reduction_complex_exploration(
        cells,
        adjacencies,
        complete=True,
    )

    assert exploration.is_complete()
    assert exploration.unpaired_facets().cardinality() == 0
    assert exploration.adjacencies().cardinality() == 4
    assert exploration.adjacency_transporters().cardinality() == 4
    adjacency = exploration.adjacencies()[0]
    assert adjacency.source() in exploration.cells()
    assert adjacency.target() in exploration.cells()
    assert adjacency.common_face().is_face_of(adjacency.source())
    assert adjacency.common_face().is_face_of(adjacency.target())
    assert adjacency.transporter() in lattice.O()
    assert adjacency.source().transport(adjacency.transporter()).is_equal_to(
        adjacency.target()
    )
    assert exploration.generation_is_full(lattice.O())




