"""Tests for sage.quadratic_forms.quadratic_form.QuadraticForm

Doc sections: Construction, Basic Invariants & Properties, Local Properties & Algorithms,
Reduction/Transformation/Isometries, Representation, Genus, Mass Formulas, Conway-Sloane
Mass Methods, Local Density Methods, Local-Global Representation, Local Field Invariants,
Jordan Decomposition, Equivalence & Isometry, Automorphism & Geometry, Neighbor Enumeration,
Reduction Theory & Binary Forms, Variable Substitutions & Transformations, Form Structure
& Algebra, Theta Series & Enumeration, Matrix Forms & Representations, Invariants & Special Methods.
"""

import pytest
from sage.all import QQ, ZZ, DiagonalQuadraticForm, Matrix, vector
from sage.quadratic_forms.quadratic_form import QuadraticForm

TEST_TARGET = QuadraticForm


@pytest.mark.timeout(10)
def test_construction_from_matrix():
    """QuadraticForm(R: Ring, n: Integer, entries: list) -> QuadraticForm
    
    Construction. Constructor over ring `R` with `n` variables."""
    m = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(m)
    assert q.dim() == 2


@pytest.mark.timeout(10)
def test_gram_matrix():
    """.Gram_matrix() -> Matrix
    
    Basic Invariants & Properties. Gram matrix (may alias to gram_matrix())."""
    # x^2 + 2*xy + y^2 has Gram matrix [[1, 1], [1, 1]]
    q = QuadraticForm(ZZ, 2, [1, 2, 1])
    g = q.Gram_matrix()
    expected = Matrix(ZZ, [[1, 1], [1, 1]])
    assert g == expected


@pytest.mark.timeout(10)
def test_hessian_matrix():
    """.Hessian_matrix() -> Matrix
    
    Basic Invariants & Properties. Hessian matrix of form."""
    q = QuadraticForm(ZZ, 2, [1, 2, 1])
    # Hessian is 2 * Gram_matrix if Gram is integral, or the matrix M defining q(x) = 1/2 x^T M x?
    # Actually Q(x) = 1/2 x^T H x. For [1, 2, 1] (x+y)^2, H should be [[2, 2], [2, 2]]
    h = q.Hessian_matrix()
    expected = Matrix(ZZ, [[2, 2], [2, 2]])
    assert h == expected


@pytest.mark.timeout(10)
def test_det():
    """.det() -> int
    
    Form Structure & Algebra. Determinant of Gram matrix."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    # det usually refers to det of Hessian? Or Gram?
    # disc is b^2 - 4ac = -4.
    # Hessian is [[2, 0], [0, 2]], det 4.
    # Gram is [[1, 0], [0, 1]], det 1.
    # Let's check what det() returns.
    assert q.det() == 4


@pytest.mark.timeout(10)
def test_gram_det():
    """.Gram_det() -> int
    
    Basic Invariants & Properties. Determinant of Gram matrix."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    # Gram matrix is [[1, 0], [0, 1]]
    assert q.Gram_det() == 1


@pytest.mark.timeout(10)
def test_base_ring():
    """.base_ring() -> Ring
    
    Invariants & Special Methods. Returns base ring of form."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.base_ring() == ZZ


@pytest.mark.timeout(10)
def test_category():
    """.category() -> Category
    
    Returns the category of the form (inherited from parent class)."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.category() is not None


@pytest.mark.timeout(10)
def test_parent():
    """.parent() -> Parent
    
    Returns the parent structure (inherited from parent class)."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.parent() is not None


@pytest.mark.timeout(10)
def test_discriminant():
    """.disc() -> int
    
    Form Structure & Algebra. Discriminant: (-1)^(n/2)·det for even n, det/2 for odd n."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    # Discriminant of x^2 + y^2 is -4 (b^2 - 4ac)
    assert q.disc() == -4


@pytest.mark.timeout(10)
def test_signature():
    """.signature() -> Integer
    
    Basic Invariants & Properties. Returns the signature (over reals)."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.signature() == 2


@pytest.mark.timeout(10)
def test_level():
    """.level() -> Integer
    
    Basic Invariants & Properties. Returns the level of the quadratic form."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.level() == 4


@pytest.mark.timeout(10)
def test_is_definite():
    """.is_definite() -> Boolean
    
    Basic Invariants & Properties. Returns `True` if the form is definite."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.is_definite() is True


@pytest.mark.timeout(10)
def test_is_integral():
    """.has_integral_Gram_matrix() -> bool
    
    Basic Invariants & Properties. Tests if Gram matrix entries are integral."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.has_integral_Gram_matrix() is True


@pytest.mark.timeout(10)
def test_dim():
    """.dim() -> int
    
    Form Structure & Algebra. Dimension (number of variables)."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.dim() == 2


@pytest.mark.timeout(10)
def test_is_positive_definite():
    """.is_positive_definite() -> bool
    
    Local Field Invariants. Tests if all eigenvalues > 0."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.is_positive_definite() is True


@pytest.mark.timeout(10)
def test_is_negative_definite():
    """.is_negative_definite() -> bool
    
    Local Field Invariants. Tests if all eigenvalues < 0."""
    q = QuadraticForm(ZZ, 2, [-1, 0, -1])
    assert q.is_negative_definite() is True


@pytest.mark.timeout(10)
def test_is_indefinite():
    """.is_indefinite() -> bool
    
    Local Field Invariants. Tests if form is indefinite."""
    q = QuadraticForm(ZZ, 2, [1, 0, -1])
    assert q.is_indefinite() is True


@pytest.mark.timeout(10)
def test_is_isotropic():
    """.is_isotropic() -> bool
    
    Local Field Invariants. Tests if form has non-trivial zeros at prime p."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    assert q.is_isotropic(5) is True


@pytest.mark.timeout(10)
def test_is_anisotropic():
    """.is_anisotropic() -> bool
    
    Local Field Invariants. Tests if form has no non-trivial zeros at prime p."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    assert q.is_anisotropic(2) is True


