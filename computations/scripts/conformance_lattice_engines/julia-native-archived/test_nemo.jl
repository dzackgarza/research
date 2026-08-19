# Tests for §4: Nemo.jl matrix-level lattice operations

@testitem "lll: LLL reduction of ZZMatrix" begin
    # method: lll(B::ZZMatrix)
    using Oscar
    B = ZZ[1 0; 1 2]
    L = lll(B)
    @test nrows(L) == 2
    @test ncols(L) == 2
    # LLL-reduced first row should be shorter
end

@testitem "lll_with_transform: returns reduced basis and transform" begin
    # method: lll_with_transform
    using Oscar
    B = ZZ[1 0; 1 2]
    L, T = lll_with_transform(B)
    @test L == T * B
end

@testitem "lll_gram: LLL on Gram matrix" begin
    # method: lll_gram
    using Oscar
    G = ZZ[4 2; 2 4]
    L = lll_gram(G)
    @test nrows(L) == 2
end

@testitem "lll_gram_with_transform: Gram LLL + transform" begin
    # method: lll_gram_with_transform
    using Oscar
    G = ZZ[4 2; 2 4]
    L, T = lll_gram_with_transform(G)
    @test L == T * G * transpose(T)
end

@testitem "hnf: Hermite normal form" begin
    # method: hnf
    using Oscar
    X = ZZ[2 3; 4 5]
    H = hnf(X)
    @test nrows(H) == 2
    # HNF is upper triangular
    @test H[2, 1] == 0
end

@testitem "hnf_with_transform: HNF + transformation matrix" begin
    # method: hnf_with_transform
    using Oscar
    X = ZZ[2 3; 4 5]
    H, U = hnf_with_transform(X)
    @test H == U * X
end

@testitem "snf: Smith normal form" begin
    # method: snf
    using Oscar
    X = ZZ[2 4; 6 8]
    D = snf(X)
    @test nrows(D) == 2
    # SNF is diagonal
    @test D[1, 2] == 0
    @test D[2, 1] == 0
    # Invariant factors divide
    @test mod(D[2, 2], D[1, 1]) == 0
end

@testitem "snf_with_transform: SNF + transformation matrices" begin
    # method: snf_with_transform
    using Oscar
    X = ZZ[2 4; 6 8]
    D, U, V = snf_with_transform(X)
    @test D == U * X * V
end

@testitem "coverage guard: Nemo ZZMatrix methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    sample = ZZ[2 1; 1 2]
    assert_runtime_methods_covered(
        @__FILE__, sample;
        module_prefixes = ["Nemo", "AbstractAlgebra"],
    )
end
