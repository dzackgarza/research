r"""Root-lattice discriminant actions retained from the archived mathematics suite.

Conway--Sloane, chapter 4: ``A_n`` has cyclic glue group and the diagram
automorphism acts by negation; ``D_4`` has trivial Weyl action on its glue but
full triality permutes the three nonzero classes.  The assertions below use the
live owned discriminant-image subgroups.
"""

from dzack_research.preamble.all import Lattices


def test_a4_discriminant_image_is_negation_on_c5() -> None:
    lattice = Lattices.A4
    form = lattice.discriminant_group()
    image = lattice.Aut().discriminant_image()
    generator = form.module_generators()[0]

    assert tuple(form.invariants()) == (5,)
    assert image.cardinality() == 2
    assert set(image.orbit(generator)) == {generator, -generator}


def test_d4_weyl_group_is_trivial_on_glue_but_triality_is_not() -> None:
    lattice = Lattices.D4
    automorphisms = lattice.Aut()
    reflections = tuple(
        lattice.reflection(root) for root in lattice.module_generators()
    )
    weyl = automorphisms.subgroup_on(reflections)
    full_image = automorphisms.discriminant_image()
    form = lattice.discriminant_group()
    zero = form.zero()
    nonzero = {element for element in form if element != zero}
    generator = form.module_generators()[0]

    assert automorphisms.cardinality() == 1152
    assert weyl.cardinality() == 192
    assert weyl.discriminant_image().cardinality() == 1
    assert full_image.cardinality() == 6
    assert form.orthogonal_group().cardinality() == 6
    assert set(full_image.orbit(generator)) == nonzero


def test_d4_triality_fuses_the_three_order_two_glue_subgroups() -> None:
    lattice = Lattices.D4
    form = lattice.discriminant_group()
    triality = lattice.Aut().discriminant_image()
    subgroup_orbits = tuple(form.orbits_on_subobjects(group=triality))
    isotropic_orbits = tuple(form.orbits_on_isotropic_subobjects(group=triality))

    assert sorted(len(orbit) for orbit in subgroup_orbits) == [1, 1, 3]
    assert len(isotropic_orbits) == 1
    assert len(isotropic_orbits[0]) == 1
