from __future__ import annotations

import pytest

from sage.all import CartanMatrix, Matrix, QQ, ZZ, identity_matrix, matrix

import sage_lattice_category_spike.lattice_categories as lc


def assert_matrix_equal(left, right):
    assert matrix(QQ, left) == matrix(QQ, right)


def test_cartan_and_hyperbolic_constructors_match_integral_lattice_doctests():
    # Reference: free_quadratic_module_integer_symmetric.py IntegralLattice constructor doctests.
    assert lc.Lattice("U").signature_pair() == (1, 1)
    assert_matrix_equal(lc.Lattice("H").gram_matrix(), matrix(QQ, 2, 2, [0, 1, 1, 0]))
    assert_matrix_equal(lc.Lattice("A2").gram_matrix(), CartanMatrix(["A", 2]))
    assert_matrix_equal(lc.Lattice(["A", 2]).gram_matrix(), CartanMatrix(["A", 2]))
    assert_matrix_equal(lc.Lattice("D4").gram_matrix(), CartanMatrix(["D", 4]))


def test_rational_span_and_fractional_dual_follow_free_quadratic_module_doctests():
    # References: dual_lattice doctest and free_quadratic_module span/span_of_basis doctests.
    L = lc.Lattice("A2")
    L_dual = L.dual_lattice()

    assert not hasattr(L, "ambient_module")
    assert not hasattr(L, "ambient_space")
    assert not hasattr(L, "ambient_quadratic_space")
    assert not hasattr(L, "ambient_vector_space")
    assert L.rational_span().base_ring() is QQ
    assert L.rationalization_module().dimension() == 2
    assert L.is_submodule(L_dual)
    assert_matrix_equal(L_dual.basis_matrix(), matrix(QQ, 2, 2, [QQ(1) / 3, QQ(2) / 3, 0, 1]))
    assert L_dual.dual_lattice() == L

    W = L.span_of_basis([[QQ(1) / 5, QQ(2) / 5], [QQ(1) / 7, QQ(1) / 7]], base_ring=ZZ)
    assert_matrix_equal(W.basis_matrix(), matrix(QQ, 2, 2, [QQ(1) / 5, QQ(2) / 5, QQ(1) / 7, QQ(1) / 7]))


def test_nonintegral_sublattice_is_owned_fractional_lattice_not_rejected_by_default():
    # Reference: IntegralLattice.sublattice rejects this, but the consolidated spec broadens it.
    U = lc.Lattice("U")
    fractional = U.sublattice([[QQ(1) / 2, -QQ(1) / 2]], label="fractional_line")

    assert fractional.base_ring() is ZZ
    assert not fractional.is_integral()
    assert_matrix_equal(fractional.gram_matrix(), matrix(QQ, 1, 1, [-QQ(1) / 2]))
    with pytest.raises(ValueError):
        U.sublattice([[QQ(1) / 2, -QQ(1) / 2]], check_integral=True)


def test_overlattice_and_maximal_overlattice_follow_integral_lattice_doctests():
    # References: IntegralLattice.overlattice and maximal_overlattice doctests.
    L = lc.Lattice(Matrix(ZZ, 2, 2, [2, 0, 0, 2]))
    M = L.overlattice([[QQ(1) / 2, QQ(1) / 2]])
    assert_matrix_equal(M.gram_matrix(), matrix(QQ, 2, 2, [1, 1, 1, 2]))

    N = lc.Lattice(matrix.diagonal([2, 4, 4, 8]))
    assert N.maximal_overlattice().is_even()


