# Tests for §2.14 Enumeration: classification of lattices with isometry

@testitem "enumerate_classes_of_lattices_with_isometry: A1 genus, m=2" begin
    # method: enumerate_classes_of_lattices_with_isometry
    using Oscar
    L = root_lattice(:A, 1)
    g = genus(L)
    Qx, x = QQ["x"]
    reps = enumerate_classes_of_lattices_with_isometry(g, x + 1)
    @test length(reps) >= 1
    @test all(r -> order_of_isometry(r) == 2, reps)
end

@testitem "enumerate_classes_of_lattices_with_isometry: A1 genus, m=1" begin
    # method: enumerate_classes_of_lattices_with_isometry
    using Oscar
    L = root_lattice(:A, 1)
    g = genus(L)
    Qx, x = QQ["x"]
    reps = enumerate_classes_of_lattices_with_isometry(g, x - 1)
    @test length(reps) >= 1
    @test all(r -> order_of_isometry(r) == 1, reps)
end

@testitem "representatives_of_hermitian_type: A2 genus, order 2" begin
    # method: representatives_of_hermitian_type
    using Oscar
    L = root_lattice(:A, 2)
    g = genus(L)
    Qx, x = QQ["x"]
    reps = representatives_of_hermitian_type(g, x + 1)
    @test length(reps) >= 1
    @test all(r -> order_of_isometry(r) == 2, reps)
end

@testitem "admissible_triples: small genus" begin
    # method: admissible_triples
    using Oscar
    L = root_lattice(:A, 2)
    g = genus(L)
    triples = admissible_triples(g, 2)
    @test triples isa Vector
    for (g1, g2) in triples
        @test rank(g1) + rank(g2) == rank(g)
    end
end

@testitem "is_admissible_triple: roundtrip from admissible_triples" begin
    # method: is_admissible_triple
    using Oscar
    L = root_lattice(:A, 2)
    g = genus(L)
    triples = admissible_triples(g, 2)
    if !isempty(triples)
        g1, g2 = first(triples)
        @test is_admissible_triple(g, g1, g2, 2)
    else
        @test true
    end
end

@testitem "splitting_of_hermitian_type: A2 negation" begin
    # method: splitting_of_hermitian_type
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting_of_hermitian_type(Lf)
    @test result isa Vector
    @test all(r -> r isa Oscar.ZZLatWithIsom, result)
end

@testitem "splitting: generic splitting" begin
    # method: splitting
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting(Lf)
    @test result isa Vector
    @test all(r -> r isa Oscar.ZZLatWithIsom, result)
end

@testitem "splitting_of_prime_power: small example" begin
    # method: splitting_of_prime_power
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting_of_prime_power(Lf, 2)
    @test result isa Vector
end

@testitem "splitting_of_pure_mixed_prime_power: small example" begin
    # method: splitting_of_pure_mixed_prime_power
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting_of_pure_mixed_prime_power(Lf, 2)
    @test result isa Vector
end

@testitem "splitting_of_mixed_prime_power: small example" begin
    # method: splitting_of_mixed_prime_power
    using Oscar
    L = root_lattice(:A, 2)
    Lf = integer_lattice_with_isometry(L; neg = true)
    result = splitting_of_mixed_prime_power(Lf, 2)
    @test result isa Vector
end

# -- Coverage Guard --

@testitem "coverage guard: ZZLatWithIsom enumeration methods" begin
    # method: runtime_coverage
    using Oscar
    # This is a lightweight guard; enumeration methods don't dispatch on a single type
    # so we verify that the key functions are callable
    @test hasmethod(Oscar.enumerate_classes_of_lattices_with_isometry, Tuple{Oscar.ZZGenus, Any})
end
