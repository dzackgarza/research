# Tests for §2.13: QuadSpaceWithIsom

# -- Construction --

@testitem "quadratic_space_with_isometry: pair space with identity" begin
    # method: quadratic_space_with_isometry
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test rank(Vf) == 2
    @test order_of_isometry(Vf) == 1
end

@testitem "quadratic_space_with_isometry: pair with negation" begin
    # method: quadratic_space_with_isometry
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V; neg = true)
    @test rank(Vf) == 2
    @test order_of_isometry(Vf) == 2
end

# -- Accessors --

@testitem "space: extract space from QuadSpaceWithIsom" begin
    # method: space
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test rank(space(Vf)) == 2
end

@testitem "isometry: extract isometry matrix" begin
    # method: isometry
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    f = isometry(Vf)
    @test f == identity_matrix(QQ, 2)
end

@testitem "order_of_isometry: QuadSpaceWithIsom" begin
    # method: order_of_isometry
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V; neg = true)
    @test order_of_isometry(Vf) == 2
end

# -- Attributes --

@testitem "dim/rank: through QuadSpaceWithIsom" begin
    # method: dim
    # method: rank
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test dim(Vf) == 2
    @test rank(Vf) == 2
end

@testitem "gram_matrix/det/discriminant: QuadSpaceWithIsom" begin
    # method: gram_matrix
    # method: det
    # method: discriminant
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    @test gram_matrix(Vf) == QQ[2 1; 1 2]
    d = det(Vf)
    @test d == 3
    @test discriminant(Vf) == (-1)^dim(Vf) * d
end

@testitem "diagonal/signature_tuple: positive definite space" begin
    # method: diagonal
    # method: signature_tuple
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    diag = diagonal(Vf)
    @test length(diag) == 2
    @test all(x -> x > 0, diag)
    @test signature_tuple(Vf) == (2, 0)
end

@testitem "is_definite/is_positive_definite/is_negative_definite: QuadSpaceWithIsom" begin
    # method: is_definite
    # method: is_positive_definite
    # method: is_negative_definite
    using Oscar
    V_pd = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf_pd = quadratic_space_with_isometry(V_pd)
    @test is_definite(Vf_pd)
    @test is_positive_definite(Vf_pd)
    @test !is_negative_definite(Vf_pd)

    V_indef = quadratic_space(QQ, QQ[0 1; 1 0])
    Vf_indef = quadratic_space_with_isometry(V_indef)
    @test !is_definite(Vf_indef)
end

# -- Polynomials --

@testitem "characteristic_polynomial: QuadSpaceWithIsom" begin
    # method: characteristic_polynomial
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V; neg = true)
    p = characteristic_polynomial(Vf)
    @test degree(p) == 2
end

@testitem "minimal_polynomial: QuadSpaceWithIsom" begin
    # method: minimal_polynomial
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf_id = quadratic_space_with_isometry(V)
    Vf_neg = quadratic_space_with_isometry(V; neg = true)
    p_id = minimal_polynomial(Vf_id)
    p_neg = minimal_polynomial(Vf_neg)
    @test degree(p_id) == 1   # identity: x - 1
    @test degree(p_neg) == 1  # negation: x + 1
end

# -- Operations --

@testitem "^: raise QuadSpaceWithIsom isometry to power" begin
    # method: ^
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf_neg = quadratic_space_with_isometry(V; neg = true)
    Vf2 = Vf_neg^2
    @test order_of_isometry(Vf2) == 1
end

@testitem "direct_sum: equivariant direct sum of QuadSpaceWithIsom" begin
    # method: direct_sum
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    Wg = quadratic_space_with_isometry(V; neg = true)
    S, _, _ = direct_sum(Vf, Wg)
    @test rank(S) == 4
    @test det(S) == det(Vf) * det(Wg)
end

@testitem "rescale: det scales by a^dim" begin
    # method: rescale
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    Wf = rescale(Vf, 3)
    @test det(Wf) == 3^dim(Vf) * det(Vf)
end

@testitem "rational_spinor_norm: returns QQFieldElem" begin
    # method: rational_spinor_norm
    using Oscar
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    Vf = quadratic_space_with_isometry(V)
    s = rational_spinor_norm(Vf)
    @test s isa QQFieldElem
end

# -- Coverage Guard --

@testitem "coverage guard: QuadSpaceWithIsom methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    V = quadratic_space(QQ, QQ[2 1; 1 2])
    sample = quadratic_space_with_isometry(V)
    assert_runtime_methods_covered(@__FILE__, sample)
end
