# Tests for §2.16: Hermitian genera

@testitem "genus: global genus of hermitian lattice" begin
    # method: genus(L::HermLat)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    @test rank(g) == 2
end

@testitem "genus: local genus of hermitian lattice" begin
    # method: genus(L::HermLat, p)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    p = prime_decomposition(OK, 2)[1][1]
    g = genus(L, p)
    @test rank(g) == 2
end

@testitem "representative: hermitian genus representative" begin
    # method: representative(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    R = representative(g)
    @test rank(R) == 2
end

@testitem "representatives: all classes in hermitian genus" begin
    # method: representatives(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    reps = representatives(g)
    @test length(reps) >= 1
end

@testitem "mass: hermitian lattice mass" begin
    # method: mass
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    m = mass(L)
    @test m > 0
end

@testitem "rank: hermitian genus rank" begin
    # method: rank(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    @test rank(g) == 2
end

@testitem "signatures: hermitian genus signatures" begin
    # method: signatures(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    sigs = signatures(g)
    @test length(sigs) >= 1
end

@testitem "is_integral: hermitian genus integrality" begin
    # method: is_integral(G)
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    g = genus(L)
    @test is_integral(g) == true
end

@testitem "coverage guard: hermitian genera methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    sample = genus(L)
    assert_runtime_methods_covered(@__FILE__, sample)
end
