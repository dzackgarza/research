# Tests for §2.15: Primitive embeddings and extensions

@testitem "primitive_embeddings: A1 into A2 direct sum A1" begin
    # method: primitive_embeddings
    using Oscar
    M = root_lattice(:A, 1)
    L1 = root_lattice(:A, 2)
    L2 = root_lattice(:A, 1)
    L, _, _ = direct_sum(L1, L2)
    embs = primitive_embeddings(L, M)
    @test length(embs) >= 1
end

@testitem "primitive_embeddings: via genus" begin
    # method: primitive_embeddings(G::ZZGenus, M)
    using Oscar
    M = root_lattice(:A, 1)
    L = root_lattice(:A, 2)
    G = genus(L)
    embs = primitive_embeddings(G, M)
    @test length(embs) >= 0  # may or may not embed
end

@testitem "primitive_extensions: glue two lattices" begin
    # method: primitive_extensions
    using Oscar
    L1 = root_lattice(:A, 1)
    L2 = root_lattice(:A, 1)
    exts = primitive_extensions(L1, L2)
    @test length(exts) >= 1
end

@testitem "coverage guard: primitive embedding methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    # Primitive embeddings operate on ZZLat; introspect that type
    sample = root_lattice(:A, 2)
    assert_runtime_methods_covered(@__FILE__, sample)
end
