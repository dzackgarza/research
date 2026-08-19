import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_gram_matrix_returns_correct_matrix():
    """
    method: gram_matrix
    """
    code = r'''
    # method: gram_matrix
    using Oscar
    G = ZZ[2 1; 1 2]
    L = integer_lattice(gram = G)
    @test gram_matrix(L) == G
'''
    _jl_eval_testitem(code)

def test_2_basis_matrix_identity_for_standard_construction():
    """
    method: basis_matrix
    """
    code = r'''
    # method: basis_matrix
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 2])
    B = basis_matrix(L)
    @test nrows(B) == 2
    @test ncols(B) == 2
'''
    _jl_eval_testitem(code)

def test_3_ambient_space_returns_quadratic_space():
    """
    method: ambient_space
    """
    code = r'''
    # method: ambient_space
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    V = ambient_space(L)
    @test rank(V) == 2
'''
    _jl_eval_testitem(code)

def test_4_rational_span_returns_quadratic_space_over_qq():
    """
    method: rational_span
    """
    code = r'''
    # method: rational_span
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    V = rational_span(L)
    @test rank(V) == 2
'''
    _jl_eval_testitem(code)

def test_5_rank_returns_lattice_rank():
    """
    method: rank
    """
    code = r'''
    # method: rank
    using Oscar
    L = integer_lattice(gram = ZZ[2 1 0; 1 2 0; 0 0 4])
    @test rank(L) == 3
'''
    _jl_eval_testitem(code)

def test_6_degree_ambient_dimension():
    """
    method: degree
    """
    code = r'''
    # method: degree
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    @test degree(L) >= rank(L)
'''
    _jl_eval_testitem(code)

def test_7_signature_tuple_positive_definite_a2():
    """
    method: signature_tuple
    """
    code = r'''
    # method: signature_tuple
    using Oscar
    L = root_lattice(:A, 2)
    p, n, z = signature_tuple(L)
    @test p == 2
    @test n == 0
'''
    _jl_eval_testitem(code)

def test_8_signature_tuple_indefinite_hyperbolic_plane():
    """
    method: signature_tuple
    """
    code = r'''
    # method: signature_tuple
    using Oscar
    L = hyperbolic_plane_lattice()
    @test signature_tuple(L) == (1, 1, 0)
'''
    _jl_eval_testitem(code)

def test_9_det_determinant_of_gram_matrix():
    """
    method: det
    """
    code = r'''
    # method: det
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    @test det(L) == 3
'''
    _jl_eval_testitem(code)

def test_10_discriminant_lattice_discriminant():
    """
    method: discriminant
    """
    code = r'''
    # method: discriminant
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    d = discriminant(L)
    @test d == (-1)^rank(L) * det(L)
'''
    _jl_eval_testitem(code)

def test_11_scale_scale_ideal():
    """
    method: scale
    """
    code = r'''
    # method: scale
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 4])
    s = scale(L)
    @test s == 2
'''
    _jl_eval_testitem(code)

def test_12_norm_norm_ideal():
    """
    method: norm
    """
    code = r'''
    # method: norm
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 4])
    n = norm(L)
    @test n == 2
'''
    _jl_eval_testitem(code)

def test_13_is_positive_definite_true_for_a2():
    """
    method: is_positive_definite
    """
    code = r'''
    # method: is_positive_definite
    using Oscar
    L = root_lattice(:A, 2)
    @test is_positive_definite(L) == true
'''
    _jl_eval_testitem(code)

def test_14_is_negative_definite_false_for_a2():
    """
    method: is_negative_definite
    """
    code = r'''
    # method: is_negative_definite
    using Oscar
    L = root_lattice(:A, 2)
    @test is_negative_definite(L) == false
'''
    _jl_eval_testitem(code)

def test_15_is_definite_true_for_positive_definite_lattice():
    """
    method: is_definite
    """
    code = r'''
    # method: is_definite
    using Oscar
    L = root_lattice(:A, 2)
    @test is_definite(L) == true
'''
    _jl_eval_testitem(code)

def test_16_is_definite_false_for_indefinite_lattice():
    """
    method: is_definite
    """
    code = r'''
    # method: is_definite
    using Oscar
    L = hyperbolic_plane_lattice()
    @test is_definite(L) == false
'''
    _jl_eval_testitem(code)

def test_17_is_even_true_for_e8():
    """
    method: is_even
    """
    code = r'''
    # method: is_even
    using Oscar
    L = root_lattice(:E, 8)
    @test is_even(L) == true
'''
    _jl_eval_testitem(code)

def test_18_is_integral_true_for_integer_lattice():
    """
    method: is_integral
    """
    code = r'''
    # method: is_integral
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    @test is_integral(L) == true
'''
    _jl_eval_testitem(code)

def test_19_is_unimodular_true_for_e8():
    """
    method: is_unimodular
    """
    code = r'''
    # method: is_unimodular
    using Oscar
    L = root_lattice(:E, 8)
    @test is_unimodular(L) == true
'''
    _jl_eval_testitem(code)

def test_20_is_unimodular_false_for_a2():
    """
    method: is_unimodular
    """
    code = r'''
    # method: is_unimodular
    using Oscar
    L = root_lattice(:A, 2)
    @test is_unimodular(L) == false
'''
    _jl_eval_testitem(code)

def test_21_is_primary_a2_is_3_primary():
    """
    method: is_primary
    """
    code = r'''
    # method: is_primary
    using Oscar
    L = root_lattice(:A, 2)
    @test is_primary(L, 3) == true
'''
    _jl_eval_testitem(code)

def test_22_is_primary_with_prime_returns_true_p_for_primary_lattice():
    """
    method: is_primary_with_prime
    """
    code = r'''
    # method: is_primary_with_prime
    using Oscar
    L = root_lattice(:A, 2)
    flag, p = is_primary_with_prime(L)
    @test flag == true
    @test p == 3
'''
    _jl_eval_testitem(code)

def test_23_is_elementary_a1_is_2_elementary():
    """
    method: is_elementary
    """
    code = r'''
    # method: is_elementary
    using Oscar
    L = root_lattice(:A, 1)
    @test is_elementary(L, 2) == true
'''
    _jl_eval_testitem(code)

def test_24_is_elementary_with_prime_returns_true_p():
    """
    method: is_elementary_with_prime
    """
    code = r'''
    # method: is_elementary_with_prime
    using Oscar
    L = root_lattice(:A, 1)
    flag, p = is_elementary_with_prime(L)
    @test flag == true
    @test p == 2
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'ambient_space',
    'basis_matrix',
    'degree',
    'det',
    'discriminant',
    'gram_matrix',
    'is_definite',
    'is_elementary',
    'is_elementary_with_prime',
    'is_even',
    'is_integral',
    'is_negative_definite',
    'is_positive_definite',
    'is_primary',
    'is_primary_with_prime',
    'is_unimodular',
    'norm',
    'rank',
    'rational_span',
    'scale',
    'signature_tuple',
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