@pytest.mark.timeout(10)
def test_reduced_form():
    """.lll() -> QuadraticForm
    
    Invariants & Special Methods. LLL reduction variant."""
    q = QuadraticForm(ZZ, 2, [10, 10, 10])
    r = q.lll()
    assert r.dim() == 2


@pytest.mark.timeout(10)
def test_rational_diagonal_form():
    """.rational_diagonal_form() -> QuadraticForm
    
    Reduction, Transformation & Isometries. Returns an equivalent diagonal form over Q."""
    q = QuadraticForm(ZZ, 2, [0, 1, -1])
    d = q.rational_diagonal_form()
    assert d.dim() == 2


@pytest.mark.timeout(10)
def test_change_ring():
    """.change_ring() -> QuadraticForm
    
    Invariants & Special Methods. Coerces form to ring R."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    qq = q.change_ring(QQ)
    assert qq.base_ring() == QQ


@pytest.mark.timeout(10)
def test_is_globally_equivalent_to():
    """.is_globally_equivalent_to() -> bool | Matrix
    
    Equivalence & Isometry. Tests global equivalence over ℤ using PARI. **⚠️ Requires positive-definite forms.** Returns transformation matrix if return_matrix=True."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
    assert q.is_globally_equivalent_to(q) is True


@pytest.mark.timeout(10)
def test_representation_number_list():
    """.representation_number_list() -> list[int]
    
    Representation. Returns list of representation counts as vector (all norms up to max)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    lst = q.representation_number_list(5)
    assert len(lst) == 5


@pytest.mark.timeout(10)
def test_solve():
    """.solve() -> Vector
    
    Representation. Returns a vector `x` such that Q(x) = c."""
    q = DiagonalQuadraticForm(QQ, [1, -1])
    sol = q.solve(3)
    assert q(sol) == 3


@pytest.mark.timeout(10)
def test_theta_series():
    """.theta_series() -> PowerSeries
    
    Representation. Returns the theta series expansion up to `bound`."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    ts = q.theta_series(5)
    assert ts is not None


@pytest.mark.timeout(10)
def test_is_primitive():
    """.is_primitive() -> bool
    
    Form Structure & Algebra. Tests if form is primitive (gcd=1)."""
    q = QuadraticForm(ZZ, 2, [2, 3, 4])
    assert q.is_primitive() is True


@pytest.mark.timeout(10)
def test_is_primitive_false():
    """.is_primitive() -> bool
    
    Form Structure & Algebra. Tests if form is primitive (gcd=1)."""
    q = QuadraticForm(ZZ, 2, [2, 4, 8])
    assert q.is_primitive() is False


@pytest.mark.timeout(10)
def test_content():
    """.content() -> int
    
    Form Structure & Algebra. Returns GCD of all matrix coefficients."""
    q = QuadraticForm(ZZ, 2, [2, 4, 8])
    assert q.content() == 2


@pytest.mark.timeout(10)
def test_primitive():
    """.primitive() -> QuadraticForm
    
    Form Structure & Algebra. Returns primitive part (content removed)."""
    q = QuadraticForm(ZZ, 2, [2, 4, 8])
    p = q.primitive()
    assert p.is_primitive() is True


@pytest.mark.timeout(10)
def test_adjoint():
    """.adjoint() -> QuadraticForm
    
    Form Structure & Algebra. Returns adjoint form."""
    q = QuadraticForm(ZZ, 2, [1, 2, 3])
    adj = q.adjoint()
    assert adj is not None


@pytest.mark.timeout(10)
def test_global_genus_symbol():
    """.global_genus_symbol() -> Genus
    
    Genus. Returns the genus symbol of the quadratic form."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    g = q.global_genus_symbol()
    assert g is not None


@pytest.mark.timeout(10)
def test_local_genus_symbol():
    """.local_genus_symbol() -> GenusSymbol_p_adic
    
    Genus. Local genus symbol at prime p (alternative access method)."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    ls = q.local_genus_symbol(2)
    assert ls is not None


@pytest.mark.timeout(10)
def test_hasse_invariant():
    """.hasse_invariant() -> Integer
    
    Local Properties & Algorithms. Returns the Hasse invariant at prime `p` (typically +/- 1)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    assert q.hasse_invariant(2) == 1


@pytest.mark.timeout(10)
def test_clifford_invariant():
    """.clifford_invariant() -> int
    
    Local Properties & Algorithms. Returns Clifford invariant (mod 8)."""
    q = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
    assert q.clifford_invariant(2) == 1


@pytest.mark.timeout(10)
def test_swap_variables():
    """.swap_variables() -> QuadraticForm | None
    
    Variable Substitutions & Transformations. Swaps variables x_r ↔ x_s. Modifies in place if in_place=True."""
    q = QuadraticForm(ZZ, 2, [1, 2, 3])
    swapped = q.swap_variables(0, 1)
    assert swapped is not None


@pytest.mark.timeout(10)
def test_scale_by_factor():
    """.scale_by_factor() -> QuadraticForm
    
    Variable Substitutions & Transformations. Scales all values by c. Set change_value_ring_flag=True if scaling requires field extension."""
    q = DiagonalQuadraticForm(ZZ, [3, 9])
    s = q.scale_by_factor(3)
    assert s.content() == 9


@pytest.mark.timeout(10)
def test_extract_variables():
    """.extract_variables() -> QuadraticForm
    
    Variable Substitutions & Transformations. Extracts specified variables. Returns reduced-dimensional form."""
    q = QuadraticForm(ZZ, 3, range(1, 7))
    sub = q.extract_variables([0, 2])
    assert sub.dim() == 2


@pytest.mark.timeout(10)
def test_jordan_blocks_by_scale_and_unimodular():
    """.jordan_blocks_by_scale_and_unimodular() -> list[tuple[int, QuadraticForm]]
    
    Jordan Decomposition. Returns [(scale, unimodular_form), ...] for each Jordan block."""
    q = QuadraticForm(ZZ, 2, [1, 0, 6])
    blocks = q.jordan_blocks_in_unimodular_list_by_scale_power(3)
    assert isinstance(blocks, list)


@pytest.mark.timeout(10)
def test_local_density():
    """.local_density() -> Rational
    
    Local Density Methods. Returns local density at prime p for representing m."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    ld = q.local_density(2, 1)
    assert ld > 0


