from __future__ import annotations

import pytest

from sage.all import CartanMatrix, Matrix, QQ, ZZ, identity_matrix, matrix

import sage_lattice_category_spike.lattice_categories as lc
from sage.groups.additive_abelian.qmodnz import QmodnZ


def assert_matrix_equal(left, right):
    assert matrix(QQ, left) == matrix(QQ, right)


def as_finite_quadratic_form(form):
    # Present any finite quadratic form (discriminant group or subquotient) as the
    # canonical quadratic-discriminant-form TYPE via its quadratic Gram (q on the
    # diagonal, b off it), so two forms can be compared as forms, not by group invariants.
    generators = form.gens()
    gram = matrix(
        QQ, len(generators), len(generators),
        [form.q(generators[i]) if i == j else form.b(generators[i], generators[j])
         for i in range(len(generators)) for j in range(len(generators))],
    )
    return lc.TorsionQuadraticForm(gram)


def test_cartan_and_hyperbolic_constructors_match_integral_lattice_doctests():
    # Reference: free_quadratic_module_integer_symmetric.py IntegralLattice constructor doctests.
    assert lc.Lattice("U").signature_pair() == (1, 1)
    assert_matrix_equal(lc.Lattice("H").gram_matrix(), matrix(QQ, 2, 2, [0, 1, 1, 0]))
    assert_matrix_equal(lc.Lattice("A2").gram_matrix(), CartanMatrix(["A", 2]))
    assert_matrix_equal(lc.Lattice(["A", 2]).gram_matrix(), CartanMatrix(["A", 2]))
    assert_matrix_equal(lc.Lattice("D4").gram_matrix(), CartanMatrix(["D", 4]))


def test_rationalization_and_fractional_dual_follow_free_quadratic_module_doctests():
    # References: dual doctest and free_quadratic_module span/span_of_basis doctests.
    L = lc.Lattice("A2")
    L_dual = L.dual()

    assert not hasattr(L, "ambient_module")
    assert not hasattr(L, "ambient_space")
    assert not hasattr(L, "ambient_vector_space")
    assert not hasattr(L, "rationalization_module")
    assert L.rationalization().base_ring() is QQ
    assert L.rationalization().rank() == 2
    # The based dual is (ZZ, G^{-1}); L embeds in L# via the metric inclusion (matrix G).
    assert L.dual_inclusion().image().is_submodule(L_dual)
    assert L_dual.dual() == L


def test_nonintegral_rational_generators_use_fractional_sublattice_contract():
    # Reference: IntegralLattice.sublattice rejects this; the consolidated category broadens it through fractional_sublattice.
    U = lc.Lattice("U")
    fractional = U.fractional_sublattice([[QQ(1) / 2, -QQ(1) / 2]], label="fractional_line")

    assert fractional.base_ring() is ZZ
    assert not fractional.is_integral()
    assert_matrix_equal(fractional.gram_matrix(), matrix(QQ, 1, 1, [-QQ(1) / 2]))
    with pytest.raises(AssertionError):
        U.sublattice([[QQ(1) / 2, -QQ(1) / 2]])


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
    assert A.cover() == L.dual()
    assert A.relation_lattice() == L
    assert A.primary_part(2).invariants() == (2, 2)
    assert_matrix_equal(A.primary_part(2).gram_matrix_quadratic(), matrix(QQ, 2, 2, [1, QQ(1) / 2, QQ(1) / 2, 1]))
    assert A.primary_part(5).invariants() == (5,)
    assert_matrix_equal(A.primary_part(5).gram_matrix_quadratic(), matrix(QQ, 1, 1, [QQ(4) / 5]))
    assert A.is_finite()
    assert A.list() == A.elements()
    assert A.random_element() in A.elements()


def test_discriminant_preimage_lattice_allows_nonintegral_source_preimages():
    # Reference: A_L = L^vee / L source metadata; preimages exist before isotropic gluing.
    L = lc.Lattice("A2")
    A = L.discriminant_group()
    full_preimage = A.preimage_lattice(A.subgroup_generated_by([A.gen(0)]))

    assert full_preimage == L.dual()
    assert not full_preimage.is_integral()
    assert A.coset_representative(A.gen(0)) == A.lift(A.gen(0))
    with pytest.raises(ValueError):
        A.overlattice_from_isotropic_subgroup([A.gen(0)])


def test_gluing_accepts_sage_integral_lattice_glue_shape():
    # Reference: IntegralLatticeGluing single-lattice doctest.
    L1 = lc.Lattice(matrix(ZZ, 1, 1, [4]))
    g1 = L1.discriminant_group().gens()[0]
    M = lc.IntegralLatticeGluing([L1], [[2 * g1]])

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
    assert D.orthogonal_group(kind="quadratic").order() == 6
    assert D.order() == 8
    assert D.is_finite()
    assert D.list() == D.elements()
    assert D.random_element() in D.elements()
    assert D.exponent() == 2
    assert D.invariants() == (2, 2, 2)
    assert D.cover() is D
    assert D.relations().cardinality() == 1
    assert D.smith_form_gens() == D.gens()
    assert D.smith_form_gen(2) == D.gen(2)
    assert D.linear_combination_of_smith_form_gens((1, 0, 1)) == D.gen(0) + D.gen(2)
    assert D.gens_to_smith() == identity_matrix(ZZ, 3)
    assert D.smith_to_gens() == identity_matrix(ZZ, 3)
    assert tuple(D.gens_vector(D.gen(0) + D.gen(2))) == (1, 0, 1)
    assert tuple(D.gens_vector(D.gen(0) + D.gen(2))) == (1, 0, 1)
    assert D.coordinates(D.gen(1)) == (0, 1, 0)
    assert D.coordinates(D.gen(1)) == (0, 1, 0)
    assert D.generator_relations() == matrix.diagonal(ZZ, D.invariants())
    assert D.projection(D.lift(D.gen(1))) == D.gen(1)
    assert D.basis_from_generators(D.gens()) == D.gens()
    assert D.p_torsion(2).cardinality() == 8
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
    assert D.action_of_isometry(L.isometry_group().from_matrix(reflection))(D.gen(0)) == -D.gen(0)


