
from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FiniteGroups,
    Lattices,
    MatrixSpaces,
    Set,
    signature_pair,
)


def _module_matrix(morphism):
    linear = morphism.domain().module_category().Mor(
        morphism.domain(), morphism.codomain()
    )(morphism)
    assert linear.parent() in MatrixSpaces(linear.parent().base_ring())
    return linear








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
    change = ZZ.matrix_space(2, 2).from_rows([[1, 1], [0, 1]])
    reframed_gram = lattice.gram_tensor().pullback(change)
    reframed = Lattices(ZZ)(reframed_gram)

    mor = reframed.Isom(lattice)
    assert mor.is_empty() is False
    witness = mor.an_element()
    assert _module_matrix(witness).parent() in MatrixSpaces(ZZ)
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
    _values = lattice.successive_minima()
    assert _values.cardinality() == 2
    assert _values[0] == 1
    assert _values[1] == 1
    assert lattice.hadamard_ratio() == 1
    assert lattice.covering_radius() ** 2 == QQ(1) / 2
    assert lattice.center_density() == QQ(1) / 4
    assert lattice.contact_polytope().n_vertices() == 4
    assert lattice.voronoi_relevant_vectors().cardinality() == 4




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
        assert _module_matrix(automorphism).parent() in MatrixSpaces(ZZ)
        for left in lattice.module_generators():
            for right in lattice.module_generators():
                assert lattice.b(left, right) == lattice.b(
                    automorphism(left), automorphism(right)
                )






def test_indefinite_isometry_ladder_uses_parity_as_an_exact_obstruction() -> None:
    even = Lattices(ZZ)("U")
    odd = Lattices(ZZ)([[1, 0], [0, -1]])

    assert even.signature_pair() == odd.signature_pair() == signature_pair(1, 1)
    assert even.Isom(odd).is_empty() is True
    assert even.is_isometric(odd) is False








def test_definite_target_embedding_mor_enumerates_all_a1_into_a2_roots() -> None:
    source = Lattices(ZZ)("A1")
    target = Lattices(ZZ)("A2")
    mor = source.Emb(target)
    embeddings = mor

    assert mor.cardinality() == 6
    source_generator = source.module_generators()[0]
    images = Set(embedding(source_generator) for embedding in embeddings)
    assert images == Set(target.roots())
    assert mor.is_empty() is False
    assert mor.an_element()(source_generator) in images




def test_even_overlattice_inclusions_enumerate_isotropic_glue_for_u2() -> None:
    lattice = Lattices(ZZ)([[0, 2], [2, 0]])
    inclusions = lattice.even_overlattice_inclusions()

    assert inclusions.cardinality() == 3
    assert inclusions.condition_set(lambda inclusion: inclusion.index() == ZZ(1)).cardinality() == 1
    assert inclusions.condition_set(lambda inclusion: inclusion.index() == ZZ(2)).cardinality() == 2
    assert all(inclusion.codomain().is_even() for inclusion in inclusions)
    assert sum(inclusion.codomain().is_unimodular() for inclusion in inclusions) == 2


def test_nikulin_even_unimodular_embedding_existence_controls_embedding_mor() -> None:
    target = Lattices(ZZ)("U")
    a1 = Lattices(ZZ)("A1")
    a2 = Lattices(ZZ)("A2")
    odd = Lattices(ZZ)([[-1]])

    assert a1.embeds_in_even_unimodular(1, 1)
    assert not a2.embeds_in_even_unimodular(1, 1)
    assert a1.Emb(target).is_empty() is False
    assert a2.Emb(target).is_empty() is True
    assert odd.Emb(target).is_empty() is True




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
    determinant_one = automorphisms.condition_set(lambda automorphism: automorphism.determinant() == 1)
    assert determinant_one.cardinality() == 6
    assert all(automorphism in special for automorphism in determinant_one)
    assert all(
        (automorphism in special) == (automorphism.determinant() == 1)
        for automorphism in automorphisms
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


def test_the_component_character_is_multiplicative_and_cuts_out_the_cone_subgroup() -> None:
    r"""\(\chi_\Omega\) separates the two reflections of \(U\) and is a morphism.

    \(e+f\) and \(e-f\) are orthogonal, so \(s_{e+f}s_{e-f}=-\mathrm{id}\),
    which exchanges the two components of the positive cone.  A character
    that merely recorded the determinant would send that product to the
    identity and fail here.
    """
    lattice = Lattices(ZZ)("U")
    e, f = lattice.module_generators()
    exchanging = lattice.reflection(e + f)
    preserving = lattice.reflection(e - f)
    negation = lattice.O()(lambda label: -lattice.module_generator(label))
    character = lattice.component_character()
    trivial = character.codomain().one()

    assert exchanging * preserving == negation
    assert character(preserving) == trivial
    assert character(exchanging) != trivial
    assert character(negation) == character(exchanging) * character(preserving)
    assert character(negation) != trivial

    cone_group = lattice.positive_cone_subgroup()
    assert preserving in cone_group
    assert exchanging not in cone_group
    assert negation not in cone_group




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
    assert extension.line.module_rank() == extension.complement.module_rank() == 1
    assert extension.sum_lattice.module_rank() == lattice.module_rank() == 2
    assert extension.index == 2
    assert extension.inclusion.index() == 2
    assert extension.gluing_subgroup.cardinality() == 2
    assert extension.gluing_subgroup.is_isotropic()
    assert extension.line_discriminant_inclusion.is_injective()
    assert extension.complement_discriminant_inclusion.is_injective()




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
