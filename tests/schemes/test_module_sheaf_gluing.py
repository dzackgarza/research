from __future__ import annotations


def _rank_one_generator(module):
    return module.module_generator(next(iter(module.module_generating_set())))


def _rank_one_transition(source, target, unit):
    source_generator = _rank_one_generator(source)
    target_generator = _rank_one_generator(target)
    forward = source.module_category().Mor(source, target)(
        lambda _label: target.scalar_multiple(unit, target_generator)
    )
    inverse = target.module_category().Mor(target, source)(
        lambda _label: source.scalar_multiple(unit.inverse_of_unit(), source_generator)
    )
    return source.module_category().Core().Mor(source, target)(forward, inverse)




def _gluing_datum(sheaf):
    return sheaf.gluing_datum()


def test_two_chart_module_descent_builds_the_actual_compatible_section_module() -> None:
    from dzack_research.preamble.all import Modules, QQ

    algebra = QQ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    scheme = (algebra).affine_spectrum()
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    left, right = cover.opens()
    left_module = left.coordinate_algebra().free_module(1)
    right_module = right.coordinate_algebra().free_module(1)
    left_overlap = cover.restrict_module(left_module, 0, 1)
    right_overlap = cover.restrict_module(right_module, 1, 0)

    overlap_x = scheme.structure_sheaf().restriction_map(
        scheme,
        cover.overlap(0, 1),
    )(x)
    transition = _rank_one_transition(left_overlap, right_overlap, overlap_x)
    sheaf = cover.glue_modules(
        (left_module, right_module),
        {(0, 1): transition},
    )
    gluing = _gluing_datum(sheaf)
    assert sheaf in cover.cech_coverage().sheaves(Modules(algebra))
    sections = sheaf.global_sections()
    construction = gluing.compatible_sections_construction()
    diagram = construction.diagram()
    shape = diagram.domain()
    left_generator = _rank_one_generator(left_module)
    right_generator = _rank_one_generator(right_module)
    right_x = scheme.structure_sheaf().restriction_map(scheme, right)(x)
    compatible = gluing.compatible_section(
        (
            left_generator,
            right_module.scalar_multiple(right_x, right_generator),
        )
    )

    assert construction.object() is sections
    assert diagram.codomain() is Modules(algebra)
    assert diagram(shape.source()) is gluing.local_section_product_construction().object()
    assert diagram(shape.target()) is gluing.matching_section_product_construction().object()
    inclusion = construction.structure_morphism(shape.source())
    assert inclusion.codomain() is gluing.local_section_product_construction().object()
    assert diagram(shape.left()) * inclusion == diagram(shape.right()) * inclusion
    assert compatible in sections
    assert gluing.compatible_section_component(compatible, 0) == left_generator
    assert sheaf.sections_on_chart(0) is left_module
    assert sheaf.sections_on_intersection(0, 0, 1) is left_overlap
    assert sheaf.transition(0, 1).domain() is left_overlap
    assert sheaf.transition(0, 1).codomain() is right_overlap

    scaled = sections.scalar_multiple(x, compatible)
    left_x = scheme.structure_sheaf().restriction_map(scheme, left)(x)
    assert gluing.compatible_section_component(scaled, 0) == left_module.scalar_multiple(
        left_x,
        left_generator,
    )
    assert sections.scalar_action()(x)(compatible) == scaled

    try:
        gluing.compatible_section((left_generator, right_generator))
    except ValueError as error:
        assert "do not agree" in str(error)
    else:
        raise AssertionError("the noncompatible local tuple must not define a global section")












