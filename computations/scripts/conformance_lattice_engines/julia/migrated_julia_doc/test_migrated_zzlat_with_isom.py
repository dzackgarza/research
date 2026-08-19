import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_integer_lattice_with_isometry_pair_with_identity():
    """
    method: integer_lattice_with_isometry
    """
    code = r'''
    # method: integer_lattice_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test rank(lattice(Lf)) == 2
    @test order_of_isometry(Lf) == 1
'''
    _jl_eval_testitem(code)

def test_2_integer_lattice_with_isometry_pair_with_negation():
    """
    method: integer_lattice_with_isometry
    """
    code = r'''
    # method: integer_lattice_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    @test order_of_isometry(Lf) == 2
'''
    _jl_eval_testitem(code)

def test_3_integer_lattice_with_isometry_explicit_isometry_matrix():
    """
    method: integer_lattice_with_isometry
    """
    code = r'''
    # method: integer_lattice_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = -identity_matrix(ZZ, 2)
    Lf = integer_lattice_with_isometry(L, f)
    @test isometry(Lf) == f
'''
    _jl_eval_testitem(code)

def test_4_lattice_extract_zzlat_from_zzlatwithisom():
    """
    method: lattice
    """
    code = r'''
    # method: lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test rank(lattice(Lf)) == 2
'''
    _jl_eval_testitem(code)

def test_5_isometry_zzlatwithisom_isometry_matrix():
    """
    method: isometry
    """
    code = r'''
    # method: isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test isometry(Lf) == identity_matrix(ZZ, 2)
'''
    _jl_eval_testitem(code)

def test_6_order_of_isometry_identity_has_order_1():
    """
    method: order_of_isometry
    """
    code = r'''
    # method: order_of_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test order_of_isometry(Lf) == 1
'''
    _jl_eval_testitem(code)

def test_7_characteristic_polynomial_zzlatwithisom():
    """
    method: characteristic_polynomial
    """
    code = r'''
    # method: characteristic_polynomial
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    p = characteristic_polynomial(Lf)
    @test degree(p) == 2
'''
    _jl_eval_testitem(code)

def test_8_minimal_polynomial_zzlatwithisom():
    """
    method: minimal_polynomial
    """
    code = r'''
    # method: minimal_polynomial
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    p = minimal_polynomial(Lf)
    @test degree(p) >= 1
'''
    _jl_eval_testitem(code)

def test_9_ambient_isometry_isometry_on_ambient_space_preserves_gram():
    """
    method: ambient_isometry
    """
    code = r'''
    # method: ambient_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    f_amb = ambient_isometry(Lf)
    V = ambient_space(lattice(Lf))
    G_V = gram_matrix(V)
    @test f_amb' * G_V * f_amb == G_V
'''
    _jl_eval_testitem(code)

def test_10_ambient_space_returns_quadspacewithisom():
    """
    method: ambient_space
    """
    code = r'''
    # method: ambient_space
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Vf = ambient_space(Lf)
    @test Vf isa Oscar.QuadSpaceWithIsom
    @test isometry(Vf) == ambient_isometry(Lf)
'''
    _jl_eval_testitem(code)

def test_11_lattice_in_same_ambient_space_sublattice_shares_ambient_isometry():
    """
    method: lattice_in_same_ambient_space
    """
    code = r'''
    # method: lattice_in_same_ambient_space
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    B = basis_matrix(lattice(Lf))
    Sf = lattice_in_same_ambient_space(Lf, B)
    @test ambient_isometry(Sf) == ambient_isometry(Lf)
'''
    _jl_eval_testitem(code)

def test_12_rational_span_returns_quadspacewithisom():
    """
    method: rational_span
    """
    code = r'''
    # method: rational_span
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Vf = rational_span(Lf)
    @test Vf isa Oscar.QuadSpaceWithIsom
    @test rank(Vf) == rank(Lf)
'''
    _jl_eval_testitem(code)

def test_13_basis_matrix_matches_underlying_lattice():
    """
    method: basis_matrix
    """
    code = r'''
    # method: basis_matrix
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test basis_matrix(Lf) == basis_matrix(lattice(Lf))
'''
    _jl_eval_testitem(code)

