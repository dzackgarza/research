r"""Archive reconciliation for free lattices as one formed-module object."""

from dzack_research.preamble.all import Lattices, ZZ


def test_free_lattice_form_is_defined_on_the_lattice_itself() -> None:
    lattice = Lattices(ZZ)([[2, 1], [1, 2]])
    form = lattice.form()

    assert form.module() is lattice
    assert lattice.unformed_module() is lattice

    first, second = tuple(lattice.module_generators())
    assert first.parent() is lattice
    assert second.parent() is lattice
    assert form(first, first) == lattice.b(first, first) == ZZ(2)
    assert form(first, second) == lattice.b(first, second) == ZZ(1)
    assert form(second, second) == lattice.b(second, second) == ZZ(2)


def test_gram_matrix_is_the_selected_framing_of_that_same_form() -> None:
    lattice = Lattices(ZZ)([[0, 1], [1, 0]])
    form = lattice.form()
    generators = tuple(lattice.module_generators())
    gram = lattice.gram_matrix()

    assert form.module() is lattice
    assert lattice.module_rank() == 2
    for i, left in enumerate(generators):
        for j, right in enumerate(generators):
            assert gram[i, j] == form(left, right)