@pytest.mark.timeout(10)
def test_local_primitive_density():
    """.local_primitive_density() -> Rational
    
    Local Density Methods. Returns local primitive density (only primitive solutions)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    lpd = q.local_primitive_density(2, 1)
    assert lpd > 0


@pytest.mark.timeout(10)
def test_add_symmetric():
    """.add_symmetric() -> QuadraticForm | None
    
    Variable Substitutions & Transformations. Symmetric row/column operation: adds c times j-th to i-th."""
    q = QuadraticForm(ZZ, 3, range(1, 7))
    q2 = q.add_symmetric(-1, 1, 0)
    assert q2 is not None


@pytest.mark.timeout(10)
def test_adjoint_primitive():
    """.adjoint_primitive() -> QuadraticForm
    
    Form Structure & Algebra. Returns primitive adjoint form (adjoint with content removed)."""
    q = QuadraticForm(ZZ, 2, [1, 2, 3])
    ap = q.adjoint_primitive()
    assert ap.is_primitive() is True


@pytest.mark.timeout(10)
def test_anisotropic_primes():
    """.anisotropic_primes() -> list[int]
    
    Local Field Invariants. Returns list of primes where form is anisotropic."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    primes = q.anisotropic_primes()
    assert isinstance(primes, list)


@pytest.mark.timeout(10)
def test_antiadjoint():
    """.antiadjoint() -> QuadraticForm
    
    Form Structure & Algebra. Returns form whose adjoint is the given form."""
    q = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
    aa = q.adjoint().antiadjoint()
    assert aa is not None


@pytest.mark.timeout(10)
def test_automorphism_group():
    """.automorphism_group() -> MatrixGroup
    
    Automorphism & Geometry. **⚠️ Requires positive-definite form.** Uses PARI's qfauto(). Raises ValueError on indefinite forms."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    ag = q.automorphism_group()
    assert ag is not None


@pytest.mark.timeout(10)
def test_automorphisms():
    """.automorphisms() -> MatrixGroup
    
    Reduction, Transformation & Isometries. Returns the group of orthogonal automorphisms O(q)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    autos = q.automorphisms()
    assert len(autos) > 0


@pytest.mark.timeout(10)
def test_basiclemma():
    """.basiclemma() -> Rational
    
    Form Structure & Algebra. Applies basic lemma for ternary representation (without arguments)."""
    q = QuadraticForm(ZZ, 2, [2, 1, 3])
    bl = q.basiclemma(6)
    assert bl is not None


@pytest.mark.timeout(10)
def test_basiclemmavec():
    """.basiclemmavec() -> Vector
    
    Representation. Returns a vector `v` such that Q(v) is coprime to `M`."""
    q = QuadraticForm(ZZ, 2, [2, 1, 5])
    vec = q.basiclemmavec(10)
    assert vec is not None


@pytest.mark.timeout(10)
def test_basis_of_short_vectors():
    """.basis_of_short_vectors() -> tuple | tuple[tuple, tuple]
    
    Automorphism & Geometry. **⚠️ Requires positive-definite form.** Returns basis of vectors with minimal Q(v) values. If show_lengths=True, also returns their lengths."""
    q = DiagonalQuadraticForm(ZZ, [1, 3, 5, 7])
    basis = q.basis_of_short_vectors()
    assert len(basis) == 4


@pytest.mark.timeout(10)
def test_bilinear_map():
    """.bilinear_map() -> MapFunction
    
    Matrix Forms & Representations. Returns bilinear extension of form."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    v = vector(ZZ, [1, 0])
    w = vector(ZZ, [0, 1])
    val = q.bilinear_map(v, w)
    assert val == 0


@pytest.mark.timeout(10)
def test_cholesky_decomposition():
    """.cholesky_decomposition() -> Matrix
    
    Invariants & Special Methods. Cholesky factorization of Gram matrix."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    cd = q.cholesky_decomposition()
    assert cd.nrows() == 2


@pytest.mark.timeout(10)
def test_clifford_conductor():
    """.clifford_conductor() -> int
    
    Form Structure & Algebra. Returns Clifford conductor."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    cc = q.clifford_conductor()
    assert cc is not None


@pytest.mark.timeout(10)
def test_coefficients():
    """.coefficients() -> list
    
    Matrix Forms & Representations. Returns coefficient list."""
    q = QuadraticForm(ZZ, 2, [1, 2, 3])
    coeffs = q.coefficients()
    assert coeffs == [1, 2, 3]


@pytest.mark.timeout(10)
def test_complementary_subform_to_vector():
    """.complementary_subform_to_vector() -> QuadraticForm
    
    Form Structure & Algebra. Returns orthogonal complement of v."""
    q = DiagonalQuadraticForm(ZZ, [1, 3, 5])
    comp = q.complementary_subform_to_vector([1, 0, 0])
    assert comp.dim() == 2


@pytest.mark.timeout(10)
def test_compute_definiteness():
    """.compute_definiteness() -> str
    
    Local Field Invariants. Returns "positive definite", "negative definite", "indefinite", or "degenerate"."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    q.compute_definiteness()
    assert q.is_definite() is True


@pytest.mark.timeout(10)
def test_conway_mass():
    """.conway_mass() -> Rational
    
    Conway-Sloane Mass Methods. Global mass using Conway-Sloane formula."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    m = q.conway_mass()
    assert m > 0


@pytest.mark.timeout(10)
def test_count_congruence_solutions():
    """.count_congruence_solutions_as_vector() -> list[int]
    
    Local Density Methods. Counts solutions Q(x)≡m (mod p^k) by type: [All, Good, Zero, Bad, BadI, BadII]. zvec/nzvec specify coordinates."""
    q = DiagonalQuadraticForm(ZZ, [1, 2, 3])
    count = q.count_congruence_solutions(3, 1, 0, None, None)
    assert count >= 0


@pytest.mark.timeout(10)
def test_delta():
    """.delta()
    
    Undocumented method (inherited from parent class)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 37])
    assert q.delta() is not None


