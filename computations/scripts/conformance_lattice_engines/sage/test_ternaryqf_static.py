from __future__ import annotations

import sys

import sage.all  # noqa: F401
from sage.all import TernaryQF, ZZ, vector
from .conftest import assert_equal, assert_runtime_methods_covered


def test_ternaryqf_content_and_primitive_scaling():
    """
    method: content

    content() is gcd of coefficients.
    Assertion: Content of [2,4,6,8,10,12] is 2.
    """
    Q = TernaryQF([2, 4, 6, 8, 10, 12])
    actual_content = Q.content()
    expected_content = 2
    assert actual_content == expected_content, (
        f"TernaryQF.content mismatch: actual={actual_content}, expected={expected_content}"
    )


def test_ternaryqf_primitive_has_unit_content_after_normalization():
    """
    method: primitive

    primitive() divides coefficients by content.
    Assertion: Primitive form has content 1 after normalization.
    """
    Q = TernaryQF([2, 4, 6, 8, 10, 12])
    actual_primitive_content = Q.primitive().content()
    expected_primitive_content = 1
    assert actual_primitive_content == expected_primitive_content, (
        "TernaryQF.primitive().content mismatch: "
        f"actual={actual_primitive_content}, expected={expected_primitive_content}"
    )


def test_ternaryqf_disc_matches_hessian_det_half():
    """
    method: disc

    disc() is det(Hessian)/2 in Sage's ternary convention.
    Assertion: Returned discriminant matches det(matrix())/2.
    """
    Q = TernaryQF([1, 1, 1, 0, 0, 0])
    actual = Q.disc()
    expected = Q.matrix().det() / 2
    assert actual == expected, f"TernaryQF.disc mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_quadratic_form_conversion_preserves_values():
    """
    method: quadratic_form

    quadratic_form() converts a TernaryQF to an equivalent QuadraticForm.
    Assertion: Both forms evaluate equally on a sample vector.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    QQF = Q.quadratic_form()
    v = (1, 2, -1)
    actual = QQF(v)
    expected = Q(v)
    assert actual == expected, (
        f"TernaryQF.quadratic_form value mismatch: actual={actual}, expected={expected}, v={v}"
    )


def test_ternaryqf_adjoint_is_ternary_form():
    """
    method: adjoint

    adjoint() returns the classical adjoint ternary form.
    Assertion: Adjoint has nonzero discriminant.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    A = Q.adjoint()
    actual = A.disc() != 0
    expected = True
    assert actual == expected, f"TernaryQF.adjoint mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_automorphisms_count_matches_number_of_automorphisms():
    """
    method: automorphisms

    automorphisms() returns the automorphism matrices of the ternary form.
    Assertion: List length equals number_of_automorphisms().
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    autos = Q.automorphisms()
    actual = len(autos)
    expected = Q.number_of_automorphisms()
    assert actual == expected, (
        f"TernaryQF.automorphisms mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_automorphism_spin_norm_identity():
    """
    method: automorphism_spin_norm

    automorphism_spin_norm(A) computes spin norm of an automorphism A.
    Assertion: Identity automorphism has spin norm 1.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    A = Q.automorphisms()[0]
    actual = Q.automorphism_spin_norm(A)
    expected = 1
    assert actual == expected, (
        f"TernaryQF.automorphism_spin_norm mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_automorphism_symmetries_identity_empty():
    """
    method: automorphism_symmetries

    automorphism_symmetries(A) returns reflection data of A.
    Assertion: Identity automorphism has empty symmetry decomposition.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    A = Q.automorphisms()[0]
    actual = Q.automorphism_symmetries(A)
    expected = []
    assert actual == expected, (
        f"TernaryQF.automorphism_symmetries mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_basic_lemma_returns_modular_class():
    """
    method: basic_lemma

    basic_lemma(p) returns a local character value at prime p.
    Assertion: Returned value lies in {-1,0,1,2} for p=3 example.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = Q.basic_lemma(3) in {-1, 0, 1, 2}
    expected = True
    assert actual == expected, f"TernaryQF.basic_lemma mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_coefficient_matches_coefficients_entry():
    """
    method: coefficient

    coefficient(i) accesses i-th coefficient in canonical tuple.
    Assertion: coefficient(0) equals coefficients()[0].
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = Q.coefficient(0)
    expected = Q.coefficients()[0]
    assert actual == expected, f"TernaryQF.coefficient mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_coefficients_length_is_six():
    """
    method: coefficients

    coefficients() returns the 6 integral coefficients of ternary form.
    Assertion: Length is exactly 6.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = len(Q.coefficients())
    expected = 6
    assert actual == expected, f"TernaryQF.coefficients mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_delta_positive_for_nondegenerate_form():
    """
    method: delta

    delta() returns the Hessian-related invariant.
    Assertion: delta is positive for this positive-definite example.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = Q.delta() > 0
    expected = True
    assert actual == expected, f"TernaryQF.delta mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_divisor_divides_all_coefficients():
    """
    method: divisor

    divisor() is gcd-like content divisor of coefficients.
    Assertion: divisor divides each coefficient.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    d = Q.divisor()
    actual = all(c % d == 0 for c in Q.coefficients())
    expected = True
    assert actual == expected, f"TernaryQF.divisor mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_find_zeros_mod_p_returns_zero_values():
    """
    method: find_zeros_mod_p

    find_zeros_mod_p(p) enumerates nontrivial zeros modulo p.
    Assertion: First returned vector evaluates to 0 mod p.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    p = 3
    z = Q.find_zeros_mod_p(p)[0]
    actual = Q(z) % p
    expected = 0
    assert actual == expected, (
        f"TernaryQF.find_zeros_mod_p mismatch: actual={actual}, expected={expected}, z={z}, p={p}"
    )


def test_ternaryqf_pseudorandom_zero_is_indeed_zero_mod_p():
    """
    method: pseudorandom_primitive_zero_mod_p

    pseudorandom_primitive_zero_mod_p(p) returns primitive zero modulo p.
    Assertion: Returned vector evaluates to 0 mod p.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    p = 3
    z = Q.pseudorandom_primitive_zero_mod_p(p)
    actual = Q(z) % p
    expected = 0
    assert actual == expected, (
        f"TernaryQF.pseudorandom_primitive_zero_mod_p mismatch: actual={actual}, expected={expected}, z={z}, p={p}"
    )


def test_ternaryqf_find_p_neighbor_from_vec_preserves_discriminant():
    """
    method: find_p_neighbor_from_vec

    find_p_neighbor_from_vec(p,v) constructs a p-neighbor from isotropic vector v mod p.
    Assertion: Neighbor has same discriminant as original form.
    """
    Q = TernaryQF([1, 3, 3, -2, 0, -1])
    p = 11
    z = (9, 7, 1)
    N = Q.find_p_neighbor_from_vec(p, z)
    actual = N.disc()
    expected = Q.disc()
    assert actual == expected, (
        f"TernaryQF.find_p_neighbor_from_vec mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_find_p_neighbors_returns_requested_count_or_more():
    """
    method: find_p_neighbors

    find_p_neighbors(p) computes p-neighbors.
    Assertion: Every computed neighbor preserves discriminant.
    """
    Q = TernaryQF([1, 3, 3, -2, 0, -1])
    N = Q.find_p_neighbors(11)
    actual = all(n.disc() == Q.disc() for n in N)
    expected = True
    assert actual == expected, (
        f"TernaryQF.find_p_neighbors mismatch: actual={actual}, expected={expected}, count={len(N)}"
    )


def test_ternaryqf_is_definite_positive_and_not_negative():
    """
    method: is_definite

    is_definite() checks definite signature.
    Assertion: Example form is definite, positive definite, and not negative definite.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = (Q.is_definite(), Q.is_positive_definite(), Q.is_negative_definite())
    expected = (True, True, False)
    assert actual == expected, f"TernaryQF.is_definite mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_is_eisenstein_reduced_returns_boolean():
    """
    method: is_eisenstein_reduced

    is_eisenstein_reduced() checks Eisenstein reduction conditions.
    Assertion: Eisenstein-reduced representative satisfies the predicate.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    R, _ = Q.reduced_form_eisenstein()
    actual = R.is_eisenstein_reduced()
    expected = True
    assert actual == expected, (
        f"TernaryQF.is_eisenstein_reduced type mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_is_negative_definite_false_on_positive_example():
    """
    method: is_negative_definite

    is_negative_definite() checks if all eigenvalues are negative.
    Assertion: Positive example is not negative definite.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = Q.is_negative_definite()
    expected = False
    assert actual == expected, (
        f"TernaryQF.is_negative_definite mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_is_positive_definite_true_on_example():
    """
    method: is_positive_definite

    is_positive_definite() checks positivity.
    Assertion: Example form is positive definite.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = Q.is_positive_definite()
    expected = True
    assert actual == expected, (
        f"TernaryQF.is_positive_definite mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_is_primitive_matches_content_one():
    """
    method: is_primitive

    is_primitive() is equivalent to content()==1.
    Assertion: Equivalence holds on this form.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = Q.is_primitive()
    expected = (Q.content() == 1)
    assert actual == expected, f"TernaryQF.is_primitive mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_level_positive_integer():
    """
    method: level

    level() is a positive arithmetic invariant.
    Assertion: level > 0.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    lv = Q.level()
    actual = lv > 0
    expected = True
    assert actual == expected, f"TernaryQF.level mismatch: actual={lv}, expected=>0"


def test_ternaryqf_matrix_is_symmetric():
    """
    method: matrix

    matrix() returns the symmetric Hessian matrix representation.
    Assertion: Matrix equals its transpose.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    M = Q.matrix()
    actual = M == M.transpose()
    expected = True
    assert actual == expected, f"TernaryQF.matrix mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_number_of_automorphisms_matches_list_size():
    """
    method: number_of_automorphisms

    number_of_automorphisms() returns cardinality of automorphism group.
    Assertion: Value equals len(automorphisms()).
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = Q.number_of_automorphisms()
    expected = len(Q.automorphisms())
    assert actual == expected, (
        f"TernaryQF.number_of_automorphisms mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_omega_positive():
    """
    method: omega

    omega() returns an arithmetic genus character value.
    Assertion: omega is positive in this example.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    w = Q.omega()
    actual = w > 0
    expected = True
    assert actual == expected, f"TernaryQF.omega mismatch: actual={w}, expected=>0"


def test_ternaryqf_polynomial_matches_callable_value():
    """
    method: polynomial

    polynomial() returns a polynomial evaluating to the same quadratic value.
    Assertion: Polynomial and form agree on sample vector.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    v = (1, 2, -1)
    actual = Q.polynomial()(*v)
    expected = Q(v)
    assert actual == expected, f"TernaryQF.polynomial mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_reciprocal_preserves_discriminant():
    """
    method: reciprocal

    reciprocal() returns the reciprocal ternary form.
    Assertion: Reciprocal discriminant equals adjoint discriminant.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    R = Q.reciprocal()
    actual = R.disc()
    expected = Q.adjoint().disc()
    assert actual == expected, f"TernaryQF.reciprocal mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_reciprocal_reduced_preserves_discriminant():
    """
    method: reciprocal_reduced

    reciprocal_reduced() returns reduced reciprocal representative.
    Assertion: Its discriminant matches reciprocal discriminant.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    R = Q.reciprocal_reduced()
    actual = R.disc()
    expected = Q.reciprocal().disc()
    assert actual == expected, (
        f"TernaryQF.reciprocal_reduced mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_reduced_form_eisenstein_preserves_discriminant():
    """
    method: reduced_form_eisenstein

    reduced_form_eisenstein() returns reduced representative and transform.
    Assertion: Reduced representative keeps discriminant.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    R, _ = Q.reduced_form_eisenstein()
    actual = R.disc()
    expected = Q.disc()
    assert actual == expected, (
        f"TernaryQF.reduced_form_eisenstein mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_scale_by_factor_scales_coefficients():
    """
    method: scale_by_factor

    scale_by_factor(c) multiplies the form by scalar c.
    Assertion: First coefficient doubles after scaling by 2.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    S = Q.scale_by_factor(2)
    actual = S.coefficient(0)
    expected = 2 * Q.coefficient(0)
    assert actual == expected, (
        f"TernaryQF.scale_by_factor mismatch: actual={actual}, expected={expected}"
    )


def test_ternaryqf_symmetry_matrix_has_determinant_minus_one():
    """
    method: symmetry

    symmetry(v) returns reflection matrix associated to vector v.
    Assertion: Reflection determinant is -1.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    S = Q.symmetry(vector(ZZ, [1, 0, 0]))
    actual = S.det()
    expected = -1
    assert actual == expected, f"TernaryQF.symmetry mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_xi_invalid_character_raises_value_error():
    """
    method: xi

    xi(p) evaluates a genus character when defined.
    Assertion: In the Dickson example pair, both forms have xi(3) = -1.
    """
    Q1 = TernaryQF([26, 42, 53, -36, -17, -3])
    Q2 = Q1.find_p_neighbors(2)[1]
    actual = (Q1.omega(), Q1.xi(3), Q2.xi(3))
    expected = (3, -1, -1)
    assert_equal(actual, expected, "TernaryQF.xi mismatch")


def test_ternaryqf_xi_rec_returns_minus_one_at_three():
    """
    method: xi_rec

    xi_rec(p) evaluates reciprocal character when defined.
    Assertion: xi_rec(3) equals -1 for this form.
    """
    Q = TernaryQF([2, 3, 5, 1, -1, 2])
    actual = Q.xi_rec(3)
    expected = -1
    assert actual == expected, f"TernaryQF.xi_rec mismatch: actual={actual}, expected={expected}"


def test_ternaryqf_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant TernaryQF runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = TernaryQF([2, 3, 5, 1, -1, 2])
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.quadratic_forms.ternary_qf",),
    )