def test_discriminant_group_cover_relations_and_primary_forms_match_doctests():
    # Reference: IntegralLattice.discriminant_group doctest.
    L = lc.Lattice(Matrix(ZZ, 2, 2, [4, 2, 2, -4]))
    A = L.discriminant_group()

    assert A.invariants() == (2, 10)
    assert_matrix_equal(A.gram_matrix_quadratic(), matrix(QQ, 2, 2, [1, QQ(1) / 2, QQ(1) / 2, QQ(1) / 5]))
    assert A.dual_cover() == L.dual_lattice()
    assert A.relation_lattice() == L
    assert A.cover() == A.V()
    assert A.relations() == A.W()
    assert A.primary_part(2).invariants() == (2, 2)
    assert_matrix_equal(A.primary_part(2).gram_matrix_quadratic(), matrix(QQ, 2, 2, [1, QQ(1) / 2, QQ(1) / 2, 1]))
    assert A.primary_part(5).invariants() == (5,)
    assert_matrix_equal(A.primary_part(5).gram_matrix_quadratic(), matrix(QQ, 1, 1, [QQ(4) / 5]))
    assert A.is_finite()
    assert A.list() == A.elements()
    assert A.random_element() in A.elements()


def test_gluing_accepts_sage_integral_lattice_glue_shape():
    # Reference: IntegralLatticeGluing single-lattice doctest.
    L1 = lc.Lattice(matrix(ZZ, 1, 1, [4]))
    g1 = L1.discriminant_group().gens()[0]
    M = lc.IntegralLatticeGluing([L1], [[2 * g1]])

    assert_matrix_equal(M.basis_matrix(), matrix(QQ, 1, 1, [QQ(1) / 2]))
    assert_matrix_equal(M.gram_matrix(), matrix(QQ, 1, 1, [1]))


def test_local_modification_uses_sage_gram_matrix_contract_not_discriminant_gens_only():
    # Reference: free_quadratic_module_integer_symmetric.local_modification doctest.
    L = lc.Lattice("A3").twist(15)
    M = L.maximal_overlattice()
    for p in ZZ(L.determinant()).prime_divisors():
        M = M.local_modification(L.gram_matrix(), p)
    assert M.genus() == L.genus()


def test_discriminant_normal_form_identifies_reference_isomorphic_forms():
    # Reference: torsion_quadratic_module.normal_form issue-24864 doctest.
    L1 = lc.Lattice(matrix(ZZ, 3, 3, [-4, 0, 0, 0, 4, 0, 0, 0, -2]))
    L2 = lc.Lattice(matrix(ZZ, 3, 3, [-4, 0, 0, 0, -4, 0, 0, 0, 2]))

    AL1 = L1.discriminant_group()
    AL2 = L2.discriminant_group()

    assert AL1.normal_form() == AL2.normal_form()
    assert AL1.is_isomorphic(AL2)
    assert AL1.normal_form()[0] == (2, 4, 4)
    assert_matrix_equal(
        AL1.normal_form()[1],
        matrix(QQ, 3, 3, [QQ(1) / 2, 0, 0, 0, QQ(1) / 4, 0, 0, 0, QQ(5) / 4]),
    )


def test_brown_invariant_and_genus_follow_torsion_quadratic_module_doctests():
    # References: torsion_quadratic_module brown_invariant/genus/is_genus doctests.
    D4 = lc.Lattice("D4")
    assert D4.discriminant_group().brown_invariant() == 4

    L3 = lc.Lattice(3 * Matrix(ZZ, 2, 2, [2, 1, 1, 2]))
    L = D4.direct_sum(L3)
    D = L.discriminant_group()
    assert D.is_genus((6, 0))
    assert not D.is_genus((4, 2))
    assert D.is_genus((16, 2))
    assert D.genus(L.signature_pair()) == L.genus()


