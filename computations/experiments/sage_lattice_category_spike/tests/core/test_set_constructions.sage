r"""Set constructions: finite Cartesian products and tagged disjoint unions
with their refinement rules (issue #211, constructions commit of CP1).

The construction owns its construction-specific behavior (decision:
sets-owns-cardinality-through-standard-constructions): the empty product is
the finite singleton, an empty factor takes precedence over everything, a
finite product of countable factors is countable and receives one fair
enumeration, infinitude and uncountability propagate exactly when every
other factor is nonempty, and coproduct cardinality is the sum over tagged
summands. Maps act componentwise; projections and injections are elements
of the actual homsets.
"""

from __future__ import annotations

import itertools

from sage.all import ZZ, oo
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.cardinals import aleph0, continuum
from sage_lattice_category_spike.objects.fundamental_sets import Integers, Reals
from sage_lattice_category_spike.objects.set_constructions import (
    CartesianProduct,
    DisjointUnion,
    cartesian_product_morphism,
)
from sage_lattice_category_spike.objects.sets import Sets


class PrimesBelowSeven(Parent):
    r"""The finite set {2, 3, 5}, operationally countable. A facade that is
    a PROPER subset of its host must own membership: the facade default
    delegates to the host."""

    def __init__(self):
        Parent.__init__(self, facade=ZZ, category=Sets().Finite().Facade())

    def __iter__(self):
        return iter([ZZ(2), ZZ(3), ZZ(5)])

    def __contains__(self, x):
        return x in (2, 3, 5)

    def cardinality(self):
        return ZZ(3)


class EmptySet(Parent):
    r"""The empty set, finite with cardinality zero."""

    def __init__(self):
        Parent.__init__(self, facade=ZZ, category=Sets().Finite().Facade())

    def __iter__(self):
        return iter(())

    def __contains__(self, x):
        return False

    def cardinality(self):
        return ZZ(0)


def test_empty_product_is_the_finite_singleton():
    empty_product = CartesianProduct()
    assert empty_product.is_finite()
    assert empty_product.cardinality() == 1
    elements = list(empty_product)
    assert len(elements) == 1
    assert elements[0] == empty_product(())


def test_empty_factor_takes_precedence_over_everything():
    r"""A product with an empty factor is the finite empty set, even when
    another factor is uncountable."""
    product = CartesianProduct(Reals(), EmptySet())
    assert product.is_finite()
    assert not product.is_uncountable()
    assert product.cardinality() == 0
    assert list(product) == []


def test_finite_product_multiplies_exact_cardinalities():
    primes = PrimesBelowSeven()
    product = CartesianProduct(primes, primes)
    assert product.is_finite()
    assert product.cardinality() == 9
    elements = list(product)
    assert len(elements) == 9
    assert len(set(elements)) == 9
    assert product((3, 5)) in product
    assert (4, 5) not in product
    assert product[product.index(product((5, 2)))] == product((5, 2))


def test_countable_product_of_infinite_factors_is_fairly_enumerated():
    integers = Integers()
    product = CartesianProduct(integers, integers)
    assert product.is_countable()
    assert not product.is_finite()
    assert product.cardinality() == oo

    assert product.cardinality() == aleph0

    prefix = list(itertools.islice(iter(product), 16))
    assert len(set(prefix)) == 16
    assert product((0, 0)) in prefix
    assert product((0, 1)) in prefix[:4]
    assert product((1, 0)) in prefix[:4]

    witness = product((3, -2))
    assert product[product.index(witness)] == witness


def test_uncountable_factor_propagates_when_others_are_nonempty():
    product = CartesianProduct(Integers(), Reals())
    assert product.is_uncountable()
    assert not product.is_countable()
    assert not product.is_finite()
    assert product.cardinality() == continuum
    assert product.cardinality() > aleph0


