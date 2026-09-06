from __future__ import annotations

from itertools import combinations


def _three_chart_cover():
    r"""``A^1_Q`` covered by ``D(x)``, ``D(1-x)`` and ``D(2-x)``."""
    from dzack_research.preamble.all import QQ, PolynomialRing, Spec

    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(
        x,
        algebra.one() - x,
        algebra(2) - x,
    )
    return algebra, x, scheme, cover


def _rank_one_generator(module):
    return module.module_generator(next(iter(module.module_generating_set())))


def _rank_one_transition(source, target, unit):
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    source_generator = _rank_one_generator(source)
    target_generator = _rank_one_generator(target)
    forward = module_homset(source, target)(
        lambda _label: target.scalar_multiple(unit, target_generator)
    )
    inverse = module_homset(target, source)(
        lambda _label: source.scalar_multiple(unit.inverse_of_unit(), source_generator)
    )
    return Isomorphism(forward, inverse)


def test_a_cover_addresses_its_charts_by_the_labels_of_its_atlas() -> None:
    r"""The atlas indexes the charts, so a chart is asked for by its label."""
    algebra, x, _scheme, cover = _three_chart_cover()
    atlas = cover.atlas()

    assert int(atlas.cardinality().finite_value()) == 3
    for label in atlas:
        assert cover.open(label).distinguished_open_element() == (
            cover.defining_element(label)
        )
    assert cover.defining_element(0) == x
    assert cover.defining_element(1) == algebra.one() - x
    assert cover.open(2).distinguished_open_element() == algebra(2) - x


def test_an_intersection_is_taken_of_a_set_of_labels_not_a_sequence() -> None:
    r"""``U_i cap U_j`` does not depend on the order the two charts are named.

    The intersection is indexed by the set of charts, so naming a chart twice
    or naming the pair in the other order selects the same open, and its
    defining element is the product over that set.
    """
    _algebra, _x, _scheme, cover = _three_chart_cover()

    overlap = cover.intersection(0, 1)
    assert cover.intersection(1, 0) is overlap
    assert cover.intersection(0, 1, 0) is overlap
    assert cover.overlap(0, 1) is overlap
    assert overlap.distinguished_open_element() == (
        cover.defining_element(0) * cover.defining_element(1)
    )
    assert cover.intersection(0) is cover.open(0)

    triple = cover.intersection(0, 1, 2)
    assert triple is cover.intersection(2, 1, 0)
    assert triple.distinguished_open_element() == (
        cover.defining_element(0)
        * cover.defining_element(1)
        * cover.defining_element(2)
    )


def test_descent_data_is_keyed_by_pairs_of_atlas_labels() -> None:
    r"""Transitions handed in as label pairs are the transitions the datum holds.

    The datum below is assembled by ranging over the atlas, with no count of
    the charts and no position anywhere, and it answers for the same pairs it
    was given, in both directions.
    """
    from dzack_research.preamble.all import FreeModule

    _algebra, _x, _scheme, cover = _three_chart_cover()
    atlas = cover.atlas()

    local_modules = {
        label: FreeModule(cover.open(label).coordinate_algebra(), 1) for label in atlas
    }
    transitions = {}
    for left, right in combinations(atlas, 2):
        source = cover.restrict_module(local_modules[left], left, right)
        target = cover.restrict_module(local_modules[right], right, left)
        transitions[left, right] = _rank_one_transition(
            source,
            target,
            source.base_ring().one(),
        )

    datum = cover.glue_modules(
        tuple(local_modules[label] for label in atlas),
        transitions,
    )

    for left, right in combinations(atlas, 2):
        assert datum.transition(left, right) is transitions[left, right]
        assert datum.transition(right, left).forward() is (
            transitions[left, right].inverse()
        )
    for label in atlas:
        assert datum.local_module(label) is local_modules[label]
