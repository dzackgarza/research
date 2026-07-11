from __future__ import annotations

import sage_lattice_category_spike.lattice_categories as lc


def test_a2_e6_glued_e8_orthogonal_complements_match_conway_sloane():
    r"""Conway-Sloane Ch. 4 identifies E_6 as the orthogonal complement of
    A_2 in E_8, and Nikulin Cor. 1.6.2 identifies the discriminant forms of
    complementary primitive sublattices in an even unimodular lattice by
    anti-isometry. This exercises ``orthogonal_complement`` inside the nontrivial
    A_2 + E_6 overlattice that reconstructs E_8, not just a direct-sum block.
    """
    a2 = lc.Lattice("A2")
    e6 = lc.Lattice("E6")
    ambient = a2.direct_sum(e6)
    discriminant_form = ambient.discriminant_group()
    glue = discriminant_form.subgroup_generated_by(
        [discriminant_form.gen(0) + 2 * discriminant_form.gen(1)]
    )
    glued = discriminant_form.overlattice_from_isotropic_subgroup(glue)

    assert discriminant_form.is_isotropic_subgroup(glue)
    assert glued.is_even() and glued.is_unimodular()
    assert glued.is_isometric(lc.Lattice("E8"))

    a2_in_e8 = glued.subobject(
        [glued([1, 0, 0, 0, 0, 0, 0, 0]), glued([0, 1, 0, 0, 0, 0, 0, 0])],
        label="A2_in_E8",
    )
    e6_in_e8 = glued.subobject(
        [glued(row) for row in ([0]*i + [1] + [0]*(7-i) for i in range(2, 8))],
        label="E6_in_E8",
    )

    assert glued.is_primitive(a2_in_e8) and glued.is_primitive(e6_in_e8)
    assert a2_in_e8.is_isometric(a2)
    assert e6_in_e8.is_isometric(e6)

    complement_of_a2 = glued.orthogonal_complement(a2_in_e8)
    complement_of_e6 = glued.orthogonal_complement(e6_in_e8)
    assert complement_of_a2.is_isometric(e6)
    assert complement_of_e6.is_isometric(a2)
    assert complement_of_a2.discriminant_group().is_isomorphic(
        a2_in_e8.discriminant_group().twist(-1),
        kind="quadratic",
    )
    assert complement_of_e6.discriminant_group().is_isomorphic(
        e6_in_e8.discriminant_group().twist(-1),
        kind="quadratic",
    )