def test_projections_are_homset_elements_acting_componentwise():
    primes = PrimesBelowSeven()
    integers = Integers()
    product = CartesianProduct(primes, integers)
    first = product.projection(0)
    second = product.projection(1)

    assert first.parent() is Hom(product, primes, SageSets())
    pair = product((5, -7))
    assert pair.value == (5, -7)
    assert first(pair) == 5
    assert second(pair) == -7
    assert second(pair).parent() is ZZ


def test_cartesian_product_morphism_acts_componentwise():
    integers = Integers()
    negate = SetMorphism(Hom(integers, integers, SageSets()), lambda v: -v)
    double = SetMorphism(Hom(integers, integers, SageSets()), lambda v: 2 * v)
    product_map = cartesian_product_morphism(negate, double)

    domain = CartesianProduct(integers, integers)
    assert product_map.domain() is domain
    image = product_map(domain((3, 5)))
    assert image == product_map.codomain()((-3, 10))


def test_disjoint_union_tags_summands_and_sums_cardinality():
    primes = PrimesBelowSeven()
    union = DisjointUnion(primes, primes)
    assert union.is_finite()
    assert union.cardinality() == 6
    elements = list(union)
    assert len(set(elements)) == 6
    assert union((0, 2)) != union((1, 2))

    empty_union = DisjointUnion()
    assert empty_union.is_finite()
    assert empty_union.cardinality() == 0
    assert list(empty_union) == []


def test_disjoint_union_interleaves_countable_summands_fairly():
    integers = Integers()
    primes = PrimesBelowSeven()
    union = DisjointUnion(integers, primes)
    assert union.is_countable()
    assert not union.is_finite()
    assert union.cardinality() == oo

    prefix = list(itertools.islice(iter(union), 8))
    assert len(set(prefix)) == 8
    assert union((0, 0)) in prefix
    assert union((1, 2)) in prefix

    injection = union.injection(1)
    assert injection.parent() is Hom(primes, union, SageSets())
    assert injection(ZZ(5)) == union((1, 5))
    assert injection(ZZ(5)) in union


def test_uncountable_summand_makes_the_union_uncountable():
    union = DisjointUnion(Integers(), Reals())
    assert union.is_uncountable()
    assert not union.is_finite()
    assert union.cardinality() == continuum


def test_disjoint_union_membership_agrees_with_construction_on_sage_integer_tags():
    r"""A preparsed literal tag is a Sage Integer, not a Python int: the
    advertised raw ``(tag, element)`` representation must be accepted by
    membership exactly where the element constructor accepts it."""
    union = DisjointUnion(Integers(), Integers())
    assert (ZZ(1), ZZ(5)) in union
    assert (int(1), int(5)) in union
    assert union((ZZ(1), ZZ(5))) == union((int(1), int(5)))
    assert (ZZ(2), ZZ(5)) not in union
    assert ("1", ZZ(5)) not in union


def test_owned_constructions_stay_aligned_with_the_delegated_native_machinery():
    r"""The owned parents delegate fair iteration to Sage's native
    constructions; this pins the alignment at the REAL boundary — the
    owned enumeration is exactly the delegated one's, element for element,
    and the owned points carry the owned parent while agreeing with the
    native raw representation (the Integer-tag drift was exactly such a
    wrapper/native disagreement)."""
    from itertools import islice

    from sage.categories.cartesian_product import cartesian_product
    from sage.sets.disjoint_union_enumerated_sets import DisjointUnionEnumeratedSets
    from sage.sets.family import Family

    integers = Integers()
    product = CartesianProduct(integers, integers)
    native_product = cartesian_product([integers, integers])
    for owned, native in islice(zip(product, native_product), 12):
        assert tuple(owned.value) == tuple(native)
        assert owned.parent() is product

    union = DisjointUnion(integers, integers)
    native_union = DisjointUnionEnumeratedSets(Family({0: integers, 1: integers}), keepkey=True)
    for owned, native in islice(zip(union, native_union), 12):
        assert (int(owned.value[0]), owned.value[1]) == (int(native[0]), native[1])
        assert owned.parent() is union
        assert native in union
