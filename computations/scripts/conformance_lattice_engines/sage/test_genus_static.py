from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.all import Genus, ZZ, matrix
from .conftest import assert_runtime_methods_covered


def test_genus_determinant_matches_input_gram_det():
    """
    method: determinant

    determinant() returns determinant of a representative Gram matrix.
    Assertion: Determinant equals det of the constructor matrix.
    """
    G = matrix(ZZ, [[2, 0], [0, 6]])
    g = Genus(G)
    actual = g.determinant()
    expected = G.det()
    assert actual == expected, f"Genus.determinant mismatch: actual={actual}, expected={expected}"


def test_genus_signature_pair_for_indefinite_example():
    """
    method: signature_pair

    signature_pair() returns (p,n) of any representative in the genus.
    Assertion: Indefinite diagonal input yields (1,1).
    """
    g = Genus(matrix(ZZ, [[2, 0], [0, -2]]))
    actual = g.signature_pair()
    expected = (1, 1)
    assert actual == expected, f"Genus.signature_pair mismatch: actual={actual}, expected={expected}"


def test_genus_representative_preserves_dimension():
    """
    method: representative

    representative() returns an integer Gram matrix in the genus.
    Assertion: Returned representative has the documented genus dimension.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    R = g.representative()
    actual = R.nrows()
    expected = g.dimension()
    assert actual == expected, (
        f"Genus.representative dimension mismatch: actual={actual}, expected={expected}"
    )


def test_genus_rank_alias_matches_dimension():
    """
    method: rank

    rank() is an alias for genus dimension.
    Assertion: rank equals dimension on the same genus.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    actual = g.rank()
    expected = g.dimension()
    assert actual == expected, f"Genus.rank mismatch: actual={actual}, expected={expected}"


def test_genus_local_symbols_nonempty_for_nonsingular_example():
    """
    method: local_symbols

    local_symbols() returns p-adic genus symbols at relevant primes.
    Assertion: Symbol list is nonempty for a nontrivial genus.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    actual = len(g.local_symbols()) > 0
    expected = True
    assert actual == expected, f"Genus.local_symbols mismatch: actual={actual}, expected={expected}"


def test_genus_signature_is_difference_of_signature_pair():
    """
    method: signature

    signature() equals p-n for signature_pair()=(p,n).
    Assertion: Equality holds on an indefinite genus example.
    """
    g = Genus(matrix(ZZ, [[2, 0], [0, -2]]))
    p, n = g.signature_pair()
    actual = g.signature()
    expected = p - n
    assert actual == expected, f"Genus.signature mismatch: actual={actual}, expected={expected}"


def test_genus_discriminant_form_cardinality_matches_abs_determinant():
    """
    method: discriminant_form

    discriminant_form() returns the finite discriminant module.
    Assertion: Cardinality equals absolute determinant in rank-1 example.
    """
    G = matrix(ZZ, [[2]])
    g = Genus(G)
    D = g.discriminant_form()
    actual = D.cardinality()
    expected = abs(G.det())
    assert actual == expected, (
        f"Genus.discriminant_form cardinality mismatch: actual={actual}, expected={expected}"
    )


def test_genus_direct_sum_dimension_adds():
    """
    method: direct_sum

    direct_sum(other) returns genus of orthogonal sum.
    Assertion: Dimension adds under direct sum.
    """
    g1 = Genus(matrix(ZZ, [[2]]))
    g2 = Genus(matrix(ZZ, [[4]]))
    gs = g1.direct_sum(g2)
    actual = gs.dimension()
    expected = g1.dimension() + g2.dimension()
    assert actual == expected, f"Genus.direct_sum dimension mismatch: actual={actual}, expected={expected}"


def test_genus_level_positive_integer():
    """
    method: level

    level() returns denominator of inverse Gram matrix representative.
    Assertion: Level is a positive integer.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    actual = g.level()
    expected = actual > 0
    assert expected, f"Genus.level positivity mismatch: actual={actual}, expected=>0"


def test_genus_dim_and_dimension_aliases_match_rank():
    """
    method: dim

    dim()/dimension()/rank() are alias accessors for genus dimension.
    Assertion: All alias values are equal.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    actual = (g.dim(), g.dimension(), g.rank())
    expected = (g.rank(), g.rank(), g.rank())
    assert actual == expected, f"Genus dim aliases mismatch: actual={actual}, expected={expected}"


def test_genus_det_alias_matches_determinant():
    """
    method: det

    det() aliases determinant() for genus determinant.
    Assertion: det equals determinant.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    actual = g.det()
    expected = g.determinant()
    assert actual == expected, f"Genus.det alias mismatch: actual={actual}, expected={expected}"


