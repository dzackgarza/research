from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.all import BinaryQF, ZZ, matrix
from .conftest import assert_runtime_methods_covered


def test_binaryqf_discriminant_formula():
    """
    method: discriminant

    discriminant() returns D=b^2-4ac for ax^2+bxy+cy^2.
    Assertion: Computed value matches the exact defining formula.
    """
    Q = BinaryQF(1, 2, 3)
    actual = Q.discriminant()
    expected = 2 * 2 - 4 * 1 * 3
    assert actual == expected, f"BinaryQF.discriminant mismatch: actual={actual}, expected={expected}"


def test_binaryqf_determinant_relation_to_discriminant():
    """
    method: determinant

    determinant()/det() returns det(Gram)=-D/4.
    Assertion: Determinant equals -discriminant/4 on a concrete form.
    """
    Q = BinaryQF(1, -1, 67)
    actual = Q.determinant()
    expected = -Q.discriminant() / 4
    assert actual == expected, f"BinaryQF.determinant mismatch: actual={actual}, expected={expected}"


def test_binaryqf_positive_definite_criterion_example():
    """
    method: is_positive_definite

    is_positive_definite() uses classical binary criteria D<0 and a>0.
    Assertion: x^2+y^2 is detected as positive definite.
    """
    Q = BinaryQF(1, 0, 1)
    actual = Q.is_positive_definite()
    expected = True
    assert actual is expected, (
        f"BinaryQF.is_positive_definite mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_reduced_form_preserves_discriminant():
    """
    method: reduced_form

    reduced_form() returns an equivalent reduced binary form.
    Assertion: Discriminant is invariant under reduction.
    """
    Q = BinaryQF(5, 7, 3)
    R = Q.reduced_form()
    actual = R.discriminant()
    expected = Q.discriminant()
    assert actual == expected, (
        f"BinaryQF.reduced_form discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_content_matches_coefficient_gcd():
    """
    method: content

    content() returns gcd(a,b,c) for BinaryQF(a,b,c).
    Assertion: Content equals gcd(2,4,6)=2.
    """
    Q = BinaryQF(2, 4, 6)
    actual = Q.content()
    expected = 2
    assert actual == expected, f"BinaryQF.content mismatch: actual={actual}, expected={expected}"


def test_binaryqf_is_primitive_detects_unit_content():
    """
    method: is_primitive

    is_primitive() checks whether gcd(a,b,c)=1.
    Assertion: Form (1,2,3) is primitive.
    """
    Q = BinaryQF(1, 2, 3)
    actual = Q.is_primitive()
    expected = True
    assert actual == expected, f"BinaryQF.is_primitive mismatch: actual={actual}, expected={expected}"


def test_binaryqf_polynomial_roundtrip_constructor():
    """
    method: from_polynomial

    from_polynomial(f) reconstructs the binary form from a bivariate polynomial.
    Assertion: Roundtrip preserves the discriminant.
    """
    Q = BinaryQF(3, -2, 5)
    R = BinaryQF.from_polynomial(Q.polynomial())
    actual = R.discriminant()
    expected = Q.discriminant()
    assert actual == expected, (
        f"BinaryQF.from_polynomial roundtrip mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_is_reduced_on_simple_posdef_example():
    """
    method: is_reduced

    is_reduced() checks Gauss reduction conditions.
    Assertion: x^2+y^2 is reduced.
    """
    Q = BinaryQF(1, 0, 1)
    actual = Q.is_reduced()
    expected = True
    assert actual == expected, f"BinaryQF.is_reduced mismatch: actual={actual}, expected={expected}"


def test_binaryqf_principal_has_requested_discriminant():
    """
    method: principal

    principal(D) returns the principal form of discriminant D.
    Assertion: Resulting form has discriminant -4.
    """
    Q = BinaryQF.principal(-4)
    actual = Q.discriminant()
    expected = -4
    assert actual == expected, (
        f"BinaryQF.principal discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_polynomial_evaluates_like_form():
    """
    method: polynomial

    polynomial() returns the bivariate polynomial defining the same quadratic map.
    Assertion: Polynomial value at (x,y) matches form evaluation.
    """
    Q = BinaryQF(5, 7, 3)
    f = Q.polynomial()
    actual = f(2, -1)
    expected = Q(2, -1)
    assert actual == expected, f"BinaryQF.polynomial mismatch: actual={actual}, expected={expected}"


def test_binaryqf_det_alias_matches_determinant():
    """
    method: det

    det() aliases determinant() for binary forms.
    Assertion: det equals determinant.
    """
    Q = BinaryQF(5, 7, 3)
    actual = Q.det()
    expected = Q.determinant()
    assert actual == expected, f"BinaryQF.det alias mismatch: actual={actual}, expected={expected}"


def test_binaryqf_form_class_preserves_discriminant():
    """
    method: form_class

    form_class() maps to the class-group element of the form.
    Assertion: Representative in class has the same discriminant.
    """
    Q = BinaryQF(1, 1, 3)
    C = Q.form_class()
    R = C.form()
    actual = R.discriminant()
    expected = Q.discriminant()
    assert actual == expected, (
        f"BinaryQF.form_class discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_has_fundamental_discriminant_true_example():
    """
    method: has_fundamental_discriminant

    has_fundamental_discriminant() checks if discriminant is fundamental.
    Assertion: Form with discriminant -11 is fundamental.
    """
    Q = BinaryQF(1, 1, 3)
    actual = Q.has_fundamental_discriminant()
    expected = True
    assert actual == expected, (
        f"BinaryQF.has_fundamental_discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_is_equivalent_reflexive():
    """
    method: is_equivalent

    is_equivalent(other) checks proper equivalence of forms.
    Assertion: Any form is equivalent to itself.
    """
    Q = BinaryQF(5, 7, 3)
    actual = Q.is_equivalent(Q)
    expected = True
    assert actual == expected, f"BinaryQF.is_equivalent mismatch: actual={actual}, expected={expected}"


def test_binaryqf_indefinite_aliases_match_on_indefinite_example():
    """
    method: is_indef

    is_indef()/is_indefinite() are equivalent indefinite checks.
    Assertion: Both return True on x^2+xy-y^2.
    """
    Q = BinaryQF(1, 1, -1)
    actual = (Q.is_indef(), Q.is_indefinite())
    expected = (True, True)
    assert actual == expected, f"BinaryQF.is_indef aliases mismatch: actual={actual}, expected={expected}"


def test_binaryqf_is_indefinite_true_for_positive_discriminant():
    """
    method: is_indefinite

    is_indefinite() detects positive-discriminant forms.
    Assertion: x^2+xy-y^2 is indefinite.
    """
    Q = BinaryQF(1, 1, -1)
    actual = Q.is_indefinite()
    expected = True
    assert actual == expected, f"BinaryQF.is_indefinite mismatch: actual={actual}, expected={expected}"


def test_binaryqf_negative_definite_aliases_match():
    """
    method: is_negative_definite

    is_negative_definite()/is_negdef() are equivalent negative-definite predicates.
    Assertion: For -x^2-y^2 both are True.
    """
    Q = BinaryQF(-1, 0, -1)
    actual = (Q.is_negative_definite(), Q.is_negdef())
    expected = (True, True)
    assert actual == expected, (
        f"BinaryQF.is_negative_definite aliases mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_is_negdef_true_for_negative_identity():
    """
    method: is_negdef

    is_negdef() checks negative definiteness.
    Assertion: -x^2-y^2 is negative definite.
    """
    Q = BinaryQF(-1, 0, -1)
    actual = Q.is_negdef()
    expected = True
    assert actual == expected, f"BinaryQF.is_negdef mismatch: actual={actual}, expected={expected}"


def test_binaryqf_nonsingular_is_logical_negation_of_singular():
    """
    method: is_nonsingular

    is_nonsingular() is equivalent to not is_singular().
    Assertion: Relation holds on a nondegenerate form.
    """
    Q = BinaryQF(5, 7, 3)
    actual = Q.is_nonsingular()
    expected = (not Q.is_singular())
    assert actual == expected, (
        f"BinaryQF.is_nonsingular mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_is_posdef_alias_matches_positive_definite():
    """
    method: is_posdef

    is_posdef() aliases is_positive_definite().
    Assertion: Alias values agree for x^2+y^2.
    """
    Q = BinaryQF(1, 0, 1)
    actual = Q.is_posdef()
    expected = Q.is_positive_definite()
    assert actual == expected, f"BinaryQF.is_posdef alias mismatch: actual={actual}, expected={expected}"


def test_binaryqf_is_reducible_false_for_primitive_nonsquare_discriminant():
    """
    method: is_reducible

    is_reducible() tests reducibility over Z.
    Assertion: x^2+xy+3y^2 is irreducible.
    """
    Q = BinaryQF(1, 1, 3)
    actual = Q.is_reducible()
    expected = False
    assert actual == expected, f"BinaryQF.is_reducible mismatch: actual={actual}, expected={expected}"


def test_binaryqf_is_singular_false_for_nonzero_discriminant():
    """
    method: is_singular

    is_singular() detects discriminant zero.
    Assertion: Form with discriminant -11 is nonsingular.
    """
    Q = BinaryQF(1, 1, 3)
    actual = Q.is_singular()
    expected = False
    assert actual == expected, f"BinaryQF.is_singular mismatch: actual={actual}, expected={expected}"


def test_binaryqf_is_weakly_reduced_true_for_simple_reduced_form():
    """
    method: is_weakly_reduced

    is_weakly_reduced() checks weak reduction conditions.
    Assertion: x^2+y^2 is weakly reduced.
    """
    Q = BinaryQF(1, 0, 1)
    actual = Q.is_weakly_reduced()
    expected = True
    assert actual == expected, f"BinaryQF.is_weakly_reduced mismatch: actual={actual}, expected={expected}"


def test_binaryqf_is_zero_false_for_nonzero_form():
    """
    method: is_zero

    is_zero() checks whether all coefficients vanish.
    Assertion: Nonzero form is not zero.
    """
    Q = BinaryQF(1, 0, 1)
    actual = Q.is_zero()
    expected = False
    assert actual == expected, f"BinaryQF.is_zero mismatch: actual={actual}, expected={expected}"


def test_binaryqf_matrix_action_left_identity_fixes_form():
    """
    method: matrix_action_left

    matrix_action_left(M) applies left linear change by M.
    Assertion: Identity action fixes the form.
    """
    Q = BinaryQF(5, 7, 3)
    I = matrix(ZZ, [[1, 0], [0, 1]])
    actual = Q.matrix_action_left(I)
    expected = Q
    assert actual == expected, (
        f"BinaryQF.matrix_action_left identity mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_matrix_action_right_identity_fixes_form():
    """
    method: matrix_action_right

    matrix_action_right(M) applies right linear change by M.
    Assertion: Identity action fixes the form.
    """
    Q = BinaryQF(5, 7, 3)
    I = matrix(ZZ, [[1, 0], [0, 1]])
    actual = Q.matrix_action_right(I)
    expected = Q
    assert actual == expected, (
        f"BinaryQF.matrix_action_right identity mismatch: actual={actual}, expected={expected}"
    )


def test_binaryqf_complex_point_is_root_of_specialization():
    """
    method: complex_point

    complex_point() gives a complex root of ax^2+bxy+cy^2 at y=1.
    Assertion: a z^2 + b z + c is numerically near zero.
    """
    Q = BinaryQF(5, 7, 3)
    z = Q.complex_point()
    actual = abs(5 * z * z + 7 * z + 3) < 1e-10
    expected = True
    assert actual == expected, (
        f"BinaryQF.complex_point root check mismatch: actual={actual}, expected={expected}, z={z}"
    )


def test_binaryqf_cycle_contains_equivalent_forms():
    """
    method: cycle

    cycle() returns a reduction cycle for reduced indefinite forms.
    Assertion: Cycle has expected length 3 and every form is equivalent to base form.
    """
    Q = BinaryQF(2, 3, -1).reduced_form()
    cyc = Q.cycle()
    actual = (len(cyc), all(Q.is_equivalent(R) for R in cyc))
    expected = (3, True)
    assert actual == expected, f"BinaryQF.cycle mismatch: actual={actual}, expected={expected}, cycle={cyc}"


def test_binaryqf_small_prime_value_is_represented():
    """
    method: small_prime_value

    small_prime_value() returns a represented prime (or small value) for primitive forms.
    Assertion: Returned value is represented by the form.
    """
    Q = BinaryQF(5, 7, 3)
    p = Q.small_prime_value()
    sol = Q.solve_integer(p)
    actual = Q(*sol) == p
    expected = True
    assert actual == expected, (
        f"BinaryQF.small_prime_value representation mismatch: actual={actual}, expected={expected}, p={p}, sol={sol}"
    )


def test_binaryqf_solve_integer_returns_exact_representation():
    """
    method: solve_integer

    solve_integer(n) returns integer coordinates representing n when possible.
    Assertion: Returned coordinates evaluate to the requested integer.
    """
    Q = BinaryQF(5, 7, 3)
    n = 1
    x, y = Q.solve_integer(n)
    actual = Q(x, y)
    expected = n
    assert actual == expected, (
        f"BinaryQF.solve_integer mismatch: actual={actual}, expected={expected}, solution={(x, y)}"
    )


def test_binaryqf_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant BinaryQF runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    sample = BinaryQF(5, 7, 3)
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.quadratic_forms.binary_qf",),
    )
