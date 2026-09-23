from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories import lattice_engines
from dzack_research.preamble.categories.reduction_complexes import (
    _perfect_domain_traversal_from_records,
)


def test_full_adjacency_records_cross_to_cells_stabilizers_and_transporters() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    records = (
        {
            "x": {
                "EXT": [[1, 0], [0, 1]],
                "GRP": [[1, 0]],
            },
            "ListAdj": [
                {
                    "x": {
                        "eInc": [0, 1],
                        "eBigMat": [[0, 1], [-1, 0]],
                    },
                    "iOrb": 0,
                },
                {
                    "x": {
                        "eInc": [1, 0],
                        "eBigMat": [[0, -1], [1, 0]],
                    },
                    "iOrb": 0,
                },
            ],
        },
    )

    traversal = _perfect_domain_traversal_from_records(lattice, records)
    assert traversal.is_complete()
    assert traversal.cells().cardinality() == 1
    assert traversal.adjacencies().cardinality() == 2
    assert traversal.unpaired_facets().cardinality() == 0

    cell = traversal.cells()[0]
    stabilizers = traversal.cell_stabilizer_generators(cell)
    assert stabilizers.cardinality() == 1
    swap = stabilizers[0]
    e0 = lattice.basis_vector(0)
    e1 = lattice.basis_vector(1)
    assert swap(e0) == e1
    assert swap(e1) == e0
    assert cell.transported_by(swap).is_equal_to(cell)

    adjacency = traversal.adjacencies()[0]
    assert adjacency.source() is cell
    assert adjacency.target_representative() is cell
    assert adjacency.common_face().dimension() == 1
    assert adjacency.common_face().is_face_of(adjacency.source())
    assert adjacency.common_face().is_face_of(adjacency.neighbor())
    assert cell.transported_by(adjacency.target_to_neighbor()).is_equal_to(
        adjacency.neighbor()
    )
    assert adjacency.neighbor().transported_by(adjacency.neighbor_to_target()).is_equal_to(
        cell
    )
    assert traversal.group_generators().cardinality() >= 2
    generated = traversal.generation_subgroup()
    assert generated.supergroup() is lattice.O()
    assert all(generator in generated for generator in traversal.group_generators())
    assert traversal.generates_orthogonal_group()


def test_provider_prefix_missing_a_facet_is_not_accepted_as_complete() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    records = (
        {
            "x": {
                "EXT": [[1, 0], [0, 1]],
                "GRP": [[1, 0]],
            },
            "ListAdj": [
                {
                    "x": {
                        "eInc": [0, 1],
                        "eBigMat": [[0, 1], [-1, 0]],
                    },
                    "iOrb": 0,
                }
            ],
        },
    )

    try:
        _perfect_domain_traversal_from_records(lattice, records)
    except ValueError as error:
        assert "every facet" in str(error)
    else:
        raise AssertionError("an incomplete perfect-domain prefix was accepted as complete")


def test_gap_face_indices_are_normalized_to_an_incidence_vector(monkeypatch) -> None:
    gap_output = """return [rec(
        x:=rec(EXT:=[[1,0],[0,1]], GRP:=Group([(1,2)])),
        ListAdj:=[rec(
            x:=rec(eInc:=[2], eBigMat:=[[0,1],[-1,0]]),
            iOrb:=0
        )]
    )];"""
    monkeypatch.setattr(
        lattice_engines,
        "lorentzian_perfect_domain_traversal",
        lambda _gram, _option: gap_output,
    )
    records = lattice_engines._lorentzian_perfect_domain_records(
        [[1, 0], [0, 1]],
        "total",
    )
    group_row = records[0]["x"]["GRP"][0]
    incidence = records[0]["ListAdj"][0]["x"]["eInc"]
    assert group_row[0] == 1
    assert group_row[1] == 0
    assert incidence[0] == 0
    assert incidence[1] == 1
