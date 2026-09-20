import pytest

from dzack_research.preamble.all import GF, QQ, AffineSpaces, Modules
from dzack_research.preamble.categories.abstract_categories.presheaves import DescentDataOnCover
from dzack_research.preamble.categories.group.magmas import AdditiveGroups
from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAtlasModuleGluingData,
    FiniteAtlasModuleTransition,
)
from dzack_research.preamble.categories.modules.fibered_modules import (
    ModulesOverCommutativeRings,
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
    left = AffineSpaces(QQ)(1, names=("x",))
    right = AffineSpaces(QQ)(1, names=("y",))
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
    transition = Schemes(QQ).Core().Mor(left_overlap, right_overlap)(forward, reverse)
    return left, right, transition


def _punctured_line(name):
    chart = AffineSpaces(QQ)(1, names=(name,))
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
    return Schemes(QQ).Core().Mor(source_overlap, target_overlap)(forward, reverse)


def test_varying_ring_module_fibre_and_two_nonidentity_semilinear_maps_compose() -> None:
    field = GF(5)
    ring = field.polynomial_ring("x")
    x = ring.algebra_generator("x")
    first_scalar = ring.Mor(ring)({"x": -x})
    second_scalar = ring.Mor(ring)({"x": x + ring.one()})
    source = ring.free_module(finite_ordered_set(("source",)))
    middle = ring.free_module(finite_ordered_set(("middle",)))
    target = ring.free_module(finite_ordered_set(("target",)))
    fibered = ModulesOverCommutativeRings()

    assert fibered.fiber(ring) is Modules(ring)
    assert fibered.cocartesian_transport(first_scalar).ring_map() is first_scalar
    assert fibered.cartesian_transport(first_scalar).ring_map() is first_scalar

    first = fibered.Mor(source, middle)(
        first_scalar,
        {"source": middle.module_generator("middle")},
    )
    second = fibered.Mor(middle, target)(
        second_scalar,
        {"middle": target.module_generator("target")},
    )
    composite = second * first
    composite_scalar = second_scalar * first_scalar
    generator = source.module_generator("source")

    assert composite.scalar_map() == composite_scalar
    assert first.additive_map()(generator) == middle.module_generator("middle")
    assert first.linearization().domain() is first.extended_source()
    assert first.linearization().codomain() is middle
    assert composite(generator) == target.module_generator("target")
    assert composite(source.scalar_multiple(x, generator)) == target.scalar_multiple(
        composite_scalar(x),
        composite(generator),
    )


def test_varying_ring_module_rejects_additive_map_incompatible_with_scalar_map() -> None:
    field = GF(3)
    ring = field.polynomial_ring("x")
    x = ring.algebra_generator("x")
    scalar_map = ring.Mor(ring)({"x": -x})
    module = ring.free_module(finite_ordered_set(("e",)))
    additive = AdditiveGroups().AdditiveCommutative().HomCategory().Of(
        module,
        module,
    ).elementwise(lambda element: element)

    with pytest.raises(ValueError, match="not scalar-linear"):
        ModulesOverCommutativeRings().Mor(module, module)(scalar_map, additive)


def test_semilinear_module_transition_keeps_distinct_overlap_rings() -> None:
    left, right, scheme_transition = _distinct_punctured_lines()
    glued = Schemes(QQ).glue_affine_charts(left, right, scheme_transition)
    datum = glued.gluing_datum()
    left_overlap = datum.left_overlap()
    right_overlap = datum.right_overlap()
    assert left_overlap.coordinate_algebra() is not right_overlap.coordinate_algebra()

    source = left_overlap.coordinate_algebra().free_module(1)
    target = right_overlap.coordinate_algebra().free_module(1)
    source_label = next(iter(source.module_generating_set()))
    target_label = next(iter(target.module_generating_set()))
    forward_scalar = scheme_transition.forward().coordinate_algebra_morphism()
    reverse_scalar = scheme_transition.inverse().coordinate_algebra_morphism()
    fibered_modules = ModulesOverCommutativeRings()
    pullback = fibered_modules.Mor(target, source)(
        forward_scalar,
        {target_label: source.module_generator(source_label)},
    )
    inverse_pullback = fibered_modules.Mor(source, target)(
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
    assert target in fibered_modules and source in fibered_modules
    assert transition.pullback() in fibered_modules.Mor(target, source)
    assert fibered_modules.projection()(transition.pullback()) is forward_scalar
    assert fibered_modules.projection()(target) is target.base_ring()
    left_identity = transition.pullback() * transition.inverse_pullback()
    assert fibered_modules.projection()(left_identity) == forward_scalar * reverse_scalar
    assert left_identity == SemilinearModuleMorphism.identity(source)
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
    datum = glued.finite_affine_atlas()
    local_modules = {
        label: datum.chart(label).coordinate_algebra().free_module(1)
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

    descent = FiniteAtlasModuleGluingData(datum)(
        local_modules,
        module_transitions,
    )
    assert descent in FiniteAtlasModuleGluingData(datum)
    assert descent in DescentDataOnCover(datum.coverage(), datum)

    left_middle = descent.transition_on_triple("left", "middle", "right")
    middle_right = descent.transition_on_triple("middle", "right", "left")
    left_right = descent.transition_on_triple("left", "right", "middle")
    assert left_middle.pullback() * middle_right.pullback() == left_right.pullback()
    assert (
        descent.pair_module("left", "middle").base_ring()
        is not descent.pair_module("middle", "left").base_ring()
    )

    construction = descent.compatible_sections_construction()
    shape = construction.diagram().domain()
    assert construction.object() is descent.compatible_sections()
    assert construction.diagram()(shape.source()) is descent.local_section_product_construction().object()
    assert (
        construction.diagram()(shape.target())
        is descent.matching_section_product_construction().object()
    )
    components = {
        label: local_modules[label].module_generator(
            next(iter(local_modules[label].module_generating_set()))
        )
        for label in labels
    }
    section = descent.compatible_section(components)
    for label in labels:
        assert descent.compatible_section_component(section, label) == components[label]


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
    datum = Schemes(QQ).glue_affine_atlas(charts, scheme_transitions).finite_affine_atlas()
    local_modules = {
        label: datum.chart(label).coordinate_algebra().free_module(1)
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
    source = FiniteAtlasModuleGluingData(datum)(local_modules, transition_data)
    target = FiniteAtlasModuleGluingData(datum)(local_modules, transition_data)
    local_maps = {}
    for label in labels:
        module = local_modules[label]
        generator = next(iter(module.module_generating_set()))
        local_maps[label] = module.module_category().Mor(module, module)(
            {generator: module.scalar_multiple(2, module.module_generator(generator))}
        )

    morphism = source.morphism_to(target, local_maps)

    assert morphism in FiniteAtlasModuleGluingData(datum).Mor(source, target)
    for label in labels:
        module = local_modules[label]
        generator = next(iter(module.module_generating_set()))
        assert morphism.local_map(label)(module.module_generator(generator)) == module.scalar_multiple(
            2, module.module_generator(generator)
        )
