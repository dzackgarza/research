from dzack_research.preamble.all import ZZ, Lattices
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)


def test_marked_cell_transport_preserves_labels_and_repeated_vectors() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    cell = lattice.reduction_cell(((1, 0), (0, 1)))
    labels = finite_ordered_set(("first", "repeat", "second"))
    e0 = lattice.basis_vector(0)
    e1 = lattice.basis_vector(1)
    selected = {"first": e0, "repeat": e0, "second": e1}
    marks = finite_indexed_family(
        labels,
        lambda label: selected[label],
        name="Repeated marked vectors",
    )
    marked = cell.with_marks(marks)

    lattice_labels = lattice.module_generating_set()
    reflection = lattice.Aut()(
        {
            lattice_labels[0]: -e0,
            lattice_labels[1]: e1,
        }
    )
    transported = marked.transported_by(reflection)

    assert transported.marked_vectors().index_set() is labels
    assert transported.marked_vectors()["first"] == -e0
    assert transported.marked_vectors()["repeat"] == -e0
    assert transported.marked_vectors()["second"] == e1
    assert transported.cell().is_equal_to(
        lattice.reduction_cell(((-1, 0), (0, 1)))
    )
    assert marked.transporter_witness_to(transported, lattice.O()) is not None


def test_zero_norm_vector_is_not_a_mark_for_nonisotropic_reduction() -> None:
    lattice = Lattices(ZZ)("U")
    cell = lattice.reduction_cell(((1, 0), (0, 1)))
    labels = finite_ordered_set(("isotropic",))
    marks = finite_indexed_family(
        labels,
        lambda _label: lattice.basis_vector(0),
    )

    try:
        cell.with_marks(marks)
    except ValueError as error:
        assert "nonzero norm" in str(error)
    else:
        raise AssertionError("an isotropic vector was accepted as a marked nonzero-norm vector")
