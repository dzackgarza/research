from __future__ import annotations

from typing import Any


def _generator(module: Any) -> Any:
    return module.module_generator(next(iter(module.module_generating_set())))


def _transition(source: Any, target: Any, unit: Any) -> Any:
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    source_generator = _generator(source)
    target_generator = _generator(target)
    return Isomorphism(
        module_homset(source, target)(
            lambda _label: target.scalar_multiple(unit, target_generator)
        ),
        module_homset(target, source)(
            lambda _label: source.scalar_multiple(
                unit.inverse_of_unit(),
                source_generator,
            )
        ),
    )


def test_rank_one_descent_is_an_invertible_sheaf_with_tensor_powers() -> None:
    from sage.rings.rational_field import QQ as SageQQ

    from dzack_research.preamble.all import (
        FreeModule,
        InvertibleSheaf,
        Spec,
        TrivialInvertibleSheaf,
    )
    from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

    QQ = _own_ring(SageQQ)

    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    local_modules = tuple(
        FreeModule(open_subscheme.coordinate_algebra(), 1)
        for open_subscheme in cover.opens()
    )
    left_overlap = cover.restrict_module(local_modules[0], 0, 1)
    right_overlap = cover.restrict_module(local_modules[1], 1, 0)
    overlap_x = scheme.structure_sheaf().restriction_map(
        scheme,
        cover.overlap(0, 1),
    )(x)
    datum = cover.glue_modules(
        local_modules,
        {(0, 1): _transition(left_overlap, right_overlap, overlap_x)},
    )
    line = InvertibleSheaf(datum)

    assert line.scheme() is scheme
    assert line.cover() is cover
    assert line.transition_unit(0, 1) == overlap_x
    assert line.transition_unit(1, 0) == overlap_x.inverse_of_unit()
    assert line.local_trivialization(0).domain() is local_modules[0]

    square = line.tensor_power(2)
    dual = line.dual()
    neutral = line.tensor_product(dual)
    trivial = TrivialInvertibleSheaf(cover)
    assert square.transition_unit(0, 1) == overlap_x**2
    assert dual.transition_unit(0, 1) == overlap_x.inverse_of_unit()
    assert neutral.transition_unit(0, 1) == overlap_x.parent().one()
    assert line.tensor_power(0).transition_unit(0, 1) == overlap_x.parent().one()
    assert trivial.transition_unit(0, 1) == overlap_x.parent().one()


def test_invertible_sheaf_sections_and_morphisms_use_module_descent() -> None:
    from sage.rings.rational_field import QQ as SageQQ

    from dzack_research.preamble.all import (
        FreeModule,
        InvertibleSheaf,
        Spec,
    )
    from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

    QQ = _own_ring(SageQQ)

    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    local_modules = tuple(
        FreeModule(open_subscheme.coordinate_algebra(), 1)
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
        )
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
        module_homset(module, module)(
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
        FreeModule,
        InvertibleSheaf,
        Spec,
    )
    from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

    QQ = _own_ring(SageQQ)

    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    local_modules = tuple(
        FreeModule(open_subscheme.coordinate_algebra(), 2)
        for open_subscheme in cover.opens()
    )
    left_overlap = cover.restrict_module(local_modules[0], 0, 1)
    right_overlap = cover.restrict_module(local_modules[1], 1, 0)
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )

    forward = module_homset(left_overlap, right_overlap)(
        {
            label: right_overlap.module_generator(label)
            for label in left_overlap.module_generating_set()
        }
    )
    inverse = module_homset(right_overlap, left_overlap)(
        {
            label: left_overlap.module_generator(label)
            for label in right_overlap.module_generating_set()
        }
    )
    datum = cover.glue_modules(
        local_modules,
        {(0, 1): Isomorphism(forward, inverse)},
    )
    with raises(TypeError, match="rank-one finite free"):
        InvertibleSheaf(datum)