def test_lattice_module_wrapper_names_preserve_owned_lattice_contract():
    # Reference: free_module/free_quadratic_module methods promoted by the consolidated category spec.
    A2 = lc.Lattice("A2")
    A2_dual = A2.dual()
    A2_QQ = A2.base_extend(QQ)

    assert not any(hasattr(A2, name) for name in ("ambient_module", "ambient_space", "ambient_vector_space"))
    assert A2_QQ == A2.rationalization()
    assert A2_QQ.base_ring() is QQ
    assert A2.dual() == A2_dual
    assert not A2.is_self_dual()
    assert lc.Lattice("U").is_self_dual()
    assert A2.absolute_discriminant() == 3
    assert A2.discriminant() == -3
    assert not A2.is_degenerate()
    assert A2.radical().rank() == 0
    assert A2_dual.denominator() == 3
    finite_index_sub = A2.sublattice([[2, 0], [0, 2]], label="2A2")
    assert finite_index_sub.index_in(A2) == 4

    fractional = A2.fractional_sublattice([[QQ(1) / 3, 0]])
    assert fractional.base_ring() is ZZ
    assert not fractional.is_integral()
    assert fractional.clear_denominators().is_integral()
    assert A2.sublattice([[1, 0]]).rank() == 1
    assert A2.sublattice([[1, 0]], label="A1_in_A2").rank() == 1
    assert A2.zero_lattice().rank() == 0
    assert A2.span([[1, 0]], base_ring=QQ).base_ring() is QQ
    assert A2.span_of_basis([[1, 0]], base_ring=QQ).base_ring() is QQ
    assert A2.span([[1, 0], [0, 1]], check_integral=True, check_even=True).is_even()
    with pytest.raises(ValueError):
        A2.span([[QQ(1) / 3, 0]], check_integral=True)
    assert A2.index_in_saturation() == A2.index_in(A2.saturation())
    nonprimitive_line = lc.Lattice("U").sublattice([[2, 0]], label="2e")
    assert nonprimitive_line.saturation(in_ambient=lc.Lattice("U")) == nonprimitive_line.primitive_closure(lc.Lattice("U"))
    assert_matrix_equal(A2.scale(2).gram_matrix(), 4 * A2.gram_matrix())
    assert A2.saturation().is_integral()


def test_discriminant_group_additive_abelian_group_api_matches_fgp_surface():
    # Reference: FGP quotient/module Smith-coordinate methods surfaced on discriminant groups.
    L = lc.Lattice(Matrix(ZZ, 2, 2, [4, 2, 2, -4]))
    A = L.discriminant_group()
    x = A.gen(0) + 3 * A.gen(1)

    assert A.underlying_abelian_group() is A
    assert A.order() == A.cardinality() == 20
    assert A.exponent() == 10
    assert not A.is_cyclic()
    assert A.generator_orders() == (2, 10)
    assert A.invariants() == (2, 10)
    assert A.elementary_divisors() == (2, 2, 5)
    assert A.rank_p(2) == 2
    assert A.rank_p(5) == 1
    assert sorted(part.invariants() for part in A.primary_decomposition()) == [(2, 2), (5,)]
    assert A.primary_part(5).invariants() == (5,)
    assert A.coordinates(x) == (1, 3)
    assert A.discrete_log(x) == (1, 3)
    assert A.discrete_exp((1, 3)) == x
    assert A.subgroup_generated_by([2 * A.gen(1)]).cardinality() == 5
    assert A.subgroup_generated_by([2 * A.gen(1)]).cardinality() == 5
    assert A.subgroup_generated_by([2 * A.gen(1)]).cardinality() == 5
    assert A.contains_subgroup(A.subgroup_generated_by([2 * A.gen(1)]))
    assert A.torsion_subgroup() is A


def test_discriminant_action_inverse_image_matches_fgp_morphism_doctest():
    # Reference: FGP morphism doctests expose kernel, image, lift, and inverse_image.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 4]))
    g = D.gen(0)
    doubling = D.hom([2 * g])
    image = D.subgroup_generated_by([2 * g])

    assert doubling.kernel().cardinality() == 2
    assert doubling.image() == image
    assert doubling.im_gens() == image.gens()
    assert doubling.lift(2 * g) == g
    with pytest.raises(ValueError):
        doubling.lift(g)
    assert doubling.inverse_image(D.subgroup_generated_by([])).cardinality() == 2
    assert doubling.inverse_image(image).cardinality() == 4


def test_discriminant_form_subgroup_source_and_action_api_is_bound():
    # Reference: torsion quadratic module subgroup/form API plus lattice source metadata.
    L = lc.Lattice(matrix(ZZ, 1, 1, [4]))
    D = L.discriminant_group()
    g = D.gen(0)
    H = D.subgroup_generated_by([2 * g])
    Z = D.subgroup_generated_by([])

    assert D.cover_lattice() == L.dual()
    assert D.cover() == L.dual()
    assert D.relation_lattice() == L
    assert D.projection(D.lift(g)) == g
    assert D.coset_representative(g) == D.lift(g)
    assert D.is_isotropic_element(D.zero())
    assert not D.is_isotropic_element(2 * g)
    assert D.is_isotropic_subgroup(Z)
    assert not D.is_isotropic_subgroup(H)
    assert D.is_anisotropic()
    assert D.orthogonal(H).cardinality() == 2
    # orthogonal quotient by the trivial subgroup is A itself -- as a FORM, not merely
    # a group of the same invariants.
    assert as_finite_quadratic_form(D.orthogonal_quotient(Z)).is_isomorphic(
        as_finite_quadratic_form(D), kind="quadratic"
    )
    with pytest.raises(ValueError):
        D.orthogonal_quotient(H)

    M = D.preimage_lattice(H, label="<1>")
    assert_matrix_equal(M.gram_matrix(), matrix(QQ, 1, 1, [1]))
    assert D.discriminant_form_of_overlattice(H).invariants() == ()

    negation = L.isometry_group().from_matrix(matrix(ZZ, 1, 1, [-1]))
    action = D.action_of_isometry(negation)
    assert action(g) == -g
    image = D.action_of_lattice_group([negation])
    assert image.order() == 2
    assert D.orbit(g, group=image) == frozenset({g, -g})


