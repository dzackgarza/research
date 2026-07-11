r"""Literature fixtures for the dual-graph stratification of Mbar(g, n).

References:

* Harris-Morrison, *Moduli of Curves* (GTM 187), Ch. 2-3 (stable curves, the
  boundary, and dual graphs).
* Arbarello-Cornalba-Griffiths, *Geometry of Algebraic Curves II*, Ch. XII
  (the boundary strata and clutching maps).
* Deligne-Mumford, *The irreducibility of the space of curves of given genus*,
  Publ. IHES 36 (1969).

These are structural facts about small moduli spaces that any correct model of
the dual-graph stratification must reproduce.
"""

from __future__ import annotations

from dm_moduli_spike import DMCompactificationModel, ModuliFactor


def test_m04_is_a_line_with_three_boundary_points():
    # Mbar(0,4) = P^1, with exactly three boundary points 12|34, 13|24, 14|23.
    model = DMCompactificationModel(0, 4)
    assert model.dimension() == 1
    stratification = model.stratification()
    assert stratification.rank_sizes() == (1, 3)
    boundary = stratification.strata(codim=1)
    assert len(boundary) == 3
    # each boundary point glues two three-pointed lines with trivial automorphism
    for stratum in boundary:
        presentation = stratum.open_stack_presentation()
        assert presentation.product() == (ModuliFactor(0, 3), ModuliFactor(0, 3))
        assert presentation.group_order() == 1


def test_m11_boundary_is_the_nodal_cubic_with_a_z2_automorphism():
    # The single boundary point of Mbar(1,1) is the nodal cubic; its dual graph
    # (one genus-0 vertex, one loop, one marking) has automorphism number 2
    # (the loop branch swap), matching the 1/2 in the orbifold Euler number.
    model = DMCompactificationModel(1, 1)
    assert model.dimension() == 1
    boundary = model.stratification().strata(codim=1)
    assert len(boundary) == 1
    nodal = boundary[0]
    assert nodal.curve_type().total_genus() == 1
    assert nodal.curve_type().automorphism_number() == 2
    assert nodal.clutching_morphism().target() == ModuliFactor(1, 1, compact=True)


def test_mbar2_has_the_classical_stratum_counts():
    # Mbar(2) has dimension 3 and a graded stratification with 1, 2, 2, 2 strata
    # in codimensions 0..3 (the two deepest points are the two maximally
    # degenerate stable genus-2 curves: the theta and dumbbell graphs).
    model = DMCompactificationModel(2, 0)
    assert model.dimension() == 3
    stratification = model.stratification()
    assert stratification.rank_sizes() == (1, 2, 2, 2)
    deepest = stratification.strata(codim=3)
    assert len(deepest) == 2
    for stratum in deepest:
        assert stratum.dimension() == 0
        assert stratum.codimension() == 3
