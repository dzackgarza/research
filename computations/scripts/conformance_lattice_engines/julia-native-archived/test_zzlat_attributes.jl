# Tests for §2.4: ZZLat intrinsic data / attributes

@testitem "gram_matrix: returns correct matrix" begin
    # method: gram_matrix
    using Oscar
    G = ZZ[2 1; 1 2]
    L = integer_lattice(gram = G)
    @test gram_matrix(L) == G
end

@testitem "basis_matrix: identity for standard construction" begin
    # method: basis_matrix
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 2])
    B = basis_matrix(L)
    @test nrows(B) == 2
    @test ncols(B) == 2
end

@testitem "ambient_space: returns quadratic space" begin
    # method: ambient_space
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    V = ambient_space(L)
    @test rank(V) == 2
end

@testitem "rational_span: returns quadratic space over QQ" begin
    # method: rational_span
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    V = rational_span(L)
    @test rank(V) == 2
end

@testitem "rank: returns lattice rank" begin
    # method: rank
    using Oscar
    L = integer_lattice(gram = ZZ[2 1 0; 1 2 0; 0 0 4])
    @test rank(L) == 3
end

@testitem "degree: ambient dimension" begin
    # method: degree
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    @test degree(L) >= rank(L)
end

@testitem "signature_tuple: positive definite A2" begin
    # method: signature_tuple
    using Oscar
    L = root_lattice(:A, 2)
    p, n, z = signature_tuple(L)
    @test p == 2
    @test n == 0
end

@testitem "signature_tuple: indefinite hyperbolic plane" begin
    # method: signature_tuple
    using Oscar
    L = hyperbolic_plane_lattice()
    @test signature_tuple(L) == (1, 1, 0)
end

@testitem "det: determinant of Gram matrix" begin
    # method: det
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    @test det(L) == 3
end

@testitem "discriminant: lattice discriminant" begin
    # method: discriminant
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    d = discriminant(L)
    @test d == (-1)^rank(L) * det(L)
end

@testitem "scale: scale ideal" begin
    # method: scale
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 4])
    s = scale(L)
    @test s == 2
end

@testitem "norm: norm ideal" begin
    # method: norm
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 4])
    n = norm(L)
    @test n == 2
end

@testitem "is_positive_definite: true for A2" begin
    # method: is_positive_definite
    using Oscar
    L = root_lattice(:A, 2)
    @test is_positive_definite(L) == true
end

@testitem "is_negative_definite: false for A2" begin
    # method: is_negative_definite
    using Oscar
    L = root_lattice(:A, 2)
    @test is_negative_definite(L) == false
end

@testitem "is_definite: true for positive definite lattice" begin
    # method: is_definite
    using Oscar
    L = root_lattice(:A, 2)
    @test is_definite(L) == true
end

@testitem "is_definite: false for indefinite lattice" begin
    # method: is_definite
    using Oscar
    L = hyperbolic_plane_lattice()
    @test is_definite(L) == false
end

@testitem "is_even: true for E8" begin
    # method: is_even
    using Oscar
    L = root_lattice(:E, 8)
    @test is_even(L) == true
end

@testitem "is_integral: true for integer lattice" begin
    # method: is_integral
    using Oscar
    L = integer_lattice(gram = ZZ[2 1; 1 2])
    @test is_integral(L) == true
end

@testitem "is_unimodular: true for E8" begin
    # method: is_unimodular
    using Oscar
    L = root_lattice(:E, 8)
    @test is_unimodular(L) == true
end

@testitem "is_unimodular: false for A2" begin
    # method: is_unimodular
    using Oscar
    L = root_lattice(:A, 2)
    @test is_unimodular(L) == false
end

@testitem "is_primary: A2 is 3-primary" begin
    # method: is_primary
    using Oscar
    L = root_lattice(:A, 2)
    @test is_primary(L, 3) == true
end

@testitem "is_primary_with_prime: returns (true, p) for primary lattice" begin
    # method: is_primary_with_prime
    using Oscar
    L = root_lattice(:A, 2)
    flag, p = is_primary_with_prime(L)
    @test flag == true
    @test p == 3
end

@testitem "is_elementary: A1 is 2-elementary" begin
    # method: is_elementary
    using Oscar
    L = root_lattice(:A, 1)
    @test is_elementary(L, 2) == true
end

@testitem "is_elementary_with_prime: returns (true, p)" begin
    # method: is_elementary_with_prime
    using Oscar
    L = root_lattice(:A, 1)
    flag, p = is_elementary_with_prime(L)
    @test flag == true
    @test p == 2
end

@testitem "coverage guard: attribute methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    sample = integer_lattice(gram = ZZ[2 1; 1 2])
    assert_runtime_methods_covered(@__FILE__, sample)
end
