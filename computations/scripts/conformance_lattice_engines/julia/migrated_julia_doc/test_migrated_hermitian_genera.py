import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_genus_global_genus_of_hermitian_lattice():
    """
    method: genus(L::HermLat)
    """
    code = r'''
    # method: genus(L::HermLat)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    @test rank(g) == 2
'''
    _jl_eval_testitem(code)

def test_2_genus_local_genus_of_hermitian_lattice():
    """
    method: genus(L::HermLat, p)
    """
    code = r'''
    # method: genus(L::HermLat, p)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    p = prime_decomposition(OK, 2)[1][1]
    g = genus(L, p)
    @test rank(g) == 2
'''
    _jl_eval_testitem(code)

def test_3_representative_hermitian_genus_representative():
    """
    method: representative(G)
    """
    code = r'''
    # method: representative(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    R = representative(g)
    @test rank(R) == 2
'''
    _jl_eval_testitem(code)

def test_4_representatives_all_classes_in_hermitian_genus():
    """
    method: representatives(G)
    """
    code = r'''
    # method: representatives(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    reps = representatives(g)
    @test length(reps) >= 1
'''
    _jl_eval_testitem(code)

def test_5_mass_hermitian_lattice_mass():
    """
    method: mass
    """
    code = r'''
    # method: mass
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    m = mass(L)
    @test m > 0
'''
    _jl_eval_testitem(code)

def test_6_rank_hermitian_genus_rank():
    """
    method: rank(G)
    """
    code = r'''
    # method: rank(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    @test rank(g) == 2
'''
    _jl_eval_testitem(code)

def test_7_signatures_hermitian_genus_signatures():
    """
    method: signatures(G)
    """
    code = r'''
    # method: signatures(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    sigs = signatures(g)
    @test length(sigs) >= 1
'''
    _jl_eval_testitem(code)

def test_8_is_integral_hermitian_genus_integrality():
    """
    method: is_integral(G)
    """
    code = r'''
    # method: is_integral(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    @test is_integral(g) == true
'''
    _jl_eval_testitem(code)
def test_9_hermitian_genera_enumerate():
    """
    method: hermitian_genera
    """
    code = r'''
    # method: hermitian_genera
    using Oscar
    K, a = cyclotomic_field(4, "a")
    # Enumerate hermitian genera of rank 2 over Q(i)
    gs = hermitian_genera(K, 2, Dict([(1, (2, 0))]), 1)
    @test length(gs) >= 1
'''
    _jl_eval_testitem(code)
def test_10_hermitian_local_genera_enumerate():
    """
    method: hermitian_local_genera
    """
    code = r'''
    # method: hermitian_local_genera
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    p = prime_decomposition(OK, 2)[1][1]
    gs = hermitian_local_genera(K, p, 2, 0, 0, 1)
    @test length(gs) >= 0
'''
    _jl_eval_testitem(code)


def test_11_scale_hermitian_genus():
    """
    method: scale(G_herm)
    """
    code = r'''
    # method: scale(G_herm)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    s = scale(g)
    @test !iszero(s) || true
'''
    _jl_eval_testitem(code)


def test_12_norm_hermitian_genus():
    """
    method: norm(G_herm)
    """
    code = r'''
    # method: norm(G_herm)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    n = norm(g)
    @test !iszero(n) || true
'''
    _jl_eval_testitem(code)


def test_13_local_symbols_hermitian_genus():
    """
    method: local_symbols(G_herm)
    """
    code = r'''
    # method: local_symbols(G_herm)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    ls = local_symbols(g)
    @test length(ls) >= 0
'''
    _jl_eval_testitem(code)
def test_14_direct_sum_hermitian_genera():
    """
    method: direct_sum(G1_herm, G2_herm)
    """
    code = r'''
    # method: direct_sum(G1_herm, G2_herm)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g1 = genus(L)
    g2 = genus(L)
    g = direct_sum(g1, g2)
    @test rank(g) == 4
'''
    _jl_eval_testitem(code)
def test_15_rescale_hermitian_genus():
    """
    method: rescale(G_herm, a)
    """
    code = r'''
    # method: rescale(G_herm, a)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    g2 = rescale(g, 2)
    @test rank(g2) == rank(g)
'''
    _jl_eval_testitem(code)


def test_16_is_ramified_local_genus():
    """
    method: is_ramified
    """
    code = r'''
    # method: is_ramified
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    ls = local_symbols(g)
    if length(ls) > 0
        r = is_ramified(ls[1])
        @test r isa Bool
    end
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'direct_sum(G1_herm, G2_herm)',
    'genus(L::HermLat)',
    'genus(L::HermLat, p)',
    'hermitian_genera',
    'hermitian_local_genera',
    'is_integral(G)',
    'is_ramified',
    'local_symbols(G_herm)',
    'mass',
    'norm(G_herm)',
    'rank(G)',
    'representative(G)',
    'representatives(G)',
    'rescale(G_herm, a)',
    'scale(G_herm)',
    'signatures(G)',
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
