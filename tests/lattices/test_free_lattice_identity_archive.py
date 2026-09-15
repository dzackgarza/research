r"""Archive reconciliation for free lattices as one formed-module object."""

from dzack_research.preamble.all import ZZ, Lattices


def test_free_lattice_retains_its_actual_unformed_free_module() -> None:
    lattice = Lattices(ZZ)([[2, 1], [1, 2]])
    form = lattice.form()

    assert form.module() is lattice
    unformed = lattice.unformed_module()
    assert unformed is not lattice
    assert unformed.module_generating_set() is lattice.module_generating_set()

    first, second = lattice.module_generators()
    forget = lattice.forget_form_morphism()
    equip = lattice.equip_form_morphism()

    assert forget.domain() is lattice
    assert forget.codomain() is unformed
    assert equip.domain() is unformed
    assert equip.codomain() is lattice
    framing = lattice.framing_morphism()
    assert framing is equip
    assert framing.domain() is unformed
    assert framing.codomain() is lattice
    assert equip(forget(first)) == first
    second_unformed = unformed.module_generators()[1]
    assert forget(equip(second_unformed)) == second_unformed
    assert first.parent() is lattice
    assert second.parent() is lattice
    assert form(first, first) == lattice.b(first, first) == ZZ(2)
    assert form(first, second) == lattice.b(first, second) == ZZ(1)
    assert form(second, second) == lattice.b(second, second) == ZZ(2)


def test_gram_matrix_is_the_selected_framing_of_that_same_form() -> None:
    lattice = Lattices(ZZ)([[0, 1], [1, 0]])
    form = lattice.form()
    generators = lattice.module_generators()
    gram = lattice.gram_matrix()

    assert form.module() is lattice
    assert lattice.module_rank() == 2
    for i, left in enumerate(generators):
        for j, right in enumerate(generators):
            assert gram[i, j] == form(left, right)
