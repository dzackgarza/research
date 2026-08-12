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
    gluing = form.overlattice_from_isotropic_subgroup(subgroup)
    glued = gluing.codomain()

    assert gluing.index() == 2
    assert quotient.invariants() == ()
    assert quotient.order() == 1
    assert glued.is_even()
    assert glued.is_unimodular()
    assert glued.signature_pair() == (1, 1)
    assert glued.discriminant_group().invariants() == ()


def test_conway_sloane_d8_isotropic_self_glue_reconstructs_e8():
    """Conway-Sloane's D8+ glue uses an isotropic D8 glue class to obtain E8."""

    d8 = lc.Lattice("D8(-1)")
    e8 = lc.Lattice("E8(-1)")
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
        glued = form.overlattice_from_isotropic_subgroup(subgroup).codomain()

        assert form.q(glue_vector) == 0
        assert form.is_lagrangian(subgroup)
        assert glued.is_even()
        assert glued.is_unimodular()
        assert len(glued.roots()) == 240
        assert glued.is_isometric(e8)


def test_conway_sloane_d8_maximal_overlattice_is_the_d8_plus_e8_glue():
    """The public maximal-overlattice search should find CS99's D8+ = E8 glue.

    Conway-Sloane Ch. 4 lists D8+ as the even unimodular E8 lattice obtained by
    adjoining isotropic D8 glue. Nikulin Prop. 1.4.1 identifies that operation
    with passing to an even overlattice from an isotropic subgroup.
    """
    d8 = lc.Lattice("D8(-1)")
    e8 = lc.Lattice("E8(-1)")

    full_embedding = d8.maximal_overlattice()
    two_primary_embedding = d8.maximal_overlattice(2)
    three_primary_embedding = d8.maximal_overlattice(3)

    for embedding in (full_embedding, two_primary_embedding):
        maximal = embedding.codomain()
        assert embedding.index() == 2                      # [E8 : D8] = 2
        assert maximal.is_even()
        assert maximal.is_unimodular()
        assert maximal.determinant() == 1
        assert maximal.minimum() == 2
        assert len(maximal.roots()) == 240
        assert maximal.discriminant_group().invariants() == ()
        assert maximal.is_isometric(e8)
        assert abs(ZZ(d8.determinant() / maximal.determinant())) == embedding.index() ** 2

    # no 3-primary glue exists: the maximal 3-overlattice is D8 itself, and
    # the witness says so -- the composed embedding is the identity
    assert three_primary_embedding.is_identity()
    three_primary_maximal = three_primary_embedding.codomain()
    assert three_primary_maximal.determinant() == d8.determinant()
    assert three_primary_maximal.discriminant_group().invariants() == (2, 2)
    assert len(three_primary_maximal.roots()) == 112
    assert three_primary_maximal.is_isometric(d8)


def test_conway_sloane_a2_discriminant_form_is_anisotropic_and_nonmetabolic():
    """A2 has glue group C3; in Cartan normalization its exact finite q is 2/3.

    Conway-Sloane list the A2 glue group as cyclic of order three.  Combining
    that with Nikulin's discriminant-form definition gives the exact q and b
    tables below for the Cartan-normalized root lattice.
    """

    form = lc.Lattice("A2(-1)").discriminant_group()
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


def test_nikulin_non_lagrangian_u2_a2_glue_leaves_a2_discriminant_form():
    r"""Nikulin Prop. 1.4.1 gives q_{S'} = H^\perp/H for overlattice glue.

    For S = U(2) (+) A2, gluing along one U(2) order-two isotropic subgroup is
    not Lagrangian; the remaining quotient is the A2 discriminant form C3 with
    q([1]) = q([2]) = 2/3 from the Conway-Sloane A2 glue table.
    """
    lattice = lc.Lattice("U").twist(2).direct_sum(lc.Lattice("A2(-1)"))
    form = lattice.discriminant_group()
    glue_vector = next(
        element
        for element in form.isotropic_elements()
        if _coordinates(form, element) == (1, 0)
    )
    subgroup = form.subgroup_generated_by([glue_vector])

    assert lattice.is_even()
    assert lattice.signature_pair() == (3, 1)
    assert lattice.determinant() == -12
    assert form.invariants() == (2, 6)
    assert form.is_isotropic_subgroup(subgroup)
    assert not form.is_lagrangian(subgroup)
    assert sorted(_coordinates(form, element) for element in form.isotropic_elements()) == [
        (0, 0),
        (1, 0),
        (1, 3),
    ]

    assert sorted(
        _coordinates(form, element)
        for element in form.orthogonal(subgroup).elements()
    ) == [(0, 0), (0, 2), (0, 4), (1, 0), (1, 2), (1, 4)]
    quotient = form.orthogonal_quotient(subgroup)
    overlattice = form.overlattice_from_isotropic_subgroup(subgroup).codomain()
    overlattice_form = form.discriminant_form_of_overlattice(subgroup)

    assert quotient.invariants() == (3,)
    assert overlattice_form.is_isomorphic(quotient, kind="quadratic")
    assert overlattice.determinant() == -3
    assert overlattice.signature_pair() == lattice.signature_pair()
    assert overlattice.discriminant_group().invariants() == (3,)
    assert abs(ZZ(lattice.determinant() / overlattice.determinant())) == 4

    elements = _cyclic_elements_by_coefficient(overlattice_form)
    assert {coeff: overlattice_form.q(element) for coeff, element in elements.items()} == {
        (0,): 0,
        (1,): QQ(2) / 3,
        (2,): QQ(2) / 3,
    }


def test_nikulin_local_modification_accepts_public_primary_subgroup_objects():
    r"""Nikulin Prop. 1.4.1 is p-local on primary discriminant parts.

    For S = A2 (+) A2(-1) (+) U(2), the 2-primary and 3-primary parts each
    contain nontrivial isotropic subgroups. The public local_modification API
    should accept the subgroup objects returned by the public p-primary
    discriminant form, not only a copied generator list.
    """
    lattice = lc.Lattice("A2(-1)").direct_sum(lc.Lattice("A2(-1)").twist(-1)).direct_sum(
        lc.Lattice("U").twist(2)
    )

    assert lattice.is_even()
    assert lattice.signature_pair() == (3, 3)
    assert lattice.determinant() == -36
    assert lattice.discriminant_group().invariants() == (6, 6)

    expected = {
        2: {"determinant": -9, "invariants": (3, 3), "determinant_ratio": 4},
        3: {"determinant": -4, "invariants": (2, 2), "determinant_ratio": 9},
    }
    for p, row in expected.items():
        primary_form = lattice.discriminant_group(primary=p)
        subgroup = next(
            subgroup
            for subgroup in primary_form.isotropic_subgroups()
            if subgroup.cardinality() == p
        )
        modified = lattice.local_modification(subgroup, p)

        assert modified.is_even()
        assert modified.signature_pair() == lattice.signature_pair()
        assert modified.determinant() == row["determinant"]
        assert modified.discriminant_group().invariants() == row["invariants"]
        assert abs(ZZ(lattice.determinant() / modified.determinant())) == row["determinant_ratio"]
