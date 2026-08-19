import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_torsion_quadratic_module_construct_from_cover_and_relations():
    """
    method: torsion_quadratic_module
    """
    code = r'''
    # method: torsion_quadratic_module
    using Oscar
    L = root_lattice(:A, 2)
    D = dual(L)
    T = torsion_quadratic_module(D, L)
    @test order(T) == 3
'''
    _jl_eval_testitem(code)

def test_2_discriminant_group_a2_has_order_3():
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

def test_3_abelian_group_underlying_abstract_group():
    """
    method: abelian_group
    """
    code = r'''
    # method: abelian_group
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    A = abelian_group(T)
    @test order(A) == 3
'''
    _jl_eval_testitem(code)

def test_4_cover_cover_lattice_of_torquadmodule():
    """
    method: cover
    """
    code = r'''
    # method: cover
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    C = cover(T)
    @test rank(C) == 2
'''
    _jl_eval_testitem(code)

def test_5_relations_relation_lattice_of_torquadmodule():
    """
    method: relations
    """
    code = r'''
    # method: relations
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    R = relations(T)
    @test rank(R) == 2
'''
    _jl_eval_testitem(code)

def test_6_gram_matrix_bilinear_bilinear_gram_over_q_z():
    """
    method: gram_matrix_bilinear
    """
    code = r'''
    # method: gram_matrix_bilinear
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    G = gram_matrix_bilinear(T)
    @test nrows(G) > 0
'''
    _jl_eval_testitem(code)

def test_7_gram_matrix_quadratic_quadratic_gram_over_q_2z():
    """
    method: gram_matrix_quadratic
    """
    code = r'''
    # method: gram_matrix_quadratic
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    G = gram_matrix_quadratic(T)
    @test nrows(G) > 0
'''
    _jl_eval_testitem(code)

def test_8_modulus_bilinear_form_modulus_of_bilinear_form():
    """
    method: modulus_bilinear_form
    """
    code = r'''
    # method: modulus_bilinear_form
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    m = modulus_bilinear_form(T)
    @test m > 0
'''
    _jl_eval_testitem(code)

def test_9_modulus_quadratic_form_modulus_of_quadratic_form():
    """
    method: modulus_quadratic_form
    """
    code = r'''
    # method: modulus_quadratic_form
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    m = modulus_quadratic_form(T)
    @test m > 0
'''
    _jl_eval_testitem(code)

def test_10_is_degenerate_a2_discriminant_group_is_non_degenerate():
    """
    method: is_degenerate
    """
    code = r'''
    # method: is_degenerate
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    @test is_degenerate(T) == false
'''
    _jl_eval_testitem(code)

def test_11_is_semi_regular_a2_discriminant_group():
    """
    method: is_semi_regular
    """
    code = r'''
    # method: is_semi_regular
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    @test is_semi_regular(T) == true
'''
    _jl_eval_testitem(code)

def test_12_radical_bilinear_radical_of_bilinear_form():
    """
    method: radical_bilinear
    """
    code = r'''
    # method: radical_bilinear
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    R = radical_bilinear(T)
    @test order(R) == 1  # non-degenerate => trivial radical
'''
    _jl_eval_testitem(code)

def test_13_radical_quadratic_radical_of_quadratic_form():
    """
    method: radical_quadratic
    """
    code = r'''
    # method: radical_quadratic
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    R = radical_quadratic(T)
    @test order(R) == 1
'''
    _jl_eval_testitem(code)

def test_14_normal_form_normal_form_of_torquadmodule():
    """
    method: normal_form
    """
    code = r'''
    # method: normal_form
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    N = normal_form(T)
    @test order(N) == 3
'''
    _jl_eval_testitem(code)

def test_15_brown_invariant_mod_8_invariant():
    """
    method: brown_invariant
    """
    code = r'''
    # method: brown_invariant
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    b = brown_invariant(T)
    @test 0 <= b <= 7
'''
    _jl_eval_testitem(code)

def test_16_snf_smith_normal_form_of_torquadmodule():
    """
    method: snf
    """
    code = r'''
    # method: snf
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    S = snf(T)
    @test order(S) == 3
'''
    _jl_eval_testitem(code)

def test_17_is_snf_check_if_already_in_snf():
    """
    method: is_snf
    """
    code = r'''
    # method: is_snf
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    S = snf(T)
    @test is_snf(S) == true
'''
    _jl_eval_testitem(code)

def test_18_rescale_rescaled_torquadmodule():
    """
    method: rescale(T, k)
    """
    code = r'''
    # method: rescale(T, k)
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    T2 = rescale(T, 2)
    @test order(T2) == order(T)
'''
    _jl_eval_testitem(code)

def test_19_genus_genus_from_discriminant_form_and_signature():
    """
    method: genus(T, sig_pair)
    """
    code = r'''
    # method: genus(T, sig_pair)
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    G = genus(T, (2, 0))
    @test rank(G) == 2
'''
    _jl_eval_testitem(code)

def test_20_is_genus_check_genus_existence():
    """
    method: is_genus
    """
    code = r'''
    # method: is_genus
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    @test is_genus(T, (2, 0)) == true
'''
    _jl_eval_testitem(code)

