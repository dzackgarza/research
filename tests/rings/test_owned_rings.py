from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _own_ring,
)


def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_session_integer_and_rational_rings_are_owned_views() -> None:
    session = _session()
    ZZ = session["ZZ"]
    QQ = session["QQ"]
    OwnedRings = session["OwnedRings"]
    OwnedFields = session["OwnedFields"]
    assert ZZ is not SageZZ
    assert QQ is not SageQQ
    assert ZZ in OwnedRings()
    assert QQ in OwnedFields()
    assert ZZ(3).parent() is ZZ
    assert QQ(3).parent() is QQ


def test_owned_ordered_ring_elements_compare_with_python_integers() -> None:
    session = _session()
    ZZ = session["ZZ"]
    QQ = session["QQ"]

    assert ZZ(2) > 1
    assert 1 < ZZ(2)
    assert ZZ(2) <= 2
    assert 2 >= ZZ(2)
    assert max(1, ZZ(2)) == ZZ(2)
    assert min(3, QQ(3) / 2) == QQ(3) / 2


def test_owned_ring_power_constructs_a_free_module_over_the_owned_ring() -> None:
    session = _session()
    ZZ = session["ZZ"]

    module = ZZ**3
    assert module.base_ring() is ZZ
    assert module.module_rank() == 3
    assert module is ZZ**3
    assert ZZ.free_module(ZZ(3)) is module
    assert ZZ.free_module(SageZZ(3)) is module


def test_owned_polynomial_and_matrix_ring_constructors_cross_to_the_engine() -> None:
    session = _session()
    QQ = session["QQ"]
    OwnedRings = session["OwnedRings"]

    polynomials = QQ.polynomial_ring("x")
    matrices = QQ.matrix_space(2)

    assert polynomials in OwnedRings()
    assert matrices in OwnedRings()
    assert polynomials.base_ring() is QQ
    assert matrices.base_ring() is QQ
    assert polynomials.algebra_generator("x").parent() is polynomials
    assert matrices.one().parent() is matrices
    assert QQ["x"] is polynomials


def test_owned_polynomial_ring_has_owned_selected_algebra_generators() -> None:
    session = _session()
    QQ = session["QQ"]
    ring = QQ["x, y"]

    x, y = ring.algebra_generators()
    assert x.parent() is ring
    assert y.parent() is ring
    assert ring.algebra_generating_set() == finite_ordered_set(("x", "y"))


def test_fraction_field_returns_the_owned_field() -> None:
    session = _session()
    ZZ = session["ZZ"]
    QQ = session["QQ"]

    assert ZZ.fraction_field() is QQ


def test_exact_reals_keep_the_owned_integer_rational_and_algebraic_inclusions() -> None:
    session = _session()
    ZZ = session["ZZ"]
    QQ = session["QQ"]
    AA = session["AA"]
    QQbar = session["QQbar"]
    RR = session["RR"]

    assert RR.has_coerce_map_from(ZZ)
    assert RR.has_coerce_map_from(QQ)
    assert RR.has_coerce_map_from(AA)
    assert not RR.has_coerce_map_from(QQbar)


def test_commutative_ring_is_its_own_center() -> None:
    session = _session()
    QQ = session["QQ"]

    assert QQ.ring_center() is QQ
    assert QQ.is_central(QQ(3)) is True


def test_noncommutative_center_is_a_predicate_subring() -> None:
    session = _session()
    QQ = session["QQ"]

    matrices = QQ.matrix_space(2)
    center = matrices.ring_center()

    assert center in session["OwnedRings"]()
    assert center in session["CommutativeRings"]()
    assert center.algebra_base_ring() is center
    assert center.regular_module() is center
    assert center.ambient_ring() is matrices
    assert center.inclusion().domain() is center
    assert center.inclusion().codomain() is matrices

    # Centrality is decided on the matrix units, the chosen algebra generators.
    assert matrices.one() in center
    assert next(iter(matrices.algebra_generators())) not in center


def test_owned_ring_constructors_return_owned_rings() -> None:
    session = _session()
    ZZ = session["ZZ"]
    OwnedFields = session["OwnedFields"]
    OwnedRings = session["OwnedRings"]

    assert session["GF"](5) in OwnedFields()
    assert session["PrimeField"](5) in session["PrimeFields"]()
    assert session["Zmod"](8) in OwnedRings()
    assert session["QuadraticField"](2, "a") in OwnedFields()
    assert session["QuadraticField"](ZZ(2), "a") in OwnedFields()
    assert session["QuadraticField"](SageZZ(2), "a") in OwnedFields()


