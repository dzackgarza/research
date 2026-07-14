r"""Tier-1 literature oracle: Arbarello-Cornalba boundary divisors and clutching.

* Arbarello-Cornalba, *Geometry of Algebraic Curves II* (2011), Ch. XII
  (Thm. XII.2.2 boundary strata; Prop. XII.2.3 clutching maps for
  irreducible and separating nodes).
"""

from __future__ import annotations

import pytest

from dm_moduli_spike.objects.model import _enumerate_stable_graph_levels

from dm_moduli_spike.testing_support.support.fixtures import (
    boundary_label,
    clutching_signature,
    expected_boundary_labels,
    expected_clutching_signature_irr,
    expected_clutching_signature_sep,
    stable_pairs,
)

pytestmark = pytest.mark.ci


@pytest.mark.parametrize("g,n", stable_pairs())
def test_codimension_one_boundary_labels_match_AC(g, n):
    r"""AC Ch. XII Thm. XII.2.2: codimension-one boundary type labels."""
    boundary = _enumerate_stable_graph_levels(g, n).strata(codim=1)
    actual = {boundary_label(stratum, g, n) for stratum in boundary}
    expected = expected_boundary_labels(g, n)
    assert actual == expected


@pytest.mark.parametrize("g,n", stable_pairs())
def test_irreducible_boundary_clutching_source_matches_AC(g, n):
    r"""AC Ch. XII Prop. XII.2.3: irreducible node clutching source `M_{g-1,n+2}`."""
    if g < 1:
        return
    irr = next(
        stratum
        for stratum in _enumerate_stable_graph_levels(g, n).strata(codim=1)
        if boundary_label(stratum, g, n) == ("irr",)
    )
    assert clutching_signature(irr) == expected_clutching_signature_irr(g, n)


@pytest.mark.parametrize("g,n", stable_pairs())
def test_separating_boundary_clutching_sources_match_AC(g, n):
    r"""AC Ch. XII Prop. XII.2.3: separating node clutching product factors."""
    for stratum in _enumerate_stable_graph_levels(g, n).strata(codim=1):
        label = boundary_label(stratum, g, n)
        if label[0] != "sep":
            continue
        _, a, marking_set = label
        assert clutching_signature(stratum) == expected_clutching_signature_sep(g, n, a, marking_set)
