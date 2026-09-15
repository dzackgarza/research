r"""``G_L = {g in G : g(L) = L}`` for a lattice inside a rational space.

A lattice in a ``QQ``-space ``V`` is a monomorphism ``L -> Res(V)`` with ``ZZ``
on both sides, and the integral stabilizer of a rational group ``G`` is cut out
of ``G`` by ``g(L) = L``.  The specimens live in the hyperbolic plane over
``QQ``, where ``diag(t, 1/t)`` is an isometry for every nonzero ``t``: on the
isotropic line ``ZZ e_0`` that isometry gives ``g(L) < L``, which separates the
equality from the containment.

Unverified: written without running the suite.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FreeModule,
    Lattices,
    Modules,
    IntegralStructureAction,
)


def _the_rational_hyperbolic_plane():
    r"""``U`` over ``QQ`` together with ``Res(U)``, the same group read over ``ZZ``."""
    plane = Lattices(QQ)("U")
    restriction = Modules(QQ).restriction_of_scalars(
        ZZ.Mor(QQ)(lambda element: QQ(element))
    )
    return plane, restriction(plane)


def test_an_isometry_carrying_the_standard_lattice_onto_itself_stabilizes_it() -> None:
    r"""The swap of the two isotropic generators preserves ``ZZ e_0 + ZZ e_1``."""
    plane, space = _the_rational_hyperbolic_plane()
    e0, e1 = plane.module_generators()
    standard_module = FreeModule(ZZ, 2)
    standard = standard_module.Mono(space)(
        {0: space.wrap(e0), 1: space.wrap(e1)}
    )
    orthogonal_group = plane.Aut()
    swap = orthogonal_group({0: e1, 1: e0})

    assert swap in IntegralStructureAction(orthogonal_group, standard).stabilizer()


def test_an_isometry_moving_a_generator_off_the_lattice_leaves_the_stabilizer() -> None:
    r"""``diag(2, 1/2)`` sends ``e_1`` to ``e_1/2``, which is not in the lattice."""
    plane, space = _the_rational_hyperbolic_plane()
    e0, e1 = plane.module_generators()
    standard_module = FreeModule(ZZ, 2)
    standard = standard_module.Mono(space)(
        {0: space.wrap(e0), 1: space.wrap(e1)}
    )
    orthogonal_group = plane.Aut()
    scaling = orthogonal_group(
        {
            0: plane.scalar_multiple(QQ(2), e0),
            1: plane.scalar_multiple(QQ(1) / 2, e1),
        }
    )

    assert scaling not in IntegralStructureAction(orthogonal_group, standard).stabilizer()


def test_an_isometry_shrinking_an_isotropic_line_leaves_its_stabilizer() -> None:
    r"""``diag(2, 1/2)`` carries ``ZZ e_0`` onto ``2 ZZ e_0``, properly inside it.

    The containment ``g(L) <= L`` holds and the equality does not, so a
    stabilizer that tested only that containment would admit this isometry.
    Negation, which does carry the line onto itself, is admitted.
    """
    plane, space = _the_rational_hyperbolic_plane()
    e0, e1 = plane.module_generators()
    line_module = FreeModule(ZZ, 1)
    line = line_module.Mono(space)({0: space.wrap(e0)})
    orthogonal_group = plane.Aut()
    scaling = orthogonal_group(
        {
            0: plane.scalar_multiple(QQ(2), e0),
            1: plane.scalar_multiple(QQ(1) / 2, e1),
        }
    )
    negation = orthogonal_group({0: -e0, 1: -e1})

    stabilizer = IntegralStructureAction(orthogonal_group, line).stabilizer()

    assert line.is_in_image(space.wrap(scaling(e0)))
    assert scaling not in stabilizer
    assert negation in stabilizer


def test_commensurable_lattices_have_different_stabilizers_in_one_group() -> None:
    r"""``2M <= L <= M`` for ``M = ZZ e_0 + ZZ e_1/2``, and the swap preserves only ``L``."""
    plane, space = _the_rational_hyperbolic_plane()
    e0, e1 = plane.module_generators()
    half = plane.scalar_multiple(QQ(1) / 2, e1)
    standard_module = FreeModule(ZZ, 2)
    finer_module = FreeModule(ZZ, 2)
    doubled_module = FreeModule(ZZ, 2)
    standard = standard_module.Mono(space)(
        {0: space.wrap(e0), 1: space.wrap(e1)}
    )
    finer = finer_module.Mono(space)(
        {0: space.wrap(e0), 1: space.wrap(half)}
    )
    doubled = doubled_module.Mono(space)(
        {0: space.wrap(plane.scalar_multiple(QQ(2), e0)), 1: space.wrap(e1)},
    )
    orthogonal_group = plane.Aut()
    swap = orthogonal_group({0: e1, 1: e0})

    assert standard.factor_through(finer).codomain() is finer.domain()
    assert doubled.factor_through(standard).codomain() is standard.domain()
    assert swap in IntegralStructureAction(orthogonal_group, standard).stabilizer()
    assert swap not in IntegralStructureAction(orthogonal_group, finer).stabilizer()
