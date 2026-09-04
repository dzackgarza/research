import pytest
from sage.misc.unknown import Unknown

from dzack_research.preamble.all import (
    FiniteGroups,
    Lattices,
    MatrixSpace,
    MatrixSpaces,
    QQ,
    Set,
    signature_pair,
    tensor,
    ZZ,
)
from dzack_research.preamble.tensors import Tensor


def test_lll_is_a_change_of_framing_with_actual_isometry_witness() -> None:
    lattice = Lattices(ZZ)([[4, 1], [1, 2]])
    reduction = lattice.lll_reduction()
    reduced = reduction.reduced

    assert lattice.is_positive_definite()
    assert reduced.is_positive_definite()
    assert reduction.isometry.domain() is reduced
    assert reduction.isometry.codomain() is lattice
    assert reduced.gram_tensor() == lattice.gram_tensor().pullback(
        reduction.change_of_basis_matrix
    )
    for generator in reduced.module_generators():
        assert generator.q() == reduction.isometry(generator).q()


def test_bkz_and_hkz_are_reframings_with_exact_isometry_witnesses() -> None:
    lattice = Lattices(ZZ)([[10, 3, 1], [3, 8, 2], [1, 2, 6]])

    for reduction in (lattice.bkz_reduction(block_size=2), lattice.hkz_reduction()):
        assert reduction.isometry.domain() is reduction.reduced
        assert reduction.isometry.codomain() is lattice
        assert reduction.reduced.gram_tensor() == lattice.gram_tensor().pullback(
            reduction.change_of_basis_matrix
        )
        assert abs(reduction.change_of_basis_matrix.det()) == 1


def test_negative_definite_root_lattice_shortest_vectors_are_actual_roots() -> None:
    a2 = Lattices(ZZ)("A2")
    assert a2.is_negative_definite()
    assert a2.minimum() == -2
    shortest = a2.shortest_vectors()
    assert shortest.cardinality() == 6
    assert all(vector.q() == -2 and vector.is_root() for vector in shortest)
    assert a2.kissing_number() == 6


def test_square_lattice_minimum_theta_and_packing_radius() -> None:
    lattice = Lattices(ZZ)(2)
    assert lattice.minimum() == 1
    assert lattice.vectors_of_square(1).cardinality() == 4
    theta = lattice.theta_series(5)
    assert theta[0] == 1
    assert theta[1] == 4
    assert lattice.packing_radius() == QQ(1) / 2
    assert lattice.kissing_number() == 4


def test_definite_isometry_decision_returns_an_actual_odd_lattice_witness() -> None:
    lattice = Lattices(ZZ)([[3, 1], [1, 2]])
    change = MatrixSpace(ZZ, 2, 2).from_rows([[1, 1], [0, 1]])
    reframed_gram = lattice.gram_tensor().pullback(change)
    reframed = Lattices(ZZ)(reframed_gram)

    homset = reframed.Isom(lattice)
    assert homset.is_empty() is False
    witness = homset.an_element()
    assert witness.matrix().parent() in MatrixSpaces(ZZ)
    for left in reframed.module_generators():
        for right in reframed.module_generators():
            assert reframed.b(left, right) == lattice.b(
                witness(left), witness(right)
            )
    assert reframed.is_isometric(lattice) is True
    assert reframed.is_isometric(Lattices(ZZ)([[1, 0], [0, 1]])) is False


def test_exact_cvp_babai_minima_and_voronoi_geometry_on_square_lattice() -> None:
    lattice = Lattices(ZZ)(2)
    e1, _e2 = lattice.module_generators()
    target = (QQ(3) / 4, QQ(1) / 4)

    assert lattice.closest_vector(target) == e1
    assert lattice.babai(target) == e1
    assert lattice.successive_minima() == (1, 1)
    assert lattice.hadamard_ratio() == 1
    assert lattice.covering_radius() ** 2 == QQ(1) / 2
    assert lattice.center_density() == QQ(1) / 4
    assert lattice.contact_polytope().n_vertices() == 4
    assert lattice.voronoi_relevant_vectors().cardinality() == 4


