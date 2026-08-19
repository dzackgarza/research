"""Tests for sage.quadratic_forms.ternary_qf.TernaryQF

Ternary quadratic forms in three variables with integer coefficients.
"""

import pytest
from sage.all import ZZ, identity_matrix, vector
from sage.quadratic_forms.ternary_qf import TernaryQF

TEST_TARGET = TernaryQF


@pytest.mark.timeout(10)
def test_construction():
    """TernaryQF(entries: list) -> TernaryQF
    
    Constructor from a list of coefficients [a, b, c, d, e, f] representing ax^2 + by^2 + cz^2 + dyz + exz + fxy.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.matrix().nrows() == 3


@pytest.mark.timeout(10)
def test_matrix():
    """.matrix() -> Matrix
    
    Returns the 3x3 symmetric matrix.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    m = f.matrix()
    assert m.nrows() == 3


@pytest.mark.timeout(10)
def test_discriminant():
    """.disc() -> Integer
    
    Returns the discriminant of the form.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.disc() == 4


@pytest.mark.timeout(10)
def test_disc():
    """.disc() -> Integer
    
    Returns the discriminant of the form.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.disc() == 4


@pytest.mark.timeout(10)
def test_coefficient():
    """.coefficient(n: int) -> Integer
    
    Returns the n-th coefficient (0 ≤ n ≤ 5) for ax²+by²+cz²+dyz+exz+fxy.
    """
    f = TernaryQF([1, 2, 3, 0, 0, 0])
    assert f.coefficient(0) == 1


@pytest.mark.timeout(10)
def test_coefficients():
    """.coefficients() -> tuple[Integer, ...]
    
    Returns full coefficient tuple (a, b, c, d, e, f).
    """
    f = TernaryQF([1, 2, 3, 0, 0, 0])
    assert len(f.coefficients()) == 6


@pytest.mark.timeout(10)
def test_content():
    """.content() -> Integer
    
    Returns GCD of all coefficients.
    """
    f = TernaryQF([2, 2, 2, 0, 0, 0])
    assert f.content() == 2


@pytest.mark.timeout(10)
def test_content_multiple():
    """.content() -> Integer
    
    Returns GCD of all coefficients.
    """
    f = TernaryQF([4, 6, 8, 0, 0, 0])
    assert f.content() == 2


@pytest.mark.timeout(10)
def test_level():
    """.level() -> Integer
    
    Returns level of the ternary form.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.level() == 4


@pytest.mark.timeout(10)
def test_polynomial():
    """.polynomial() -> Polynomial
    
    Returns polynomial representation.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.polynomial() is not None


@pytest.mark.timeout(10)
def test_is_primitive():
    """.is_primitive() -> bool
    
    Tests if form is primitive (gcd=1).
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.is_primitive() is True


@pytest.mark.timeout(10)
def test_is_primitive_false():
    """.is_primitive() -> bool
    
    Tests if form is primitive (gcd=1).
    """
    f = TernaryQF([2, 2, 2, 0, 0, 0])
    assert f.is_primitive() is False


@pytest.mark.timeout(10)
def test_primitive():
    """.primitive() -> TernaryQF
    
    Returns primitive part (content removed).
    """
    f = TernaryQF([2, 2, 2, 0, 0, 0])
    p = f.primitive()
    assert p.is_primitive() is True


@pytest.mark.timeout(10)
def test_adjoint():
    """.adjoint() -> TernaryQF
    
    Returns adjoint form.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.adjoint() is not None


@pytest.mark.timeout(10)
def test_quadratic_form_conversion():
    """.quadratic_form() -> QuadraticForm
    
    Converts ternary form to general QuadraticForm object.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    q = f.quadratic_form()
    assert q.dim() == 3


@pytest.mark.timeout(10)
def test_scale_by_factor():
    """.scale_by_factor(c) -> TernaryQF
    
    Scales all coefficients by factor c.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    s = f.scale_by_factor(2)
    assert s.content() == 2


@pytest.mark.timeout(10)
def test_reciprocal():
    """.reciprocal() -> TernaryQF
    
    Returns reciprocal form (adjoint/determinant variant).
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.reciprocal() is not None


@pytest.mark.timeout(10)
def test_find_zeros_mod_p():
    """.find_zeros_mod_p(p: Integer) -> list[Vector]
    
    Finds isotropic vectors (zeros) modulo p.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    zeros = f.find_zeros_mod_p(2)
    assert len(zeros) > 0


@pytest.mark.timeout(10)
def test_number_of_automorphisms():
    """.number_of_automorphisms() -> int
    
    Returns count of automorphisms (det ±1).
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.number_of_automorphisms() == 24


@pytest.mark.timeout(10)
def test_is_eisenstein_reduced():
    """.is_eisenstein_reduced() -> Boolean
    
    ⚠️ Requires positive-definite form. Returns True if in unique Eisenstein reduced form.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.is_eisenstein_reduced() is True


