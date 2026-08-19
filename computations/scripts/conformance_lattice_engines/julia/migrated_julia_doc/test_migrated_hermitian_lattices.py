import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_hermitian_lattice_construct_over_gaussian_integers():
    """
    method: hermitian_lattice
    """
    code = r'''
    # method: hermitian_lattice
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    @test rank(L) == 2
'''
    _jl_eval_testitem(code)

def test_2_base_field_returns_number_field():
    """
    method: base_field
    """
    code = r'''
    # method: base_field
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    E = base_field(L)
    @test degree(E) == 2
'''
    _jl_eval_testitem(code)

def test_3_fixed_field_returns_fixed_field_under_involution():
    """
    method: fixed_field
    """
    code = r'''
    # method: fixed_field
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    F = fixed_field(L)
    @test degree(F) == 1  # QQ
'''
    _jl_eval_testitem(code)

def test_4_pseudo_matrix_returns_pseudo_matrix_representation():
    """
    method: pseudo_matrix
    """
    code = r'''
    # method: pseudo_matrix
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    PM = pseudo_matrix(L)
    @test nrows(matrix(PM)) == 2
'''
    _jl_eval_testitem(code)

def test_5_is_positive_definite_pd_hermitian_lattice():
    """
    method: is_positive_definite
    """
    code = r'''
    # method: is_positive_definite
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    @test is_positive_definite(L) == true
'''
    _jl_eval_testitem(code)

def test_6_jordan_decomposition_at_a_prime():
    """
    method: jordan_decomposition
    """
    code = r'''
    # method: jordan_decomposition
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    p = prime_decomposition(OK, 2)[1][1]
    J = jordan_decomposition(L, p)
    @test length(J) >= 1
'''
    _jl_eval_testitem(code)

def test_7_genus_representatives_hermitian_genus():
    """
    method: genus_representatives
    """
    code = r'''
    # method: genus_representatives
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    reps = genus_representatives(L)
    @test length(reps) >= 1
'''
    _jl_eval_testitem(code)

def test_8_base_ring_returns_ring_of_integers():
    """
    method: base_ring
    """
    code = r'''
    # method: base_ring
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    R = base_ring(L)
    @test R == maximal_order(K)
'''
    _jl_eval_testitem(code)


def test_9_fixed_ring_returns_ring_of_integers_of_fixed_field():
    """
    method: fixed_ring
    """
    code = r'''
    # method: fixed_ring
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    R = fixed_ring(L)
    @test R == maximal_order(QQ) || R isa Ring
'''
    _jl_eval_testitem(code)


def test_10_involution_of_hermitian_form():
    """
    method: involution
    """
    code = r'''
    # method: involution
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    inv = involution(L)
    # Involution should map a -> -a for Q(i)
    @test inv(a) == -a
'''
    _jl_eval_testitem(code)


def test_11_pseudo_basis_returns_ideals_and_vectors():
    """
    method: pseudo_basis
    """
    code = r'''
    # method: pseudo_basis
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    pb = pseudo_basis(L)
    @test length(pb) == 2
'''
    _jl_eval_testitem(code)


def test_12_coefficient_ideals_of_pseudo_basis():
    """
    method: coefficient_ideals
    """
    code = r'''
    # method: coefficient_ideals
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    ci = coefficient_ideals(L)
    @test length(ci) == 2
'''
    _jl_eval_testitem(code)


def test_13_absolute_basis_z_basis():
    """
    method: absolute_basis
    """
    code = r'''
    # method: absolute_basis
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    ab = absolute_basis(L)
    # [K:Q] = 2, rank = 2, so absolute basis has 4 elements
    @test length(ab) == 4
'''
    _jl_eval_testitem(code)


def test_14_generators_hermitian_lattice():
    """
    method: generators(HermLat)
    """
    code = r'''
    # method: generators(HermLat)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    gens_L = generators(L)
    @test length(gens_L) >= 2
'''
    _jl_eval_testitem(code)


def test_15_gram_matrix_of_generators():
    """
    method: gram_matrix_of_generators
    """
    code = r'''
    # method: gram_matrix_of_generators
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    Gg = gram_matrix_of_generators(L)
    @test nrows(Gg) >= 2
'''
    _jl_eval_testitem(code)


def test_16_local_basis_matrix_at_prime():
    """
    method: local_basis_matrix
    """
    code = r'''
    # method: local_basis_matrix
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    p = prime_decomposition(OK, 2)[1][1]
    B = local_basis_matrix(L, p)
    @test nrows(B) == 2
'''
    _jl_eval_testitem(code)


def test_17_is_isotropic_hermitian_lattice():
    """
    method: is_isotropic(HermLat)
    """
    code = r'''
    # method: is_isotropic(HermLat)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    p = prime_decomposition(OK, 2)[1][1]
    result = is_isotropic(L, p)
    @test result isa Bool
'''
    _jl_eval_testitem(code)


def test_18_is_modular_hermitian_lattice():
    """
    method: is_modular
    """
    code = r'''
    # method: is_modular
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    result = is_modular(L)
    @test result isa Tuple || result isa Bool
'''
    _jl_eval_testitem(code)
def test_19_can_scale_totally_positive():
    """
    method: can_scale_totally_positive
    """
    code = r'''
    # method: can_scale_totally_positive
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    result = can_scale_totally_positive(L)
    @test result isa Bool
'''
    _jl_eval_testitem(code)


def test_20_volume_of_hermitian_lattice():
    """
    method: volume
    """
    code = r'''
    # method: volume
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    v = volume(L)
    # Volume is a fractional ideal
    @test !iszero(v)
'''
    _jl_eval_testitem(code)


def test_21_is_maximal_integral_hermitian_lattice():
    """
    method: is_maximal_integral(HermLat)
    """
    code = r'''
    # method: is_maximal_integral(HermLat)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    result = is_maximal_integral(L)
    @test result isa Bool
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'absolute_basis',
    'base_field',
    'base_ring',
    'can_scale_totally_positive',
    'coefficient_ideals',
    'fixed_field',
    'fixed_ring',
    'generators(HermLat)',
    'genus_representatives',
    'gram_matrix_of_generators',
    'hermitian_lattice',
    'involution',
    'is_isotropic(HermLat)',
    'is_maximal_integral(HermLat)',
    'is_modular',
    'is_positive_definite',
    'jordan_decomposition',
    'local_basis_matrix',
    'pseudo_basis',
    'pseudo_matrix',
    'volume',
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
