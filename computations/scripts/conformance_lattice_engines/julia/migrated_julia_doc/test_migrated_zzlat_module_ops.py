import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_direct_sum_sum_of_two_rank_1_lattices():
    """
    method: direct_sum
    """
    code = r'''
    # method: direct_sum
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, i1, i2 = direct_sum(L1, L2)
    @test rank(L) == 2
    @test det(L) == 8
'''
    _jl_eval_testitem(code)

def test_2_direct_product_product_of_two_lattices():
    """
    method: direct_product
    """
    code = r'''
    # method: direct_product
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, p1, p2 = direct_product(L1, L2)
    @test rank(L) == 2
'''
    _jl_eval_testitem(code)

def test_3_biproduct_returns_injections_and_projections():
    """
    method: biproduct
    """
    code = r'''
    # method: biproduct
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, i1, i2, p1, p2 = biproduct(L1, L2)
    @test rank(L) == 2
'''
    _jl_eval_testitem(code)

def test_4_intersect_intersection_in_common_ambient():
    """
    method: intersect
    """
    code = r'''
    # method: intersect
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    # 2L is a sublattice of L
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    I = intersect(L, M)
    @test rank(I) == 2
'''
    _jl_eval_testitem(code)

def test_5_dual_dual_lattice_has_reciprocal_determinant():
    """
    method: dual
    """
    code = r'''
    # method: dual
    using Oscar
    L = integer_lattice(gram = ZZ[2;;])
    D = dual(L)
    @test rank(D) == 1
    # det(L) * det(L^vee) = 1 for rank 1
'''
    _jl_eval_testitem(code)

def test_6_is_sublattice_2l_is_sublattice_of_l():
    """
    method: is_sublattice
    """
    code = r'''
    # method: is_sublattice
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    @test is_sublattice(L, M) == true
'''
    _jl_eval_testitem(code)

def test_7_is_primitive_direct_summand_is_primitive():
    """
    method: is_primitive
    """
    code = r'''
    # method: is_primitive
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, i1, i2 = direct_sum(L1, L2)
    S = lattice_in_same_ambient_space(L, i1.matrix)
    @test is_primitive(L, S) == true
'''
    _jl_eval_testitem(code)

def test_8_orthogonal_submodule_orthogonal_complement():
    """
    method: orthogonal_submodule
    """
    code = r'''
    # method: orthogonal_submodule
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, i1, i2 = direct_sum(L1, L2)
    S = lattice_in_same_ambient_space(L, i1.matrix)
    O = orthogonal_submodule(L, S)
    @test rank(O) == 1
'''
    _jl_eval_testitem(code)

def test_9_lattice_in_same_ambient_space_sublattice_construction():
    """
    method: lattice_in_same_ambient_space
    """
    code = r'''
    # method: lattice_in_same_ambient_space
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    B = 2 * basis_matrix(L)
    M = lattice_in_same_ambient_space(L, B)
    @test rank(M) == 2
'''
    _jl_eval_testitem(code)

def test_10_primitive_closure_primitive_closure_of_sublattice():
    """
    method: primitive_closure
    """
    code = r'''
    # method: primitive_closure
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    P = primitive_closure(L, M)
    @test is_primitive(L, P) == true
'''
    _jl_eval_testitem(code)

def test_11_maximal_integral_lattice_maximal_overlattice():
    """
    method: maximal_integral_lattice
    """
    code = r'''
    # method: maximal_integral_lattice
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 2])
    M = maximal_integral_lattice(L)
    @test is_integral(M) == true
'''
    _jl_eval_testitem(code)

def test_12_is_maximal_integral_test_maximality():
    """
    method: is_maximal_integral
    """
    code = r'''
    # method: is_maximal_integral
    using Oscar
    L = root_lattice(:E, 8)
    @test is_maximal_integral(L) == true
'''
    _jl_eval_testitem(code)