def test_lattice_exact_sequence_wrappers_use_owned_finite_quotients():
    # Reference: FGP quotient cover/relation/lift/projection contract promoted to lattices.
    A2 = lc.Lattice("A2")
    A2_dual = A2.dual()
    quotient = A2_dual.finite_quotient(A2)

    assert quotient.cover_lattice() == A2_dual
    assert quotient.relation_lattice() == A2
    assert quotient.invariants() == A2.discriminant_group().invariants()
    assert quotient.cardinality() == A2.discriminant_group().cardinality()
    assert quotient.underlying_abelian_group() is quotient
    assert quotient.exponent() == 3
    assert quotient.is_cyclic()
    assert quotient.short_name() == "Z/3"
    quotient_automorphisms = quotient.automorphism_group()
    assert quotient_automorphisms.order() == 2
    assert {action(quotient.gen(0)) for action in quotient_automorphisms} == {quotient.gen(0), -quotient.gen(0)}
    assert all(action.is_automorphism() for action in quotient_automorphisms)
    assert quotient.generator_orders() == (3,)
    assert quotient.rank_p(3) == 1
    assert quotient.rank_p(3) == 1
    assert quotient.torsion_subgroup() is quotient
    assert quotient.projection(quotient.lift(quotient.gen(0))) == quotient.gen(0)
    assert quotient.quotient_map()(quotient.lift(quotient.gen(0))) == quotient.gen(0)
    assert quotient.coset_representative(quotient.gen(0)) == quotient.lift(quotient.gen(0))
    assert quotient.preimage_lattice(quotient.subgroup_generated_by([quotient.gen(0)])) == A2_dual
    assert quotient.preimage_lattice([]) == A2
    assert A2_dual.finite_quotient(A2).invariants() == (3,)
    assert A2_dual.quotient_map_to(A2)(quotient.lift(quotient.gen(0))) == quotient.gen(0)
    assert quotient.is_finite()
    assert quotient.list() == quotient.elements()
    assert quotient.random_element() in quotient.elements()
    assert quotient.smith_form_gens() == quotient.gens()
    assert quotient.smith_form_gen(0) == quotient.gen(0)
    assert quotient.smith_form_gens() == quotient.gens()
    assert quotient.linear_combination_of_smith_form_gens([1]) == quotient.gen(0)
    assert quotient.gens_to_smith() == identity_matrix(ZZ, 1)
    assert quotient.smith_to_gens() == identity_matrix(ZZ, 1)
    assert tuple(quotient.gens_vector(quotient.gen(0))) == (1,)
    assert tuple(quotient.gens_vector(quotient.gen(0))) == (1,)
    assert quotient.coordinates(quotient.gen(0)) == (1,)
    assert quotient.coordinates(quotient.gen(0)) == (1,)
    assert quotient.generator_relations() == matrix(ZZ, 1, 1, [3])
    assert quotient.invariants() == (3,)
    assert quotient.elementary_divisors() == (3,)
    full_subgroup = quotient.subgroup_generated_by([quotient.gen(0)])
    assert full_subgroup.cardinality() == 3
    assert quotient.contains_subgroup(full_subgroup)
    assert quotient.quotient_group(full_subgroup).invariants() == ()
    assert quotient.primary_part(3).cardinality() == 3
    assert quotient.p_torsion(3).cardinality() == 3
    assert quotient.primary_decomposition()[0].cardinality() == 3
    assert len(quotient.all_submodules()) == 2
    assert quotient.basis_from_generators(quotient.gens()) == quotient.gens()
    assert len(quotient.cosets(full_subgroup)) == 1
    with pytest.raises(AssertionError):
        quotient.discrete_exp(())

    cover_mod_four = lc.Lattice(matrix(QQ, 1, 1, [QQ(1) / 4]))
    quotient_mod_four = cover_mod_four.finite_quotient(cover_mod_four.sublattice([[4]], label="4L"))
    doubling = quotient_mod_four.hom([2 * quotient_mod_four.gen(0)])
    assert doubling.kernel().cardinality() == 2
    assert doubling.image().cardinality() == 2
    assert doubling.im_gens() == doubling.image().gens()
    assert doubling.lift(2 * quotient_mod_four.gen(0)) in quotient_mod_four.elements()
    with pytest.raises(ValueError):
        doubling.lift(quotient_mod_four.gen(0))
    with pytest.raises(AssertionError):
        quotient_mod_four.discrete_exp((1, 0))


def test_lattice_morphism_lift_and_image_generators_are_bound():
    A2 = lc.Lattice("A2")
    identity = A2.Hom(A2).from_matrix(identity_matrix(ZZ, 2))

    assert identity.lift(A2.gen(1)) == A2.gen(1)
    assert identity.im_gens() == A2.gens()
    assert A2.hom(identity_matrix(ZZ, 2))(A2.gen(0)) == A2.gen(0)
    norm_eight = lc.Lattice(matrix(ZZ, 1, 1, [8]))
    norm_two = lc.Lattice(matrix(ZZ, 1, 1, [2]))
    nonprimitive_embedding = norm_eight.embedding(matrix(ZZ, 1, 1, [2]), codomain=norm_two)
    assert_matrix_equal(nonprimitive_embedding.image().gram_matrix(), norm_eight.gram_matrix())
    with pytest.raises(ValueError):
        norm_eight.embedding(matrix(ZZ, 1, 1, [2]), codomain=norm_two, primitive=True)
    assert A2.discriminant_group().smith_form_gens() == A2.discriminant_group().gens()


def test_lattice_similarity_is_scalar_form_preserving_not_an_isometry():
    # Reference: similarity maps preserve the bilinear form up to an explicit scalar.
    A2 = lc.Lattice("A2")
    twist = A2.twist(2)

    similarity = A2.similarity(identity_matrix(ZZ, 2), codomain=twist, scalar=2)
    assert similarity.scalar() == 2
    assert similarity(A2.gen(0)).q() == 2 * A2.gen(0).q()
    with pytest.raises(AssertionError):
        A2.similarity(identity_matrix(ZZ, 2), codomain=twist, scalar=3)


