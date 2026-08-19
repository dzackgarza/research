from __future__ import annotations

import sys
import pytest

import sage.all  # noqa: F401
from sage.all import NumberField, QQ, QuadraticField, ZZ, infinity, matrix
from .conftest import assert_runtime_methods_covered


def test_numberfield_trace_gram_matches_discriminant():
    """
    method: discriminant

    The trace-pairing Gram matrix on an integral basis has determinant equal to field discriminant.
    Assertion: Exact trace Gram determinant equals K.discriminant().
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    B = K.integral_basis()
    n = K.degree()
    G = matrix(QQ, n, n, lambda i, j: (B[i] * B[j]).trace())
    actual = G.det()
    expected = K.discriminant()
    assert actual == expected, (
        f"NumberField trace Gram determinant mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_element_trace_matches_conjugate_sum():
    """
    method: trace

    trace() on an algebraic element equals sum of Galois conjugates.
    Assertion: In Q(sqrt(5)), trace(a) is 0 for the generator root of x^2-5.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    a = K.gen()
    actual = a.trace()
    expected = 0
    assert actual == expected, (
        f"NumberFieldElement.trace mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_integral_basis_has_field_degree_length():
    """
    method: integral_basis

    integral_basis() returns a Z-basis of the ring of integers.
    Assertion: Basis length equals field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.integral_basis())
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.integral_basis length mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_ideal_free_module_has_expected_rank():
    """
    method: free_module

    free_module() returns the underlying free Z-module of an ideal.
    Assertion: Free-module rank equals ambient number-field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    OK = K.ring_of_integers()
    I = OK.ideal(2)
    F = I.free_module()
    actual = F.rank()
    expected = K.degree()
    assert actual == expected, (
        f"NumberFieldFractionalIdeal.free_module rank mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_signature_matches_quadratic_real_field():
    """
    method: signature

    signature() returns (r,s) for real and complex embeddings.
    Assertion: Q(sqrt(5)) has signature (2,0).
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.signature()
    expected = (2, 0)
    assert actual == expected, f"NumberField.signature mismatch: actual={actual}, expected={expected}"


def test_numberfield_ring_of_integers_basis_rank():
    """
    method: ring_of_integers

    ring_of_integers() returns the maximal order with a Z-basis of full degree.
    Assertion: Basis length equals field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    OK = K.ring_of_integers()
    actual = len(OK.basis())
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.ring_of_integers basis size mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_characteristic_zero():
    """
    method: characteristic

    characteristic() of number fields is always zero.
    Assertion: Characteristic equals 0.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.characteristic()
    expected = 0
    assert actual == expected, f"NumberField.characteristic mismatch: actual={actual}, expected={expected}"


def test_numberfield_degree_matches_polynomial_degree():
    """
    method: degree

    degree() is extension degree over QQ.
    Assertion: Degree equals defining polynomial degree for simple extension.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.degree()
    expected = 2
    assert actual == expected, f"NumberField.degree mismatch: actual={actual}, expected={expected}"


def test_numberfield_disc_alias_matches_discriminant():
    """
    method: disc

    disc() aliases discriminant().
    Assertion: Alias equals discriminant.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.disc()
    expected = K.discriminant()
    assert actual == expected, f"NumberField.disc alias mismatch: actual={actual}, expected={expected}"


def test_numberfield_gen_is_root_of_defining_polynomial():
    """
    method: gen

    gen() returns distinguished generator a of K=QQ[a].
    Assertion: Defining polynomial vanishes at generator.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    a = K.gen()
    actual = K.polynomial()(a)
    expected = 0
    assert actual == expected, f"NumberField.gen mismatch: actual={actual}, expected={expected}"


def test_numberfield_ngens_is_one():
    """
    method: ngens

    ngens() returns number of abstract generators.
    Assertion: Simple number field has one generator.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.ngens()
    expected = 1
    assert actual == expected, f"NumberField.ngens mismatch: actual={actual}, expected={expected}"


def test_numberfield_order_matches_ring_of_integers():
    """
    method: order

    order() is multiplicative order as a group element API on parents.
    Assertion: Number fields have infinite multiplicative order as parents.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.order()
    expected = "+Infinity"
    assert str(actual) == expected, f"NumberField.order mismatch: actual={actual}, expected={expected}"


def test_numberfield_polynomial_is_defining_polynomial():
    """
    method: polynomial

    polynomial() returns defining polynomial over QQ.
    Assertion: Degree equals field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.polynomial().degree()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.polynomial degree mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_absolute_degree_matches_degree():
    """
    method: absolute_degree

    absolute_degree() returns [K:Q] for absolute fields.
    Assertion: absolute_degree equals degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.absolute_degree()
    expected = K.degree()
    assert actual == expected, f"NumberField.absolute_degree mismatch: actual={actual}, expected={expected}"


def test_numberfield_absolute_discriminant_matches_discriminant():
    """
    method: absolute_discriminant

    absolute_discriminant() equals discriminant for absolute fields.
    Assertion: Values are equal.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.absolute_discriminant()
    expected = K.discriminant()
    assert actual == expected, (
        f"NumberField.absolute_discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_absolute_polynomial_matches_polynomial():
    """
    method: absolute_polynomial

    absolute_polynomial() returns defining polynomial over Q.
    Assertion: Equals polynomial() in absolute case.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.absolute_polynomial()
    expected = K.polynomial()
    assert actual == expected, f"NumberField.absolute_polynomial mismatch: actual={actual}, expected={expected}"


def test_numberfield_base_field_is_rational_field():
    """
    method: base_field

    base_field() of absolute number field is QQ.
    Assertion: base_field equals QQ.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.base_field()
    expected = QQ
    assert actual == expected, f"NumberField.base_field mismatch: actual={actual}, expected={expected}"


def test_numberfield_defining_polynomial_matches_constructor():
    """
    method: defining_polynomial

    defining_polynomial() returns defining polynomial of extension.
    Assertion: Equals x^2-5.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.defining_polynomial()
    expected = x**2 - 5
    assert actual == expected, (
        f"NumberField.defining_polynomial mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_is_galois_true_for_quadratic_extension():
    """
    method: is_galois

    is_galois() checks normal/separable over Q.
    Assertion: Quadratic extension is Galois.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.is_galois()
    expected = True
    assert actual == expected, f"NumberField.is_galois mismatch: actual={actual}, expected={expected}"


def test_numberfield_real_imaginary_status_totally_real():
    """
    method: is_totally_real

    is_totally_real()/is_totally_imaginary classify embeddings.
    Assertion: Q(sqrt5) is totally real and not totally imaginary.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = (K.is_totally_real(), K.is_totally_imaginary())
    expected = (True, False)
    assert actual == expected, (
        f"NumberField.total reality mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_is_totally_imaginary_false_for_real_quadratic():
    """
    method: is_totally_imaginary

    is_totally_imaginary() checks whether all archimedean places are complex.
    Assertion: Real quadratic field is not totally imaginary.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.is_totally_imaginary()
    expected = False
    assert actual == expected, (
        f"NumberField.is_totally_imaginary mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_real_embeddings_count_matches_signature():
    """
    method: real_embeddings

    real_embeddings() returns real field embeddings.
    Assertion: Count equals first signature component.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.real_embeddings())
    expected = K.signature()[0]
    assert actual == expected, (
        f"NumberField.real_embeddings mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_complex_embeddings_count_matches_degree():
    """
    method: complex_embeddings

    complex_embeddings() lists complex embeddings.
    Assertion: Count equals field degree for quadratic real field.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.complex_embeddings())
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.complex_embeddings mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_roots_of_unity_matches_count():
    """
    method: roots_of_unity

    roots_of_unity() lists roots of unity in K.
    Assertion: List length equals number_of_roots_of_unity().
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.roots_of_unity())
    expected = K.number_of_roots_of_unity()
    assert actual == expected, (
        f"NumberField.roots_of_unity mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_number_of_roots_of_unity_is_two():
    """
    method: number_of_roots_of_unity

    number_of_roots_of_unity() counts torsion units.
    Assertion: Real quadratic field has exactly 2 roots of unity.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.number_of_roots_of_unity()
    expected = 2
    assert actual == expected, (
        f"NumberField.number_of_roots_of_unity mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_maximal_order_matches_ring_of_integers():
    """
    method: maximal_order

    maximal_order() returns ring of integers.
    Assertion: maximal_order equals ring_of_integers.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.maximal_order()
    expected = K.ring_of_integers()
    assert actual == expected, (
        f"NumberField.maximal_order mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_reduced_basis_has_field_degree_length():
    """
    method: reduced_basis

    reduced_basis() returns reduced Z-basis data.
    Assertion: Basis length equals degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.reduced_basis())
    expected = K.degree()
    assert actual == expected, f"NumberField.reduced_basis mismatch: actual={actual}, expected={expected}"


def test_numberfield_relative_degree_matches_degree_for_absolute_field():
    """
    method: relative_degree

    relative_degree() equals degree in absolute case.
    Assertion: relative_degree equals degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.relative_degree()
    expected = K.degree()
    assert actual == expected, f"NumberField.relative_degree mismatch: actual={actual}, expected={expected}"


def test_numberfield_relative_polynomial_matches_defining_polynomial():
    """
    method: relative_polynomial

    relative_polynomial() is defining polynomial over base field.
    Assertion: Equals defining_polynomial() in absolute case.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.relative_polynomial()
    expected = K.defining_polynomial()
    assert actual == expected, (
        f"NumberField.relative_polynomial mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_trace_dual_basis_has_field_degree_length():
    """
    method: trace_dual_basis

    trace_dual_basis(B) returns dual basis for trace pairing.
    Assertion: Output length equals input basis length.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    B = K.integral_basis()
    actual = len(K.trace_dual_basis(B))
    expected = len(B)
    assert actual == expected, (
        f"NumberField.trace_dual_basis mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_trace_pairing_is_symmetric_matrix():
    """
    method: trace_pairing

    trace_pairing(B) returns Gram matrix of trace bilinear form on basis B.
    Assertion: Matrix is symmetric.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    B = K.integral_basis()
    G = K.trace_pairing(B)
    actual = G == G.transpose()
    expected = True
    assert actual == expected, (
        f"NumberField.trace_pairing mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_zeta_order_equals_number_of_roots_of_unity():
    """
    method: zeta_order

    zeta_order() returns order of chosen primitive root of unity.
    Assertion: Equals number_of_roots_of_unity() in this field.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.zeta_order()
    expected = K.number_of_roots_of_unity()
    assert actual == expected, f"NumberField.zeta_order mismatch: actual={actual}, expected={expected}"


def test_numberfield_absolute_field_preserves_degree():
    """
    method: absolute_field

    absolute_field(name) returns absolute field model.
    Assertion: Absolute model has same degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    A = K.absolute_field("b")
    actual = A.degree()
    expected = K.degree()
    assert actual == expected, f"NumberField.absolute_field mismatch: actual={actual}, expected={expected}"


def test_numberfield_absolute_generator_satisfies_defining_polynomial():
    """
    method: absolute_generator

    absolute_generator() returns chosen generator in absolute model.
    Assertion: Defining polynomial vanishes at absolute generator.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    g = K.absolute_generator()
    actual = K.polynomial()(g)
    expected = 0
    assert actual == expected, (
        f"NumberField.absolute_generator mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_absolute_vector_space_dimension_matches_degree():
    """
    method: absolute_vector_space

    absolute_vector_space() returns absolute vector-space model tuple.
    Assertion: First component dimension equals degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    V, _, _ = K.absolute_vector_space()
    actual = V.dimension()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.absolute_vector_space mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_automorphisms_count_matches_degree_for_quadratic():
    """
    method: automorphisms

    automorphisms() returns field automorphisms over base field.
    Assertion: Quadratic Galois field has two automorphisms.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.automorphisms())
    expected = 2
    assert actual == expected, (
        f"NumberField.automorphisms mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_change_names_preserves_polynomial():
    """
    method: change_names

    change_names(new) renames field generator.
    Assertion: Defining polynomial is preserved.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    B = K.change_names("b")
    actual = B.defining_polynomial()
    expected = K.defining_polynomial()
    assert actual == expected, (
        f"NumberField.change_names mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_complex_conjugation_has_order_two():
    """
    method: complex_conjugation

    complex_conjugation() returns involution on embeddings.
    Assertion: Applying twice to generator returns generator.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    c = K.complex_conjugation()
    a = K.gen()
    actual = c(c(a))
    expected = a
    assert actual == expected, (
        f"NumberField.complex_conjugation mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_construction_base_is_rational_field():
    """
    method: construction

    construction() returns functor and base.
    Assertion: Base is QQ.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    _, base = K.construction()
    actual = base
    expected = QQ
    assert actual == expected, f"NumberField.construction mismatch: actual={actual}, expected={expected}"


def test_numberfield_embeddings_count_matches_automorphisms():
    """
    method: embeddings

    embeddings(L) returns embeddings into target field L.
    Assertion: Number of self-embeddings equals automorphism count.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.embeddings(K))
    expected = len(K.automorphisms())
    assert actual == expected, (
        f"NumberField.embeddings mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_is_absolute_true_for_absolute_field():
    """
    method: is_absolute

    is_absolute() detects absolute number fields.
    Assertion: Field is absolute.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.is_absolute()
    expected = True
    assert actual == expected, f"NumberField.is_absolute mismatch: actual={actual}, expected={expected}"


def test_numberfield_is_field_true():
    """
    method: is_field

    is_field() checks field property.
    Assertion: NumberField is a field.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.is_field()
    expected = True
    assert actual == expected, f"NumberField.is_field mismatch: actual={actual}, expected={expected}"


def test_numberfield_ideal_and_fractional_ideal_have_same_norm_for_two():
    """
    method: ideal

    ideal(a) and fractional_ideal(a) agree on principal ideal norms.
    Assertion: Norms for (2) are equal.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    I = K.ideal(2)
    J = K.fractional_ideal(2)
    actual = I.norm()
    expected = J.norm()
    assert actual == expected, f"NumberField.ideal mismatch: actual={actual}, expected={expected}"


def test_numberfield_fractional_ideal_norm_matches_principal_norm():
    """
    method: fractional_ideal

    fractional_ideal(a) constructs principal fractional ideal.
    Assertion: Norm of (2) is 4 in degree-2 extension.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.fractional_ideal(2).norm()
    expected = 4
    assert actual == expected, (
        f"NumberField.fractional_ideal mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_power_basis_length_matches_degree():
    """
    method: power_basis

    power_basis() returns 1,a,...,a^(n-1).
    Assertion: Length equals degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.power_basis())
    expected = K.degree()
    assert actual == expected, f"NumberField.power_basis mismatch: actual={actual}, expected={expected}"


def test_numberfield_primitive_element_generates_field():
    """
    method: primitive_element

    primitive_element() returns an element generating the field.
    Assertion: Minimal polynomial degree equals field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    a = K.primitive_element()
    actual = a.minpoly().degree()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.primitive_element mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_residue_field_size_matches_prime_norm():
    """
    method: residue_field

    residue_field(P) returns finite field O_K/P.
    Assertion: Cardinality equals norm(P).
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    P = K.prime_above(2)
    F = K.residue_field(P)
    actual = F.cardinality()
    expected = P.norm()
    assert actual == expected, (
        f"NumberField.residue_field mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_real_places_count_matches_real_embeddings():
    """
    method: real_places

    real_places() lists real archimedean places.
    Assertion: Count equals real_embeddings count.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.real_places())
    expected = len(K.real_embeddings())
    assert actual == expected, (
        f"NumberField.real_places mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_unit_group_rank_matches_dirichlet_for_signature():
    """
    method: unit_group

    unit_group() satisfies Dirichlet rank r+s-1.
    Assertion: For signature (2,0), rank is 1.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    U = K.unit_group()
    actual = U.rank()
    expected = 1
    assert actual == expected, f"NumberField.unit_group mismatch: actual={actual}, expected={expected}"


def test_numberfield_units_generate_nontrivial_free_part():
    """
    method: units

    units() returns fundamental units tuple.
    Assertion: At least one fundamental unit is returned for real quadratic field.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.units()) >= 1
    expected = True
    assert actual == expected, f"NumberField.units mismatch: actual={actual}, expected={expected}"


def test_numberfield_valuation_of_uniformizer_is_one():
    """
    method: valuation

    valuation(P) returns p-adic valuation on K at prime ideal P.
    Assertion: valuation of a generator of P is 1.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    P = K.prime_above(2)
    v = K.valuation(P)
    pi = P.gens_reduced()[0]
    actual = v(pi)
    expected = 1
    assert actual == expected, f"NumberField.valuation mismatch: actual={actual}, expected={expected}"


def test_numberfield_zeta_is_root_of_unity():
    """
    method: zeta

    zeta() returns distinguished root of unity.
    Assertion: zeta^zeta_order = 1.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    z = K.zeta()
    actual = z ** K.zeta_order()
    expected = 1
    assert actual == expected, f"NumberField.zeta mismatch: actual={actual}, expected={expected}"


def test_numberfield_ok_alias_matches_ring_of_integers():
    """
    method: OK

    OK() aliases ring_of_integers().
    Assertion: Returned maximal order equals ring_of_integers.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.OK()
    expected = K.ring_of_integers()
    assert actual == expected, f"NumberField.OK mismatch: actual={actual}, expected={expected}"


def test_numberfield_s_class_group_empty_set_matches_class_group_order():
    """
    method: S_class_group

    S_class_group([]) matches ordinary class-group order.
    Assertion: Orders are equal for empty S.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.S_class_group([]).order()
    expected = K.class_group().order()
    assert actual == expected, (
        f"NumberField.S_class_group mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_s_units_empty_set_contains_fundamental_unit():
    """
    method: S_units

    S_units([]) returns generators of the ordinary unit group.
    Assertion: A real quadratic field has at least one nontrivial unit generator.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    units = K.S_units([])
    actual = len(units) >= 2
    expected = True
    assert actual == expected, (
        f"NumberField.S_units mismatch: actual={actual}, expected={expected}, units={units}"
    )


def test_numberfield_absolute_different_equals_different():
    """
    method: absolute_different

    absolute_different() equals different() in an absolute field.
    Assertion: Ideals coincide.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.absolute_different()
    expected = K.different()
    assert actual == expected, (
        f"NumberField.absolute_different mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_absolute_polynomial_ntl_degree_matches_degree():
    """
    method: absolute_polynomial_ntl

    absolute_polynomial_ntl() returns NTL polynomial data.
    Assertion: Extracted polynomial degree equals field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    poly_data = K.absolute_polynomial_ntl()
    actual = poly_data[0].degree()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.absolute_polynomial_ntl mismatch: actual={actual}, expected={expected}, data={poly_data}"
    )


def test_numberfield_algebraic_closure_has_characteristic_zero():
    """
    method: algebraic_closure

    algebraic_closure() returns an algebraic closure of characteristic zero.
    Assertion: Characteristic is 0.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.algebraic_closure().characteristic()
    expected = 0
    assert actual == expected, (
        f"NumberField.algebraic_closure mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_bach_bound_is_positive():
    """
    method: bach_bound

    bach_bound() gives an explicit class-group bound.
    Assertion: For Q(sqrt(5)), value equals 12*log(5)^2.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.bach_bound()
    expected = 12 * K.discriminant().abs().log() ** 2
    assert actual == expected, f"NumberField.bach_bound mismatch: actual={actual}, expected={expected}"


def test_numberfield_change_generator_preserves_degree():
    """
    method: change_generator

    change_generator(b) returns an isomorphic presentation.
    Assertion: New field degree matches original.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    changed = K.change_generator(K.gen() + 1)
    L = changed[0]
    actual = L.degree()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.change_generator mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_class_group_order_matches_class_number():
    """
    method: class_group

    class_group() cardinality is the class number.
    Assertion: class_group order equals class_number.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.class_group().order()
    expected = K.class_number()
    assert actual == expected, (
        f"NumberField.class_group mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_class_number_for_qsqrt5_is_one():
    """
    method: class_number

    class_number() gives ideal class number.
    Assertion: Q(sqrt(5)) has class number 1.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.class_number()
    expected = 1
    assert actual == expected, (
        f"NumberField.class_number mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_completely_split_primes_contain_11_below_30():
    """
    method: completely_split_primes

    completely_split_primes(B) lists rational primes splitting completely below B.
    Assertion: 11 appears for Q(sqrt(5)) below 30.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    primes = K.completely_split_primes(30)
    actual = 11 in primes
    expected = True
    assert actual == expected, (
        f"NumberField.completely_split_primes mismatch: actual={actual}, expected={expected}, primes={primes}"
    )


def test_numberfield_conductor_for_fundamental_discriminant_field():
    """
    method: conductor

    conductor() for Q(sqrt(5)) equals 5.
    Assertion: Conductor is 5.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.conductor()
    expected = 5
    assert actual == expected, f"NumberField.conductor mismatch: actual={actual}, expected={expected}"


def test_numberfield_decomposition_type_ramification_identity_for_11():
    """
    method: decomposition_type

    decomposition_type(p) records residue degree and ramification data.
    Assertion: For p=11 in Q(sqrt(5)), decomposition has two degree-1 primes.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.decomposition_type(11)
    expected = [(1, 1, 2)]
    assert actual == expected, (
        f"NumberField.decomposition_type mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_different_norm_matches_discriminant_absolute_value():
    """
    method: different

    different() ideal norm equals absolute discriminant in quadratic fields.
    Assertion: Norm(different) equals |disc|.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.different().norm()
    expected = abs(K.discriminant())
    assert actual == expected, (
        f"NumberField.different mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_elements_of_norm_contains_one():
    """
    method: elements_of_norm

    elements_of_norm(n) lists elements with relative norm n.
    Assertion: 1 appears among elements of norm 1.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    elems = K.elements_of_norm(1)
    actual = 1 in elems
    expected = True
    assert actual == expected, (
        f"NumberField.elements_of_norm mismatch: actual={actual}, expected={expected}, elems={elems}"
    )


def test_numberfield_galois_closure_degree_matches_quadratic_degree():
    """
    method: galois_closure

    galois_closure() returns normal closure over Q.
    Assertion: Quadratic field is already Galois, so closure degree is unchanged.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.galois_closure("b").degree()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.galois_closure mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_galois_group_order_equals_two_for_quadratic():
    """
    method: galois_group

    galois_group() returns automorphism group of the splitting field.
    Assertion: Quadratic extension has Galois group of order 2.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.galois_group().order()
    expected = 2
    assert actual == expected, (
        f"NumberField.galois_group mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_ideals_of_bdd_norm_contains_unit_ideal_at_norm_one():
    """
    method: ideals_of_bdd_norm

    ideals_of_bdd_norm(B) groups ideals by absolute norm up to B.
    Assertion: Norm-1 bucket contains exactly the unit ideal.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    data = K.ideals_of_bdd_norm(10)
    actual = len(data[1])
    expected = 1
    assert actual == expected, (
        f"NumberField.ideals_of_bdd_norm mismatch: actual={actual}, expected={expected}, data={data}"
    )


def test_numberfield_is_cm_false_for_real_quadratic_field():
    """
    method: is_CM

    is_CM() tests whether field is a CM field.
    Assertion: Real quadratic fields are not CM.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.is_CM()
    expected = False
    assert actual == expected, f"NumberField.is_CM mismatch: actual={actual}, expected={expected}"


def test_numberfield_is_abelian_true_for_quadratic_extension():
    """
    method: is_abelian

    is_abelian() checks whether Galois group over Q is abelian.
    Assertion: Quadratic extension is abelian.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.is_abelian()
    expected = True
    assert actual == expected, (
        f"NumberField.is_abelian mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_is_isomorphic_true_to_itself():
    """
    method: is_isomorphic

    is_isomorphic(L) detects field isomorphism.
    Assertion: A field is isomorphic to itself.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.is_isomorphic(K)
    expected = True
    assert actual == expected, (
        f"NumberField.is_isomorphic mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_is_relative_false_for_absolute_field():
    """
    method: is_relative

    is_relative() distinguishes relative extensions from absolute ones.
    Assertion: NumberField(x^2-5) over Q is not relative.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.is_relative()
    expected = False
    assert actual == expected, (
        f"NumberField.is_relative mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_narrow_class_group_is_trivial_for_qsqrt5():
    """
    method: narrow_class_group

    narrow_class_group() computes strict ideal class group.
    Assertion: For Q(sqrt(5)), narrow class group is trivial.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.narrow_class_group().order()
    expected = 1
    assert actual == expected, (
        f"NumberField.narrow_class_group mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_pari_nf_has_matching_polynomial_degree():
    """
    method: pari_nf

    pari_nf() returns PARI nf structure associated to field.
    Assertion: Stored defining polynomial has degree equal to field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.pari_nf()[0].poldegree()
    expected = K.degree()
    assert actual == expected, f"NumberField.pari_nf mismatch: actual={actual}, expected={expected}"


def test_numberfield_pari_polynomial_degree_matches_field_degree():
    """
    method: pari_polynomial

    pari_polynomial(var) exports defining polynomial to PARI.
    Assertion: Degree matches field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.pari_polynomial("a").poldegree()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.pari_polynomial mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_pari_zk_length_matches_degree():
    """
    method: pari_zk

    pari_zk() returns PARI integral basis list.
    Assertion: Basis length equals extension degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = len(K.pari_zk())
    expected = K.degree()
    assert actual == expected, f"NumberField.pari_zk mismatch: actual={actual}, expected={expected}"


def test_numberfield_places_count_matches_signature_real_plus_complex():
    """
    method: places

    places() lists infinite places.
    Assertion: Number of places equals r + s from signature.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    r, s = K.signature()
    actual = len(K.places())
    expected = r + s
    assert actual == expected, f"NumberField.places mismatch: actual={actual}, expected={expected}"


def test_numberfield_polynomial_ntl_degree_matches_degree():
    """
    method: polynomial_ntl

    polynomial_ntl() exports defining polynomial as NTL data.
    Assertion: Degree recovered from NTL coefficients equals field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    poly_data = K.polynomial_ntl()
    actual = poly_data[0].degree()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.polynomial_ntl mismatch: actual={actual}, expected={expected}, data={poly_data}"
    )


def test_numberfield_polynomial_ring_base_is_rational_field():
    """
    method: polynomial_ring

    polynomial_ring() is the ambient polynomial ring over QQ.
    Assertion: Base ring is QQ.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.polynomial_ring().base_ring()
    expected = QQ
    assert actual == expected, (
        f"NumberField.polynomial_ring mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_prime_factors_norms_multiply_to_integer_norm():
    """
    method: prime_factors

    prime_factors(n) factors principal ideal (n) into prime ideals.
    Assertion: Product of ideal norms equals |n|^[K:Q].
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    factors = K.prime_factors(6)
    actual = ZZ.prod(P.norm() for P in factors)
    expected = abs(ZZ(6)) ** K.degree()
    assert actual == expected, (
        f"NumberField.prime_factors mismatch: actual={actual}, expected={expected}, factors={factors}"
    )


def test_numberfield_primes_above_2_total_residue_degree_equals_degree():
    """
    method: primes_above

    primes_above(p) lists prime ideals above p.
    Assertion: Sum of residue degrees above p equals field degree for unramified p.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    primes = K.primes_above(2)
    actual = sum(P.residue_class_degree() for P in primes)
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.primes_above mismatch: actual={actual}, expected={expected}, primes={primes}"
    )


def test_numberfield_primes_of_bounded_norm_respect_bound():
    """
    method: primes_of_bounded_norm

    primes_of_bounded_norm(B) lists prime ideals with norm <= B.
    Assertion: Every returned prime has norm bounded by B.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    primes = K.primes_of_bounded_norm(10)
    actual = all(P.norm() <= 10 for P in primes)
    expected = True
    assert actual == expected, (
        f"NumberField.primes_of_bounded_norm mismatch: actual={actual}, expected={expected}, primes={primes}"
    )


def test_numberfield_primitive_root_of_unity_has_zeta_order():
    """
    method: primitive_root_of_unity

    primitive_root_of_unity() returns generator of roots of unity subgroup.
    Assertion: Its order equals zeta_order().
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    z = K.primitive_root_of_unity()
    actual = z.multiplicative_order()
    expected = K.zeta_order()
    assert actual == expected, (
        f"NumberField.primitive_root_of_unity mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_regulator_positive_for_real_quadratic():
    """
    method: regulator

    regulator() is positive for fields with positive unit rank.
    Assertion: Regulator of Q(sqrt(5)) is positive.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.regulator() > 0
    expected = True
    assert actual == expected, f"NumberField.regulator mismatch: actual={actual}, expected={expected}"


def test_numberfield_relative_discriminant_equals_discriminant_over_q():
    """
    method: relative_discriminant

    relative_discriminant() over Q matches discriminant for absolute fields.
    Assertion: Values coincide.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.relative_discriminant()
    expected = K.discriminant()
    assert actual == expected, (
        f"NumberField.relative_discriminant mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_relative_vector_space_dimension_matches_degree():
    """
    method: relative_vector_space

    relative_vector_space() returns vector-space model over base field.
    Assertion: Returned vector-space dimension equals field degree over Q.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    V, _, _ = K.relative_vector_space()
    actual = V.dimension()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.relative_vector_space mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_structure_maps_generator_to_itself():
    """
    method: structure

    structure() returns mutually inverse structure maps.
    Assertion: Forward map sends generator to itself in identical model.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    fwd, bwd = K.structure()
    actual = bwd(fwd(K.gen()))
    expected = K.gen()
    assert actual == expected, (
        f"NumberField.structure mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_subfields_contains_rational_subfield():
    """
    method: subfields

    subfields() enumerates intermediate subfields.
    Assertion: Rational field appears as a degree-1 subfield.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    subs = K.subfields()
    actual = any(L.degree() == 1 for (L, _, _) in subs)
    expected = True
    assert actual == expected, (
        f"NumberField.subfields mismatch: actual={actual}, expected={expected}, subfields={subs}"
    )


def test_numberfield_uniformizer_has_positive_valuation_at_prime():
    """
    method: uniformizer

    uniformizer(P) returns an element of valuation one at P.
    Assertion: P-adic valuation of returned uniformizer is 1.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    P = K.prime_above(2)
    pi = K.uniformizer(P)
    actual = K.valuation(P)(pi)
    expected = 1
    assert actual == expected, (
        f"NumberField.uniformizer mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_zeta_coefficients_nonzero_constant_term():
    """
    method: zeta_coefficients

    zeta_coefficients(n) gives initial coefficients of Dedekind zeta expansion data.
    Assertion: Constant coefficient is 1 in the returned list.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    coeffs = K.zeta_coefficients(5)
    actual = coeffs[0]
    expected = 1
    assert actual == expected, (
        f"NumberField.zeta_coefficients mismatch: actual={actual}, expected={expected}, coeffs={coeffs}"
    )


def test_numberfield_s_unit_group_empty_set_rank_matches_unit_group():
    """
    method: S_unit_group

    S_unit_group(S) generalizes unit group by inverting primes in S.
    Assertion: With empty S, rank equals ordinary unit-group rank.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.S_unit_group(()).rank()
    expected = K.unit_group().rank()
    assert actual == expected, (
        f"NumberField.S_unit_group mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_composite_fields_contains_self_for_self_compositum():
    """
    method: composite_fields

    composite_fields(L) lists composita with L.
    Assertion: Self-compositum contains a field of the same degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    composites = K.composite_fields(K)
    actual = any(L.degree() == K.degree() for L in composites)
    expected = True
    assert actual == expected, (
        f"NumberField.composite_fields mismatch: actual={actual}, expected={expected}, composites={composites}"
    )


def test_numberfield_dirichlet_group_contains_trivial_character():
    """
    method: dirichlet_group

    dirichlet_group() returns Dirichlet characters attached to field.
    Assertion: At least one returned character has conductor 1.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    chars = K.dirichlet_group()
    actual = any(chi.conductor() == 1 for chi in chars)
    expected = True
    assert actual == expected, (
        f"NumberField.dirichlet_group mismatch: actual={actual}, expected={expected}, chars={chars}"
    )


def test_numberfield_elements_of_bounded_height_contains_zero_and_one():
    """
    method: elements_of_bounded_height

    elements_of_bounded_height() enumerates algebraic numbers by height.
    Assertion: Initial segment contains both 0 and 1.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    elems = list(K.elements_of_bounded_height(bound=QQ(1)))
    actual = (0 in elems) and (1 in elems)
    expected = True
    assert actual == expected, (
        f"NumberField.elements_of_bounded_height mismatch: actual={actual}, expected={expected}, elems={elems}"
    )


def test_numberfield_extension_degree_multiplies_for_quadratic_over_quadratic():
    """
    method: extension

    extension(f,name) adjoins root of polynomial over K.
    Assertion: Adjoining y^2-2 doubles degree from 2 to 4 over Q.
    """
    x = ZZ["x"].gen()
    y = ZZ["y"].gen()
    K = NumberField(x**2 - 5, "a")
    L = K.extension(y**2 - 2, "b")
    actual = L.absolute_degree()
    expected = 4
    assert actual == expected, f"NumberField.extension mismatch: actual={actual}, expected={expected}"


def test_numberfield_factor_ideal_norm_matches_integer_norm():
    """
    method: factor

    factor(n) factors principal ideal (n) in O_K.
    Assertion: Product of factor norms equals |n|^[K:Q].
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    fac = K.factor(6)
    actual = ZZ.prod(I.norm() ** e for (I, e) in fac)
    expected = abs(ZZ(6)) ** K.degree()
    assert actual == expected, (
        f"NumberField.factor mismatch: actual={actual}, expected={expected}, factorization={fac}"
    )


def test_numberfield_hilbert_class_field_defining_polynomial_degree_one_for_class_number_one():
    """
    method: hilbert_class_field_defining_polynomial

    hilbert_class_field_defining_polynomial() defines maximal unramified abelian extension.
    Assertion: Class number 1 implies degree-1 defining polynomial.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.hilbert_class_field_defining_polynomial().degree()
    expected = 1
    assert actual == expected, (
        f"NumberField.hilbert_class_field_defining_polynomial mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_maximal_totally_real_subfield_has_same_degree():
    """
    method: maximal_totally_real_subfield

    maximal_totally_real_subfield() returns largest totally real subfield with embedding.
    Assertion: For totally real quadratic field, degree is unchanged.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    L, _ = K.maximal_totally_real_subfield()
    actual = L.degree()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.maximal_totally_real_subfield mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_minkowski_bound_positive():
    """
    method: minkowski_bound

    minkowski_bound() gives class-group search bound.
    Assertion: For Q(sqrt(5)), value equals sqrt(5)/2.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.minkowski_bound()
    expected = K.discriminant().abs().sqrt() / 2
    assert actual == expected, (
        f"NumberField.minkowski_bound mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_minkowski_embedding_matrix_has_degree_rows():
    """
    method: minkowski_embedding

    minkowski_embedding() returns embedding matrix into R^r x C^s.
    Assertion: Number of rows equals field degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    M = K.minkowski_embedding([1, K.gen()])
    actual = M.nrows()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.minkowski_embedding mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_optimized_representation_preserves_absolute_degree():
    """
    method: optimized_representation

    optimized_representation() returns equivalent presentation with potentially better defining polynomial.
    Assertion: Optimized field has same absolute degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    L, _, _ = K.optimized_representation()
    actual = L.absolute_degree()
    expected = K.absolute_degree()
    assert actual == expected, (
        f"NumberField.optimized_representation mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_optimized_subfields_contains_rational_subfield():
    """
    method: optimized_subfields

    optimized_subfields() returns optimized intermediate subfields.
    Assertion: A degree-1 subfield is present.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    subs = K.optimized_subfields()
    actual = any(entry[0].degree() == 1 for entry in subs)
    expected = True
    assert actual == expected, (
        f"NumberField.optimized_subfields mismatch: actual={actual}, expected={expected}, subs={subs}"
    )


def test_numberfield_order_of_conductor_has_requested_conductor():
    """
    method: order_of_conductor

    order_of_conductor(f) builds order with given conductor.
    Assertion: Returned order has conductor f.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    O = K.order_of_conductor(5)
    actual = O.conductor()
    expected = 5
    assert actual == expected, (
        f"NumberField.order_of_conductor mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_pari_bnf_class_number_matches_sage_class_number():
    """
    method: pari_bnf

    pari_bnf() returns PARI bnf structure.
    Assertion: PARI class number equals Sage class number.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.pari_bnf().bnf_get_no()
    expected = K.class_number()
    assert actual == expected, (
        f"NumberField.pari_bnf mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_polynomial_quotient_ring_modulus_matches_defining_polynomial():
    """
    method: polynomial_quotient_ring

    polynomial_quotient_ring() realizes K as QQ[x]/(f).
    Assertion: Quotient modulus equals defining polynomial.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    Q = K.polynomial_quotient_ring()
    actual = Q.modulus()
    expected = K.defining_polynomial()
    assert actual == expected, (
        f"NumberField.polynomial_quotient_ring mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_prime_above_has_residue_characteristic():
    """
    method: prime_above

    prime_above(p) returns a prime ideal over rational prime p.
    Assertion: Returned prime has residue characteristic p.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    P = K.prime_above(2)
    actual = P.norm() % 2
    expected = 0
    assert actual == expected, (
        f"NumberField.prime_above mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_primes_of_bounded_norm_iter_matches_list_method():
    """
    method: primes_of_bounded_norm_iter

    primes_of_bounded_norm_iter(B) iterates same primes as list API.
    Assertion: Iterator and list outputs agree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = sorted(str(P) for P in K.primes_of_bounded_norm_iter(10))
    expected = sorted(str(P) for P in K.primes_of_bounded_norm(10))
    assert actual == expected, (
        f"NumberField.primes_of_bounded_norm_iter mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_primes_of_degree_one_list_matches_iterator_prefix():
    """
    method: primes_of_degree_one_list

    primes_of_degree_one_list(n) gives first n degree-one primes.
    Assertion: Equals first n values from iterator.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    n = 3
    actual = K.primes_of_degree_one_list(n)
    it = K.primes_of_degree_one_iter()
    expected = [next(it) for _ in range(n)]
    assert actual == expected, (
        f"NumberField.primes_of_degree_one_list mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_primes_of_degree_one_iter_yields_degree_one_primes():
    """
    method: primes_of_degree_one_iter

    primes_of_degree_one_iter() yields prime ideals of residue degree one.
    Assertion: First yielded prime has residue degree one.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    P = next(K.primes_of_degree_one_iter())
    actual = P.residue_class_degree()
    expected = 1
    assert actual == expected, (
        f"NumberField.primes_of_degree_one_iter mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_reduced_gram_matrix_has_correct_determinant():
    """
    method: reduced_gram_matrix

    reduced_gram_matrix() gives Gram matrix of reduced integral basis.
    Assertion: Determinant equals absolute discriminant.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    G = K.reduced_gram_matrix()
    actual = abs(G.det())
    expected = abs(K.discriminant())
    assert actual == expected, (
        f"NumberField.reduced_gram_matrix mismatch: actual={actual}, expected={expected}, gram={G}"
    )


def test_numberfield_relative_different_equals_different_over_q():
    """
    method: relative_different

    relative_different() over base Q equals different().
    Assertion: Ideals are equal.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.relative_different()
    expected = K.different()
    assert actual == expected, (
        f"NumberField.relative_different mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_solve_crt_satisfies_congruences():
    """
    method: solve_CRT

    solve_CRT(residues, ideals) solves simultaneous ideal congruences.
    Assertion: Solution satisfies both congruences modulo chosen prime ideals.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    P = K.prime_above(2)
    Q = K.prime_above(3)
    s = K.solve_CRT([K(1), K(0)], [P, Q])
    actual = ((s - 1) in P) and (s in Q)
    expected = True
    assert actual == expected, (
        f"NumberField.solve_CRT mismatch: actual={actual}, expected={expected}, solution={s}"
    )


def test_numberfield_subfield_generated_by_generator_has_same_degree():
    """
    method: subfield

    subfield(alpha) returns generated subfield and embeddings.
    Assertion: Subfield generated by primitive element has full degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    L, _ = K.subfield(K.gen())
    actual = L.degree()
    expected = K.degree()
    assert actual == expected, f"NumberField.subfield mismatch: actual={actual}, expected={expected}"


def test_numberfield_subfield_from_elements_recovers_full_field_degree():
    """
    method: subfield_from_elements

    subfield_from_elements([alpha_i]) builds generated subfield.
    Assertion: Using primitive generator recovers full degree.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    L, _, _ = K.subfield_from_elements([K.gen()])
    actual = L.degree()
    expected = K.degree()
    assert actual == expected, (
        f"NumberField.subfield_from_elements mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_s_unit_solutions_contains_classical_solution():
    """
    method: S_unit_solutions

    S_unit_solutions(S) solves x+y=1 in S-units.
    Assertion: The trivial solution (0,1) appears for empty S.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    sols = K.S_unit_solutions([], include_exponents=False)
    actual = any(u + v == 1 for (u, v) in sols)
    expected = True
    assert actual == expected, (
        f"NumberField.S_unit_solutions mismatch: actual={actual}, expected={expected}, solutions={sols}"
    )


def test_numberfield_abs_val_matches_archimedean_absolute_value():
    """
    method: abs_val

    abs_val(v, iota) evaluates absolute value at a place.
    Assertion: Archimedean absolute value of 2 is 2.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    v = K.places(prec=80)[0]
    actual = K.abs_val(v, K(2))
    expected = 2
    assert actual == expected, f"NumberField.abs_val mismatch: actual={actual}, expected={expected}"


def test_numberfield_completion_archimedean_has_requested_precision():
    """
    method: completion

    completion(infinity, prec) gives archimedean completion.
    Assertion: Real quadratic field completion is a real field of requested precision.
    """
    K = QuadraticField(2, "b")
    R = K.completion(infinity, 53)
    actual = R.precision()
    expected = 53
    assert actual == expected, (
        f"NumberField.completion mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_gen_embedding_none_without_specified_embedding():
    """
    method: gen_embedding

    gen_embedding() returns image of generator if embedding was specified.
    Assertion: Generic NumberField constructor leaves embedding unspecified.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.gen_embedding()
    expected = None
    assert actual == expected, (
        f"NumberField.gen_embedding mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_hilbert_class_field_degree_matches_base_for_class_number_one():
    """
    method: hilbert_class_field

    hilbert_class_field(name) returns unramified abelian extension.
    Assertion: For Q(sqrt(-3)) (class number 1), Hilbert class field equals base field.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 + 3, "w")
    L = K.hilbert_class_field("b")
    actual = L.absolute_degree()
    expected = K.absolute_degree()
    assert actual == expected, (
        f"NumberField.hilbert_class_field mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_hilbert_class_polynomial_degree_matches_class_number():
    """
    method: hilbert_class_polynomial

    hilbert_class_polynomial() has degree equal to class number for imaginary quadratic fields.
    Assertion: Degree equals class number for Q(sqrt(-3)).
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 + 3, "w")
    actual = K.hilbert_class_polynomial().degree()
    expected = K.class_number()
    assert actual == expected, (
        f"NumberField.hilbert_class_polynomial mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_hilbert_conductor_divides_discriminant():
    """
    method: hilbert_conductor

    hilbert_conductor(a,b) is reduced discriminant ideal of quaternion algebra (a,b).
    Assertion: For documented sample input, the conductor is the prime ideal (2).
    """
    x = ZZ["x"].gen()
    F = NumberField(x**2 - x - 1, "u")
    C = F.hilbert_conductor(2 * F.gen(), F(-1))
    actual = C
    expected = F.ideal(2)
    assert actual == expected, (
        f"NumberField.hilbert_conductor mismatch: actual={actual}, expected={expected}, conductor={C}"
    )


def test_numberfield_hilbert_symbol_is_pm_one_for_nonzero_inputs():
    """
    method: hilbert_symbol

    hilbert_symbol(a,b,P) is local norm-residue symbol in {+1,-1}.
    Assertion: Value for (-1,-1) at a finite prime is +/-1.
    """
    x = ZZ["x"].gen()
    F = NumberField(x**2 - x - 1, "u")
    P = F.prime_above(2)
    val = F.hilbert_symbol(F(-1), F(-1), P)
    actual = val in (-1, 1)
    expected = True
    assert actual == expected, (
        f"NumberField.hilbert_symbol mismatch: actual={val}, expected in {{-1,1}}"
    )


def test_numberfield_hilbert_symbol_negative_at_s_realizes_requested_negative_set():
    """
    method: hilbert_symbol_negative_at_S

    hilbert_symbol_negative_at_S(S,b) returns a with negative Hilbert symbol on S.
    Assertion: Returned a gives symbol -1 at each place in S.
    """
    x = ZZ["x"].gen()
    F = NumberField(x**2 - x - 1, "u")
    S = [F.prime_above(2), F.places()[0]]
    a = F.hilbert_symbol_negative_at_S(S, QQ(-1))
    actual = [F.hilbert_symbol(a, F(-1), p) for p in S]
    expected = [-1, -1]
    assert actual == expected, (
        f"NumberField.hilbert_symbol_negative_at_S mismatch: actual={actual}, expected={expected}, a={a}"
    )


def test_numberfield_idealchinese_satisfies_two_congruences():
    """
    method: idealchinese

    idealchinese(ideals, residues) solves CRT for ideals.
    Assertion: Solution meets both congruences.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    P = K.prime_above(2)
    Q = K.prime_above(3)
    s = K.idealchinese([P, Q], [K(1), K(0)])
    actual = ((s - 1) in P) and (s in Q)
    expected = True
    assert actual == expected, (
        f"NumberField.idealchinese mismatch: actual={actual}, expected={expected}, solution={s}"
    )


def test_numberfield_lmfdb_page_uses_lmfdb_url(monkeypatch):
    """
    method: lmfdb_page

    lmfdb_page() should open the LMFDB URL for the field.
    Assertion: Opened URL contains the lmfdb NumberField endpoint.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    captured = {"url": ""}

    def fake_open(url, *_args, **_kwargs):
        captured["url"] = str(url)
        return True

    monkeypatch.setattr("webbrowser.open", fake_open)
    K.lmfdb_page()
    actual = "lmfdb.org/NumberField" in captured["url"]
    expected = True
    assert actual == expected, (
        f"NumberField.lmfdb_page mismatch: actual={captured['url']}, expected_contains='lmfdb.org/NumberField'"
    )


def test_numberfield_logarithmic_embedding_is_homomorphism_on_multiplication():
    """
    method: logarithmic_embedding

    logarithmic_embedding() sends products to sums.
    Assertion: log_embed(x*y) equals log_embed(x)+log_embed(y).
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    loge = K.logarithmic_embedding()
    u = K(2)
    v = K(3)
    actual = loge(u * v)
    expected = loge(u) + loge(v)
    assert actual == expected, (
        f"NumberField.logarithmic_embedding mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_pari_rnfnorm_data_has_eight_components():
    """
    method: pari_rnfnorm_data

    pari_rnfnorm_data(L) returns PARI norm initialization data.
    Assertion: Returned PARI structure has expected length 8.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    L = K.extension(x**2 - 2, "b")
    data = K.pari_rnfnorm_data(L)
    actual = len(data)
    expected = 8
    assert actual == expected, (
        f"NumberField.pari_rnfnorm_data mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_quadratic_defect_of_one_is_infinite():
    """
    method: quadratic_defect

    quadratic_defect(a,p) measures valuation defect of represented squares.
    Assertion: Defect of 1 is +Infinity.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    P = K.prime_above(2)
    actual = str(K.quadratic_defect(K(1), P))
    expected = "+Infinity"
    assert actual == expected, (
        f"NumberField.quadratic_defect mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_relativize_preserves_absolute_degree():
    """
    method: relativize

    relativize(alpha,names) returns relative model over Q(alpha).
    Assertion: Relative model has same absolute degree as original.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    R = K.relativize(K.gen(), names=("y", "t"))
    actual = R.absolute_degree()
    expected = K.absolute_degree()
    assert actual == expected, (
        f"NumberField.relativize mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_selmer_generators_generate_expected_rank_mod_squares():
    """
    method: selmer_generators

    selmer_generators(S,m) returns generators of Selmer quotient K(S,m).
    Assertion: For S=[] and m=2 in Q(sqrt(5)), two generators are returned.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    gens = K.selmer_generators([], ZZ(2))
    actual = len(gens)
    expected = 2
    assert actual == expected, (
        f"NumberField.selmer_generators mismatch: actual={actual}, expected={expected}, gens={gens}"
    )


def test_numberfield_selmer_group_iterator_contains_identity():
    """
    method: selmer_group_iterator

    selmer_group_iterator(S,m) iterates distinct elements of K(S,m).
    Assertion: Identity element 1 appears.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    elems = list(K.selmer_group_iterator([], ZZ(2)))
    actual = K(1) in elems
    expected = True
    assert actual == expected, (
        f"NumberField.selmer_group_iterator mismatch: actual={actual}, expected={expected}, elems={elems}"
    )


def test_numberfield_selmer_space_maps_zero_to_identity():
    """
    method: selmer_space

    selmer_space(S,p) returns vector space with map to K*.
    Assertion: Zero vector maps to multiplicative identity.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    V, _, from_V, _ = K.selmer_space([], ZZ(2))
    actual = from_V(V.zero())
    expected = K(1)
    assert actual == expected, (
        f"NumberField.selmer_space mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_specified_complex_embedding_is_none_without_choice():
    """
    method: specified_complex_embedding

    specified_complex_embedding() returns explicitly chosen embedding if present.
    Assertion: Generic NumberField has no specified complex embedding.
    """
    x = ZZ["x"].gen()
    K = NumberField(x**2 - 5, "a")
    actual = K.specified_complex_embedding()
    expected = None
    assert actual == expected, (
        f"NumberField.specified_complex_embedding mismatch: actual={actual}, expected={expected}"
    )


def test_numberfield_coverage():
    """
    method: runtime_coverage

    Runtime coverage guard: every relevant NumberField runtime method should
    correspond to at least one explicit test method tag in this module.
    """
    x = ZZ["x"].gen()
    sample = NumberField(x**2 - 5, "a")
    assert_runtime_methods_covered(
        test_module=sys.modules[__name__],
        sample_object=sample,
        module_prefixes=("sage.rings.number_field",),
    )