def test_finite_discriminant_form_orthogonal_group_matches_torsion_doctest():
    # Reference: TorsionQuadraticForm(matrix.identity(3)/2).orthogonal_group().order() == 6.
    D = lc.TorsionQuadraticForm(identity_matrix(QQ, 3) / 2)
    OD = D.orthogonal_group()

    assert OD.order() == 6
    assert D.isometry_group(kind="quadratic").order() == 6
    assert D.order() == 8
    assert D.is_finite()
    assert D.list() == D.elements()
    assert D.random_element() in D.elements()
    assert D.exponent() == 2
    assert D.zero() == D.identity()
    assert D.invariant_factors() == (2, 2, 2)
    assert D.coordinates(D.gen(0) + D.gen(2)) == (1, 0, 1)
    swap = D.hom([D.gen(1), D.gen(0), D.gen(2)])
    assert_matrix_equal(OD(swap), matrix(ZZ, 3, 3, [0, 1, 0, 1, 0, 0, 0, 0, 1]))


def test_explicit_lattice_isometries_induce_discriminant_actions_without_full_indefinite_group():
    # Reference: torsion_quadratic_module explicit generator pattern for discriminant actions.
    L = lc.Lattice("A4")
    reflection = -identity_matrix(ZZ, 4)
    D = L.discriminant_group()
    induced = D.orthogonal_group_from_lattice_gens([reflection])

    assert induced.order() == 2
    assert D.action_of_isometry(L.isometry_group(gens=[reflection])[0])(D.gen(0)) == -D.gen(0)


def test_lattice_module_wrapper_names_preserve_owned_lattice_contract():
    # Reference: free_module/free_quadratic_module methods promoted by the consolidated category spec.
    A2 = lc.Lattice("A2")
    A2_dual = A2.dual()
    A2_QQ = A2.change_base_ring(QQ)

    assert not any(hasattr(A2, name) for name in ("ambient_module", "ambient_space", "ambient_quadratic_space"))
    assert A2_QQ == A2.rational_span()
    assert A2_QQ.base_ring() is QQ
    assert_matrix_equal(A2.basis_matrix(kind="user"), A2.basis_matrix())
    skew_basis = lc.Lattice("U").span_of_basis([[1, 1], [1, 0]], label="skew")
    expected_echelon_gram = (
        skew_basis.basis_matrix(kind="echelon")
        * skew_basis.ambient_gram_matrix()
        * skew_basis.basis_matrix(kind="echelon").transpose()
    )
    assert_matrix_equal(skew_basis.gram_matrix(basis="user"), skew_basis.gram_matrix())
    assert_matrix_equal(skew_basis.gram_matrix(basis="echelon"), expected_echelon_gram)
    assert_matrix_equal(skew_basis.inner_product_matrix(basis="echelon"), expected_echelon_gram)
    assert A2.coordinates(A2.gen(1)) == (0, 1)
    assert A2.ambient_coordinates(A2.gen(1)) == (0, 1)
    assert A2.dual_lattice() == A2_dual
    assert not A2.is_self_dual()
    assert lc.Lattice("U").is_self_dual()
    assert A2.absolute_discriminant() == 3
    assert A2.signed_discriminant() == -3
    assert not A2.is_degenerate()
    assert A2.radical().rank() == 0
    assert A2_dual.denominator() == 3
    assert A2.relative_index(A2_dual) == A2.index_in(A2_dual)

    fractional = A2.fractional_sublattice([[QQ(1) / 3, 0]])
    assert fractional.base_ring() is ZZ
    assert not fractional.is_integral()
    assert fractional.clear_denominators().is_integral()
    assert A2.submodule([[1, 0]]).rank() == 1
    assert A2.submodule_with_basis([[1, 0]]).rank() == 1
    assert A2.zero_submodule().rank() == 0
    assert A2.vector_space_span([[1, 0]]).base_ring() is QQ
    assert A2.vector_space_span_of_basis([[1, 0]]).base_ring() is QQ
    assert A2.index_in_saturation() == A2.index_in(A2.saturation())
    nonprimitive_line = lc.Lattice("U").sublattice([[2, 0]], label="2e")
    assert nonprimitive_line.saturation(in_ambient=lc.Lattice("U")).basis_matrix() == matrix(QQ, 1, 2, [1, 0])
    assert nonprimitive_line.saturation(in_ambient=lc.Lattice("U")) == nonprimitive_line.primitive_closure(lc.Lattice("U"))
    assert_matrix_equal(A2.scale(2).gram_matrix(), 4 * A2.gram_matrix())
    assert A2.integral_saturation().is_integral()
    assert A2.underlying_quadratic_module() is A2
    with pytest.raises(NotImplementedError):
        A2.underlying_quotient_module()


