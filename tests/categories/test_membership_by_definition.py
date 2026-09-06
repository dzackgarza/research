r"""A category that imposes no condition of its own contains what it is defined by.

Placement is how an object acquires a chosen datum or an axiom, and it is the
right answer for every category that asks something of an object.  It is the
wrong answer for a category whose objects are exactly the objects of its
supercategories: nothing has to be put into an intersection to be in it.
"""

from dzack_research.preamble.all import (
    FinitelyGeneratedFormModules,
    FinitelyGeneratedFreeFormModules,
    FormModules,
    FramedFreeModules,
    FreeFormModules,
    Lattices,
    Modules,
    QQ,
    VectorSpaces,
    ZZ,
)


def test_the_hyperbolic_plane_is_a_free_form_module() -> None:
    hyperbolic_plane = Lattices(ZZ)("U")

    assert hyperbolic_plane in FormModules(ZZ)
    assert hyperbolic_plane in FramedFreeModules(ZZ)
    assert hyperbolic_plane in FreeFormModules(ZZ)


def test_the_hyperbolic_plane_is_a_finitely_generated_free_form_module() -> None:
    hyperbolic_plane = Lattices(ZZ)("U")

    assert hyperbolic_plane in FinitelyGeneratedFormModules(ZZ)
    assert hyperbolic_plane in FinitelyGeneratedFreeFormModules(ZZ)


def test_a_module_over_a_field_is_a_vector_space_over_it() -> None:
    line = Modules(QQ).an_object()

    assert line in Modules(QQ)
    assert line in VectorSpaces(QQ)


def test_a_category_that_states_a_condition_still_decides_by_placement() -> None:
    r"""The intersection reading is a statement, not a weakening of membership.

    ``FormModules(ZZ)`` asks for a form, which is a chosen datum, so a module
    with no form is outside it however many of its supercategories hold the
    module.
    """
    line = Modules(ZZ).an_object()

    assert line in Modules(ZZ)
    assert line not in FormModules(ZZ)
    assert line not in FreeFormModules(ZZ)
