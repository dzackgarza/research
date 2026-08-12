r"""Footgun guards: a lattice element is a linear combination of generators --
NOT a coordinate tuple, list, or free-module vector, and not an element of R^n.

These assert strictly OFF the coordinate representations (never ON a particular
symbolic form, which is deliberately left open): an element must not be equal to,
contained among, or rendered as its raw coordinates. The coordinate vector is an
internal encoding, not the object's identity or its presentation.

See the trap ``a-sage-element-must-implement-richcmp-not-a-python-eq...`` and the
symbolic-gradient corrections: comparing coefficient tuples is legitimate internal
equality, but exposing or rendering the element AS those coordinates is the
footgun that invites reasoning about it as a vector in R^n.
"""
from __future__ import annotations

import pytest

from sage.all import ZZ, matrix, vector

from sage_lattice_category_spike.lattice_categories import Lattice, Lattices


CONSTRUCTORS = [
    pytest.param(lambda: Lattice("A2"), id="Lattice_A2_posdef"),
    pytest.param(lambda: Lattice("D4"), id="Lattice_D4_posdef"),
    pytest.param(lambda: Lattices(ZZ).from_gram_matrix(matrix(ZZ, [[2, 0], [0, 2]])), id="from_gram_definite_rank2"),
    pytest.param(lambda: Lattices(ZZ).from_gram_matrix(matrix(ZZ, [[2]])), id="from_gram_definite_rank1"),
    pytest.param(lambda: Lattice("U"), id="U_hyperbolic_plane"),
]


def _coordinate_forms(element):
    r"""The raw coordinate objects the element must NOT be conflated with."""
    coordinates = list(element.coefficient_vector())
    return [tuple(coordinates), coordinates, vector(ZZ, coordinates)]


@pytest.mark.parametrize("construct", CONSTRUCTORS)
def test_element_is_not_equal_to_any_coordinate_object(construct):
    r"""``element == (its coordinates as tuple/list/vector)`` must be False: the
    element lives in the lattice, the coordinates live in R^n; they are distinct
    objects and must never compare equal via coercion."""
    lattice = construct()
    for element in (lattice.zero(), lattice.gen(0)):
        for coordinate_object in _coordinate_forms(element):
            assert element != coordinate_object
            assert not (element == coordinate_object)


@pytest.mark.parametrize("construct", CONSTRUCTORS)
def test_element_is_not_contained_among_coordinate_objects(construct):
    r"""Membership routes through ``==``: an element must not be found inside a
    container of its own coordinate representations."""
    lattice = construct()
    for element in (lattice.zero(), lattice.gen(0)):
        assert element not in tuple(_coordinate_forms(element))


@pytest.mark.parametrize("construct", CONSTRUCTORS)
def test_element_repr_is_not_a_bare_coordinate(construct):
    r"""The element must not RENDER as its raw coordinates -- a lattice element
    is a combination of generators, not the tuple/list/vector of coefficients.
    Asserts off the coordinate reprs only, not on any particular symbolic form."""
    lattice = construct()
    for element in (lattice.zero(), lattice.gen(0)):
        coordinates = element.coefficient_vector()
        assert repr(element) != repr(coordinates)
        assert repr(element) != repr(vector(ZZ, list(coordinates)))
        assert repr(element) != repr(tuple(coordinates))
        assert repr(element) != repr(list(coordinates))
