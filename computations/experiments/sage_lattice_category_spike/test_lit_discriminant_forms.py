"""Literature-cited finite discriminant-form arithmetic tests.

The cited local sources used for these finite-form facts are:

* Nikulin, Integral symmetric bilinear forms and some of their applications,
  Sections 1.3-1.4 and 1.6: discriminant forms, isotropic subgroups, and
  overlattice glue.
* Conway-Sloane, Sphere Packings, Lattices and Groups, Ch. 4: glue groups for
  A2 and D8, and the D8+ construction of E8.
"""

from sage.all import QQ, ZZ, matrix

import sage_lattice_category_spike.lattice_categories as lc


def _coordinates(form, element):
    return tuple(ZZ(c) for c in form.coordinates(element))


def _cyclic_elements_by_coefficient(form):
    return {_coordinates(form, element): element for element in form.elements()}


def test_nikulin_rank_one_sign_pair_separates_quadratic_from_bilinear_form():
    """The forms <2> and <-2> have the same 2-primary group/b but opposite q.

    Nikulin defines q(x + L) = x^2 mod 2Z on L*/L and records that negating a
    lattice negates its finite quadratic form and signature mod 8.
    """

    plus = lc.Lattice(matrix(ZZ, 1, 1, [2])).discriminant_group()
    minus = lc.Lattice(matrix(ZZ, 1, 1, [-2])).discriminant_group()
    g_plus = plus.gen(0)
    g_minus = minus.gen(0)

    assert plus.invariants() == (2,)
    assert minus.invariants() == (2,)
    assert plus.q(g_plus) == QQ(1) / 2
    assert minus.q(g_minus) == QQ(3) / 2
    assert plus.b(g_plus, g_plus) == QQ(1) / 2
    assert minus.b(g_minus, g_minus) == QQ(1) / 2

    assert plus.is_isomorphic(minus, kind="bilinear")
    assert not plus.is_isomorphic(minus, kind="quadratic")
    assert plus.brown_invariant() == 1
    assert minus.brown_invariant() == 7


def test_nikulin_lagrangian_glue_of_rank_one_sign_pair_has_trivial_quotient():
    """For <2> + <-2>, the diagonal order-two subgroup is Lagrangian glue.

    Nikulin Prop. 1.4.1 identifies even overlattices with isotropic subgroups H
    and gives the new discriminant form as H^perp/H.  The diagonal element has
    q = 1/2 + 3/2 = 0 in Q/2Z, so the quotient must be trivial.
    """

    positive_line = lc.Lattice(matrix(ZZ, 1, 1, [2]))
    negative_line = lc.Lattice(matrix(ZZ, 1, 1, [-2]))
    direct_sum = positive_line.direct_sum(negative_line)
    form = direct_sum.discriminant_group()
    diagonal = form.gen(0) + form.gen(1)
    subgroup = [form.zero(), diagonal]

    assert form.invariants() == (2, 2)
    assert form.q(diagonal) == 0
    assert form.is_isotropic_subgroup(subgroup)
    assert form.is_lagrangian(subgroup)
    assert set(form.orthogonal(subgroup).elements()) == set(subgroup)

    quotient = form.orthogonal_quotient(subgroup)
    glued = form.overlattice_from_isotropic_subgroup(subgroup)

    assert quotient.invariants() == ()
    assert quotient.order() == 1
    assert glued.is_even()
    assert glued.is_unimodular()
    assert glued.signature_pair() == (1, 1)
    assert glued.discriminant_group().invariants() == ()


def test_conway_sloane_d8_isotropic_self_glue_reconstructs_e8():
    """Conway-Sloane's D8+ glue uses an isotropic D8 glue class to obtain E8."""

    d8 = lc.Lattice("D8")
    e8 = lc.Lattice("E8")
    form = d8.discriminant_group()
    nonzero_isotropic = [
        element
        for element in form.elements()
        if _coordinates(form, element) != (0, 0) and form.is_isotropic_element(element)
    ]

    assert form.invariants() == (2, 2)
    assert len(nonzero_isotropic) == 2

    for glue_vector in nonzero_isotropic:
        subgroup = [form.zero(), glue_vector]
        glued = form.overlattice_from_isotropic_subgroup(subgroup)

        assert form.q(glue_vector) == 0
        assert form.is_lagrangian(subgroup)
        assert glued.is_even()
        assert glued.is_unimodular()
        assert len(glued.roots()) == 240
        assert glued.is_isometric(e8)


def test_conway_sloane_a2_discriminant_form_is_anisotropic_and_nonmetabolic():
    """A2 has glue group C3; in Cartan normalization its exact finite q is 2/3.

    Conway-Sloane list the A2 glue group as cyclic of order three.  Combining
    that with Nikulin's discriminant-form definition gives the exact q and b
    tables below for the Cartan-normalized root lattice.
    """

    form = lc.Lattice("A2").discriminant_group()
    elements = _cyclic_elements_by_coefficient(form)

    assert form.invariants() == (3,)
    assert {coeff: form.q(element) for coeff, element in elements.items()} == {
        (0,): 0,
        (1,): QQ(2) / 3,
        (2,): QQ(2) / 3,
    }
    assert {
        (left, right): form.b(left_element, right_element)
        for left, left_element in elements.items()
        for right, right_element in elements.items()
    } == {
        ((0,), (0,)): 0,
        ((0,), (1,)): 0,
        ((0,), (2,)): 0,
        ((1,), (0,)): 0,
        ((1,), (1,)): QQ(2) / 3,
        ((1,), (2,)): QQ(1) / 3,
        ((2,), (0,)): 0,
        ((2,), (1,)): QQ(1) / 3,
        ((2,), (2,)): QQ(2) / 3,
    }

    assert set(form.isotropic_elements()) == {form.zero()}
    assert form.is_anisotropic()
    assert not form.is_metabolic()
    assert form.lagrangian_subgroups() == ()
