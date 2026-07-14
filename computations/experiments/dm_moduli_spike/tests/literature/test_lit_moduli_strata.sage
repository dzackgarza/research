r"""Tier-1 literature fixtures for small dual-graph stratifications.

These tests recover published stratification facts with precise citations.
Stronger whole-poset oracles live in sibling literature modules.

References: Harris-Morrison *Moduli of Curves* Ch. 2–3; Arbarello-Cornalba
Ch. XII; Chan Fig. 3 (`\overline{\mathcal M}_{2,0}`).
"""

from __future__ import annotations

import pytest
from sage.rings.integer_ring import ZZ

from dm_moduli_spike import Mbar_gn, QuotientStack, spec
from dm_moduli_spike.objects.gamma import StableGraphCategory
from dm_moduli_spike.testing_support.support.fixtures import CHAN_M20_COVERS, flag_generator_images, m20_types


def test_M04_stratification_has_one_open_and_three_codim_one_boundary_strata():
    r"""Stratification fact for `\overline{\mathcal M}_{0,4}`.

    Recovers: dimension one; one smooth stratum; three codimension-one boundary
    strata with clutching source `\overline{\mathcal M}_{0,3}\times\overline{\mathcal M}_{0,3}`
    and trivial graph automorphism group.  This is strictly weaker than the
    compatible-split whole-poset oracle in ``test_lit_M0n_poset_oracle.sage``.

    Reference: Harris-Morrison, *Moduli of Curves*, Ch. 2 (stable pointed curves).
    """
    XSbar = Mbar_gn(0, 4, base=spec(ZZ))
    assert XSbar.dimension() == 1
    Sigma = XSbar.stratification()
    smooth = [S for S in Sigma.strata() if S.index().num_edges() == 0]
    boundary = [S for S in Sigma.strata() if S.index().num_edges() == 1]
    assert len(smooth) == 1
    assert len(boundary) == 3
    for stratum in boundary:
        underlying = stratum.underlying_stack()
        assert isinstance(underlying, QuotientStack)
        assert int(underlying.group().order()) == 1
        factors = stratum.clutching_morphism().domain().factors()
        assert sorted((f.genus(), f.number_of_markings()) for f in factors) == [(0, 3), (0, 3)]


def test_M11_nodal_boundary_has_published_combinatorics_and_branch_swap():
    r"""Complete published description of the unique `\overline{\mathcal M}_{1,1}` boundary stratum.

    Recovers: one genus-zero vertex; one loop; one marking; clutching source
    `\overline{\mathcal M}_{0,3}`; the marking leg fixed; the two loop half-edges
    exchanged by `\operatorname{Aut}(\Gamma)`.

    Reference: Harris-Morrison, *Moduli of Curves*, Ch. 3; Arbarello-Cornalba,
    *Geometry of Algebraic Curves II*, Ch. XII (irreducible node).
    """
    XSbar = Mbar_gn(1, 1, base=spec(ZZ))
    boundary = [S for S in XSbar.stratification().strata() if S.index().num_edges() == 1]
    assert len(boundary) == 1
    nodal = boundary[0]
    record = nodal.index()._canonical_record()
    assert record.num_vertices() == 1
    assert record.vertex_genera == (0,)
    assert record.num_edges() == 1
    assert record.num_markings() == 1
    factors = nodal.clutching_morphism().domain().factors()
    assert [(f.genus(), f.number_of_markings()) for f in factors] == [(0, 3)]
    loop_flags = [
        flag
        for flag in range(record.num_flags())
        if record.flag_vertex[flag] == 0 and record.flag_involution[flag] != flag
    ]
    assert len(loop_flags) == 2
    flag_perm = flag_generator_images(record)[0]
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
    types = m20_types()
    assert set(types) == set(CHAN_M20_COVERS) | {"I", "II", "III", "IV", "V", "VI", "VII"}
    poset = StableGraphCategory(2, 0).specialization_poset()
    actual_covers = {
        (generic.canonical_key(), special.canonical_key())
        for generic, special in poset.cover_relations()
    }
    expected_covers = {
        (types[generic].canonical_key(), types[special].canonical_key())
        for generic, specials in CHAN_M20_COVERS.items()
        for special in specials
    }
    assert actual_covers == expected_covers
