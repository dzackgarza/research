# TernaryQF Methods

This document lists the methods associated with the `TernaryQF` class in SageMath, which handles quadratic forms in three variables with integer coefficients.

## Construction

* `TernaryQF(entries: list) -> TernaryQF`
    * Constructor from a list of coefficients `[a, b, c, d, e, f]` representing ax^2 + by^2 + cz^2 + dyz + exz + fxy.

## Specific Algorithms

* `.is_eisenstein_reduced() -> Boolean`
    * **⚠️ Requires positive-definite form.** Returns `True` if in unique Eisenstein reduced form.
* `.reduced_form_eisenstein() -> TernaryQF`
     * **⚠️ Requires positive-definite form.** Returns an equivalent Eisenstein-reduced ternary form.
* `.automorphisms(slow: bool = True) -> list[Matrix]`
    * **⚠️ Requires definite form (positive or negative).** Raises ValueError on indefinite forms. `slow=True` uses comprehensive method; `slow=False` uses lookup table (reduced forms only).
* `.is_equivalent(other: TernaryQF) -> Boolean`
    * **⚠️ Requires positive-definite form.** Tests for equivalence with another ternary form.

## Basic Invariants

* `.matrix() -> Matrix`
    * Returns the 3x3 symmetric matrix.
* `.disc() -> Integer`
     * Returns the discriminant of the form.
* `.coefficient(n: int) -> Integer`
     * Returns the n-th coefficient (0 ≤ n ≤ 5) for ax²+by²+cz²+dyz+exz+fxy.
* `.coefficients() -> tuple[Integer, ...]`
     * Returns full coefficient tuple (a, b, c, d, e, f).
* `.content() -> Integer`
    * Returns GCD of all coefficients.
* `.divisor() -> Integer`
    * Returns divisor (GCD of coefficients).
* `.level() -> Integer`
    * Returns level of the ternary form.
* `.polynomial() -> Polynomial`
    * Returns polynomial representation.

## Reduction & Equivalence

* `.reduced_form_eisenstein() -> TernaryQF`
    * **⚠️ Requires positive-definite form.** Eisenstein reduction (variant of `reduced_form()`).
* `.reciprocal_reduced() -> TernaryQF`
    * **⚠️ Requires positive-definite form.** Returns reciprocal reduction.

## Automorphisms & Symmetry

* `.number_of_automorphisms() -> int`
    * Returns count of automorphisms (det ±1).
* `.automorphism_spin_norm() -> int`
    * Returns spin norm of automorphisms.
* `.automorphism_symmetries() -> list`
    * Returns symmetry group structure.
* `.symmetry() -> list`
    * Returns symmetry properties of the form.
* `.possible_automorphisms() -> list`
    * Returns possible automorphism structure.

## Neighbors & Local Analysis

* `.find_p_neighbors() -> list[TernaryQF]`
    * Finds all p-neighbors of this ternary form (p-adic neighbor enumeration).
* `.find_p_neighbor_from_vec(p: Integer, v: Vector) -> TernaryQF`
    * Finds p-neighbor from primitive p-divisible vector v.
* `.find_zeros_mod_p(p: Integer) -> list[Vector]`
    * Finds isotropic vectors (zeros) modulo p.
* `.pseudorandom_primitive_zero_mod_p(p: Integer) -> Vector`
    * Finds random primitive isotropic vector modulo p.

## Form Structure

* `.primitive() -> TernaryQF`
    * Returns primitive part (content removed).
* `.is_primitive() -> bool`
    * Tests if form is primitive (gcd=1).
* `.adjoint() -> TernaryQF`
    * Returns adjoint form.
* `.basic_lemma() -> Rational`
    * Returns value from basic lemma for representation.
* `.quadratic_form() -> QuadraticForm`
    * Converts ternary form to general QuadraticForm object.
* `.scale_by_factor(c) -> TernaryQF`
    * Scales all coefficients by factor c.

## Invariants

* `.omega() -> Rational`
    * Omega invariant for ternary forms.
* `.xi() -> Rational`
    * Xi invariant.
* `.xi_rec() -> Rational`
    * Recursive xi invariant.
* `.reciprocal() -> TernaryQF`
    * Returns reciprocal form (adjoint/determinant variant).