from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.lattices import Lattices
from dzack_research.preamble.categories.reduction_complexes import (
    rational_reduction_cell,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring


def test_exact_rational_cells_retain_walls_rays_and_facet_incidence() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)([[1, 0], [0, 1]])
    first = rational_reduction_cell(lattice, ((1, 0), (0, 1)))
    second = rational_reduction_cell(lattice, ((-1, 0), (0, 1)))

    assert first.dimension() == 2
    assert first.facets().cardinality() == 2
    assert first.extreme_rays().cardinality() == 2
    assert first.is_adjacent_to(second)

    common = first.intersection(second)
    assert common.dimension() == 1
    assert common.is_face_of(first)
    assert common.is_face_of(second)
    assert common.contains((0, 3))
    assert not common.contains((1, 0))


def test_cell_stabilizer_is_an_actual_subgroup_of_the_lattice_group() -> None:
    integers = _own_ring(SageZZ)
    lattice = Lattices(integers)([[1, 0], [0, 1]])
    cell = rational_reduction_cell(lattice, ((1, 0), (0, 1)))
    orthogonal_group = lattice.O()
    labels = tuple(lattice.module_generating_set())
    swap = orthogonal_group(
        {
            labels[0]: lattice.module_generator(labels[1]),
            labels[1]: lattice.module_generator(labels[0]),
        }
    )
    first_sign_change = orthogonal_group(
        {
            labels[0]: -lattice.module_generator(labels[0]),
            labels[1]: lattice.module_generator(labels[1]),
        }
    )

    stabilizer = cell.stabilizer(orthogonal_group)
    assert stabilizer.supergroup() is orthogonal_group
    assert swap in stabilizer
    assert first_sign_change not in stabilizer