@pytest.mark.timeout(10)
def test_discrec():
    """.discrec()
    
    Undocumented method (inherited from parent class)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 37])
    assert q.discrec() is not None


@pytest.mark.timeout(10)
def test_divide_variable():
    """.divide_variable() -> QuadraticForm | None
    
    Variable Substitutions & Transformations. Substitution x_i → x_i/c."""
    q = DiagonalQuadraticForm(ZZ, [1, 9])
    q2 = q.divide_variable(3, 1)
    assert q2 is not None


@pytest.mark.timeout(10)
def test_elementary_substitution():
    """.elementary_substitution() -> QuadraticForm | None
    
    Variable Substitutions & Transformations. Substitution x_i → x_i + c·x_j."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    q2 = q.elementary_substitution(1, 0, 1)
    assert q2 is not None


@pytest.mark.timeout(10)
def test_find_p_neighbor_from_vec():
    """.find_p_neighbor_from_vec() -> QuadraticForm | Matrix
    
    Neighbor Enumeration. Given y with p²|Q(y), returns p-neighbor. Returns transformation matrix if return_matrix=True."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
    v = vector([0, 2, 1, 1])
    nb = q.find_p_neighbor_from_vec(3, v)
    assert nb is not None


@pytest.mark.timeout(10)
def test_from_polynomial():
    """.from_polynomial() -> QuadraticForm
    
    Matrix Forms & Representations. Constructs form from polynomial."""
    r = ZZ["x,y"]
    x, y = r.gens()
    p = x**2 + y**2
    q = QuadraticForm.from_polynomial(p)
    assert q.dim() == 2


@pytest.mark.timeout(10)
def test_gcd():
    """.gcd() -> int
    
    Form Structure & Algebra. Alias for content()."""
    q = QuadraticForm(ZZ, 2, [2, 4, 6])
    assert q.gcd() == 2


@pytest.mark.timeout(10)
def test_genera():
    """.genera()
    
    Undocumented method (inherited from parent class)."""
    genera = QuadraticForm.genera((4, 0), 125, even=True)
    assert len(genera) > 0


@pytest.mark.timeout(10)
def test_hasse_conductor():
    """.hasse_conductor() -> int
    
    Local Field Invariants. Conductor derived from Hasse invariants."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    hc = q.hasse_conductor()
    assert hc is not None


@pytest.mark.timeout(10)
def test_is_adjoint():
    """.is_adjoint() -> bool
    
    Form Structure & Algebra. Tests if form is adjoint to another."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert isinstance(q.is_adjoint(), bool)


@pytest.mark.timeout(10)
def test_is_even():
    """.is_even() -> bool
    
    Conway-Sloane Mass Methods. Returns True if form is even."""
    q = QuadraticForm(ZZ, 2, [1, 1, 1])
    assert q.is_even() is True


@pytest.mark.timeout(10)
def test_is_hyperbolic():
    """.is_hyperbolic() -> bool
    
    Local Field Invariants. Tests if isotropic with signature (1,1) or (n,0)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    assert q.is_hyperbolic(5) is True


@pytest.mark.timeout(10)
def test_is_locally_equivalent_to():
    """.is_locally_equivalent_to() -> bool
    
    Equivalence & Isometry. Tests local equivalence at all primes by comparing Jordan decompositions."""
    q1 = QuadraticForm(ZZ, 3, [1, 0, -1, 2, -1, 5])
    q2 = QuadraticForm(ZZ, 3, [2, 1, 2, 2, 1, 3])
    assert q1.is_locally_equivalent_to(q2) is True


@pytest.mark.timeout(10)
def test_is_locally_represented_number():
    """.is_locally_represented_number() -> bool
    
    Local-Global Representation. Tests if m is locally represented at all places."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    assert q.is_locally_represented_number(2) is True


@pytest.mark.timeout(10)
def test_is_locally_universal_at_all_primes():
    """.is_locally_universal_at_all_primes() -> bool
    
    Local Field Invariants. Tests universality at all finite primes."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
    assert q.is_locally_universal_at_all_primes() is True


@pytest.mark.timeout(10)
def test_is_odd():
    """.is_odd() -> bool
    
    Conway-Sloane Mass Methods. Returns True if form is odd."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.is_odd() is True


@pytest.mark.timeout(10)
def test_is_rationally_isometric():
    """.is_rationally_isometric() -> bool
    
    Equivalence & Isometry. Tests isometry over ℚ."""
    q1 = DiagonalQuadraticForm(QQ, [1, 1])
    q2 = DiagonalQuadraticForm(QQ, [2, 2])
    assert q1.is_rationally_isometric(q2) is True


@pytest.mark.timeout(10)
def test_is_zero():
    """.is_zero()
    
    Undocumented method (inherited from parent class)."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    # x^2 + y^2 = 0 mod 2 => x=1, y=1 -> 1+1=2=0
    assert q.is_zero([1, 1], 2) is True


@pytest.mark.timeout(10)
def test_local_normal_form():
    """.local_normal_form() -> QuadraticForm
    
    Jordan Decomposition. **⚠️ Requires base ring ℤ.** Returns Jordan decomposition form over p-adic integers."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    lnf = q.local_normal_form(2)
    assert lnf is not None


@pytest.mark.timeout(10)
def test_mass_by_siegel_densities():
    """.mass__by_Siegel_densities() -> Rational
    
    Mass Formulas. Computes mass using Siegel density formula. Algorithms: 'Pall' for odd primes, 'Watson' or 'Kitaoka' for p=2."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    m = q.mass__by_Siegel_densities()
    assert m > 0


@pytest.mark.timeout(10)
def test_minkowski_reduction():
    """.minkowski_reduction() -> tuple[QuadraticForm, Matrix]
    
    Reduction Theory & Binary Forms. Minkowski-reduced form (successive minima ordering)."""
    q = QuadraticForm(ZZ, 2, [10, 10, 10])
    red, _ = q.minkowski_reduction()
    assert red.dim() == 2


