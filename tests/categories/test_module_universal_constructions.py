import pytest

from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.abstract_categories.functors import DiscreteCategory
from dzack_research.preamble.categories.abstract_categories.products import (
    ColimitsOfCategory,
    DirectedSystem,
    FiniteSequenceDiagram,
    InverseSystem,
    LimitsOfCategory,
    PosetCategory,
)
from dzack_research.preamble.categories.functors.core import (
    Functor,
    IdentityFunctor,
    NaturalTransformation,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.sets import NN, Sets, finite_ordered_set
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def test_module_equalizer_is_the_apex_of_its_actual_universal_cone() -> None:
    plane = ZZ.free_module(finite_ordered_set(("x", "y")))
    line = ZZ.free_module(finite_ordered_set(("z",)))
    probe = ZZ.free_module(finite_ordered_set(("t",)))
    x, y = plane.module_generators()
    z = line.module_generator("z")
    t = probe.module_generator("t")

    left = plane.module_category().Mor(plane, line)({"x": z, "y": line.zero()})
    right = plane.module_category().Mor(plane, line)({"x": line.zero(), "y": z})
    selected = Modules(ZZ).equalizer_construction(left, right)
    assert Modules(ZZ).equalizer(left, right) is selected.object()

    diagram = selected.diagram()
    shape = diagram.domain()
    assert diagram(shape.left()) is left
    assert diagram(shape.right()) is right
    inclusion = selected.structure_morphism(shape.source())
    assert inclusion.codomain() is plane
    assert selected.structure_morphism(shape.target()) == left * inclusion
    assert left * inclusion == right * inclusion

    diagonal = probe.module_category().Mor(probe, plane)({"t": x + y})
    cone = (diagram).Cones().cone(
        probe,
        lambda index: diagonal if index is shape.source() else left * diagonal,
    )
    factor = selected.factor(cone).apex_map()
    assert factor.domain() is probe
    assert factor.codomain() is selected.object()
    assert inclusion * factor == diagonal
    assert inclusion(factor(t)) == x + y


def test_module_coequalizer_is_the_apex_of_its_actual_universal_cocone() -> None:
    source = ZZ.free_module(finite_ordered_set(("t",)))
    plane = ZZ.free_module(finite_ordered_set(("x", "y")))
    target = ZZ.free_module(finite_ordered_set(("z",)))
    source.module_generator("t")
    x, y = plane.module_generators()
    z = target.module_generator("z")

    left = source.module_category().Mor(source, plane)({"t": x})
    right = source.module_category().Mor(source, plane)({"t": y})
    selected = Modules(ZZ).coequalizer_construction(left, right)
    assert Modules(ZZ).coequalizer(left, right) is selected.object()

    diagram = selected.diagram()
    shape = diagram.domain()
    projection = selected.costructure_morphism(shape.target())
    assert projection.domain() is plane
    assert selected.costructure_morphism(shape.source()) == projection * left
    assert projection * left == projection * right

    summation = plane.module_category().Mor(plane, target)({"x": z, "y": z})
    cocone = (diagram).Cocones().cocone(
        target,
        lambda index: summation * left if index is shape.source() else summation,
    )
    factor = selected.factor(cocone).apex_map()
    assert factor.domain() is selected.object()
    assert factor.codomain() is target
    assert factor * projection == summation
    assert factor(projection(x)) == z
    assert factor(projection(y)) == z


def test_zero_and_times_two_separate_equalizer_from_coequalizer() -> None:
    line = ZZ.free_module(finite_ordered_set(("e",)))
    e = line.module_generator("e")
    zero = line.module_category().Mor(line, line)({"e": line.zero()})
    twice = line.module_category().Mor(line, line)({"e": 2 * e})

    equalizer = Modules(ZZ).equalizer(zero, twice)
    assert equalizer.module_rank() == 0

    coequalizer = Modules(ZZ).coequalizer(zero, twice)
    invariants = coequalizer.invariant_factors()
    assert invariants.cardinality() == 1
    assert invariants[0] == ZZ(2)


def test_nonidentity_natural_transformation_induces_maps_on_selected_constructions() -> None:
    plane = ZZ.free_module(finite_ordered_set(("x", "y")))
    line = ZZ.free_module(finite_ordered_set(("z",)))
    x, y = plane.module_generators()
    z = line.module_generator("z")
    left = plane.module_category().Mor(plane, line)({"x": z, "y": line.zero()})
    right = plane.module_category().Mor(plane, line)({"x": line.zero(), "y": z})

    equalizer = Modules(ZZ).equalizer_construction(left, right)
    diagram = equalizer.diagram()
    shape = diagram.domain()
    twice_plane = plane.module_category().Mor(plane, plane)({"x": 2 * x, "y": 2 * y})
    twice_line = line.module_category().Mor(line, line)({"z": 2 * z})
    transformation = NaturalTransformation(
        diagram,
        diagram,
        lambda index: twice_plane if index is shape.source() else twice_line,
    )
    induced_equalizer = equalizer.induced_map(transformation, equalizer)
    inclusion = equalizer.structure_morphism(shape.source())
    assert inclusion * induced_equalizer == twice_plane * inclusion

    coequalizer = Modules(ZZ).coequalizer_construction(left, right)
    induced_coequalizer = coequalizer.induced_map(transformation, coequalizer)
    projection = coequalizer.costructure_morphism(shape.target())
    assert induced_coequalizer * projection == projection * twice_line


def test_diagram_restriction_retains_the_indexing_functor_and_composes() -> None:
    line = ZZ.free_module(finite_ordered_set(("e",)))
    e = line.module_generator("e")
    zero = line.module_category().Mor(line, line)({"e": line.zero()})
    twice = line.module_category().Mor(line, line)({"e": 2 * e})
    diagram = Modules(ZZ).equalizer_construction(zero, twice).diagram()
    shape = diagram.domain()

    class CollapseToTarget(Functor):
        def __init__(self):
            super().__init__(shape, shape)

        def _apply_object(self, _obj):
            return shape.target()

        def _apply_morphism(self, _morphism):
            return shape.identity(shape.target())

    indexing = CollapseToTarget()
    restricted = diagram.restrict(indexing)
    assert restricted.original_diagram() is diagram
    assert restricted.indexing_functor() is indexing
    assert restricted(shape.source()) is line
    assert restricted(shape.target()) is line
    assert restricted(shape.left()) == line.module_category().Mor(line, line).identity()
    assert restricted(shape.right()) == line.module_category().Mor(line, line).identity()

    identity = IdentityFunctor(shape)
    twice_restricted = restricted.restrict(identity)
    assert twice_restricted.original_diagram() is restricted
    assert twice_restricted.indexing_functor() is identity
    assert twice_restricted(shape.left()) == restricted(shape.left())


def test_inverse_system_reverses_its_declared_index_category() -> None:
    labels = finite_ordered_set(("m", "n"))
    index = DiscreteCategory(labels)
    line = ZZ.free_module(finite_ordered_set(("e",)))
    systems = InverseSystem(index, line.category())

    assert systems.base_index_category() is index
    assert systems.index_category().base_category() is index
    assert systems.index_category() is not index


def test_module_product_and_coproduct_use_selected_universal_constructions() -> None:
    left = ZZ.free_module(finite_ordered_set(("x",)))
    right = ZZ.free_module(finite_ordered_set(("y",)))
    probe = ZZ.free_module(finite_ordered_set(("t",)))
    x = left.module_generator("x")
    y = right.module_generator("y")
    t = probe.module_generator("t")

    product = Modules(ZZ).product_construction((left, right))
    assert Modules(ZZ).product((left, right)) is product.object()
    product_shape = product.diagram().domain()
    to_left = probe.module_category().Mor(probe, left)({"t": 2 * x})
    to_right = probe.module_category().Mor(probe, right)({"t": 3 * y})
    cone = (product.diagram()).Cones().cone(
        probe,
        lambda index: to_left if int(index.value()) == 0 else to_right,
    )
    into_product = product.factor(cone).apex_map()
    assert product.structure_morphism(product_shape(0)) * into_product == to_left
    assert product.structure_morphism(product_shape(1)) * into_product == to_right

    coproduct = Modules(ZZ).coproduct_construction((left, right))
    assert Modules(ZZ).coproduct((left, right)) is coproduct.object()
    coproduct_shape = coproduct.diagram().domain()
    from_left = left.module_category().Mor(left, probe)({"x": 5 * t})
    from_right = right.module_category().Mor(right, probe)({"y": 7 * t})
    cocone = (coproduct.diagram()).Cocones().cocone(
        probe,
        lambda index: from_left if int(index.value()) == 0 else from_right,
    )
    from_coproduct = coproduct.factor(cocone).apex_map()
    assert from_coproduct * coproduct.costructure_morphism(coproduct_shape(0)) == from_left
    assert from_coproduct * coproduct.costructure_morphism(coproduct_shape(1)) == from_right


def test_empty_product_and_coproduct_distinguish_terminal_and_initial_sets() -> None:
    empty_index = finite_ordered_set(())
    empty_family = indexed_family(
        empty_index,
        lambda _index: finite_ordered_set(("unused",)),
        name="Empty family of sets",
    )

    product = Sets().product_construction(empty_family)
    coproduct = Sets().coproduct_construction(empty_family)

    assert product.object().cardinality() == cardinal(1)
    assert coproduct.object().cardinality() == cardinal(0)
    assert product.object() is not coproduct.object()

    probe = finite_ordered_set(("a", "b"))
    product_cone = (product.diagram()).Cones().cone(
        probe,
        lambda _index: None,
    )
    into_terminal = product.factor(product_cone).apex_map()
    assert into_terminal.domain() is probe
    assert into_terminal.codomain() is product.object()

    coproduct_cocone = (coproduct.diagram()).Cocones().cocone(
        probe,
        lambda _index: None,
    )
    from_initial = coproduct.factor(coproduct_cocone).apex_map()
    assert from_initial.domain() is coproduct.object()
    assert from_initial.codomain() is probe


def test_finite_sequence_limit_and_colimit_use_product_equalizer_reductions() -> None:
    line = ZZ.free_module(finite_ordered_set(("e",)))
    probe = ZZ.free_module(finite_ordered_set(("t",)))
    e = line.module_generator("e")
    t = probe.module_generator("t")
    twice = line.module_category().Mor(line, line)({"e": 2 * e})
    thrice = line.module_category().Mor(line, line)({"e": 3 * e})
    diagram = FiniteSequenceDiagram((line, line, line), (twice, thrice), line.category())

    limit = LimitsOfCategory(diagram.domain(), line.category()).construction(diagram)
    shape = diagram.domain()
    assert diagram(shape.Mor(shape(0), shape(2)).unique()) == thrice * twice
    assert twice * limit.structure_morphism(shape(0)) == limit.structure_morphism(shape(1))
    assert thrice * limit.structure_morphism(shape(1)) == limit.structure_morphism(shape(2))

    to_zero = probe.module_category().Mor(probe, line)({"t": e})
    to_one = twice * to_zero
    to_two = thrice * to_one
    cone = (diagram).Cones().cone(
        probe,
        lambda index: (to_zero, to_one, to_two)[index.position()],
    )
    into_limit = limit.factor(cone).apex_map()
    assert limit.structure_morphism(shape(0)) * into_limit == to_zero
    assert limit.structure_morphism(shape(2)) * into_limit == to_two

    colimit = ColimitsOfCategory(diagram.domain(), line.category()).construction(diagram)
    assert colimit.object() in line.category()
    assert colimit.object().module_rank() == 1
    from_zero = line.module_category().Mor(line, probe)({"e": 6 * t})
    from_one = line.module_category().Mor(line, probe)({"e": 3 * t})
    from_two = line.module_category().Mor(line, probe)({"e": t})
    assert colimit.costructure_morphism(shape(1)) * twice == colimit.costructure_morphism(shape(0))
    assert colimit.costructure_morphism(shape(2)) * thrice == colimit.costructure_morphism(shape(1))
    cocone = (diagram).Cocones().cocone(
        probe,
        lambda index: (from_zero, from_one, from_two)[index.position()],
    )
    from_colimit = colimit.factor(cocone).apex_map()
    assert from_colimit * colimit.costructure_morphism(shape(0)) == from_zero
    assert from_colimit * colimit.costructure_morphism(shape(2)) == from_two


def test_limit_functor_maps_nonidentity_stagewise_transformation_through_projections() -> None:
    line = ZZ.free_module(finite_ordered_set(("e",)))
    e = line.module_generator("e")

    source_twice = line.module_category().Mor(line, line)({"e": 2 * e})
    source_thrice = line.module_category().Mor(line, line)({"e": 3 * e})
    target_fourfold = line.module_category().Mor(line, line)({"e": 4 * e})
    target_ninefold = line.module_category().Mor(line, line)({"e": 9 * e})
    source = FiniteSequenceDiagram(
        (line, line, line),
        (source_twice, source_thrice),
        line.category(),
    )
    target = FiniteSequenceDiagram(
        (line, line, line),
        (target_fourfold, target_ninefold),
        line.category(),
    )
    shape = source.domain()
    stage_maps = (
        line.module_category().Mor(line, line)({"e": e}),
        line.module_category().Mor(line, line)({"e": 2 * e}),
        line.module_category().Mor(line, line)({"e": 6 * e}),
    )
    transformation = NaturalTransformation(
        source,
        target,
        lambda index: stage_maps[index.position()],
    )

    limits = LimitsOfCategory(shape, line.category())
    limit_functor = limits.defining_functor()
    diagrams = limit_functor.domain()
    source_object = diagrams(source)
    target_object = diagrams(target)
    transformation_morphism = diagrams.Mor(source_object, target_object)(transformation)

    source_limit = limits.construction(source)
    target_limit = limits.construction(target)
    induced = limit_functor.on_morphism(transformation_morphism)
    assert induced.domain() is source_limit.object()
    assert induced.codomain() is target_limit.object()

    for stage_index in range(3):
        stage = shape(stage_index)
        assert (
            target_limit.structure_morphism(stage) * induced
            == transformation.component(stage) * source_limit.structure_morphism(stage)
        )


def test_colimit_functor_maps_nonidentity_stagewise_transformation_on_representatives() -> None:
    line = ZZ.free_module(finite_ordered_set(("e",)))
    e = line.module_generator("e")

    source_twice = line.module_category().Mor(line, line)({"e": 2 * e})
    source_thrice = line.module_category().Mor(line, line)({"e": 3 * e})
    target_fourfold = line.module_category().Mor(line, line)({"e": 4 * e})
    target_ninefold = line.module_category().Mor(line, line)({"e": 9 * e})
    source = FiniteSequenceDiagram(
        (line, line, line),
        (source_twice, source_thrice),
        line.category(),
    )
    target = FiniteSequenceDiagram(
        (line, line, line),
        (target_fourfold, target_ninefold),
        line.category(),
    )
    shape = source.domain()
    assert target.domain() is shape

    stage_maps = (
        line.module_category().Mor(line, line)({"e": e}),
        line.module_category().Mor(line, line)({"e": 2 * e}),
        line.module_category().Mor(line, line)({"e": 6 * e}),
    )
    transformation = NaturalTransformation(
        source,
        target,
        lambda index: stage_maps[index.position()],
    )
    assert stage_maps[1] * source_twice == target_fourfold * stage_maps[0]
    assert stage_maps[2] * source_thrice == target_ninefold * stage_maps[1]

    colimits = ColimitsOfCategory(shape, line.category())
    colimit_functor = colimits.defining_functor()
    diagrams = colimit_functor.domain()
    source_object = diagrams(source)
    target_object = diagrams(target)
    transformation_morphism = diagrams.Mor(source_object, target_object)(transformation)

    source_colimit = colimits.construction(source)
    target_colimit = colimits.construction(target)
    induced = colimit_functor.on_morphism(transformation_morphism)
    assert induced.domain() is source_colimit.object()
    assert induced.codomain() is target_colimit.object()

    for stage_index in range(3):
        stage = shape(stage_index)
        source_leg = source_colimit.costructure_morphism(stage)
        target_leg = target_colimit.costructure_morphism(stage)
        assert induced * source_leg == target_leg * transformation.component(stage)
        representative = source_leg(e)
        expected = target_leg(stage_maps[stage_index](e))
        assert induced(representative) == expected


def test_directed_system_on_N_squared_retains_incomparable_indices_and_finite_rectangles() -> None:
    grid = Sets().product((NN, NN))
    index = PosetCategory(
        grid,
        le=lambda left, right: left[0] <= right[0] and left[1] <= right[1],
    )
    line = ZZ.free_module(finite_ordered_set(("e",)))
    e = line.module_generator("e")

    class GridSystem(Functor):
        def __init__(self):
            super().__init__(index, line.category())

        def _apply_object(self, _obj):
            return line

        def _apply_morphism(self, morphism):
            source = morphism.domain().value()
            target = morphism.codomain().value()
            exponent = (
                int(target[0]) - int(source[0])
                + int(target[1]) - int(source[1])
            )
            return line.module_category().Mor(line, line)({"e": (2**exponent) * e})

    system = GridSystem()
    systems = DirectedSystem(index, line.category())
    assert systems(system) in systems
    northeast = index(grid((0, 1)))
    southeast = index(grid((1, 0)))
    assert index.Mor(northeast, southeast).cardinality() == cardinal(0)
    assert index.Mor(southeast, northeast).cardinality() == cardinal(0)

    rectangle_points = finite_ordered_set(
        tuple(grid(point) for point in ((0, 0), (0, 1), (1, 0), (1, 1)))
    )
    rectangle = PosetCategory(rectangle_points, le=index.le)

    class RectangleInclusion(Functor):
        def __init__(self):
            super().__init__(rectangle, index)

        def _apply_object(self, obj):
            return index(obj.value())

        def _apply_morphism(self, morphism):
            return index.Mor(
                self(morphism.domain()), self(morphism.codomain())
            ).unique()

    restricted = system.restrict(RectangleInclusion())
    construction = LimitsOfCategory(rectangle, line.category()).construction(restricted)
    assert construction.diagram() is restricted
    assert construction.structure_morphism(rectangle(grid((1, 1)))).codomain() is line

    with pytest.raises(NotImplementedError, match="finite represented shape"):
        LimitsOfCategory(index, line.category()).construction(system)


def test_inverse_tower_retains_transition_maps_without_claiming_an_infinite_limit() -> None:
    line = ZZ.free_module(finite_ordered_set(("e",)))
    e = line.module_generator("e")
    base_index = PosetCategory(NN)
    inverse_systems = InverseSystem(base_index, line.category())
    opposite = inverse_systems.index_category()

    class DoublingTower(Functor):
        def __init__(self):
            super().__init__(opposite, line.category())

        def _apply_object(self, _obj):
            return line

        def _apply_morphism(self, morphism):
            underlying = morphism.underlying_arrow()
            source = int(underlying.domain().value())
            target = int(underlying.codomain().value())
            return line.module_category().Mor(line, line)({"e": (2 ** (target - source)) * e})

    tower = DoublingTower()
    base_arrow = base_index.Mor(base_index(0), base_index(2)).unique()
    tower_arrow = opposite.Mor(opposite(base_index(2)), opposite(base_index(0)))(
        base_arrow
    )
    assert tower(tower_arrow)(e) == 4 * e
    with pytest.raises(NotImplementedError):
        LimitsOfCategory(opposite, line.category()).construction(tower)


def test_direct_sequence_coprojection_can_fail_to_be_injective() -> None:
    line = ZZ.free_module(finite_ordered_set(("e",)))
    zero = ZZ.free_module(finite_ordered_set(()))
    collapse = line.module_category().Mor(line, zero).zero()
    diagram = FiniteSequenceDiagram((line, zero), (collapse,), line.category())
    colimit = ColimitsOfCategory(diagram.domain(), line.category()).construction(diagram)
    shape = diagram.domain()

    first_coprojection = colimit.costructure_morphism(shape(0))
    assert not first_coprojection.is_injective()
