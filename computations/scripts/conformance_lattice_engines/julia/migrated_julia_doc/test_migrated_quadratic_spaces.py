import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_hermitian_space_construct_from_gram():
    """
    method: hermitian_space
    """
    code = r'''
    # method: hermitian_space
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    V = hermitian_space(K, G)
    @test rank(V) == 2
    @test is_regular(V) == true
'''
    _jl_eval_testitem(code)


def test_2_diagonal_with_transform_returns_diagonal_and_matrix():
    """
    method: diagonal_with_transform
    """
    code = r'''
    # method: diagonal_with_transform
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    D, T = diagonal_with_transform(V)
    # T diagonalizes V: T * G * T^t should be diagonal
    @test length(D) == 2
    # All diagonal entries should be nonzero for non-degenerate form
    for d in D
        @test d != 0
    end
'''
    _jl_eval_testitem(code)


def test_3_orthogonal_basis_returns_orthogonal_vectors():
    """
    method: orthogonal_basis
    """
    code = r'''
    # method: orthogonal_basis
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    B = orthogonal_basis(V)
    @test nrows(B) == 2
    # Gram on orthogonal basis should be diagonal
    G = gram_matrix(V)
    GG = B * G * transpose(B)
    # Off-diagonal entries should be zero
    @test GG[1, 2] == 0
    @test GG[2, 1] == 0
'''
    _jl_eval_testitem(code)


def test_4_is_regular_nondegenerate_space():
    """
    method: is_regular
    """
    code = r'''
    # method: is_regular
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    @test is_regular(V) == true
'''
    _jl_eval_testitem(code)


def test_5_is_quadratic_type_check():
    """
    method: is_quadratic
    """
    code = r'''
    # method: is_quadratic
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    @test is_quadratic(V) == true
'''
    _jl_eval_testitem(code)


def test_6_invariants_returns_rational_invariants():
    """
    method: invariants
    """
    code = r'''
    # method: invariants
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    inv = invariants(V)
    # invariants returns (dim, det, finite_places, negative_places)
    @test inv[1] == 2  # dimension
    @test inv[2] == 3  # det = 2*2 - 1*1 = 3
'''
    _jl_eval_testitem(code)


def test_7_is_locally_represented_by_a1_by_a2():
    """
    method: is_locally_represented_by
    """
    code = r'''
    # method: is_locally_represented_by
    using Oscar
    U = quadratic_space(QQ, QQ[2;;])
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    # U (rank 1) should be locally represented by V (rank 2) at prime 2
    @test is_locally_represented_by(U, V, 2) == true
'''
    _jl_eval_testitem(code)


def test_8_is_represented_by_rank_1_in_rank_2():
    """
    method: is_represented_by
    """
    code = r'''
    # method: is_represented_by
    using Oscar
    U = quadratic_space(QQ, QQ[2;;])
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    @test is_represented_by(U, V) == true
'''
    _jl_eval_testitem(code)


def test_9_inner_product_on_space():
    """
    method: inner_product(V, v, w)
    """
    code = r'''
    # method: inner_product(V, v, w)
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    v = QQ[1, 0]
    w = QQ[0, 1]
    ip = inner_product(V, v, w)
    # b(e1, e2) = G[1,2] = 1
    @test ip == 1
'''
    _jl_eval_testitem(code)


def test_10_orthogonal_complement_on_space():
    """
    method: orthogonal_complement(V, M)
    """
    code = r'''
    # method: orthogonal_complement(V, M)
    using Oscar
    V = quadratic_space(QQ, QQ[1 0; 0 1])
    M = matrix(QQ, 1, 2, [1, 0])  # span of e1
    OC = orthogonal_complement(V, M)
    @test nrows(OC) == 1
    # OC should be span of e2 (orthogonal to e1 in standard inner product)
'''
    _jl_eval_testitem(code)


def test_11_orthogonal_projection_on_space():
    """
    method: orthogonal_projection
    """
    code = r'''
    # method: orthogonal_projection
    using Oscar
    V = quadratic_space(QQ, QQ[1 0; 0 1])
    M = matrix(QQ, 1, 2, [1, 0])  # span of e1
    P = orthogonal_projection(V, M)
    @test nrows(P) == 2
    @test ncols(P) == 2
'''
    _jl_eval_testitem(code)


def test_12_is_isotropic_at_prime():
    """
    method: is_isotropic(V, p)
    """
    code = r'''
    # method: is_isotropic(V, p)
    using Oscar
    # Hyperbolic plane is isotropic everywhere
    V = quadratic_space(QQ, QQ[0 1; 1 0])
    @test is_isotropic(V, 2) == true
    @test is_isotropic(V, 3) == true
'''
    _jl_eval_testitem(code)
def test_13_is_locally_hyperbolic_hermitian_space():
    """
    method: is_locally_hyperbolic
    """
    code = r'''
    # method: is_locally_hyperbolic
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    # Hyperbolic hermitian space: Gram = [[0,1],[1,0]]
    G = matrix(K, 2, 2, [0, 1, 1, 0])
    V = hermitian_space(K, G)
    p = prime_decomposition(OK, 2)[1][1]
    @test is_locally_hyperbolic(V, p) isa Bool
'''
    _jl_eval_testitem(code)
def test_14_restrict_scalars():
    """
    method: restrict_scalars
    """
    code = r'''
    # method: restrict_scalars
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 1, 1, [1])
    V = hermitian_space(K, G)
    W, f = restrict_scalars(V, QQ)
    @test rank(W) == 2  # [K:QQ] * rank(V) = 2 * 1 = 2
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'diagonal_with_transform',
    'hermitian_space',
    'inner_product(V, v, w)',
    'invariants',
    'is_isotropic(V, p)',
    'is_locally_hyperbolic',
    'is_locally_represented_by',
    'is_quadratic',
    'is_regular',
    'is_represented_by',
    'orthogonal_basis',
    'orthogonal_complement(V, M)',
    'orthogonal_projection',
    'restrict_scalars',
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
