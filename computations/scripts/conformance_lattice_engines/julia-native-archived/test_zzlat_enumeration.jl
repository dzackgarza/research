# Tests for §2.6: Vector enumeration

@testitem "short_vectors: A2 has 6 vectors of norm 2" begin
    # method: short_vectors
    using Oscar
    L = root_lattice(:A, 2)
    sv = short_vectors(L, 2)
    # A2 has 6 roots; short_vectors returns up to sign, so 3 pairs
    @test length(sv) == 3
end

@testitem "shortest_vectors: A2 minimum norm is 2" begin
    # method: shortest_vectors
    using Oscar
    L = root_lattice(:A, 2)
    sv = shortest_vectors(L)
    @test length(sv) == 3  # up to sign
end

@testitem "minimum: A2 has minimum 2" begin
    # method: minimum
    using Oscar
    L = root_lattice(:A, 2)
    @test minimum(L) == 2
end

@testitem "minimum: E8 has minimum 2" begin
    # method: minimum
    using Oscar
    L = root_lattice(:E, 8)
    @test minimum(L) == 2
end

@testitem "kissing_number: A2 kissing number is 6" begin
    # method: kissing_number
    using Oscar
    L = root_lattice(:A, 2)
    @test kissing_number(L) == 6
end

@testitem "kissing_number: E8 kissing number is 240" begin
    # method: kissing_number
    using Oscar
    L = root_lattice(:E, 8)
    @test kissing_number(L) == 240
end

@testitem "close_vectors: finds vectors near target" begin
    # method: close_vectors
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    # Find lattice points within distance^2 <= 1 of (1/2, 1/2)
    cv = close_vectors(L, QQ[1//2, 1//2], 1)
    @test length(cv) > 0
end

@testitem "short_vectors: with lower and upper bound" begin
    # method: short_vectors
    using Oscar
    L = root_lattice(:D, 4)
    sv = short_vectors(L, 2, 4)
    @test length(sv) > 0
    for (v, n) in sv
        @test 2 <= n <= 4
    end
end

@testitem "coverage guard: enumeration methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    sample = integer_lattice(gram = ZZ[2 1; 1 2])
    assert_runtime_methods_covered(@__FILE__, sample)
end