def test_root_enumeration_and_root_sublattice_are_formed_and_embedded() -> None:
    lattice = Lattices(ZZ)("A2")
    roots = lattice.roots()

    assert roots.cardinality() == 6
    assert lattice.roots_of_square(-2) == roots
    assert lattice.vectors_of_square_and_divisibility(-2, 1) == roots
    root_sublattice = lattice.root_sublattice()
    assert root_sublattice.rank() == 2
    assert root_sublattice.inclusion().codomain() is lattice
    assert str(root_sublattice.cartan_type()) == "['A', 2]"


def test_owned_lattice_orthogonal_group_uses_sage_only_as_definite_engine() -> None:
    lattice = Lattices(ZZ)("A2")
    group = lattice.orthogonal_group()

    assert group is lattice.Aut()
    assert group is lattice.bilinear_orthogonal_group()
    assert group is lattice.quadratic_orthogonal_group()
    assert group in FiniteGroups()
    assert group.order() == 12
    for automorphism in group.group_generators():
        assert automorphism.parent() is group
        assert automorphism.matrix().parent() in MatrixSpaces(ZZ)
        for left in lattice.module_generators():
            for right in lattice.module_generators():
                assert lattice.b(left, right) == lattice.b(
                    automorphism(left), automorphism(right)
                )


def test_isometry_homset_is_a_torsor_under_codomain_orthogonal_group() -> None:
    source = Lattices(ZZ)([[4, 1], [1, 2]])
    reduction = source.lll_reduction()
    target = reduction.reduced
    homset = source.Isom(target)
    first = homset.an_element()
    automorphism = next(iter(target.Aut().group_generators()))
    second = homset.act(automorphism, first)
    transporter = homset.transporter(first, second)

    assert transporter.parent() is target.Aut()
    for generator in source.module_generators():
        assert transporter(first(generator)) == second(generator)
        assert homset.act(transporter, first)(generator) == second(generator)


def test_similarity_is_an_isometry_from_the_scaled_twist() -> None:
    source = Lattices(ZZ)([[2]])
    target = Lattices(ZZ)([[6]])

    assert source.is_similar(target, 3) is True
    similarity = source.similarity(3, codomain=target)
    assert similarity.domain().gram_tensor().is_equal_tensor(source.twist(3).gram_tensor())
    assert similarity.codomain() is target
    generator = source.module_generators()[0]
    twisted_generator = similarity.domain().module_generators()[0]
    assert target.q(similarity(twisted_generator)) == 3 * source.q(generator)


def test_indefinite_isometry_ladder_uses_parity_as_an_exact_obstruction() -> None:
    even = Lattices(ZZ)("U")
    odd = Lattices(ZZ)([[1, 0], [0, -1]])

    assert even.signature_pair() == odd.signature_pair() == signature_pair(1, 1)
    assert even.Isom(odd).is_empty() is True
    assert even.is_isometric(odd) is False