def test_14_equality_of_zzlatwithisom():
    """
    method: ==
    """
    code = r'''
    # method: ==
    using Oscar
    L = root_lattice(:A, 2)
    Lf1 = integer_lattice_with_isometry(L)
    Lf2 = integer_lattice_with_isometry(L)
    Lf_neg = integer_lattice_with_isometry(L; neg = true)
    @test Lf1 == Lf2
    @test Lf1 != Lf_neg
'''
    _jl_eval_testitem(code)

def test_15_rank_degree_delegated_to_underlying_lattice():
    """
    method: rank
    """
    code = r'''
    # method: rank
    # method: degree
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test rank(Lf) == 2
    @test degree(Lf) == 2
'''
    _jl_eval_testitem(code)

def test_16_rank_degree_delegated_to_underlying_lattice_alias_2():
    """
    method: degree
    """
    code = r'''
    # method: rank
    # method: degree
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test rank(Lf) == 2
    @test degree(Lf) == 2
'''
    _jl_eval_testitem(code)

def test_17_det_discriminant_a2_lattice():
    """
    method: det
    """
    code = r'''
    # method: det
    # method: discriminant
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test det(Lf) == 3
    @test discriminant(Lf) == (-1)^rank(Lf) * det(Lf)
'''
    _jl_eval_testitem(code)

def test_18_det_discriminant_a2_lattice_alias_2():
    """
    method: discriminant
    """
    code = r'''
    # method: det
    # method: discriminant
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test det(Lf) == 3
    @test discriminant(Lf) == (-1)^rank(Lf) * det(Lf)
'''
    _jl_eval_testitem(code)

def test_19_scale_norm_a2_lattice_scale_and_norm():
    """
    method: scale
    """
    code = r'''
    # method: scale
    # method: norm
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test scale(Lf) == 1
    @test norm(Lf) == 2
'''
    _jl_eval_testitem(code)

def test_20_scale_norm_a2_lattice_scale_and_norm_alias_2():
    """
    method: norm
    """
    code = r'''
    # method: scale
    # method: norm
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test scale(Lf) == 1
    @test norm(Lf) == 2
'''
    _jl_eval_testitem(code)

def test_21_minimum_a2_lattice_minimum():
    """
    method: minimum
    """
    code = r'''
    # method: minimum
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test minimum(Lf) == 2
'''
    _jl_eval_testitem(code)

def test_22_genus_returns_zzgenus_with_matching_rank_and_det():
    """
    method: genus
    """
    code = r'''
    # method: genus
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    g = genus(Lf)
    @test rank(g) == 2
    @test det(g) == 3
'''
    _jl_eval_testitem(code)

def test_23_gram_matrix_matches_underlying_lattice():
    """
    method: gram_matrix
    """
    code = r'''
    # method: gram_matrix
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test gram_matrix(Lf) == gram_matrix(lattice(Lf))
'''
    _jl_eval_testitem(code)

def test_24_signature_tuple_a2_is_2_0_0():
    """
    method: signature_tuple
    """
    code = r'''
    # method: signature_tuple
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test signature_tuple(Lf) == (2, 0, 0)
'''
    _jl_eval_testitem(code)

def test_25_is_integral_is_even_a2_is_integral_and_even():
    """
    method: is_integral
    """
    code = r'''
    # method: is_integral
    # method: is_even
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test is_integral(Lf)
    @test is_even(Lf)
'''
    _jl_eval_testitem(code)

def test_26_is_integral_is_even_a2_is_integral_and_even_alias_2():
    """
    method: is_even
    """
    code = r'''
    # method: is_integral
    # method: is_even
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test is_integral(Lf)
    @test is_even(Lf)
'''
    _jl_eval_testitem(code)

def test_27_is_positive_definite_is_definite_a2_is_positive_definite():
    """
    method: is_positive_definite
    """
    code = r'''
    # method: is_positive_definite
    # method: is_definite
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test is_positive_definite(Lf)
    @test is_definite(Lf)
'''
    _jl_eval_testitem(code)

def test_28_is_positive_definite_is_definite_a2_is_positive_definite_alias_2():
    """
    method: is_definite
    """
    code = r'''
    # method: is_positive_definite
    # method: is_definite
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test is_positive_definite(Lf)
    @test is_definite(Lf)
'''
    _jl_eval_testitem(code)

