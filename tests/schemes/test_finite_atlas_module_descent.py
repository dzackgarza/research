from dzack_research.preamble.all import QQ, AffineSpace
from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreeModule,
)

from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAtlasModuleGluingDatum,
    FiniteAtlasModuleGluingMorphism,
    FiniteAtlasModuleTransition,
    SemilinearModuleMorphism,
)
from dzack_research.preamble.categories.schemes.schemes import Schemes
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)


def _distinct_punctured_lines():
    left = AffineSpace(1, QQ, names=("x",))
    right = AffineSpace(1, QQ, names=("y",))
    x = left.coordinate_algebra().algebra_generator("x")
    y = right.coordinate_algebra().algebra_generator("y")
    left_overlap = left.distinguished_open(x)
    right_overlap = right.distinguished_open(y)
    left_ring = left_overlap.coordinate_algebra()
    right_ring = right_overlap.coordinate_algebra()
    left_localization = left_ring.localization_map()
    right_localization = right_ring.localization_map()

    def to_left(element):
        numerator, denominator = right_ring.localization_fraction_data(element)
        source = right.coordinate_algebra()
        pullback = source.Mor(left.coordinate_algebra())({"y": x})
        return (
            left_localization(pullback(numerator))
            * left_localization(pullback(denominator)).inverse_of_unit()
        )

    def to_right(element):
        numerator, denominator = left_ring.localization_fraction_data(element)
        source = left.coordinate_algebra()
        pullback = source.Mor(right.coordinate_algebra())({"x": y})
        return (
            right_localization(pullback(numerator))
            * right_localization(pullback(denominator)).inverse_of_unit()
        )

    forward = left_overlap.Mor(right_overlap)(
        right_ring.Mor(left_ring)(to_left)
    )
    reverse = right_overlap.Mor(left_overlap)(
        left_ring.Mor(right_ring)(to_right)
    )
    return left, right, Isomorphism(forward, reverse)


def _punctured_line(name):
    chart = AffineSpace(1, QQ, names=(name,))
    coordinate = chart.coordinate_algebra().algebra_generator(name)
    return chart, coordinate, chart.distinguished_open(coordinate)


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
    return Isomorphism(forward, reverse)


def test_semilinear_module_transition_keeps_distinct_overlap_rings() -> None:
    left, right, scheme_transition = _distinct_punctured_lines()
    glued = Schemes(QQ).glue_affine_charts(left, right, scheme_transition)
    datum = glued.gluing_datum()
    left_overlap = datum.left_overlap()
    right_overlap = datum.right_overlap()
    assert left_overlap.coordinate_algebra() is not right_overlap.coordinate_algebra()

    source = FreeModule(left_overlap.coordinate_algebra(), 1)
    target = FreeModule(right_overlap.coordinate_algebra(), 1)
    source_label = next(iter(source.module_generating_set()))
    target_label = next(iter(target.module_generating_set()))
    forward_scalar = scheme_transition.forward().coordinate_algebra_morphism()
    reverse_scalar = scheme_transition.inverse().coordinate_algebra_morphism()
    pullback = SemilinearModuleMorphism(
        target,
        source,
        forward_scalar,
        {target_label: source.module_generator(source_label)},
    )
    inverse_pullback = SemilinearModuleMorphism(
        source,
        target,
        reverse_scalar,
        {source_label: target.module_generator(target_label)},
    )
    transition = FiniteAtlasModuleTransition(
        scheme_transition,
        source,
        target,
        pullback,
        inverse_pullback,
    )

    assert transition.pullback().scalar_map().domain() is right_overlap.coordinate_algebra()
    assert transition.pullback().scalar_map().codomain() is left_overlap.coordinate_algebra()
    assert transition.pullback() * transition.inverse_pullback() == SemilinearModuleMorphism.identity(source)
    assert transition.inverse_pullback() * transition.pullback() == SemilinearModuleMorphism.identity(target)


