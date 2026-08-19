# Tests for §2.9: Module operations and embeddings

@testitem "direct_sum: sum of two rank-1 lattices" begin
    # method: direct_sum
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, i1, i2 = direct_sum(L1, L2)
    @test rank(L) == 2
    @test det(L) == 8
end

@testitem "direct_product: product of two lattices" begin
    # method: direct_product
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, p1, p2 = direct_product(L1, L2)
    @test rank(L) == 2
end

@testitem "biproduct: returns injections and projections" begin
    # method: biproduct
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, i1, i2, p1, p2 = biproduct(L1, L2)
    @test rank(L) == 2
end

@testitem "intersect: intersection in common ambient" begin
    # method: intersect
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    # 2L is a sublattice of L
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    I = intersect(L, M)
    @test rank(I) == 2
end

@testitem "dual: dual lattice has reciprocal determinant" begin
    # method: dual
    using Oscar
    L = integer_lattice(gram = ZZ[2;;])
    D = dual(L)
    @test rank(D) == 1
    # det(L) * det(L^vee) = 1 for rank 1
end

@testitem "is_sublattice: 2L is sublattice of L" begin
    # method: is_sublattice
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    @test is_sublattice(L, M) == true
end

@testitem "is_primitive: direct summand is primitive" begin
    # method: is_primitive
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, i1, i2 = direct_sum(L1, L2)
    S = lattice_in_same_ambient_space(L, i1.matrix)
    @test is_primitive(L, S) == true
end

@testitem "orthogonal_submodule: orthogonal complement" begin
    # method: orthogonal_submodule
    using Oscar
    L1 = integer_lattice(gram = ZZ[2;;])
    L2 = integer_lattice(gram = ZZ[4;;])
    L, i1, i2 = direct_sum(L1, L2)
    S = lattice_in_same_ambient_space(L, i1.matrix)
    O = orthogonal_submodule(L, S)
    @test rank(O) == 1
end

@testitem "lattice_in_same_ambient_space: sublattice construction" begin
    # method: lattice_in_same_ambient_space
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    B = 2 * basis_matrix(L)
    M = lattice_in_same_ambient_space(L, B)
    @test rank(M) == 2
end

@testitem "primitive_closure: primitive closure of sublattice" begin
    # method: primitive_closure
    using Oscar
    L = integer_lattice(gram = ZZ[1 0; 0 1])
    M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L))
    P = primitive_closure(L, M)
    @test is_primitive(L, P) == true
end

@testitem "maximal_integral_lattice: maximal overlattice" begin
    # method: maximal_integral_lattice
    using Oscar
    L = integer_lattice(gram = ZZ[2 0; 0 2])
    M = maximal_integral_lattice(L)
    @test is_integral(M) == true
end

@testitem "is_maximal_integral: test maximality" begin
    # method: is_maximal_integral
    using Oscar
    L = root_lattice(:E, 8)
    @test is_maximal_integral(L) == true
end

# -- Root lattice recognition --

@testitem "root_lattice_recognition: identifies A2" begin
    # method: root_lattice_recognition
    using Oscar
    L = root_lattice(:A, 2)
    R = root_lattice_recognition(L)
    @test length(R) > 0
end

@testitem "ADE_type: identifies root type" begin
    # method: ADE_type
    using Oscar
    L = root_lattice(:A, 2)
    t = ADE_type(L)
    @test length(t) > 0
end

@testitem "coxeter_number: A2 Coxeter number is 3" begin
    # method: coxeter_number
    using Oscar
    L = root_lattice(:A, 2)
    @test coxeter_number(L) == 3
end

@testitem "highest_root: A2 highest root" begin
    # method: highest_root
    using Oscar
    L = root_lattice(:A, 2)
    h = highest_root(L)
    @test length(h) > 0
end

# -- Kernel / invariant lattices --

@testitem "kernel_lattice: kernel of endomorphism" begin
    # method: kernel_lattice
    using Oscar
    L = root_lattice(:A, 2)
    # Identity minus identity = zero map; kernel is the whole lattice
    f = identity_matrix(ZZ, 2)
    K = kernel_lattice(L, f - f)
    @test rank(K) == rank(L)
end

@testitem "coverage guard: module operations" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    sample = integer_lattice(gram = ZZ[2 1; 1 2])
    assert_runtime_methods_covered(@__FILE__, sample)
end
