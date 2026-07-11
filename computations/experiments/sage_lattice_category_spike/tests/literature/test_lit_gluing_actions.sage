r"""Literature-cited public gluing and discriminant-action tests.

These tests pin behavior to Conway and Sloane, *Sphere Packings, Lattices and
Groups*, 3rd ed. (1999) [CS10], using the spike's public lattice APIs rather
than implementation helpers.

CS10 Chapter 4 is the independent oracle:

  - sec. 3: glue vectors live in the dual quotient L^*/L, and integral
    overlattices are obtained by adjoining compatible glue vectors;
  - sec. 6.1: A_n has cyclic glue group C_{n+1}, and the order-two diagram
    automorphism sends [i] to [n+1-i];
  - sec. 7.1 and 7.2: D_4 has glue group V_4, Weyl subgroup order
    2^3 * 4!, full automorphism order (2^3 * 4!) * 3!, and the three nonzero
    glue cosets are equivalent;
  - sec. 8.1: E_8 is even unimodular with minimal norm 2 and 240 minimal
    vectors.
"""

from __future__ import annotations

from math import factorial

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ
from sage.rings.rational_field import QQ

import sage_lattice_category_spike.lattice_categories as lc


def _coefficient_rows(elements):
    return sorted(tuple(element.coefficient_vector()) for element in elements)


def _orbit_rows(orbits):
    return sorted(tuple(_coefficient_rows(orbit)) for orbit in orbits)


def _matrix_rows(matrix_):
    return tuple(tuple(row) for row in matrix_.rows())


def _subgroup_orbit_rows(orbits):
    return sorted(
        tuple(
            sorted(
                tuple(_coefficient_rows(subgroup.elements()))
                for subgroup in orbit
            )
        )
        for orbit in orbits
    )


def test_a4_a4_order_five_glue_reconstructs_e8_through_public_gluing_surfaces():
    r"""A_4 has glue group C_5 [CS10, Ch. 4 sec. 6.1].  The order-five
    isotropic glue between two A_4 components is a Ch. 4 sec. 3 overlattice;
    the resulting even unimodular rank-eight root lattice has the E_8 root
    count from Ch. 4 sec. 8.1.
    """
    left = lc.Lattice("A4(-1)")
    right = lc.Lattice("A4(-1)")
    left_generator = left.discriminant_group().gen(0)
    right_generator = right.discriminant_group().gen(0)

    via_constructor = lc.IntegralLatticeGluing(
        [left, right],
        [[left_generator, 2 * right_generator]],
        label="A4_A4_order_five_glue",
    )

    ambient = left.direct_sum(right)
    discriminant_form = ambient.discriminant_group()
    glue_generator = discriminant_form.gen(0) + discriminant_form.gen(1)
    glue_subgroup = discriminant_form.subgroup_generated_by([glue_generator])
    via_lattice_glue = ambient.glue([glue_generator], label="A4_A4_order_five_glue")

    assert glue_subgroup.cardinality() == 5
    assert discriminant_form.is_isotropic_subgroup(glue_subgroup)
    assert discriminant_form.orthogonal_quotient(glue_subgroup).invariants() == ()

    e8 = lc.Lattice("E8(-1)")
    for glued in (via_constructor, via_lattice_glue):
        assert glued.is_even()
        assert glued.is_unimodular()
        assert glued.minimum() == 2
        assert len(glued.roots()) == 240
        assert glued.discriminant_group().invariants() == ()
        assert glued.is_isometric(e8)

    assert via_constructor.is_isometric(via_lattice_glue)


def test_a2_e6_gluing_returns_primitive_complementary_embeddings_in_e8():
    r"""CS10 Ch. 4 sec. 8 identifies E_6 as the orthogonal complement of
    A_2 in E_8. The public gluing constructor should therefore return actual
    primitive isometric summand embeddings when asked, not just the glued
    overlattice.
    """
    a2 = lc.Lattice("A2(-1)")
    e6 = lc.Lattice("E6(-1)")

    glued, (a2_embedding, e6_embedding) = lc.IntegralLatticeGluing(
        [a2, e6],
        [[a2.discriminant_group().gen(0), 2 * e6.discriminant_group().gen(0)]],
        return_embeddings=True,
        label="A2_E6_order_three_glue",
    )

    assert glued.is_even() and glued.is_unimodular()
    assert glued.minimum() == 2 and len(glued.roots()) == 240
    assert glued.is_isometric(lc.Lattice("E8(-1)"))
    assert a2_embedding.is_injective()
    assert e6_embedding.is_injective()

    a2_image = a2_embedding.image()
    e6_image = e6_embedding.image()
    assert glued.is_primitive(a2_image)
    assert glued.is_primitive(e6_image)
    assert a2_image.is_isometric(a2)
    assert e6_image.is_isometric(e6)
    assert glued.orthogonal_complement(a2_image).is_isometric(e6)
    assert glued.orthogonal_complement(e6_image).is_isometric(a2)


