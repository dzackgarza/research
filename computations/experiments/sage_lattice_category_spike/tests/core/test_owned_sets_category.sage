r"""Owned finite-set routes for current spike parents.

The finite/enumerated Sets foundation is a shared category boundary. A genus
uses its finite enumerated tier, while a discriminant form is a finite
abelian group and must use its finite tier. Both routes retain Sage's generic
finite-set behavior while exposing the spike-owned root to later parents.
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