def test_discriminant_group_additive_abelian_group_api_matches_fgp_surface():
    # Reference: FGP quotient/module Smith-coordinate methods surfaced on discriminant groups.
    L = lc.Lattice(Matrix(ZZ, 2, 2, [4, 2, 2, -4]))
    A = L.discriminant_group()
    x = A.gen(0) + 3 * A.gen(1)

    assert A.as_additive_abelian_group() is A
    assert A.underlying_abelian_group() is A
    assert A.order() == A.cardinality() == 20
    assert A.exponent() == 10
    assert not A.is_cyclic()
    assert A.zero() == A.identity()
    assert A.generator_orders() == (2, 10)
    assert A.invariant_factors() == (2, 10)
    assert A.elementary_divisors() == (2, 2, 5)
    assert A.rank_p(2) == 2
    assert A.length_p(5) == 1
    assert sorted(part.invariants() for part in A.primary_parts()) == [(2, 2), (5,)]
    assert A.p_primary_part(5).invariants() == (5,)
    assert A.coordinates(x) == (1, 3)
    assert A.discrete_log(x) == (1, 3)
    assert A.discrete_exp((1, 3)) == x
    assert A.subgroup_generated_by([2 * A.gen(1)]).cardinality() == 5
    assert A.from_generators([2 * A.gen(1)]).cardinality() == 5
    assert A.subgroup([2 * A.gen(1)]).cardinality() == 5
    assert A.contains_subgroup(A.subgroup([2 * A.gen(1)]))
    assert A.torsion_subgroup() is A


def test_discriminant_action_inverse_image_matches_fgp_morphism_doctest():
    # Reference: FGP morphism doctests expose kernel, image, lift, and inverse_image.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 4]))
    g = D.gen(0)
    doubling = D.hom([2 * g])
    image = D.subgroup([2 * g])

    assert doubling.kernel().cardinality() == 2
    assert doubling.image() == image
    assert doubling.im_gens() == image.gens()
    assert doubling.lift(2 * g) == g
    with pytest.raises(ValueError):
        doubling.lift(g)
    assert doubling.inverse_image(D.subgroup([])).cardinality() == 2
    assert doubling.inverse_image(image).cardinality() == 4


def test_discriminant_form_subgroup_source_and_action_api_is_bound():
    # Reference: torsion quadratic module subgroup/form API plus lattice source metadata.
    L = lc.Lattice(matrix(ZZ, 1, 1, [4]))
    D = L.discriminant_group()
    g = D.gen(0)
    H = D.subgroup([2 * g])
    Z = D.subgroup([])

    assert D.cover_lattice() == L.dual_lattice()
    assert D.dual_lattice() == L.dual_lattice()
    assert D.relation_lattice() == L
    assert D.lift_to_dual(g) == D.lift(g)
    assert D.project_from_dual(D.lift_to_dual(g)) == g
    assert D.coset_representative(g) == D.lift(g)
    assert D.is_isotropic_element(D.zero())
    assert not D.is_isotropic_element(2 * g)
    assert D.is_isotropic_subgroup(Z)
    assert not D.is_isotropic_subgroup(H)
    assert D.is_anisotropic()
    assert D.orthogonal(H).cardinality() == 2
    assert D.orthogonal_complement(H) == D.orthogonal(H)
    assert D.orthogonal_quotient(Z).invariants() == D.invariants()

    M = D.preimage_lattice(H, label="<1>")
    assert_matrix_equal(M.gram_matrix(), matrix(QQ, 1, 1, [1]))
    assert D.discriminant_form_of_overlattice(H).invariants() == ()

    negation = L.isometry_group(gens=[matrix(ZZ, 1, 1, [-1])])[0]
    action = D.action_of_lattice_isometry(negation)
    assert action(g) == -g
    image = D.image_of_lattice_group([negation])
    assert image.order() == 2
    assert D.orbit(g, group=image) == frozenset({g, -g})


