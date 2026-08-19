import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_integer_lattice_construct_from_gram_matrix():
    """
    method: integer_lattice
    """
    code = r'''
    # method: integer_lattice
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    @test gram_matrix(L) == ZZ[2 1; 1 2]
    @test rank(L) == 2
'''
    _jl_eval_testitem(code)

def test_2_integer_lattice_construct_from_basis_and_gram():
    """
    method: integer_lattice(B; gram)
    """
    code = r'''
    # method: integer_lattice(B; gram)
    using Oscar
    B = ZZ[1 0; 0 1]
    L = integer_lattice(B; gram = ZZ[2 0; 0 2])
    @test rank(L) == 2
    @test gram_matrix(L) == ZZ[2 0; 0 2]
'''
    _jl_eval_testitem(code)

def test_3_lattice_construct_in_quadratic_space():
    """
    method: lattice
    """
    code = r'''
    # method: lattice
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    B = identity_matrix(QQ, 2)
    L = lattice(V, B)
    @test rank(L) == 2
'''
    _jl_eval_testitem(code)

def test_4_quadratic_lattice_construct_from_generators_and_gram():
    """
    method: quadratic_lattice
    """
    code = r'''
    # method: quadratic_lattice
    using Oscar
    L = quadratic_lattice(QQ, identity_matrix(QQ, 2); gram = QQ[2 0; 0 2])
    @test rank(L) == 2
'''
    _jl_eval_testitem(code)

def test_5_root_lattice_a2_has_rank_2_and_det_3():
    """
    method: root_lattice
    """
    code = r'''
    # method: root_lattice
    using Oscar
    L = root_lattice(:A, 2)
    @test rank(L) == 2
    @test det(L) == 3
'''
    _jl_eval_testitem(code)

def test_6_root_lattice_d4_has_rank_4():
    """
    method: root_lattice
    """
    code = r'''
    # method: root_lattice
    using Oscar
    L = root_lattice(:D, 4)
    @test rank(L) == 4
'''
    _jl_eval_testitem(code)

def test_7_root_lattice_e8_is_even_unimodular_of_rank_8():
    """
    method: root_lattice
    """
    code = r'''
    # method: root_lattice
    using Oscar
    L = root_lattice(:E, 8)
    @test rank(L) == 8
    @test abs(det(L)) == 1
    @test is_even(L)
'''
    _jl_eval_testitem(code)

def test_8_hyperbolic_plane_lattice_signature_1_1():
    """
    method: hyperbolic_plane_lattice
    """
    code = r'''
    # method: hyperbolic_plane_lattice
    using Oscar
    L = hyperbolic_plane_lattice()
    @test signature_tuple(L) == (1, 1, 0)
    @test det(L) == -1
'''
    _jl_eval_testitem(code)

def test_9_leech_lattice_rank_24_even_unimodular():
    """
    method: leech_lattice
    """
    code = r'''
    # method: leech_lattice
    using Oscar
    L = leech_lattice()
    @test rank(L) == 24
    @test abs(det(L)) == 1
    @test is_even(L)
'''
    _jl_eval_testitem(code)

def test_10_k3_lattice_rank_22_signature_3_19():
    """
    method: k3_lattice
    """
    code = r'''
    # method: k3_lattice
    using Oscar
    L = k3_lattice()
    @test rank(L) == 22
    p, n, z = signature_tuple(L)
    @test p == 3
    @test n == 19
'''
    _jl_eval_testitem(code)

def test_11_rescale_flips_sign_of_gram():
    """
    method: rescale
    """
    code = r'''
    # method: rescale
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 2])
    M = rescale(L, -1)
    @test gram_matrix(M) == ZZ[-2 0; 0 -2]
'''
    _jl_eval_testitem(code)

def test_12_rescale_scales_gram_by_integer():
    """
    method: rescale
    """
    code = r'''
    # method: rescale
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = rescale(L, 3)
    @test gram_matrix(M) == ZZ[3 0; 0 3]
'''
    _jl_eval_testitem(code)

def test_13_mukai_lattice_rank_24_indefinite():
    """
    method: mukai_lattice
    """
    code = r'''
    # method: mukai_lattice
    using Oscar
    L = mukai_lattice()
    @test rank(L) == 24
    p, n, z = signature_tuple(L)
    # Mukai lattice has signature (4, 20)
    @test p == 4
    @test n == 20
'''
    _jl_eval_testitem(code)

def test_14_hyperkaehler_lattice_k3_type():
    """
    method: hyperkaehler_lattice
    """
    code = r'''
    # method: hyperkaehler_lattice
    using Oscar
    L = hyperkaehler_lattice(:K3)
    @test rank(L) >= 3
    p, n, z = signature_tuple(L)
    @test p == 3
    @test n == 20
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'hyperkaehler_lattice',
    'hyperbolic_plane_lattice',
    'integer_lattice',
    'integer_lattice(B; gram)',
    'k3_lattice',
    'lattice',
    'leech_lattice',
    'mukai_lattice',
    'quadratic_lattice',
    'rescale',
    'root_lattice',
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
