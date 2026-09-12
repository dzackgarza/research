r"""Comparison maps at the supported local-module boundary."""

from dzack_research.preamble.all import (
    BasedFreeModule,
    FinitelyPresentedAlgebra,
    PolynomialRing,
    QQ,
    module_homset,
)
from dzack_research.preamble.categories.sets import finite_ordered_set


def test_generated_localization_extension_and_contraction_are_the_same_ideal() -> None:
    ring = PolynomialRing(QQ, ("x", "y"))
    x = ring.algebra_generator("x")
    y = ring.algebra_generator("y")
    ideal = ring.ideal(y)
    localization = ring.localization(x)

    extended = ideal.extension_to_localization(localization)
    contracted = extended.contraction_from_localization()

    assert extended.ring() is localization
    assert contracted.ring() is ring
    assert contracted == ideal


def test_prime_local_units_and_residue_map_use_the_selected_local_ring() -> None:
    ring = PolynomialRing(QQ, ("x",))
    x = ring.algebra_generator("x")
    point = ring.spectrum()(ring.ideal(x))
    local = point.local_ring()
    include = local.localization_map()

    assert not include(x).is_unit()
    assert include(ring.one() + x).is_unit()
    assert point.residue_map()(x) == point.residue_field().zero()
    assert local.residue_map()(include(x)) == point.residue_field().zero()
    assert local.source_residue_map()(x) == point.residue_map()(x)


def test_nonreduced_local_map_kernel_agrees_before_and_after_transport() -> None:
    presentation = PolynomialRing(QQ, ("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    node = FinitelyPresentedAlgebra(presentation, (x * y,))
    x0 = node.algebra_generator("x")
    y0 = node.algebra_generator("y")
    point = node.spectrum()(node.ideal(x0, y0))

    free = BasedFreeModule(node, finite_ordered_set(("g",)))
    generator = free.module_generator("g")
    multiply_x = module_homset(free, free)(
        {"g": free.scalar_multiple(x0, generator)}
    )
    local_free = free.localize_at_prime(point)
    transported = local_free.localization_functor()(multiply_x)
    local_generator = local_free.module_generator("g")
    direct = module_homset(local_free, local_free)(
        {
            "g": local_free.scalar_multiple(
                point.local_ring().localization_map()(x0),
                local_generator,
            )
        }
    )

    assert transported(local_generator) == direct(local_generator)
    transported_kernel = transported.kernel()
    direct_kernel = direct.kernel()
    y_local = point.local_ring().localization_map()(y0)
    y_generator = local_free.scalar_multiple(y_local, local_generator)
    assert transported_kernel.inclusion().is_in_image(y_generator)
    assert direct_kernel.inclusion().is_in_image(y_generator)
    assert transported_kernel == direct_kernel