def test_lattice_exact_sequence_wrappers_use_owned_finite_quotients():
    # Reference: FGP quotient cover/relation/lift/projection contract promoted to lattices.
    A2 = lc.Lattice("A2")
    A2_dual = A2.dual_lattice()
    quotient = A2_dual.quotient_by_sublattice(A2)

    assert quotient.cover_lattice() == A2_dual
    assert quotient.relation_lattice() == A2
    assert quotient.cover() == quotient.V()
    assert quotient.relations() == quotient.W()
    assert quotient.invariants() == A2.discriminant_group().invariants()
    assert quotient.cardinality() == A2.discriminant_group().cardinality()
    assert quotient.projection(quotient.lift(quotient.gen(0))) == quotient.gen(0)
    assert quotient.quotient_map()(quotient.lift(quotient.gen(0))) == quotient.gen(0)
    assert A2_dual.finite_quotient(A2).invariants() == (3,)
    assert A2_dual.quotient_map_to(A2)(quotient.lift(quotient.gen(0))) == quotient.gen(0)
    assert quotient.is_finite()
    assert quotient.list() == quotient.elements()
    assert quotient.random_element() in quotient.elements()
    assert quotient.smith_form_gens() == quotient.gens()
    assert quotient.smith_form_gen(0) == quotient.gen(0)
    assert quotient.smith_generators() == quotient.gens()
    assert quotient.linear_combination_of_smith_form_gens([1]) == quotient.gen(0)
    assert quotient.gens_to_smith() == identity_matrix(ZZ, 1)
    assert quotient.smith_to_gens() == identity_matrix(ZZ, 1)
    assert tuple(quotient.gens_vector(quotient.gen(0))) == (1,)
    assert tuple(quotient.coordinate_vector(quotient.gen(0))) == (1,)
    assert quotient.coordinates_in_smith_basis(quotient.gen(0)) == (1,)
    assert quotient.coordinates_in_generators(quotient.gen(0)) == (1,)
    assert quotient.generator_relations() == matrix(ZZ, 1, 1, [3])
    assert quotient.invariant_factors() == (3,)
    assert quotient.elementary_divisors() == (3,)

    cover_mod_four = lc.Lattice(matrix(QQ, 1, 1, [QQ(1) / 4]))
    quotient_mod_four = cover_mod_four.finite_quotient(cover_mod_four.sublattice([[4]], label="4L"))
    doubling = quotient_mod_four.hom([2 * quotient_mod_four.gen(0)])
    assert doubling.kernel().cardinality() == 2
    assert doubling.image().cardinality() == 2
    assert doubling.im_gens() == doubling.image().gens()
    assert doubling.lift(2 * quotient_mod_four.gen(0)) in quotient_mod_four.elements()
    with pytest.raises(ValueError):
        doubling.lift(quotient_mod_four.gen(0))


def test_lattice_morphism_lift_and_image_generators_are_bound():
    A2 = lc.Lattice("A2")
    identity = A2.Hom(A2).from_matrix(identity_matrix(ZZ, 2))

    assert identity.lift(A2.gen(1)) == A2.gen(1)
    assert identity.im_gens() == A2.gens()
    assert A2.discriminant_group().smith_generators() == A2.discriminant_group().gens()


def test_lattice_similarity_is_scalar_form_preserving_not_an_isometry():
    # Reference: similarity maps preserve the bilinear form up to an explicit scalar.
    A2 = lc.Lattice("A2")
    twist = A2.twist(2)

    similarity = A2.similarity(identity_matrix(ZZ, 2), codomain=twist, scalar=2)
    assert similarity.scalar() == 2
    assert similarity(A2.gen(0)).q() == 2 * A2.gen(0).q()
    with pytest.raises(ValueError):
        A2.similarity(identity_matrix(ZZ, 2), codomain=twist, scalar=3)


