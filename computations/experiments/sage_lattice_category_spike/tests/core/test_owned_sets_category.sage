r"""Owned finite-set routes for current spike parents.

The countable/finite Sets foundation is a shared category boundary. A genus
and a discriminant form use its finite tier. Both routes retain Sage's generic
iterator and finite-set behavior while exposing the spike-owned root to later
parents.
"""

from __future__ import annotations

from sage_lattice_category_spike import Lattice, Sets


def test_discriminant_form_uses_the_owned_finite_sets_route():
    r"""The discriminant form of A2 is a finite object of the owned root.

    Its order is three, independently fixed by the determinant of the A2
    Gram matrix, so this checks both the shared category route and retained
    finite-set cardinality behavior on a real current parent.
    """
    discriminant_form = Lattice("A2").discriminant_group()

    assert discriminant_form in Sets().Finite(), (
        "a discriminant form must route through the owned finite Sets category"
    )
    assert discriminant_form.cardinality() == 3


def test_finite_sets_refine_the_owned_countable_sets_category():
    r"""Finite A2 genus data carries a countability witness.

    Finite sets refine it because their iteration terminates and can therefore
    be materialized.
    """
    genus = Lattice("A2").genus()
    countable_sets = Sets().Countable()

    assert Sets().Finite().is_subcategory(countable_sets)
    assert genus in countable_sets
    assert genus.list() == list(genus)


def test_countability_witness_has_the_python_indexing_interface():
    r"""Indexing and reverse lookup expose the chosen enumeration.

    The A2 genus has one isometry class, so its zeroth element and its first
    bounded slice must select that canonical class, and ``index`` must invert
    that selection. Sage's ``unrank`` and ``rank`` may implement these Python
    operations but create no owned mathematical operations.
    """
    a2 = Lattice("A2")
    genus = a2.genus()
    representative = genus[0]

    assert representative.is_isometric(a2)
    assert genus[:1] == [representative]
    assert genus.index(representative) == 0
    assert genus[genus.index(representative)].is_isometric(representative)


def test_countable_index_does_not_collide_with_mathematical_rank():
    r"""Reverse lookup is independent of another operation named ``rank``.

    The sourced A2 discriminant form reports its source lattice's rank two but
    has three elements in its chosen enumeration. ``index`` must invert that
    enumeration rather than dispatching to the unrelated mathematical
    ``rank()`` operation.
    """
    discriminant_form = Lattice("A2").discriminant_group()

    assert discriminant_form.rank() == 2
    assert [discriminant_form.index(element) for element in discriminant_form] == [0, 1, 2]
