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

from sage.all import QQ, ZZ, Integer, matrix

from sage_lattice_category_spike.lattice_categories import Lattice
from sage_lattice_category_spike.objects.cardinals import Cardinal, aleph0
from sage_lattice_category_spike.objects.magmas import AdditiveGroups, Groups
from sage_lattice_category_spike.objects.modules import (
    FiniteFreeModules,
    FiniteProjectiveModules,
    Modules,
)
from sage_lattice_category_spike.objects.sets import Sets


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


def test_discriminant_groups_route_through_the_owned_additive_spine():
    group = Lattice("A2").discriminant_group()
    assert group in AdditiveGroups().AdditiveCommutative().Finite()


def test_a_discriminant_group_rolls_up_through_its_cyclic_factor_product():
    r"""The finite abelian group's rollup point is its cyclic-factor
    decomposition ``D = prod Z/n_i``: cardinality is the product's Cardinal
    and enumeration maps the factor product back through the group's own
    element constructor. The group-theory spelling ``order()`` keeps its
    classical Integer type."""
    group = Lattice("A2").discriminant_group()

    cardinality = group.cardinality()
    assert isinstance(cardinality, Cardinal)
    assert cardinality == 3
    assert group.is_finite()

    order = group.order()
    assert order == 3
    assert isinstance(order, Integer)

    elements = group.elements()
    assert len(elements) == 3
    assert len(set(elements)) == 3
    assert all(element.parent() is group for element in elements)
    assert group.zero() in elements

    trivial = Lattice("E8").discriminant_group()
    assert trivial.cardinality() == 1
    assert trivial.elements() == (trivial.zero(),)


def test_a_genus_is_a_finite_set_placed_in_the_owned_axioms():
    genus = Lattice("A2").genus()
    assert genus in Sets().Finite()

    cardinality = genus.cardinality()
    assert isinstance(cardinality, Cardinal)
    assert cardinality == 1
    assert cardinality == genus.class_number()
    assert genus.is_finite()

    representatives = list(genus)
    assert len(representatives) == 1
    assert representatives[0].genus() == genus


def test_the_isometry_homset_routes_through_the_torsor_node():
    r"""Isom(L, M) carries its O(M)-torsor structure as first-class data
    (acting_group + act) and its set behavior arrives through the general
    node's typed operations — the leaf spellings are gone."""
    a2 = Lattice("A2")
    homset = a2.Isom(a2)

    cardinality = homset.cardinality()
    assert isinstance(cardinality, Cardinal)
    assert cardinality == 12
    assert homset.acting_group() is a2.isometry_group()

    isometries = list(homset)
    assert len(isometries) == 12
    assert len(set(isometries)) == 12

    first, second = isometries[0], isometries[7]
    mover = homset.transporter(first, second)
    assert homset.act(mover, first) == second

    empty = a2.Isom(Lattice("A1").direct_sum(Lattice("A1")))
    assert empty.cardinality() == 0
    assert isinstance(empty.cardinality(), Cardinal)
    assert list(empty) == []


def test_isometry_groups_route_through_the_owned_group_node():
    r"""O(L) is placed in the owned Groups() node, so the forwarding root
    serves its set behavior: cardinality arrives through the underlying
    set's finite materialization, while order() keeps its classical
    Integer type from the engine."""
    group = Lattice("A2").isometry_group()
    assert group in Groups().Finite()

    cardinality = group.cardinality()
    assert isinstance(cardinality, Cardinal)
    assert cardinality == 12
    assert group.order() == 12
    assert isinstance(group.order(), Integer)
