# Tests for §2.17: Isometry group actions on lattices

@testitem "is_isometry: identity is an isometry" begin
    # method: is_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = identity_matrix(ZZ, 2)
    @test is_isometry(L, f) == true
end

@testitem "is_isometry: non-isometry detected" begin
    # method: is_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = ZZ[2 0; 0 1]
    @test is_isometry(L, f) == false
end

@testitem "is_isometry: negation is an isometry" begin
    # method: is_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = -identity_matrix(ZZ, 2)
    @test is_isometry(L, f) == true
end

@testitem "saturation: primitive closure in lattice" begin
    # method: saturation
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    S = saturation(L, M)
    @test is_primitive(L, S) == true
end

@testitem "is_saturated_with_saturation: test and compute" begin
    # method: is_saturated_with_saturation
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    flag, S = is_saturated_with_saturation(L, M)
    @test flag == false
    @test is_primitive(L, S) == true
end

@testitem "coverage guard: isometry action methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    sample = integer_lattice(gram = ZZ[2 1; 1 2])
    assert_runtime_methods_covered(@__FILE__, sample)
end