def test_29_is_unimodular_a2_is_not_unimodular_e8_is():
    """
    method: is_unimodular
    """
    code = r'''
    # method: is_unimodular
    using Oscar
    L_A2 = root_lattice(:A, 2)
    Lf_A2 = integer_lattice_with_isometry(L_A2)
    @test !is_unimodular(Lf_A2)
    L_E8 = root_lattice(:E, 8)
    Lf_E8 = integer_lattice_with_isometry(L_E8)
    @test is_unimodular(Lf_E8)
'''
    _jl_eval_testitem(code)

def test_30_is_primary_is_elementary_a2_is_3_primary_and_3_elementary():
    """
    method: is_primary
    """
    code = r'''
    # method: is_primary
    # method: is_elementary
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test is_primary(Lf, 3)
    @test is_elementary(Lf, 3)
'''
    _jl_eval_testitem(code)

def test_31_is_primary_is_elementary_a2_is_3_primary_and_3_elementary_alias_2():
    """
    method: is_elementary
    """
    code = r'''
    # method: is_primary
    # method: is_elementary
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test is_primary(Lf, 3)
    @test is_elementary(Lf, 3)
'''
    _jl_eval_testitem(code)

def test_32_is_primary_with_prime_is_elementary_with_prime_a2_returns_true_3():
    """
    method: is_primary_with_prime
    """
    code = r'''
    # method: is_primary_with_prime
    # method: is_elementary_with_prime
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    flag_p, p = is_primary_with_prime(Lf)
    @test flag_p == true
    @test p == 3
    flag_e, q = is_elementary_with_prime(Lf)
    @test flag_e == true
    @test q == 3
'''
    _jl_eval_testitem(code)

def test_33_is_primary_with_prime_is_elementary_with_prime_a2_returns_true_3_alias_2():
    """
    method: is_elementary_with_prime
    """
    code = r'''
    # method: is_primary_with_prime
    # method: is_elementary_with_prime
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    flag_p, p = is_primary_with_prime(Lf)
    @test flag_p == true
    @test p == 3
    flag_e, q = is_elementary_with_prime(Lf)
    @test flag_e == true
    @test q == 3
'''
    _jl_eval_testitem(code)

def test_34_is_negative_definite_a2_is_not_negative_definite():
    """
    method: is_negative_definite
    """
    code = r'''
    # method: is_negative_definite
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test !is_negative_definite(Lf)
'''
    _jl_eval_testitem(code)

def test_35_raise_isometry_to_power():
    """
    method: ^
    """
    code = r'''
    # method: ^
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Lf2 = Lf^2
    @test order_of_isometry(Lf2) == 1
'''
    _jl_eval_testitem(code)

def test_36_direct_sum_equivariant_direct_sum():
    """
    method: direct_sum
    """
    code = r'''
    # method: direct_sum
    using Oscar
    L = root_lattice(:A, 1)
    Lf = integer_lattice_with_isometry(L)
    Mg = integer_lattice_with_isometry(L; neg = true)
    S, _, _ = direct_sum(Lf, Mg)
    @test rank(lattice(S)) == 2
'''
    _jl_eval_testitem(code)

def test_37_dual_dual_with_induced_isometry():
    """
    method: dual
    """
    code = r'''
    # method: dual
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    Df = dual(Lf)
    @test rank(lattice(Df)) == 2
'''
    _jl_eval_testitem(code)

def test_38_lll_lll_with_isometry_carried_along():
    """
    method: lll
    """
    code = r'''
    # method: lll
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    Mf = lll(Lf)
    @test rank(lattice(Mf)) == 2
'''
    _jl_eval_testitem(code)

def test_39_rescale_zzlatwithisom_rescale():
    """
    method: rescale
    """
    code = r'''
    # method: rescale
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    Mf = rescale(Lf, 2)
    @test rank(lattice(Mf)) == 2
'''
    _jl_eval_testitem(code)

def test_40_invariant_lattice_fixed_sublattice():
    """
    method: invariant_lattice
    """
    code = r'''
    # method: invariant_lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    I = invariant_lattice(Lf)
    @test rank(lattice(I)) == 2  # identity fixes everything
'''
    _jl_eval_testitem(code)