def test_nikulin_and_eichler_nonemptiness_do_not_invent_witnesses() -> None:
    hyperbolic = Lattices(ZZ)("U")
    reframed_hyperbolic = Lattices(ZZ)([[2, 1], [1, 0]])
    nikulin_homset = hyperbolic.Isom(reframed_hyperbolic)

    assert nikulin_homset.is_empty() is False
    with pytest.raises(NotImplementedError, match="Nikulin"):
        nikulin_homset.an_element()

    source = Lattices(ZZ)([[0, 1, 0], [1, 0, 0], [0, 0, -6]])
    change = MatrixSpace(ZZ, 3, 3).from_rows([[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    target = Lattices(ZZ)(source.gram_tensor().pullback(change))
    eichler_homset = source.Isom(target)

    assert not source.is_p_elementary(2)
    assert eichler_homset.is_empty() is False
    with pytest.raises(NotImplementedError, match="Eichler"):
        eichler_homset.an_element()


def test_unresolved_odd_indefinite_binary_isometry_remains_unknown() -> None:
    source = Lattices(ZZ)([[1, 0], [0, -1]])
    change = MatrixSpace(ZZ, 2, 2).from_rows([[1, 2], [0, 1]])
    target = Lattices(ZZ)(source.gram_tensor().pullback(change))

    assert source.gram_tensor().is_equal_tensor(target.gram_tensor()) is False
    assert source.Isom(target).is_empty() is Unknown
    assert source.is_isometric(target) is Unknown


def test_indefinite_isometry_backend_supplies_exact_witness_when_available(monkeypatch) -> None:
    from py_polyhedral import binaries as polyhedral

    source = Lattices(ZZ)([[1, 0], [0, -1]])
    change = MatrixSpace(ZZ, 2, 2).from_rows([[1, 2], [0, 1]])
    target = Lattices(ZZ)(source.gram_tensor().pullback(change))
    backend_rows = [[1, 0], [-2, 1]]

    monkeypatch.setattr(
        polyhedral,
        "binary_available",
        lambda name: name == "INDEF_FORM_TestEquivalence",
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_test_equivalence",
        lambda _codomain_gram, _domain_gram: backend_rows,
    )

    homset = source.Isom(target)
    assert homset.is_empty() is False
    witness = homset.an_element()
    assert witness.domain() is source and witness.codomain() is target
    assert target.gram_tensor().pullback(witness).is_equal_tensor(
        source.gram_tensor()
    )


def test_definite_target_embedding_homset_enumerates_all_a1_into_a2_roots() -> None:
    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)("A2")
    homset = source.Emb(target)
    embeddings = homset

    assert homset.cardinality() == 6
    source_generator = source.module_generators()[0]
    images = Set(embedding(source_generator) for embedding in embeddings)
    assert images == Set(target.roots())
    assert homset.is_empty() is False
    assert homset.an_element()(source_generator) in images


def test_definite_target_embedding_homset_detects_sign_obstruction() -> None:
    source = Lattices(ZZ)([[2]])
    target = Lattices(ZZ)("A2")
    homset = source.Emb(target)

    assert homset.is_empty()
    assert homset.is_empty() is True
    with pytest.raises(ValueError, match="embedding homset is empty"):
        homset.an_element()


def test_even_overlattice_inclusions_enumerate_isotropic_glue_for_u2() -> None:
    lattice = Lattices(ZZ)([[0, 2], [2, 0]])
    inclusions = lattice.even_overlattice_inclusions()

    assert inclusions.cardinality() == 3
    assert sorted(int(inclusion.index()) for inclusion in inclusions) == [1, 2, 2]
    assert all(inclusion.codomain().is_even() for inclusion in inclusions)
    assert sum(inclusion.codomain().is_unimodular() for inclusion in inclusions) == 2


def test_nikulin_even_unimodular_embedding_existence_controls_embedding_homset() -> None:
    target = Lattices(ZZ)("U")
    a1 = Lattices(ZZ)("A1")
    a2 = Lattices(ZZ)("A2")
    odd = Lattices(ZZ)([[-1]])

    assert a1.embeds_in_even_unimodular(1, 1)
    assert not a2.embeds_in_even_unimodular(1, 1)
    assert a1.Emb(target).is_empty() is False
    assert a2.Emb(target).is_empty() is True
    assert odd.Emb(target).is_empty() is True


def test_explicit_even_unimodular_embedding_crosses_oscar_data_into_live_morphism(monkeypatch) -> None:
    from dzack_research.preamble.categories import lattice_engines

    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)("U")
    target_gram = target.gram_tensor()
    embedding_matrix = MatrixSpace(ZZ, 2, 1).from_rows([[1], [-1]])

    monkeypatch.setattr(
        lattice_engines,
        "oscar_even_unimodular_primitive_embedding",
        lambda _gram, _positive, _negative: (target_gram, embedding_matrix),
    )

    primitive = source.embed_in_even_unimodular(1, 1)
    assert primitive.is_primitive()
    generator = source.module_generators()[0]
    assert primitive(generator).q() == generator.q() == -2
    assert primitive.codomain().is_even() and primitive.codomain().is_unimodular()

    requested = source.Emb(target).an_element()
    assert requested.domain() is source and requested.codomain() is target
    assert requested(generator).q() == -2


def test_discriminant_functor_and_representation_use_live_form_isometries() -> None:
    lattice = Lattices(ZZ)("A2")
    automorphisms = lattice.Aut()
    discriminant = lattice.discriminant_group()
    representation = lattice.discriminant_representation()

    assert representation.domain() is automorphisms
    assert representation.codomain() is discriminant.O()
    for automorphism in automorphisms.group_generators():
        induced = automorphism.discriminant_isometry()
        represented = representation(automorphism)
        assert represented.parent() is discriminant.O()
        for generator in discriminant.module_generators():
            assert represented(generator) == induced(generator)
            assert induced.inverse()(induced(generator)) == generator

    image = lattice.discriminant_image()
    assert image.cardinality() == discriminant.O().cardinality() == 2
    assert lattice.discriminant_representation_is_surjective()

    stable = lattice.stable_orthogonal_group()
    assert automorphisms.one() in stable
    assert all(
        representation(automorphism) == discriminant.O().one()
        for automorphism in automorphisms
        if automorphism in stable
    )

    special = lattice.SO()
    determinant_one = tuple(
        automorphism for automorphism in automorphisms if automorphism.determinant() == 1
    )
    assert len(determinant_one) == 6
    assert all(automorphism in special for automorphism in determinant_one)
    assert all(
        (automorphism in special) == (automorphism.determinant() == 1)
        for automorphism in automorphisms
    )


def test_discriminant_functor_acts_on_isometries_between_distinct_lattices() -> None:
    source = Lattices(ZZ)([[3, 1], [1, 2]])
    change = MatrixSpace(ZZ, 2, 2).from_rows([[1, 1], [0, 1]])
    target = Lattices(ZZ)(source.gram_tensor().pullback(change))
    isometry = source.Isom(target).an_element()
    induced = isometry.discriminant_isometry()

    assert induced.domain() is source.discriminant_group()
    assert induced.codomain() is target.discriminant_group()
    for generator in induced.domain().module_generators():
        assert induced.inverse()(induced(generator)) == generator


def test_discriminant_inclusion_is_extension_by_zero_for_an_orthogonal_summand() -> None:
    summand = Lattices(ZZ)("A1")
    complement = Lattices(ZZ)("A2")
    ambient = summand + complement
    ambient_generators = ambient.module_generators()
    inclusion = summand.Emb(ambient)((ambient_generators[0],))
    discriminant_inclusion = inclusion.discriminant_inclusion()

    source = summand.discriminant_quadratic_form()
    target = ambient.discriminant_quadratic_form()
    assert discriminant_inclusion.domain() is source
    assert discriminant_inclusion.codomain() is target
    assert discriminant_inclusion.is_injective()
    assert source.cardinality() == 2
    assert target.cardinality() == 6
    for generator in source.module_generators():
        assert target.q(discriminant_inclusion(generator)) == source.q(generator)


def test_discriminant_inclusion_rejects_a_non_direct_finite_index_embedding() -> None:
    source = Lattices(ZZ)([[4]])
    target = Lattices(ZZ)([[1]])
    target_generator = target.module_generators()[0]
    inclusion = source.Emb(target)((2 * target_generator,))

    with pytest.raises(ValueError, match="not an orthogonal direct summand"):
        inclusion.discriminant_inclusion()


def test_discriminant_inclusion_forgets_quadratic_refinement_in_an_odd_ambient() -> None:
    summand = Lattices(ZZ)("A1")
    ambient = summand + Lattices(ZZ)([[1]])
    inclusion = summand.Emb(ambient)((ambient.module_generators()[0],))
    induced = inclusion.discriminant_inclusion()

    assert induced.domain() is summand.discriminant_bilinear_form()
    assert induced.codomain() is ambient.discriminant_bilinear_form()
    for generator in induced.domain().module_generators():
        assert induced.codomain().b(induced(generator), induced(generator)) == induced.domain().b(
            generator, generator
        )


def test_primitive_complement_glue_map_is_the_discriminant_anti_isometry() -> None:
    ambient = Lattices(ZZ)("U")
    e, f = ambient.module_generators()
    first = ambient.subobject_on((e + f,))
    second = ambient.subobject_on((e - f,))
    glue = ambient.glue_map(first, second)

    assert first.is_primitive() and second.is_primitive()
    assert first.sum(second).index() == 2
    assert glue.domain().cardinality() == glue.codomain().cardinality() == 2
    assert glue.domain().inclusion().codomain() is first.discriminant_quadratic_form()
    assert (
        glue.codomain().inclusion().codomain().unformed_module()
        is second.discriminant_quadratic_form()
    )
    for generator in glue.domain().module_generators():
        assert glue.domain().q(generator) == glue.codomain().q(glue(generator))


def test_primitive_extension_with_no_glue_returns_the_zero_anti_isometry() -> None:
    left = Lattices(ZZ)("A1")
    right = Lattices(ZZ)("A2")
    ambient = left + right
    generators = ambient.module_generators()
    first = ambient.subobject_on((generators[0],))
    second = ambient.subobject_on(generators[1:])
    glue = ambient.glue_map(first, second)

    assert first.sum(second).index() == 1
    assert glue.domain().cardinality() == 1
    assert glue.codomain().cardinality() == 1
    assert glue.domain().rank() == 0


def test_cyclic_subgroup_is_the_literal_subgroup_generated_by_a_live_isometry() -> None:
    lattice = Lattices(ZZ)("A2")
    generator = next(iter(lattice.Aut().group_generators()))
    subgroup = generator.cyclic_subgroup()

    assert subgroup.supergroup() is lattice.Aut()
    assert subgroup.generator() == generator
    assert subgroup.inclusion()(generator) == generator
    assert subgroup.is_abelian()
    assert subgroup.is_finite() is True
    assert subgroup.order() >= ZZ(2)
    assert lattice.Aut().order() % subgroup.order() == 0
    assert Set(subgroup).cardinality() == subgroup.order()
    assert subgroup.one() in subgroup
    assert generator in subgroup
    assert all(element.parent() is lattice.Aut() for element in elements)


def test_cyclic_subgroup_does_not_assume_an_indefinite_isometry_has_finite_order() -> None:
    lattice = Lattices(ZZ)([[1, 0], [0, -2]])
    e, f = lattice.module_generators()
    isometry = lattice.Aut()((3 * e + 2 * f, 4 * e + 3 * f))
    subgroup = isometry.cyclic_subgroup()

    assert isometry.determinant() == 1
    assert subgroup.supergroup() is lattice.Aut()
    assert subgroup == subgroup.parent().subgroup_generated_by(Set((isometry,)))
    assert subgroup.is_finite() is Unknown
    assert subgroup.order() is Unknown
    with pytest.raises(NotImplementedError, match="enumerating a cyclic subgroup"):
        tuple(subgroup)


def test_indefinite_polyhedral_wrapper_crossings_are_live_tensor_morphisms(monkeypatch) -> None:
    from py_polyhedral import binaries as polyhedral

    lattice = Lattices(ZZ)([[1, 0], [0, -2]])
    e, f = lattice.module_generators()

    # py_polyhedral/polyhedral_common uses right action on coordinate rows.
    # This is the transpose of the live column-action matrix sending
    # e -> 3e+2f and f -> 4e+3f.
    hyperbolic_generator = [[3, 2], [4, 3]]
    reflection_fixing_e = [[1, 0], [0, -1]]

    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_automorphism_group",
        lambda _gram: [hyperbolic_generator],
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_test_equivalence_vector",
        lambda _gram, _left, _right: hyperbolic_generator,
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_stabilizer_vector",
        lambda _gram, _vector: [reflection_fixing_e],
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_get_orbit_representative",
        lambda _gram, _square: [[1, 0]],
    )

    group = lattice.O()
    generator = group.group_generators().unrank(0)
    assert generator(e) == 3 * e + 2 * f
    assert generator(f) == 4 * e + 3 * f

    witness = group.vector_equivalence_witness(e, 3 * e + 2 * f)
    assert witness(e) == 3 * e + 2 * f

    stabilizer = group.vector_stabilizer_generators(e)
    assert stabilizer.cardinality() == 1
    assert stabilizer[0](e) == e
    assert stabilizer[0](f) == -f

    representatives = group.vector_orbit_representatives(1)
    assert representatives == (e,)