def test_genus_signature_pair_of_matrix_alias():
    """
    method: signature_pair_of_matrix

    signature_pair_of_matrix() aliases signature_pair().
    Assertion: Alias value equals primary method.
    """
    g = Genus(matrix(ZZ, [[2, 0], [0, -2]]))
    actual = g.signature_pair_of_matrix()
    expected = g.signature_pair()
    assert actual == expected, (
        f"Genus.signature_pair_of_matrix alias mismatch: actual={actual}, expected={expected}"
    )


def test_genus_scale_and_norm_are_positive():
    """
    method: scale

    scale() and norm() return positive integer invariants for positive lattices.
    Assertion: Both invariants are > 0.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    actual = (g.scale() > 0, g.norm() > 0)
    expected = (True, True)
    assert actual == expected, f"Genus.scale/norm positivity mismatch: actual={actual}, expected={expected}"


def test_genus_dimension_matches_representative_size():
    """
    method: dimension

    dimension() is the rank of representative Gram matrices in the genus.
    Assertion: dimension equals representative matrix row count.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    R = g.representative()
    actual = g.dimension()
    expected = R.nrows()
    assert actual == expected, f"Genus.dimension mismatch: actual={actual}, expected={expected}"


def test_genus_mass_positive_rational():
    """
    method: mass

    mass() is the Minkowski-Siegel mass of the genus.
    Assertion: Mass is a positive rational number.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    m = g.mass()
    actual = m > 0
    expected = True
    assert actual == expected, f"Genus.mass positivity mismatch: actual={m}, expected=>0"


def test_genus_norm_divides_scale_times_two():
    """
    method: norm

    norm() is a positive integer invariant related to value ideal.
    Assertion: norm is positive and divides 2*scale in this even example.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    n = g.norm()
    s = g.scale()
    actual = (n > 0, (2 * s) % n == 0)
    expected = (True, True)
    assert actual == expected, f"Genus.norm divisibility mismatch: actual={actual}, expected={expected}"


def test_genus_representatives_returns_nonempty_same_rank_matrices():
    """
    method: representatives

    representatives() returns explicit Gram representatives in the genus.
    Assertion: For this genus there is one representative, with matching dimension and local symbols.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    reps = g.representatives()
    actual = (
        len(reps),
        all(M.nrows() == g.dimension() for M in reps),
        all(Genus(M).local_symbols() == g.local_symbols() for M in reps),
    )
    expected = (1, True, True)
    assert actual == expected, f"Genus.representatives mismatch: actual={actual}, expected={expected}"


def test_genus_spinor_generators_nonempty_for_proper_and_improper():
    """
    method: spinor_generators

    spinor_generators(proper) returns generators for spinor kernel classes.
    Assertion: For this genus, proper and full generator lists coincide and equal [5].
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    sp_proper = g.spinor_generators(True)
    sp_all = g.spinor_generators(False)
    actual = (sp_proper, sp_all)
    expected = ([5], [5])
    assert actual == expected, (
        f"Genus.spinor_generators mismatch: actual={actual}, expected={expected}"
    )


def test_genus_is_even_true_for_even_diagonal():
    """
    method: is_even

    is_even() checks parity of norms in the genus.
    Assertion: Diagonal Gram [2,2] genus is even.
    """
    g = Genus(matrix(ZZ, [[2, 0], [0, 2]]))
    actual = g.is_even()
    expected = True
    assert actual == expected, f"Genus.is_even mismatch: actual={actual}, expected={expected}"


def test_genus_local_symbol_returns_prime_data():
    """
    method: local_symbol

    local_symbol(p) returns the p-adic local symbol.
    Assertion: local_symbol(2) matches the 2-adic entry in local_symbols().
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    sym = g.local_symbols()
    actual = g.local_symbol(2)
    expected = sym[0]
    assert actual == expected, f"Genus.local_symbol mismatch: actual={actual}, expected={expected}"


def test_genus_rational_representative_shape():
    """
    method: rational_representative

    rational_representative() gives a diagonal rational representative.
    Assertion: Matrix size matches genus dimension.
    """
    g = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    R = g.rational_representative()
    actual = (R.nrows(), R.ncols())
    expected = (g.dimension(), g.dimension())
    assert actual == expected, (
        f"Genus.rational_representative shape mismatch: actual={actual}, expected={expected}"
    )


def test_genus_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant Genus runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = Genus(matrix(ZZ, [[2, 1], [1, 2]]))
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.quadratic_forms.genera.genus",),
    )
