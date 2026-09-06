r"""The positive companion to ``tests/test_owned_category_graph_purity.py``.

The purity specimen asserts what the foundational graph does *not* contain: no
``sage.categories.*`` node reachable through ``super_categories()``.  Nothing in
it can fail on a graph that is pure and answers nothing, so it passes equally on
a working foundation and a hollow one.

This file asserts what the graph *does*.  Each test takes one of the same ten
roots, builds a small object, and asks it for the elementary operations its
categories promise, against values a reader can check by hand.  It is the
termination condition for `TODO-PRIORITIES.md` Priority 3 step 7: while any of
these fails, removing a Sage supercategory edge has taken away mathematics that
was never restored at its owned owner.

Specimens are deliberately small.  U, C_4, and ZZ[x] carry every claim here; a
larger lattice would prove nothing extra and cost a reader time.
"""

from dzack_research.preamble.categories.rings.ring_foundation import OwnedRings
from dzack_research.preamble.categories.sets.set_categories import Sets


def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope


def test_the_owned_integers_answer_their_ring_operations() -> None:
    ZZ = _session()["ZZ"]

    assert ZZ in OwnedRings()
    assert ZZ.zero() + ZZ(7) == ZZ(7)
    assert ZZ.one() * ZZ(7) == ZZ(7)
    assert ZZ(3) + ZZ(4) == ZZ(7)
    assert ZZ(3) * ZZ(4) == ZZ(12)
    assert (-ZZ(3)) + ZZ(3) == ZZ.zero()


def test_a_free_module_answers_its_module_operations() -> None:
    session = _session()
    ZZ = session["ZZ"]

    module = ZZ**2
    assert module.base_ring() is ZZ
    assert module.module_rank() == 2

    v, w = module.module_generators()
    assert v + w == w + v
    assert ZZ(3) * v == v + v + v
    assert v - v == module.zero()
    assert (v + w).parent() is module


def test_cardinality_is_inherited_through_the_construction() -> None:
    r"""A module is built on an underlying set, so it answers set questions.

    `AGENTS.md`: "``L.cardinality()`` must work without ``Lattices`` naming
    cardinality."  The same holds one level down: ``Modules`` does not name
    cardinality either.  ZZ^2 is countably infinite, so it is not finite and its
    cardinality equals that of ZZ.
    """
    session = _session()
    ZZ = session["ZZ"]

    module = ZZ**2
    assert module in Sets()
    assert not module.is_finite()
    assert module.cardinality() == ZZ.cardinality()


def test_a_finite_cyclic_group_answers_its_group_operations() -> None:
    session = _session()
    Groups = session["Groups"]

    C4 = Groups.C(4)
    assert C4.order() == 4

    g, = C4.group_generators()
    assert g * C4.one() == g
    assert g**4 == C4.one()
    assert g**2 != C4.one()
    assert g * g.inverse() == C4.one()


def test_an_abelian_group_has_the_canonical_integer_action() -> None:
    r"""An abelian group is a ZZ-module; the action is not optional data."""
    session = _session()
    ZZ = session["ZZ"]
    Groups = session["Groups"]

    C4 = Groups.C(4)
    g, = C4.group_generators()
    assert ZZ(3) * g == g * g * g
    assert ZZ(4) * g == C4.one()
    assert ZZ(-1) * g == g.inverse()


def test_a_polynomial_algebra_answers_its_algebra_operations() -> None:
    session = _session()
    ZZ = session["ZZ"]
    PolynomialRing = session["PolynomialRing"]

    A = PolynomialRing(ZZ, "x")
    x, = A.algebra_generators()
    assert A.base_ring() is ZZ
    assert A.one() * x == x
    assert A.zero() + x == x
    assert (x + A.one()) * (x - A.one()) == x**2 - A.one()


def test_the_hyperbolic_plane_answers_its_lattice_operations() -> None:
    r"""U is the rank-2 even unimodular lattice of signature (1, 1)."""
    session = _session()
    ZZ = session["ZZ"]
    Lattices = session["Lattices"]

    U = Lattices(ZZ)("U")
    assert U.module_rank() == 2
    assert U.determinant() == -1
    assert U.signature_pair() == session["signature_pair"](1, 1)

    e, f = U.module_generators()
    assert U.form()(e, e) == ZZ.zero()
    assert U.form()(f, f) == ZZ.zero()
    assert U.form()(e, f) == ZZ.one()
