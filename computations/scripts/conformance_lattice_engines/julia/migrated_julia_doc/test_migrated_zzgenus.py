import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_genus_compute_genus_of_a2():
    """
    method: genus(L::ZZLat)
    """
    code = r'''
    # method: genus(L::ZZLat)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    @test rank(G) == 2
    @test det(G) == 3
'''
    _jl_eval_testitem(code)

def test_2_genus_from_gram_matrix():
    """
    method: genus(A::MatElem)
    """
    code = r'''
    # method: genus(A::MatElem)
    using Oscar
    G = genus(ZZ[2 1; 1 2])
    @test rank(G) == 2
'''
    _jl_eval_testitem(code)

def test_3_genus_local_genus_at_prime():
    """
    method: genus(L, p)
    """
    code = r'''
    # method: genus(L, p)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    @test prime(S) == 3
'''
    _jl_eval_testitem(code)

def test_4_representative_genus_representative_matches_rank():
    """
    method: representative
    """
    code = r'''
    # method: representative
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    R = representative(G)
    @test rank(R) == 2
'''
    _jl_eval_testitem(code)

def test_5_representatives_genus_representatives_of_a2():
    """
    method: representatives
    """
    code = r'''
    # method: representatives
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    reps = representatives(G)
    @test length(reps) >= 1
'''
    _jl_eval_testitem(code)

def test_6_mass_genus_mass_is_positive():
    """
    method: mass
    """
    code = r'''
    # method: mass
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    m = mass(G)
    @test m > 0
'''
    _jl_eval_testitem(code)

def test_7_dim_genus_dimension_equals_rank():
    """
    method: dim(gen)
    """
    code = r'''
    # method: dim(gen)
    using Oscar
    L = root_lattice(:A, 3)
    G = genus(L)
    @test dim(G) == 3
'''
    _jl_eval_testitem(code)

def test_8_signature_genus_signature():
    """
    method: signature(gen)
    """
    code = r'''
    # method: signature(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    p, n = signature(G)
    @test p == 2
    @test n == 0
'''
    _jl_eval_testitem(code)

def test_9_iseven_genus_evenness():
    """
    method: iseven(gen)
    """
    code = r'''
    # method: iseven(gen)
    using Oscar
    L = root_lattice(:E, 8)
    G = genus(L)
    @test iseven(G) == true
'''
    _jl_eval_testitem(code)

def test_10_is_definite_genus_definiteness():
    """
    method: is_definite(gen)
    """
    code = r'''
    # method: is_definite(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    @test is_definite(G) == true
'''
    _jl_eval_testitem(code)

def test_11_level_genus_level():
    """
    method: level
    """
    code = r'''
    # method: level
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    lv = level(G)
    @test lv > 0
'''
    _jl_eval_testitem(code)

def test_12_scale_genus_scale():
    """
    method: scale(gen)
    """
    code = r'''
    # method: scale(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    s = scale(G)
    @test s > 0
'''
    _jl_eval_testitem(code)

def test_13_norm_genus_norm():
    """
    method: norm(gen)
    """
    code = r'''
    # method: norm(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    n = norm(G)
    @test n > 0
'''
    _jl_eval_testitem(code)

def test_14_primes_list_of_primes_in_genus():
    """
    method: primes
    """
    code = r'''
    # method: primes
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    ps = primes(G)
    @test 3 in ps  # A2 has det 3
'''
    _jl_eval_testitem(code)

def test_15_is_integral_genus_integrality():
    """
    method: is_integral(gen)
    """
    code = r'''
    # method: is_integral(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    @test is_integral(G) == true
'''
    _jl_eval_testitem(code)

def test_16_local_symbol_retrieve_local_genus():
    """
    method: local_symbol
    """
    code = r'''
    # method: local_symbol
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    S = local_symbol(G, 3)
    @test prime(S) == 3
'''
    _jl_eval_testitem(code)

