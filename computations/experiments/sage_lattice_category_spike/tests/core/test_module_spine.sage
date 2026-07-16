r"""Module spine: owned free/projective nodes, rollup, coordinates
(issue #212, CP2).

The owned ``Modules(R)`` chains into the additive root (so ALL set
behavior is already rolled up through the underlying-set route — modules
add no forwarding of their own) and dispatches to ``VectorSpaces(K)``
over a field, mirroring Sage. Freeness and finite projectivity are
mathematical properties, strictly weaker than a chosen basis: the owned
``FreeModules(R)``/``FiniteFreeModules(R)``/``FiniteProjectiveModules(R)``
nodes carry the opt-in-with-trust predicate overrides (``is_free -> True``,
``is_torsionfree`` via ``is_free``, ``is_torsion -> False``), and
coordinates exist ONLY through a separately chosen basis, as a set
isomorphism ``U(M) <-> U(R) x ... x U(R)`` whose inverse returns module
elements."""

from __future__ import annotations

import itertools

from sage.all import QQ, ZZ, FreeModule, vector
from sage.categories.modules import Modules as SageModules
from sage.categories.vector_spaces import VectorSpaces as SageVectorSpaces
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.cardinals import aleph0
from sage_lattice_category_spike.objects.fundamental_sets import Integers
from sage_lattice_category_spike.objects.magmas import AdditiveGroups, AdditiveMagmas
from sage_lattice_category_spike.objects.modules import (
    FiniteFreeModules,
    FiniteProjectiveModules,
    FreeModules,
    Modules,
    VectorSpaces,
)
from sage_lattice_category_spike.objects.set_constructions import CartesianProduct


def test_the_module_spine_has_the_exact_owned_edges():
    assert Modules(ZZ).is_subcategory(SageModules(ZZ))
    assert Modules(ZZ).is_subcategory(AdditiveGroups())
    assert FreeModules(ZZ).is_subcategory(Modules(ZZ))
    assert FiniteProjectiveModules(ZZ).is_subcategory(Modules(ZZ))
    assert FiniteFreeModules(ZZ).is_subcategory(FreeModules(ZZ))
    assert FiniteFreeModules(ZZ).is_subcategory(FiniteProjectiveModules(ZZ))


def test_modules_over_a_field_dispatch_to_vector_spaces():
    dispatched = Modules(QQ)
    assert dispatched is VectorSpaces(QQ)
    assert dispatched.is_subcategory(SageVectorSpaces(QQ))
    assert dispatched.is_subcategory(SageModules(QQ))
    assert dispatched.is_subcategory(AdditiveMagmas())


class RankTwoIntegerModule(Parent):
    r"""``ZZ^2`` as an owned finite free module: facade over Sage's free
    module, supplying ONLY the enumeration witness (through the coordinate
    inverse and the fair product enumeration) — every predicate and every
    set behavior must arrive through the category."""

    def __init__(self):
        Parent.__init__(self, facade=FreeModule(ZZ, 2), category=FiniteFreeModules(ZZ).Countable().Infinite())

    def __iter__(self):
        host = FreeModule(ZZ, 2)
        for point in CartesianProduct(Integers().underlying_set(), Integers().underlying_set()):
            element = host(point.value)
            element.set_immutable()
            yield element


def test_opt_in_predicate_overrides_live_at_the_owned_nodes():
    module = RankTwoIntegerModule()
    assert module.is_free()
    assert module.is_torsionfree()
    assert not module.is_torsion()
    assert module.is_projective()
    assert module.is_finitely_generated()
    assert "is_free" not in vars(RankTwoIntegerModule)


def test_positive_rank_integer_modules_are_countably_infinite_through_composition():
    module = RankTwoIntegerModule()
    assert module.cardinality() == aleph0
    assert module.is_countable()
    assert not module.is_finite()

    coordinates = CartesianProduct(Integers().underlying_set(), Integers().underlying_set())
    assert coordinates.cardinality() == module.cardinality()

    prefix = list(itertools.islice(iter(module), 6))
    assert len(set(prefix)) == 6
    assert vector(ZZ, (0, 0)) in [p for p in prefix]


def test_coordinates_exist_only_through_a_chosen_basis_and_invert_to_module_elements():
    module = RankTwoIntegerModule()
    host = FreeModule(ZZ, 2)
    basis = (host((1, 1)), host((0, 1)))

    coordinates = module.coordinates(basis)
    from_coordinates = module.from_coordinates(basis)

    point = coordinates(host((3, 5)))
    assert point.value == (3, 2)

    element = from_coordinates(point)
    assert element == host((3, 5))
    assert element.parent() is host

    target = coordinates.codomain()
    assert from_coordinates(target((-2, 7))) == host((-2, 5))
    assert coordinates(from_coordinates(target((-2, 7)))) == target((-2, 7))
