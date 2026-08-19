# Tests for §2.12: Hermitian lattices (HermLat / QuadLat)

@testitem "hermitian_lattice: construct over Gaussian integers" begin
    # method: hermitian_lattice
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    @test rank(L) == 2
end

@testitem "base_field: returns number field" begin
    # method: base_field
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    E = base_field(L)
    @test degree(E) == 2
end

@testitem "fixed_field: returns fixed field under involution" begin
    # method: fixed_field
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    F = fixed_field(L)
    @test degree(F) == 1  # QQ
end

@testitem "pseudo_matrix: returns pseudo-matrix representation" begin
    # method: pseudo_matrix
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    PM = pseudo_matrix(L)
    @test nrows(matrix(PM)) == 2
end

@testitem "is_positive_definite: PD hermitian lattice" begin
    # method: is_positive_definite
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    @test is_positive_definite(L) == true
end

@testitem "jordan_decomposition: at a prime" begin
    # method: jordan_decomposition
    using Oscar
    K, a = cyclotomic_field(4, "a")
    OK = maximal_order(K)
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    p = prime_decomposition(OK, 2)[1][1]
    J = jordan_decomposition(L, p)
    @test length(J) >= 1
end

@testitem "genus_representatives: hermitian genus" begin
    # method: genus_representatives
    using Oscar
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    L = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    reps = genus_representatives(L)
    @test length(reps) >= 1
end

@testitem "coverage guard: hermitian lattice methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    K, a = cyclotomic_field(4, "a")
    G = matrix(K, 2, 2, [1, 0, 0, 1])
    sample = hermitian_lattice(K, identity_matrix(K, 2); gram = G)
    assert_runtime_methods_covered(@__FILE__, sample)
end
