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
