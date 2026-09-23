from dzack_research.preamble.all import ZZ, Lattices


def test_the_two_automorphisms_of_the_a2_diagram_lift_to_two_distinct_isometries() -> None:
    r"""``Aut`` of the ``A2`` Dynkin diagram is ``ZZ/2``; both elements lift to isometries.

    ``|O(A2)| / |W(A2)| = 12 / 6 = 2`` (Humphreys, *Reflection Groups and
    Coxeter Groups*, 2.10 and the table of 2.11).
    """
    lattice = Lattices(ZZ)("A2")
    generators = lattice.module_generators()
    configuration = lattice.vector_configuration(generators)
    automorphisms = configuration.configuration_automorphism_group()
    assert automorphisms.order() == 2

    identity, swap = (
        configuration.ambient_isometry_from_automorphism(automorphism)
        for automorphism in automorphisms
    )
    assert identity != swap
    for isometry in (identity, swap):
        assert isometry in lattice.O()
        for left in generators:
            for right in generators:
                assert isometry(left).b(isometry(right)) == left.b(right)


def test_the_triality_group_of_the_d4_diagram_lifts_injectively_into_o_d4() -> None:
    r"""``Aut`` of the ``D4`` diagram is ``S_3`` and lifts to six distinct elements of ``O(D4)``.

    ``|O(D4)| / |W(D4)| = 1152 / 192 = 6`` (Humphreys, 2.10-2.11).
    """
    lattice = Lattices(ZZ)("D4")
    generators = lattice.module_generators()
    configuration = lattice.vector_configuration(generators)
    automorphisms = configuration.configuration_automorphism_group()
    assert automorphisms.order() == 6

    lifts = [
        configuration.ambient_isometry_from_automorphism(automorphism)
        for automorphism in automorphisms
    ]
    for index, isometry in enumerate(lifts):
        assert isometry in lattice.O()
        assert all(isometry != other for other in lifts[index + 1 :])
        for left in generators:
            for right in generators:
                assert isometry(left).b(isometry(right)) == left.b(right)