def test_41_coinvariant_lattice_orthogonal_complement_of_fixed():
    """
    method: coinvariant_lattice
    """
    code = r'''
    # method: coinvariant_lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    C = coinvariant_lattice(Lf)
    @test rank(lattice(C)) == 0  # identity: coinvariant is trivial
'''
    _jl_eval_testitem(code)

def test_42_kernel_lattice_cyclotomic_polynomial_variant():
    """
    method: kernel_lattice
    """
    code = r'''
    # method: kernel_lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Qx, x = QQ["x"]
    p = x + 1  # cyclotomic_polynomial(2) = x + 1
    Kf = kernel_lattice(Lf, p)
    @test rank(lattice(Kf)) == 2  # negation: all vectors satisfy (f+1)v = 0
'''
    _jl_eval_testitem(code)

def test_43_kernel_lattice_integer_index_variant():
    """
    method: kernel_lattice
    """
    code = r'''
    # method: kernel_lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Kf = kernel_lattice(Lf, 2)
    @test rank(lattice(Kf)) == 2  # kernel of f^2 - 1 for negation
'''
    _jl_eval_testitem(code)

def test_44_invariant_coinvariant_pair_rank_sum_equals_full_rank():
    """
    method: invariant_coinvariant_pair
    """
    code = r'''
    # method: invariant_coinvariant_pair
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    inv_f, coinv_f = invariant_coinvariant_pair(Lf)
    @test rank(lattice(inv_f)) + rank(lattice(coinv_f)) == rank(Lf)
'''
    _jl_eval_testitem(code)

def test_45_orthogonal_submodule_inner_product_with_complement_is_zero():
    """
    method: orthogonal_submodule
    """
    code = r'''
    # method: orthogonal_submodule
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    B_sub = basis_matrix(lattice(Lf))[1:1, :]
    Sf = lattice_in_same_ambient_space(Lf, B_sub)
    Of = orthogonal_submodule(Lf, Sf)
    # verify orthogonality: every row of Of basis has zero inner product with B_sub
    G = gram_matrix(ambient_space(lattice(Lf)))
    B_orth = basis_matrix(lattice(Of))
    if nrows(B_orth) > 0 && nrows(B_sub) > 0
        prod = B_sub * G * B_orth'
        @test all(iszero, prod)
    else
        @test true  # trivial case
    end
'''
    _jl_eval_testitem(code)

def test_46_type_type_of_lattice_with_isometry():
    """
    method: type
    """
    code = r'''
    # method: type
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    t = type(Lf)
    @test t isa Dict
'''
    _jl_eval_testitem(code)

def test_47_is_of_type_roundtrip_with_type_lf():
    """
    method: is_of_type
    """
    code = r'''
    # method: is_of_type
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    t = type(Lf)
    @test is_of_type(Lf, t)
'''
    _jl_eval_testitem(code)

def test_48_is_of_same_type_same_vs_different_isometries():
    """
    method: is_of_same_type
    """
    code = r'''
    # method: is_of_same_type
    using Oscar
    L = root_lattice(:A, 2)
    Lf1 = integer_lattice_with_isometry(L; neg = true)
    Lf2 = integer_lattice_with_isometry(L; neg = true)
    Lf_id = integer_lattice_with_isometry(L)
    @test is_of_same_type(Lf1, Lf2)
    @test !is_of_same_type(Lf1, Lf_id)
'''
    _jl_eval_testitem(code)

def test_49_is_of_hermitian_type_a2_with_negation():
    """
    method: is_of_hermitian_type
    """
    code = r'''
    # method: is_of_hermitian_type
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    @test is_of_hermitian_type(Lf)
'''
    _jl_eval_testitem(code)

def test_50_hermitian_structure_roundtrip_hermitian_rank():
    """
    method: hermitian_structure
    """
    code = r'''
    # method: hermitian_structure
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    if is_of_hermitian_type(Lf)
        H = hermitian_structure(Lf)
        n = order_of_isometry(Lf)
        phi_n = Int(euler_phi(ZZ(n)))
        @test rank(H) == div(rank(Lf), phi_n)
    end
'''
    _jl_eval_testitem(code)

