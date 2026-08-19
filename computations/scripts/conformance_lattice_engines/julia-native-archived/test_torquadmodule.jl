# Tests for §2.11: Discriminant groups (TorQuadModule)

@testitem "torsion_quadratic_module: construct from cover and relations" begin
    # method: torsion_quadratic_module
    using Oscar
    L = root_lattice(:A, 2)
    D = dual(L)
    T = torsion_quadratic_module(D, L)
    @test order(T) == 3
end

@testitem "discriminant_group: A2 has order 3" begin
    # method: discriminant_group
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    @test order(T) == 3
end

@testitem "abelian_group: underlying abstract group" begin
    # method: abelian_group
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    A = abelian_group(T)
    @test order(A) == 3
end

@testitem "cover: cover lattice of TorQuadModule" begin
    # method: cover
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    C = cover(T)
    @test rank(C) == 2
end

@testitem "relations: relation lattice of TorQuadModule" begin
    # method: relations
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    R = relations(T)
    @test rank(R) == 2
end

@testitem "gram_matrix_bilinear: bilinear Gram over Q/Z" begin
    # method: gram_matrix_bilinear
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    G = gram_matrix_bilinear(T)
    @test nrows(G) > 0
end

@testitem "gram_matrix_quadratic: quadratic Gram over Q/2Z" begin
    # method: gram_matrix_quadratic
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    G = gram_matrix_quadratic(T)
    @test nrows(G) > 0
end

@testitem "modulus_bilinear_form: modulus of bilinear form" begin
    # method: modulus_bilinear_form
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    m = modulus_bilinear_form(T)
    @test m > 0
end

@testitem "modulus_quadratic_form: modulus of quadratic form" begin
    # method: modulus_quadratic_form
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    m = modulus_quadratic_form(T)
    @test m > 0
end

@testitem "is_degenerate: A2 discriminant group is non-degenerate" begin
    # method: is_degenerate
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    @test is_degenerate(T) == false
end

@testitem "is_semi_regular: A2 discriminant group" begin
    # method: is_semi_regular
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    @test is_semi_regular(T) == true
end

@testitem "radical_bilinear: radical of bilinear form" begin
    # method: radical_bilinear
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    R = radical_bilinear(T)
    @test order(R) == 1  # non-degenerate => trivial radical
end

@testitem "radical_quadratic: radical of quadratic form" begin
    # method: radical_quadratic
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    R = radical_quadratic(T)
    @test order(R) == 1
end

@testitem "normal_form: normal form of TorQuadModule" begin
    # method: normal_form
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    N = normal_form(T)
    @test order(N) == 3
end

@testitem "brown_invariant: mod 8 invariant" begin
    # method: brown_invariant
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    b = brown_invariant(T)
    @test 0 <= b <= 7
end

@testitem "snf: Smith normal form of TorQuadModule" begin
    # method: snf
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    S = snf(T)
    @test order(S) == 3
end

@testitem "is_snf: check if already in SNF" begin
    # method: is_snf
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    S = snf(T)
    @test is_snf(S) == true
end

@testitem "rescale: rescaled TorQuadModule" begin
    # method: rescale(T, k)
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    T2 = rescale(T, 2)
    @test order(T2) == order(T)
end

@testitem "genus: genus from discriminant form and signature" begin
    # method: genus(T, sig_pair)
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    G = genus(T, (2, 0))
    @test rank(G) == 2
end

@testitem "is_genus: check genus existence" begin
    # method: is_genus
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    @test is_genus(T, (2, 0)) == true
end

@testitem "direct_sum: TorQuadModule direct sum" begin
    # method: direct_sum(T1, T2)
    using Oscar
    L1 = root_lattice(:A, 1)
    L2 = root_lattice(:A, 2)
    T1 = discriminant_group(L1)
    T2 = discriminant_group(L2)
    T, _, _ = direct_sum(T1, T2)
    @test order(T) == 6
end

@testitem "is_isometric_with_isometry: TorQuadModule isometry test" begin
    # method: is_isometric_with_isometry(T, U)
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    U = discriminant_group(L)
    flag, f = is_isometric_with_isometry(T, U)
    @test flag == true
end

@testitem "is_anti_isometric_with_anti_isometry: anti-isometry test" begin
    # method: is_anti_isometric_with_anti_isometry
    using Oscar
    L = root_lattice(:A, 2)
    T = discriminant_group(L)
    # rescale by -1 gives anti-isometric module
    U = rescale(T, -1)
    flag, f = is_anti_isometric_with_anti_isometry(T, U)
    @test flag == true
end

@testitem "submodules: enumerate submodules" begin
    # method: submodules
    using Oscar
    L = root_lattice(:A, 1)
    T = discriminant_group(L)
    subs = submodules(T)
    @test length(collect(subs)) >= 1
end

@testitem "coverage guard: TorQuadModule methods" begin
    # method: runtime_coverage
    using Oscar
    include("coverage_utils.jl")
    L = root_lattice(:A, 2)
    sample = discriminant_group(L)
    assert_runtime_methods_covered(@__FILE__, sample)
end
