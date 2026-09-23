from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FiniteGroups,
    FiniteGSets,
    FractionFieldQuotients,
    Lattices,
    TorsionBilinearFormModules,
    TorsionQuadraticFormModules,
)

ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/framed/formed/torsionform/torsion_modules_with_form.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py",
    "owner_overrides": {
        "DiscriminantForms": "src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py",
        "DiscriminantForms.super_categories": "src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py",
        "DiscriminantForms.ParentMethods": "src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py",
        "DiscriminantForms.ParentMethods.correlation": "src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py",
        "DiscriminantForms.ParentMethods.source_lattice": "src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py",
        "DiscriminantForms.ParentMethods.overlattice_from_isotropic_subobject": "src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py",
        "DiscriminantForms.ParentMethods.discriminant_form_of_overlattice": "src/dzack_research/preamble/categories/modules/framed/formed/discriminant_modules.py",
    },
    "disposition": "reconciled-live-owner",
}

def _matrix(ring, rows):
    rows = tuple(tuple(row) for row in rows)
    columns = 0 if not rows else len(rows[0])
    return ring.matrix_space(len(rows), columns).from_rows(rows)



def test_bilinear_torsion_form_descends_from_relations_and_gram() -> None:
    values = FractionFieldQuotients(ZZ)(1)
    form = TorsionBilinearFormModules(ZZ).from_relations_and_gram(_matrix(ZZ, [[2]]), _matrix(QQ, [[QQ(1) / 2]]), values)
    generator = form.module_generators()[0]

    assert form.cardinality() == 2
    assert form.value_module() is values
    assert form.b(generator, generator) == values(QQ(1) / 2)
    assert form.b(2 * generator, generator) == values.zero()


def test_bilinear_torsion_form_rejects_non_descending_gram() -> None:
    values = FractionFieldQuotients(ZZ)(1)
    try:
        TorsionBilinearFormModules(ZZ).from_relations_and_gram(_matrix(ZZ, [[2]]), _matrix(QQ, [[QQ(1) / 4]]), values)
    except ValueError as error:
        assert "does not descend" in str(error)
    else:
        raise AssertionError("a non-descending bilinear form was accepted")


def test_quadratic_torsion_form_and_its_bilinear_polarization() -> None:
    quadratic_values = FractionFieldQuotients(ZZ)(2)
    form = TorsionQuadraticFormModules(ZZ).from_relations_and_gram(_matrix(ZZ, [[2]]), _matrix(QQ, [[QQ(1) / 2]]), quadratic_values)
    generator = form.module_generators()[0]
    bilinear = form.associated_bilinear_form()
    bilinear_generator = bilinear.module_generators()[0]

    assert form.q(generator) == quadratic_values(QQ(1) / 2)
    assert form.q(2 * generator) == quadratic_values.zero()
    assert bilinear.value_module().modulus() == 1
    assert bilinear.b(bilinear_generator, bilinear_generator) == bilinear.value_module()(QQ(1) / 2)


def test_quadratic_torsion_form_rejects_relation_with_nonzero_norm() -> None:
    values = FractionFieldQuotients(ZZ)(2)
    try:
        TorsionQuadraticFormModules(ZZ).from_relations_and_gram(_matrix(ZZ, [[2]]), _matrix(QQ, [[QQ(1) / 4]]), values)
    except ValueError as error:
        assert "does not descend" in str(error)
    else:
        raise AssertionError("a non-descending quadratic form was accepted")


def test_bilinear_invariant_factor_form_is_a_form_preserving_isomorphism() -> None:
    values = FractionFieldQuotients(ZZ)(1)
    form = TorsionBilinearFormModules(ZZ).from_relations_and_gram(
        _matrix(ZZ, [[2, 0], [0, 1]]),
        _matrix(QQ, [[QQ(1) / 2, 0], [0, 0]]),
        values,
    )
    normalization = form.invariant_factor_form()
    normalized = normalization.codomain()

    assert form.number_of_module_generators() == 2
    assert normalized.number_of_module_generators() == 1
    assert normalized.value_module() is values
    for generator in form.module_generators():
        assert normalization.inverse()(normalization(generator)) == generator
    for left in form.module_generators():
        for right in form.module_generators():
            assert form.b(left, right) == normalized.b(
                normalization(left), normalization(right)
            )