def test_discriminant_quotient_is_not_orthogonal_quotient_alias():
    # Reference: FGP quotient API is ordinary finite-group quotient; orthogonal quotient is separate.
    L = lc.Lattice(Matrix(ZZ, 2, 2, [4, 2, 2, -4]))
    A = L.discriminant_group()
    H = A.subgroup_generated_by([2 * A.gen(1)])
    quotient = A.quotient_group(H)

    assert H.cardinality() == 5
    assert quotient.relations() == H
    assert quotient.underlying_abelian_group() is quotient
    assert quotient.cardinality() == 4
    assert quotient.invariants() == (2, 2)
    assert quotient.exponent() == 2
    assert not quotient.is_cyclic()
    assert quotient.short_name() == "Z/2 + Z/2"
    quotient_automorphisms = quotient.automorphism_group()
    quotient_nonzero_elements = set(quotient.elements()) - {quotient.zero()}
    assert quotient_automorphisms.order() == 6
    assert {action(quotient.gen(0)) for action in quotient_automorphisms} == quotient_nonzero_elements
    assert all(action.is_automorphism() for action in quotient_automorphisms)
    assert quotient.generator_orders() == (2, 2)
    assert quotient.rank_p(2) == 2
    assert quotient.rank_p(2) == 2
    assert quotient.smith_form_gens() == quotient.gens()
    assert quotient.smith_form_gen(1) == quotient.gen(1)
    assert quotient.linear_combination_of_smith_form_gens((1, 1)) == quotient.gen(0) + quotient.gen(1)
    assert quotient.gens_to_smith() == identity_matrix(ZZ, 2)
    assert quotient.smith_to_gens() == identity_matrix(ZZ, 2)
    assert tuple(quotient.gens_vector(quotient.gen(0) + quotient.gen(1))) == (1, 1)
    assert tuple(quotient.gens_vector(quotient.gen(0) + quotient.gen(1))) == (1, 1)
    assert quotient.coordinates(quotient.gen(1)) == (0, 1)
    assert quotient.coordinates(quotient.gen(1)) == (0, 1)
    assert quotient.generator_relations() == matrix.diagonal(ZZ, quotient.invariants())
    assert quotient.projection(quotient.lift(quotient.gen(0))) == quotient.gen(0)
    quotient_line = quotient.subgroup_generated_by([quotient.gen(0)])
    assert quotient.contains_subgroup(quotient_line)
    assert quotient.quotient_group(quotient_line).invariants() == (2,)
    assert len(quotient.cosets(quotient_line)) == 2
    assert quotient.primary_part(2).cardinality() == 4
    assert quotient.p_torsion(2).cardinality() == 4
    assert len(quotient.all_submodules()) == 5
    assert quotient.basis_from_generators(quotient.gens()) == quotient.gens()
    assert quotient.torsion_subgroup() is quotient
    assert as_finite_quadratic_form(A.orthogonal_quotient(A.subgroup_generated_by([]))).is_isomorphic(
        as_finite_quadratic_form(A), kind="quadratic"
    )


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

    assert positive.is_isomorphic(negative, kind="group")
    assert positive.is_isomorphic(negative, kind="bilinear")
    assert not positive.is_isomorphic(negative, kind="quadratic")
    assert positive.isometry_to(positive, kind="quadratic").is_identity()


def test_underlying_abelian_automorphism_group_is_not_the_form_orthogonal_group():
    # Reference: discriminant groups need Aut(A) separately from O(q_A).
    D = lc.TorsionQuadraticForm(identity_matrix(QQ, 3) / 2)

    assert D.quadratic_orthogonal_group().order() == 6
    assert D.automorphism_group().order() == 168


def test_finite_quadratic_form_has_additive_group_generation_aliases():
    # Reference: additive abelian wrapper exposes from_generators and torsion subgroup helpers.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 5]))

    assert D.subgroup_generated_by([D.gen(0)]).cardinality() == D.cardinality()
    assert D.subgroup_generated_by([2 * D.gen(0)]).cardinality() == D.cardinality()
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
    dual_pairing = D.pontryagin_dual()
    assert all(dual_pairing[x](y) == D.b(x, y) for x in D.elements() for y in D.elements())
    assert D.pontryagin_dual()[D.gen(0)](D.gen(0)) == QQ(1) / 2


def test_finite_quadratic_form_promotes_torsion_quadratic_module_operations():
    # Reference: TorsionQuadraticModule finite form methods without source-lattice metadata.
    D = lc.TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(1) / 2, QQ(1) / 3]))
    H = D.subgroup_generated_by([D.gen(0)])

    assert D.value_module() == QmodnZ(QQ(1)) and D.value_module().n == 1
    assert D.value_module_qf() == QmodnZ(QQ(2)) and D.value_module_qf().n == 2
    assert D.primary_part(2).invariants() == (2,)
    assert D.primary_part(3).invariants() == (3,)
    assert sorted(part.invariants() for part in D.primary_decomposition()) == [(2,), (3,)]
    assert D.contains_subgroup(H)
    assert D.quotient_group(H).invariants() == (3,)
    assert len(D.cosets(H)) == 3
    assert D.orthogonal(H).cardinality() == 3
    assert D.restricted_form(H) == matrix(QQ, 1, 1, [QQ(1) / 2])
    assert D.normal_form() == D.normal_form(partial=True)
    assert D.is_isomorphic(lc.TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(1) / 3, QQ(1) / 2])))
    assert D.twist(2).gram_matrix_bilinear() == matrix(QQ, 1, 1, [QQ(2) / 3])
    with pytest.raises(AssertionError):
        D.discrete_exp((1,))


def test_finite_quadratic_form_normal_form_uses_generator_changes_not_only_permutations():
    # Reference: torsion quadratic module normal forms classify forms up to generator changes.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 5]))
    D_changed_generator = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(9) / 5]))

    assert D.is_isomorphic(D_changed_generator)
    assert D.normal_form() == D_changed_generator.normal_form()
    normal_form, change = D_changed_generator.normal_form(return_isometry=True)
    assert normal_form == D.normal_form()
    assert change.is_automorphism()