def test_discriminant_quotient_is_not_orthogonal_quotient_alias():
    # Reference: FGP quotient API is ordinary finite-group quotient; orthogonal quotient is separate.
    L = lc.Lattice(Matrix(ZZ, 2, 2, [4, 2, 2, -4]))
    A = L.discriminant_group()
    H = A.subgroup([2 * A.gen(1)])
    quotient = A.quotient(H)

    assert H.cardinality() == 5
    assert quotient.relations() == H
    assert quotient.cardinality() == 4
    assert quotient.invariants() == (2, 2)
    assert quotient.projection(quotient.lift(quotient.gen(0))) == quotient.gen(0)
    assert A.orthogonal_quotient(A.subgroup([])).invariants() == A.invariants()


def test_discriminant_normal_form_can_return_change_of_generators():
    # Reference: torsion quadratic module normal_form has an isometry/change-of-generators option.
    L = lc.Lattice(matrix(ZZ, 3, 3, [-4, 0, 0, 0, 4, 0, 0, 0, -2]))
    A = L.discriminant_group()

    normal_form, change = A.normal_form(return_isometry=True)
    assert normal_form == A.normal_form()
    assert change.is_automorphism()


def test_discriminant_group_isomorphism_kind_distinguishes_group_bilinear_and_quadratic():
    # Reference: discriminant groups need group, bilinear, and quadratic isomorphism modes.
    positive = lc.Lattice(matrix(ZZ, 1, 1, [2])).discriminant_group()
    negative = lc.Lattice(matrix(ZZ, 1, 1, [-2])).discriminant_group()

    assert positive.is_isomorphic_to(negative, kind="group")
    assert positive.is_isomorphic_to(negative, kind="bilinear")
    assert not positive.is_isomorphic_to(negative, kind="quadratic")
    assert positive.isometry_to(positive, kind="quadratic").is_identity()


def test_underlying_abelian_automorphism_group_is_not_the_form_orthogonal_group():
    # Reference: discriminant groups need Aut(A) separately from O(q_A).
    D = lc.TorsionQuadraticForm(identity_matrix(QQ, 3) / 2)

    assert D.quadratic_orthogonal_group().order() == 6
    assert D.automorphism_group().order() == 168


def test_finite_quadratic_form_has_additive_group_generation_aliases():
    # Reference: additive abelian wrapper exposes from_generators and torsion subgroup helpers.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 5]))

    assert D.from_generators([D.gen(0)]).cardinality() == D.cardinality()
    assert D.from_generators([2 * D.gen(0)]).cardinality() == D.cardinality()
    assert D.torsion_subgroup() is D


def test_finite_quadratic_form_drops_trivial_presentation_factors():
    # Reference: finite form presentations should omit order-one generator factors.
    D = lc.TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(1) / 2, 0]))
    expected = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 2]))

    assert D.invariants() == (2,)
    assert D.gram_matrix_bilinear() == expected.gram_matrix_bilinear()
    assert D.gram_matrix_quadratic() == expected.gram_matrix_quadratic()
    assert D.is_nondegenerate()
    assert D.radical().cardinality() == 1
    assert D.character_group() is D
    assert D.pontryagin_dual() is D
    assert D.pairing_character(D.gen(0))(D.gen(0)) == QQ(1) / 2
    assert D.pairing_isomorphism_to_dual()[D.gen(0)](D.gen(0)) == QQ(1) / 2


