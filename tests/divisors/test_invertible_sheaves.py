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

    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
    from dzack_research.preamble.categories.schemes.ringed_spaces import (
        QuasiCoherentSheaves,
    )

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
    invertible = QuasiCoherentSheaves(scheme).Invertible()
    trivialized = invertible.WithChosenTrivialization()
    line = trivialized(datum)

    assert line in invertible
    assert line in trivialized
    assert line.trivializing_cover() is cover
    assert line.is_invertible()
    assert line.scheme() is scheme
    assert line.cover() is cover
    assert line.transition_unit(0, 1) == overlap_x
    assert line.transition_unit(1, 0) == overlap_x.inverse_of_unit()
    assert line.local_trivialization(0).domain() is local_modules[0]

    square = line.tensor_power(2)
    dual = line.dual_sheaf()
    neutral = line.tensor_product(dual)
    trivial = trivialized.trivial(cover)
    assert square.transition_unit(0, 1) == overlap_x**2
    assert dual.transition_unit(0, 1) == overlap_x.inverse_of_unit()
    assert neutral.transition_unit(0, 1) == overlap_x.parent().one()
    assert line.tensor_power(0).transition_unit(0, 1) == overlap_x.parent().one()
    assert trivial.transition_unit(0, 1) == overlap_x.parent().one()