@pytest.mark.timeout(10)
def test_multiply_variable():
    """.multiply_variable() -> QuadraticForm | None
    
    Variable Substitutions & Transformations. Substitution x_i → c·x_i."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    q2 = q.multiply_variable(2, 0)
    assert q2 is not None


@pytest.mark.timeout(10)
def test_neighbor_iteration():
    """.neighbor_iteration() -> list[QuadraticForm]
    
    Neighbor Enumeration. **Static method.** Finds all genus classes via p-neighbor graph. Algorithms: 'orbits', 'random', 'exhaustion'."""
    from sage.quadratic_forms.quadratic_form__neighbors import neighbor_iteration

    q = QuadraticForm(ZZ, 3, [1, 0, 0, 2, 1, 3])
    # Limiting to a small number for speed
    nbrs = neighbor_iteration([q], 3, max_classes=2)
    assert len(nbrs) > 0


@pytest.mark.timeout(10)
def test_number_of_automorphisms():
    """.number_of_automorphisms() -> int
    
    Automorphism & Geometry. Returns count of automorphisms (det ±1). Caches result."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    assert q.number_of_automorphisms() == 8


@pytest.mark.timeout(10)
def test_omega():
    """.omega() -> Rational
    
    Invariants & Special Methods. Omega invariant."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 37])
    assert q.omega() == 4


@pytest.mark.timeout(10)
def test_orbits_lines_mod_p():
    """.orbits_lines_mod_p() -> list[list[Vector]]
    
    Neighbor Enumeration. Returns orbits of lines mod p under group action."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    orbits = q.orbits_lines_mod_p(3)
    assert isinstance(orbits, list)


@pytest.mark.timeout(10)
def test_parity():
    """.parity() -> str
    
    Conway-Sloane Mass Methods. Returns 'even' or 'odd' based on Jordan components at p=2."""
    q = QuadraticForm(ZZ, 2, [1, 0, 1])
    assert q.parity() == "odd"


@pytest.mark.timeout(10)
def test_polynomial():
    """.polynomial() -> Polynomial
    
    Matrix Forms & Representations. Polynomial representation."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    poly = q.polynomial()
    assert poly.degree() == 2


@pytest.mark.timeout(10)
def test_reciprocal():
    """.reciprocal() -> QuadraticForm
    
    Invariants & Special Methods. Returns reciprocal form."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 37])
    r = q.reciprocal()
    assert r.dim() == 3


@pytest.mark.timeout(10)
def test_reduced_binary_form():
    """.reduced_binary_form() -> tuple[QuadraticForm, Matrix]
    
    Reduction Theory & Binary Forms. Returns reduced form satisfying |b|≤a≤c for ax²+bxy+cy². Returns (form, transformation)."""
    q = QuadraticForm(ZZ, 2, [5, 5, 2])
    red, _ = q.reduced_binary_form()
    assert red.dim() == 2


@pytest.mark.timeout(10)
def test_representation_vector_list():
    """.representation_vector_list() -> list[Vector]
    
    Representation. **⚠️ Requires positive-definite form.** Returns a list of all vectors `v` such that Q(v) = n."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    vecs = q.representation_vector_list(5)
    assert isinstance(vecs, list)


@pytest.mark.timeout(10)
def test_short_vector_list_up_to_length():
    """.short_vector_list_up_to_length() -> list[list[Vector]]
    
    Automorphism & Geometry. **⚠️ Requires positive-definite form.** Returns sorted list of short vectors by length. Includes one of ±v if up_to_sign_flag."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    vecs = q.short_vector_list_up_to_length(3)
    assert isinstance(vecs, list)


@pytest.mark.timeout(10)
def test_siegel_product():
    """.siegel_product() -> Rational
    
    Invariants & Special Methods. Siegel product."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
    sp = q.siegel_product(1)
    assert sp > 0


@pytest.mark.timeout(10)
def test_split_local_cover():
    """.split_local_cover() -> QuadraticForm
    
    Invariants & Special Methods. Returns covers of local isotropic subspaces."""
    q = DiagonalQuadraticForm(ZZ, [7, 5, 3])
    split = q.split_local_cover()
    assert split is not None


@pytest.mark.timeout(10)
def test_sum_by_coefficients_with():
    """.sum_by_coefficients_with() -> QuadraticForm
    
    Invariants & Special Methods. Sum by coefficient manipulation."""
    q1 = QuadraticForm(ZZ, 2, [1, 0, 1])
    q2 = QuadraticForm(ZZ, 2, [1, 0, 1])
    sum_q = q1.sum_by_coefficients_with(q2)
    assert sum_q.dim() == 2


@pytest.mark.timeout(10)
def test_vectors_by_length():
    """.vectors_by_length() -> dict[int, list[Vector]]
    
    Automorphism & Geometry. Organizes all short vectors by their norm, returning dict mapping norm → list of vectors."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    vecs = q.vectors_by_length(2)
    assert isinstance(vecs, list)


@pytest.mark.timeout(10)
def test_xi():
    """.xi() -> Rational
    
    Invariants & Special Methods. Xi invariant."""
    q = QuadraticForm(ZZ, 3, [1, 1, 1, 14, 3, 14])
    assert q.xi(5) is not None


@pytest.mark.timeout(10)
def test_xi_rec():
    """.xi_rec() -> Rational
    
    Invariants & Special Methods. Recursive xi invariant."""
    q = QuadraticForm(ZZ, 3, [1, 1, 1, 14, 3, 14])
    assert q.xi_rec(5) is not None


@pytest.mark.timeout(10)
def test_matrix():
    """.matrix() -> Matrix
    
    Matrix Forms & Representations. Matrix form of quadratic form."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    assert q.matrix() == Matrix(ZZ, [[2, 0], [0, 2]])


@pytest.mark.timeout(10)
def test_CS_genus_symbol_list():
    """.CS_genus_symbol_list() -> list[GenusSymbol_p_adic]
    
    Genus. Returns list of local genus symbols at all primes dividing 2·det."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    syms = q.CS_genus_symbol_list()
    assert isinstance(syms, list)


