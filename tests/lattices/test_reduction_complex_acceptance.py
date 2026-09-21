from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.reduction_complexes import (
    _perfect_domain_traversal_from_records,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family


def _completed_single_orbit_traversal():
    lattice = Lattices(ZZ)(ZZ**2)
    records = (
        {
            "x": {"EXT": [[1, 0], [0, 1]], "GRP": [[1, 0]]},
            "ListAdj": [
                {"x": {"eInc": [0, 1], "eBigMat": [[0, 1], [-1, 0]]}, "iOrb": 0},
                {"x": {"eInc": [1, 0], "eBigMat": [[0, -1], [1, 0]]}, "iOrb": 0},
            ],
        },
    )
    return lattice, _perfect_domain_traversal_from_records(lattice, records)


def test_reduction_complex_acceptance_keeps_faces_transporters_marks_and_completeness() -> None:
    lattice, traversal = _completed_single_orbit_traversal()
    assert traversal.is_complete()
    assert traversal.unpaired_facets().cardinality() == 0
    adjacency = traversal.adjacencies()[0]
    face = adjacency.common_face()
    assert face.is_face_of(adjacency.source())
    assert face.is_face_of(adjacency.neighbor())
    transporter = adjacency.target_to_neighbor()
    assert adjacency.target_representative().transported_by(transporter).is_equal_to(
        adjacency.neighbor()
    )
    assert traversal.generates_orthogonal_group()

    cell = traversal.cells()[0]
    labels = finite_ordered_set(("v",))
    mark = lattice.basis_vector(0)
    marked = cell.with_marks(
        finite_indexed_family(labels, lambda _label: mark, name="Acceptance mark")
    )
    transported = marked.transported_by(transporter)
    assert transported.marked_vectors()["v"] == transporter(mark)
    assert transported.marked_vectors().index_set() is labels


def test_reduction_complex_acceptance_does_not_promote_a_prefix_to_complete() -> None:
    lattice, traversal = _completed_single_orbit_traversal()
    cell = traversal.cells()[0]
    prefix = lattice.reduction_complex_exploration((cell,), (), complete=False)
    assert not prefix.is_complete()
    assert prefix.unpaired_facets().cardinality() > 0
