r"""The underlying linear map of an algebra morphism is a module morphism.

``U`` changes neither an element nor its image.  What it must deliver is a map
that answers the module level: the kernel and the coordinate matrix are
computed from the algebra morphism, not read off state that a bare morphism
never established.

The specimen is the fat point ``QQ[x]/(x^2)`` projecting onto the reduced
point ``QQ[x]/(x)``.  Both are free of finite rank over ``QQ``, so each is its
own underlying module, and the kernel of the projection is the line spanned by
the nilpotent.
"""

from dzack_research.preamble.all import (
    FinitelyPresentedAlgebra,
    Modules,
    PolynomialRing,
    QQ,
    algebra_underlying_module_functor,
)


def _fat_point_projection():
    r"""Return the fat point, the reduced point, and the projection between them."""
    line = PolynomialRing(QQ, "x")
    x = line.algebra_generator("x")
    fat_point = FinitelyPresentedAlgebra(line, [x**2])
    point, projection = fat_point._quotient_by_algebra_elements([fat_point(x)])
    return fat_point, point, projection


def test_the_underlying_map_sends_the_same_elements_to_the_same_images() -> None:
    fat_point, point, projection = _fat_point_projection()
    x = fat_point.algebra_generator("x")
    forget = algebra_underlying_module_functor(QQ)

    underlying = forget(projection)

    assert underlying.domain() is forget(fat_point)
    assert underlying.codomain() is forget(point)
    assert underlying.parent() is Modules(QQ).Mor(fat_point, point)
    assert underlying(fat_point.one()) == point.one()
    assert underlying(x) == point.zero()


def test_the_underlying_map_answers_the_module_level() -> None:
    fat_point, point, projection = _fat_point_projection()
    forget = algebra_underlying_module_functor(QQ)

    underlying = forget(projection)
    kernel = underlying.kernel()

    assert not underlying.is_injective()
    assert kernel.rank() == 1
    for label in kernel.module_generating_set():
        generator = kernel.inclusion()(kernel.module_generator(label))
        assert underlying(generator) == point.zero()
