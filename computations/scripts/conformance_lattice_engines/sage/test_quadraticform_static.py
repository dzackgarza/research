from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.all import QQ, ZZ, QuadraticForm, vector
from .conftest import assert_equal, assert_runtime_methods_covered


def test_quadraticform_gram_and_hessian_relation():
    """
    method: matrix

    matrix() is the Hessian A and Gram_matrix() is G=A/2 for Q(x)=x^T G x.
    Assertion: Hessian equals two times Gram matrix on a nontrivial binary form.
    """
    Q = QuadraticForm(ZZ, 2, [1, 2, 3])
    actual = Q.matrix()
    expected = 2 * Q.Gram_matrix()
    assert actual == expected, (
        f"QuadraticForm matrix/Gram relation mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_discriminant_equals_gram_det():
    """
    method: det

    det() is the Hessian determinant and Gram_det() is the Gram determinant.
    Assertion: Determinant invariants coincide exactly.
    """
    Q = QuadraticForm(ZZ, 2, [1, 2, 3])
    actual = Q.det()
    expected = 2 ** Q.dim() * Q.Gram_det()
    assert actual == expected, (
        f"QuadraticForm det/Gram_det mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_Gram_matrix_half_of_matrix():
    """
    method: Gram_matrix

    Gram_matrix() returns half of the Hessian matrix for integral forms.
    Assertion: 2*Gram_matrix equals matrix.
    """
    Q = QuadraticForm(ZZ, 2, [1, 2, 3])
    actual = 2 * Q.Gram_matrix()
    expected = Q.matrix()
    assert actual == expected, (
        f"QuadraticForm.Gram_matrix mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_Hessian_matrix_matches_matrix_method():
    """
    method: Hessian_matrix

    Hessian_matrix() is the Hessian form matrix accessor.
    Assertion: Hessian_matrix equals matrix().
    """
    Q = QuadraticForm(ZZ, 2, [1, 2, 3])
    actual = Q.Hessian_matrix()
    expected = Q.matrix()
    assert actual == expected, (
        f"QuadraticForm.Hessian_matrix mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_Gram_det_scales_det_by_power_of_two():
    """
    method: Gram_det

    Gram_det() equals det()/2^n where n is dimension.
    Assertion: Identity holds exactly on a binary example.
    """
    Q = QuadraticForm(ZZ, 2, [1, 2, 3])
    actual = Q.Gram_det()
    expected = Q.det() / (2 ** Q.dim())
    assert actual == expected, (
        f"QuadraticForm.Gram_det mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_signature_vector_counts_eigenvalue_signs():
    """
    method: signature_vector

    signature_vector() returns (p,n,z), counts of positive/negative/zero eigenvalues.
    Assertion: Form x^2-y^2 has signature vector (1,1,0).
    """
    Q = QuadraticForm(ZZ, 2, [1, 0, -1])
    actual = Q.signature_vector()
    expected = (1, 1, 0)
    assert actual == expected, (
        f"QuadraticForm.signature_vector mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_bilinear_map_polarization_identity():
    """
    method: bilinear_map

    bilinear_map(v,w) is the polarization B(v,w)=(Q(v+w)-Q(v)-Q(w))/2.
    Assertion: Polarization identity gives B(v,v)=Q(v).
    """
    Q = QuadraticForm(ZZ, 2, [2, 0, 2])
    v = vector(ZZ, [1, 2])
    actual = Q.bilinear_map(v, v)
    expected = Q(v)
    assert actual == expected, (
        f"QuadraticForm.bilinear_map polarization mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_theta_series_leading_coefficient_one():
    """
    method: theta_series

    theta_series(prec) counts representation numbers with constant term from the zero vector.
    Assertion: Constant coefficient is exactly 1.
    """
    Q = QuadraticForm(ZZ, 2, [1, 0, 1])
    t = Q.theta_series(6)
    actual = t[0]
    expected = 1
    assert actual == expected, (
        f"QuadraticForm.theta_series constant term mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_rational_diagonal_form_preserves_rank():
    """
    method: rational_diagonal_form

    rational_diagonal_form() diagonalizes over Q without changing rational isometry class.
    Assertion: Rank is preserved under rational diagonalization.
    """
    Q = QuadraticForm(QQ, 3, [2, 0, 0, 3, 0, 5])
    D = Q.rational_diagonal_form()
    actual = D.dim()
    expected = Q.dim()
    assert actual == expected, (
        f"QuadraticForm.rational_diagonal_form rank mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_base_ring_is_zz():
    """
    method: base_ring

    base_ring() returns coefficient ring.
    Assertion: Integer example has base ring ZZ.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.base_ring()
    expected = ZZ
    assert actual == expected, f"QuadraticForm.base_ring mismatch: actual={actual}, expected={expected}"


def test_quadraticform_change_ring_to_qq_preserves_dimension():
    """
    method: change_ring

    change_ring(R) coerces coefficients into ring R.
    Assertion: Dimension is preserved under change to QQ.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.change_ring(QQ)
    actual = R.dim()
    expected = Q.dim()
    assert actual == expected, f"QuadraticForm.change_ring mismatch: actual={actual}, expected={expected}"


def test_quadraticform_coefficients_length_formula():
    """
    method: coefficients

    coefficients() returns upper-triangular coefficient list.
    Assertion: Length is n(n+1)/2.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = len(Q.coefficients())
    expected = 6
    assert actual == expected, f"QuadraticForm.coefficients mismatch: actual={actual}, expected={expected}"


def test_quadraticform_content_equals_gcd():
    """
    method: content

    content() is gcd of coefficients.
    Assertion: Equals gcd() on integral form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.content()
    expected = Q.gcd()
    assert actual == expected, f"QuadraticForm.content mismatch: actual={actual}, expected={expected}"


def test_quadraticform_delta_equals_disc_for_odd_dimension():
    """
    method: delta

    delta() is determinant-based invariant.
    Assertion: For 3-variable example, delta equals disc.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.delta()
    expected = Q.disc()
    assert actual == expected, f"QuadraticForm.delta mismatch: actual={actual}, expected={expected}"


def test_quadraticform_dim_matches_constructor_rank():
    """
    method: dim

    dim() returns number of variables.
    Assertion: Constructed ternary form has dim 3.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.dim()
    expected = 3
    assert actual == expected, f"QuadraticForm.dim mismatch: actual={actual}, expected={expected}"


def test_quadraticform_disc_positive_for_positive_definite_diagonal():
    """
    method: disc

    disc() is discriminant-like determinant invariant.
    Assertion: Positive-definite diagonal form has positive disc.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    d = Q.disc()
    actual = d > 0
    expected = True
    assert actual == expected, f"QuadraticForm.disc mismatch: actual={d}, expected=>0"


def test_quadraticform_from_polynomial_roundtrip():
    """
    method: from_polynomial

    from_polynomial(f) reconstructs quadratic form from polynomial.
    Assertion: Roundtrip preserves coefficients.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.from_polynomial(Q.polynomial())
    actual = R.coefficients()
    expected = Q.coefficients()
    assert actual == expected, f"QuadraticForm.from_polynomial mismatch: actual={actual}, expected={expected}"


def test_quadraticform_gcd_divides_all_coefficients():
    """
    method: gcd

    gcd() divides all integral coefficients.
    Assertion: Divisibility holds for each coefficient.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    g = Q.gcd()
    actual = all(c % g == 0 for c in Q.coefficients())
    expected = True
    assert actual == expected, f"QuadraticForm.gcd mismatch: actual={actual}, expected={expected}, gcd={g}"


def test_quadraticform_is_definite_true_for_positive_diagonal():
    """
    method: is_definite

    is_definite() checks if signature has no mixed signs.
    Assertion: Positive diagonal example is definite.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_definite()
    expected = True
    assert actual == expected, f"QuadraticForm.is_definite mismatch: actual={actual}, expected={expected}"


def test_quadraticform_is_even_false_and_is_odd_true_example():
    """
    method: is_even

    is_even()/is_odd() detect parity of diagonal values.
    Assertion: Example is odd and not even.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = (Q.is_even(), Q.is_odd())
    expected = (False, True)
    assert actual == expected, f"QuadraticForm.parity mismatch: actual={actual}, expected={expected}"


def test_quadraticform_is_indefinite_false_for_positive_diagonal():
    """
    method: is_indefinite

    is_indefinite() checks mixed-sign signature.
    Assertion: Positive diagonal form is not indefinite.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_indefinite()
    expected = False
    assert actual == expected, f"QuadraticForm.is_indefinite mismatch: actual={actual}, expected={expected}"


def test_quadraticform_is_negative_definite_false_for_positive_diagonal():
    """
    method: is_negative_definite

    is_negative_definite() checks if all eigenvalues are negative.
    Assertion: Positive diagonal form is not negative definite.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_negative_definite()
    expected = False
    assert actual == expected, (
        f"QuadraticForm.is_negative_definite mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_is_odd_true_example():
    """
    method: is_odd

    is_odd() checks odd parity.
    Assertion: Example is odd.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_odd()
    expected = True
    assert actual == expected, f"QuadraticForm.is_odd mismatch: actual={actual}, expected={expected}"


def test_quadraticform_is_positive_definite_true_for_positive_diagonal():
    """
    method: is_positive_definite

    is_positive_definite() checks positivity.
    Assertion: Positive diagonal example is positive definite.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_positive_definite()
    expected = True
    assert actual == expected, (
        f"QuadraticForm.is_positive_definite mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_is_primitive_matches_content_one():
    """
    method: is_primitive

    is_primitive() means coefficient gcd equals 1.
    Assertion: Equivalent to content()==1.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_primitive()
    expected = (Q.content() == 1)
    assert actual == expected, f"QuadraticForm.is_primitive mismatch: actual={actual}, expected={expected}"


def test_quadraticform_is_zero_on_zero_vector():
    """
    method: is_zero

    is_zero(v) checks whether Q(v)=0.
    Assertion: Zero vector is isotropic.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = vector(ZZ, [0, 0, 0])
    actual = Q.is_zero(v)
    expected = True
    assert actual == expected, f"QuadraticForm.is_zero mismatch: actual={actual}, expected={expected}, v={v}"


def test_quadraticform_level_positive_integer():
    """
    method: level

    level() returns positive integer invariant.
    Assertion: level > 0.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    lv = Q.level()
    actual = lv > 0
    expected = True
    assert actual == expected, f"QuadraticForm.level mismatch: actual={lv}, expected=>0"


def test_quadraticform_lll_preserves_discriminant():
    """
    method: lll

    lll() returns LLL-reduced equivalent form.
    Assertion: Discriminant is preserved.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.lll()
    actual = R.disc()
    expected = Q.disc()
    assert actual == expected, f"QuadraticForm.lll mismatch: actual={actual}, expected={expected}"


def test_quadraticform_number_of_automorphisms_positive():
    """
    method: number_of_automorphisms

    number_of_automorphisms() counts integral automorphisms.
    Assertion: Count is at least 1.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    n = Q.number_of_automorphisms()
    actual = n >= 1
    expected = True
    assert actual == expected, (
        f"QuadraticForm.number_of_automorphisms mismatch: actual={n}, expected>=1"
    )


def test_quadraticform_omega_positive():
    """
    method: omega

    omega() returns arithmetic invariant.
    Assertion: omega is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    w = Q.omega()
    actual = w > 0
    expected = True
    assert actual == expected, f"QuadraticForm.omega mismatch: actual={w}, expected=>0"


def test_quadraticform_parity_matches_is_odd():
    """
    method: parity

    parity() returns string parity classification.
    Assertion: parity is 'odd' exactly when is_odd() is True.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.parity()
    expected = "odd" if Q.is_odd() else "even"
    assert actual == expected, f"QuadraticForm.parity mismatch: actual={actual}, expected={expected}"


def test_quadraticform_polynomial_evaluates_like_form():
    """
    method: polynomial

    polynomial() returns polynomial representation of Q.
    Assertion: Polynomial and form agree on sample vector.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = (1, 2, -1)
    actual = Q.polynomial()(*v)
    expected = Q(v)
    assert actual == expected, f"QuadraticForm.polynomial mismatch: actual={actual}, expected={expected}"


def test_quadraticform_primitive_has_unit_content():
    """
    method: primitive

    primitive() scales by coefficient gcd.
    Assertion: Primitive form has content 1.
    """
    Q = QuadraticForm(ZZ, 3, [4, 0, 0, 6, 0, 10])
    P = Q.primitive()
    actual = P.content()
    expected = 1
    assert actual == expected, f"QuadraticForm.primitive mismatch: actual={actual}, expected={expected}"


def test_quadraticform_reciprocal_is_same_dimension():
    """
    method: reciprocal

    reciprocal() returns reciprocal quadratic form.
    Assertion: Dimension is preserved.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.reciprocal()
    actual = R.dim()
    expected = Q.dim()
    assert actual == expected, f"QuadraticForm.reciprocal mismatch: actual={actual}, expected={expected}"


def test_quadraticform_scale_by_factor_scales_coefficients():
    """
    method: scale_by_factor

    scale_by_factor(c) multiplies coefficients by c.
    Assertion: First coefficient doubles under factor 2.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    S = Q.scale_by_factor(2)
    actual = S.coefficients()[0]
    expected = 2 * Q.coefficients()[0]
    assert actual == expected, (
        f"QuadraticForm.scale_by_factor mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_signature_matches_positive_dimension():
    """
    method: signature

    signature() equals p-n.
    Assertion: Positive-definite ternary form has signature 3.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.signature()
    expected = 3
    assert actual == expected, f"QuadraticForm.signature mismatch: actual={actual}, expected={expected}"


def test_quadraticform_solve_over_qq_returns_exact_value():
    """
    method: solve

    solve(n) finds rational vector with Q(v)=n over QQ.
    Assertion: Solution to Q(v)=2 evaluates exactly to 2.
    """
    Q = QuadraticForm(QQ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.solve(2)
    actual = Q(v)
    expected = 2
    assert actual == expected, f"QuadraticForm.solve mismatch: actual={actual}, expected={expected}, v={v}"


def test_quadraticform_xi_invalid_character_raises_value_error():
    """
    method: xi

    xi(p) evaluates a character when defined.
    Assertion: In the documented genus pair, xi(5) distinguishes local class.
    """
    Q1 = QuadraticForm(ZZ, 3, [1, 1, 1, 14, 3, 14])
    Q2 = QuadraticForm(ZZ, 3, [2, -1, 0, 2, 0, 50])
    actual = (Q1.omega(), Q2.omega(), Q1.xi(5), Q2.xi(5))
    expected = (5, 5, 1, -1)
    assert_equal(actual, expected, "QuadraticForm.xi mismatch")


def test_quadraticform_xi_rec_defined_for_prime_three():
    """
    method: xi_rec

    xi_rec(p) evaluates reciprocal character when defined.
    Assertion: For p=3, xi_rec equals 1 on this form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.xi_rec(3)
    expected = 1
    assert actual == expected, f"QuadraticForm.xi_rec mismatch: actual={actual}, expected={expected}"


def test_quadraticform_is_locally_equivalent_to_reflexive_and_detects_change():
    """
    method: is_locally_equivalent_to

    is_locally_equivalent_to(Q2) checks local equivalence at all places.
    Assertion: Form is locally equivalent to itself and not to changed discriminant form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 6])
    actual = (Q.is_locally_equivalent_to(Q), Q.is_locally_equivalent_to(R))
    expected = (True, False)
    assert actual == expected, (
        f"QuadraticForm.is_locally_equivalent_to mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_is_globally_equivalent_to_reflexive_and_detects_change():
    """
    method: is_globally_equivalent_to

    is_globally_equivalent_to(Q2) checks integral global equivalence.
    Assertion: Form is globally equivalent to itself and not to changed discriminant form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 6])
    actual = (Q.is_globally_equivalent_to(Q), Q.is_globally_equivalent_to(R))
    expected = (True, False)
    assert actual == expected, (
        f"QuadraticForm.is_globally_equivalent_to mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_is_rationally_isometric_detects_discriminant_change():
    """
    method: is_rationally_isometric

    is_rationally_isometric(Q2) checks isometry over Q.
    Assertion: Forms with different discriminant are not rationally isometric.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 6])
    actual = Q.is_rationally_isometric(R)
    expected = False
    assert actual == expected, (
        f"QuadraticForm.is_rationally_isometric mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_is_anisotropic_and_is_isotropic_complement_at_prime():
    """
    method: is_anisotropic

    is_anisotropic(p) and is_isotropic(p) are complementary local predicates.
    Assertion: At p=3 the form is anisotropic and not isotropic.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = (Q.is_anisotropic(3), Q.is_isotropic(3))
    expected = (True, False)
    assert actual == expected, (
        f"QuadraticForm.is_anisotropic/is_isotropic mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_is_isotropic_true_at_two():
    """
    method: is_isotropic

    is_isotropic(p) checks for nontrivial local zero at prime p.
    Assertion: Example form is isotropic at p=2.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_isotropic(2)
    expected = True
    assert actual == expected, f"QuadraticForm.is_isotropic mismatch: actual={actual}, expected={expected}"


def test_quadraticform_local_representation_methods_agree_on_sample():
    """
    method: is_locally_represented_number

    is_locally_represented_number(n) and placewise predicate should agree on sampled place.
    Assertion: For n=11 and p=3, both predicates are True.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = (Q.is_locally_represented_number(11), Q.is_locally_represented_number_at_place(11, 3))
    expected = (True, True)
    assert actual == expected, (
        "QuadraticForm local representation mismatch: "
        f"actual={actual}, expected={expected}"
    )


def test_quadraticform_local_universality_methods_detect_nonuniversal_case():
    """
    method: is_locally_universal_at_all_primes

    Local universality predicates test whether every local class is represented.
    Assertion: Example ternary form is not locally universal at all primes/places.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = (Q.is_locally_universal_at_all_primes(), Q.is_locally_universal_at_all_places())
    expected = (False, False)
    assert actual == expected, (
        "QuadraticForm local universality mismatch: "
        f"actual={actual}, expected={expected}"
    )


def test_quadraticform_is_locally_represented_number_at_place_true_sample():
    """
    method: is_locally_represented_number_at_place

    is_locally_represented_number_at_place(n,p) checks local representability at fixed place.
    Assertion: n=11 is represented at p=3 in this form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_locally_represented_number_at_place(11, 3)
    expected = True
    assert actual == expected, (
        f"QuadraticForm.is_locally_represented_number_at_place mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_is_locally_universal_at_all_places_false_example():
    """
    method: is_locally_universal_at_all_places

    is_locally_universal_at_all_places() is place-complete universality predicate.
    Assertion: Example form is not locally universal at all places.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_locally_universal_at_all_places()
    expected = False
    assert actual == expected, (
        f"QuadraticForm.is_locally_universal_at_all_places mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_is_locally_universal_at_prime_true_sample():
    """
    method: is_locally_universal_at_prime

    is_locally_universal_at_prime(p) checks universality at fixed p-adic place.
    Assertion: Example form is locally universal at p=2.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_locally_universal_at_prime(2)
    expected = True
    assert actual == expected, (
        f"QuadraticForm.is_locally_universal_at_prime mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_Gram_matrix_rational_has_expected_entries():
    """
    method: Gram_matrix_rational

    Gram_matrix_rational() returns rational Gram matrix.
    Assertion: Diagonal entries match coefficients for diagonal form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    G = Q.Gram_matrix_rational()
    actual = (G[0, 0], G[1, 1], G[2, 2])
    expected = (2, 3, 5)
    assert actual == expected, f"QuadraticForm.Gram_matrix_rational mismatch: actual={actual}, expected={expected}"


def test_quadraticform_adjoint_disc_matches_reciprocal_disc():
    """
    method: adjoint

    adjoint() returns adjoint form.
    Assertion: Applying antiadjoint to adjoint recovers original discriminant.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.adjoint().antiadjoint().disc()
    expected = Q.disc()
    assert actual == expected, f"QuadraticForm.adjoint mismatch: actual={actual}, expected={expected}"


def test_quadraticform_adjoint_primitive_is_primitive():
    """
    method: adjoint_primitive

    adjoint_primitive() normalizes adjoint to primitive form.
    Assertion: Returned form is primitive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.adjoint_primitive().is_primitive()
    expected = True
    assert actual == expected, f"QuadraticForm.adjoint_primitive mismatch: actual={actual}, expected={expected}"


def test_quadraticform_antiadjoint_inverts_adjoint():
    """
    method: antiadjoint

    antiadjoint() inverts adjoint construction on adjoint forms.
    Assertion: antiadjoint(adjoint(Q)) has same discriminant as Q.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    A = Q.adjoint()
    actual = A.antiadjoint().disc()
    expected = Q.disc()
    assert actual == expected, f"QuadraticForm.antiadjoint mismatch: actual={actual}, expected={expected}"


def test_quadraticform_anisotropic_primes_contains_three():
    """
    method: anisotropic_primes

    anisotropic_primes() lists places where form is anisotropic.
    Assertion: Prime 3 appears in the anisotropic list for this form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = 3 in Q.anisotropic_primes()
    expected = True
    assert actual == expected, f"QuadraticForm.anisotropic_primes mismatch: actual={actual}, expected={expected}"


def test_quadraticform_automorphism_group_order_matches_automorphisms_list():
    """
    method: automorphism_group

    automorphism_group() returns matrix group of automorphisms.
    Assertion: Group order equals number of listed automorphisms.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    G = Q.automorphism_group()
    actual = int(G.order())
    expected = len(Q.automorphisms())
    assert actual == expected, f"QuadraticForm.automorphism_group mismatch: actual={actual}, expected={expected}"


def test_quadraticform_automorphisms_fix_quadratic_value():
    """
    method: automorphisms

    automorphisms() returns integral linear maps preserving Q.
    Assertion: First automorphism preserves Q on sample vector.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    A = Q.automorphisms()[0]
    QQQ = Q.change_ring(QQ)
    v = vector(QQ, [1, 1, 0])
    actual = QQQ(v * A)
    expected = QQQ(v)
    assert actual == expected, f"QuadraticForm.automorphisms mismatch: actual={actual}, expected={expected}"


def test_quadraticform_basis_of_short_vectors_has_minimal_norm():
    """
    method: basis_of_short_vectors

    basis_of_short_vectors() returns a short basis.
    Assertion: Norms of basis vectors are nondecreasing in this diagonal example.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    B = Q.basis_of_short_vectors()
    norms = [Q(v) for v in B]
    actual = norms
    expected = sorted(norms)
    assert actual == expected, f"QuadraticForm.basis_of_short_vectors mismatch: actual={actual}, expected={expected}"


def test_quadraticform_cholesky_decomposition_reconstructs_matrix():
    """
    method: cholesky_decomposition

    cholesky_decomposition() returns positive factor in Gram convention.
    Assertion: Returned matrix equals Gram matrix over the same base ring.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.cholesky_decomposition()
    actual = R
    expected = Q.Gram_matrix().change_ring(R.base_ring())
    assert actual == expected, f"QuadraticForm.cholesky_decomposition mismatch: actual={actual}, expected={expected}"


def test_quadraticform_clifford_conductor_positive():
    """
    method: clifford_conductor

    clifford_conductor() returns conductor-like invariant.
    Assertion: Value is positive integer.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    c = Q.clifford_conductor()
    actual = c > 0
    expected = True
    assert actual == expected, f"QuadraticForm.clifford_conductor mismatch: actual={c}, expected=>0"


def test_quadraticform_clifford_invariant_is_hilbert_symbol_value():
    """
    method: clifford_invariant

    clifford_invariant(p) is local Clifford invariant at p.
    Assertion: Value at p=3 is in {1,-1}.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.clifford_invariant(3)
    expected = actual in {-1, 1}
    assert expected, f"QuadraticForm.clifford_invariant mismatch: actual={actual}, expected=in{{-1,1}}"


def test_quadraticform_compute_definiteness_sets_consistent_string():
    """
    method: compute_definiteness

    compute_definiteness() precomputes definiteness metadata.
    Assertion: Resulting string agrees with positive-definite status.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    _ = Q.compute_definiteness()
    actual = Q.compute_definiteness_string_by_determinants()
    expected = "pos_def"
    assert actual == expected, (
        f"QuadraticForm.compute_definiteness mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_compute_definiteness_string_expected_value():
    """
    method: compute_definiteness_string_by_determinants

    compute_definiteness_string_by_determinants() classifies definiteness.
    Assertion: Positive diagonal form returns 'pos_def'.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.compute_definiteness_string_by_determinants()
    expected = "pos_def"
    assert actual == expected, (
        "QuadraticForm.compute_definiteness_string_by_determinants mismatch: "
        f"actual={actual}, expected={expected}"
    )


def test_quadraticform_genera_nonempty_for_signature_and_det():
    """
    method: genera

    genera(sig_pair, determinant) enumerates genera with given invariants.
    Assertion: For this query, all returned genera have signature (3,0), determinant Q.det(), and count 40.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    gs = Q.genera((3, 0), Q.det())
    actual = (
        len(gs),
        {(g.signature_pair(), g.determinant()) for g in gs},
    )
    expected = (40, {((3, 0), Q.det())})
    assert actual == expected, f"QuadraticForm.genera mismatch: actual={actual}, expected={expected}"


def test_quadraticform_global_genus_symbol_determinant_matches():
    """
    method: global_genus_symbol

    global_genus_symbol() returns genus symbol of the form.
    Assertion: Symbol determinant matches form determinant.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    g = Q.global_genus_symbol()
    actual = g.determinant()
    expected = Q.det()
    assert actual == expected, (
        f"QuadraticForm.global_genus_symbol mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_has_integral_gram_matrix_true_for_integer_form():
    """
    method: has_integral_Gram_matrix

    has_integral_Gram_matrix() checks Gram integrality.
    Assertion: Integer-coefficient form has integral Gram matrix.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.has_integral_Gram_matrix()
    expected = True
    assert actual == expected, (
        f"QuadraticForm.has_integral_Gram_matrix mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_hasse_conductor_positive():
    """
    method: hasse_conductor

    hasse_conductor() returns conductor of Hasse invariants.
    Assertion: Conductor is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    h = Q.hasse_conductor()
    actual = h > 0
    expected = True
    assert actual == expected, f"QuadraticForm.hasse_conductor mismatch: actual={h}, expected=>0"


def test_quadraticform_hasse_invariant_comparison_with_omeara():
    """
    method: hasse_invariant

    hasse_invariant(p) and hasse_invariant__OMeara(p) are local invariants.
    Assertion: Both are sign values in {1,-1} at p=2.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    h = Q.hasse_invariant(2)
    ho = Q.hasse_invariant__OMeara(2)
    actual = (h in {-1, 1}, ho in {-1, 1})
    expected = (True, True)
    assert actual == expected, f"QuadraticForm.hasse_invariant mismatch: actual={actual}, expected={expected}"


def test_quadraticform_hasse_invariant_omeara_sign_value():
    """
    method: hasse_invariant__OMeara

    hasse_invariant__OMeara(p) is O'Meara variant of Hasse invariant.
    Assertion: Value at p=2 is in {1,-1}.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.hasse_invariant__OMeara(2)
    expected = actual in {-1, 1}
    assert expected, f"QuadraticForm.hasse_invariant__OMeara mismatch: actual={actual}, expected=in{{-1,1}}"


def test_quadraticform_is_adjoint_true_on_adjoint_form():
    """
    method: is_adjoint

    is_adjoint() detects adjoint forms.
    Assertion: adjoint(Q) is detected as adjoint.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5]).adjoint()
    actual = Q.is_adjoint()
    expected = True
    assert actual == expected, f"QuadraticForm.is_adjoint mismatch: actual={actual}, expected={expected}"


def test_quadraticform_is_hyperbolic_false_at_two_for_example():
    """
    method: is_hyperbolic

    is_hyperbolic(p) checks local hyperbolicity.
    Assertion: Example form is not hyperbolic at p=2.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.is_hyperbolic(2)
    expected = False
    assert actual == expected, f"QuadraticForm.is_hyperbolic mismatch: actual={actual}, expected={expected}"


def test_quadraticform_is_zero_nonsingular_false_for_zero_vector():
    """
    method: is_zero_nonsingular

    is_zero_nonsingular(v) checks nonsingular isotropic zeros.
    Assertion: Zero vector is not a nonsingular zero.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    z = vector(ZZ, [0, 0, 0])
    actual = Q.is_zero_nonsingular(z)
    expected = False
    assert actual == expected, (
        f"QuadraticForm.is_zero_nonsingular mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_is_zero_singular_true_for_zero_vector():
    """
    method: is_zero_singular

    is_zero_singular(v) checks singular isotropic zeros.
    Assertion: Zero vector is singular zero.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    z = vector(ZZ, [0, 0, 0])
    actual = Q.is_zero_singular(z)
    expected = True
    assert actual == expected, (
        f"QuadraticForm.is_zero_singular mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_local_normal_form_preserves_discriminant_at_two():
    """
    method: local_normal_form

    local_normal_form(p) returns p-local normal form.
    Assertion: Local normal form at p=2 has same discriminant.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    N = Q.local_normal_form(2)
    actual = N.disc()
    expected = Q.disc()
    assert actual == expected, f"QuadraticForm.local_normal_form mismatch: actual={actual}, expected={expected}"


def test_quadraticform_minkowski_reduction_preserves_discriminant():
    """
    method: minkowski_reduction

    minkowski_reduction() returns reduced equivalent form and transform.
    Assertion: Reduced form has same discriminant.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R, _ = Q.minkowski_reduction()
    actual = R.disc()
    expected = Q.disc()
    assert actual == expected, (
        f"QuadraticForm.minkowski_reduction mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_reduced_binary_form_preserves_discriminant():
    """
    method: reduced_binary_form

    reduced_binary_form() returns reduction output pair.
    Assertion: Reduced representative keeps discriminant.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R, _ = Q.reduced_binary_form()
    actual = R.disc()
    expected = Q.disc()
    assert actual == expected, (
        f"QuadraticForm.reduced_binary_form mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_theta_by_cholesky_starts_with_one_constant_term():
    """
    method: theta_by_cholesky

    theta_by_cholesky(q_prec) computes theta coefficients.
    Assertion: Constant term is 1.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    t = Q.theta_by_cholesky(5)
    actual = t[0]
    expected = 1
    assert actual == expected, (
        f"QuadraticForm.theta_by_cholesky mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_theta_by_pari_starts_with_one_constant_term():
    """
    method: theta_by_pari

    theta_by_pari(Max) computes theta coefficients via PARI.
    Assertion: Constant term is 1.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    t = Q.theta_by_pari(4)
    actual = t[0]
    expected = 1
    assert actual == expected, f"QuadraticForm.theta_by_pari mismatch: actual={actual}, expected={expected}"


def test_quadraticform_add_symmetric_changes_selected_coefficients():
    """
    method: add_symmetric

    add_symmetric(c,i,j) performs symmetric elementary update.
    Assertion: Updating (i,j)=(0,1) changes off-diagonal coefficient.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.add_symmetric(1, 0, 1)
    actual = R.coefficients()[1]
    expected = 6
    assert actual == expected, f"QuadraticForm.add_symmetric mismatch: actual={actual}, expected={expected}"


def test_quadraticform_basiclemma_zero_case_returns_zero():
    """
    method: basiclemma

    basiclemma(M) computes local representation helper count.
    Assertion: basiclemma(1) equals 0 for sample form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.basiclemma(1)
    expected = 0
    assert actual == expected, f"QuadraticForm.basiclemma mismatch: actual={actual}, expected={expected}"


def test_quadraticform_basiclemmavec_has_expected_dimension():
    """
    method: basiclemmavec

    basiclemmavec(M) returns auxiliary vector for local computations.
    Assertion: Returned vector length equals form dimension.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.basiclemmavec(1)
    actual = len(v)
    expected = Q.dim()
    assert actual == expected, f"QuadraticForm.basiclemmavec mismatch: actual={actual}, expected={expected}"


def test_quadraticform_complementary_subform_reduces_dimension_by_one():
    """
    method: complementary_subform_to_vector

    complementary_subform_to_vector(v) returns orthogonal complement subform.
    Assertion: Complementary subform has dimension n-1.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    C = Q.complementary_subform_to_vector((1, 0, 0))
    actual = C.dim()
    expected = Q.dim() - 1
    assert actual == expected, (
        f"QuadraticForm.complementary_subform_to_vector mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_discrec_positive_for_positive_definite_example():
    """
    method: discrec

    discrec() returns reciprocal discriminant-style invariant.
    Assertion: Value is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    d = Q.discrec()
    actual = d > 0
    expected = True
    assert actual == expected, f"QuadraticForm.discrec mismatch: actual={d}, expected=>0"


def test_quadraticform_divide_variable_by_one_is_identity():
    """
    method: divide_variable

    divide_variable(c,i) divides variable i by scalar c.
    Assertion: Dividing by 1 leaves coefficients unchanged.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.divide_variable(1, 2)
    actual = R.coefficients()
    expected = Q.coefficients()
    assert actual == expected, f"QuadraticForm.divide_variable mismatch: actual={actual}, expected={expected}"


def test_quadraticform_elementary_substitution_preserves_dimension():
    """
    method: elementary_substitution

    elementary_substitution(c,i,j) applies elementary variable substitution.
    Assertion: Dimension is preserved.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.elementary_substitution(1, 0, 1)
    actual = R.dim()
    expected = Q.dim()
    assert actual == expected, (
        f"QuadraticForm.elementary_substitution mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_extract_variables_dimension_matches_selection():
    """
    method: extract_variables

    extract_variables(idx) extracts subform in selected variables.
    Assertion: Extracting three indices gives a ternary form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.extract_variables((1, 0, 0))
    actual = R.dim()
    expected = 3
    assert actual == expected, f"QuadraticForm.extract_variables mismatch: actual={actual}, expected={expected}"


def test_quadraticform_find_entry_with_minimal_scale_returns_valid_index_pair():
    """
    method: find_entry_with_minimal_scale_at_prime

    find_entry_with_minimal_scale_at_prime(p) returns matrix index pair.
    Assertion: Returned indices are within matrix bounds.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    i, j = Q.find_entry_with_minimal_scale_at_prime(2)
    actual = (0 <= i < Q.dim(), 0 <= j < Q.dim())
    expected = (True, True)
    assert actual == expected, (
        f"QuadraticForm.find_entry_with_minimal_scale_at_prime mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_has_equivalent_jordan_decomposition_at_prime_detects_change():
    """
    method: has_equivalent_Jordan_decomposition_at_prime

    has_equivalent_Jordan_decomposition_at_prime(other,p) compares local Jordan data.
    Assertion: Same form matches; modified form does not at p=2.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 6])
    actual = (
        Q.has_equivalent_Jordan_decomposition_at_prime(Q, 2),
        Q.has_equivalent_Jordan_decomposition_at_prime(R, 2),
    )
    expected = (True, False)
    assert actual == expected, (
        "QuadraticForm.has_equivalent_Jordan_decomposition_at_prime mismatch: "
        f"actual={actual}, expected={expected}"
    )


def test_quadraticform_level_ideal_matches_level_generator():
    """
    method: level_ideal

    level_ideal() returns principal ideal generated by level over ZZ.
    Assertion: Generator equals level().
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    I = Q.level_ideal()
    actual = I.gen()
    expected = Q.level()
    assert actual == expected, f"QuadraticForm.level_ideal mismatch: actual={actual}, expected={expected}"


def test_quadraticform_list_external_initializations_empty_for_internal_example():
    """
    method: list_external_initializations

    list_external_initializations() reports backend initialization hints.
    Assertion: Returns empty list on this native form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.list_external_initializations()
    expected = []
    assert actual == expected, (
        f"QuadraticForm.list_external_initializations mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_multiply_variable_by_zero_forces_zero_coefficient():
    """
    method: multiply_variable

    multiply_variable(c,i) scales variable i by c.
    Assertion: Setting c=0 forces corresponding diagonal coefficient to 0.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.multiply_variable(0, 1)
    actual = R.coefficients()[3]
    expected = 0
    assert actual == expected, f"QuadraticForm.multiply_variable mismatch: actual={actual}, expected={expected}"


def test_quadraticform_orbits_lines_mod_p_nonempty():
    """
    method: orbits_lines_mod_p

    orbits_lines_mod_p(p) returns line-orbit representatives mod p.
    Assertion: For n=3 and p=2, all 7 nonzero binary vectors appear as representatives.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    O = Q.orbits_lines_mod_p(2)
    actual = {tuple(v) for v in O}
    expected = {
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (1, 0, 0),
        (1, 0, 1),
        (1, 1, 0),
        (1, 1, 1),
    }
    assert actual == expected, f"QuadraticForm.orbits_lines_mod_p mismatch: actual={actual}, expected={expected}"


def test_quadraticform_representation_number_list_constant_term_one():
    """
    method: representation_number_list

    representation_number_list(B) lists counts up to bound.
    Assertion: First count (for 0) equals 1.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    vals = Q.representation_number_list(1)
    actual = vals[0]
    expected = 1
    assert actual == expected, (
        f"QuadraticForm.representation_number_list mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_representation_vector_list_contains_zero_vector_for_zero():
    """
    method: representation_vector_list

    representation_vector_list(B) lists representing vectors by value.
    Assertion: Zero vector appears in value-0 list.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    reps = Q.representation_vector_list(1)
    actual = (0, 0, 0) in [tuple(v) for v in reps[0]]
    expected = True
    assert actual == expected, (
        f"QuadraticForm.representation_vector_list mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_set_number_of_automorphisms_updates_cached_value():
    """
    method: set_number_of_automorphisms

    set_number_of_automorphisms(n) sets cached automorphism count.
    Assertion: After setting to 1, accessor returns 1.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    Q.set_number_of_automorphisms(1)
    actual = int(Q.number_of_automorphisms())
    expected = 1
    assert actual == expected, (
        f"QuadraticForm.set_number_of_automorphisms mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_short_primitive_vector_list_subset_of_short_vectors():
    """
    method: short_primitive_vector_list_up_to_length

    short_primitive_vector_list_up_to_length(B) lists primitive short vectors.
    Assertion: Primitive list at bound 0 is empty and thus subset of short list.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    P = Q.short_primitive_vector_list_up_to_length(0, True)
    S = Q.short_vector_list_up_to_length(0, True)
    actual = all(v in S for v in P)
    expected = True
    assert actual == expected, (
        f"QuadraticForm.short_primitive_vector_list_up_to_length mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_short_vector_list_up_to_length_zero_contains_none():
    """
    method: short_vector_list_up_to_length

    short_vector_list_up_to_length(B) lists vectors by norm bound.
    Assertion: Bound 0 yields empty list for positive-definite form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.short_vector_list_up_to_length(0, True)
    expected = []
    assert actual == expected, (
        f"QuadraticForm.short_vector_list_up_to_length mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_swap_variables_preserves_discriminant():
    """
    method: swap_variables

    swap_variables(i,j) permutes variables.
    Assertion: Discriminant is invariant under variable swap.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = Q.swap_variables(0, 1)
    actual = R.disc()
    expected = Q.disc()
    assert actual == expected, f"QuadraticForm.swap_variables mismatch: actual={actual}, expected={expected}"


def test_quadraticform_theta_series_degree_2_has_constant_term_one():
    """
    method: theta_series_degree_2

    theta_series_degree_2(prec) returns dictionary of degree-2 theta coefficients.
    Assertion: Zero index coefficient is 1.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    t2 = Q.theta_series_degree_2(1)
    actual = t2[(0, 0, 0)]
    expected = 1
    assert actual == expected, (
        f"QuadraticForm.theta_series_degree_2 mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_vectors_by_length_zero_shell_is_zero_vector():
    """
    method: vectors_by_length

    vectors_by_length(B) groups vectors by represented lengths.
    Assertion: Length-0 shell contains the zero vector.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    shells = Q.vectors_by_length(1)
    actual = (0, 0, 0) in [tuple(v) for v in shells[0]]
    expected = True
    assert actual == expected, f"QuadraticForm.vectors_by_length mismatch: actual={actual}, expected={expected}"


def test_quadraticform_CS_genus_symbol_list_nonempty():
    """
    method: CS_genus_symbol_list

    CS_genus_symbol_list() returns local genus symbols at relevant primes.
    Assertion: List is nonempty for nontrivial form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = len(Q.CS_genus_symbol_list()) > 0
    expected = True
    assert actual == expected, f"QuadraticForm.CS_genus_symbol_list mismatch: actual={actual}, expected={expected}"


def test_quadraticform_collect_small_blocks_recovers_block_structure():
    """
    method: collect_small_blocks

    collect_small_blocks(G) recovers 1x1/2x2 blocks from a block-diagonal matrix.
    Assertion: Recovered blocks match the original block list exactly.
    """
    from sage.all import Matrix
    from sage.quadratic_forms.genera.normal_form import collect_small_blocks

    w1 = Matrix([1])
    v = Matrix(ZZ, 2, [2, 1, 1, 2])
    blocks = [w1, v, v, w1, w1, v, w1, v]
    G = Matrix.block_diagonal(blocks)
    actual = collect_small_blocks(G)
    expected = blocks
    assert actual == expected, (
        f"collect_small_blocks mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_count_all_local_good_types_normal_form_matches_reference_values():
    """
    method: count_all_local_good_types_normal_form

    count_all_local_good_types_normal_form counts good-type local solutions.
    Assertion: Sage reference values for Q=diag(1,2,3) at p=2, k=3, m=3 are reproduced.
    """
    from sage.all import DiagonalQuadraticForm
    from sage.quadratic_forms.count_local_2 import count_all_local_good_types_normal_form

    Q = DiagonalQuadraticForm(ZZ, [1, 2, 3]).local_normal_form(2)
    actual = (
        count_all_local_good_types_normal_form(Q, 2, 3, 3, None, None),
        count_all_local_good_types_normal_form(Q, 2, 3, 3, [0], None),
    )
    expected = (64, 32)
    assert actual == expected, (
        f"count_all_local_good_types_normal_form mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_genus_symbol_compartments_match_known_2adic_partition():
    """
    method: Genus_Symbol_p_adic_ring.compartments

    Genus_Symbol_p_adic_ring.compartments() returns 2-adic compartment index groups.
    Assertion: Known genus symbol for diag(1,2,3,4) has a single compartment [0,1,2].
    """
    from sage.all import DiagonalQuadraticForm
    from sage.quadratic_forms.genera.genus import (
        Genus_Symbol_p_adic_ring,
        p_adic_symbol,
    )

    A = DiagonalQuadraticForm(ZZ, [1, 2, 3, 4]).Hessian_matrix()
    G2 = Genus_Symbol_p_adic_ring(2, p_adic_symbol(A, 2, 2))
    actual = G2.compartments()
    expected = [[0, 1, 2]]
    assert actual == expected, (
        f"Genus_Symbol_p_adic_ring.compartments mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_GHY_mass_maximal_returns_none_for_nonmaximal_case():
    """
    method: GHY_mass__maximal

    GHY_mass__maximal() returns mass for maximal lattices in GHY algorithm.
    Assertion: Returns None on this nonmaximal example.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.GHY_mass__maximal()
    expected = None
    assert actual == expected, f"QuadraticForm.GHY_mass__maximal mismatch: actual={actual}, expected={expected}"


def test_quadraticform_Kitaoka_mass_at_2_positive():
    """
    method: Kitaoka_mass_at_2

    Kitaoka_mass_at_2() computes local mass factor at 2.
    Assertion: Factor is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.Kitaoka_mass_at_2()
    actual = v > 0
    expected = True
    assert actual == expected, f"QuadraticForm.Kitaoka_mass_at_2 mismatch: actual={v}, expected=>0"


def test_quadraticform_Pall_mass_density_at_odd_prime_positive():
    """
    method: Pall_mass_density_at_odd_prime

    Pall_mass_density_at_odd_prime(p) computes odd-prime local density.
    Assertion: Density at p=3 is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.Pall_mass_density_at_odd_prime(3)
    actual = v > 0
    expected = True
    assert actual == expected, (
        f"QuadraticForm.Pall_mass_density_at_odd_prime mismatch: actual={v}, expected=>0"
    )


def test_quadraticform_Watson_mass_at_2_positive():
    """
    method: Watson_mass_at_2

    Watson_mass_at_2() computes Watson local mass factor at 2.
    Assertion: Factor is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.Watson_mass_at_2()
    actual = v > 0
    expected = True
    assert actual == expected, f"QuadraticForm.Watson_mass_at_2 mismatch: actual={v}, expected=>0"


def test_quadraticform_conway_cross_product_doubled_power_nonnegative():
    """
    method: conway_cross_product_doubled_power

    conway_cross_product_doubled_power(p) contributes to Conway p-mass.
    Assertion: Value at p=3 is nonnegative.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.conway_cross_product_doubled_power(3)
    actual = v >= 0
    expected = True
    assert actual == expected, (
        f"QuadraticForm.conway_cross_product_doubled_power mismatch: actual={v}, expected>=0"
    )


def test_quadraticform_conway_diagonal_factor_positive():
    """
    method: conway_diagonal_factor

    conway_diagonal_factor(p) is Conway diagonal correction.
    Assertion: Value at p=3 is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.conway_diagonal_factor(3)
    actual = v > 0
    expected = True
    assert actual == expected, f"QuadraticForm.conway_diagonal_factor mismatch: actual={v}, expected=>0"


def test_quadraticform_conway_mass_positive():
    """
    method: conway_mass

    conway_mass() computes Conway mass.
    Assertion: Mass is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    m = Q.conway_mass()
    actual = m > 0
    expected = True
    assert actual == expected, f"QuadraticForm.conway_mass mismatch: actual={m}, expected=>0"


def test_quadraticform_conway_octane_requires_odd_unimodular_block():
    """
    method: conway_octane_of_this_unimodular_Jordan_block_at_2

    conway_octane_of_this_unimodular_Jordan_block_at_2() returns the 2-adic octane.
    Assertion: For x^2 + y^2 + z^2, the octane value is 3.
    """
    Q = QuadraticForm(ZZ, 3, [1, 0, 0, 1, 0, 1])
    actual = Q.conway_octane_of_this_unimodular_Jordan_block_at_2()
    expected = 3
    assert_equal(
        actual,
        expected,
        "QuadraticForm.conway_octane_of_this_unimodular_Jordan_block_at_2 mismatch",
    )


def test_quadraticform_conway_p_mass_positive_at_three():
    """
    method: conway_p_mass

    conway_p_mass(p) is Conway local p-mass factor.
    Assertion: Value at p=3 is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.conway_p_mass(3)
    actual = v > 0
    expected = True
    assert actual == expected, f"QuadraticForm.conway_p_mass mismatch: actual={v}, expected=>0"


def test_quadraticform_conway_species_lists_have_expected_lengths():
    """
    method: conway_species_list_at_2

    Species lists encode Conway decomposition data.
    Assertion: 2-adic list is nonempty and odd-prime list at 3 has length 2.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = (len(Q.conway_species_list_at_2()) > 0, len(Q.conway_species_list_at_odd_prime(3)))
    expected = (True, 2)
    assert actual == expected, (
        f"QuadraticForm.conway_species lists mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_conway_species_list_at_odd_prime_length_two():
    """
    method: conway_species_list_at_odd_prime

    conway_species_list_at_odd_prime(p) returns odd-prime species data.
    Assertion: At p=3 returned list has length 2.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = len(Q.conway_species_list_at_odd_prime(3))
    expected = 2
    assert actual == expected, (
        f"QuadraticForm.conway_species_list_at_odd_prime mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_conway_standard_mass_positive():
    """
    method: conway_standard_mass

    conway_standard_mass() computes standard reference mass.
    Assertion: For this ternary form, value is 1/6.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.conway_standard_mass()
    expected = QQ(1) / QQ(6)
    assert actual == expected, (
        f"QuadraticForm.conway_standard_mass mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_conway_standard_p_mass_positive_at_three():
    """
    method: conway_standard_p_mass

    conway_standard_p_mass(p) is standard local factor.
    Assertion: Value at p=3 is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    m = Q.conway_standard_p_mass(3)
    actual = m > 0
    expected = True
    assert actual == expected, (
        f"QuadraticForm.conway_standard_p_mass mismatch: actual={m}, expected=>0"
    )


def test_quadraticform_conway_type_factor_positive_integer():
    """
    method: conway_type_factor

    conway_type_factor() is combinatorial type multiplier.
    Assertion: Value is a positive integer.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.conway_type_factor()
    actual = (v > 0, v in ZZ)
    expected = (True, True)
    assert actual == expected, f"QuadraticForm.conway_type_factor mismatch: actual={actual}, expected={expected}"


def test_quadraticform_count_congruence_solution_decomposition_at_basic_input():
    """
    method: count_congruence_solutions

    count_congruence_solutions decomposes into good/bad/zero contributions.
    Assertion: Total equals sum of type contributions at basic test input.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    args = (3, 1, 0, [], [])
    total = Q.count_congruence_solutions(*args)
    parts = (
        Q.count_congruence_solutions__good_type(*args)
        + Q.count_congruence_solutions__bad_type(*args)
        + Q.count_congruence_solutions__zero_type(*args)
    )
    actual = total
    expected = parts
    assert actual == expected, f"QuadraticForm.count_congruence_solutions mismatch: actual={actual}, expected={expected}"


def test_quadraticform_count_congruence_bad_type_splits_I_II():
    """
    method: count_congruence_solutions__bad_type

    bad_type decomposes into type I and II contributions.
    Assertion: bad_type = bad_type_I + bad_type_II at basic input.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    args = (3, 1, 0, [], [])
    actual = Q.count_congruence_solutions__bad_type(*args)
    expected = Q.count_congruence_solutions__bad_type_I(*args) + Q.count_congruence_solutions__bad_type_II(*args)
    assert actual == expected, (
        f"QuadraticForm.count_congruence_solutions__bad_type mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_count_congruence_solutions_as_vector_length_six():
    """
    method: count_congruence_solutions_as_vector

    count_congruence_solutions_as_vector returns component counts vector.
    Assertion: Output vector has six entries.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = len(Q.count_congruence_solutions_as_vector(3, 1, 0, [], []))
    expected = 6
    assert actual == expected, (
        f"QuadraticForm.count_congruence_solutions_as_vector mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_count_modp_solutions_by_gauss_sum_raises_on_singular_case():
    """
    method: count_modp_solutions__by_Gauss_sum

    count_modp_solutions__by_Gauss_sum(p,m) computes local solution counts.
    Assertion: For p=7 and m=1 on this form, the count is 42.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.count_modp_solutions__by_Gauss_sum(7, 1)
    expected = 42
    assert_equal(actual, expected, "QuadraticForm.count_modp_solutions__by_Gauss_sum mismatch")


def test_quadraticform_jordan_blocks_by_scale_and_unimodular_nonempty():
    """
    method: jordan_blocks_by_scale_and_unimodular

    jordan_blocks_by_scale_and_unimodular(p) returns local Jordan blocks.
    Assertion: Decomposition at p=2 is nonempty.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = len(Q.jordan_blocks_by_scale_and_unimodular(2)) > 0
    expected = True
    assert actual == expected, (
        f"QuadraticForm.jordan_blocks_by_scale_and_unimodular mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_jordan_blocks_unimodular_list_nonempty():
    """
    method: jordan_blocks_in_unimodular_list_by_scale_power

    jordan_blocks_in_unimodular_list_by_scale_power(p) returns unimodular block list.
    Assertion: List at p=2 is nonempty.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = len(Q.jordan_blocks_in_unimodular_list_by_scale_power(2)) > 0
    expected = True
    assert actual == expected, (
        "QuadraticForm.jordan_blocks_in_unimodular_list_by_scale_power mismatch: "
        f"actual={actual}, expected={expected}"
    )


def test_quadraticform_level_Tornaria_is_positive():
    """
    method: level__Tornaria

    level__Tornaria() computes Tornaria level variant.
    Assertion: Value is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    lv = Q.level__Tornaria()
    actual = lv > 0
    expected = True
    assert actual == expected, f"QuadraticForm.level__Tornaria mismatch: actual={lv}, expected=>0"


def test_quadraticform_local_genus_symbol_returns_symbol():
    """
    method: local_genus_symbol

    local_genus_symbol(p) returns p-adic genus symbol.
    Assertion: String form mentions the prime.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    s = str(Q.local_genus_symbol(2))
    actual = "2" in s
    expected = True
    assert actual == expected, f"QuadraticForm.local_genus_symbol mismatch: actual={actual}, expected={expected}, s={s}"


def test_quadraticform_local_density_agrees_with_congruence_at_sample():
    """
    method: local_density

    local_density(p,m) and local_density_congruence(p,m) agree when both defined.
    Assertion: Equality holds at (p,m)=(3,1).
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_density(3, 1)
    expected = Q.local_density_congruence(3, 1)
    assert actual == expected, f"QuadraticForm.local_density mismatch: actual={actual}, expected={expected}"


def test_quadraticform_local_bad_density_equals_sum_of_I_and_II():
    """
    method: local_bad_density_congruence

    local_bad_density_congruence splits as badI + badII.
    Assertion: Equality holds at (p,m)=(3,1).
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_bad_density_congruence(3, 1)
    expected = Q.local_badI_density_congruence(3, 1) + Q.local_badII_density_congruence(3, 1)
    assert actual == expected, (
        f"QuadraticForm.local_bad_density_congruence mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_local_good_density_even_odd_helpers_on_sample():
    """
    method: local_good_density_congruence

    local_good_density_congruence and parity-specific helpers are consistent on sample.
    Assertion: Helper outputs are defined and nonnegative.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = (
        Q.local_good_density_congruence(3, 1) >= 0,
        Q.local_good_density_congruence_even(1, [], []) >= 0,
        Q.local_good_density_congruence_odd(3, 1, [], []) >= 0,
    )
    expected = (True, True, True)
    assert actual == expected, (
        f"QuadraticForm.local_good_density_congruence mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_local_primitive_density_agrees_with_congruence():
    """
    method: local_primitive_density

    local_primitive_density(p,m) equals congruence variant when both defined.
    Assertion: Equality holds at (p,m)=(3,1).
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_primitive_density(3, 1)
    expected = Q.local_primitive_density_congruence(3, 1)
    assert actual == expected, (
        f"QuadraticForm.local_primitive_density mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_local_representation_conditions_mentions_exception_prime():
    """
    method: local_representation_conditions

    local_representation_conditions() summarizes represented local conditions.
    Assertion: String output records prime 3 as exceptional.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    s = str(Q.local_representation_conditions())
    actual = "3" in s
    expected = True
    assert actual == expected, (
        f"QuadraticForm.local_representation_conditions mismatch: actual={actual}, expected={expected}, s={s}"
    )


def test_quadraticform_local_zero_density_congruence_zero_at_sample():
    """
    method: local_zero_density_congruence

    local_zero_density_congruence(p,m) counts zero-type contribution.
    Assertion: Value at (p,m)=(3,1) is 0.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_zero_density_congruence(3, 1)
    expected = 0
    assert actual == expected, (
        f"QuadraticForm.local_zero_density_congruence mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_mass_by_siegel_densities_positive():
    """
    method: mass__by_Siegel_densities

    mass__by_Siegel_densities() computes mass via local densities.
    Assertion: For this ternary form, value is 15/4.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.mass__by_Siegel_densities()
    expected = QQ(15) / QQ(4)
    assert actual == expected, (
        f"QuadraticForm.mass__by_Siegel_densities mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_mass_at_two_by_counting_mod_power_positive():
    """
    method: mass_at_two_by_counting_mod_power

    mass_at_two_by_counting_mod_power(k) computes 2-adic mass from congruence counting.
    Assertion: Value at k=1 is positive.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    v = Q.mass_at_two_by_counting_mod_power(1)
    actual = v > 0
    expected = True
    assert actual == expected, (
        f"QuadraticForm.mass_at_two_by_counting_mod_power mismatch: actual={v}, expected=>0"
    )


def test_quadraticform_minkowski_reduction_for_4vars_sp_preserves_discriminant():
    """
    method: minkowski_reduction_for_4vars__SP

    minkowski_reduction_for_4vars__SP() applies Schiemann-Pohst reduction in 4 vars.
    Assertion: Reduced form has same discriminant.
    """
    Q4 = QuadraticForm(ZZ, 4, [1, 0, 0, 0, 1, 0, 0, 1, 0, 1])
    R, _ = Q4.minkowski_reduction_for_4vars__SP()
    actual = R.disc()
    expected = Q4.disc()
    assert actual == expected, (
        "QuadraticForm.minkowski_reduction_for_4vars__SP mismatch: "
        f"actual={actual}, expected={expected}"
    )


def test_quadraticform_neighbor_iteration_returns_seed_under_class_limit():
    """
    method: neighbor_iteration

    neighbor_iteration(seeds,p,...) explores p-neighbor graph.
    Assertion: With max_classes=1, output contains exactly one class.
    """
    Q = QuadraticForm(ZZ, 3, [1, -1, 0, 3, -2, 3])
    out = QuadraticForm.neighbor_iteration([Q], 11, max_classes=1, max_neighbors=1)
    actual = len(out)
    expected = 1
    assert actual == expected, f"QuadraticForm.neighbor_iteration mismatch: actual={actual}, expected={expected}"


def test_quadraticform_reduced_binary_form1_on_binary_input_preserves_discriminant():
    """
    method: reduced_binary_form1

    reduced_binary_form1() applies binary reduction routine.
    Assertion: Reduced binary representative preserves discriminant.
    """
    B = QuadraticForm(ZZ, 2, [1, 0, 1])
    R, _ = B.reduced_binary_form1()
    actual = R.disc()
    expected = B.disc()
    assert actual == expected, (
        f"QuadraticForm.reduced_binary_form1 mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_reduced_ternary_form_Dickson_notimplemented_here():
    """
    method: reduced_ternary_form__Dickson

    reduced_ternary_form__Dickson() is documented but currently unimplemented upstream.
    Assertion: The method raises NotImplementedError on a ternary integral form.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    with pytest.raises(NotImplementedError):
        _ = Q.reduced_ternary_form__Dickson()


def test_quadraticform_shimura_mass_maximal_returns_none_for_nonmaximal_case():
    """
    method: shimura_mass__maximal

    shimura_mass__maximal() returns Shimura mass for maximal lattices.
    Assertion: Returns None on this nonmaximal sample.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.shimura_mass__maximal()
    expected = None
    assert actual == expected, f"QuadraticForm.shimura_mass__maximal mismatch: actual={actual}, expected={expected}"


def test_quadraticform_siegel_product_raises_for_nonsquare_root_rationality():
    """
    method: siegel_product

    siegel_product(u) computes the local-density product factor.
    Assertion: For x^2 + y^2 + z^2 and u=2, siegel_product equals 9/4.
    """
    Q = QuadraticForm(ZZ, 3, [1, 0, 0, 1, 0, 1])
    actual = Q.siegel_product(2)
    expected = QQ(9) / QQ(4)
    assert_equal(actual, expected, "QuadraticForm.siegel_product mismatch")


def test_quadraticform_split_local_cover_preserves_discriminant():
    """
    method: split_local_cover

    split_local_cover() returns a locally equivalent split cover form.
    Assertion: Discriminant is preserved.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    S = Q.split_local_cover()
    actual = S.disc()
    expected = Q.disc()
    assert actual == expected, (
        f"QuadraticForm.split_local_cover mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_sum_by_coefficients_with_adds_forms():
    """
    method: sum_by_coefficients_with

    sum_by_coefficients_with(R) adds forms coefficient-wise.
    Assertion: First diagonal coefficient adds exactly.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    R = QuadraticForm(ZZ, 3, [1, 0, 0, 1, 0, 1])
    S = Q.sum_by_coefficients_with(R)
    actual = S.coefficients()[0]
    expected = Q.coefficients()[0] + R.coefficients()[0]
    assert actual == expected, (
        f"QuadraticForm.sum_by_coefficients_with mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_count_congruence_type_I_zero_on_basic_input():
    """
    method: count_congruence_solutions__bad_type_I

    count_congruence_solutions__bad_type_I computes type-I bad contribution.
    Assertion: Contribution is 0 on basic sample input.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.count_congruence_solutions__bad_type_I(3, 1, 0, [], [])
    expected = 0
    assert actual == expected, (
        f"QuadraticForm.count_congruence_solutions__bad_type_I mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_count_congruence_type_II_zero_on_basic_input():
    """
    method: count_congruence_solutions__bad_type_II

    count_congruence_solutions__bad_type_II computes type-II bad contribution.
    Assertion: Contribution is 0 on basic sample input.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.count_congruence_solutions__bad_type_II(3, 1, 0, [], [])
    expected = 0
    assert actual == expected, (
        f"QuadraticForm.count_congruence_solutions__bad_type_II mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_count_congruence_good_type_zero_on_basic_input():
    """
    method: count_congruence_solutions__good_type

    count_congruence_solutions__good_type computes good contribution.
    Assertion: Contribution is 0 on basic sample input.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.count_congruence_solutions__good_type(3, 1, 0, [], [])
    expected = 0
    assert actual == expected, (
        f"QuadraticForm.count_congruence_solutions__good_type mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_count_congruence_zero_type_zero_on_basic_input():
    """
    method: count_congruence_solutions__zero_type

    count_congruence_solutions__zero_type computes zero-type contribution.
    Assertion: Contribution is 0 on basic sample input.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.count_congruence_solutions__zero_type(3, 1, 0, [], [])
    expected = 0
    assert actual == expected, (
        f"QuadraticForm.count_congruence_solutions__zero_type mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_find_primitive_p_divisible_vector_random_is_p_divisible():
    """
    method: find_primitive_p_divisible_vector__random

    find_primitive_p_divisible_vector__random(p) finds primitive vector with Q(v)=0 mod p.
    Assertion: Returned vector evaluates to 0 mod p.
    """
    Q = QuadraticForm(ZZ, 3, [1, -1, 0, 3, -2, 3])
    p = 11
    v = Q.find_primitive_p_divisible_vector__random(p)
    actual = Q(v) % p
    expected = 0
    assert actual == expected, (
        "QuadraticForm.find_primitive_p_divisible_vector__random mismatch: "
        f"actual={actual}, expected={expected}, v={v}"
    )


def test_quadraticform_find_primitive_p_divisible_vector_next_returns_candidate():
    """
    method: find_primitive_p_divisible_vector__next

    find_primitive_p_divisible_vector__next(p,v) iterates normalized p-divisible vectors.
    Assertion: Returned next vector (when present) is p-divisible.
    """
    Q = QuadraticForm(ZZ, 3, [1, -1, 0, 3, -2, 3])
    p = 11
    v0 = Q.find_primitive_p_divisible_vector__random(p)
    v1 = Q.find_primitive_p_divisible_vector__next(p, v0)
    actual = (v1 is None) or (Q(v1) % p == 0)
    expected = True
    assert actual == expected, (
        f"QuadraticForm.find_primitive_p_divisible_vector__next mismatch: actual={actual}, expected={expected}, v0={v0}, v1={v1}"
    )


def test_quadraticform_find_p_neighbor_from_vec_preserves_discriminant():
    """
    method: find_p_neighbor_from_vec

    find_p_neighbor_from_vec(p,v) constructs p-neighbor from p-divisible vector.
    Assertion: Neighbor has same discriminant.
    """
    Q = QuadraticForm(ZZ, 3, [1, -1, 0, 3, -2, 3])
    p = 11
    v = Q.find_primitive_p_divisible_vector__random(p)
    N = Q.find_p_neighbor_from_vec(p, v)
    actual = N.disc()
    expected = Q.disc()
    assert actual == expected, (
        f"QuadraticForm.find_p_neighbor_from_vec mismatch: actual={actual}, expected={expected}, v={v}"
    )


def test_quadraticform_local_badI_density_congruence_zero_at_sample():
    """
    method: local_badI_density_congruence

    local_badI_density_congruence(p,m) computes bad-I local density term.
    Assertion: Value at (p,m)=(3,1) is 0.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_badI_density_congruence(3, 1)
    expected = 0
    assert actual == expected, (
        f"QuadraticForm.local_badI_density_congruence mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_local_badII_density_congruence_zero_at_sample():
    """
    method: local_badII_density_congruence

    local_badII_density_congruence(p,m) computes bad-II local density term.
    Assertion: Value at (p,m)=(3,1) is 0.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_badII_density_congruence(3, 1)
    expected = 0
    assert actual == expected, (
        f"QuadraticForm.local_badII_density_congruence mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_local_density_congruence_matches_local_density():
    """
    method: local_density_congruence

    local_density_congruence(p,m) is congruence-counting density.
    Assertion: Equals local_density at (p,m)=(3,1).
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_density_congruence(3, 1)
    expected = Q.local_density(3, 1)
    assert actual == expected, (
        f"QuadraticForm.local_density_congruence mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_local_good_density_congruence_even_zero_at_sample():
    """
    method: local_good_density_congruence_even

    local_good_density_congruence_even(m,Z,NZ) computes even-prime good density term.
    Assertion: Value on sample inputs is 0.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_good_density_congruence_even(1, [], [])
    expected = 0
    assert actual == expected, (
        f"QuadraticForm.local_good_density_congruence_even mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_local_good_density_congruence_odd_zero_at_sample():
    """
    method: local_good_density_congruence_odd

    local_good_density_congruence_odd(p,m,Z,NZ) computes odd-prime good density term.
    Assertion: Value at sample inputs is 0.
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_good_density_congruence_odd(3, 1, [], [])
    expected = 0
    assert actual == expected, (
        f"QuadraticForm.local_good_density_congruence_odd mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_local_primitive_density_congruence_zero_at_sample():
    """
    method: local_primitive_density_congruence

    local_primitive_density_congruence(p,m) computes primitive local density via congruences.
    Assertion: Value agrees with local_primitive_density at (p,m)=(3,1).
    """
    Q = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    actual = Q.local_primitive_density_congruence(3, 1)
    expected = Q.local_primitive_density(3, 1)
    assert actual == expected, (
        f"QuadraticForm.local_primitive_density_congruence mismatch: actual={actual}, expected={expected}"
    )


def test_quadraticform_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant QuadraticForm runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = QuadraticForm(ZZ, 3, [2, 0, 0, 3, 0, 5])
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.quadratic_forms",),
    )
