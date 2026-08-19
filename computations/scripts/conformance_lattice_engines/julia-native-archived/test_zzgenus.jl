# Tests for §2.7: Genus and classification

@testitem "genus: compute genus of A2" begin
    # method: genus(L::ZZLat)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    @test rank(G) == 2
    @test det(G) == 3
end

@testitem "genus: from Gram matrix" begin
    # method: genus(A::MatElem)
    using Oscar
    G = genus(ZZ[2 1; 1 2])
    @test rank(G) == 2
end

@testitem "genus: local genus at prime" begin
    # method: genus(L, p)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    @test prime(S) == 3
end

@testitem "representative: genus representative matches rank" begin
    # method: representative
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    R = representative(G)
    @test rank(R) == 2
end

@testitem "representatives: genus representatives of A2" begin
    # method: representatives
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    reps = representatives(G)
    @test length(reps) >= 1
end

@testitem "mass: genus mass is positive" begin
    # method: mass
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    m = mass(G)
    @test m > 0
end

@testitem "dim: genus dimension equals rank" begin
    # method: dim(gen)
    using Oscar
    L = root_lattice(:A, 3)
    G = genus(L)
    @test dim(G) == 3
end

@testitem "signature: genus signature" begin
    # method: signature(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    p, n = signature(G)
    @test p == 2
    @test n == 0
end

@testitem "iseven: genus evenness" begin
    # method: iseven(gen)
    using Oscar
    L = root_lattice(:E, 8)
    G = genus(L)
    @test iseven(G) == true
end

@testitem "is_definite: genus definiteness" begin
    # method: is_definite(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    @test is_definite(G) == true
end

@testitem "level: genus level" begin
    # method: level
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    lv = level(G)
    @test lv > 0
end

@testitem "scale: genus scale" begin
    # method: scale(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    s = scale(G)
    @test s > 0
end

@testitem "norm: genus norm" begin
    # method: norm(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    n = norm(G)
    @test n > 0
end

@testitem "primes: list of primes in genus" begin
    # method: primes
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    ps = primes(G)
    @test 3 in ps  # A2 has det 3
end

@testitem "is_integral: genus integrality" begin
    # method: is_integral(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    @test is_integral(G) == true
end

@testitem "local_symbol: retrieve local genus" begin
    # method: local_symbol
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    S = local_symbol(G, 3)
    @test prime(S) == 3
end

@testitem "quadratic_space: genus quadratic space" begin
    # method: quadratic_space(gen)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    V = quadratic_space(G)
    @test rank(V) == 2
end

@testitem "rational_representative: genus rational form" begin
    # method: rational_representative
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    R = rational_representative(G)
    @test rank(R) == 2
end

@testitem "rescale: genus rescaling" begin
    # method: rescale(gen, a)
    using Oscar
    L = root_lattice(:A, 2)
    G = genus(L)
    G2 = rescale(G, 2)
    @test det(G2) == det(G) * 2^rank(G)
end

@testitem "direct_sum: genus direct sum" begin
    # method: direct_sum(G1::ZZGenus, G2::ZZGenus)
    using Oscar
    L1 = root_lattice(:A, 1)
    L2 = root_lattice(:A, 1)
    G1 = genus(L1)
    G2 = genus(L2)
    G = direct_sum(G1, G2)
    @test rank(G) == 2
end

@testitem "represents: genus representation" begin
    # method: represents
    using Oscar
    L1 = root_lattice(:A, 2)
    L2 = root_lattice(:A, 1)
    G1 = genus(L1)
    G2 = genus(L2)
    @test represents(G1, G2) == true
end

@testitem "integer_genera: enumerate genus symbols" begin
    # method: integer_genera
    using Oscar
    gs = integer_genera((2, 0), 3)
    @test length(gs) >= 1
end

@testitem "discriminant_group: L^vee/L as TorQuadModule" begin
    # method: discriminant_group
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    @test order(T) == 3
end

@testitem "genus_representatives: all classes in genus" begin
    # method: genus_representatives
    using Oscar
    L = root_lattice(:A, 2)
    reps = genus_representatives(L)
    @test length(reps) >= 1
end

# -- ZZLocalGenus methods --

@testitem "prime: local genus prime" begin
    # method: prime(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    @test prime(S) == 3
end

@testitem "iseven: local genus evenness" begin
    # method: iseven(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    @test iseven(S) isa Bool
end

@testitem "hasse_invariant: local genus Hasse invariant" begin
    # method: hasse_invariant(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    h = hasse_invariant(S)
    @test h in [1, -1]
end

@testitem "det: local genus determinant" begin
    # method: det(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    @test det(S) != 0
end

@testitem "rank: local genus rank" begin
    # method: rank(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    @test rank(S) == 2
end

@testitem "excess: local genus excess" begin
    # method: excess(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    e = excess(S)
    @test e isa Integer
end

@testitem "signature: local genus signature" begin
    # method: signature(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    sig = signature(S)
    @test sig isa Integer
end

@testitem "oddity: local genus 2-adic oddity" begin
    # method: oddity(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 2)
    o = oddity(S)
    @test o isa Integer
end

@testitem "representative: local genus representative" begin
    # method: representative(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    R = representative(S)
    @test rank(R) == 2
end

@testitem "gram_matrix: local genus Gram matrix" begin
    # method: gram_matrix(S)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    G = gram_matrix(S)
    @test nrows(G) == 2
end

@testitem "rescale: local genus rescaling" begin
    # method: rescale(S, a)
    using Oscar
    L = root_lattice(:A, 2)
    S = genus(L, 3)
    S2 = rescale(S, 2)
    @test rank(S2) == rank(S)
end

@testitem "direct_sum: local genus direct sum" begin
    # method: direct_sum(S1, S2)
    using Oscar
    L = root_lattice(:A, 1)
    S1 = genus(L, 2)
    S2 = genus(L, 2)
    S = direct_sum(S1, S2)
    @test rank(S) == 2
end

@testitem "coverage guard: ZZGenus methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    L = root_lattice(:A, 2)
    sample = genus(L)
    assert_runtime_methods_covered(@__FILE__, sample)
end

@testitem "coverage guard: ZZLocalGenus methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    L = root_lattice(:A, 2)
    sample = genus(L, 3)
    assert_runtime_methods_covered(@__FILE__, sample)
end
