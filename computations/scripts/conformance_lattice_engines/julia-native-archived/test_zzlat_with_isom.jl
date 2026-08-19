# Tests for §2.14: ZZLatWithIsom

# -- Construction (existing) --

@testitem "integer_lattice_with_isometry: pair with identity" begin
    # method: integer_lattice_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test rank(lattice(Lf)) == 2
    @test order_of_isometry(Lf) == 1
end

@testitem "integer_lattice_with_isometry: pair with negation" begin
    # method: integer_lattice_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    @test order_of_isometry(Lf) == 2
end

@testitem "integer_lattice_with_isometry: explicit isometry matrix" begin
    # method: integer_lattice_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    f = -identity_matrix(ZZ, 2)
    Lf = integer_lattice_with_isometry(L, f)
    @test isometry(Lf) == f
end

@testitem "lattice: extract ZZLat from ZZLatWithIsom" begin
    # method: lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test rank(lattice(Lf)) == 2
end

@testitem "isometry: ZZLatWithIsom isometry matrix" begin
    # method: isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test isometry(Lf) == identity_matrix(ZZ, 2)
end

@testitem "order_of_isometry: identity has order 1" begin
    # method: order_of_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test order_of_isometry(Lf) == 1
end

@testitem "characteristic_polynomial: ZZLatWithIsom" begin
    # method: characteristic_polynomial
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    p = characteristic_polynomial(Lf)
    @test degree(p) == 2
end

@testitem "minimal_polynomial: ZZLatWithIsom" begin
    # method: minimal_polynomial
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    p = minimal_polynomial(Lf)
    @test degree(p) >= 1
end

# -- Accessors (new) --

@testitem "ambient_isometry: isometry on ambient space preserves Gram" begin
    # method: ambient_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    f_amb = ambient_isometry(Lf)
    V = ambient_space(lattice(Lf))
    G_V = gram_matrix(V)
    @test f_amb' * G_V * f_amb == G_V
end

@testitem "ambient_space: returns QuadSpaceWithIsom" begin
    # method: ambient_space
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Vf = ambient_space(Lf)
    @test Vf isa Oscar.QuadSpaceWithIsom
    @test isometry(Vf) == ambient_isometry(Lf)
end

@testitem "lattice_in_same_ambient_space: sublattice shares ambient isometry" begin
    # method: lattice_in_same_ambient_space
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    B = basis_matrix(lattice(Lf))
    Sf = lattice_in_same_ambient_space(Lf, B)
    @test ambient_isometry(Sf) == ambient_isometry(Lf)
end

@testitem "rational_span: returns QuadSpaceWithIsom" begin
    # method: rational_span
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Vf = rational_span(Lf)
    @test Vf isa Oscar.QuadSpaceWithIsom
    @test rank(Vf) == rank(Lf)
end

@testitem "basis_matrix: matches underlying lattice" begin
    # method: basis_matrix
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test basis_matrix(Lf) == basis_matrix(lattice(Lf))
end

@testitem "==: equality of ZZLatWithIsom" begin
    # method: ==
    using Oscar
    L = root_lattice(:A, 2)
    Lf1 = integer_lattice_with_isometry(L)
    Lf2 = integer_lattice_with_isometry(L)
    Lf_neg = integer_lattice_with_isometry(L; neg = true)
    @test Lf1 == Lf2
    @test Lf1 != Lf_neg
end

# -- Delegated Attributes (new) --

@testitem "rank/degree: delegated to underlying lattice" begin
    # method: rank
    # method: degree
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test rank(Lf) == 2
    @test degree(Lf) == 2
end

@testitem "det/discriminant: A2 lattice" begin
    # method: det
    # method: discriminant
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test det(Lf) == 3
    @test discriminant(Lf) == (-1)^rank(Lf) * det(Lf)
end

@testitem "scale/norm: A2 lattice scale and norm" begin
    # method: scale
    # method: norm
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test scale(Lf) == 1
    @test norm(Lf) == 2
end

@testitem "minimum: A2 lattice minimum" begin
    # method: minimum
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test minimum(Lf) == 2
end

@testitem "genus: returns ZZGenus with matching rank and det" begin
    # method: genus
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    g = genus(Lf)
    @test rank(g) == 2
    @test det(g) == 3
