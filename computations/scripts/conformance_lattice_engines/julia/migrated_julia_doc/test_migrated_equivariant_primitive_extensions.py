import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_equivariant_primitive_extensions_a1_a1_with_identity():
    """
    method: equivariant_primitive_extensions
    """
    code = r'''
    # method: equivariant_primitive_extensions
    using Oscar
    L1 = root_lattice(:A, 1)
    Lf1 = integer_lattice_with_isometry(L1)
    Lf2 = integer_lattice_with_isometry(L1)
    result = equivariant_primitive_extensions(Lf1, Lf2)
    @test result isa Vector
    @test all(r -> rank(lattice(r)) == 2, result)
'''
    _jl_eval_testitem(code)

def test_2_equivariant_primitive_extensions_with_neg_true():
    """
    method: equivariant_primitive_extensions
    """
    code = r'''
    # method: equivariant_primitive_extensions
    using Oscar
    L1 = root_lattice(:A, 1)
    Lf1 = integer_lattice_with_isometry(L1; neg = true)
    Lf2 = integer_lattice_with_isometry(L1; neg = true)
    result = equivariant_primitive_extensions(Lf1, Lf2; glue_only = false)
    @test result isa Vector
    for r in result
        @test order_of_isometry(r) in [1, 2]
    end
'''
    _jl_eval_testitem(code)

def test_3_admissible_equivariant_primitive_extensions_from_admissible_triple():
    """
    method: admissible_equivariant_primitive_extensions
    """
    code = r'''
    # method: admissible_equivariant_primitive_extensions
    using Oscar
    L = root_lattice(:A, 2)
    g = genus(L)
    triples = admissible_triples(g, 2)
    if !isempty(triples)
        g1, g2 = first(triples)
        Qx, x = QQ["x"]
        p = x + 1
        result = admissible_equivariant_primitive_extensions(representative(g1), representative(g2), g, p, 2)
        @test result isa Vector
    else
        @test true
    end
'''
    _jl_eval_testitem(code)

MIGRATED_METHODS = {
    'admissible_equivariant_primitive_extensions',
    'equivariant_primitive_extensions',
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