@pytest.mark.timeout(10)
def test_GHY_mass__maximal():
    """.GHY_mass__maximal() -> Rational
    
    Mass Formulas. **Unimplemented stub.** Intended for GHY formula for maximal lattices."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    if q.is_definite():
        assert q.GHY_mass__maximal() is not None


@pytest.mark.timeout(10)
def test_shimura_mass__maximal():
    """.shimura_mass__maximal() -> Rational
    
    Mass Formulas. **Unimplemented stub.** Intended for Shimura's formula for maximal lattices over totally real fields."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    if q.is_definite():
        assert q.shimura_mass__maximal() is not None


@pytest.mark.timeout(10)
def test_Kitaoka_mass_at_2():
    """.Kitaoka_mass_at_2() -> Rational
    
    Mass Formulas. Local mass at p=2 using Kitaoka's formula."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    q.Kitaoka_mass_at_2()


@pytest.mark.timeout(10)
def test_Watson_mass_at_2():
    """.Watson_mass_at_2() -> Rational
    
    Mass Formulas. Local mass at p=2 using Watson's Theorem (1976)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    q.Watson_mass_at_2()


@pytest.mark.timeout(10)
def test_conway_standard_mass():
    """.conway_standard_mass() -> Rational
    
    Conway-Sloane Mass Methods. Infinite product of standard mass factors."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    assert q.conway_standard_mass() > 0


@pytest.mark.timeout(10)
def test_conway_standard_p_mass():
    """.conway_standard_p_mass() -> Rational
    
    Conway-Sloane Mass Methods. Standard (generic) Conway-Sloane p-mass formula."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    assert q.conway_standard_p_mass(2) > 0


@pytest.mark.timeout(10)
def test_conway_species_list_at_2():
    """.conway_species_list_at_2() -> list[int]
    
    Conway-Sloane Mass Methods. Species list at prime p=2 (accounts for parity and binding)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    assert q.conway_species_list_at_2() is not None


@pytest.mark.timeout(10)
def test_conway_species_list_at_odd_prime():
    """.conway_species_list_at_odd_prime() -> list[int]
    
    Conway-Sloane Mass Methods. Species classifying orthogonal group type at odd prime p."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    assert q.conway_species_list_at_odd_prime(3) is not None


@pytest.mark.timeout(10)
def test_local_good_density_congruence():
    """.local_good_density_congruence() -> Rational
    
    Local Density Methods. Good-type local density. Dispatches to odd/even implementations."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    p = 2
    k = 1
    q.local_good_density_congruence(p, k, [], [])


@pytest.mark.timeout(10)
def test_count_congruence_solutions_as_vector():
    """.count_congruence_solutions_as_vector() -> list[int]
    
    Local Density Methods. Counts solutions Q(x)≡m (mod p^k) by type: [All, Good, Zero, Bad, BadI, BadII]. zvec/nzvec specify coordinates."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    vec = q.count_congruence_solutions_as_vector(3, 1, 0, None, None)
    assert len(vec) > 0


@pytest.mark.timeout(10)
def test_is_locally_represented_number_at_place():
    """.is_locally_represented_number_at_place() -> bool
    
    Local-Global Representation. Tests if m is locally represented at place p (prime or ∞)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    assert q.is_locally_represented_number_at_place(2, 2)


@pytest.mark.timeout(10)
def test_is_locally_universal_at_prime():
    """.is_locally_universal_at_prime() -> bool
    
    Local Field Invariants. Tests if form represents all integers at prime p."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    assert q.is_locally_universal_at_prime(2) is False


@pytest.mark.timeout(10)
def test_hasse_invariant__OMeara():
    """.hasse_invariant__OMeara() -> int
    
    Local Field Invariants. Hasse invariant using O'Meara's formula."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    q.hasse_invariant__OMeara(2)


@pytest.mark.timeout(10)
def test_theta_by_cholesky():
    """.theta_by_cholesky() -> PowerSeries
    
    Theta Series & Enumeration. Theta series via Cholesky decomposition."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    ts = q.theta_by_cholesky(10)
    assert ts[10] is not None


@pytest.mark.timeout(10)
def test_theta_by_pari():
    """.theta_by_pari() -> PowerSeries
    
    Theta Series & Enumeration. Theta series via PARI computation."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    ts = q.theta_by_pari(10)
    assert ts[0] == 1


@pytest.mark.timeout(10)
def test_reduced_binary_form1():
    """.reduced_binary_form1() -> tuple[QuadraticForm, Matrix]
    
    Reduction Theory & Binary Forms. Reduced form in proper class (det=1) with |b|≤a≤c."""
    q2 = QuadraticForm(ZZ, 2, [1, 1, 1])
    q2.reduced_binary_form1()


@pytest.mark.timeout(10)
def test_reduced_ternary_form__Dickson():
    """.reduced_ternary_form__Dickson() -> QuadraticForm
    
    Reduction Theory & Binary Forms. **Unimplemented stub.** Intended for Dickson's unique reduction conditions."""
    q3 = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    q3.reduced_ternary_form__Dickson()


@pytest.mark.timeout(10)
def test_level__Tornaria():
    """.level__Tornaria() -> Integer
    
    Form Structure & Algebra. Returns level computed via Tornaria method."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    l = q.level__Tornaria()
    assert l == q.level()


@pytest.mark.timeout(10)
def test_level_ideal():
    """.level_ideal() -> Ideal
    
    Form Structure & Algebra. Returns level ideal."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    li = q.level_ideal()
    assert li is not None


@pytest.mark.timeout(10)
def test_short_primitive_vector_list_up_to_length():
    """.short_primitive_vector_list_up_to_length() -> list[list[Vector]]
    
    Automorphism & Geometry. **⚠️ Requires positive-definite form.** Same as above but only primitive vectors (gcd=1)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    vecs = q.short_primitive_vector_list_up_to_length(2)
    assert isinstance(vecs, list)


@pytest.mark.timeout(10)
def test_jordan_blocks_by_scale_and_unimodular():
    """.jordan_blocks_by_scale_and_unimodular() -> list[tuple[int, QuadraticForm]]
    
    Jordan Decomposition. Returns [(scale, unimodular_form), ...] for each Jordan block."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 2])
    blocks = q.jordan_blocks_by_scale_and_unimodular(2)
    assert isinstance(blocks, list)


