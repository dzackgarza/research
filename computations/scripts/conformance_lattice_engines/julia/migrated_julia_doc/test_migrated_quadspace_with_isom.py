import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_quadratic_space_with_isometry_pair_space_with_identity():
    """
    method: quadratic_space_with_isometry
    """
    code = r'''
    # method: quadratic_space_with_isometry
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test rank(Vf) == 2
    @test order_of_isometry(Vf) == 1
'''
    _jl_eval_testitem(code)

def test_2_quadratic_space_with_isometry_pair_with_negation():
    """
    method: quadratic_space_with_isometry
    """
    code = r'''
    # method: quadratic_space_with_isometry
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V; neg = true)
    @test rank(Vf) == 2
    @test order_of_isometry(Vf) == 2
'''
    _jl_eval_testitem(code)

def test_3_space_extract_space_from_quadspacewithisom():
    """
    method: space
    """
    code = r'''
    # method: space
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test rank(space(Vf)) == 2
'''
    _jl_eval_testitem(code)

def test_4_isometry_extract_isometry_matrix():
    """
    method: isometry
    """
    code = r'''
    # method: isometry
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    f = isometry(Vf)
    @test f == identity_matrix(QQ, 2)
'''
    _jl_eval_testitem(code)

def test_5_order_of_isometry_quadspacewithisom():
    """
    method: order_of_isometry
    """
    code = r'''
    # method: order_of_isometry
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V; neg = true)
    @test order_of_isometry(Vf) == 2
'''
    _jl_eval_testitem(code)

def test_6_dim_rank_through_quadspacewithisom():
    """
    method: dim
    """
    code = r'''
    # method: dim
    # method: rank
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test dim(Vf) == 2
    @test rank(Vf) == 2
'''
    _jl_eval_testitem(code)

def test_7_dim_rank_through_quadspacewithisom_alias_2():
    """
    method: rank
    """
    code = r'''
    # method: dim
    # method: rank
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test dim(Vf) == 2
    @test rank(Vf) == 2
'''
    _jl_eval_testitem(code)

def test_8_gram_matrix_det_discriminant_quadspacewithisom():
    """
    method: gram_matrix
    """
    code = r'''
    # method: gram_matrix
    # method: det
    # method: discriminant
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test gram_matrix(Vf) == QQ[2 1; 1 2]
    d = det(Vf)
    @test d == 3
    @test discriminant(Vf) == (-1)^dim(Vf) * d
'''
    _jl_eval_testitem(code)

def test_9_gram_matrix_det_discriminant_quadspacewithisom_alias_2():
    """
    method: det
    """
    code = r'''
    # method: gram_matrix
    # method: det
    # method: discriminant
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test gram_matrix(Vf) == QQ[2 1; 1 2]
    d = det(Vf)
    @test d == 3
    @test discriminant(Vf) == (-1)^dim(Vf) * d
'''
    _jl_eval_testitem(code)

def test_10_gram_matrix_det_discriminant_quadspacewithisom_alias_3():
    """
    method: discriminant
    """
    code = r'''
    # method: gram_matrix
    # method: det
    # method: discriminant
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test gram_matrix(Vf) == QQ[2 1; 1 2]
    d = det(Vf)
    @test d == 3
    @test discriminant(Vf) == (-1)^dim(Vf) * d
'''
    _jl_eval_testitem(code)

def test_11_diagonal_signature_tuple_positive_definite_space():
    """
    method: diagonal
    """
    code = r'''
    # method: diagonal
    # method: signature_tuple
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    diag = diagonal(Vf)
    @test length(diag) == 2
    @test all(x -> x > 0, diag)
    @test signature_tuple(Vf) == (2, 0)
'''
    _jl_eval_testitem(code)

def test_12_diagonal_signature_tuple_positive_definite_space_alias_2():
    """
    method: signature_tuple
    """
    code = r'''
    # method: diagonal
    # method: signature_tuple
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    diag = diagonal(Vf)
    @test length(diag) == 2
    @test all(x -> x > 0, diag)
    @test signature_tuple(Vf) == (2, 0)
'''
    _jl_eval_testitem(code)