def test_indefinite_complement_gluing_route_uses_full_finite_discriminant_orthogonal_group() -> None:
    lattice = Lattices(ZZ)("U") + Lattices(ZZ)([[12]])
    vector = tuple(lattice.module_generators())[-1]
    extension = lattice.vector_primitive_extension(vector)

    assert extension.complement.signature_pair() == signature_pair(1, 1)
    assert extension.index == 1
    assert extension.gluing_subgroup.cardinality() == 1

    classes = lattice.gluing_route_discriminant_classes(vector, vector)
    discriminant_group = lattice.discriminant_group().O()
    assert classes.cardinality() == discriminant_group.order()
    assert all(automorphism.parent() is discriminant_group for automorphism in classes)
    assert set(classes) == set(discriminant_group)


def test_stable_complement_root_reflections_use_indefinite_root_orbit_representatives(monkeypatch) -> None:
    from py_polyhedral import binaries as polyhedral

    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("A1")
    vector = tuple(lattice.module_generators())[-1]

    def representatives(_gram, square):
        if square == 2:
            return [[1, 1]]
        if square == -2:
            return [[1, -1]]
        return []

    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_get_orbit_representative",
        representatives,
    )

    reflections = lattice.stable_complement_root_reflections(vector)
    assert reflections.cardinality() == 2
    assert all(reflection(vector) == vector for reflection in reflections)
    discriminant_group = lattice.discriminant_group().O()
    assert all(
        reflection.discriminant_morphism() == discriminant_group.one()
        for reflection in reflections
    )


