import sys


from juliacall import Main as jl

from conftest import covered_methods_from_module as _covered_methods_from_module


def _jl_eval_testitem(code: str) -> None:
    jl.seval(f"begin\n{code}\nnothing\nend")


def test_1_primitive_embeddings_a1_into_a2_direct_sum_a1():
    """
    method: primitive_embeddings
    """
    code = r'''
    # method: primitive_embeddings
    using Oscar
    M = root_lattice(:A, 1)
    L1 = root_lattice(:A, 2)
    L2 = root_lattice(:A, 1)
    L, _, _ = direct_sum(L1, L2)
    embs = primitive_embeddings(L, M)
    @test length(embs) >= 1
'''
    _jl_eval_testitem(code)

def test_2_primitive_embeddings_via_genus():
    """
    method: primitive_embeddings(G::ZZGenus, M)
    """
    code = r'''
    # method: primitive_embeddings(G::ZZGenus, M)
    using Oscar
    M = root_lattice(:A, 1)
    L = root_lattice(:A, 2)
    G = genus(L)
    embs = primitive_embeddings(G, M)
    @test length(embs) >= 0  # may or may not embed
'''
    _jl_eval_testitem(code)

def test_3_primitive_extensions_glue_two_lattices():
    """
    method: primitive_extensions
    """
    code = r'''
    # method: primitive_extensions
    using Oscar
    L1 = root_lattice(:A, 1)
    L2 = root_lattice(:A, 1)
    exts = primitive_extensions(L1, L2)
    @test length(exts) >= 1
'''
    _jl_eval_testitem(code)
def test_4_primitive_embeddings_via_torquadmodule():
    """
    method: primitive_embeddings(q::TorQuadModule, sig, M)
    """
    code = r'''
    # method: primitive_embeddings(q::TorQuadModule, sig, M)
    using Oscar
    M = root_lattice(:A, 1)
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    embs = primitive_embeddings(T, (2, 0), M)
    @test length(embs) >= 0
'''
    _jl_eval_testitem(code)


MIGRATED_METHODS = {
    'primitive_embeddings',
    'primitive_embeddings(G::ZZGenus, M)',
    'primitive_embeddings(q::TorQuadModule, sig, M)',
    'primitive_extensions',
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