def test_13_is_definite_is_positive_definite_is_negative_definite_quadspacewithisom():
    """
    method: is_definite
    """
    code = r'''
    # method: is_definite
    # method: is_positive_definite
    # method: is_negative_definite
    using Oscar
    V_pd = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf_pd = quadratic_space_with_isometry(V_pd)
    @test is_definite(Vf_pd)
    @test is_positive_definite(Vf_pd)
    @test !is_negative_definite(Vf_pd)

    V_indef = quadratic_space(QQ, QQ[0 1; 1 0])
    Vf_indef = quadratic_space_with_isometry(V_indef)
    @test !is_definite(Vf_indef)
'''
    _jl_eval_testitem(code)

def test_14_is_definite_is_positive_definite_is_negative_definite_quadspacewithisom_alias_2():
    """
    method: is_positive_definite
    """
    code = r'''
    # method: is_definite
    # method: is_positive_definite
    # method: is_negative_definite
    using Oscar
    V_pd = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf_pd = quadratic_space_with_isometry(V_pd)
    @test is_definite(Vf_pd)
    @test is_positive_definite(Vf_pd)
    @test !is_negative_definite(Vf_pd)

    V_indef = quadratic_space(QQ, QQ[0 1; 1 0])
    Vf_indef = quadratic_space_with_isometry(V_indef)
    @test !is_definite(Vf_indef)
'''
    _jl_eval_testitem(code)

def test_15_is_definite_is_positive_definite_is_negative_definite_quadspacewithisom_alias_3():
    """
    method: is_negative_definite
    """
    code = r'''
    # method: is_definite
    # method: is_positive_definite
    # method: is_negative_definite
    using Oscar
    V_pd = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf_pd = quadratic_space_with_isometry(V_pd)
    @test is_definite(Vf_pd)
    @test is_positive_definite(Vf_pd)
    @test !is_negative_definite(Vf_pd)

    V_indef = quadratic_space(QQ, QQ[0 1; 1 0])
    Vf_indef = quadratic_space_with_isometry(V_indef)
    @test !is_definite(Vf_indef)
'''
    _jl_eval_testitem(code)

def test_16_characteristic_polynomial_quadspacewithisom():
    """
    method: characteristic_polynomial
    """
    code = r'''
    # method: characteristic_polynomial
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V; neg = true)
    p = characteristic_polynomial(Vf)
    @test degree(p) == 2
'''
    _jl_eval_testitem(code)

def test_17_minimal_polynomial_quadspacewithisom():
    """
    method: minimal_polynomial
    """
    code = r'''
    # method: minimal_polynomial
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf_id = quadratic_space_with_isometry(V)
    Vf_neg = quadratic_space_with_isometry(V; neg = true)
    p_id = minimal_polynomial(Vf_id)
    p_neg = minimal_polynomial(Vf_neg)
    @test degree(p_id) == 1   # identity: x - 1
    @test degree(p_neg) == 1  # negation: x + 1
'''
    _jl_eval_testitem(code)

def test_18_raise_quadspacewithisom_isometry_to_power():
    """
    method: ^
    """
    code = r'''
    # method: ^
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf_neg = quadratic_space_with_isometry(V; neg = true)
    Vf2 = Vf_neg^2
    @test order_of_isometry(Vf2) == 1
'''
    _jl_eval_testitem(code)

def test_19_direct_sum_equivariant_direct_sum_of_quadspacewithisom():
    """
    method: direct_sum
    """
    code = r'''
    # method: direct_sum
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    Wg = quadratic_space_with_isometry(V; neg = true)
    S, _, _ = direct_sum(Vf, Wg)
    @test rank(S) == 4
    @test det(S) == det(Vf) * det(Wg)
'''
    _jl_eval_testitem(code)

def test_20_rescale_det_scales_by_a_dim():
    """
    method: rescale
    """
    code = r'''
    # method: rescale
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    Wf = rescale(Vf, 3)
    @test det(Wf) == 3^dim(Vf) * det(Vf)
'''
    _jl_eval_testitem(code)

def test_21_rational_spinor_norm_returns_qqfieldelem():
    """
    method: rational_spinor_norm
    """
    code = r'''
    # method: rational_spinor_norm
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    s = rational_spinor_norm(Vf)
    @test s isa QQFieldElem
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    '^',
    'characteristic_polynomial',
    'det',
    'diagonal',
    'dim',
    'direct_sum',
    'discriminant',
    'gram_matrix',
    'is_definite',
    'is_negative_definite',
    'is_positive_definite',
    'isometry',
    'minimal_polynomial',
    'order_of_isometry',
    'quadratic_space_with_isometry',
    'rank',
    'rational_spinor_norm',
    'rescale',
    'signature_tuple',
    'space',
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
