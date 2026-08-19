# BinaryQF Methods

This document lists the methods associated with the `BinaryQF` class in SageMath (`sage.quadratic_forms.binary_qf`). This class represents binary quadratic forms ax^2 + bxy + cy^2.

## Construction

* `BinaryQF(a: Integer, b: Integer, c: Integer) -> BinaryQF`
    * Constructor from coefficients a, b, c.
* `BinaryQF(coeffs: list) -> BinaryQF`
    * Constructor from a list `[a, b, c]`.

## Properties

* `.discriminant() -> Integer`
    * Returns the discriminant b^2 - 4ac.
* `.is_positive_definite() -> Boolean`
    * Returns `True` if positive definite.
* `.is_negative_definite() -> Boolean`
    * Returns `True` if negative definite.
* `.is_indefinite() -> Boolean`
    * Returns `True` if indefinite.
* `.is_reduced() -> Boolean`
    * Returns `True` if the form is reduced (in the standard fundamental domain).
* `.is_primitive() -> Boolean`
    * Returns `True` if gcd(a, b, c) = 1.

## Reduction & Equivalence

* `.reduced_form(algorithm: str = 'default') -> BinaryQF`
    * Returns the equivalent reduced binary quadratic form.
* `.is_equivalent(other: BinaryQF) -> Boolean`
    * Returns `True` if properly equivalent (under SL_2(Z)).
* `.equivalent_form_and_matrix() -> tuple[BinaryQF, Matrix]`
    * Returns the reduced form and the unimodular transformation matrix.

## Composition & Arithmetic

* `.composition(other: BinaryQF) -> BinaryQF`
    * Returns the composition (Dirichlet composition) of two forms.
* `.inverse() -> BinaryQF`
    * Returns the inverse form in the class group.
* `.matrix_action(M: Matrix) -> BinaryQF`
    * Returns the form transformed by the 2x2 matrix `M`.

## Representation

* `.solve_integer(n: Integer) -> tuple[Integer, Integer]`
    * Returns a solution (x, y) such that Q(x, y) = n.
* `.representation_number(n: Integer) -> Integer`
    * Returns the number of representations of n.

## Class Field Theory

* `.complex_point() -> ComplexNumber`
    * **⚠️ Requires positive-definite form.** Returns the root in the upper half-plane.
* `.cycle() -> list[BinaryQF]`
    * **⚠️ Requires indefinite form.** Returns the cycle of reduced forms.

## Form Variants & Aliases

* `.det() -> Integer`
    * Determinant of form (b²-4ac for ax²+bxy+cy²).
* `.determinant() -> Integer`
    * Determinant (alias for `det()`).
* `.is_posdef() -> Boolean`
    * Tests if form is positive definite (abbreviation of `is_positive_definite()`).
* `.is_negdef() -> Boolean`
    * Tests if form is negative definite (abbreviation of `is_negative_definite()`).
* `.is_indef() -> Boolean`
    * Tests if form is indefinite (abbreviation of `is_indefinite()`).
* `.is_singular() -> Boolean`
    * Tests if form is singular (determinant = 0).
* `.is_nonsingular() -> Boolean`
    * Tests if form is non-singular (determinant ≠ 0).

## Form Properties

* `.content() -> Integer`
    * Returns GCD of coefficients a, b, c.
* `.has_fundamental_discriminant() -> Boolean`
    * Tests if discriminant b²-4ac is fundamental (not divisible by any perfect square > 1).
* `.is_weakly_reduced() -> Boolean`
    * Tests if form satisfies weaker reduction criteria (weaker than standard reduced form).
* `.is_reducible() -> Boolean`
    * Tests if form is reducible over ℚ.
* `.is_zero() -> Boolean`
    * Tests if form is identically zero.
* `.principal() -> Boolean`
    * Tests if form is in the principal genus (det = ±1).
* `.small_prime_value() -> Integer`
    * Returns smallest prime value represented by the form.

## Form Construction & Conversion

* `.from_polynomial(p) -> BinaryQF`
    * **Static/class method.** Constructs binary form from polynomial.
* `.polynomial() -> Polynomial`
    * Returns polynomial representation ax²+bxy+cy².
* `.matrix_action_left(M: Matrix) -> BinaryQF`
    * Applies matrix action from left.
* `.matrix_action_right(M: Matrix) -> BinaryQF`
    * Applies matrix action from right.