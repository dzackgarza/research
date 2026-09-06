r"""The form functors and their adjunctions display as the mathematics they are.

A functor printed as its Python identity tells a reader nothing, and an
adjunction is displayed through its two adjoints, so an unnamed adjoint takes
the adjunction down with it.  Every other functor in the preamble names
itself; these four are asked the same question here.
"""

from dzack_research.preamble.all import (
    BilinearFreeFormAdjunction,
    BilinearUnderlyingModuleFunctor,
    FreeBilinearFormFunctor,
    FreeQuadraticFormFunctor,
    QuadraticFreeFormAdjunction,
    QuadraticUnderlyingModuleFunctor,
    ZZ,
)


def test_each_form_functor_names_its_construction_and_its_ring() -> None:
    assert repr(FreeBilinearFormFunctor(ZZ)) == f"Free bilinear-form functor on {ZZ}-modules"
    assert repr(FreeQuadraticFormFunctor(ZZ)) == f"Free quadratic-form functor on {ZZ}-modules"
    assert (
        repr(BilinearUnderlyingModuleFunctor(ZZ))
        == f"Underlying-module functor on bilinear formed {ZZ}-modules"
    )
    assert (
        repr(QuadraticUnderlyingModuleFunctor(ZZ))
        == f"Underlying-module functor on quadratic formed {ZZ}-modules"
    )


def test_each_free_form_adjunction_displays_both_of_its_adjoints() -> None:
    for adjunction in (BilinearFreeFormAdjunction(ZZ), QuadraticFreeFormAdjunction(ZZ)):
        shown = repr(adjunction)

        assert repr(adjunction.left_adjoint()) in shown
        assert repr(adjunction.right_adjoint()) in shown
