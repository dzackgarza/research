from __future__ import annotations

from typing import Any


def _generator(module: Any) -> Any:
    return module.module_generator(next(iter(module.module_generating_set())))


def _line_bundle_with_x_transition() -> tuple[Any, Any, Any]:
    from sage.rings.rational_field import QQ as SageQQ

    from dzack_research.preamble.all import FreeModule, InvertibleSheaf, Spec
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
        Isomorphism,
    )
    from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        module_homset,
    )
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

    QQ = _own_ring(SageQQ)
    algebra = PolynomialRing(QQ, "x")
    x = algebra.algebra_generator("x")
    scheme = Spec(algebra)
    cover = scheme.distinguished_open_cover(x, algebra.one() - x)
    local_modules = tuple(
        FreeModule(open_subscheme.coordinate_algebra(), 1)
        for open_subscheme in cover.opens()
    )
    left_overlap = cover.restrict_module(local_modules[0], 0, 1)
    right_overlap = cover.restrict_module(local_modules[1], 1, 0)
    overlap_x = scheme.structure_sheaf().restriction_map(
        scheme,
        cover.overlap(0, 1),
    )(x)
    transition = Isomorphism(
        module_homset(left_overlap, right_overlap)(
            lambda _label: right_overlap.scalar_multiple(
                overlap_x,
                _generator(right_overlap),
            )
        ),
        module_homset(right_overlap, left_overlap)(
            lambda _label: left_overlap.scalar_multiple(
                overlap_x.inverse_of_unit(),
                _generator(left_overlap),
            )
        ),
    )
    line = InvertibleSheaf(
        cover.glue_modules(local_modules, {(0, 1): transition})
    )
    return line, x, overlap_x


def _branch_section(line: Any, x: Any, degree: int) -> Any:
    power = line.tensor_power(degree)
    right_x = line.scheme().structure_sheaf().restriction_map(
        line.scheme(),
        line.cover().open(1),
    )(x)
    return power.global_sections()(
        (
            _generator(power.local_module(0)),
            power.local_module(1).scalar_multiple(
                right_x**degree,
                _generator(power.local_module(1)),
            ),
        )
    )


def test_cyclic_cover_algebra_keeps_local_equations_modules_and_multiplication() -> None:
    from dzack_research.preamble.all import CyclicCoverAlgebra
    from dzack_research.preamble.categories.algebras.algebras import (
        AlgebrasWithChosenFinitePresentation,
    )
    from dzack_research.preamble.categories.modules.pure.modules import (
        FinitelyGeneratedFreeModules,
    )

    line, x, overlap_x = _line_bundle_with_x_transition()
    branch = _branch_section(line, x, 2)
    cyclic = CyclicCoverAlgebra(line, branch, 2)

    assert cyclic.degree() == 2
    assert cyclic.line_bundle() is line
    assert cyclic.branch_section() is branch
    assert cyclic.local_branch_coefficient(0) == cyclic.local_algebra(0).base_ring().one()

    right_x = line.scheme().structure_sheaf().restriction_map(
        line.scheme(),
        line.cover().open(1),
    )(x)
    assert cyclic.local_branch_coefficient(1) == right_x**2
    for index in range(2):
        local = cyclic.local_algebra(index)
        assert cyclic.local_underlying_module(index) is local
        assert local in FinitelyGeneratedFreeModules(local.base_ring())
        assert local in AlgebrasWithChosenFinitePresentation(local.base_ring())
        assert int(local.module_rank()) == 2
        multiplication = cyclic.local_multiplication(index)
        assert multiplication.codomain() is local
        z = local.algebra_generator("z")
        one_basis = local.module_generator(0)
        z_basis = local.module_generator(1)
        assert multiplication(
            multiplication.domain().pure_tensor(z_basis, z_basis)
        ) == local(cyclic.local_branch_coefficient(index))
        assert multiplication(
            multiplication.domain().pure_tensor(one_basis, z_basis)
        ) == z_basis
        assert z**2 == local(cyclic.local_branch_coefficient(index))
        assert cyclic.local_equation(index) == (
            cyclic.local_presentation(index)[0].algebra_generator("z") ** 2
            - cyclic.local_branch_coefficient(index)
        )

    transition = cyclic.transition(0, 1).forward()
    source = transition.domain()
    target = transition.codomain()
    assert transition(source.algebra_generator("z")) == (
        target(overlap_x.inverse_of_unit()) * target.algebra_generator("z")
    )
    assert int(cyclic.restricted_algebra(0, 0, 1).module_rank()) == 2
    assert int(cyclic.restricted_algebra(1, 0, 1).module_rank()) == 2
    restricted = cyclic.restricted_algebra(0, 0, 1)
    assert restricted.multiplication_morphism().codomain() is restricted
    assert cyclic.sheaf().global_sections() is cyclic.global_sections()
    assert cyclic.underlying_module_datum() is cyclic.gluing_datum().underlying_module_datum()


def test_cyclic_cover_rejects_branch_section_with_wrong_line_power_descent() -> None:
    from pytest import raises

    from dzack_research.preamble.all import CyclicCoverAlgebra, TrivialInvertibleSheaf

    line, _x, _overlap_x = _line_bundle_with_x_transition()
    trivial_power = TrivialInvertibleSheaf(line.cover()).tensor_power(2)
    wrong_branch = trivial_power.global_sections()(
        tuple(_generator(trivial_power.local_module(index)) for index in range(2))
    )

    with raises(ValueError, match=r"section of the stated L\^n"):
        CyclicCoverAlgebra(line, wrong_branch, 2)


def test_cyclic_cover_degree_three_uses_rank_three_scalar_extensions() -> None:
    from dzack_research.preamble.all import CyclicCoverAlgebra

    line, x, overlap_x = _line_bundle_with_x_transition()
    branch = _branch_section(line, x, 3)
    cyclic = CyclicCoverAlgebra(line, branch, 3)

    assert all(int(local.module_rank()) == 3 for local in cyclic.local_algebras())
    transition = cyclic.transition(0, 1).forward()
    assert transition(transition.domain().algebra_generator("z")) == (
        transition.codomain()(overlap_x.inverse_of_unit())
        * transition.codomain().algebra_generator("z")
    )
    assert int(cyclic.restricted_algebra(0, 0, 1).module_rank()) == 3
