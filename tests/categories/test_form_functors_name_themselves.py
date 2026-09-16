r"""The form functors and their adjunctions display as the mathematics they are.

A functor printed as its Python identity tells a reader nothing, and an
adjunction is displayed through its two adjoints, so an unnamed adjoint takes
the adjunction down with it.  Every other functor in the preamble names
itself; these four are asked the same question here.
"""

from dzack_research.preamble.all import Modules, ZZ



def test_each_form_functor_names_its_construction_ring_and_endpoints() -> None:
    bilinear = Modules(ZZ).bilinear_free_form_adjunction()
    quadratic = Modules(ZZ).quadratic_free_form_adjunction()
    functors = (
        (bilinear.left_adjoint(), "Free bilinear-form functor"),
        (quadratic.left_adjoint(), "Free quadratic-form functor"),
        (bilinear.right_adjoint(), "Underlying-module functor"),
        (quadratic.right_adjoint(), "Underlying-module functor"),
    )
    for functor, label in functors:
        shown = repr(functor)
        assert label in shown
        assert str(ZZ) in shown
        assert str(functor.domain()) in shown
        assert str(functor.codomain()) in shown
        assert " -> " in shown


def test_each_free_form_adjunction_displays_its_categorical_endpoints() -> None:
    for adjunction in (
        Modules(ZZ).bilinear_free_form_adjunction(),
        Modules(ZZ).quadratic_free_form_adjunction(),
    ):
        shown = repr(adjunction)
        left = adjunction.left_adjoint()
        assert str(left.domain()) in shown
        assert str(left.codomain()) in shown
        assert " <-> " in shown