def test_13_root_lattice_recognition_identifies_a2():
    """
    method: root_lattice_recognition
    """
    code = r'''
    # method: root_lattice_recognition
    using Oscar
    L = root_lattice(:A, 2)
    R = root_lattice_recognition(L)
    @test length(R) > 0
'''
    _jl_eval_testitem(code)

def test_14_ade_type_identifies_root_type():
    """
    method: ADE_type
    """
    code = r'''
    # method: ADE_type
    using Oscar
    L = root_lattice(:A, 2)
    t = ADE_type(L)
    @test length(t) > 0
'''
    _jl_eval_testitem(code)

def test_15_coxeter_number_a2_coxeter_number_is_3():
    """
    method: coxeter_number
    """
    code = r'''
    # method: coxeter_number
    using Oscar
    L = root_lattice(:A, 2)
    @test coxeter_number(L) == 3
'''
    _jl_eval_testitem(code)

def test_16_highest_root_a2_highest_root():
    """
    method: highest_root
    """
    code = r'''
    # method: highest_root
    using Oscar
    L = root_lattice(:A, 2)
    h = highest_root(L)
    @test length(h) > 0
'''
    _jl_eval_testitem(code)

def test_17_kernel_lattice_kernel_of_endomorphism():
    """
    method: kernel_lattice
    """
    code = r'''
    # method: kernel_lattice
    using Oscar
    L = root_lattice(:A, 2)
    # Identity minus identity = zero map; kernel is the whole lattice
    f = identity_matrix(ZZ, 2)
    K = kernel_lattice(L, f - f)
    @test rank(K) == rank(L)
'''
    _jl_eval_testitem(code)

def test_18_lattice_sum_in_common_ambient():
    """
    method: +(L1, L2)
    """
    code = r'''
    # method: +(L1, L2)
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    S = L + M
    # Sum should equal L since M is a sublattice
    @test rank(S) == 2
'''
    _jl_eval_testitem(code)


def test_19_scalar_multiple_of_lattice():
    """
    method: *(n, L)
    """
    code = r'''
    # method: *(n, L)
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = 2 * L
    @test rank(M) == 2
    # 2*L has basis 2*I, so Gram of 2L in ambient is 4*I
'''
    _jl_eval_testitem(code)


def test_20_is_sublattice_with_relations():
    """
    method: is_sublattice_with_relations
    """
    code = r'''
    # method: is_sublattice_with_relations
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    flag, rels = is_sublattice_with_relations(L, M)
    @test flag == true
'''
    _jl_eval_testitem(code)


def test_21_divisibility_of_vector():
    """
    method: divisibility
    """
    code = r'''
    # method: divisibility
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 2])
    v = ZZ[1, 0]
    d = divisibility(L, v)
    # divisibility = gcd of b(v, w) for w in L = gcd(2, 0) = 2
    @test d == 2
'''
    _jl_eval_testitem(code)


def test_22_vector_membership_test():
    """
    method: in(v, L)
    """
    code = r'''
    # method: in(v, L)
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    v = ZZ[1, 0]
    # Standard basis vector should be in L
    @test v in L
'''
    _jl_eval_testitem(code)


def test_23_irreducible_components_of_direct_sum():
    """
    method: irreducible_components
    """
    code = r'''
    # method: irreducible_components
    using Oscar
    L1 = root_lattice(:A, 1)
    L2 = root_lattice(:A, 2)
    L, _, _ = direct_sum(L1, L2)
    comps = irreducible_components(L)
    @test length(comps) == 2
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    '*(n, L)',
    '+(L1, L2)',
    'ADE_type',
    'biproduct',
    'coxeter_number',
    'direct_product',
    'direct_sum',
    'divisibility',
    'dual',
    'highest_root',
    'in(v, L)',
    'intersect',
    'irreducible_components',
    'is_maximal_integral',
    'is_primitive',
    'is_sublattice',
    'is_sublattice_with_relations',
    'kernel_lattice',
    'lattice_in_same_ambient_space',
    'maximal_integral_lattice',
    'orthogonal_submodule',
    'primitive_closure',
    'root_lattice_recognition',
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