@pytest.mark.timeout(10)
def test_Gram_matrix_rational():
    """.Gram_matrix_rational() -> Matrix
    
    Matrix Forms & Representations. Rational Gram matrix variant."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    G = q.Gram_matrix_rational()
    assert G.base_ring() == QQ


@pytest.mark.timeout(10)
def test_Pall_mass_density_at_odd_prime():
    """.Pall_mass_density_at_odd_prime() -> Rational
    
    Mass Formulas. Local representation density at odd prime p using Pall's formula (1965)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    d = q.Pall_mass_density_at_odd_prime(3)
    assert d > 0


@pytest.mark.timeout(10)
def test_conway_cross_product_doubled_power():
    """.conway_cross_product_doubled_power() -> int
    
    Conway-Sloane Mass Methods. Returns 2× power of p in 'cross product' term of Conway formula."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    res = q.conway_cross_product_doubled_power(3)
    assert res is not None


@pytest.mark.timeout(10)
def test_conway_diagonal_factor():
    """.conway_diagonal_factor() -> Rational
    
    Conway-Sloane Mass Methods. Diagonal factor in Conway's p-mass formula."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    res = q.conway_diagonal_factor(3)
    assert res is not None


@pytest.mark.timeout(10)
def test_conway_octane_of_this_unimodular_Jordan_block_at_2():
    """.conway_octane_of_this_unimodular_Jordan_block_at_2() -> int
    
    Conway-Sloane Mass Methods. "Octane" invariant mod 8 of unimodular Jordan block at p=2."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    res = q.conway_octane_of_this_unimodular_Jordan_block_at_2()
    assert res is not None


@pytest.mark.timeout(10)
def test_conway_p_mass():
    """.conway_p_mass() -> Rational
    
    Conway-Sloane Mass Methods. Conway's p-mass (local mass at prime p)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    res = q.conway_p_mass(2)
    assert res > 0


@pytest.mark.timeout(10)
def test_conway_type_factor():
    """.conway_type_factor() -> Rational
    
    Conway-Sloane Mass Methods. Special factor for p=2 in mass formula."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    res = q.conway_type_factor()
    assert res is not None


@pytest.mark.timeout(10)
def test_count_congruence_solutions__bad_type():
    """.count_congruence_solutions__bad_type() -> int
    
    Local Density Methods. Counts "bad-type" solutions."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.count_congruence_solutions__bad_type(2, 1, 0, None, None)
    assert res >= 0


@pytest.mark.timeout(10)
def test_count_congruence_solutions__bad_type_I():
    """.count_congruence_solutions__bad_type_I() -> int
    
    Local Density Methods. Counts "bad type I" solutions."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.count_congruence_solutions__bad_type_I(2, 1, 0, None, None)
    assert res >= 0


@pytest.mark.timeout(10)
def test_count_congruence_solutions__bad_type_II():
    """.count_congruence_solutions__bad_type_II() -> int
    
    Local Density Methods. Counts "bad type II" solutions."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.count_congruence_solutions__bad_type_II(2, 1, 0, None, None)
    assert res >= 0


@pytest.mark.timeout(10)
def test_count_congruence_solutions__good_type():
    """.count_congruence_solutions__good_type() -> int
    
    Local Density Methods. Counts "good-type" solutions (henselian lifting available)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.count_congruence_solutions__good_type(2, 1, 0, None, None)
    assert res >= 0


@pytest.mark.timeout(10)
def test_count_congruence_solutions__zero_type():
    """.count_congruence_solutions__zero_type() -> int
    
    Local Density Methods. Counts solutions where m≡0 (mod p)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.count_congruence_solutions__zero_type(2, 1, 0, None, None)
    assert res >= 0


@pytest.mark.timeout(10)
def test_count_modp_solutions__by_Gauss_sum():
    """.count_modp_solutions__by_Gauss_sum() -> int
    
    Local Density Methods. Counts solutions Q(x)≡m (mod p) using Gauss sum formula (p>2 only)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.count_modp_solutions__by_Gauss_sum(3, 1)
    assert res >= 0


@pytest.mark.timeout(10)
def test_find_entry_with_minimal_scale_at_prime():
    """.find_entry_with_minimal_scale_at_prime() -> tuple[int, int]
    
    Jordan Decomposition. Finds matrix entry with minimal p-adic valuation. Returns (row, col)."""
    q = DiagonalQuadraticForm(ZZ, [2, 4])
    res = q.find_entry_with_minimal_scale_at_prime(2)
    assert res is not None


@pytest.mark.timeout(10)
def test_find_primitive_p_divisible_vector__next():
    """.find_primitive_p_divisible_vector__next() -> Vector | None
    
    Neighbor Enumeration. Iteratively finds next p-primitive p-divisible vector. Returns None when exhausted."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
    res = q.find_primitive_p_divisible_vector__next(2)
    assert res is not None


@pytest.mark.timeout(10)
def test_find_primitive_p_divisible_vector__random():
    """.find_primitive_p_divisible_vector__random() -> Vector
    
    Neighbor Enumeration. Finds random p-primitive vector y with p|Q(y) (roughly 1/p success rate)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
    res = q.find_primitive_p_divisible_vector__random(2)
    assert res is not None


@pytest.mark.timeout(10)
def test_has_equivalent_Jordan_decomposition_at_prime():
    """.has_equivalent_Jordan_decomposition_at_prime() -> bool
    
    Equivalence & Isometry. Tests equivalence of p-adic Jordan decompositions."""
    q = DiagonalQuadraticForm(ZZ, [1, 2, 4])
    assert q.has_equivalent_Jordan_decomposition_at_prime(q, 2)


@pytest.mark.timeout(10)
def test_is_locally_universal_at_all_places():
    """.is_locally_universal_at_all_places() -> bool
    
    Local Field Invariants. Tests universality at all primes and ∞."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
    result = q.is_locally_universal_at_all_places()
    assert isinstance(result, bool)


@pytest.mark.timeout(10)
def test_is_zero_nonsingular():
    """.is_zero_nonsingular() -> bool
    
    Tests if zero is nonsingular (inherited from parent class)."""
    q = DiagonalQuadraticForm(ZZ, [1, -1])
    assert q.is_zero_nonsingular([1, 1], 3)


