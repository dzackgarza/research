from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.categories.reduction_complexes import (
    rational_reduction_cell,
)


def test_adjacent_rational_cells_retain_their_common_facet_and_transporter() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    first = rational_reduction_cell(lattice, ((1, 0), (0, 1)))
    second = rational_reduction_cell(lattice, ((-1, 0), (0, 1)))

    assert first.is_adjacent_to(second)
    common = first.intersection(second)
    assert common.dimension() == 1
    assert common.is_face_of(first)
    assert common.is_face_of(second)

    labels = lattice.module_generating_set()
    reflection = lattice.Aut()(
        {
            labels[0]: -lattice.module_generator(labels[0]),
            labels[1]: lattice.module_generator(labels[1]),
        }
    )
    transported = first.transported_by(reflection)
    assert transported.is_equal_to(second)
    assert transported.transported_by(reflection).is_equal_to(first)

    witness = first.transporter_witness_to(second, lattice.O())
    assert witness is not None
    assert first.transported_by(witness).is_equal_to(second)
    assert witness in lattice.O()


def test_cell_stabilizer_and_transporter_are_distinct_group_operations() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    quadrant = rational_reduction_cell(lattice, ((1, 0), (0, 1)))
    stabilizer = quadrant.stabilizer(lattice.O())

    identity = lattice.O().one()
    assert identity in stabilizer
    assert quadrant.transported_by(identity).is_equal_to(quadrant)
    assert quadrant.transporter_witness_to(quadrant, lattice.O()) is not None