def test_finite_quadratic_form_bilinear_isomorphism_uses_generator_changes():
    # Reference: bilinear and quadratic isomorphism modes are distinct finite-form contracts.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 5]))
    bilinear_change = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(4) / 5]))

    assert D.is_isomorphic(bilinear_change, kind="group")
    assert D.is_isomorphic(bilinear_change, kind="bilinear")
    assert not D.is_isomorphic(bilinear_change, kind="quadratic")


def test_discriminant_group_bilinear_orthogonal_group_can_be_larger_than_quadratic():
    # Reference: finite bilinear forms and finite quadratic forms are separate categories.
    D = lc.Lattice(matrix(ZZ, 1, 1, [8])).discriminant_group()

    assert D.quadratic_orthogonal_group().order() == 2
    assert D.bilinear_orthogonal_group().order() == 4


def test_orthogonal_quotient_keeps_smith_invariants_not_only_cardinality():
    # Reference: gluing uses the finite quadratic module H^perp/H, with Smith data.
    L = lc.Lattice(matrix.diagonal(ZZ, [2, 2, 2, 2]))
    A = L.discriminant_group()
    H = A.subgroup_generated_by([A.discrete_exp((1, 1, 1, 1))])
    quotient = A.orthogonal_quotient(H)
    first, second = quotient.gens()

    assert H.is_quadratic_isotropic()
    assert quotient.cardinality() == 4
    assert quotient.invariants() == (2, 2)
    assert quotient.underlying_abelian_group() is quotient
    assert not quotient.is_cyclic()
    assert quotient.short_name() == "Z/2 + Z/2"
    quotient_automorphisms = quotient.automorphism_group()
    quotient_nonzero_elements = set(quotient.elements()) - {quotient.zero()}
    assert quotient_automorphisms.order() == 6
    assert {action(first) for action in quotient_automorphisms} == quotient_nonzero_elements
    assert all(action.is_automorphism() for action in quotient_automorphisms)
    assert quotient.generator_orders() == (2, 2)
    assert quotient.elementary_divisors() == (2, 2)
    assert quotient.rank_p(2) == 2
    assert quotient.rank_p(2) == 2
    assert quotient.is_finite()
    assert quotient.projection(quotient.lift(first)) == first
    assert quotient.discrete_exp((1, 0)) == first
    assert quotient.linear_combination_of_smith_form_gens((0, 1)) == second
    assert quotient.gens_to_smith() == identity_matrix(ZZ, 2)
    assert quotient.smith_to_gens() == identity_matrix(ZZ, 2)
    assert tuple(quotient.gens_vector(first)) == (1, 0)
    assert tuple(quotient.gens_vector(second)) == (0, 1)
    assert quotient.coordinates(first) == (1, 0)
    assert quotient.coordinates(second) == (0, 1)
    assert quotient.generator_relations() == matrix.diagonal(ZZ, quotient.invariants())
    assert quotient.coordinates(second) == (0, 1)
    line = quotient.subgroup_generated_by([first])
    assert quotient.contains_subgroup(line)
    assert quotient.quotient_group(line).invariants() == (2,)
    assert len(quotient.cosets(line)) == 2
    assert quotient.primary_part(2).cardinality() == 4
    assert quotient.p_torsion(2).cardinality() == 4
    assert len(quotient.all_submodules()) == 5
    assert quotient.basis_from_generators(quotient.gens()) == quotient.gens()
    assert quotient.torsion_subgroup() is quotient
    assert quotient.q(first) == 1
    assert quotient.q(second) == 1
    assert quotient.b(first, second) == QQ(1) / 2
    assert_matrix_equal(
        quotient.gram_matrix_quadratic(),
        matrix(QQ, 2, 2, [1, QQ(1) / 2, QQ(1) / 2, 1]),
    )
    assert A.subquotient_form(H, H).cardinality() == 1
    assert_matrix_equal(
        A.subquotient_form(H, A.orthogonal(H)).gram_matrix_quadratic(),
        quotient.gram_matrix_quadratic(),
    )
    with pytest.raises(ValueError):
        A.orthogonal_quotient(A.subgroup_generated_by([A.gen(0)]))
    with pytest.raises(ValueError):
        A.subquotient_form(H, A.subgroup_generated_by([]))


def test_discriminant_group_enumerates_all_finite_subgroups():
    # Reference: subgroup/all_subgroups should surface the finite abelian group API.
    A = lc.Lattice(matrix.diagonal(ZZ, [2, 2, 2])).discriminant_group()

    subgroup_orders = sorted(subgroup.cardinality() for subgroup in A.all_submodules())

    assert subgroup_orders == [1] + [2] * 7 + [4] * 7 + [8]


def test_pushforward_and_pullback_forms_compute_transported_pairings():
    # Reference: quotient/form API distinguishes induced forms from raw group quotients.
    D = lc.TorsionQuadraticForm(matrix(QQ, 1, 1, [QQ(1) / 5]))
    scaling = D.hom([2 * D.gen(0)])

    assert scaling.is_automorphism()
    assert not scaling.preserves_form()
    assert_matrix_equal(D.pullback_form(scaling), matrix(QQ, 1, 1, [QQ(4) / 5]))
    assert_matrix_equal(D.pushforward_form(scaling), matrix(QQ, 1, 1, [QQ(9) / 5]))


def test_supplied_generators_live_only_in_typed_subgroups_of_the_isometry_group():
    # Spec 3.3: O(L).subgroup(gens) is the ONLY home for caller-supplied
    # generators; it answers subgroup questions (preserves), never O(L)-level ones.
    A2 = lc.Lattice("A2")
    swap = matrix(ZZ, 2, 2, [0, 1, 1, 0])
    preserved = A2.sublattice([[1, 1], [1, -1]], label="swap_preserved")
    not_preserved = A2.sublattice([[2, 0], [0, 1]], label="not_swap_preserved")

    O_A2 = A2.isometry_group()
    assert O_A2.subgroup([identity_matrix(ZZ, 2)]).preserves(A2)
    assert O_A2.subgroup([swap]).preserves(preserved)
    assert not O_A2.subgroup([swap]).preserves(not_preserved)
    with pytest.raises(AssertionError):
        O_A2.subgroup([swap]).preserves(lc.Lattice("U"))  # incompatible ambient
    with pytest.raises(ValueError):
        O_A2.subgroup([matrix(ZZ, 2, 2, [2, 0, 0, 1])])  # not an isometry
    assert not hasattr(A2, "acts_on")  # deleted with no successor spelling


