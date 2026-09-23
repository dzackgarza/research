from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)


def _marked_quadrant():
    lattice = Lattices(ZZ)(ZZ**2)
    e0 = lattice.basis_vector(0)
    e1 = lattice.basis_vector(1)
    cell = lattice.reduction_cell(((1, 0), (0, 1)))
    labels = finite_ordered_set(("first", "second"))
    selected = {"first": e0, "second": e1}
    marks = finite_indexed_family(
        labels,
        lambda label: selected[label],
        name="Coordinate marks",
    )
    return lattice, cell.with_marks(marks)


def test_marked_stabilizer_preserves_cell_and_labels() -> None:
    lattice, marked = _marked_quadrant()
    stabilizer = marked.stabilizer(lattice.O())
    identity = lattice.O().one()
    assert identity in stabilizer

    e0 = lattice.basis_vector(0)
    e1 = lattice.basis_vector(1)
    swap = lattice.Aut()({
        lattice.module_generating_set()[0]: e1,
        lattice.module_generating_set()[1]: e0,
    })
    assert swap in marked.cell().stabilizer(lattice.O())
    assert swap not in stabilizer


def test_marked_adjacency_retains_common_face_and_mark_transporter() -> None:
    lattice, marked = _marked_quadrant()
    e0 = lattice.basis_vector(0)
    e1 = lattice.basis_vector(1)
    labels = lattice.module_generating_set()
    reflection = lattice.Aut()({labels[0]: -e0, labels[1]: e1})
    target = marked.transported_by(reflection)

    adjacency = marked.adjacency_to(target, lattice.O())
    assert adjacency is not None
    assert adjacency.source() is marked
    assert adjacency.target() is target
    assert adjacency.transporter()(e0) == -e0
    assert adjacency.transporter()(e1) == e1
    assert adjacency.common_face().dimension() == 1
