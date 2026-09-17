r"""Archive reconciliation for free lattices as one formed-module object."""

from dzack_research.preamble.all import ZZ, Lattices


def test_free_lattice_retains_its_actual_unformed_free_module() -> None:
    lattice = Lattices(ZZ)([[2, 1], [1, 2]])
    form = lattice.form()

    assert form.module() is lattice.unformed_module()
    unformed = lattice.unformed_module()
    assert unformed is not lattice
    assert unformed.module_generating_set() is lattice.module_generating_set()

    first, second = lattice.module_generators()
    framing = lattice.framing_morphism()
    assert framing.codomain() is lattice
    for label in lattice.module_generating_set():
        assert framing(framing.domain().module_generator(label)) == lattice.module_generator(label)
    assert lattice(unformed(first)) == first
    second_unformed = unformed.module_generators()[1]
    assert unformed(lattice(second_unformed)) == second_unformed
    assert first.parent() is lattice
    assert second.parent() is lattice
    assert form(unformed(first), unformed(first)) == lattice.b(first, first) == ZZ(2)
    assert form(unformed(first), unformed(second)) == lattice.b(first, second) == ZZ(1)
    assert form(unformed(second), unformed(second)) == lattice.b(second, second) == ZZ(2)


def test_gram_matrix_is_the_selected_framing_of_that_same_form() -> None:
    lattice = Lattices(ZZ)([[0, 1], [1, 0]])
    form = lattice.form()
    generators = lattice.module_generators()
    gram = lattice.gram_matrix()

    assert form.module() is lattice.unformed_module()
    assert lattice.module_rank() == 2
    for i, left in enumerate(generators):
        for j, right in enumerate(generators):
            assert gram[i, j] == form(lattice.unformed_module()(left), lattice.unformed_module()(right))
