from dzack_research.preamble.all import (
    FreeModule,
    Lattices,
    Modules,
    QQ,
    ZZ,
    integral_transporter,
    module_embedding,
)


def _rational_hyperbolic_space():
    plane = Lattices(QQ)("U")
    restriction = Modules(QQ).restriction_of_scalars(
        ZZ.Mor(QQ)(lambda element: QQ(element))
    )
    return plane, restriction(plane)


def test_oscar_transporter_lifts_to_the_actual_rational_orthogonal_group() -> None:
    plane, space = _rational_hyperbolic_space()
    e0, e1 = plane.module_generators()
    source = module_embedding(
        FreeModule(ZZ, 2),
        space,
        {0: space.wrap(e0), 1: space.wrap(e1)},
    )
    target = module_embedding(
        FreeModule(ZZ, 2),
        space,
        {
            0: space.wrap(plane.scalar_multiple(QQ(2), e0)),
            1: space.wrap(plane.scalar_multiple(QQ(1) / 2, e1)),
        },
    )

    witness = integral_transporter(plane.Aut(), source, target)
    assert witness is not None
    assert witness in plane.Aut()
    for generator in source.domain().module_generators():
        image = space.wrap(witness(source(generator).underlying_element()))
        assert target.is_in_image(image)
    inverse = ~witness
    for generator in target.domain().module_generators():
        image = space.wrap(inverse(target(generator).underlying_element()))
        assert source.is_in_image(image)


def test_nonisometric_commensurable_lattices_have_no_full_orthogonal_transporter() -> None:
    plane, space = _rational_hyperbolic_space()
    e0, e1 = plane.module_generators()
    source = module_embedding(
        FreeModule(ZZ, 2),
        space,
        {0: space.wrap(e0), 1: space.wrap(e1)},
    )
    target = module_embedding(
        FreeModule(ZZ, 2),
        space,
        {
            0: space.wrap(plane.scalar_multiple(QQ(2), e0)),
            1: space.wrap(e1),
        },
    )

    assert integral_transporter(plane.Aut(), source, target) is None
