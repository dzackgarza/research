r"""Induced subposets from arbitrary stable-type subsets."""

from __future__ import annotations

from dm_moduli_spike import DMCompactificationModel
from dm_moduli_spike.objects.stratification import build_stratification_from_types


def test_intermediate_deletion_adds_direct_cover():
    model = DMCompactificationModel(2, 1)
    full = model.stratification()
    smooth = model.curve_types().smooth()
    codim_two = full.curve_type_levels()[2][0]
    subset = build_stratification_from_types(
        model.curve_types(),
        (smooth, codim_two),
        induced_order=True,
    )
    assert subset.construction_mode() == "induced_subposet"
    assert len(subset.covers()) == 1
    generic, special = subset.covers()[0]
    assert generic.curve_type() == smooth
    assert special.curve_type() == codim_two
    poset = subset.specialization_poset()
    assert poset.is_lequal(generic, special)
    assert poset.cover_relations() == [[generic, special]]


def test_adjacent_rank_mode_skips_nonconsecutive_covers():
    model = DMCompactificationModel(2, 1)
    full = model.stratification()
    smooth = model.curve_types().smooth()
    codim_two = full.curve_type_levels()[2][0]
    subset = build_stratification_from_types(
        model.curve_types(),
        (smooth, codim_two),
        induced_order=False,
    )
    assert subset.construction_mode() == "enumerated"
    assert subset.covers() == ()
