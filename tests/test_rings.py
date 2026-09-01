from sage.categories.commutative_rings import CommutativeRings
from sage.categories.rings import Rings as SageRings
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ


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
    engine_ring = session["engine_ring"]

    assert ZZ is not SageZZ
    assert QQ is not SageQQ
    assert ZZ in OwnedRings()
    assert QQ in OwnedFields()
    assert engine_ring(ZZ) is SageZZ
    assert engine_ring(QQ) is SageQQ
    assert ZZ(3).parent() is SageZZ
    assert QQ(3).parent() is SageQQ


def test_owned_ring_power_constructs_a_free_module_over_the_owned_ring() -> None:
    session = _session()
    ZZ = session["ZZ"]

    module = ZZ**3
    assert module.base_ring() is ZZ
    assert module.rank() == 3
    assert module is ZZ**3


def test_owned_polynomial_and_matrix_ring_constructors_cross_to_the_engine() -> None:
    session = _session()
    QQ = session["QQ"]
    OwnedRings = session["OwnedRings"]
    engine_ring = session["engine_ring"]
    PolynomialRing = session["PolynomialRing"]
    MatrixSpace = session["MatrixSpace"]

    polynomials = PolynomialRing(QQ, "x")
    matrices = MatrixSpace(QQ, 2)

    assert polynomials in OwnedRings()
    assert matrices in OwnedRings()
    assert polynomials.base_ring() is QQ
    assert matrices.base_ring() is QQ
    assert engine_ring(polynomials).base_ring() is SageQQ
    assert engine_ring(matrices).base_ring() is SageQQ

    assert QQ["x"] is polynomials


def test_owned_polynomial_ring_supports_sage_generator_assignment_hook() -> None:
    session = _session()
    QQ = session["QQ"]
    ring = QQ["x, y"]

    x, y = ring._first_ngens(2)
    assert x.parent() is session["engine_ring"](ring)
    assert y.parent() is session["engine_ring"](ring)
    assert ring.variable_names() == ("x", "y")


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
    MatrixSpace = session["MatrixSpace"]

    matrices = MatrixSpace(QQ, 2)
    center = matrices.ring_center()

    assert center in SageRings()
    assert center in CommutativeRings()
    assert center.ambient_ring() is matrices
    assert center.inclusion().domain() is center
    assert center.inclusion().codomain() is matrices

    try:
        matrices.one() in center
    except NotImplementedError:
        pass
    else:
        raise AssertionError(
            "centrality in a matrix ring was guessed without a represented generating set"
        )


def test_owned_ring_constructors_return_owned_rings() -> None:
    session = _session()
    OwnedFields = session["OwnedFields"]
    OwnedRings = session["OwnedRings"]

    assert session["GF"](5) in OwnedFields()
    assert session["PrimeField"](5) in session["PrimeFields"]()
    assert session["Zmod"](8) in OwnedRings()
    assert session["QuadraticField"](2, "a") in OwnedFields()


def test_algebraic_adjunction_is_a_number_field_or_order() -> None:
    session = _session()
    ZZ = session["ZZ"]
    QQ = session["QQ"]
    I = session["I"]
    sqrt = session["sqrt"]
    OwnedOrders = session["OwnedOrders"]
    OwnedFields = session["OwnedFields"]
    aleph0 = session["aleph0"]

    gaussian = ZZ[I]
    cyclotomic_field = QQ[I]
    order = ZZ[sqrt(2)]

    assert gaussian in OwnedOrders()
    assert cyclotomic_field in OwnedFields()
    assert order in OwnedOrders()
    assert gaussian.cardinality() == aleph0
    assert order.cardinality() == aleph0
    assert ZZ["x"].variable_names() == ("x",)
    assert QQ["x"].variable_names() == ("x",)


def test_lattices_still_use_the_owned_integer_ring() -> None:
    session = _session()
    ZZ = session["ZZ"]
    lattice = session["Lattices"](ZZ)("U")

    assert lattice.base_ring() is ZZ
    assert repr(lattice).startswith("Integral lattice")

    from dzack_research.preamble.categories.lattices import Lattices

    assert Lattices(SageZZ) is Lattices(ZZ)


def test_loading_sage_namespace_restores_owned_ring_names(tmp_path) -> None:
    session = _session()
    ZZ = session["ZZ"]
    script = tmp_path / "rings.sage"
    script.write_text("from sage.all import *\nloaded = True\n")

    session["load"](str(script), session)

    assert session["loaded"] is True
    assert session["ZZ"] is ZZ
    assert session["engine_ring"](session["ZZ"]) is SageZZ


def test_owned_ring_cardinality_distinguishes_countable_and_uncountable_infinite_rings() -> None:
    session = _session()
    assert session["ZZ"].cardinality() == session["aleph0"]
    assert session["QQ"].cardinality() == session["aleph0"]
    assert session["QQbar"].cardinality() == session["aleph0"]
    assert session["RR"].cardinality() == session["continuum"]
    assert session["CC"].cardinality() == session["continuum"]
    assert session["Zp"](5).cardinality() == session["continuum"]
    assert session["Qp"](5).cardinality() == session["continuum"]
