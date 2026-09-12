from dzack_research.preamble.all import Lattices, ZZ
from dzack_research.preamble.categories.reduction_complexes import (
    rational_reduction_cell,
)


def test_faces_are_owned_cells_with_exact_incidence() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    cell = rational_reduction_cell(lattice, ((1, 0), (0, 1)))

    rays = cell.faces(1)
    assert rays.cardinality() == 2
    for face in rays:
        assert face.lattice() is lattice
        assert face.dimension() == 1
        assert face.is_face_of(cell)
    assert cell.faces(2).cardinality() == 1
    assert cell.faces(2)[0].is_equal_to(cell)
    assert cell.faces(3).cardinality() == 0


def test_face_stabilizer_retains_the_cell_face_incidence() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    cell = rational_reduction_cell(lattice, ((1, 0), (0, 1)))
    face = cell.facet((1, 0))
    orthogonal = lattice.O()
    labels = tuple(lattice.module_generating_set())
    e0 = lattice.module_generator(labels[0])
    e1 = lattice.module_generator(labels[1])
    identity = orthogonal.one()
    swap = orthogonal({labels[0]: e1, labels[1]: e0})

    stabilizer = cell.face_stabilizer(face, orthogonal)
    assert stabilizer.supergroup() is orthogonal
    assert identity in stabilizer
    assert swap in cell.stabilizer(orthogonal)
    assert swap not in stabilizer


def test_face_incidence_retains_face_cell_and_pair_stabilizer() -> None:
    lattice = Lattices(ZZ)(ZZ**2)
    cell = rational_reduction_cell(lattice, ((1, 0), (0, 1)))
    orthogonal = lattice.O()

    incidences = cell.face_incidences(1, orthogonal)
    assert incidences.cardinality() == 2
    for face in incidences.index_set():
        incidence = incidences[face]
        assert incidence.face() is face
        assert incidence.cell() is cell
        assert incidence.codimension() == 1
        assert incidence.stabilizer().supergroup() is orthogonal
        assert orthogonal.one() in incidence.stabilizer()