def test_isotropic_line_plane_flag_orbits_equivalence_and_stabilizers_are_live_subobjects(monkeypatch) -> None:
    from py_polyhedral import binaries as polyhedral

    lattice = Lattices(ZZ)("U") + Lattices(ZZ)("U")
    identity = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    line_block = [[1, 0, 0, 0]]
    plane_block = [[1, 0, 0, 0], [0, 0, 1, 0]]

    def orbit_blocks(_gram, rank, nature):
        if rank == 1:
            return [line_block]
        if rank == 2 and nature in {"plane", "flag"}:
            return [plane_block]
        return []

    monkeypatch.setattr(polyhedral, "indefinite_form_isotropic_k_stuff", orbit_blocks)
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_test_equivalence_isotropic_k_plane",
        lambda _gram, _left, _right, choice="plane": identity,
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_stabilizer_isotropic_subspace",
        lambda _gram, _basis, choice="plane": [identity],
    )

    line = lattice.isotropic_line_orbit_representatives()[0]
    plane = lattice.isotropic_plane_orbit_representatives()[0]
    flag = lattice.isotropic_flag_orbit_representatives()[0]

    assert line.rank() == 1 and line.is_primitive()
    assert plane.rank() == 2 and plane.is_primitive()
    assert flag.rank() == 2
    assert tuple(term.rank() for term in flag.terms()) == (1, 2)

    line_witness = lattice.O().isotropic_equivalence_witness(line, line)
    plane_witness = lattice.O().isotropic_equivalence_witness(plane, plane)
    flag_witness = lattice.O().isotropic_equivalence_witness(flag, flag, flag=True)
    assert all(witness.parent() is lattice.O() for witness in (line_witness, plane_witness, flag_witness))

    line_stabilizer = lattice.O().isotropic_stabilizer_generators(line)
    plane_stabilizer = lattice.O().isotropic_stabilizer_generators(plane)
    flag_stabilizer = lattice.O().isotropic_stabilizer_generators(flag, flag=True)
    assert line_stabilizer.cardinality() == plane_stabilizer.cardinality() == flag_stabilizer.cardinality() == 1


