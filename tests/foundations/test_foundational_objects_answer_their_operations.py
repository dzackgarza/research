r"""The positive companion to ``tests/test_owned_category_graph_purity.py``.

The purity specimen asserts what the foundational graph does *not* contain: no
``sage.categories.*`` node reachable through ``super_categories()``.  Nothing in
it can fail on a graph that is pure and answers nothing, so it passes equally on
a working foundation and a hollow one.

This file asserts what the graph *does*.  Each test takes one of the same ten
roots, builds a small object, and asks it for the elementary operations its
categories promise, against values a reader can check by hand.  It is the
termination condition for the root `TODO.md` Priority 3 step 7: while any of
these fails, removing a Sage supercategory edge has taken away mathematics that
was never restored at its owned owner.

Specimens are deliberately small.  U, C_4, and ZZ[x] carry every claim here; a
larger lattice would prove nothing extra and cost a reader time.
"""



def _session():
    scope = {}
    exec("from dzack_research.preamble.all import *", scope)
    return scope














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
