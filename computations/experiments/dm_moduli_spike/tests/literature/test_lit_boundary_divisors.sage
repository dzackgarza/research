r"""Tier-1 literature oracle: Arborello-Cornalba boundary divisors and clutching.

* Arbarello-Cornalba, *Geometry of Algebraic Curves II*, Ch. XII (boundary
  strata, irreducible and separating nodes, clutching maps).
"""

from __future__ import annotations

import pytest

from dm_moduli_spike import DMCompactificationModel
from tests.support.fixtures import (
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
    model = DMCompactificationModel(g, n)
    boundary = model.stratification().strata(codim=1)
    actual = {boundary_label(stratum.curve_type(), g, n) for stratum in boundary}
    expected = expected_boundary_labels(g, n)
    assert actual == expected


@pytest.mark.parametrize("g,n", stable_pairs())
def test_irreducible_boundary_clutching_source_matches_AC(g, n):
    if g < 1:
        return
    model = DMCompactificationModel(g, n)
    irr = next(
        stratum
        for stratum in model.stratification().strata(codim=1)
        if boundary_label(stratum.curve_type(), g, n) == ("irr",)
    )
    assert clutching_signature(irr) == expected_clutching_signature_irr(g, n)


@pytest.mark.parametrize("g,n", stable_pairs())
def test_separating_boundary_clutching_sources_match_AC(g, n):
    model = DMCompactificationModel(g, n)
    for stratum in model.stratification().strata(codim=1):
        label = boundary_label(stratum.curve_type(), g, n)
        if label[0] != "sep":
            continue
        _, a, marking_set = label
        assert clutching_signature(stratum) == expected_clutching_signature_sep(g, n, a, marking_set)
