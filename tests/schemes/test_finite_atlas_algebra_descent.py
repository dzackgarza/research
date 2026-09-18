r"""Algebra descent across affine atlases with genuinely distinct overlap rings."""

from dzack_research.preamble.all import QQ, AffineSpaces
from dzack_research.preamble.categories.abstract_categories.presheaves import DescentDataOnCover
from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAtlasAlgebraGluingData,
    SemilinearAlgebraMorphism,
)
from dzack_research.preamble.categories.schemes.schemes import Schemes
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)


def _punctured_line(name):
    chart = AffineSpaces(QQ)(1, names=(name,))
    coordinate = chart.coordinate_algebra().algebra_generator(name)
    return chart, coordinate


def _renaming_overlap_isomorphism(source, source_coordinate, target, target_coordinate):
    source_overlap = source.distinguished_open(source_coordinate)
    target_overlap = target.distinguished_open(target_coordinate)
    source_ring = source_overlap.coordinate_algebra()
    target_ring = target_overlap.coordinate_algebra()
    source_localization = source_ring.localization_map()
    target_localization = target_ring.localization_map()
    source_name = str(source_coordinate)
    target_name = str(target_coordinate)

    def pull_to_source(element):
        numerator, denominator = target_ring.localization_fraction_data(element)
        rename = target.coordinate_algebra().Mor(source.coordinate_algebra())(
            {target_name: source_coordinate}
        )
        return (
            source_localization(rename(numerator))
            * source_localization(rename(denominator)).inverse_of_unit()
        )

    def pull_to_target(element):
        numerator, denominator = source_ring.localization_fraction_data(element)
        rename = source.coordinate_algebra().Mor(target.coordinate_algebra())(
            {source_name: target_coordinate}
        )
        return (
            target_localization(rename(numerator))
            * target_localization(rename(denominator)).inverse_of_unit()
        )

    forward = source_overlap.Mor(target_overlap)(
        target_ring.Mor(source_ring)(pull_to_source)
    )
    reverse = target_overlap.Mor(source_overlap)(
        source_ring.Mor(target_ring)(pull_to_target)
    )
    return Schemes(QQ).Core().Mor(source_overlap, target_overlap)(forward, reverse)


def _three_chart_datum():
    left, x = _punctured_line("x")
    middle, y = _punctured_line("y")
    right, z = _punctured_line("z")
    labels = finite_ordered_set(("left", "middle", "right"))
    charts_by_label = {"left": left, "middle": middle, "right": right}
    charts = finite_indexed_family(
        labels,
        lambda label: charts_by_label[label],
        name="Three affine charts for algebra descent",
    )
    transitions = {
        ("left", "middle"): _renaming_overlap_isomorphism(left, x, middle, y),
        ("left", "right"): _renaming_overlap_isomorphism(left, x, right, z),
        ("middle", "right"): _renaming_overlap_isomorphism(middle, y, right, z),
    }
    datum = Schemes(QQ).glue_affine_atlas(charts, transitions).finite_affine_atlas()
    return labels, datum


def _rank_one_polynomial_algebras(labels, datum):
    return {
        label: datum.chart(label).coordinate_algebra().polynomial_ring("t")
        for label in labels
    }


def _identity_transition_data(_labels, datum, _local_algebras):
    transitions = {}
    for source_label, target_label in datum.transition_index_set():
        transitions[source_label, target_label] = (
            lambda label, _domain, codomain: codomain.algebra_generator(label),
            lambda label, _domain, codomain: codomain.algebra_generator(label),
        )
    return transitions


def test_pair_transition_is_an_actual_semilinear_algebra_isomorphism() -> None:
    labels, datum = _three_chart_datum()
    local_algebras = _rank_one_polynomial_algebras(labels, datum)
    descent = FiniteAtlasAlgebraGluingData(datum)(
        local_algebras,
        _identity_transition_data(labels, datum, local_algebras),
    )
    assert descent in FiniteAtlasAlgebraGluingData(datum)
    assert descent in DescentDataOnCover(datum.coverage(), datum)

    transition = descent.transition("left", "middle")
    pullback = transition.pullback()
    assert isinstance(pullback, SemilinearAlgebraMorphism)
    assert pullback.source().base_ring() is not pullback.target().base_ring()
    assert (
        pullback.scalar_map()
        == datum.transition_between("left", "middle").forward().coordinate_algebra_morphism()
    )
    generator = pullback.source().algebra_generator(
        next(iter(pullback.source().algebra_generating_set()))
    )
    assert pullback(generator * generator) == pullback(generator) * pullback(generator)
    assert pullback(pullback.source().one()) == pullback.target().one()
    assert pullback * transition.inverse_pullback() == SemilinearAlgebraMorphism.identity(
        transition.source_algebra()
    )


def test_three_chart_algebra_descent_uses_actual_triple_overlap_cocycle() -> None:
    labels, datum = _three_chart_datum()
    local_algebras = _rank_one_polynomial_algebras(labels, datum)
    descent = FiniteAtlasAlgebraGluingData(datum)(
        local_algebras,
        _identity_transition_data(labels, datum, local_algebras),
    )

    left_middle = descent.transition_on_triple("left", "middle", "right")
    middle_right = descent.transition_on_triple("middle", "right", "left")
    left_right = descent.transition_on_triple("left", "right", "middle")
    assert left_middle.pullback() * middle_right.pullback() == left_right.pullback()
    assert (
        descent.pair_algebra("left", "middle").base_ring()
        is not descent.pair_algebra("middle", "left").base_ring()
    )


def test_nonidentity_local_algebra_maps_glue_on_distinct_charts() -> None:
    labels, datum = _three_chart_datum()
    local_algebras = _rank_one_polynomial_algebras(labels, datum)
    transitions = _identity_transition_data(labels, datum, local_algebras)
    source = FiniteAtlasAlgebraGluingData(datum)(local_algebras, transitions)
    target = FiniteAtlasAlgebraGluingData(datum)(local_algebras, transitions)
    local_maps = {}
    for label in labels:
        algebra = local_algebras[label]
        generator_label = next(iter(algebra.algebra_generating_set()))
        generator = algebra.algebra_generator(generator_label)
        local_maps[label] = algebra.Mor(algebra)({generator_label: generator * generator})

    morphism = source.morphism_to(target, local_maps)
    assert morphism in FiniteAtlasAlgebraGluingData(datum).Mor(source, target)
    for label in labels:
        algebra = local_algebras[label]
        generator_label = next(iter(algebra.algebra_generating_set()))
        generator = algebra.algebra_generator(generator_label)
        assert morphism.local_map(label)(generator) == generator * generator
