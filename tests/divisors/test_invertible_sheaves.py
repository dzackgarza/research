from __future__ import annotations

from typing import Any


def _generator(module: Any) -> Any:
    return module.module_generator(next(iter(module.module_generating_set())))


def _transition(source: Any, target: Any, unit: Any) -> Any:
    source_generator = _generator(source)
    target_generator = _generator(target)
    forward = source.module_category().Mor(source, target)(
        lambda _label: target.scalar_multiple(unit, target_generator)
    )
    inverse = target.module_category().Mor(target, source)(
        lambda _label: source.scalar_multiple(
            unit.inverse_of_unit(),
            source_generator,
        )
    )
    return source.module_category().Core().Mor(source, target)(forward, inverse)


def test_rank_one_descent_is_an_invertible_sheaf_with_tensor_powers() -> None:
    from sage.rings.rational_field import QQ as SageQQ

    from dzack_research.preamble.all import (
        InvertibleSheaf,
        )
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

    QQ = _own_ring(SageQQ)

    algebra = QQ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    scheme = (algebra).affine_spectrum()
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    local_modules = tuple(
        open_subscheme.coordinate_algebra().free_module(1)
        for open_subscheme in cover.opens()
    )
    left_overlap = cover.restrict_module(local_modules[0], 0, 1)
    right_overlap = cover.restrict_module(local_modules[1], 1, 0)
    overlap_x = scheme.structure_sheaf().restriction_map(
        scheme,
        cover.overlap(0, 1),
    )(x)
    sheaf = cover.glue_modules(
        local_modules,
        {(0, 1): _transition(left_overlap, right_overlap, overlap_x)},
    )
    datum = sheaf.gluing_datum()
    line = InvertibleSheaf(datum)

    assert line.scheme() is scheme
    assert line.cover() is cover
    assert line.transition_unit(0, 1) == overlap_x
    assert line.transition_unit(1, 0) == overlap_x.inverse_of_unit()
    assert line.local_trivialization(0).domain() is local_modules[0]

    square = line.tensor_power(2)
    dual = line.dual_sheaf()
    neutral = line.tensor_product(dual)
    trivial = InvertibleSheaf.trivial(cover)
    assert square.transition_unit(0, 1) == overlap_x**2
    assert dual.transition_unit(0, 1) == overlap_x.inverse_of_unit()
    assert neutral.transition_unit(0, 1) == overlap_x.parent().one()
    assert line.tensor_power(0).transition_unit(0, 1) == overlap_x.parent().one()
    assert trivial.transition_unit(0, 1) == overlap_x.parent().one()


def test_invertible_sheaf_sections_and_morphisms_use_module_descent() -> None:
    from sage.rings.rational_field import QQ as SageQQ

    from dzack_research.preamble.all import (
        InvertibleSheaf,
        )
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

    QQ = _own_ring(SageQQ)

    algebra = QQ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    scheme = (algebra).affine_spectrum()
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    local_modules = tuple(
        open_subscheme.coordinate_algebra().free_module(1)
        for open_subscheme in cover.opens()
    )
    left_overlap = cover.restrict_module(local_modules[0], 0, 1)
    right_overlap = cover.restrict_module(local_modules[1], 1, 0)
    overlap_x = scheme.structure_sheaf().restriction_map(
        scheme,
        cover.overlap(0, 1),
    )(x)
    line = InvertibleSheaf(
        cover.glue_modules(
            local_modules,
            {(0, 1): _transition(left_overlap, right_overlap, overlap_x)},
        ).gluing_datum()
    )

    left_generator = _generator(local_modules[0])
    right_generator = _generator(local_modules[1])
    right_x = scheme.structure_sheaf().restriction_map(scheme, cover.open(1))(x)
    section = line.global_sections()(
        (
            left_generator,
            local_modules[1].scalar_multiple(right_x, right_generator),
        )
    )
    local_maps = tuple(
        module.module_category().Mor(module, module)(
            lambda label, module=module: module.scalar_multiple(
                module.base_ring()(2),
                module.module_generator(label),
            )
        )
        for module in local_modules
    )
    morphism = line.morphism_to(line, local_maps)
    image = morphism.global_sections_map()(section)

    assert image.parent() is line.global_sections()
    assert image.component(0) == local_maps[0](left_generator)
    assert image.component(1) == local_maps[1](section.component(1))


def test_invertible_sheaf_rejects_non_rank_one_local_modules() -> None:
    from pytest import raises
    from sage.rings.rational_field import QQ as SageQQ

    from dzack_research.preamble.all import (
        InvertibleSheaf,
        )
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

    QQ = _own_ring(SageQQ)

    algebra = QQ.polynomial_ring("x")
    x = algebra.algebra_generator("x")
    scheme = (algebra).affine_spectrum()
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    local_modules = tuple(
        open_subscheme.coordinate_algebra().free_module(2)
        for open_subscheme in cover.opens()
    )
    left_overlap = cover.restrict_module(local_modules[0], 0, 1)
    right_overlap = cover.restrict_module(local_modules[1], 1, 0)
    forward = left_overlap.module_category().Mor(left_overlap, right_overlap)(
        {
            label: right_overlap.module_generator(label)
            for label in left_overlap.module_generating_set()
        }
    )
    inverse = right_overlap.module_category().Mor(right_overlap, left_overlap)(
        {
            label: left_overlap.module_generator(label)
            for label in right_overlap.module_generating_set()
        }
    )
    datum = cover.glue_modules(
        local_modules,
        {
            (0, 1): left_overlap.module_category()
            .Core()
            .Mor(left_overlap, right_overlap)(forward, inverse)
        },
    ).gluing_datum()
    with raises(TypeError, match="rank-one finite free"):
        InvertibleSheaf(datum)