def test_finite_quadratic_form_promotes_torsion_quadratic_module_operations():
    # Reference: TorsionQuadraticModule finite form methods without source-lattice metadata.
    D = lc.TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(1) / 2, QQ(1) / 3]))
    H = D.subgroup([D.gen(0)])

    assert D.value_module() == (QQ, ZZ)
    assert D.value_module_qf() == (QQ, 2 * ZZ)
    assert D.primary_part(2).invariants() == (2,)
    assert D.p_primary_part(3).invariants() == (3,)
    assert sorted(part.invariants() for part in D.primary_parts()) == [(2,), (3,)]
    assert D.all_subgroups() == D.all_submodules()
    assert D.contains_subgroup(H)
    assert D.quotient_group(H).invariants() == (3,)
    assert len(D.cosets(H)) == 3
    assert D.orthogonal_complement(H).cardinality() == 3
    assert D.restricted_form(H) == matrix(QQ, 1, 1, [QQ(1) / 2])
    assert D.normal_form() == D.normal_form(partial=True)
    assert D.is_isomorphic_to(lc.TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(1) / 3, QQ(1) / 2])))
    assert D.twist(2).gram_matrix_bilinear() == matrix(QQ, 1, 1, [QQ(2) / 3])


def test_finite_quadratic_form_normal_form_uses_generator_changes_not_only_permutations():
    # Reference: torsion quadratic module normal forms classify forms up to generator changes.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 5]))
    D_changed_generator = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(9) / 5]))

    assert D.is_isomorphic_to(D_changed_generator)
    assert D.normal_form() == D_changed_generator.normal_form()
    normal_form, change = D_changed_generator.normal_form(return_isometry=True)
    assert normal_form == D.normal_form()
    assert change.is_automorphism()


def test_finite_quadratic_form_bilinear_isomorphism_uses_generator_changes():
    # Reference: bilinear and quadratic isomorphism modes are distinct finite-form contracts.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 5]))
    bilinear_change = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(4) / 5]))

    assert D.is_isomorphic_to(bilinear_change, kind="group")
    assert D.is_isomorphic_to(bilinear_change, kind="bilinear")
    assert not D.is_isomorphic_to(bilinear_change, kind="quadratic")


def test_discriminant_group_bilinear_orthogonal_group_can_be_larger_than_quadratic():
    # Reference: finite bilinear forms and finite quadratic forms are separate categories.
    D = lc.Lattice(matrix(ZZ, 1, 1, [8])).discriminant_group()

    assert D.quadratic_orthogonal_group().order() == 2
    assert D.bilinear_orthogonal_group().order() == 4


def test_orthogonal_quotient_keeps_smith_invariants_not_only_cardinality():
    # Reference: gluing uses the finite quadratic module H^perp/H, with Smith data.
    L = lc.Lattice(matrix.diagonal(ZZ, [2, 2, 2, 2]))
    A = L.discriminant_group()
    H = A.subgroup([A.discrete_exp((1, 1, 1, 1))])
    quotient = A.orthogonal_quotient(H)

    assert H.is_quadratic_isotropic()
    assert quotient.cardinality() == 4
    assert quotient.invariants() == (2, 2)


def test_discriminant_group_enumerates_all_finite_subgroups():
    # Reference: subgroup/all_subgroups should surface the finite abelian group API.
    A = lc.Lattice(matrix.diagonal(ZZ, [2, 2, 2])).discriminant_group()

    subgroup_orders = sorted(subgroup.cardinality() for subgroup in A.all_subgroups())

    assert subgroup_orders == [1] + [2] * 7 + [4] * 7 + [8]
    assert A.subgroups() == A.all_subgroups()


def test_pushforward_and_pullback_forms_compute_transported_pairings():
    # Reference: quotient/form API distinguishes induced forms from raw group quotients.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 5]))
    scaling = D.hom([2 * D.gen(0)])

    assert scaling.is_automorphism()
    assert not scaling.preserves_form()
    assert_matrix_equal(D.pullback_form(scaling), matrix(QQ, 1, 1, [QQ(4) / 5]))
    assert_matrix_equal(D.pushforward_form(scaling), matrix(QQ, 1, 1, [QQ(9) / 5]))
