from dzack_research.preamble.all import ZZ, Lattices


def test_square_voronoi_cell_retains_facets_incidence_and_stabilizers() -> None:
    lattice = Lattices(ZZ)(ZZ ** 2)
    cell = lattice.voronoi_cell()

    assert cell.lattice() is lattice
    assert cell.n_vertices() == 4
    assert cell.n_facets() == 4
    assert cell.incidences().cardinality() == 8
    assert cell.stabilizer() is lattice.O()

    for facet in cell.facets():
        normal = facet.relevant_vector()
        assert normal.parent() is lattice
        assert normal != lattice.zero()
        assert facet.vertices().cardinality() == 2
        stabilizer = facet.stabilizer()
        assert stabilizer.supergroup() is lattice.O()
        assert stabilizer.stabilized_object() is normal
        assert stabilizer.stabilizer_action() == "pointwise"


def test_a2_voronoi_facets_are_indexed_by_the_six_relevant_vectors() -> None:
    lattice = Lattices(ZZ)("A2")
    cell = lattice.voronoi_cell()
    facet_normals = {tuple(facet.relevant_vector().to_tuple()) for facet in cell.facets()}
    relevant = {tuple(vector.to_tuple()) for vector in lattice.voronoi_relevant_vectors()}

    assert cell.n_vertices() == 6
    assert cell.n_facets() == 6
    assert facet_normals == relevant
