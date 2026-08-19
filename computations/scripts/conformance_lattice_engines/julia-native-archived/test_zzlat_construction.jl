# Tests for §2.3: ZZLat construction methods

@testitem "integer_lattice: construct from Gram matrix" begin
    # method: integer_lattice
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    @test gram_matrix(L) == ZZ[2 1; 1 2]
    @test rank(L) == 2
end

@testitem "integer_lattice: construct from basis and Gram" begin
    # method: integer_lattice(B; gram)
    using Oscar
    B = ZZ[1 0; 0 1]
    L = integer_lattice(B; gram = ZZ[2 0; 0 2])
    @test rank(L) == 2
    @test gram_matrix(L) == ZZ[2 0; 0 2]
end

@testitem "lattice: construct in quadratic space" begin
    # method: lattice
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    B = identity_matrix(QQ, 2)
    L = lattice(V, B)
    @test rank(L) == 2
end

@testitem "quadratic_lattice: construct from generators and Gram" begin
    # method: quadratic_lattice
    using Oscar
    L = quadratic_lattice(QQ, identity_matrix(QQ, 2); gram = QQ[2 0; 0 2])
    @test rank(L) == 2
end

@testitem "root_lattice: A2 has rank 2 and det 3" begin
    # method: root_lattice
    using Oscar
    L = root_lattice(:A, 2)
    @test rank(L) == 2
    @test det(L) == 3
end

@testitem "root_lattice: D4 has rank 4" begin
    # method: root_lattice
    using Oscar
    L = root_lattice(:D, 4)
    @test rank(L) == 4
end

@testitem "root_lattice: E8 is even unimodular of rank 8" begin
    # method: root_lattice
    using Oscar
    L = root_lattice(:E, 8)
    @test rank(L) == 8
    @test abs(det(L)) == 1
    @test is_even(L)
end

@testitem "hyperbolic_plane_lattice: signature (1,1)" begin
    # method: hyperbolic_plane_lattice
    using Oscar
    L = hyperbolic_plane_lattice()
    @test signature_tuple(L) == (1, 1, 0)
    @test det(L) == -1
end

@testitem "leech_lattice: rank 24 even unimodular" begin
    # method: leech_lattice
    using Oscar
    L = leech_lattice()
    @test rank(L) == 24
    @test abs(det(L)) == 1
    @test is_even(L)
end

@testitem "k3_lattice: rank 22 signature (3,19)" begin
    # method: k3_lattice
    using Oscar
    L = k3_lattice()
    @test rank(L) == 22
    p, n, z = signature_tuple(L)
    @test p == 3
    @test n == 19
end

@testitem "rescale: flips sign of Gram" begin
    # method: rescale
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 2])
    M = rescale(L, -1)
    @test gram_matrix(M) == ZZ[-2 0; 0 -2]
end

@testitem "rescale: scales Gram by integer" begin
    # method: rescale
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = rescale(L, 3)
    @test gram_matrix(M) == ZZ[3 0; 0 3]
end

@testitem "coverage guard: construction methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    sample = integer_lattice(gram = ZZ[2 1; 1 2])
    assert_runtime_methods_covered(@__FILE__, sample)
end
