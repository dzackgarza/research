r"""Coextension of scalars ``Hom_R(S, -)`` and the ``S``-module constructor from a scalar action.

Specimens: ``S = QQ[x]/(x^2 + 1)`` over ``QQ`` and ``ZZ[S_3]`` over ``ZZ``, both
finitely framed over their scalars.
"""

from dzack_research.preamble.all import (
    QQ,
    ZZ,
    FinitelyPresentedAlgebra,
    FreeModule,
    Groups,
    Modules,
    SymmetricAlgebraOn,
    module_homset,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism


def _gaussian_rationals():
    r"""``S = QQ[x]/(x^2 + 1)`` with its class ``i`` of ``x`` and its structure map ``QQ -> S``."""
    polynomials = SymmetricAlgebraOn(QQ, ["x"])
    x = next(iter(polynomials.algebra_generators()))
    scalars = FinitelyPresentedAlgebra(polynomials, [x**2 + 1])
    return scalars, scalars(x), scalars._ring_morphism_defining_algebra_structure()


def test_a_module_over_an_algebra_is_constructed_from_its_scalar_action() -> None:
    r"""``QQ^2`` with ``i`` acting by a quarter turn is a ``QQ[i]``-module on which ``i^2 = -1``."""
    scalars, i, _ = _gaussian_rationals()
    plane = FreeModule(QQ, 2)
    endomorphisms = Modules(QQ).End(plane)
    e0, e1 = plane.module_generator(0), plane.module_generator(1)
    quarter_turn = endomorphisms({0: e1, 1: -e0})

    labels = scalars.module_generating_set()
    one_label, i_label = labels[0], labels[1]

    def action(scalar):
        coefficients = module_coefficients(scalar, scalars)
        constant = coefficients.get(one_label, QQ.zero())
        imaginary = coefficients.get(i_label, QQ.zero())
        return endomorphisms.elementwise(
            lambda vector: constant * vector + imaginary * quarter_turn(vector),
            verify_linearity=False,
        )

    gaussian_plane = Modules(scalars)(plane, ring_morphism(scalars, endomorphisms, action))

    assert gaussian_plane in Modules(scalars)
    vector = gaussian_plane(e0 + 2 * e1)
    assert gaussian_plane.scalar_multiple(i, vector) == gaussian_plane(-2 * e0 + e1)
    assert gaussian_plane.scalar_multiple(i, gaussian_plane.scalar_multiple(i, vector)) == -vector
    assert gaussian_plane.scalar_multiple(3 + 2 * i, vector) == gaussian_plane(-e0 + 8 * e1)


def test_coextension_along_a_quadratic_algebra_acts_by_the_right_regular_action() -> None:
    r"""On ``Hom_QQ(S, QQ)`` the action is ``(s . phi)(t) = phi(t s)``, so ``i`` squares to ``-1``."""
    scalars, i, structure_map = _gaussian_rationals()
    line = FreeModule(QQ, 1)
    coextension = Modules(QQ).coextension_of_scalars(structure_map)
    coextended = coextension(line)
    assert coextended in Modules(scalars)

    dual_basis = list(coextended.underlying_set().module_generators())
    phi = coextended(dual_basis[0] + 3 * dual_basis[1])
    acted = coextended.scalar_multiple(i, phi).underlying_element()
    assert acted(scalars.one()) == phi.underlying_element()(i)
    assert acted(i) == -phi.underlying_element()(scalars.one())
    assert coextended.scalar_multiple(i, coextended.scalar_multiple(i, phi)) == -phi


def test_coextension_along_a_group_algebra_is_the_coinduced_module_of_the_trivial_group() -> None:
    r"""``Hom_ZZ(ZZ[G], ZZ)`` is a ``ZZ[G]``-module of rank ``|G|`` whose invariants are the constants."""
    group = Groups.S(3)
    group_algebra = ZZ[group]
    coextension = Modules(ZZ).coextension_of_scalars(
        ring_morphism(ZZ, group_algebra, lambda integer: integer * group_algebra.one())
    )
    coextended = coextension(FreeModule(ZZ, 1))

    assert coextended in Modules(group_algebra)
    assert coextended.rank() == 6
    assert coextended.module_invariants().rank() == 1
    assert coextended.module_coinvariants().rank() == 1


def test_restriction_is_left_adjoint_to_coextension() -> None:
    r"""The Hom bijection ``Hom_QQ(Res N, M) ~ Hom_S(N, Hom_QQ(S, M))`` round-trips a chosen map."""
    scalars, i, structure_map = _gaussian_rationals()
    free_line = FreeModule(scalars, 1)
    target = FreeModule(QQ, 1)
    adjunction = Modules(scalars).restriction_coextension_adjunction(structure_map)
    restricted = adjunction.left_adjoint()(free_line)
    generator = free_line.module_generator(0)

    unit = adjunction.unit(free_line)
    assert unit(i * generator) == unit.codomain().scalar_multiple(i, unit(generator))

    labels = restricted.module_generating_set()
    weights = module_homset(restricted, target)(
        {label: (1 + int(labels.ranking_map()(label))) * target.module_generator(0) for label in labels}
    )
    transposed = adjunction.hom_set_isomorphism_forward(weights)
    assert transposed.domain() is free_line
    recovered = adjunction.hom_set_isomorphism_inverse(transposed, target)
    for label in labels:
        element = restricted.module_generator(label)
        assert recovered(element) == weights(element)


def test_restriction_along_the_structure_map_of_a_group_algebra_forgets_the_action() -> None:
    r"""Along ``ZZ -> ZZ[C2]`` restriction forgets the action and is left adjoint to coextension."""
    group = Groups.C(2)
    group_algebra = ZZ[group]
    structure_map = ring_morphism(ZZ, group_algebra, lambda integer: integer * group_algebra.one())
    plane = FreeModule(ZZ, 2)
    labels = plane.module_generating_set()
    first, second = labels[0], labels[1]
    e0, e1 = plane.module_generator(first), plane.module_generator(second)

    def swap(group_element, vector):
        if group_element == group.one():
            return vector
        coefficients = module_coefficients(vector, plane)
        return coefficients.get(second, ZZ.zero()) * e0 + coefficients.get(first, ZZ.zero()) * e1

    swapped = Modules(group_algebra)(plane, swap)
    adjunction = Modules(group_algebra).restriction_coextension_adjunction(structure_map)
    forgotten = adjunction.left_adjoint()(swapped)
    assert forgotten in Modules(ZZ)
    assert forgotten.rank() == 2

    generator = group.group_generators()[0]
    unit = adjunction.unit(swapped)
    coextended = unit.codomain()
    assert unit(swapped.act(generator, swapped.module_generator(0))) == coextended.act(
        generator, unit(swapped.module_generator(0))
    )

    target = FreeModule(ZZ, 1)
    weights = module_homset(forgotten, target)(
        {0: target.module_generator(0), 1: 3 * target.module_generator(0)}
    )
    transposed = adjunction.hom_set_isomorphism_forward(weights)
    assert transposed.domain() is swapped
    recovered = adjunction.hom_set_isomorphism_inverse(transposed, target)
    for label in forgotten.module_generating_set():
        element = forgotten.module_generator(label)
        assert recovered(element) == weights(element)