end

@testitem "gram_matrix: matches underlying lattice" begin
    # method: gram_matrix
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test gram_matrix(Lf) == gram_matrix(lattice(Lf))
end

@testitem "signature_tuple: A2 is (2,0,0)" begin
    # method: signature_tuple
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test signature_tuple(Lf) == (2, 0, 0)
end

@testitem "is_integral/is_even: A2 is integral and even" begin
    # method: is_integral
    # method: is_even
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test is_integral(Lf)
    @test is_even(Lf)
end

@testitem "is_positive_definite/is_definite: A2 is positive definite" begin
    # method: is_positive_definite
    # method: is_definite
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test is_positive_definite(Lf)
    @test is_definite(Lf)
end

@testitem "is_unimodular: A2 is not unimodular, E8 is" begin
    # method: is_unimodular
    using Oscar
    L_A2 = root_lattice(:A, 2)
    Lf_A2 = integer_lattice_with_isometry(L_A2)
    @test !is_unimodular(Lf_A2)
    L_E8 = root_lattice(:E, 8)
    Lf_E8 = integer_lattice_with_isometry(L_E8)
    @test is_unimodular(Lf_E8)
end

@testitem "is_primary/is_elementary: A2 is 3-primary and 3-elementary" begin
    # method: is_primary
    # method: is_elementary
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test is_primary(Lf, 3)
    @test is_elementary(Lf, 3)
end

@testitem "is_primary_with_prime/is_elementary_with_prime: A2 returns (true, 3)" begin
    # method: is_primary_with_prime
    # method: is_elementary_with_prime
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    flag_p, p = is_primary_with_prime(Lf)
    @test flag_p == true
    @test p == 3
    flag_e, q = is_elementary_with_prime(Lf)
    @test flag_e == true
    @test q == 3
end

@testitem "is_negative_definite: A2 is not negative definite" begin
    # method: is_negative_definite
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    @test !is_negative_definite(Lf)
end

# -- Operations (existing) --

@testitem "^: raise isometry to power" begin
    # method: ^
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Lf2 = Lf^2
    @test order_of_isometry(Lf2) == 1
end

@testitem "direct_sum: equivariant direct sum" begin
    # method: direct_sum
    using Oscar
    L = root_lattice(:A, 1)
    Lf = integer_lattice_with_isometry(L)
    Mg = integer_lattice_with_isometry(L; neg = true)
    S, _, _ = direct_sum(Lf, Mg)
    @test rank(lattice(S)) == 2
end

@testitem "dual: dual with induced isometry" begin
    # method: dual
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    Df = dual(Lf)
    @test rank(lattice(Df)) == 2
end

@testitem "lll: LLL with isometry carried along" begin
    # method: lll
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    Mf = lll(Lf)
    @test rank(lattice(Mf)) == 2
end

@testitem "rescale: ZZLatWithIsom rescale" begin
    # method: rescale
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    Mf = rescale(Lf, 2)
    @test rank(lattice(Mf)) == 2
end

# -- Kernel Sublattices --

@testitem "invariant_lattice: fixed sublattice" begin
    # method: invariant_lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    I = invariant_lattice(Lf)
    @test rank(lattice(I)) == 2  # identity fixes everything
end

@testitem "coinvariant_lattice: orthogonal complement of fixed" begin
    # method: coinvariant_lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    C = coinvariant_lattice(Lf)
    @test rank(lattice(C)) == 0  # identity: coinvariant is trivial
end

@testitem "kernel_lattice: cyclotomic polynomial variant" begin
    # method: kernel_lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Qx, x = QQ["x"]
    p = x + 1  # cyclotomic_polynomial(2) = x + 1
    Kf = kernel_lattice(Lf, p)
    @test rank(lattice(Kf)) == 2  # negation: all vectors satisfy (f+1)v = 0
end

@testitem "kernel_lattice: integer index variant" begin
    # method: kernel_lattice
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    Kf = kernel_lattice(Lf, 2)
    @test rank(lattice(Kf)) == 2  # kernel of f^2 - 1 for negation
end

