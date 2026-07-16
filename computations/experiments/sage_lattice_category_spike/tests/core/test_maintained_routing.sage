r"""Maintained parents route through the owned foundation (issue #213, CP3).

The maintained graph's central claim: every maintained parent reaches
generic set behavior through the CP1/CP2 foundation instead of leaf
implementations. Lattices are based free modules, so their route is
``Lattices(R) -> FiniteFreeModules(R) -> FiniteProjectiveModules(R) ->
Modules(R) -> ... -> Sets()``, and the based node owns the sharp rollup
point: a CHOSEN basis identifies ``U(L)`` with ``U(R) x ... x U(R)``
(the trivialization crosses the presentation boundary exactly once), so
``L.cardinality() := |U(R)^rank|`` and enumeration maps the coordinate
product back through the trivialization — yielding lattice elements,
never coordinate tuples.
"""

from __future__ import annotations

from itertools import islice

from sage.all import QQ, ZZ, matrix

from sage_lattice_category_spike.lattice_categories import Lattice
from sage_lattice_category_spike.objects.cardinals import Cardinal, aleph0
from sage_lattice_category_spike.objects.modules import (
    FiniteFreeModules,
    FiniteProjectiveModules,
    Modules,
)


def test_lattices_route_through_the_owned_module_spine():
    a2 = Lattice("A2")
    assert a2 in FiniteFreeModules(ZZ)
    assert a2 in FiniteProjectiveModules(ZZ)
    assert a2 in Modules(ZZ)
    assert a2.is_free()
    assert a2.is_torsionfree()
    assert not a2.is_torsion()


def test_a_positive_rank_lattice_is_countably_infinite_through_the_rollup():
    a2 = Lattice("A2")
    cardinality = a2.cardinality()
    assert isinstance(cardinality, Cardinal)
    assert cardinality == aleph0
    assert not a2.is_finite()
    assert a2.is_infinite()
    assert a2.is_countable()
    assert not a2.is_uncountable()

    rational = a2.base_extend(QQ)
    assert rational.cardinality() == aleph0
    assert rational.is_countable()


def test_the_rank_zero_lattice_is_the_singleton():
    trivial = Lattice(matrix(ZZ, 0, 0, []), label="zero-lattice")
    cardinality = trivial.cardinality()
    assert isinstance(cardinality, Cardinal)
    assert cardinality == 1
    assert trivial.is_finite()
    points = list(trivial)
    assert points == [trivial.zero()]
    assert points[0].parent() is trivial


def test_enumeration_returns_lattice_elements_through_the_chosen_basis():
    a2 = Lattice("A2")
    elements = list(islice(iter(a2), 24))
    assert len(set(elements)) == 24
    assert all(element.parent() is a2 for element in elements)
    assert a2.zero() in elements
    assert a2([1, 0]) in elements
    # the enumeration speaks the lattice's own vocabulary: the form
    # evaluates on enumerated elements (A2 is negative-definite here)
    assert all(element.q() <= 0 for element in elements)