def test_finite_character_quotient_splits_vector_orbits_under_special_orthogonal_group() -> None:
    lattice = Lattices(ZZ)("A1")
    root = lattice.module_generators().unrank(0)
    special = lattice.SO()

    representatives = special.vector_orbit_representatives(-2)
    assert representatives.cardinality() == 2
    assert Set(representatives) == Set((root, -root))
    assert special.vectors_are_equivalent(root, root)
    assert not special.vectors_are_equivalent(root, -root)


def test_finite_character_quotient_splits_isotropic_line_orbit_under_so_u(monkeypatch) -> None:
    from py_polyhedral import binaries as polyhedral

    lattice = Lattices(ZZ)("U")
    swap = [[0, 1], [1, 0]]
    minus_identity = [[-1, 0], [0, -1]]

    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_automorphism_group",
        lambda _gram: [swap, minus_identity],
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_isotropic_k_stuff",
        lambda _gram, rank, nature: [[[1, 0]]] if rank == 1 and nature == "plane" else [],
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_stabilizer_isotropic_subspace",
        lambda _gram, _basis, choice="plane": [minus_identity],
    )
    monkeypatch.setattr(
        polyhedral,
        "indefinite_form_test_equivalence_isotropic_k_plane",
        lambda _gram, _left, _right, choice="plane": swap,
    )

    special = lattice.SO()
    representatives = special.isotropic_orbit_representatives(1)
    assert representatives.cardinality() == 2
    lines = {
        tuple(abs(entry) for entry in representative.inclusion()(representative.module_generators()[0]).to_tuple())
        for representative in representatives
    }
    assert lines == {(ZZ(1), ZZ(0)), (ZZ(0), ZZ(1))}
    assert not special.isotropic_are_equivalent(
        representatives[0], representatives[1]
    )


