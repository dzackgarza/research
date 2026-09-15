from dzack_research.preamble.all import QQ


def test_xy_equals_t_family_retains_morphism_special_fiber_and_nonsmooth_locus() -> None:
    parameter = QQ.polynomial_ring("t")
    t = parameter.algebra_generator("t")
    family = parameter.affine_equation_family(
        ("x", "y"),
        lambda presentation: (
            presentation.algebra_generator("x")
            * presentation.algebra_generator("y")
            - presentation(t),
        ),
    )

    assert family.morphism().domain() is family.total_space()
    assert family.morphism().codomain() is family.base_scheme()
    assert family.slice_object().arrow() is family.morphism()
    assert family.is_flat()

    special = family.quotient_fiber(parameter.ideal(t))
    special_algebra = special.coordinate_algebra()
    assert special_algebra.algebra_generator("x") * special_algebra.algebra_generator("y") == special_algebra.zero()

    nonsmooth = family.nonsmooth_subscheme()
    xbar = family.total_algebra().algebra_generator("x")
    ybar = family.total_algebra().algebra_generator("y")
    assert nonsmooth.defining_ideal_owned() == family.total_algebra().ideal(xbar, ybar)