@testitem "invariant_coinvariant_pair: rank sum equals full rank" begin
    # method: invariant_coinvariant_pair
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    inv_f, coinv_f = invariant_coinvariant_pair(Lf)
    @test rank(lattice(inv_f)) + rank(lattice(coinv_f)) == rank(Lf)
end

@testitem "orthogonal_submodule: inner product with complement is zero" begin
    # method: orthogonal_submodule
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    B_sub = basis_matrix(lattice(Lf))[1:1, :]
    Sf = lattice_in_same_ambient_space(Lf, B_sub)
    Of = orthogonal_submodule(Lf, Sf)
    # verify orthogonality: every row of Of basis has zero inner product with B_sub
    G = gram_matrix(ambient_space(lattice(Lf)))
    B_orth = basis_matrix(lattice(Of))
    if nrows(B_orth) > 0 && nrows(B_sub) > 0
        prod = B_sub * G * B_orth'
        @test all(iszero, prod)
    else
        @test true  # trivial case
    end
end

# -- Type Classification (new) --

@testitem "type: type of lattice-with-isometry" begin
    # method: type
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    t = type(Lf)
    @test t isa Dict
end

@testitem "is_of_type: roundtrip with type(Lf)" begin
    # method: is_of_type
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    t = type(Lf)
    @test is_of_type(Lf, t)
end

@testitem "is_of_same_type: same vs different isometries" begin
    # method: is_of_same_type
    using Oscar
    L = root_lattice(:A, 2)
    Lf1 = integer_lattice_with_isometry(L; neg = true)
    Lf2 = integer_lattice_with_isometry(L; neg = true)
    Lf_id = integer_lattice_with_isometry(L)
    @test is_of_same_type(Lf1, Lf2)
    @test !is_of_same_type(Lf1, Lf_id)
end

@testitem "is_of_hermitian_type: A2 with negation" begin
    # method: is_of_hermitian_type
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    @test is_of_hermitian_type(Lf)
end

@testitem "hermitian_structure: roundtrip hermitian rank" begin
    # method: hermitian_structure
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    if is_of_hermitian_type(Lf)
        H = hermitian_structure(Lf)
        n = order_of_isometry(Lf)
        phi_n = Int(euler_phi(ZZ(n)))
        @test rank(H) == div(rank(Lf), phi_n)
    end
end

@testitem "trace_lattice_with_isometry: roundtrip from hermitian" begin
    # method: trace_lattice_with_isometry
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    if is_of_hermitian_type(Lf)
        H = hermitian_structure(Lf)
        Lf2 = trace_lattice_with_isometry(H)
        @test rank(Lf2) == rank(Lf)
    end
end

# -- Discriminant Group & Centralizer (new) --

@testitem "discriminant_group: ZZLatWithIsom discriminant group" begin
    # method: discriminant_group
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    T = discriminant_group(Lf)
    @test order(T) == 3
end

@testitem "discriminant_representation: returns homomorphism" begin
    # method: discriminant_representation
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    gens = automorphism_group_generators(lattice(Lf))
    G = matrix_group(gens)
    phi = discriminant_representation(lattice(Lf), G)
    @test phi isa Oscar.GAPGroupHomomorphism
end

@testitem "image_centralizer_in_Oq: returns group and homomorphism" begin
    # method: image_centralizer_in_Oq
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    G, _ = image_centralizer_in_Oq(Lf)
    @test order(G) >= 1
end

# -- Spinor Norm & Signatures (new) --

@testitem "signatures: returns Dict for A2 with negation" begin
    # method: signatures
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    sigs = signatures(Lf)
    @test sigs isa Dict
end

@testitem "rational_spinor_norm: well-defined for identity" begin
    # method: rational_spinor_norm
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L)
    s = rational_spinor_norm(Lf)
    @test s isa QQFieldElem
end

@testitem "is_hermitian: type dict check" begin
    # method: is_hermitian
    using Oscar
    L = root_lattice(:A, 2)
    Lf_neg = integer_lattice_with_isometry(L; neg = true)
    t = type(Lf_neg)
    @test Oscar.is_hermitian(t)
end

# -- Coverage Guard --

@testitem "coverage guard: ZZLatWithIsom methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    L = root_lattice(:A, 2)
    sample = integer_lattice_with_isometry(L)
    assert_runtime_methods_covered(@__FILE__, sample)
end
