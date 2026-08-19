# Tests for §2.5: ZZLat reduction (LLL)

@testitem "lll: reduces basis of positive definite lattice" begin
    # method: lll
    using Oscar
    # Start with a non-reduced basis
    L = integer_lattice(gram = ZZ[4 2; 2 4])
    M = lll(L)
    @test rank(M) == rank(L)
    @test det(M) == det(L)
end

@testitem "lll: preserves lattice isometry class" begin
    # method: lll
    using Oscar
    L = root_lattice(:A, 3)
    M = lll(L)
    @test rank(M) == 3
    # LLL preserves the lattice, only changes basis
    @test det(M) == det(L)
end

@testitem "lll: works on indefinite lattice" begin
    # method: lll
    using Oscar
    L = hyperbolic_plane_lattice()
    M = lll(L)
    @test rank(M) == 2
    @test det(M) == det(L)
end

@testitem "coverage guard: reduction methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    sample = integer_lattice(gram = ZZ[2 1; 1 2])
    assert_runtime_methods_covered(@__FILE__, sample)
end