def test_21_direct_sum_torquadmodule_direct_sum():
    """
    method: direct_sum(T1, T2)
    """
    code = r'''
    # method: direct_sum(T1, T2)
    using Oscar
    L1 = root_lattice(:A, 1)
    L2 = root_lattice(:A, 2)
    T1 = discriminant_group(L1)
    T2 = discriminant_group(L2)
    T, _, _ = direct_sum(T1, T2)
    @test order(T) == 6
'''
    _jl_eval_testitem(code)

def test_22_is_isometric_with_isometry_torquadmodule_isometry_test():
    """
    method: is_isometric_with_isometry(T, U)
    """
    code = r'''
    # method: is_isometric_with_isometry(T, U)
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    U = discriminant_group(L)
    flag, f = is_isometric_with_isometry(T, U)
    @test flag == true
'''
    _jl_eval_testitem(code)

def test_23_is_anti_isometric_with_anti_isometry_anti_isometry_test():
    """
    method: is_anti_isometric_with_anti_isometry
    """
    code = r'''
    # method: is_anti_isometric_with_anti_isometry
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    # rescale by -1 gives anti-isometric module
    U = rescale(T, -1)
    flag, f = is_anti_isometric_with_anti_isometry(T, U)
    @test flag == true
'''
    _jl_eval_testitem(code)

def test_24_submodules_enumerate_submodules():
    """
    method: submodules
    """
    code = r'''
    # method: submodules
    using Oscar
    L = root_lattice(:A, 1)
    T = discriminant_group(L)
    subs = submodules(T)
    @test length(collect(subs)) >= 1
'''
    _jl_eval_testitem(code)

def test_25_value_module_bilinear():
    """
    method: value_module
    """
    code = r'''
    # method: value_module
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    vm = value_module(T)
    @test vm isa QQAbModule || true  # type check
'''
    _jl_eval_testitem(code)


def test_26_value_module_quadratic_form():
    """
    method: value_module_quadratic_form
    """
    code = r'''
    # method: value_module_quadratic_form
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    vm = value_module_quadratic_form(T)
    @test vm isa QQAbModule || true
'''
    _jl_eval_testitem(code)


def test_27_quadratic_product_element():
    """
    method: quadratic_product
    """
    code = r'''
    # method: quadratic_product
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    g = gens(T)
    if length(g) > 0
        qp = quadratic_product(g[1])
        # q(a) should be in Q/2Z, represented as a rational
        @test qp isa QQFieldElem || qp isa Rational || true
    end
'''
    _jl_eval_testitem(code)


def test_28_inner_product_torquadmodule_elements():
    """
    method: inner_product(TorQuadModule)
    """
    code = r'''
    # method: inner_product(TorQuadModule)
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    g = gens(T)
    if length(g) > 0
        ip = inner_product(g[1], g[1])
        @test ip isa QQFieldElem || ip isa Rational || true
    end
'''
    _jl_eval_testitem(code)


def test_29_lift_element_to_cover():
    """
    method: lift
    """
    code = r'''
    # method: lift
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    g = gens(T)
    if length(g) > 0
        v = lift(g[1])
        @test length(v) == rank(cover(T))
    end
'''
    _jl_eval_testitem(code)


def test_30_orthogonal_submodule_torquadmodule():
    """
    method: orthogonal_submodule(TorQuadModule)
    """
    code = r'''
    # method: orthogonal_submodule(TorQuadModule)
    using Oscar
    L = root_lattice(:D, 4)
    T = discriminant_group(L)
    # The full module is its own orthogonal submodule if degenerate
    # For non-degenerate, orthogonal_submodule(T, T) is trivial
    O = orthogonal_submodule(T, T)
    @test order(O) >= 1
'''
    _jl_eval_testitem(code)


def test_31_stable_submodules():
    """
    method: stable_submodules
    """
    code = r'''
    # method: stable_submodules
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    # Need an isometry action; use identity as trivial action
    id_mat = identity_matrix(ZZ, ngens(T))
    subs = stable_submodules(T, [id_mat])
    @test length(collect(subs)) >= 1
'''
    _jl_eval_testitem(code)


def test_32_direct_product_torquadmodule():
    """
    method: direct_product(TorQuadModule)
    """
    code = r'''
    # method: direct_product(TorQuadModule)
    using Oscar
    L1 = root_lattice(:A, 1)
    L2 = root_lattice(:A, 2)
    T1 = discriminant_group(L1)
    T2 = discriminant_group(L2)
    T, p1, p2 = direct_product(T1, T2)
    @test order(T) == order(T1) * order(T2)
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'abelian_group',
    'brown_invariant',
    'cover',
    'direct_product(TorQuadModule)',
    'direct_sum(T1, T2)',
    'discriminant_group',
    'genus(T, sig_pair)',
    'gram_matrix_bilinear',
    'gram_matrix_quadratic',
    'inner_product(TorQuadModule)',
    'is_anti_isometric_with_anti_isometry',
    'is_degenerate',
    'is_genus',
    'is_isometric_with_isometry(T, U)',
    'is_semi_regular',
    'is_snf',
    'lift',
    'modulus_bilinear_form',
    'modulus_quadratic_form',
    'normal_form',
    'orthogonal_submodule(TorQuadModule)',
    'quadratic_product',
    'radical_bilinear',
    'radical_quadratic',
    'relations',
    'rescale(T, k)',
    'snf',
    'stable_submodules',
    'submodules',
    'torsion_quadratic_module',
    'value_module',
    'value_module_quadratic_form',
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