def test_odd_discriminant_form_remains_usable_while_odd_genus_is_unsupported():
    # Reference: Sage does not implement odd genus classification; the bilinear form still exists.
    D = lc.Lattice(matrix(ZZ, 1, 1, [3])).discriminant_group()

    assert D.value_module() == QmodnZ(QQ(1)) and D.value_module().n == 1
    assert D.value_module_qf() == QmodnZ(QQ(1)) and D.value_module_qf().n == 1
    assert D.gen(0).b(D.gen(0)) == QQ(1) / 3
    assert D.b(D.gen(0), D.gen(0)) == QQ(1) / 3
    assert D.primary_part(3).invariants() == (3,)
    assert D.subgroup_generated_by([D.gen(0)]).cardinality() == 3
    with pytest.raises(AssertionError):
        D.is_genus((1, 0), even=False)
    with pytest.raises(AssertionError):
        D.genus((1, 0), even=False)


def test_enriques_discriminant_form_reference_agrees_with_sage_at_research_scale():
    # Scale honesty: the Enriques lattice U(2) + E8(2) -- Gram = block_diagonal of
    # 2*U and 2*E8, i.e. every entry of U + E8 doubled -- has discriminant form
    # (Z/2)^10. The synthetic pipeline (lattice -> sourced discriminant form ->
    # delegated engine) must reference-agree with the direct Sage torsion module on
    # the same data. Sage's own O(q) of (Z/2)^10 does not complete, so parity is
    # asserted on the invariants Sage does complete: normal form, Brown, genus.
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
    from sage.matrix.special import block_diagonal_matrix

    enriques_gram = matrix(ZZ, block_diagonal_matrix(
        2 * IntegralLattice("U").gram_matrix(),
        2 * IntegralLattice("E8").gram_matrix(),
    ))
    L = lc.Lattice(enriques_gram)
    D = L.discriminant_group()
    oracle = IntegralLattice(enriques_gram).discriminant_group()

    # Oracle constants, from IntegralLattice(enriques_gram).discriminant_group():
    #   .invariants() == (2,)*10
    #   .brown_invariant() == 0
    #   .normal_form() Gram == block_diagonal of five hyperbolic planes [[0,1/2],[1/2,0]]
    #   .signature_pair of the lattice == (9, 1)
    expected_normal_form_gram = matrix(QQ, block_diagonal_matrix(
        [matrix(QQ, 2, 2, [0, QQ(1) / 2, QQ(1) / 2, 0])] * 5
    ))

    assert D.invariants() == (2,) * 10
    assert D.brown_invariant() == 0
    assert D.normal_form()[0] == (2,) * 10
    assert_matrix_equal(D.normal_form()[1], expected_normal_form_gram)
    assert L.signature_pair() == (9, 1)
    assert D.is_genus(L.signature_pair())
    assert D.genus(L.signature_pair()) == L.genus()

    # reference-agreement with the direct Sage computation on the same data
    assert D.normal_form()[0] == tuple(oracle.invariants())
    assert_matrix_equal(D.normal_form()[1], oracle.normal_form().gram_matrix_quadratic())
    assert D.brown_invariant() == oracle.brown_invariant()

def test_torsion_quadratic_module_doctest_parity_ledger_rows():
    # T5 mapped rows from sage/modules/torsion_quadratic_module.py doctests;
    # every expected value is copied verbatim from the source doctest output.
    D4 = lc.Lattice("D4")
    D = D4.discriminant_group()

    # brown_invariant doctest: IntegralLattice("D4").discriminant_group().brown_invariant() == 4
    assert D.brown_invariant() == 4

    # is_genus doctest: L = D4 + 3*A2-form; signatures (6,0) True, (4,2) False, (16,2) True
    L3 = lc.Lattice(3 * matrix(ZZ, 2, [2, 1, 1, 2]), label="3A2")
    L = D4.direct_sum(L3)
    DL = L.discriminant_group()
    assert DL.is_genus((6, 0))
    assert not DL.is_genus((4, 2))
    assert DL.is_genus((16, 2))

    # genus doctest: D.genus(L.signature_pair()) == L.genus() for D4 + A2
    LA = D4.direct_sum(lc.Lattice("A2"))
    assert LA.discriminant_group().genus(LA.signature_pair()) == LA.genus()

    # primary_part doctest: T = (Z/6)^3 has primary_part(2) = (Z/2)^3, and
    # primary_part at the full annihilator is the whole form
    T6 = lc.Lattice(matrix.diagonal(ZZ, [6, 6, 6])).discriminant_group()
    assert T6.invariants() == (6, 6, 6)
    assert T6.primary_part(2).invariants() == (2, 2, 2)
    # (the doctest's composite-annihilator idiom reroutes: the spike's
    # primary_part takes a prime, and the content is prime recombination)
    assert T6.primary_part(2).cardinality() * T6.primary_part(3).cardinality() == T6.cardinality()

    # twist doctest: q = diag(3/9, 1/9); invariants stable under unit/square twists
    q = lc.TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(3) / 9, QQ(1) / 9]))
    assert q.twist(-1).invariants() == (3, 9)
    assert q.twist(3).invariants() == (3, 9)
    assert q.twist(4).invariants() == (3, 9)

    # orthogonal_submodule_to doctest: T = (Z/3)^10, S = first five generators;
    # the orthogonal complement has invariants (3, 3, 3, 3, 3)
    T3 = lc.Lattice(matrix.diagonal(ZZ, [3] * 10)).discriminant_group()
    S = T3.subgroup_generated_by(list(T3.gens())[:5])
    assert T3.orthogonal_submodule_to(S).invariants() == (3, 3, 3, 3, 3)

    # __classcall__ doctest rerouted (identity -> presentation equality: Sage's
    # `D1 is D2` pins a UniqueRepresentation caching artifact, and the spike's
    # Gram-presented stratum deliberately keys parent equality on identity, so
    # the surviving mathematical content is equality of the presented form data)
    q_half = matrix(QQ, [[QQ(1) / 2]])
    left, right = lc.TorsionQuadraticForm(q_half), lc.TorsionQuadraticForm(q_half)
    assert left.invariants() == right.invariants()
    assert_matrix_equal(left.gram_matrix_quadratic(), right.gram_matrix_quadratic())