def test_17_quadratic_space_genus_quadratic_space():
    """
    method: quadratic_space(gen)
    """
    code = r'''
    # method: quadratic_space(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    V = quadratic_space(G)
    @test rank(V) == 2
'''
    _jl_eval_testitem(code)

def test_18_rational_representative_genus_rational_form():
    """
    method: rational_representative
    """
    code = r'''
    # method: rational_representative
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    R = rational_representative(G)
    @test rank(R) == 2
'''
    _jl_eval_testitem(code)

def test_19_rescale_genus_rescaling():
    """
    method: rescale(gen, a)
    """
    code = r'''
    # method: rescale(gen, a)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    G2 = rescale(G, 2)
    @test det(G2) == det(G) * 2^rank(G)
'''
    _jl_eval_testitem(code)

def test_20_direct_sum_genus_direct_sum():
    """
    method: direct_sum(G1::ZZGenus, G2::ZZGenus)
    """
    code = r'''
    # method: direct_sum(G1::ZZGenus, G2::ZZGenus)
    using Oscar
    L1 = root_lattice(:A, 1)
    L2 = root_lattice(:A, 1)
    G1 = genus(L1)
    G2 = genus(L2)
    G = direct_sum(G1, G2)
    @test rank(G) == 2
'''
    _jl_eval_testitem(code)

def test_21_represents_genus_representation():
    """
    method: represents
    """
    code = r'''
    # method: represents
    using Oscar
    L1 = root_lattice(:A, 2)
    L2 = root_lattice(:A, 1)
    G1 = genus(L1)
    G2 = genus(L2)
    @test represents(G1, G2) == true
'''
    _jl_eval_testitem(code)

def test_22_integer_genera_enumerate_genus_symbols():
    """
    method: integer_genera
    """
    code = r'''
    # method: integer_genera
    using Oscar
    gs = integer_genera((2, 0), 3)
    @test length(gs) >= 1
'''
    _jl_eval_testitem(code)

def test_23_discriminant_group_l_vee_l_as_torquadmodule():
    """
    method: discriminant_group
    """
    code = r'''
    # method: discriminant_group
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    @test order(T) == 3
'''
    _jl_eval_testitem(code)

def test_24_genus_representatives_all_classes_in_genus():
    """
    method: genus_representatives
    """
    code = r'''
    # method: genus_representatives
    using Oscar
    L = root_lattice(:A, 2)
    reps = genus_representatives(L)
    @test length(reps) >= 1
'''
    _jl_eval_testitem(code)

def test_25_prime_local_genus_prime():
    """
    method: prime(S)
    """
    code = r'''
    # method: prime(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    @test prime(S) == 3
'''
    _jl_eval_testitem(code)

def test_26_iseven_local_genus_evenness():
    """
    method: iseven(S)
    """
    code = r'''
    # method: iseven(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    @test iseven(S) isa Bool
'''
    _jl_eval_testitem(code)

def test_27_hasse_invariant_local_genus_hasse_invariant():
    """
    method: hasse_invariant(S)
    """
    code = r'''
    # method: hasse_invariant(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    h = hasse_invariant(S)
    @test h in [1, -1]
'''
    _jl_eval_testitem(code)

def test_28_det_local_genus_determinant():
    """
    method: det(S)
    """
    code = r'''
    # method: det(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    @test det(S) != 0
'''
    _jl_eval_testitem(code)

def test_29_rank_local_genus_rank():
    """
    method: rank(S)
    """
    code = r'''
    # method: rank(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    @test rank(S) == 2
'''
    _jl_eval_testitem(code)

def test_30_excess_local_genus_excess():
    """
    method: excess(S)
    """
    code = r'''
    # method: excess(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    e = excess(S)
    @test e isa Integer
'''
    _jl_eval_testitem(code)

def test_31_signature_local_genus_signature():
    """
    method: signature(S)
    """
    code = r'''
    # method: signature(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    sig = signature(S)
    @test sig isa Integer
'''
    _jl_eval_testitem(code)

