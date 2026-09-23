r"""Young composition has a proper pair domain, not a monoid law on the interval."""

import pytest
from sage.rings.infinity import Infinity
from dzack_research.preamble.all import QQ, UnitInterval, GradedModules
from dzack_research.preamble.categories.group.magmas import Monoids


def test_unit_interval_exposes_the_actual_young_pair_map() -> None:
    half, one, zero = UnitInterval(QQ(1) / 2), UnitInterval.one(), UnitInterval.zero()
    pair = lambda s, t: UnitInterval.degree_pairs()(lambda i: s if int(i) == 0 else t)
    product = UnitInterval.young_degree_map()
    assert UnitInterval not in Monoids()
    assert QQ(1) / 2 in UnitInterval
    assert QQ(1) in UnitInterval and QQ(0) in UnitInterval
    assert QQ(2) not in UnitInterval and Infinity not in UnitInterval
    assert product.domain() is UnitInterval.young_pairs()
    assert product.codomain() is UnitInterval
    assert product(pair(one, one)) == one
    assert product(pair(one, half)) == half
    assert product(pair(half, half)) == zero
    assert product(pair(zero, one)) == zero
    assert pair(zero, zero) not in product.domain()
    with pytest.raises(ValueError):
        product(pair(zero, zero))
    assert GradedModules(QQ, UnitInterval).grading_index_set() is UnitInterval
    with pytest.raises(TypeError, match="monoid"):
        GradedModules(QQ, UnitInterval).grading_monoid()
