r"""Root-lattice discriminant actions retained from the archived mathematics suite.

Conway--Sloane, chapter 4: ``A_n`` has cyclic glue group and the diagram
automorphism acts by negation; ``D_4`` has trivial Weyl action on its glue but
full triality permutes the three nonzero classes.  The assertions below use the
live owned discriminant-image subgroups.
"""

from dzack_research.preamble.all import (
    Set,
    Lattices,
    finite_ordered_set,
)


def test_a4_discriminant_image_is_negation_on_c5() -> None:
    lattice = Lattices.A4
    form = lattice.discriminant_group()
    image = lattice.Aut().discriminant_image()
    generator = form.module_generators()[0]

    assert form.invariants().cardinality() == 1
    assert form.invariants()[0] == 5
    assert image.cardinality() == 2
    assert Set(image.orbit(generator)) == Set((generator, -generator))


def test_d4_weyl_group_is_trivial_on_glue_but_triality_is_not() -> None:
    lattice = Lattices.D4
    automorphisms = lattice.Aut()
    reflections = finite_ordered_set(
        [lattice.reflection(root) for root in lattice.module_generators()]
    )
    weyl = automorphisms.subgroup_on(reflections)
    full_image = automorphisms.discriminant_image()
    form = lattice.discriminant_group()
    zero = form.zero()
    nonzero = form.condition_set(lambda element: element != zero)
    generator = form.module_generators()[0]

    assert automorphisms.cardinality() == 1152
    assert weyl.cardinality() == 192
    assert weyl.discriminant_image().cardinality() == 1
    assert full_image.cardinality() == 6
    assert form.orthogonal_group().cardinality() == 6
    assert Set(full_image.orbit(generator)) == Set(nonzero)


def test_d4_triality_fuses_the_three_order_two_glue_subgroups() -> None:
    lattice = Lattices.D4
    form = lattice.discriminant_group()
    triality = lattice.Aut().discriminant_image()
    subgroup_orbits = form.orbits_on_subobjects(group=triality)
    isotropic_orbits = form.orbits_on_isotropic_subobjects(group=triality)

    assert Set(orbit.cardinality() for orbit in subgroup_orbits) == Set((1, 3))
    assert sum(orbit.cardinality() for orbit in subgroup_orbits) == 5
    assert isotropic_orbits.cardinality() == 1
    assert isotropic_orbits[0].cardinality() == 1
