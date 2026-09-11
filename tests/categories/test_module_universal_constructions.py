from dzack_research.preamble.all import BasedFreeModule, ZZ, module_homset
from dzack_research.preamble.categories.abstract_categories.constructions import (
    Coequalizer,
    CoequalizerConstruction,
    Equalizer,
    EqualizerConstruction,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    CoconeCategory,
    ConeCategory,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_module_equalizer_is_the_apex_of_its_actual_universal_cone() -> None:
    plane = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    line = BasedFreeModule(ZZ, finite_ordered_set(("z",)))
    probe = BasedFreeModule(ZZ, finite_ordered_set(("t",)))
    x, y = plane.module_generators()
    z = line.module_generator("z")
    t = probe.module_generator("t")

    left = module_homset(plane, line)({"x": z, "y": line.zero()})
    right = module_homset(plane, line)({"x": line.zero(), "y": z})
    selected = EqualizerConstruction(left, right)
    assert Equalizer(left, right) is selected.object()

    diagram = selected.diagram()
    shape = diagram.domain()
    assert diagram(shape.left()) is left
    assert diagram(shape.right()) is right
    inclusion = selected.structure_morphism(shape.source())
    assert inclusion.codomain() is plane
    assert selected.structure_morphism(shape.target()) == left * inclusion
    assert left * inclusion == right * inclusion

    diagonal = module_homset(probe, plane)({"t": x + y})
    cone = ConeCategory(diagram).cone(
        probe,
        lambda index: diagonal if index is shape.source() else left * diagonal,
    )
    factor = selected.factor(cone).apex_map()
    assert factor.domain() is probe
    assert factor.codomain() is selected.object()
    assert inclusion * factor == diagonal
    assert inclusion(factor(t)) == x + y


def test_module_coequalizer_is_the_apex_of_its_actual_universal_cocone() -> None:
    source = BasedFreeModule(ZZ, finite_ordered_set(("t",)))
    plane = BasedFreeModule(ZZ, finite_ordered_set(("x", "y")))
    target = BasedFreeModule(ZZ, finite_ordered_set(("z",)))
    t = source.module_generator("t")
    x, y = plane.module_generators()
    z = target.module_generator("z")

    left = module_homset(source, plane)({"t": x})
    right = module_homset(source, plane)({"t": y})
    selected = CoequalizerConstruction(left, right)
    assert Coequalizer(left, right) is selected.object()

    diagram = selected.diagram()
    shape = diagram.domain()
    projection = selected.costructure_morphism(shape.target())
    assert projection.domain() is plane
    assert selected.costructure_morphism(shape.source()) == projection * left
    assert projection * left == projection * right

    summation = module_homset(plane, target)({"x": z, "y": z})
    cocone = CoconeCategory(diagram).cocone(
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
    line = BasedFreeModule(ZZ, finite_ordered_set(("e",)))
    e = line.module_generator("e")
    zero = module_homset(line, line)({"e": line.zero()})
    twice = module_homset(line, line)({"e": 2 * e})

    equalizer = Equalizer(zero, twice)
    assert equalizer.module_rank() == 0

    coequalizer = Coequalizer(zero, twice)
    invariants = coequalizer.invariant_factors()
    assert invariants.cardinality() == 1
    assert invariants[0] == ZZ(2)