def test_torsion_quadratic_module_doctest_parity_value_pins():
    # T5 phase-2 pins for the torsion ledger's mapped-but-unpinned rows; every
    # fixture is deliberately tiny (ruling 2026-07-03: correctness evidence uses
    # very small lattices). Expected values verbatim from the source doctests.

    # TorsionQuadraticForm factory doctest: [[1,1/2],[1/2,1]] -> (2,2) in Q/2Z
    q1 = lc.TorsionQuadraticForm(Matrix(QQ, 2, [1, QQ(1) / 2, QQ(1) / 2, 1]))
    assert q1.invariants() == (2, 2)
    assert q1.value_module_qf() == QmodnZ(QQ(2))
    assert_matrix_equal(q1.gram_matrix_quadratic(), Matrix(QQ, 2, [1, QQ(1) / 2, QQ(1) / 2, 1]))

    # factory row diag(1/4,1/3) REROUTED: Sage's constructor Smith-collapses to
    # invariants (12,) / Gram [7/12] (that Gram is a repr of the mod-1 form, not
    # a valid reconstruction input — fed back in, both Sage and the spike read
    # [7/12] at modulus 2, a different form); the spike keeps the per-generator
    # presentation, so the surviving content is the group order, the Smith
    # invariants, and normal-form agreement with the oracle on the same data
    from sage.modules.torsion_quadratic_module import TorsionQuadraticForm as SageTorsionForm

    q2 = lc.TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(1) / 4, QQ(1) / 3]))
    oracle = SageTorsionForm(matrix.diagonal(QQ, [QQ(1) / 4, QQ(1) / 3])).normal_form()
    assert q2.cardinality() == 12
    assert q2.normal_form()[0] == tuple(oracle.invariants()) == (12,)
    assert_matrix_equal(q2.normal_form()[1], oracle.gram_matrix_quadratic())

    # factory doctest: diag(3/4, 3/8, 3/8) -> invariants (4, 8, 8)
    q3 = lc.TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(3) / 4, QQ(3) / 8, QQ(3) / 8]))
    assert q3.invariants() == (4, 8, 8)
    assert_matrix_equal(q3.gram_matrix_quadratic(), matrix.diagonal(QQ, [QQ(3) / 4, QQ(3) / 8, QQ(3) / 8]))

    # twist doctest Gram rows (the ledger test pins the invariants; these pin
    # the quadratic Grams: q = diag(3/9, 1/9))
    q = lc.TorsionQuadraticForm(matrix.diagonal(QQ, [QQ(3) / 9, QQ(1) / 9]))
    assert_matrix_equal(q.twist(-1).gram_matrix_quadratic(), matrix.diagonal(QQ, [QQ(2) / 3, QQ(8) / 9]))
    assert_matrix_equal(q.twist(3).gram_matrix_quadratic(), matrix.diagonal(QQ, [1, QQ(1) / 3]))
    assert_matrix_equal(q.twist(4).gram_matrix_quadratic(), matrix.diagonal(QQ, [QQ(4) / 3, QQ(4) / 9]))

    # orthogonal_group(gens=[f]) doctest: the swap on identity/2 generates order 2
    D2 = lc.TorsionQuadraticForm(identity_matrix(QQ, 2) / 2)
    assert D2.orthogonal_group(gens=[matrix(ZZ, 2, [0, 1, 1, 0])]).order() == 2

    # brown_invariant doctest error branch: an odd form propagates the oracle's
    # rejection (values must lie in QQ/2ZZ)
    with pytest.raises(ValueError):
        lc.TorsionQuadraticForm(matrix(QQ, [[QQ(1) / 3]])).brown_invariant()


def test_maximal_overlattice_p_local_reference_agrees_with_sage_on_small_fixture():
    # Reference: IntegralLattice.maximal_overlattice doctests. The source fixture
    # A4.twist(25*89) has a discriminant group of order 5^9 * 89^4 — rerouted to a
    # small fixture (ruling 2026-07-03: correctness evidence uses very small
    # lattices); the p-local maximization content is pinned by direct oracle
    # agreement on A2.twist(9) (discriminant group order 3^5 = 243).
    from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice

    gram = matrix(ZZ, 2, [2, -1, -1, 2])
    L = lc.Lattice("A2").twist(9)
    oracle = IntegralLattice(gram).twist(9)
    assert L.maximal_overlattice().is_even()
    assert L.maximal_overlattice().determinant() == oracle.maximal_overlattice().determinant()
    assert L.maximal_overlattice(3).determinant() == oracle.maximal_overlattice(3).determinant()


def test_free_quadratic_module_determinant_discriminant_and_gram_doctest_rows():
    # Reference: free_quadratic_module.py determinant/discriminant/gram_matrix
    # doctests. Sage's span-in-ambient builds become spans of the identity-Gram
    # parent in its own coordinates (the operation maps; the builder reroutes).
    M = lc.Lattice(identity_matrix(ZZ, 3), label="I3")
    assert M.determinant() == 1
    assert M.span([[1, 2, 3]]).determinant() == 14
    assert M.span([[1, 2, 3], [1, 1, 1]]).determinant() == 6

    # discriminant TESTS rows: FreeQuadraticModule's signed (-1)^(rank//2) * det
    # convention is exactly the spike's discriminant()
    assert lc.Lattice(identity_matrix(ZZ, 2), label="I2").discriminant() == -1
    assert lc.Lattice(identity_matrix(QQ, 3), base_ring=QQ, label="I3Q").discriminant() == -1

    # gram_matrix doctest: span_of_basis([u, v, w]) over the QQ^4 dot product
    V4 = lc.Lattice(identity_matrix(QQ, 4), base_ring=QQ, label="Q4")
    u = [QQ(1) / 2, QQ(1) / 2, QQ(1) / 2, QQ(1) / 2]
    v = [0, 1, 1, 0]
    w = [0, 0, 1, 1]
    L = V4.span_of_basis([u, v, w], base_ring=ZZ)
    assert_matrix_equal(L.gram_matrix(), Matrix(QQ, 3, [1, 1, 1, 1, 2, 1, 1, 1, 2]))

    # integer_symmetric residue pin: IntegralLattice("U").signature() == 0
    assert lc.Lattice("U").signature() == 0