def test_quadratic_invariant_factor_form_is_a_form_preserving_isomorphism() -> None:
    values = FractionFieldQuotients(ZZ)(2)
    form = TorsionQuadraticFormModules(ZZ).from_relations_and_gram(
        _matrix(ZZ, [[2, 0], [0, 1]]),
        _matrix(QQ, [[QQ(1) / 2, 0], [0, 0]]),
        values,
    )
    normalization = form.invariant_factor_form()
    normalized = normalization.codomain()

    assert form.number_of_module_generators() == 2
    assert normalized.number_of_module_generators() == 1
    assert normalized.value_module() is values
    for generator in form.module_generators():
        assert normalization.inverse()(normalization(generator)) == generator
        assert form.q(generator) == normalized.q(normalization(generator))


def test_owned_quadratic_orthogonal_group_uses_live_form_automorphisms() -> None:
    values = FractionFieldQuotients(ZZ)(2)
    form = TorsionQuadraticFormModules(ZZ).from_relations_and_gram(
        _matrix(ZZ, [[8]]),
        _matrix(QQ, [[QQ(1) / 8]]),
        values,
    )
    group = form.orthogonal_group()
    generator = form.module_generators()[0]
    category = TorsionQuadraticFormModules(ZZ)

    assert group is form.O()
    assert group is category.Aut(form)
    assert group is category.Iso(form, form)
    assert group in FiniteGroups()
    assert group.order() == 2
    assert all(automorphism.parent() is group for automorphism in group.group_generators())
    assert all(
        form.q(automorphism(generator)) == form.q(generator)
        for automorphism in group.group_generators()
    )
    trivial = group.subgroup_on((group.one(),))
    assert trivial.supergroup() is group
    from dzack_research.preamble.categories.group.groups import Subgroups

    assert trivial in Subgroups(group)
    assert trivial.inclusion().codomain() is group
    assert all(trivial.inclusion()(element) is element for element in trivial)


def test_bilinear_and_quadratic_orthogonal_groups_are_not_conflated() -> None:
    values = FractionFieldQuotients(ZZ)(2)
    quadratic = TorsionQuadraticFormModules(ZZ).from_relations_and_gram(
        _matrix(ZZ, [[8]]),
        _matrix(QQ, [[QQ(1) / 8]]),
        values,
    )
    bilinear = quadratic.associated_bilinear_form()

    assert quadratic.orthogonal_group().order() == 2
    assert bilinear.orthogonal_group().order() == 4
    assert quadratic.orthogonal_group().domain() is quadratic
    assert bilinear.orthogonal_group().domain() is bilinear


def test_mixed_prime_jordan_framing_is_distinct_and_has_an_explicit_isometry() -> None:
    form = (Lattices(ZZ)("A2") + Lattices(ZZ)("A1")).discriminant_quadratic_form()
    decomposition = form.p_adic_jordan_decomposition()
    normalization = form.p_adic_jordan_form()
    jordan = normalization.codomain()

    assert tuple(decomposition.index_set()) == (ZZ(2), ZZ(3))
    assert tuple(generator.additive_order() for generator in decomposition[ZZ(2)]) == (2,)
    assert tuple(generator.additive_order() for generator in decomposition[ZZ(3)]) == (3,)
    assert form.invariant_factor_form().codomain().module_generators().cardinality() == 1
    assert jordan.module_generators().cardinality() == 2
    assert jordan.cardinality() == form.cardinality() == 6
    assert all(
        left.b(right) == form.bilinear_value_module().zero()
        for left in decomposition[ZZ(2)]
        for right in decomposition[ZZ(3)]
    )
    for generator in form.module_generators():
        assert normalization.inverse()(normalization(generator)) == generator
        assert jordan.q(normalization(generator)) == form.q(generator)


def test_bilinear_anti_isometry_is_isometry_to_the_negative_twist() -> None:
    values = FractionFieldQuotients(ZZ)(1)
    form = TorsionBilinearFormModules(ZZ).from_relations_and_gram(
        [[3]],
        [[QQ(1) / 3]],
        values,
    )

    assert not form.is_anti_isometric(form)
    assert form.is_anti_isometric(form.twist(-1))
    assert form.twist(-1).is_isomorphic(form.twist(-1))