@pytest.mark.timeout(10)
def test_is_zero_singular():
    """.is_zero_singular() -> bool
    
    Tests if zero is singular (inherited from parent class)."""
    q = DiagonalQuadraticForm(ZZ, [0, 0])
    assert q.is_zero_singular([1, 1], 2)


@pytest.mark.timeout(10)
def test_jordan_blocks_in_unimodular_list_by_scale_power():
    """.jordan_blocks_in_unimodular_list_by_scale_power() -> list[QuadraticForm]
    
    Jordan Decomposition. Returns list of unimodular Jordan blocks ordered by scale."""
    q = DiagonalQuadraticForm(ZZ, [1, 2, 4])
    res = q.jordan_blocks_in_unimodular_list_by_scale_power(2)
    assert isinstance(res, list)


@pytest.mark.timeout(10)
def test_local_badII_density_congruence():
    """.local_badII_density_congruence() -> Rational
    
    Local Density Methods. Bad type II local density."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.local_badII_density_congruence(2, 1, [], [])
    assert res >= 0


@pytest.mark.timeout(10)
def test_local_badI_density_congruence():
    """.local_badI_density_congruence() -> Rational
    
    Local Density Methods. Bad type I local density."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.local_badI_density_congruence(2, 1, [], [])
    assert res >= 0


@pytest.mark.timeout(10)
def test_local_bad_density_congruence():
    """.local_bad_density_congruence() -> Rational
    
    Local Density Methods. Bad-type local density."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.local_bad_density_congruence(2, 1, [], [])
    assert res >= 0


@pytest.mark.timeout(10)
def test_local_density_congruence():
    """.local_density_congruence() -> Rational
    
    Local Density Methods. Main dispatcher for local density by congruence (routes to specific case handlers)."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.local_density_congruence(2, 1, [], [])
    assert res >= 0


@pytest.mark.timeout(10)
def test_local_good_density_congruence_even():
    """.local_good_density_congruence_even() -> Rational
    
    Local Density Methods. Good-type density at p=2."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.local_good_density_congruence_even(1, [], [])
    assert res >= 0


@pytest.mark.timeout(10)
def test_local_good_density_congruence_odd():
    """.local_good_density_congruence_odd() -> Rational
    
    Local Density Methods. Good-type density at odd prime p."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.local_good_density_congruence_odd(3, 1, [], [])
    assert res >= 0


@pytest.mark.timeout(10)
def test_local_primitive_density_congruence():
    """.local_primitive_density_congruence() -> Rational
    
    Local Density Methods. Primitive (non-henselian) density by congruence conditions."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.local_primitive_density_congruence(2, 1, [], [])
    assert res >= 0


@pytest.mark.timeout(10)
def test_local_representation_conditions():
    """.local_representation_conditions() -> QuadraticFormLocalRepresentationConditions
    
    Local-Global Representation. Returns conditions object describing local representability at each prime."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.local_representation_conditions(2)
    assert res is not None


@pytest.mark.timeout(10)
def test_local_zero_density_congruence():
    """.local_zero_density_congruence() -> Rational
    
    Local Density Methods. Zero-type local density."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.local_zero_density_congruence(2, 1, [], [])
    assert res >= 0


@pytest.mark.slow
@pytest.mark.timeout(300)
def test_mass_at_two_by_counting_mod_power():
    """.mass_at_two_by_counting_mod_power() -> Rational

    Mass Formulas. Computes local mass at p=2 by counting solutions mod 2^k."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1])
    res = q.mass_at_two_by_counting_mod_power(3)
    assert res > 0


@pytest.mark.timeout(10)
def test_minkowski_reduction_for_4vars__SP():
    """.minkowski_reduction_for_4vars__SP() -> QuadraticForm
    
    Reduction Theory & Binary Forms. Specialized Minkowski reduction for exactly 4 variables."""
    q = DiagonalQuadraticForm(ZZ, [1, 1, 1, 1])
    res = q.minkowski_reduction_for_4vars__SP()
    assert res is not None


@pytest.mark.timeout(10)
def test_set_number_of_automorphisms():
    """.set_number_of_automorphisms() -> None
    
    Automorphism & Geometry. Manually set automorphism count cache."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    q.set_number_of_automorphisms(8)
    assert q.number_of_automorphisms() == 8


@pytest.mark.timeout(10)
def test_signature_vector():
    """.signature_vector() -> tuple[int, int, int]
    
    Local Field Invariants. Returns signature adjusted for different conventions."""
    q = DiagonalQuadraticForm(ZZ, [1, -1])
    res = q.signature_vector()
    assert res == (1, 1, 0)


@pytest.mark.timeout(10)
def test_theta_series_degree_2():
    """.theta_series_degree_2() -> PowerSeries
    
    Theta Series & Enumeration. Theta series with degree 2 optimization."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    res = q.theta_series_degree_2(10)
    assert res is not None


@pytest.mark.timeout(10)
def test_compute_definiteness_string_by_determinants():
    """.compute_definiteness_string_by_determinants() -> str
    
    Local Field Invariants. Computes definiteness using determinant criterion."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    result = q.compute_definiteness_string_by_determinants()
    assert result in ["pos_def", "neg_def", "indefinite", "degenerate"]


@pytest.mark.timeout(10)
def test_count_congruence_solutions_by_type():
    """.count_congruence_solutions() -> Integer

    Local Properties & Algorithms. Counts solutions to Q(v) = n mod p^k.
    Doc listed as count_congruence_solutions_by_type; actual method name is
    count_congruence_solutions.
    """
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    result = q.count_congruence_solutions(2, 1, 0, None, None)
    assert isinstance(result, int) and result >= 0


@pytest.mark.timeout(10)
def test_is_locally_represented():
    """.is_locally_represented_number() -> Boolean

    Local Properties & Algorithms. Returns True if number is locally represented at all places."""
    q = DiagonalQuadraticForm(ZZ, [1, 1])
    result = q.is_locally_represented_number(1)
    assert isinstance(result, bool)
