"""Archive reconciliation for algebra functors around the free/forgetful adjunction.

The archived ``free_forgetful_adjunction.sage`` grouped tensor, symmetric,
alternating and divided-power algebra functors together, and described the
alternating construction as one of the free-algebra adjoints.  The live split is
mathematical: tensor and symmetric algebra are the represented left adjoints;
alternating and divided-power algebra remain functorial constructions but do not
acquire that ordinary forgetful adjunction.
"""

import pytest

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.sets import finite_ordered_set


def _rank_one(label):
    return ZZ.free_module(finite_ordered_set((label,)))


def test_archive_free_algebra_claim_is_retained_only_for_tensor_and_symmetric() -> None:
    source = _rank_one("x")

    tensor = source.module_category().tensor_algebra_adjunction()
    symmetric = source.module_category().symmetric_algebra_adjunction()
    assert tensor.unit(source).domain() is source
    assert symmetric.unit(source).domain() is source

    modules = source.module_category()
    alternating = modules.exterior_algebra()
    divided = modules.divided_power_algebra()
    with pytest.raises(AttributeError):
        alternating.unit(source)
    with pytest.raises(AttributeError):
        divided.unit(source)


def test_alternating_and_divided_power_functors_still_carry_nonidentity_maps() -> None:
    source = _rank_one("x")
    target = _rank_one("y")
    linear = source.module_category().Mor(source, target)(
        {"x": 2 * target.module_generator("y")}
    )

    modules = source.module_category()
    for functor in (modules.exterior_algebra(), modules.divided_power_algebra()):
        carried = functor(linear)
        source_algebra = functor(source)
        target_algebra = functor(target)
        x = source_algebra.degree_one_generator("x")
        y = target_algebra.degree_one_generator("y")

        assert carried.domain() is source_algebra
        assert carried.codomain() is target_algebra
        assert carried(x) == 2 * y