def test_finite_ring_engine_adoption_keeps_initial_semantic_placement() -> None:
    session = _session()
    GF = session["GF"]
    Zmod = session["Zmod"]
    PrimeFields = session["PrimeFields"]
    LocalRings = session["LocalRings"]
    ArtinianRings = session["ArtinianRings"]

    prime = GF(5)
    extension = GF(4)
    local = Zmod(8)

    assert _own_ring(_engine_ring(prime)) is prime
    assert _own_ring(_engine_ring(extension)) is extension
    assert _own_ring(_engine_ring(local)) is local
    assert prime in PrimeFields()
    assert extension not in PrimeFields()
    assert local in LocalRings()
    assert local in ArtinianRings()
    assert local.residue_field() is GF(2)
    assert local.residue_map().domain() is local
    assert local.residue_map().codomain() is GF(2)


def test_explicit_algebraic_extensions_are_number_fields_or_orders() -> None:
    session = _session()
    ZZ = session["ZZ"]
    QQ = session["QQ"]
    QuadraticField = session["QuadraticField"]
    OwnedOrders = session["OwnedOrders"]
    OwnedFields = session["OwnedFields"]
    aleph0 = session["aleph0"]

    gaussian_field = QuadraticField(-1, "i")
    gaussian = gaussian_field.ring_of_integers()
    real_quadratic = QuadraticField(2, "a")
    order = real_quadratic.order_generated_by(real_quadratic.primitive_element())

    assert gaussian in OwnedOrders()
    assert gaussian_field in OwnedFields()
    assert order in OwnedOrders()
    assert gaussian.cardinality() == aleph0
    assert order.cardinality() == aleph0
    assert order.module_rank() in session["Cardinalities"]()
    assert real_quadratic.signature() == session["signature_pair"](2, 0)
    assert ZZ["x"].algebra_generating_set() == finite_ordered_set(("x",))
    assert tuple(QQ["x"].algebra_generating_set()) == ("x",)


def test_lattices_still_use_the_owned_integer_ring() -> None:
    session = _session()
    ZZ = session["ZZ"]
    lattice = session["Lattices"](ZZ)("U")

    assert lattice.base_ring() is ZZ
    assert repr(lattice).startswith("Integral lattice")



def test_loading_sage_namespace_restores_owned_ring_names(tmp_path) -> None:
    session = _session()
    ZZ = session["ZZ"]
    script = tmp_path / "rings.sage"
    script.write_text("from sage.all import *\nloaded = True\n")

    session["load"](str(script), session)

    assert session["loaded"] is True
    assert session["ZZ"] is ZZ
    assert session["ZZ"](3).parent() is ZZ


def test_owned_ring_cardinality_distinguishes_countable_and_uncountable_infinite_rings() -> None:
    session = _session()
    assert session["ZZ"].cardinality() == session["aleph0"]
    assert session["QQ"].cardinality() == session["aleph0"]
    assert session["QQbar"].cardinality() == session["aleph0"]
    assert session["RR"].cardinality() == session["continuum"]
    assert session["CC"].cardinality() == session["continuum"]
    assert session["Zp"](5).cardinality() == session["continuum"]
    assert session["Qp"](5).cardinality() == session["continuum"]


def test_owned_algebraic_real_and_complex_closures_are_countable() -> None:
    session = _session()
    AA = session["AA"]
    QQbar = session["QQbar"]
    aleph0 = session["aleph0"]

    assert AA.cardinality() == aleph0
    assert QQbar.cardinality() == aleph0


def test_owned_ring_display_comes_from_mathematical_presentation() -> None:
    session = _session()
    ZZ = session["ZZ"]
    QQ = session["QQ"]
    GF = session["GF"]
    Zmod = session["Zmod"]

    assert repr(ZZ) == "Integer Ring"
    assert repr(QQ) == "Rational Field"
    assert repr(GF(5)) == "GF(5)"
    assert repr(Zmod(6)) == "ZZ/6ZZ"
    polynomial = ZZ.polynomial_ring("x")
    assert repr(polynomial) == "Integer Ring[x]"
    assert repr(polynomial.algebra_generator("x")) == "x"
    assert "object at 0x" not in repr(polynomial)