def test_free_module_index_and_saturation_doctest_rows():
    # Reference: free_module.py index_in / index_in_saturation / saturation /
    # denominator doctests, rerouted from ambient spans to spans of an
    # identity-Gram parent in its own coordinates.
    Z2 = lc.Lattice(identity_matrix(ZZ, 2), label="Z2")
    assert Z2.span([[3, 6]]).index_in(Z2.span([[1, 2]])) == 3

    L1 = Z2.span([[QQ(1) / 2, QQ(1) / 3], [4, 5]])
    L2 = Z2.span([[1, 2], [3, 4]])
    assert L2.index_in(L1) == QQ(12) / 7
    assert L1.index_in(L2) == QQ(7) / 12
    # discriminant ratio row: signs cancel at equal rank, so the spike's signed
    # convention reproduces the doctest's 49/144
    assert L1.discriminant() / L2.discriminant() == QQ(49) / 144
    from sage.rings.infinity import Infinity

    assert Z2.span([[1, 2]]).index_in(Z2) == Infinity

    # index_in_saturation doctest rows
    Z3 = lc.Lattice(identity_matrix(ZZ, 3), label="Z3")
    assert Z3.span([[2, 4, 6]]).index_in_saturation() == 2
    assert Z2.span([[QQ(1) / 2, QQ(1) / 3]]).index_in_saturation() == QQ(1) / 6

    # saturation doctests: the pinned echelon bases [3,3,2] and
    # [[1,0,-1],[0,1,2]] are ambient artifacts; their intrinsic content is the
    # Gram/determinant data those bases generate
    W = Z3.span([[9, 9, 6]])
    assert_matrix_equal(W.saturation().gram_matrix(), matrix(ZZ, 1, 1, [22]))
    assert W.index_in_saturation() == 3
    L = Z3.span([[1, 2, 3], [4, 5, 6]])
    assert L.determinant() == 54
    assert L.saturation().determinant() == 6

    # denominator doctest REROUTED: Sage's value 30 is the denominator of the
    # echelon basis matrix — an ambient-coordinate artifact the based model
    # drops. The intrinsic denominator clears the Gram; pin it by direct oracle
    # agreement on the same span data.
    Q3 = lc.Lattice(identity_matrix(QQ, 3), base_ring=QQ, label="Q3")
    spike_span = Q3.span([[1, QQ(1) / 2, QQ(1) / 3], [-QQ(1) / 5, QQ(2) / 3, 3]], base_ring=ZZ)
    oracle_span = (QQ ** 3).span([[1, QQ(1) / 2, QQ(1) / 3], [-QQ(1) / 5, QQ(2) / 3, 3]], ZZ)
    assert spike_span.denominator() == oracle_span.gram_matrix().denominator()


def test_integer_lattice_invariant_pins_and_free_module_intersection_rows():
    # References: free_module_integer.py volume/discriminant/is_unimodular
    # doctests (their gen_lattice fixture is crypto rank-10 — rerouted to a
    # tiny fixture by oracle agreement per the small-lattices ruling) and
    # free_module.py intersection doctests (pinned echelon bases rerouted to
    # their intrinsic Gram/index content).
    from sage.modules.free_module_integer import IntegerLattice

    # IntegerLattice([[2,0],[0,3]]) is basis rows in the ambient dot product,
    # i.e. Gram diag(4, 9)
    small = lc.Lattice(matrix.diagonal(ZZ, [4, 9]), label="diag49")
    oracle = IntegerLattice([[2, 0], [0, 3]])
    assert small.volume() == oracle.volume() == 6
    # naming-collision guard (ledger): Sage IntegerLattice.discriminant() is
    # |det| = the spike's absolute_discriminant(); the spike's discriminant()
    # is the signed Nikulin convention
    assert small.absolute_discriminant() == oracle.discriminant() == 36
    assert small.discriminant() == -36
    assert lc.Lattice(identity_matrix(ZZ, 2)).is_unimodular()
    assert not small.is_unimodular()

    # intersection doctest rows: [3 3] -> Gram [18], index 1 in the smaller span
    Z2 = lc.Lattice(identity_matrix(ZZ, 2), label="Z2")
    meet = Z2.span([[1, 1]]).intersection(Z2.span([[3, 3]]))
    assert_matrix_equal(meet.gram_matrix(), matrix(ZZ, 1, 1, [18]))
    assert meet.index_in(Z2.span([[3, 3]])) == 1

    # [2 2 2] -> Gram [12]
    Z3 = lc.Lattice(identity_matrix(ZZ, 3), label="Z3")
    meet3 = Z3.span([[1, 1, 1], [1, 2, 3]]).intersection(Z3.span([[2, 2, 2], [1, 0, 0]]))
    assert_matrix_equal(meet3.gram_matrix(), matrix(ZZ, 1, 1, [12]))

    # Sage's scale(c) scales the module (basis rows), not the form: the scaled
    # spans reroute to fractional spans of the same rows; [1/3 2/3] -> Gram [5/9]
    frac = Z2.span([[QQ(1) / 6, QQ(1) / 3]]).intersection(Z2.span([[QQ(1) / 15, QQ(2) / 15]]))
    assert_matrix_equal(frac.gram_matrix(), matrix(QQ, 1, 1, [QQ(5) / 9]))

    # mixed ZZ/QQ intersection is symmetric (issue-23703 row): [1/2 0 1/2] -> Gram [1/2]
    W = Z3.span([[QQ(1) / 2, 0, QQ(1) / 2]])
    K = Z3.span([[1, 0, 1], [0, 0, 1]], base_ring=QQ)
    assert_matrix_equal(W.intersection(K).gram_matrix(), matrix(QQ, 1, 1, [QQ(1) / 2]))
    assert_matrix_equal(K.intersection(W).gram_matrix(), matrix(QQ, 1, 1, [QQ(1) / 2]))
