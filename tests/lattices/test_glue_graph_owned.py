from dzack_research.preamble.all import ZZ, Lattices, isometry_primitive_extension


def test_glue_graph_is_an_owned_finite_set_of_actual_discriminant_elements() -> None:
    lattice = Lattices(ZZ)([[2, 0], [0, -2]])
    involution = lattice.Aut()(
        {
            lattice.module_generating_set()[0]: lattice.module_generator(0),
            lattice.module_generating_set()[1]: -lattice.module_generator(1),
        }
    )
    extension = isometry_primitive_extension(involution)
    graph = extension.glue_graph()

    assert graph.cardinality() == extension.index()
    invariant_ambient = extension.glue().domain().inclusion().codomain()
    coinvariant_ambient = extension.glue().codomain().inclusion().codomain()
    for left, right in graph:
        assert left.parent() is invariant_ambient
        assert right.parent() is coinvariant_ambient
