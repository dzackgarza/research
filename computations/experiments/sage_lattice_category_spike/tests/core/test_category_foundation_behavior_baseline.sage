r"""Pre-migration behavior baseline for the maintained parents (issue #213).

Characterization freeze, committed BEFORE any leaf set-method is removed:
each row records a maintained parent's CURRENT public set-flavored
behavior — exact values, exact result types, returned elements' parents,
and representative object/nonidentity-morphism behavior — probed against
the running spike at authoring time (2026-07-16). During CP3's routing,
a local implementation may be deleted ONLY while every row here stays
green; a row that was wrong on main goes to the user as evidence, never
silently 'fixed' in either direction.

Lattices themselves currently answer NO generic set questions (no
cardinality, no countability) — the routing ADDS that capability, so no
absence is frozen here.
"""

from __future__ import annotations

from sage.rings.integer import Integer

from sage_lattice_category_spike.lattice_categories import Lattice
from sage_lattice_category_spike.objects.cardinals import Cardinal


def test_baseline_discriminant_group_of_a2():
    r"""Row: A2's discriminant group — order three, exactly the cyclic
    group ZZ/3 in behavior."""
    group = Lattice("A2").discriminant_group()

    order = group.order()
    assert order == 3
    assert isinstance(order, Integer)

    elements = list(group)
    assert len(elements) == 3
    assert len(set(elements)) == 3
    assert all(element.parent() is group for element in elements)

    nonzero = [element for element in elements if element != group.zero()]
    assert len(nonzero) == 2
    witness = nonzero[0]
    assert witness + witness != group.zero()
    assert witness + witness + witness == group.zero()


def test_baseline_discriminant_group_of_a1():
    r"""Row: A1's discriminant group — order two."""
    group = Lattice("A1").discriminant_group()
    assert group.order() == 2
    assert len(list(group)) == 2


def test_baseline_isometry_group_of_a2():
    r"""Row: O(A2) — order twelve, elements are lattice morphisms with the
    right boundaries, inverses compose to the identity."""
    a2 = Lattice("A2")
    group = a2.isometry_group()

    order = group.order()
    assert order == 12
    assert isinstance(order, Integer)

    elements = list(group)
    assert len(elements) == 12
    assert all(isometry.domain() == a2 and isometry.codomain() == a2 for isometry in elements)

    nonidentity = [isometry for isometry in elements if isometry != a2.identity_morphism()]
    assert len(nonidentity) == 11
    witness = nonidentity[0]
    assert witness * witness.inverse() == a2.identity_morphism()


def test_baseline_isometry_homset_of_a2():
    r"""Row: Isom(A2, A2) — cardinality twelve as a first-class homset."""
    a2 = Lattice("A2")
    homset = a2.Isom(a2)
    cardinality = homset.cardinality()
    assert cardinality == 12
    assert isinstance(cardinality, Integer)


def test_baseline_genus_of_a2():
    r"""Row: the A2 genus — a single isometry class, with cardinality
    agreeing with the class number and the representative genuinely
    isometric to A2."""
    a2 = Lattice("A2")
    genus = a2.genus()

    cardinality = genus.cardinality()
    assert cardinality == 1
    # Row DELIBERATELY updated during CP3 routing (was Integer): the
    # ratified owned-cardinal contract makes every cardinality() in the
    # owned graph a Cardinal; the classical Integer spelling remains as
    # class_number(). Not a silent fix — see the routing commit.
    assert isinstance(cardinality, Cardinal)
    assert genus.class_number() == 1
    assert isinstance(genus.class_number(), Integer)

    representatives = genus.representatives()
    assert len(representatives) == 1
    assert representatives[0].is_isometric(a2)
