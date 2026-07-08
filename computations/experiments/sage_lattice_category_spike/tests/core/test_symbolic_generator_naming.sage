r"""Issues #3/#4: named generators and symbolic element printing.

A lattice element is a formal R-combination of named generator symbols, like
``x`` in ``k[x]`` -- the interface is ``2*e - f``, never the coordinate vector
``(2, -1)``. Generator naming enters through the same preparser protocol as
polynomial rings (``L.<e,f> = ...`` -- the preparser rewrites this to a
``names=`` keyword plus ``L._first_ngens``), and printing is Sage's own
linear-combination renderer (``sage.misc.repr.repr_lincomb``), not a
hand-rolled join.
"""
from __future__ import annotations

import pytest

from sage.all import ZZ, matrix

from sage_lattice_category_spike.lattice_categories import Lattice, Lattices, RootLattice, U


def test_preparser_generator_binding_hyperbolic_plane():
    L.<e, f> = U()
    assert repr(e) == "e"
    assert repr(f) == "f"
    assert repr(e + f) == "e + f"
    assert repr(2 * e - f) == "2*e - f"
    assert L.variable_names() == ("e", "f")


def test_preparser_generator_binding_gram_constructor():
    M.<a, b> = Lattice(matrix(ZZ, [[2, 1], [1, 2]]))
    assert repr(a) == "a"
    assert repr(-a + 3 * b) == "-a + 3*b"
    assert M.variable_names() == ("a", "b")


def test_named_generators_on_root_lattice():
    R.<r1, r2> = RootLattice("A", 2)
    assert repr(r1 + r2) == "r1 + r2"


def test_names_keyword_without_preparser():
    L = U(names=("e", "f"))
    e, f = L.gens()
    assert repr(2 * e - f) == "2*e - f"
    assert L.variable_names() == ("e", "f")


def test_category_entry_point_accepts_names():
    L = Lattices(ZZ).from_gram_matrix(matrix(ZZ, [[0, 1], [1, 0]]), names=("e", "f"))
    assert repr(L.gen(0)) == "e"


def test_zero_element_prints_as_zero():
    L.<e, f> = U()
    assert repr(e - e) == "0"
    assert repr(L.zero()) == "0"


def test_default_names_are_indexed_generator_symbols():
    L = U()
    e0, e1 = L.gens()
    assert repr(2 * e0 - e1) == "2*e_0 - e_1"


def test_name_count_mismatch_is_a_caller_contract_bug():
    with pytest.raises((AssertionError, ValueError, IndexError)):
        U(names=("e", "f", "g"))


def test_generators_survive_arithmetic_round_trip():
    L.<e, f> = U()
    x = 2 * e - f
    assert x == L((2, -1))
    assert repr(x) != repr((2, -1))
