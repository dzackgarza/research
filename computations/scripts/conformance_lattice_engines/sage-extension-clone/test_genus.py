"""Tests for sage.quadratic_forms.genus.Genus

Genus objects representing a genus of quadratic forms, typically obtained
via QuadraticForm.global_genus_symbol() or IntegralLattice.genus().

Doc sections: Construction, Global Properties, Local Analysis,
Genus Invariants, Operations.
"""

import pytest
from sage.all import ZZ, Genus, Matrix
from sage.modules.free_quadratic_module_integer_symmetric import IntegralLattice
from sage.quadratic_forms.genera.genus import GenusSymbol_global_ring
from sage.quadratic_forms.quadratic_form import QuadraticForm

TEST_TARGET = GenusSymbol_global_ring


@pytest.mark.timeout(10)
def test_genus_from_quadratic_form():
    """Genus(matrix: Matrix) -> Genus

    Construction. Constructor from a Gram matrix via QuadraticForm.global_genus_symbol().
    """
    g_mat = Matrix(ZZ, [[2, 0, 0], [0, 2, 0], [0, 0, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    assert genus is not None


@pytest.mark.timeout(10)
def test_genus_from_local_symbols():
    """Genus(local_symbols: list) -> Genus

    Construction. Constructor from a list of local genus symbols.
    Build a genus from its local data by extracting local_symbols() from an
    existing genus and reconstructing via Genus(local_symbols).
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    original = q.global_genus_symbol()
    local_syms = original.local_symbols()
    reconstructed = GenusSymbol_global_ring(original.signature_pair_of_matrix(), local_syms)
    assert reconstructed.dimension() == original.dimension()
    assert reconstructed.determinant() == original.determinant()


@pytest.mark.timeout(10)
def test_dimension():
    """.dimension() -> Integer

    Global Properties. Returns the dimension of the quadratic forms in this genus.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    assert genus.dimension() == 2


@pytest.mark.timeout(10)
def test_determinant():
    """.determinant() -> Integer

    Global Properties. Returns the Hessian determinant of the genus.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    det = genus.determinant()
    assert det is not None


@pytest.mark.timeout(10)
def test_signature():
    """.signature() -> Integer

    Global Properties. Returns the signature (p - n).
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    sig = genus.signature()
    assert sig is not None


@pytest.mark.timeout(10)
def test_level():
    """.level() -> Integer

    Global Properties. Returns the level of the genus.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    level = genus.level()
    assert level is not None


@pytest.mark.timeout(10)
def test_is_even():
    """.is_even() -> Boolean

    Global Properties. Returns True if the genus is even.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    result = genus.is_even()
    assert isinstance(result, bool)


@pytest.mark.timeout(10)
def test_local_symbol():
    """.local_symbol(p: Integer) -> LocalGenusSymbol

    Local Analysis. Returns the local genus symbol at prime p.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    local_sym = genus.local_symbol(2)
    assert local_sym is not None


@pytest.mark.timeout(10)
def test_local_symbols():
    """.local_symbols() -> list[LocalGenusSymbol]

    Local Analysis. Returns the list of all local genus symbols.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    local_syms = genus.local_symbols()
    assert isinstance(local_syms, list)


@pytest.mark.timeout(10)
def test_mass():
    """.mass() -> Rational

    Genus Invariants. Returns the mass using the Smith-Minkowski-Siegel formula.
    WARNING: Requires positive-definite or indefinite form.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    mass = genus.mass()
    assert mass is not None


@pytest.mark.timeout(10)
def test_spinor_generators():
    """.spinor_generators(proper: Boolean) -> list[Integer]

    Genus Invariants. Returns primes that generate the (proper) spinor genus classes.
    WARNING: Requires positive-definite form.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    spinor = genus.spinor_generators(False)
    assert isinstance(spinor, list)


@pytest.mark.timeout(10)
def test_discriminant_form():
    """.discriminant_form() -> DiscriminantForm

    Genus Invariants. Returns the discriminant form associated with the genus.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    df = genus.discriminant_form()
    assert df is not None


@pytest.mark.timeout(10)
def test_direct_sum():
    """.direct_sum(other: Genus) -> Genus

    Operations. Returns the genus of the direct sum of this genus and other.
    """
    g1 = Matrix(ZZ, [[2, 0], [0, 2]])
    q1 = QuadraticForm(g1)
    genus1 = q1.global_genus_symbol()

    g2 = Matrix(ZZ, [[2, 0], [0, 2]])
    q2 = QuadraticForm(g2)
    genus2 = q2.global_genus_symbol()

    ds = genus1.direct_sum(genus2)
    assert ds is not None


@pytest.mark.timeout(10)
def test_representative():
    """.representative() -> QuadraticForm

    Operations. Returns a quadratic form representing this genus.
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    rep = genus.representative()
    assert rep is not None


@pytest.mark.timeout(10)
def test_genus_from_integral_lattice():
    """.genus() -> Genus
    
    Returns the genus symbol of the integral lattice.
    """
    lat = IntegralLattice("A3")
    genus = lat.genus()
    assert genus is not None


@pytest.mark.timeout(10)
def test_det():
    """.det() -> Integer
    
    Alias for determinant().
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    assert genus.det() == genus.determinant()


@pytest.mark.timeout(10)
def test_dim():
    """.dim() -> Integer
    
    Alias for dimension().
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    assert genus.dim() == genus.dimension()


@pytest.mark.timeout(10)
def test_rank():
    """.rank() -> Integer
    
    Alias for dimension().
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    assert genus.rank() == genus.dimension()


@pytest.mark.timeout(10)
def test_norm():
    """.norm() -> Integer
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    assert genus.norm() is not None


@pytest.mark.timeout(10)
def test_rational_representative():
    """.rational_representative() -> QuadraticForm
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    rep = genus.rational_representative()
    assert rep is not None


@pytest.mark.timeout(10)
def test_representatives():
    """.representatives() -> list[QuadraticForm]
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    reps = genus.representatives()
    assert isinstance(reps, (list, tuple))
    assert len(reps) > 0


@pytest.mark.timeout(10)
def test_scale():
    """.scale() -> Rational
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    assert genus.scale() is not None


@pytest.mark.timeout(10)
def test_signature_pair():
    """.signature_pair() -> tuple[Integer, Integer]

    Global Properties. Returns the signature pair (p, n).
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    sig = genus.signature_pair()
    assert isinstance(sig, tuple)
    assert len(sig) == 2


@pytest.mark.timeout(10)
def test_signature_pair_of_matrix():
    """.signature_pair_of_matrix() -> tuple[Integer, Integer]
    
    Alias for signature_pair().
    """
    g_mat = Matrix(ZZ, [[2, 1], [1, 2]])
    q = QuadraticForm(g_mat)
    genus = q.global_genus_symbol()
    sig = genus.signature_pair_of_matrix()
    assert isinstance(sig, tuple)
    assert len(sig) == 2
    assert sig == genus.signature_pair()