def test_32_oddity_local_genus_2_adic_oddity():
    """
    method: oddity(S)
    """
    code = r'''
    # method: oddity(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    o = oddity(S)
    @test o isa Integer
'''
    _jl_eval_testitem(code)

def test_33_representative_local_genus_representative():
    """
    method: representative(S)
    """
    code = r'''
    # method: representative(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    R = representative(S)
    @test rank(R) == 2
'''
    _jl_eval_testitem(code)

def test_34_gram_matrix_local_genus_gram_matrix():
    """
    method: gram_matrix(S)
    """
    code = r'''
    # method: gram_matrix(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    G = gram_matrix(S)
    @test nrows(G) == 2
'''
    _jl_eval_testitem(code)

def test_35_rescale_local_genus_rescaling():
    """
    method: rescale(S, a)
    """
    code = r'''
    # method: rescale(S, a)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    S2 = rescale(S, 2)
    @test rank(S2) == rank(S)
'''
    _jl_eval_testitem(code)

def test_36_direct_sum_local_genus_direct_sum():
    """
    method: direct_sum(S1, S2)
    """
    code = r'''
    # method: direct_sum(S1, S2)
    using Oscar
    L = root_lattice(:A, 1)
    S1 = genus(L, 2)
    S2 = genus(L, 2)
    S = direct_sum(S1, S2)
    @test rank(S) == 2
'''
    _jl_eval_testitem(code)

def test_37_symbol_local_genus_jordan_block_invariants():
    """
    method: symbol(S, scale)
    """
    code = r'''
    # method: symbol(S, scale)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    # symbol(S, i) returns the i-th Jordan block invariants
    sym = symbol(S, 0)
    @test length(sym) >= 1
'''
    _jl_eval_testitem(code)


def test_38_dim_local_genus_dimension():
    """
    method: dim(S)
    """
    code = r'''
    # method: dim(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    @test dim(S) == 2
'''
    _jl_eval_testitem(code)


def test_39_scale_local_genus_scale():
    """
    method: scale(S)
    """
    code = r'''
    # method: scale(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    s = scale(S)
    @test s >= 0
'''
    _jl_eval_testitem(code)


def test_40_norm_local_genus_norm():
    """
    method: norm(S)
    """
    code = r'''
    # method: norm(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    n = norm(S)
    @test n >= 0
'''
    _jl_eval_testitem(code)


def test_41_level_local_genus_level():
    """
    method: level(S)
    """
    code = r'''
    # method: level(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    lv = level(S)
    @test lv > 0
'''
    _jl_eval_testitem(code)


def test_42_represents_local_genus_representation():
    """
    method: represents(S1, S2)
    """
    code = r'''
    # method: represents(S1, S2)
    using Oscar
    L1 = root_lattice(:A, 2)
    L2 = root_lattice(:A, 1)
    S1 = genus(L1, 2)
    S2 = genus(L2, 2)
    @test represents(S1, S2) == true
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'det(S)',
    'dim(S)',
    'dim(gen)',
    'direct_sum(G1::ZZGenus, G2::ZZGenus)',
    'direct_sum(S1, S2)',
    'discriminant_group',
    'excess(S)',
    'genus(A::MatElem)',
    'genus(L, p)',
    'genus(L::ZZLat)',
    'genus_representatives',
    'gram_matrix(S)',
    'hasse_invariant(S)',
    'integer_genera',
    'is_definite(gen)',
    'is_integral(gen)',
    'iseven(S)',
    'iseven(gen)',
    'level',
    'level(S)',
    'local_symbol',
    'mass',
    'norm(S)',
    'norm(gen)',
    'oddity(S)',
    'prime(S)',
    'primes',
    'quadratic_space(gen)',
    'rank(S)',
    'rational_representative',
    'representative',
    'representative(S)',
    'representatives',
    'represents',
    'represents(S1, S2)',
    'rescale(S, a)',
    'rescale(gen, a)',
    'scale(S)',
    'scale(gen)',
    'signature(S)',
    'signature(gen)',
    'symbol(S, scale)',
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
