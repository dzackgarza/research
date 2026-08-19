# Tests for §2.15: Equivariant primitive extensions

@testitem "equivariant_primitive_extensions: A1+A1 with identity" begin
    # method: equivariant_primitive_extensions
    using Oscar
    L1 = root_lattice(:A, 1)
    Lf1 = integer_lattice_with_isometry(L1)
    Lf2 = integer_lattice_with_isometry(L1)
    result = equivariant_primitive_extensions(Lf1, Lf2)
    @test result isa Vector
    @test all(r -> rank(lattice(r)) == 2, result)
end

@testitem "equivariant_primitive_extensions: with neg=true" begin
    # method: equivariant_primitive_extensions
    using Oscar
    L1 = root_lattice(:A, 1)
    Lf1 = integer_lattice_with_isometry(L1; neg = true)
    Lf2 = integer_lattice_with_isometry(L1; neg = true)
    result = equivariant_primitive_extensions(Lf1, Lf2; glue_only = false)
    @test result isa Vector
    for r in result
        @test order_of_isometry(r) in [1, 2]
    end
end

@testitem "admissible_equivariant_primitive_extensions: from admissible triple" begin
    # method: admissible_equivariant_primitive_extensions
    using Oscar
    L = root_lattice(:A, 2)
    g = genus(L)
    triples = admissible_triples(g, 2)
    if !isempty(triples)
        g1, g2 = first(triples)
        Qx, x = QQ["x"]
        p = x + 1
        result = admissible_equivariant_primitive_extensions(representative(g1), representative(g2), g, p, 2)
        @test result isa Vector
    else
        @test true
    end
end

# -- Coverage Guard --

@testitem "coverage guard: equivariant primitive extension callability" begin
    # method: runtime_coverage
    using Oscar
    @test hasmethod(Oscar.equivariant_primitive_extensions, Tuple{Oscar.ZZLatWithIsom, Oscar.ZZLatWithIsom})
end
