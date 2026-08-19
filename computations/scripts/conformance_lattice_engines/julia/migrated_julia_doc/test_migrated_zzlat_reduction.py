import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_lll_reduces_basis_of_positive_definite_lattice():
    """
    method: lll
    """
    code = r'''
    # method: lll
    using Oscar
    # Start with a non-reduced basis
    L = integer_lattice(gram = ZZ[4 2; 2 4])
    M = lll(L)
    @test rank(M) == rank(L)
    @test det(M) == det(L)
'''
    _jl_eval_testitem(code)

def test_2_lll_preserves_lattice_isometry_class():
    """
    method: lll
    """
    code = r'''
    # method: lll
    using Oscar
    L = root_lattice(:A, 3)
    M = lll(L)
    @test rank(M) == 3
    # LLL preserves the lattice, only changes basis
    @test det(M) == det(L)
'''
    _jl_eval_testitem(code)

def test_3_lll_works_on_indefinite_lattice():
    """
    method: lll
    """
    code = r'''
    # method: lll
    using Oscar
    L = hyperbolic_plane_lattice()
    M = lll(L)
    @test rank(M) == 2
    @test det(M) == det(L)
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'lll',
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