def test_positive_cone_character_and_real_spinor_norm_are_independent_computations() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    positive_reflection = lattice.reflection(e + f)
    negative_reflection = lattice.reflection(e - f)

    assert positive_reflection.determinant() == -1
    assert negative_reflection.determinant() == -1
    assert positive_reflection.preserves_positive_cone() is False
    assert negative_reflection.preserves_positive_cone() is True
    assert positive_reflection.real_spinor_norm_sign() == -1
    assert negative_reflection.real_spinor_norm_sign() == 1

    cone_group = lattice.positive_cone_subgroup()
    spinor_kernel = lattice.spinor_kernel_subgroup()
    assert negative_reflection in cone_group
    assert positive_reflection not in cone_group
    assert negative_reflection in spinor_kernel
    assert positive_reflection not in spinor_kernel


def test_centralizer_discriminant_image_matches_finite_a2_centralizer(monkeypatch) -> None:
    from dzack_research.preamble.categories import lattice_engines

    monkeypatch.setattr(
        lattice_engines,
        "oscar_centralizer_discriminant_image",
        lambda _gram, _isometry: ((tensor.matrix(ZZ, [[2]]),), ZZ(2), ZZ(1), ZZ(1)),
    )
    lattice = Lattices(ZZ)("A2")
    e, _f = lattice.module_generators()
    isometry = lattice.reflection(e)
    image = isometry.centralizer_discriminant_image()

    finite_centralizer_images = tuple(
        automorphism.discriminant_morphism()
        for automorphism in lattice.Aut()
        if automorphism * isometry == isometry * automorphism
    )
    expected = lattice.discriminant_group().O().subgroup_on(
        tuple(
            lattice.discriminant_group().O()(automorphism)
            for automorphism in finite_centralizer_images
        )
    )
    assert image.order() == expected.order()
    assert all(generator in expected for generator in image.group_generators())
    assert all(generator in image for generator in expected.group_generators())


