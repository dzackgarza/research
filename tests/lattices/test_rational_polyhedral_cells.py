from dzack_research.preamble.all import Set, ZZ, Lattices


def test_square_voronoi_cell_retains_facets_incidence_and_stabilizers() -> None:
    lattice = Lattices(ZZ)(ZZ ** 2)
    cell = lattice.voronoi_cell()

    assert cell.ambient_lattice() is lattice
    assert cell.n_vertices() == 4
    assert cell.facets().cardinality() == 4
    facets = lattice.voronoi_facets()
    assert sum(facet.vertices().cardinality() for facet in facets) == 8
    # Every isometry acts on the actual rational vertices.  This retains
    # the full-O(L) stabilizer requirement without a Voronoi-only wrapper.
    labels = tuple(lattice.module_generating_set())
    vertices = {tuple(vertex) for vertex in cell.vertices()}
    for isometry in lattice.O():
        images = [lattice.framing_coefficients(isometry(lattice.module_generator(label))) for label in labels]
        for vertex in vertices:
            assert tuple(sum(vertex[column] * images[column].get(label, 0) for column in range(len(labels))) for label in labels) in vertices

    for normal in facets.index_set():
        facet = facets[normal]
        assert normal.parent() is lattice
        assert normal != lattice.zero()
        assert facet.vertices().cardinality() == 2
        stabilizer = lattice.O().stabilizer(normal)
        assert stabilizer.supergroup() is lattice.O()
        assert stabilizer.stabilized_object() is normal
        assert stabilizer.stabilizer_action() == "pointwise"


def test_a2_voronoi_facets_are_indexed_by_the_six_relevant_vectors() -> None:
    lattice = Lattices(ZZ)("A2")
    cell = lattice.voronoi_cell()
    facet_normals = Set(lattice.voronoi_facets().index_set())
    relevant = Set(lattice.voronoi_relevant_vectors())

    assert cell.n_vertices() == 6
    assert cell.facets().cardinality() == 6
    assert facet_normals == relevant