@pytest.mark.timeout(10)
def test_reduced_form_eisenstein():
    """.reduced_form_eisenstein() -> TernaryQF
    
    ⚠️ Requires positive-definite form. Returns an equivalent Eisenstein-reduced ternary form.
    """
    f = TernaryQF([2, 3, 4, 1, 1, 1])
    r, _ = f.reduced_form_eisenstein()
    assert r.is_eisenstein_reduced() is True


@pytest.mark.timeout(10)
def test_automorphisms():
    """.automorphisms(slow: bool = True) -> list[Matrix]
    
    ⚠️ Requires definite form (positive or negative). slow=True uses comprehensive method; slow=False uses lookup table.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    autos = f.automorphisms()
    assert len(autos) > 0


@pytest.mark.timeout(10)
def test_automorphism_spin_norm():
    """.automorphism_spin_norm(M: Matrix) -> int
    
    Returns spin norm of automorphisms.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    autos = f.automorphisms()
    sn = f.automorphism_spin_norm(autos[0])
    assert sn is not None


@pytest.mark.timeout(10)
def test_automorphism_symmetries():
    """.automorphism_symmetries(M: Matrix) -> list
    
    Returns symmetry group structure.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    id_mat = identity_matrix(ZZ, 3)
    syms = f.automorphism_symmetries(id_mat)
    assert syms == []


@pytest.mark.timeout(10)
def test_basic_lemma():
    """.basic_lemma(p: int) -> Rational
    
    Returns value from basic lemma for representation.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    val = f.basic_lemma(3)
    assert val is not None


@pytest.mark.timeout(10)
def test_category():
    """.category() -> Category
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.category() is not None


@pytest.mark.timeout(10)
def test_delta():
    """.delta() -> Rational
    
    Returns delta invariant.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.delta() is not None


@pytest.mark.timeout(10)
def test_divisor():
    """.divisor() -> Integer
    
    Returns divisor (GCD of coefficients).
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.divisor() is not None


@pytest.mark.timeout(10)
def test_find_p_neighbor_from_vec():
    """.find_p_neighbor_from_vec(p: Integer, v: Vector) -> TernaryQF
    
    Finds p-neighbor from primitive p-divisible vector v.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    v = (1, 1, 1)
    res = f.find_p_neighbor_from_vec(3, v)
    assert res is not None


@pytest.mark.timeout(10)
def test_find_p_neighbors():
    """.find_p_neighbors(p: int = 11) -> list[TernaryQF]
    
    Finds all p-neighbors of this ternary form (p-adic neighbor enumeration).
    """
    f = TernaryQF([1, 3, 3, -2, 0, -1])
    neighbors = f.find_p_neighbors(11)
    assert isinstance(neighbors, list)


@pytest.mark.timeout(10)
def test_is_definite():
    """.is_definite() -> bool
    
    Tests if form is definite.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.is_definite() is True


@pytest.mark.timeout(10)
def test_is_positive_definite():
    """.is_positive_definite() -> bool
    
    Tests if form is positive definite.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.is_positive_definite() is True


@pytest.mark.timeout(10)
def test_is_negative_definite():
    """.is_negative_definite() -> bool
    
    Tests if form is negative definite.
    """
    f = TernaryQF([-1, -1, -1, 0, 0, 0])
    assert f.is_negative_definite() is True


@pytest.mark.timeout(10)
def test_omega():
    """.omega() -> Rational
    
    Omega invariant for ternary forms.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.omega() is not None


@pytest.mark.timeout(10)
def test_parent():
    """.parent() -> Parent
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    assert f.parent() is not None


@pytest.mark.timeout(10)
def test_pseudorandom_primitive_zero_mod_p():
    """.pseudorandom_primitive_zero_mod_p(p: Integer) -> Vector
    
    Finds random primitive isotropic vector modulo p.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    z = f.pseudorandom_primitive_zero_mod_p(5)
    assert z is not None


@pytest.mark.timeout(10)
def test_reciprocal_reduced():
    """.reciprocal_reduced() -> TernaryQF
    
    ⚠️ Requires positive-definite form. Returns reciprocal reduction.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    r = f.reciprocal_reduced()
    assert r is not None


@pytest.mark.timeout(10)
def test_symmetry():
    """.symmetry(v: Vector) -> Matrix
    
    Returns symmetry properties of the form.
    """
    f = TernaryQF([1, 1, 1, 0, 0, 0])
    v = vector([1, 0, 0])
    sym = f.symmetry(v)
    assert sym is not None


@pytest.mark.timeout(10)
def test_xi():
    """.xi(p: int) -> Rational
    
    Xi invariant.
    """
    f = TernaryQF([26, 42, 53, -36, -17, -3])
    assert f.xi(3) is not None


@pytest.mark.timeout(10)
def test_xi_rec():
    """.xi_rec(p: int) -> Rational
    
    Recursive xi invariant.
    """
    f = TernaryQF([26, 42, 53, -36, -17, -3])
    assert f.xi_rec(3) is not None