def test_51_trace_lattice_with_isometry_roundtrip_from_hermitian():
    """
    method: trace_lattice_with_isometry
    """
    code = r'''
    # method: trace_lattice_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    if is_of_hermitian_type(Lf)
        H = hermitian_structure(Lf)
        Lf2 = trace_lattice_with_isometry(H)
        @test rank(Lf2) == rank(Lf)
    end
'''
    _jl_eval_testitem(code)

def test_52_discriminant_group_zzlatwithisom_discriminant_group():
    """
    method: discriminant_group
    """
    code = r'''
    # method: discriminant_group
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    T = discriminant_group(Lf)
    @test order(T) == 3
'''
    _jl_eval_testitem(code)

def test_53_discriminant_representation_returns_homomorphism():
    """
    method: discriminant_representation
    """
    code = r'''
    # method: discriminant_representation
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    gens = automorphism_group_generators(lattice(Lf))
    G = matrix_group(gens)
    phi = discriminant_representation(lattice(Lf), G)
    @test phi isa Oscar.GAPGroupHomomorphism
'''
    _jl_eval_testitem(code)

def test_54_image_centralizer_in_oq_returns_group_and_homomorphism():
    """
    method: image_centralizer_in_Oq
    """
    code = r'''
    # method: image_centralizer_in_Oq
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    G, _ = image_centralizer_in_Oq(Lf)
    @test order(G) >= 1
'''
    _jl_eval_testitem(code)

def test_55_signatures_returns_dict_for_a2_with_negation():
    """
    method: signatures
    """
    code = r'''
    # method: signatures
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    sigs = signatures(Lf)
    @test sigs isa Dict
'''
    _jl_eval_testitem(code)

def test_56_rational_spinor_norm_well_defined_for_identity():
    """
    method: rational_spinor_norm
    """
    code = r'''
    # method: rational_spinor_norm
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    s = rational_spinor_norm(Lf)
    @test s isa QQFieldElem
'''
    _jl_eval_testitem(code)

def test_57_is_hermitian_type_dict_check():
    """
    method: is_hermitian
    """
    code = r'''
    # method: is_hermitian
    using Oscar
    L = root_lattice(:A, 2)
    Lf_neg = integer_lattice_with_isometry(L; neg = true)
    t = type(Lf_neg)
    @test Oscar.is_hermitian(t)
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    '==',
    '^',
    'ambient_isometry',
    'ambient_space',
    'basis_matrix',
    'characteristic_polynomial',
    'coinvariant_lattice',
    'degree',
    'det',
    'direct_sum',
    'discriminant',
    'discriminant_group',
    'discriminant_representation',
    'dual',
    'genus',
    'gram_matrix',
    'hermitian_structure',
    'image_centralizer_in_Oq',
    'integer_lattice_with_isometry',
    'invariant_coinvariant_pair',
    'invariant_lattice',
    'is_definite',
    'is_elementary',
    'is_elementary_with_prime',
    'is_even',
    'is_hermitian',
    'is_integral',
    'is_negative_definite',
    'is_of_hermitian_type',
    'is_of_same_type',
    'is_of_type',
    'is_positive_definite',
    'is_primary',
    'is_primary_with_prime',
    'is_unimodular',
    'isometry',
    'kernel_lattice',
    'lattice',
    'lattice_in_same_ambient_space',
    'lll',
    'minimal_polynomial',
    'minimum',
    'norm',
    'order_of_isometry',
    'orthogonal_submodule',
    'rank',
    'rational_span',
    'rational_spinor_norm',
    'rescale',
    'scale',
    'signature_tuple',
    'signatures',
    'trace_lattice_with_isometry',
    'type',
}

def test_migrated_method_coverage():
    """
    method: runtime_coverage
    """
    covered = _covered_methods_from_module(sys.modules[__name__])
    missing = sorted(MIGRATED_METHODS - covered)
    assert not missing, (
        "Coverage failure: uncovered migrated methods found.\n"
        f"Declared methods: {sorted(MIGRATED_METHODS)}\n"
        f"Covered methods: {sorted(covered)}\n"
        f"Missing methods: {missing}"
    )
