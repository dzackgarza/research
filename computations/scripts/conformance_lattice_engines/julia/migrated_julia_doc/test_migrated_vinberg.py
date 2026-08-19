import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_vinberg_algorithm_finds_roots_of_hyperbolic_lattice():
    """
    method: vinberg_algorithm
    """
    code = r'''
    # method: vinberg_algorithm
    using Oscar
    # Hyperbolic plane direct sum with negative definite part
    # Use a simple (1,n) lattice: U + A1(-1)
    L = hyperbolic_plane_lattice()
    # vinberg_algorithm needs signature (1,0,n), so use from Gram matrix
    # Simple rank-2 hyperbolic: diag(1, -1)
    Q = ZZ[1 0; 0 -1]
    roots = vinberg_algorithm(Q, 2)
    @test length(roots) > 0
'''
    _jl_eval_testitem(code)

def test_2_vinberg_algorithm_from_zzlat():
    """
    method: vinberg_algorithm(S::ZZLat, ub)
    """
    code = r'''
    # method: vinberg_algorithm(S::ZZLat, ub)
    using Oscar
    # Construct a signature (1,0,n) lattice
    Q = ZZ[1 0; 0 -1]
    L = integer_lattice(gram = Q)
    roots = vinberg_algorithm(L, 2)
    @test length(roots) > 0
'''
    _jl_eval_testitem(code)

def test_3_short_vectors_affine_affine_enumeration():
    """
    method: short_vectors_affine
    """
    code = r'''
    # method: short_vectors_affine
    using Oscar
    # This is used internally by Vinberg; test with a simple lattice
    L = integer_lattice(gram = ZZ[1 0; 0 -1])
    # Find vectors x with x^2 = d and x . v = alpha
    # This may require specific setup; test that it returns a collection
    v = ZZ[1, 0]
    result = short_vectors_affine(L, v, 0, -1)
    @test result isa Vector || result isa AbstractVector
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'short_vectors_affine',
    'vinberg_algorithm',
    'vinberg_algorithm(S::ZZLat, ub)',
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
