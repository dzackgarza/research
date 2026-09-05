from dzack_research.preamble.all import QQ
from dzack_research.preamble.categories.algebras.algebras import (
    AlgebrasWithChosenFinitePresentation,
    CommutativeAlgebraPushouts,
    CommutativeAlgebras,
    commutative_algebra_pushout,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    FinitelyPresentedAlgebra,
    PolynomialRing,
)


def test_xy_equals_t_relative_presentation_and_special_fiber() -> None:
    parameter = PolynomialRing(QQ, "t")
    t = parameter.algebra_generator("t")
    presentation = PolynomialRing(parameter, ("x", "y"))
    x = presentation.algebra_generator("x")
    y = presentation.algebra_generator("y")
    family = FinitelyPresentedAlgebra(presentation, (x * y - t,))
    xbar = family.algebra_generator("x")
    ybar = family.algebra_generator("y")

    assert family.base_ring() is parameter
    assert family in CommutativeAlgebras(parameter)
    assert family in AlgebrasWithChosenFinitePresentation(parameter)
    structure = family.algebra_structure_morphism()
    assert structure.domain() is parameter
    assert family(structure(t)) == xbar * ybar
    assert (
        family.algebra_presentation_morphism()(family.relations().value(0))
        == family.zero()
    )
    assert family.lift_to_presentation(xbar) == x
    assert family.lift_to_presentation(family(t)) == presentation(t)

    residue = parameter.Mor(QQ)({"t": QQ.zero()})
    special_fiber = family.base_change(residue)
    assert special_fiber.base_ring() is QQ
    assert special_fiber in AlgebrasWithChosenFinitePresentation(QQ)
    assert (
        special_fiber.algebra_generator("x")
        * special_fiber.algebra_generator("y")
        == special_fiber.zero()
    )
    fiber_presentation = special_fiber.presentation_ring()
    assert tuple(special_fiber.relations()) == (
        fiber_presentation.algebra_generator("x")
        * fiber_presentation.algebra_generator("y"),
    )


def test_pushout_accepts_maps_from_a_presented_source() -> None:
    source_presentation = PolynomialRing(QQ, "t")
    t = source_presentation.algebra_generator("t")
    source = FinitelyPresentedAlgebra(source_presentation, (t**2,))
    tbar = source.algebra_generator("t")

    target_presentation = PolynomialRing(QQ, "x")
    x = target_presentation.algebra_generator("x")
    target = FinitelyPresentedAlgebra(target_presentation, (x**2,))
    xbar = target.algebra_generator("x")

    left = source.Mor(source).identity()
    right = source.Mor(target)({"t": xbar})
    assert left.parent() is source.Mor(source)
    assert right.parent() is source.Mor(target)

    pushout = commutative_algebra_pushout(left, right)
    assert pushout in CommutativeAlgebraPushouts(QQ)
    left_pushout, right_pushout = pushout.pushout_maps()
    assert left_pushout(left(tbar)) == right_pushout(right(tbar))
