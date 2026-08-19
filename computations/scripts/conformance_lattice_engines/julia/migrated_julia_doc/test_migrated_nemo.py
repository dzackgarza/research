import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_lll_lll_reduction_of_zzmatrix():
    """
    method: lll(B::ZZMatrix)
    """
    code = r'''
    # method: lll(B::ZZMatrix)
    using Oscar
    B = ZZ[1 0; 1 2]
    L = lll(B)
    @test nrows(L) == 2
    @test ncols(L) == 2
    # LLL-reduced first row should be shorter
'''
    _jl_eval_testitem(code)

def test_2_lll_with_transform_returns_reduced_basis_and_transform():
    """
    method: lll_with_transform
    """
    code = r'''
    # method: lll_with_transform
    using Oscar
    B = ZZ[1 0; 1 2]
    L, T = lll_with_transform(B)
    @test L == T * B
'''
    _jl_eval_testitem(code)

def test_3_lll_gram_lll_on_gram_matrix():
    """
    method: lll_gram
    """
    code = r'''
    # method: lll_gram
    using Oscar
    G = ZZ[4 2; 2 4]
    L = lll_gram(G)
    @test nrows(L) == 2
'''
    _jl_eval_testitem(code)

def test_4_lll_gram_with_transform_gram_lll_transform():
    """
    method: lll_gram_with_transform
    """
    code = r'''
    # method: lll_gram_with_transform
    using Oscar
    G = ZZ[4 2; 2 4]
    L, T = lll_gram_with_transform(G)
    @test L == T * G * transpose(T)
'''
    _jl_eval_testitem(code)

def test_5_hnf_hermite_normal_form():
    """
    method: hnf
    """
    code = r'''
    # method: hnf
    using Oscar
    X = ZZ[2 3; 4 5]
    H = hnf(X)
    @test nrows(H) == 2
    # HNF is upper triangular
    @test H[2, 1] == 0
'''
    _jl_eval_testitem(code)

def test_6_hnf_with_transform_hnf_transformation_matrix():
    """
    method: hnf_with_transform
    """
    code = r'''
    # method: hnf_with_transform
    using Oscar
    X = ZZ[2 3; 4 5]
    H, U = hnf_with_transform(X)
    @test H == U * X
'''
    _jl_eval_testitem(code)

def test_7_snf_smith_normal_form():
    """
    method: snf
    """
    code = r'''
    # method: snf
    using Oscar
    X = ZZ[2 4; 6 8]
    D = snf(X)
    @test nrows(D) == 2
    # SNF is diagonal
    @test D[1, 2] == 0
    @test D[2, 1] == 0
    # Invariant factors divide
    @test mod(D[2, 2], D[1, 1]) == 0
'''
    _jl_eval_testitem(code)

def test_8_snf_with_transform_snf_transformation_matrices():
    """
    method: snf_with_transform
    """
    code = r'''
    # method: snf_with_transform
    using Oscar
    X = ZZ[2 4; 6 8]
    D, U, V = snf_with_transform(X)
    @test D == U * X * V
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'hnf',
    'hnf_with_transform',
    'lll(B::ZZMatrix)',
    'lll_gram',
    'lll_gram_with_transform',
    'lll_with_transform',
    'snf',
    'snf_with_transform',
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
