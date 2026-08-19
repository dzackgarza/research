import os
import sys

import pytest
from conftest import assert_equal, covered_methods_from_module

os.environ.setdefault("HOME", "/tmp/sage-home")
os.environ.setdefault("PYTHON_JULIAPKG_PROJECT", "/tmp/sage-home/julia_env")
os.environ.setdefault("JULIA_DEPOT_PATH", "/tmp/sage-home/.julia")

from juliacall import Main as jl


@pytest.fixture(scope="session", autouse=True)
def _init_julia_oscar() -> None:
    jl.seval("using Pkg")
    jl.seval('Pkg.activate("tests/julia_doc")')
    jl.seval("using Nemo")
    jl.seval("using Hecke")


def _jl_true(expr: str) -> bool:
    return bool(jl.seval(expr))


JULIA_BRIDGE_METHODS = {
    "integer_lattice",
    "lattice",
    "quadratic_lattice",
    "root_lattice",
    "hyperbolic_plane_lattice",
    "rescale",
    "lll",
    "dual",
    "discriminant_group",
    "basis_matrix",
    "ambient_space",
    "rational_span",
    "degree",
    "signature_tuple",
    "discriminant",
    "is_even",
    "is_unimodular",
    "is_positive_definite",
    "is_negative_definite",
    "is_primary_with_prime",
    "is_elementary_with_prime",
    "genus",
    "representative",
    "mass",
    "primes",
    "local_symbol",
    "quadratic_space",
    "rational_representative",
    "represents",
    "is_isometric",
    "is_rationally_isometric",
    "hasse_invariant",
    "witt_invariant",
    "automorphism_group_generators",
    "automorphism_group_order",
    "short_vectors",
    "shortest_vectors",
    "minimum",
    "kissing_number",
    "close_vectors",
    "direct_sum",
    "direct_product",
    "biproduct",
    "intersect",
    "is_sublattice",
    "is_primitive",
    "orthogonal_submodule",
    "lattice_in_same_ambient_space",
    "primitive_closure",
    "maximal_integral_lattice",
    "lll_with_transform",
    "lll_gram",
    "lll_gram_with_transform",
    "hnf",
    "hnf_with_transform",
    "snf",
    "snf_with_transform",
}


