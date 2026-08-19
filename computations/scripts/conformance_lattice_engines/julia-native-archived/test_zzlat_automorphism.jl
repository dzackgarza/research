# Tests for §2.8: Automorphism and isometry

@testitem "automorphism_group_generators: A2 automorphism group" begin
    # method: automorphism_group_generators
    using Oscar
    L = root_lattice(:A, 2)
    gens = automorphism_group_generators(L)
    @test length(gens) >= 1
    # Each generator should preserve the Gram matrix
    G = gram_matrix(L)
    for g in gens
        @test g * G * transpose(g) == G
    end
end

@testitem "automorphism_group_order: A2 has |Aut| = 12" begin
    # method: automorphism_group_order
    using Oscar
    L = root_lattice(:A, 2)
    @test automorphism_group_order(L) == 12
end

@testitem "is_isometric: A2 is isometric to itself" begin
    # method: is_isometric
    using Oscar
    L = root_lattice(:A, 2)
    M = root_lattice(:A, 2)
    @test is_isometric(L, M) == true
end

@testitem "is_isometric: A2 not isometric to A3" begin
    # method: is_isometric
    using Oscar
    L = root_lattice(:A, 2)
    M = root_lattice(:A, 3)
    @test is_isometric(L, M) == false
end

@testitem "is_isometric_with_isometry: returns transformation" begin
    # method: is_isometric_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    M = root_lattice(:A, 2)
    flag, T = is_isometric_with_isometry(L, M)
    @test flag == true
    @test T * gram_matrix(L) * transpose(T) == gram_matrix(M)
end

@testitem "is_rationally_isometric: same genus implies rational isometry" begin
    # method: is_rationally_isometric
    using Oscar
    L = root_lattice(:A, 2)
    M = root_lattice(:A, 2)
    @test is_rationally_isometric(L, M) == true
end

@testitem "hasse_invariant: A2 at prime 2" begin
    # method: hasse_invariant
    using Oscar
    L = root_lattice(:A, 2)
    h = hasse_invariant(L, 2)
    @test h in [1, -1]
end

@testitem "witt_invariant: A2 at prime 2" begin
    # method: witt_invariant
    using Oscar
    L = root_lattice(:A, 2)
    w = witt_invariant(L, 2)
    @test w in [1, -1]
end

@testitem "coverage guard: automorphism methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    sample = root_lattice(:A, 2)
    assert_runtime_methods_covered(@__FILE__, sample)
end