def test_a2_diagram_automorphism_induces_inversion_on_dual_quotient():
    r"""The A_2 diagram automorphism acts by inversion on A_2^*/A_2.

    CS10 Ch. 4 sec. 6.1 identifies A_n^*/A_n with the cyclic glue group
    C_{n+1} and records that the order-two diagram automorphism sends
    [i] to [n+1-i]. For A_2 this makes the nontrivial diagram automorphism
    the inversion action on C_3.
    """
    lattice = lc.Lattice("A2(-1)")
    dual = lattice.dual()
    quotient = dual.finite_quotient(lattice)
    quotient_map = dual.quotient_map_to(lattice)
    diagram_automorphism = dual.Hom(dual).from_matrix(matrix(ZZ, [[0, 1], [1, 0]]))
    induced_action = dual.induced_map_on_quotient(diagram_automorphism, quotient)

    assert lattice.rank() == 2
    assert lattice.gram_matrix() == matrix(ZZ, [[2, -1], [-1, 2]])
    assert lattice.determinant() == 3
    assert quotient.cover_lattice() == dual
    assert quotient.relation_lattice() == lattice
    assert quotient.invariants() == (3,)
    assert quotient.exponent() == 3

    elements = quotient.elements()
    assert tuple(tuple(element.coefficient_vector()) for element in elements) == ((0,), (1,), (2,))
    assert tuple(induced_action(element) for element in elements) == (
        elements[0],
        elements[2],
        elements[1],
    )
    assert induced_action.matrix() == matrix(ZZ, [[2]])
    assert induced_action.kernel().cardinality() == 1
    assert induced_action.image().cardinality() == quotient.cardinality()
    assert all(induced_action(element) == -element for element in elements)
    assert all(quotient_map(quotient.lift(element)) == element for element in elements)
    assert all(
        quotient.projection(diagram_automorphism(quotient.lift(element))) == induced_action(element)
        for element in elements
    )


def test_a4_full_isometry_action_negates_cyclic_glue_group_and_has_cs99_orbits():
    r"""CS10 Ch. 4 sec. 6.1 identifies the A_n glue group as C_{n+1} and
    says the order-two automorphism sends [i] to [n+1-i].  For A_4, this is
    negation on C_5, with orbits {0}, {+-[1]}, and {+-[2]}.
    """
    lattice = lc.Lattice("A4(-1)")
    discriminant_form = lattice.discriminant_group()
    generator = discriminant_form.gen(0)

    isometry_group = lattice.isometry_group()
    discriminant_image = isometry_group.subgroup(isometry_group.gens()).discriminant_image()
    generator_images = {action(generator) for action in discriminant_image}

    assert isometry_group.order() == 2 * factorial(5)
    assert discriminant_image.order() == 2
    assert generator_images == {generator, -generator}
    assert _orbit_rows(discriminant_form.orbits(group=discriminant_image)) == [
        ((0,),),
        ((1,), (4,)),
        ((2,), (3,)),
    ]