def test_julia_bridge_integer_lattice():
    """
    method: integer_lattice
    """
    actual = _jl_true("begin L = integer_lattice(gram = ZZ[2 1; 1 2]); rank(L) == 2 && gram_matrix(L) == ZZ[2 1; 1 2] end")
    assert_equal(actual, True, f"integer_lattice contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_lattice():
    """
    method: lattice
    """
    actual = _jl_true(
        "begin V = quadratic_space(QQ, QQ[2 1; 1 2]); L = lattice(V, identity_matrix(QQ, 2)); rank(L) == 2 end"
    )
    assert_equal(actual, True, f"lattice contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_quadratic_lattice():
    """
    method: quadratic_lattice
    """
    actual = _jl_true(
        "begin L = quadratic_lattice(QQ, identity_matrix(QQ, 2); gram = QQ[2 0; 0 2]); rank(L) == 2 && det(L) == 4 end"
    )
    assert_equal(actual, True, f"quadratic_lattice contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_root_lattice():
    """
    method: root_lattice
    """
    actual = _jl_true("begin L = root_lattice(:E, 8); rank(L) == 8 && abs(det(L)) == 1 && is_even(L) end")
    assert_equal(actual, True, f"root_lattice contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_hyperbolic_plane_lattice():
    """
    method: hyperbolic_plane_lattice
    """
    actual = tuple(jl.seval("Tuple(signature_tuple(hyperbolic_plane_lattice()))"))
    expected = (1, 0, 1)
    assert_equal(actual, expected, f"hyperbolic_plane_lattice signature mismatch: actual={actual}, expected={expected}")


def test_julia_bridge_rescale():
    """
    method: rescale
    """
    actual = _jl_true("begin L = integer_lattice(gram = ZZ[1 0; 0 1]); gram_matrix(rescale(L, 3)) == ZZ[3 0; 0 3] end")
    assert_equal(actual, True, f"rescale contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_lll():
    """
    method: lll
    """
    actual = _jl_true("begin L = root_lattice(:A, 3); M = lll(L); rank(M) == rank(L) && det(M) == det(L) end")
    assert_equal(actual, True, f"lll contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_dual():
    """
    method: dual
    """
    actual = _jl_true("begin L = integer_lattice(gram = ZZ[2;;]); D = dual(L); rank(D) == 1 && det(L) * det(D) == 1 end")
    assert_equal(actual, True, f"dual contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_discriminant_group():
    """
    method: discriminant_group
    """
    actual = _jl_true("begin L = root_lattice(:A, 2); T = discriminant_group(L); order(T) == 3 end")
    assert_equal(actual, True, f"discriminant_group contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_basis_matrix():
    """
    method: basis_matrix
    """
    actual = _jl_true("begin L = integer_lattice(gram = ZZ[2 0; 0 2]); nrows(basis_matrix(L)) == 2 && ncols(basis_matrix(L)) == 2 end")
    assert_equal(actual, True, f"basis_matrix contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_ambient_space():
    """
    method: ambient_space
    """
    actual = _jl_true("begin L = integer_lattice(gram = ZZ[2 1; 1 2]); rank(ambient_space(L)) == 2 end")
    assert_equal(actual, True, f"ambient_space contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_rational_span():
    """
    method: rational_span
    """
    actual = _jl_true("begin L = integer_lattice(gram = ZZ[2 1; 1 2]); rank(rational_span(L)) == 2 end")
    assert_equal(actual, True, f"rational_span contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_degree():
    """
    method: degree
    """
    actual = _jl_true("begin L = integer_lattice(gram = ZZ[2 1; 1 2]); degree(L) >= rank(L) end")
    assert_equal(actual, True, f"degree contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_signature_tuple():
    """
    method: signature_tuple
    """
    actual = tuple(jl.seval("Tuple(signature_tuple(root_lattice(:A, 2)))"))
    expected = (2, 0, 0)
    assert_equal(actual, expected, f"signature_tuple mismatch: actual={actual}, expected={expected}")


def test_julia_bridge_discriminant():
    """
    method: discriminant
    """
    actual = _jl_true("begin L = integer_lattice(gram = ZZ[2 1; 1 2]); discriminant(L) == -det(L) end")
    assert_equal(actual, True, f"discriminant contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_even():
    """
    method: is_even
    """
    actual = _jl_true("is_even(root_lattice(:E, 8))")
    assert_equal(actual, True, f"is_even mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_unimodular():
    """
    method: is_unimodular
    """
    actual = _jl_true("is_unimodular(root_lattice(:E, 8)) && !is_unimodular(root_lattice(:A, 2))")
    assert_equal(actual, True, f"is_unimodular mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_positive_definite():
    """
    method: is_positive_definite
    """
    actual = _jl_true("is_positive_definite(root_lattice(:A, 2))")
    assert_equal(actual, True, f"is_positive_definite mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_negative_definite():
    """
    method: is_negative_definite
    """
    actual = _jl_true("!is_negative_definite(root_lattice(:A, 2))")
    assert_equal(actual, True, f"is_negative_definite mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_primary_with_prime():
    """
    method: is_primary_with_prime
    """
    actual = _jl_true("is_primary_with_prime(root_lattice(:A, 2)) == (true, 3)")
    assert_equal(actual, True, f"is_primary_with_prime mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_elementary_with_prime():
    """
    method: is_elementary_with_prime
    """
    actual = _jl_true("is_elementary_with_prime(root_lattice(:A, 1)) == (true, 2)")
    assert_equal(actual, True, f"is_elementary_with_prime mismatch: actual={actual}, expected=True")


def test_julia_bridge_genus():
    """
    method: genus
    """
    actual = _jl_true("begin G = genus(root_lattice(:A, 2)); rank(G) == 2 && det(G) == 3 end")
    assert_equal(actual, True, f"genus contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_representative():
    """
    method: representative
    """
    actual = _jl_true("begin G = genus(root_lattice(:A, 2)); rank(representative(G)) == 2 end")
    assert_equal(actual, True, f"representative contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_mass():
    """
    method: mass
    """
    actual = _jl_true("begin G = genus(root_lattice(:A, 2)); mass(G) > 0 end")
    assert_equal(actual, True, f"mass contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_primes():
    """
    method: primes
    """
    actual = _jl_true("begin G = genus(root_lattice(:A, 2)); 3 in primes(G) end")
    assert_equal(actual, True, f"primes contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_local_symbol():
    """
    method: local_symbol
    """
    actual = _jl_true("begin G = genus(root_lattice(:A, 2)); prime(local_symbol(G, 3)) == 3 end")
    assert_equal(actual, True, f"local_symbol contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_quadratic_space():
    """
    method: quadratic_space
    """
    actual = _jl_true("begin G = genus(root_lattice(:A, 2)); rank(quadratic_space(G)) == 2 end")
    assert_equal(actual, True, f"quadratic_space contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_rational_representative():
    """
    method: rational_representative
    """
    actual = _jl_true("begin G = genus(root_lattice(:A, 2)); dim(Hecke.rational_representative(G)) == 2 end")
    assert_equal(actual, True, f"rational_representative contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_represents():
    """
    method: represents
    """
    actual = _jl_true("begin G1 = genus(root_lattice(:A, 2)); G2 = genus(root_lattice(:A, 1)); represents(G1, G2) end")
    assert_equal(actual, True, f"represents contract mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_isometric():
    """
    method: is_isometric
    """
    actual = _jl_true("is_isometric(root_lattice(:A, 2), root_lattice(:A, 2)) && !is_isometric(root_lattice(:A, 2), root_lattice(:A, 3))")
    assert_equal(actual, True, f"is_isometric mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_rationally_isometric():
    """
    method: is_rationally_isometric
    """
    actual = _jl_true("is_rationally_isometric(root_lattice(:A, 2), root_lattice(:A, 2))")
    assert_equal(actual, True, f"is_rationally_isometric mismatch: actual={actual}, expected=True")


def test_julia_bridge_hasse_invariant():
    """
    method: hasse_invariant
    """
    actual = _jl_true("begin q = quadratic_space(genus(root_lattice(:A, 2))); hasse_invariant(q, 2) in [1, -1] end")
    assert_equal(actual, True, f"hasse_invariant mismatch: actual={actual}, expected=True")


def test_julia_bridge_witt_invariant():
    """
    method: witt_invariant
    """
    actual = _jl_true("begin q = quadratic_space(genus(root_lattice(:A, 2))); witt_invariant(q, 2) in [1, -1] end")
    assert_equal(actual, True, f"witt_invariant mismatch: actual={actual}, expected=True")


def test_julia_bridge_automorphism_group_generators():
    """
    method: automorphism_group_generators
    """
    actual = _jl_true("begin L = root_lattice(:A, 2); length(automorphism_group_generators(L)) >= 1 end")
    assert_equal(actual, True, f"automorphism_group_generators mismatch: actual={actual}, expected=True")


def test_julia_bridge_automorphism_group_order():
    """
    method: automorphism_group_order
    """
    actual = _jl_true("automorphism_group_order(root_lattice(:A, 2)) == 12")
    assert_equal(actual, True, f"automorphism_group_order mismatch: actual={actual}, expected=True")


def test_julia_bridge_short_vectors():
    """
    method: short_vectors
    """
    actual = _jl_true("begin L = root_lattice(:A, 2); length(short_vectors(L, 2)) == 3 end")
    assert_equal(actual, True, f"short_vectors mismatch: actual={actual}, expected=True")


def test_julia_bridge_shortest_vectors():
    """
    method: shortest_vectors
    """
    actual = _jl_true("begin L = root_lattice(:A, 2); length(shortest_vectors(L)) == 3 end")
    assert_equal(actual, True, f"shortest_vectors mismatch: actual={actual}, expected=True")


def test_julia_bridge_minimum():
    """
    method: minimum
    """
    actual = _jl_true("minimum(root_lattice(:A, 2)) == 2")
    assert_equal(actual, True, f"minimum mismatch: actual={actual}, expected=True")


def test_julia_bridge_kissing_number():
    """
    method: kissing_number
    """
    actual = _jl_true("kissing_number(root_lattice(:A, 2)) == 6")
    assert_equal(actual, True, f"kissing_number mismatch: actual={actual}, expected=True")


def test_julia_bridge_close_vectors():
    """
    method: close_vectors
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); v = [ZZ(0), ZZ(0)]; cv = close_vectors(L, v, 0); length(cv) == 1 && cv[1][1] == v && cv[1][2] == 0 end"
    )
    assert_equal(actual, True, f"close_vectors mismatch: actual={actual}, expected=True")


def test_julia_bridge_direct_sum():
    """
    method: direct_sum
    """
    actual = _jl_true(
        "begin L1 = integer_lattice(gram = ZZ[2;;]); L2 = integer_lattice(gram = ZZ[4;;]); L = direct_sum(L1, L2)[1]; rank(L) == 2 && det(L) == 8 end"
    )
    assert_equal(actual, True, f"direct_sum mismatch: actual={actual}, expected=True")


def test_julia_bridge_direct_product():
    """
    method: direct_product
    """
    actual = _jl_true(
        "begin L1 = integer_lattice(gram = ZZ[2;;]); L2 = integer_lattice(gram = ZZ[4;;]); rank(direct_product(L1, L2)[1]) == 2 end"
    )
    assert_equal(actual, True, f"direct_product mismatch: actual={actual}, expected=True")


def test_julia_bridge_biproduct():
    """
    method: biproduct
    """
    actual = _jl_true(
        "begin L1 = integer_lattice(gram = ZZ[2;;]); L2 = integer_lattice(gram = ZZ[4;;]); rank(biproduct(L1, L2)[1]) == 2 end"
    )
    assert_equal(actual, True, f"biproduct mismatch: actual={actual}, expected=True")


def test_julia_bridge_intersect():
    """
    method: intersect
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); rank(intersect(L, M)) == 2 end"
    )
    assert_equal(actual, True, f"intersect mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_sublattice():
    """
    method: is_sublattice
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); is_sublattice(L, M) end"
    )
    assert_equal(actual, True, f"is_sublattice mismatch: actual={actual}, expected=True")


def test_julia_bridge_is_primitive():
    """
    method: is_primitive
    """
    actual = _jl_true(
        "begin L1 = integer_lattice(gram = ZZ[2;;]); L2 = integer_lattice(gram = ZZ[4;;]); ds = direct_sum(L1, L2); L = ds[1]; i1 = ds[2][1]; S = lattice_in_same_ambient_space(L, i1.matrix); is_primitive(L, S) end"
    )
    assert_equal(actual, True, f"is_primitive mismatch: actual={actual}, expected=True")


def test_julia_bridge_orthogonal_submodule():
    """
    method: orthogonal_submodule
    """
    actual = _jl_true(
        "begin L1 = integer_lattice(gram = ZZ[2;;]); L2 = integer_lattice(gram = ZZ[4;;]); ds = direct_sum(L1, L2); L = ds[1]; i1 = ds[2][1]; S = lattice_in_same_ambient_space(L, i1.matrix); rank(orthogonal_submodule(L, S)) == 1 end"
    )
    assert_equal(actual, True, f"orthogonal_submodule mismatch: actual={actual}, expected=True")


def test_julia_bridge_lattice_in_same_ambient_space():
    """
    method: lattice_in_same_ambient_space
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); rank(M) == 2 end"
    )
    assert_equal(actual, True, f"lattice_in_same_ambient_space mismatch: actual={actual}, expected=True")


def test_julia_bridge_primitive_closure():
    """
    method: primitive_closure
    """
    actual = _jl_true(
        "begin L = integer_lattice(gram = ZZ[1 0; 0 1]); M = lattice_in_same_ambient_space(L, 2 * basis_matrix(L)); P = primitive_closure(L, M); is_primitive(L, P) end"
    )
    assert_equal(actual, True, f"primitive_closure mismatch: actual={actual}, expected=True")


def test_julia_bridge_maximal_integral_lattice():
    """
    method: maximal_integral_lattice
    """
    actual = _jl_true("begin L = integer_lattice(gram = ZZ[2 0; 0 2]); rank(maximal_integral_lattice(L)) == rank(L) end")
    assert_equal(actual, True, f"maximal_integral_lattice mismatch: actual={actual}, expected=True")


def test_julia_bridge_lll_with_transform():
    """
    method: lll_with_transform
    """
    actual = _jl_true("begin B = ZZ[1 0; 1 2]; L, T = lll_with_transform(B); L == T * B end")
    assert_equal(actual, True, f"lll_with_transform mismatch: actual={actual}, expected=True")


def test_julia_bridge_lll_gram():
    """
    method: lll_gram
    """
    actual = _jl_true("begin G = ZZ[4 2; 2 4]; R = lll_gram(G); nrows(R) == 2 && ncols(R) == 2 end")
    assert_equal(actual, True, f"lll_gram mismatch: actual={actual}, expected=True")


def test_julia_bridge_lll_gram_with_transform():
    """
    method: lll_gram_with_transform
    """
    actual = _jl_true("begin G = ZZ[4 2; 2 4]; R, T = lll_gram_with_transform(G); R == T * G * transpose(T) end")
    assert_equal(actual, True, f"lll_gram_with_transform mismatch: actual={actual}, expected=True")


def test_julia_bridge_hnf():
    """
    method: hnf
    """
    actual = _jl_true("begin X = ZZ[2 3; 4 5]; H = hnf(X); H[2, 1] == 0 end")
    assert_equal(actual, True, f"hnf mismatch: actual={actual}, expected=True")


def test_julia_bridge_hnf_with_transform():
    """
    method: hnf_with_transform
    """
    actual = _jl_true("begin X = ZZ[2 3; 4 5]; H, U = hnf_with_transform(X); H == U * X end")
    assert_equal(actual, True, f"hnf_with_transform mismatch: actual={actual}, expected=True")


def test_julia_bridge_snf():
    """
    method: snf
    """
    actual = _jl_true("begin X = ZZ[2 4; 6 8]; D = snf(X); D[1,2] == 0 && D[2,1] == 0 && mod(D[2,2], D[1,1]) == 0 end")
    assert_equal(actual, True, f"snf mismatch: actual={actual}, expected=True")


def test_julia_bridge_snf_with_transform():
    """
    method: snf_with_transform
    """
    actual = _jl_true("begin X = ZZ[2 4; 6 8]; D, U, V = snf_with_transform(X); D == U * X * V end")
    assert_equal(actual, True, f"snf_with_transform mismatch: actual={actual}, expected=True")


def test_julia_bridge_coverage():
    """
    method: runtime_coverage

    Coverage guard: every declared Julia bridge lattice method should have
    at least one explicit `method:`-tagged pytest in this module.
    """
    covered = covered_methods_from_module(sys.modules[__name__])
    missing = sorted(JULIA_BRIDGE_METHODS - covered)
    assert not missing, (
        "Coverage failure: uncovered Julia bridge methods found.\n"
        f"Declared methods: {sorted(JULIA_BRIDGE_METHODS)}\n"
        f"Covered methods: {sorted(covered)}\n"
        f"Missing methods: {missing}"
    )