def test_definite_vector_orbit_equivalence_stabilizer_and_representatives() -> None:
    lattice = Lattices(ZZ)("A2")
    roots = lattice.roots()
    left, right = roots[0], roots[1]
    orthogonal_group = lattice.O()

    witness = orthogonal_group.vector_equivalence_witness(left, right)
    assert witness is not None
    assert witness(left) == right
    assert orthogonal_group.vectors_are_equivalent(left, right)

    stabilizer_generators = orthogonal_group.vector_stabilizer_generators(left)
    assert all(generator(left) == left for generator in stabilizer_generators)
    assert orthogonal_group.subgroup(stabilizer_generators).cardinality() == 2

    representatives = orthogonal_group.vector_orbit_representatives(-2)
    assert representatives.cardinality() == 1
    assert representatives[0].q() == -2
    assert all(
        orthogonal_group.vectors_are_equivalent(root, representatives[0])
        for root in roots
    )


def test_vector_primitive_extension_recovers_index_two_glue_in_u() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    extension = lattice.vector_primitive_extension(e + f)

    assert extension.vector.q() == 2
    assert extension.line.rank() == extension.complement.rank() == 1
    assert extension.sum_lattice.rank() == lattice.rank() == 2
    assert extension.index == 2
    assert extension.inclusion.index() == 2
    assert extension.gluing_subgroup.cardinality() == 2
    assert extension.gluing_subgroup.is_isotropic()
    assert extension.line_discriminant_inclusion.is_injective()
    assert extension.complement_discriminant_inclusion.is_injective()


def test_vector_primitive_extension_tracks_nontrivial_ambient_discriminant() -> None:
    lattice = Lattices(ZZ)([[0, 2], [2, 0]])
    e, f = lattice.module_generators()
    extension = lattice.vector_primitive_extension(e + f)

    assert extension.index == 2
    assert extension.discriminant_form.cardinality() == 4
    assert extension.discriminant_representatives.cardinality() == lattice.rank()
    for representative in extension.discriminant_representatives:
        for glued in extension.gluing_images:
            assert representative.b(glued) == extension.sum_form.bilinear_value_module().zero()
    for generator in extension.discriminant_form.module_generators():
        representative = extension.representative_of(generator)
        assert all(
            representative.b(glued) == extension.sum_form.bilinear_value_module().zero()
            for glued in extension.gluing_images
        )


def test_definite_complement_extensions_exhaust_the_u_vector_cosets() -> None:
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    vector = e + f

    stabilizer = lattice.definite_complement_extensions(vector, vector)
    opposite_coset = lattice.definite_complement_extensions(vector, -vector)

    assert stabilizer.cardinality() == 2
    assert opposite_coset.cardinality() == 2
    assert all(isometry(vector) == vector for isometry in stabilizer)
    assert all(isometry(vector) == -vector for isometry in opposite_coset)
    assert Set(stabilizer).cardinality() == stabilizer.cardinality()
