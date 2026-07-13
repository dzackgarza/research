r"""Tier-1 literature fixtures for small dual-graph stratifications.

These tests recover published stratification facts with precise citations.
Stronger whole-poset oracles live in sibling literature modules.

References: Harris-Morrison *Moduli of Curves* Ch. 2–3; Arbarello-Cornalba
Ch. XII; Chan Fig. 3 (`\overline{\mathcal M}_{2,0}`).
"""

from __future__ import annotations

import pytest

from dm_moduli_spike import DMCompactificationModel, ModuliFactor
from tests.support.fixtures import CHAN_M20_COVERS, m20_types


def test_M04_stratification_has_one_open_and_three_codim_one_boundary_strata():
    r"""Stratification fact for `\overline{\mathcal M}_{0,4}`.

    Recovers: dimension one; one smooth stratum; three codimension-one boundary
    strata with source factors `\overline{\mathcal M}_{0,3}\times\overline{\mathcal M}_{0,3}`
    and trivial graph automorphism group.  This is strictly weaker than the
    compatible-split whole-poset oracle in ``test_lit_M0n_poset_oracle.sage``.

    Reference: Harris-Morrison, *Moduli of Curves*, Ch. 2 (stable pointed curves).
    """
    model = DMCompactificationModel(0, 4)
    assert model.dimension() == 1
    stratification = model.stratification()
    assert len(stratification.strata(codim=0)) == 1
    boundary = stratification.strata(codim=1)
    assert len(boundary) == 3
    for stratum in boundary:
        presentation = stratum.open_stack_presentation()
        clutching = stratum.clutching_morphism()
        assert presentation.product() == tuple(
            ModuliFactor(0, 3, flags=clutching.flags_at(vertex))
            for vertex in range(len(clutching.source_factors()))
        )
        assert presentation.group_order() == 1


def test_M11_nodal_boundary_has_published_combinatorics_and_branch_swap():
    r"""Complete published description of the unique `\overline{\mathcal M}_{1,1}` boundary stratum.

    Recovers: one genus-zero vertex; one loop; one marking; clutching source
    `\overline{\mathcal M}_{0,3}`; the marking leg fixed; the two loop half-edges
    exchanged by `\operatorname{Aut}(\Gamma)`.

    Reference: Harris-Morrison, *Moduli of Curves*, Ch. 3; Arbarello-Cornalba,
    *Geometry of Algebraic Curves II*, Ch. XII (irreducible node).
    """
    model = DMCompactificationModel(1, 1)
    boundary = model.stratification().strata(codim=1)
    assert len(boundary) == 1
    nodal = boundary[0]
    record = nodal.curve_type().canonical_representative()
    assert record.num_vertices() == 1
    assert record.vertex_genera == (0,)
    assert record.num_edges() == 1
    assert record.num_markings() == 1
    clutching = nodal.clutching_morphism()
    assert clutching.source_factors() == (ModuliFactor(0, 3, compact=True),)
    action = nodal.curve_type().automorphism_action()
    loop_flags = [
        flag
        for flag in range(record.num_flags())
        if record.flag_vertex[flag] == 0 and record.flag_involution[flag] != flag
    ]
    assert len(loop_flags) == 2
    flag_perm = action.on_flags()[0]
    assert flag_perm[record.marking_to_flag[0]] == record.marking_to_flag[0]
    assert {flag_perm[loop_flags[0]], flag_perm[loop_flags[1]]} == set(loop_flags)
    assert flag_perm[loop_flags[0]] != loop_flags[0]


@pytest.mark.ci
def test_M20_has_seven_chan_types_and_published_hasse_incidence():
    r"""Chan's seven genus-two combinatorial types and their contraction incidences.

    Primary evidence is the correspondence between each published graph and its
    exact contraction incidences.  Rank vectors alone are tier-5 diagnostics.

    Reference: Chan, Figure 3; Arbarello-Cornalba, Ch. XII (edge contraction).
    """
    stratification = DMCompactificationModel(2, 0).stratification()
    types = m20_types(stratification)
    assert set(types) == set(CHAN_M20_COVERS) | {"I", "II", "III", "IV", "V", "VI", "VII"}
    poset = stratification.specialization_poset()
    actual_covers = {
        (child.curve_type().canonical_key(), parent.curve_type().canonical_key())
        for parent, child in poset.cover_relations()
    }
    expected_covers = {
        (types[child].curve_type().canonical_key(), types[parent].curve_type().canonical_key())
        for parent, children in CHAN_M20_COVERS.items()
        for child in children
    }
    assert actual_covers == expected_covers
