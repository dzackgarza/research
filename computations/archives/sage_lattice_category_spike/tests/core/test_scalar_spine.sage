r"""Scalar hierarchy and canonical placements (issue #212, CP2).

The owned scalar spine chains into the operation roots — a ring is an
additive commutative group with a compatible multiplicative monoid — and
reuses Sage's standard category names and joins (Euclidean domains, PIDs,
and friends arrive through Sage's own trunk, never a hand-written parallel
tree). The canonical scalars are the SAME one-object facades CP1 placed as
fundamental sets, with their placement refined by scalar axioms: set
refinements come from the CP1 placement, never from ring-level
declarations, and both structure-forgetting routes of the ring diamond
reach the identical underlying set on objects and morphisms.
"""

from __future__ import annotations

import itertools

from sage.all import GF, ZZ, Zmod
from sage.categories.euclidean_domains import EuclideanDomains as SageEuclideanDomains
from sage.categories.fields import Fields as SageFields
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.rings import Rings as SageRings

from sage_lattice_category_spike.objects.cardinals import aleph0, continuum
from sage_lattice_category_spike.objects.fundamental_sets import (
    FiniteField,
    IntegerModRing,
    Integers,
    NonNegativeIntegers,
    Rationals,
    Reals,
)
from sage_lattice_category_spike.objects.magmas import (
    AdditiveGroups,
    AdditiveMagmas,
    AdditiveMonoids,
    Magmas,
    Monoids,
    Semigroups,
    UnderlyingSetFunctor,
)
from sage_lattice_category_spike.objects.scalars import (
    DivisionRings,
    Fields,
    Rings,
    Rngs,
    Semirings,
)


def test_the_scalar_spine_chains_into_both_operation_roots():
    assert Rings().is_subcategory(SageRings())
    assert Rings().is_subcategory(Rngs())
    assert Rings().is_subcategory(Semirings())
    assert Rings().is_subcategory(Monoids())
    assert Rings().is_subcategory(AdditiveGroups())
    assert Rings().is_subcategory(Magmas())
    assert Rings().is_subcategory(AdditiveMagmas())
    assert Rngs().is_subcategory(Semigroups())
    assert Semirings().is_subcategory(AdditiveMonoids())
    assert Fields().is_subcategory(DivisionRings())
    assert DivisionRings().is_subcategory(Rings())
    assert Fields().is_subcategory(SageFields())


def test_canonical_scalars_sit_at_their_full_placement():
    integers = Integers()
    assert integers.category().is_subcategory(Rings().Commutative())
    assert integers.category().is_subcategory(SageEuclideanDomains())
    assert integers.is_countable()
    assert integers.cardinality() == aleph0

    naturals = NonNegativeIntegers()
    assert naturals.category().is_subcategory(Semirings().Commutative())
    assert naturals.is_countable()

    rationals = Rationals()
    assert rationals.category().is_subcategory(Fields())
    assert rationals.is_countable()
    assert rationals.cardinality() == aleph0

    reals = Reals()
    assert reals.category().is_subcategory(Fields())
    assert reals.is_uncountable()
    assert reals.cardinality() == continuum


def test_finite_scalars_have_exact_cardinality_through_their_hosts():
    mod_six = IntegerModRing(6)
    assert mod_six.category().is_subcategory(Rings().Commutative().Finite())
    assert mod_six.cardinality() == 6
    assert mod_six.is_finite()
    assert sorted(int(x) for x in mod_six) == [0, 1, 2, 3, 4, 5]
    assert Zmod(6)(4) in mod_six

    nine = FiniteField(9)
    assert nine.category().is_subcategory(Fields().Finite())
    assert nine.cardinality() == 9
    elements = list(nine)
    assert len(elements) == 9
    assert len(set(elements)) == 9


def test_no_scalar_class_repeats_a_generic_set_method():
    r"""The anti-bypass direction: the facades' own classes carry only
    their exact witnesses (enumeration, index formulas); cardinality and
    the countability predicates resolve through the forwarding roots and
    CP1's owners."""
    for facade_class in (Integers, Rationals, Reals, NonNegativeIntegers, IntegerModRing, FiniteField):
        assert "is_countable" not in vars(facade_class)
        assert "is_uncountable" not in vars(facade_class)
        assert "is_finite" not in vars(facade_class)
    for facade_class in (Integers, Rationals, Reals, NonNegativeIntegers):
        assert "cardinality" not in vars(facade_class)


def test_the_ring_diamond_reaches_one_underlying_set_on_objects_and_morphisms():
    integers = Integers()
    mod_six = IntegerModRing(6)
    through_multiplication = UnderlyingSetFunctor(Magmas())
    through_addition = UnderlyingSetFunctor(AdditiveMagmas())

    assert through_multiplication(integers) is through_addition(integers)

    reduction = SetMorphism(Hom(integers, mod_six, Rings()), lambda n: Zmod(6)(n))
    mult_image = through_multiplication(reduction)
    add_image = through_addition(reduction)
    assert mult_image.parent() is add_image.parent()
    assert mult_image(ZZ(11)) == add_image(ZZ(11)) == Zmod(6)(5)


def test_enumeration_witnesses_survive_the_placement_refinement():
    r"""The CP1 witness suite is untouched by the scalar refinement: same
    zigzag, same exact index formula, same round trips."""
    integers = Integers()
    assert list(itertools.islice(iter(integers), 5)) == [0, 1, -1, 2, -2]
    assert integers.index(-17) == 34
    assert integers.underlying_set()[integers.index(-9)] == -9
