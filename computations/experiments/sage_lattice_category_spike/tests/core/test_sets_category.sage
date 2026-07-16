r"""Owned Sets root: axioms, registration adapter, and witness contracts
(issue #211, Sets commit of CP1).

The owned ``Sets()`` sits over Sage's ``Sets()`` and reuses its standard
``Finite``/``Infinite`` axioms; project-owned ``Countable``/``Uncountable``
enter Sage's ``all_axioms`` through the exact idempotent adapter. The
relations are mathematical facts of the axiom lattice: ``Finite`` refines
``Countable``, ``Uncountable`` refines ``Infinite``, and each owned pair of
contradictory axioms is refused at the request boundary. Membership is
opt-in-with-trust: ``Countable`` forces the executable enumeration suite
through abstract methods, while ``Uncountable`` is trusted placement with
uniform consequences and no enumeration obligation.
"""

from __future__ import annotations

import json
import os
import subprocess

import pytest

from sage.all import oo
from sage.categories.sets_cat import Sets as SageSets
from sage.structure.parent import Parent

from sage_lattice_category_spike.objects.sets import Sets


# The complete documented owned registration set: the form axioms from
# objects/categories.py plus the two set axioms from objects/sets.py.
# Exactness is the contract — a new registration anywhere in the package
# must consciously extend this list.
_OWNED_REGISTRATIONS = {
    "Nondegenerate",
    "Integral",
    "Even",
    "Unimodular",
    "Definite",
    "PositiveDefinite",
    "NegativeDefinite",
    "Indefinite",
    "Hyperbolic",
    "RootGenerated",
    "Bilinear",
    "Quadratic",
    "WithSourceLattice",
    "Countable",
    "Uncountable",
}


def test_axiom_registration_is_exact_and_idempotent_in_an_isolated_process():
    r"""A fresh Sage process importing the package changes ``all_axioms`` by
    exactly the documented owned registrations, and re-running the set-axiom
    adapter changes nothing."""
    script = (
        "import sage.all  # settle Sage's own lazy axiom registrations first\n"
        "from sage.categories.category_with_axiom import all_axioms\n"
        "before = set(str(a) for a in all_axioms)\n"
        "import sage_lattice_category_spike.objects.sets\n"
        "after = set(str(a) for a in all_axioms)\n"
        "from sage_lattice_category_spike.objects.sets import register_set_axioms\n"
        "register_set_axioms()\n"
        "register_set_axioms()\n"
        "assert set(str(a) for a in all_axioms) == after, 'adapter is not idempotent'\n"
        "import json\n"
        "print(json.dumps(sorted(after - before)))\n"
    )
    result = subprocess.run(
        [os.environ["SAGE_BIN"], "-python", "-c", script],
        capture_output=True,
        text=True,
        check=True,
    )
    added = set(json.loads(result.stdout.strip().splitlines()[-1]))
    assert added == _OWNED_REGISTRATIONS


def test_owned_sets_root_sits_over_sage_sets():
    r"""The owned root is a genuine subcategory of Sage's ``Sets()``, and a
    countably infinite set is expressed as ``Sets().Countable().Infinite()``,
    not a new named root."""
    assert Sets().is_subcategory(SageSets())
    countably_infinite = Sets().Countable().Infinite()
    assert countably_infinite.is_subcategory(Sets().Countable())
    assert countably_infinite.is_subcategory(SageSets().Infinite())


def test_finite_refines_countable_and_uncountable_refines_infinite():
    r"""Every finite set receives the countable enumeration contract, and an
    uncountable set is in particular infinite."""
    assert Sets().Finite().is_subcategory(Sets().Countable())
    assert Sets().Uncountable().is_subcategory(Sets().Infinite())


def test_contradictory_owned_axioms_are_refused_at_the_request_boundary():
    r"""``Countable``/``Uncountable`` are disjoint at the owned boundary,
    ``Finite`` implies ``Countable`` so ``Finite``+``Uncountable`` is
    refused too, and ``Uncountable``+``Finite`` is refused by Sage's native
    finite/infinite incompatibility because ``Uncountable`` implies
    ``Infinite``."""
    with pytest.raises(AssertionError):
        Sets().Countable().Uncountable()
    with pytest.raises(AssertionError):
        Sets().Uncountable().Countable()
    with pytest.raises(AssertionError):
        Sets().Finite().Uncountable()
    with pytest.raises(TypeError):
        Sets().Uncountable().Finite()


class OddNaturals(Parent):
    r"""The odd natural numbers, an operationally countable infinite set:
    enumeration ``1, 3, 5, ...`` with exact indexing and reverse lookup."""

    def __init__(self):
        Parent.__init__(self, category=Sets().Countable().Infinite())

    def __iter__(self):
        value = 1
        while True:
            yield value
            value += 2

    def __getitem__(self, n):
        assert n >= 0, f"enumeration indices are nonnegative; found {n}"
        return 2 * n + 1

    def index(self, element):
        assert element % 2 == 1 and element >= 1, f"{element} is not an odd natural"
        return (element - 1) // 2


def test_countable_parent_runs_its_executable_witness_suite():
    r"""The effective-witness contract in action: exhaustive duplicate-free
    prefix, index round trips on nontrivial members, and the uniform
    infinite-set consequences arriving through the Sage ``Infinite`` join —
    not from any local implementation."""
    odds = OddNaturals()

    prefix = []
    for value in odds:
        prefix.append(value)
        if len(prefix) == 10:
            break
    assert prefix == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert len(set(prefix)) == 10

    assert odds[odds.index(7)] == 7
    assert odds[odds.index(101)] == 101
    assert odds.index(odds[36]) == 36

    assert odds.is_countable()
    assert not odds.is_uncountable()
    assert not odds.is_finite()
    assert odds.cardinality() == oo


class ClaimedCountable(Parent):
    r"""A parent that opts into ``Countable`` without supplying the suite."""

    def __init__(self):
        Parent.__init__(self, category=Sets().Countable())


def test_countable_claim_without_the_suite_fails_at_the_abstract_boundary():
    r"""Opting in is trusted, but the executable obligations are forced:
    every suite operation is a Sage abstract method, so touching it on a
    parent that never implemented it fails loudly."""
    claimed = ClaimedCountable()
    with pytest.raises(NotImplementedError):
        iter(claimed)
    with pytest.raises(NotImplementedError):
        claimed.index(1)


class ContinuumStandIn(Parent):
    r"""A parent placed in ``Uncountable`` by trusted declaration: no
    enumeration data exists or is demanded."""

    def __init__(self):
        Parent.__init__(self, category=Sets().Uncountable())


def test_uncountable_trusted_placement_owns_the_uniform_consequences():
    r"""Trusted placement instantiates cleanly with no witness suite and the
    consequences are category facts: uncountable, not countable, infinite
    cardinality."""
    from sage_lattice_category_spike.objects.cardinals import aleph0, continuum

    stand_in = ContinuumStandIn()
    assert stand_in.is_uncountable()
    assert not stand_in.is_countable()
    assert not stand_in.is_finite()
    assert stand_in.cardinality() == continuum
    assert stand_in.cardinality() > aleph0