def test_a4_group_automorphisms_separate_from_form_isometries_and_transport_forms():
    r"""The A_4 glue group is cyclic of order five [CS10, Ch. 4 sec. 6.1],
    while the diagram automorphism only realizes negation on that group.  Thus
    the finite group automorphism surface has four units, but the discriminant
    form isometry surface has only the two units preserving q([1]) = 4/5.
    """
    lattice = lc.Lattice("A4(-1)")
    discriminant_form = lattice.discriminant_group()
    generator = discriminant_form.gen(0)
    doubling = discriminant_form.hom([2 * generator])

    assert discriminant_form.invariants() == (5,)
    assert discriminant_form.q(generator) == QQ(4) / 5
    assert discriminant_form.q(2 * generator) == QQ(6) / 5
    assert discriminant_form.relations_among((generator, 2 * generator)) == (
        (0, 0),
        (1, 2),
        (2, 4),
        (3, 1),
        (4, 3),
    )

    assert doubling.is_automorphism()
    assert not doubling.preserves_bilinear_form()
    assert not doubling.preserves_quadratic_form()
    assert _matrix_rows(discriminant_form.pushforward_form(doubling)) == ((QQ(6) / 5,),)
    assert _matrix_rows(discriminant_form.pullback_form(doubling)) == ((QQ(6) / 5,),)

    assert discriminant_form.automorphism_group().order() == 4
    assert sorted(
        tuple(action(generator).coefficient_vector())
        for action in discriminant_form.automorphism_group()
    ) == [(1,), (2,), (3,), (4,)]
    assert discriminant_form.orthogonal_group().order() == 2
    assert discriminant_form.orthogonal_group(kind="bilinear").order() == 2
    assert sorted(
        tuple(action(generator).coefficient_vector())
        for action in discriminant_form.orthogonal_group()
    ) == [(1,), (4,)]


def test_d4_reflections_generate_weyl_subgroup_and_full_isometries_act_by_triality():
    r"""CS10 Ch. 4 sec. 7.1 gives the D_4 Weyl subgroup order
    2^3 * 4! = 192 and the full automorphism order multiplied by the
    order-six triality group.  The simple-root reflections also satisfy the
    simply-laced D_4 Coxeter relations read from the diagram in Fig. 4.6.
    """
    lattice = lc.Lattice("D4(-1)")
    simple_reflections = tuple(lattice.reflection(simple_root) for simple_root in lattice.gens())
    isometry_group = lattice.isometry_group()
    weyl_group = isometry_group.subgroup(simple_reflections)

    assert weyl_group.order() == 2**3 * factorial(4)
    assert isometry_group.order() == (2**3 * factorial(4)) * factorial(3)
    assert tuple(tuple((left * right).order() for right in simple_reflections) for left in simple_reflections) == (
        (1, 3, 2, 2),
        (3, 1, 3, 3),
        (2, 3, 1, 2),
        (2, 3, 2, 1),
    )

    discriminant_form = lattice.discriminant_group()
    full_discriminant_image = isometry_group.subgroup(isometry_group.gens()).discriminant_image()
    nonzero_glue_cosets = set(discriminant_form.elements()) - {discriminant_form.zero()}
    first_glue, second_glue = discriminant_form.gens()
    third_glue = first_glue + second_glue

    assert [
        discriminant_form.q(glue_vector)
        for glue_vector in (discriminant_form.zero(), first_glue, second_glue, third_glue)
    ] == [0, 1, 1, 1]
    assert discriminant_form.relations_among((first_glue, second_glue, third_glue)) == (
        (0, 0, 0),
        (1, 1, 1),
    )

    assert weyl_group.discriminant_image().order() == 1
    assert full_discriminant_image.order() == factorial(3)
    assert discriminant_form.orthogonal_group().order() == factorial(3)
    assert discriminant_form.orthogonal_group(kind="bilinear").order() == factorial(3)
    assert sorted(
        _matrix_rows(isometry.induced_map_on_discriminant_group().matrix())
        for isometry in isometry_group.gens()
    ) == [
        ((0, 1), (1, 0)),
        ((1, 0), (0, 1)),
        ((1, 0), (1, 1)),
    ]
    assert sorted(_matrix_rows(action.matrix()) for action in full_discriminant_image) == [
        ((0, 1), (1, 0)),
        ((0, 1), (1, 1)),
        ((1, 0), (0, 1)),
        ((1, 0), (1, 1)),
        ((1, 1), (0, 1)),
        ((1, 1), (1, 0)),
    ]
    for action in full_discriminant_image:
        assert action.preserves_bilinear_form()
        assert action.preserves_quadratic_form()
    assert discriminant_form.orbit(discriminant_form.gen(0), group=full_discriminant_image) == frozenset(nonzero_glue_cosets)
    assert _subgroup_orbit_rows(discriminant_form.orbits_on_subgroups(group=full_discriminant_image)) == [
        (((0, 0),),),
        (((0, 0), (0, 1)), ((0, 0), (1, 0)), ((0, 0), (1, 1))),
        (((0, 0), (0, 1), (1, 0), (1, 1)),),
    ]
    assert _subgroup_orbit_rows(discriminant_form.orbits_on_isotropic_subgroups(group=full_discriminant_image)) == [
        (((0, 0),),),
    ]
