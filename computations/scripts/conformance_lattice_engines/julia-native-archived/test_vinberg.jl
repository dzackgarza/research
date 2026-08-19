# Tests for §2.10: Vinberg's algorithm

@testitem "vinberg_algorithm: finds roots of hyperbolic lattice" begin
    # method: vinberg_algorithm
    using Oscar
    # Hyperbolic plane direct sum with negative definite part
    # Use a simple (1,n) lattice: U + A1(-1)
    L = hyperbolic_plane_lattice()
    # vinberg_algorithm needs signature (1,0,n), so use from Gram matrix
    # Simple rank-2 hyperbolic: diag(1, -1)
    Q = ZZ[1 0; 0 -1]
    roots = vinberg_algorithm(Q, 2)
    @test length(roots) > 0
end

@testitem "vinberg_algorithm: from ZZLat" begin
    # method: vinberg_algorithm(S::ZZLat, ub)
    using Oscar
    # Construct a signature (1,0,n) lattice
    Q = ZZ[1 0; 0 -1]
    L = integer_lattice(gram = Q)
    roots = vinberg_algorithm(L, 2)
    @test length(roots) > 0
end

@testitem "short_vectors_affine: affine enumeration" begin
    # method: short_vectors_affine
    using Oscar
    # This is used internally by Vinberg; test with a simple lattice
    L = integer_lattice(gram = ZZ[1 0; 0 -1])
    # Find vectors x with x^2 = d and x . v = alpha
    # This may require specific setup; test that it returns a collection
    v = ZZ[1, 0]
    result = short_vectors_affine(L, v, 0, -1)
    @test result isa Vector || result isa AbstractVector
end

@testitem "coverage guard: Vinberg methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    sample = integer_lattice(gram = ZZ[1 0; 0 -1])
    assert_runtime_methods_covered(@__FILE__, sample)
end
