
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_ring,
    _own_ring,
)


def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


















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