def test_three_chart_module_descent_composes_after_overlap_transport() -> None:
    left, x, _left_overlap = _punctured_line("x")
    middle, y, _middle_overlap = _punctured_line("y")
    right, z, _right_overlap = _punctured_line("z")
    labels = finite_ordered_set(("left", "middle", "right"))
    charts_by_label = {"left": left, "middle": middle, "right": right}
    charts = finite_indexed_family(
        labels,
        lambda label: charts_by_label[label],
        name="Three distinct affine-line charts",
    )
    scheme_transitions = {
        ("left", "middle"): _renaming_overlap_isomorphism(left, x, middle, y),
        ("left", "right"): _renaming_overlap_isomorphism(left, x, right, z),
        ("middle", "right"): _renaming_overlap_isomorphism(middle, y, right, z),
    }
    glued = Schemes(QQ).glue_affine_atlas(charts, scheme_transitions)
    datum = glued.gluing_datum()
    local_modules = {
        label: FreeModule(datum.chart(label).coordinate_algebra(), 1)
        for label in labels
    }
    module_transitions = {}
    for source_label, target_label in datum.transition_index_set():
        source_generator = next(
            iter(local_modules[source_label].module_generating_set())
        )
        target_generator = next(
            iter(local_modules[target_label].module_generating_set())
        )
        module_transitions[source_label, target_label] = (
            {target_generator: {source_generator: 1}},
            {source_generator: {target_generator: 1}},
        )

    descent = FiniteAtlasModuleGluingDatum(
        datum,
        local_modules,
        module_transitions,
    )

    left_middle = descent.transition_on_triple("left", "middle", "right")
    middle_right = descent.transition_on_triple("middle", "right", "left")
    left_right = descent.transition_on_triple("left", "right", "middle")
    assert left_middle.pullback() * middle_right.pullback() == left_right.pullback()
    assert (
        descent.pair_module("left", "middle").base_ring()
        is not descent.pair_module("middle", "left").base_ring()
    )


def test_nonidentity_local_maps_glue_semilinearly_on_three_distinct_charts() -> None:
    left, x, _left_overlap = _punctured_line("x")
    middle, y, _middle_overlap = _punctured_line("y")
    right, z, _right_overlap = _punctured_line("z")
    labels = finite_ordered_set(("left", "middle", "right"))
    charts_by_label = {"left": left, "middle": middle, "right": right}
    charts = finite_indexed_family(
        labels,
        lambda label: charts_by_label[label],
        name="Three affine charts for a module morphism",
    )
    scheme_transitions = {
        ("left", "middle"): _renaming_overlap_isomorphism(left, x, middle, y),
        ("left", "right"): _renaming_overlap_isomorphism(left, x, right, z),
        ("middle", "right"): _renaming_overlap_isomorphism(middle, y, right, z),
    }
    datum = Schemes(QQ).glue_affine_atlas(charts, scheme_transitions).gluing_datum()
    local_modules = {
        label: FreeModule(datum.chart(label).coordinate_algebra(), 1)
        for label in labels
    }
    transition_data = {}
    for source_label, target_label in datum.transition_index_set():
        source_generator = next(iter(local_modules[source_label].module_generating_set()))
        target_generator = next(iter(local_modules[target_label].module_generating_set()))
        transition_data[source_label, target_label] = (
            {target_generator: {source_generator: 1}},
            {source_generator: {target_generator: 1}},
        )
    source = FiniteAtlasModuleGluingDatum(datum, local_modules, transition_data)
    target = FiniteAtlasModuleGluingDatum(datum, local_modules, transition_data)
    local_maps = {}
    for label in labels:
        module = local_modules[label]
        generator = next(iter(module.module_generating_set()))
        local_maps[label] = module.module_category().Mor(module, module)(
            {generator: module.scalar_multiple(2, module.module_generator(generator))}
        )

    morphism = source.morphism_to(target, local_maps)

    assert isinstance(morphism, FiniteAtlasModuleGluingMorphism)
    for label in labels:
        module = local_modules[label]
        generator = next(iter(module.module_generating_set()))
        assert morphism.local_map(label)(module.module_generator(generator)) == module.scalar_multiple(
            2, module.module_generator(generator)
        )
