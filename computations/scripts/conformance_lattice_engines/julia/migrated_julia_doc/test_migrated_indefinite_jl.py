import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_indef_form_test_equivalence_two_equivalent_forms():
    """
    method: INDEF_FORM_TestEquivalence
    """
    # Indefinite.jl is not installed in the Julia env yet.
    # Two copies of the hyperbolic plane U = [[0,1],[1,0]] should be equivalent.
    code = r'''
    # method: INDEF_FORM_TestEquivalence
    using Oscar
    # Requires: using Indefinite
    Q1 = ZZ[0 1; 1 0]
    Q2 = ZZ[0 1; 1 0]
    result = INDEF_FORM_TestEquivalence(Q1, Q2)
    # Returns a unimodular matrix T such that T' * Q1 * T == Q2
    @test result !== nothing
    T = result
    @test T * Q1 * transpose(T) == Q2
    @test abs(det(T)) == 1
'''
    _jl_eval_testitem(code)
def test_2_indef_form_automorphism_group_hyperbolic_plane():
    """
    method: INDEF_FORM_AutomorphismGroup
    """
    # Indefinite.jl is not installed in the Julia env yet.
    # Aut(U) for the hyperbolic plane is infinite but finitely generated.
    code = r'''
    # method: INDEF_FORM_AutomorphismGroup
    using Oscar
    # Requires: using Indefinite
    Q = ZZ[0 1; 1 0]
    gens = INDEF_FORM_AutomorphismGroup(Q)
    @test length(gens) >= 1
    G = Q
    for g in gens
        @test g * G * transpose(g) == G
    end
'''
    _jl_eval_testitem(code)
def test_3_indef_form_get_orbit_representative_isotropic_vectors():
    """
    method: INDEF_FORM_GetOrbitRepresentative
    """
    # Indefinite.jl is not installed in the Julia env yet.
    # For U, C=0 gives primitive isotropic vectors; there should be orbits.
    code = r'''
    # method: INDEF_FORM_GetOrbitRepresentative
    using Oscar
    # Requires: using Indefinite
    Q = ZZ[0 1; 1 0]
    C = 0
    reps = INDEF_FORM_GetOrbitRepresentative(Q, C)
    @test length(reps) >= 1
    for v in reps
        @test transpose(v) * Q * v == C
    end
'''
    _jl_eval_testitem(code)
def test_4_indef_form_get_orbit_isotropic_kplane():
    """
    method: INDEF_FORM_GetOrbit_IsotropicKplane
    """
    # Indefinite.jl is not installed in the Julia env yet.
    # For U (sig (1,1)), k=1 totally isotropic subspaces exist.
    code = r'''
    # method: INDEF_FORM_GetOrbit_IsotropicKplane
    using Oscar
    # Requires: using Indefinite
    Q = ZZ[0 1; 1 0]
    k = 1
    orbits = INDEF_FORM_GetOrbit_IsotropicKplane(Q, k)
    @test length(orbits) >= 1
'''
    _jl_eval_testitem(code)
def test_5_indef_form_get_orbit_isotropic_kflag():
    """
    method: INDEF_FORM_GetOrbit_IsotropicKflag
    """
    # Indefinite.jl is not installed in the Julia env yet.
    code = r'''
    # method: INDEF_FORM_GetOrbit_IsotropicKflag
    using Oscar
    # Requires: using Indefinite
    Q = ZZ[0 1; 1 0]
    k = 1
    flags = INDEF_FORM_GetOrbit_IsotropicKflag(Q, k)
    @test length(flags) >= 1
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'INDEF_FORM_TestEquivalence',
    'INDEF_FORM_AutomorphismGroup',
    'INDEF_FORM_GetOrbitRepresentative',
    'INDEF_FORM_GetOrbit_IsotropicKplane',
    'INDEF_FORM_GetOrbit_IsotropicKflag',
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