def test_bilinear_jordan_form_preserves_the_pairing() -> None:
    form = (Lattices(ZZ)("A2") + Lattices(ZZ)("A1")).discriminant_bilinear_form()
    normalization = form.p_adic_jordan_form()
    jordan = normalization.codomain()

    assert tuple(form.p_adic_jordan_decomposition().index_set()) == (ZZ(2), ZZ(3))
    for left in form.module_generators():
        for right in form.module_generators():
            assert jordan.b(normalization(left), normalization(right)) == form.b(left, right)


def test_generic_bilinear_torsion_form_retains_subobjects_orbits_and_metabolizers() -> None:
    values = FractionFieldQuotients(ZZ)(1)
    form = TorsionBilinearFormModules(ZZ).from_relations_and_gram(
        _matrix(ZZ, [[2, 0], [0, 2]]),
        _matrix(QQ, [[0, QQ(1) / 2], [QQ(1) / 2, 0]]),
        values,
    )
    first, second = tuple(form.module_generators())

    assert form.is_anisotropic() is False
    assert form.subobject_generated_by((first,)).cardinality() == 2
    assert form.orthogonal_subobject(
        form.subobject_generated_by((first,))
    ).cardinality() == 2

    lagrangians = form.lagrangian_subobjects()
    assert lagrangians.cardinality() == 3
    assert form.is_metabolic()
    metabolizer = form.metabolizer()
    assert metabolizer.cardinality() == 2
    assert form.orthogonal_quotient(metabolizer).cardinality() == 1

    group = form.orthogonal_group()
    action = group.element_action()
    assert action in FiniteGSets(group)

    isotropic_orbits = form.orbits_on_isotropic_subobjects()
    assert sorted(int(orbit.cardinality()) for orbit in isotropic_orbits) == [1, 3]
    assert form.orbit(first).cardinality() == 3
    assert second in form.orbit(first)

    stabilizer = group.stabilizer_of_element(first)
    assert stabilizer.supergroup() is group
    assert group.one() in stabilizer
    assert all(
        automorphism(first) == first
        for automorphism in group
        if automorphism in stabilizer
    )

    line = form.subobject_generated_by((first,))
    line_stabilizer = group.stabilizer_of_subobject(line)
    line_elements = frozenset(line.inclusion()(element) for element in line.elements())
    assert line_stabilizer.supergroup() is group
    assert all(
        frozenset(automorphism(element) for element in line_elements) == line_elements
        for automorphism in group
        if automorphism in line_stabilizer
    )


def test_generic_torsion_form_reframing_and_primary_components_are_live_objects() -> None:
    values = FractionFieldQuotients(ZZ)(1)
    form = TorsionBilinearFormModules(ZZ).from_relations_and_gram(
        _matrix(ZZ, [[2, 0], [0, 3]]),
        _matrix(QQ, [[QQ(1) / 2, 0], [0, QQ(1) / 3]]),
        values,
    )
    generators = tuple(form.module_generators())
    reframing = form.reframing_isometry(generators)
    components = form.primary_components()
    gram = form.gram_matrix()

    assert reframing.domain() is form
    assert tuple(reframing.codomain().invariant_factors()) == tuple(form.invariant_factors())
    assert form.regenerate(generators) is reframing.codomain()
    assert tuple(components.index_set()) == (ZZ(2), ZZ(3))
    assert components[ZZ(2)].cardinality() == 2
    assert components[ZZ(3)].cardinality() == 3
    assert gram[0, 0] == QQ(1) / 2
    assert gram[1, 1] == QQ(1) / 3


def test_literal_cokernel_forms_retain_the_cover_projection_and_coset_lifts() -> None:
    correlation = Lattices(ZZ)("A1").correlation_morphism()
    bilinear = TorsionBilinearFormModules(ZZ).cokernel(correlation)
    quadratic = TorsionQuadraticFormModules(ZZ).cokernel(correlation)

    for form in (bilinear, quadratic):
        projection = form.projection()
        generator = next(iter(form.module_generators()))
        representative = generator.coset_representative()

        assert form.presentation() is correlation
        assert form.cover() is correlation.codomain()
        assert projection.domain() is correlation.codomain()
        assert projection.codomain() is form
        assert projection(representative) == generator
        assert form.cardinality() == 2

    generator = next(iter(bilinear.module_generators()))
    assert bilinear.b(generator, generator) == bilinear.value_module()(QQ(-1) / 2)
    q_generator = next(iter(quadratic.module_generators()))
    assert quadratic.q(q_generator) == quadratic.value_module()(QQ(-1) / 2)
