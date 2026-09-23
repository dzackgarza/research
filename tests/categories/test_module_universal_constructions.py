
from dzack_research.preamble.all import ZZ
from dzack_research.preamble.categories.abstract_categories.products import (
    PosetCategory,
)
from dzack_research.preamble.categories.functors.core import (
    Functor,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.sets import Sets, finite_ordered_set
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




















def test_twice_and_zero_on_Zmod4_have_the_order_two_equalizer_submodule() -> None:
    cover = ZZ.free_module(finite_ordered_set(("e",)))
    relations = ZZ.free_module(finite_ordered_set(("r",)))
    cyclic_four = relations.module_category().Mor(relations, cover)(
        {"r": 4 * cover.module_generator("e")}
    ).cokernel()
    generator = cyclic_four.module_generator("e")
    endomorphisms = cyclic_four.module_category().Mor(cyclic_four, cyclic_four)
    twice = endomorphisms({"e": 2 * generator})
    zero = endomorphisms.zero()

    selected = Modules(ZZ).equalizer_construction(twice, zero)
    equalizer = selected.object()
    shape = selected.diagram().domain()
    inclusion = selected.structure_morphism(shape.source())
    order_two = Modules(ZZ).equalizer_element(selected, 2 * generator)

    assert order_two != equalizer.zero()
    assert inclusion(order_two) == 2 * generator
    assert equalizer.scalar_multiple(ZZ(2), order_two) == equalizer.zero()
    assert twice * inclusion == zero * inclusion


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








def test_branching_finite_diagram_limit_imposes_compatibility_not_sequence_order() -> None:
    points = finite_ordered_set(("left", "right", "target"))
    shape = PosetCategory(
        points,
        le=lambda source, target: (
            source == target
            or target == "target" and source in ("left", "right")
        ),
    )
    line = ZZ.free_module(finite_ordered_set(("e",)))
    e = line.module_generator("e")
    twice = line.module_category().Mor(line, line)({"e": 2 * e})
    thrice = line.module_category().Mor(line, line)({"e": 3 * e})
    identity = line.module_category().Mor(line, line).identity()

    class BranchingDiagram(Functor):
        def __init__(self):
            super().__init__(shape, line.category())

        def _apply_object(self, _obj):
            return line

        def _apply_morphism(self, morphism):
            source = morphism.domain().value()
            target = morphism.codomain().value()
            match source, target:
                case left, right if left == right:
                    return identity
                case "left", "target":
                    return twice
                case "right", "target":
                    return thrice
                case _:
                    raise ValueError("unexpected arrow in the branching index category")

    diagram = BranchingDiagram()
    construction = line.category().Limits(shape).construction(diagram)
    assert shape.Mor(shape("left"), shape("right")).cardinality() == cardinal(0)
    assert shape.Mor(shape("right"), shape("left")).cardinality() == cardinal(0)
    assert construction.object().module_rank() == 1

    probe = ZZ.free_module(finite_ordered_set(("t",)))
    t = probe.module_generator("t")
    to_left = probe.module_category().Mor(probe, line)({"t": 3 * e})
    to_right = probe.module_category().Mor(probe, line)({"t": 2 * e})
    to_target = probe.module_category().Mor(probe, line)({"t": 6 * e})
    cone = diagram.Cones().cone(
        probe,
        lambda index: {
            "left": to_left,
            "right": to_right,
            "target": to_target,
        }[index.value()],
    )
    factor = construction.factor(cone).apex_map()
    assert construction.structure_morphism(shape("left")) * factor == to_left
    assert construction.structure_morphism(shape("right")) * factor == to_right
    assert twice * to_left == thrice * to_right == to_target








