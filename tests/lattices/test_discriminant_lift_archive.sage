r"""Lifting discriminant-form automorphisms to lattice isometries."""

from dzack_research.preamble.all import *


def test_O_A2_surjects_onto_O_of_its_discriminant_form() -> None:
    r"""disc(A2) = Z/3 with q = +-2/3 mod 2, so O(q_{A2}) = {+-1} has order 2;
    the nontrivial element -1 is induced by the isometry -1 of A2, so
    O(A2) -> O(q_{A2}) is surjective."""
    lattice = Lattices(ZZ)("A2")
    form = lattice.discriminant_group()
    form_isometries = form.orthogonal_group()
    generator = form.module_generators()[0]

    assert form_isometries.cardinality() == 2
    assert lattice.O().discriminant_image().cardinality() == 2

    target = [g for g in form_isometries if g != form_isometries.one()][0]
    assert target(generator) == -generator

    lifted = lattice.O().discriminant_lift(target)
    assert lifted in lattice.O()
    assert lifted.discriminant_morphism() == target
