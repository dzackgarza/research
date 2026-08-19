import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_is_isometry_identity_is_an_isometry():
    """
    method: is_isometry
    """
    code = r'''
    # method: is_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = identity_matrix(ZZ, 2)
    @test is_isometry(L, f) == true
'''
    _jl_eval_testitem(code)

def test_2_is_isometry_non_isometry_detected():
    """
    method: is_isometry
    """
    code = r'''
    # method: is_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = ZZ[2 0; 0 1]
    @test is_isometry(L, f) == false
'''
    _jl_eval_testitem(code)

def test_3_is_isometry_negation_is_an_isometry():
    """
    method: is_isometry
    """
    code = r'''
    # method: is_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = -identity_matrix(ZZ, 2)
    @test is_isometry(L, f) == true
'''
    _jl_eval_testitem(code)

def test_4_saturation_primitive_closure_in_lattice():
    """
    method: saturation
    """
    code = r'''
    # method: saturation
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    S = saturation(L, M)
    @test is_primitive(L, S) == true
'''
    _jl_eval_testitem(code)

def test_5_is_saturated_with_saturation_test_and_compute():
    """
    method: is_saturated_with_saturation
    """
    code = r'''
    # method: is_saturated_with_saturation
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    flag, S = is_saturated_with_saturation(L, M)
    @test flag == false
    @test is_primitive(L, S) == true
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'is_isometry',
    'is_saturated_with_saturation',
    'saturation',
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
