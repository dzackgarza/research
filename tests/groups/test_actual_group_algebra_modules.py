r"""Actual ``R[G]`` module parents and their retained coefficient restrictions.

These assertions distinguish a module whose scalar ring is literally ``R[G]``
from an ``R``-module carrying an extra category annotation.  They are committed
unverified under the repository's terminal-T execution policy.
"""

from dzack_research.preamble.all import (
    AdditiveGroups,
    FinitelyPresentedTorsionModules,
    FreeModule,
    Groups,
    Modules,
    QQ,
    ZZ,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings.ring_foundation import ring_morphism


def _sign_module(ring):
    group = Groups.C(2)
    group_algebra = ring[group]
    line = FreeModule(ring, 1)
    generator = group.group_generators()[0]

    def sign(group_element, vector):
        return vector if group_element == group.one() else -vector

    return group, group_algebra, line, generator, Modules(group_algebra)(line, sign)


def test_group_action_constructs_an_actual_group_algebra_module_parent() -> None:
    group, group_algebra, line, generator, module = _sign_module(QQ)
    label = line.module_generating_set()[0]
    vector = module.module_generator(label)

    assert module in Modules(group_algebra)
    assert module.base_ring() is group_algebra
    assert module.group_algebra() is group_algebra
    assert module.coefficient_ring() is QQ
    assert module.scalar_restriction() is line
    assert module.unacted_module() is line

    scalar_action = module.scalar_action()
    assert scalar_action.domain() is group_algebra
    assert scalar_action.codomain() is AdditiveGroups().AdditiveCommutative().End(
        line.underlying_additive_group()
    )
    group_scalar = group_algebra.module_generator(generator)
    assert module.scalar_multiple(group_scalar, vector) == module.act(generator, vector)

    forget = module.forget_action_morphism()
    equip = module.equip_action_morphism()
    assert forget(vector) == line.module_generator(label)
    assert equip(forget(vector)) == vector
    assert module.module_rank() == line.module_rank()


def test_scalar_restriction_along_R_to_RG_recovers_the_exact_coefficient_module() -> None:
    _group, group_algebra, line, _generator, module = _sign_module(QQ)
    structure_map = group_algebra.algebra_structure_morphism()
    restriction = Modules(group_algebra).restriction_of_scalars(structure_map)

    assert structure_map.domain() is QQ
    assert structure_map.codomain() is group_algebra
    assert restriction(module) is line


def test_equivariant_hom_is_coefficient_linear_underneath() -> None:
    _group, group_algebra, line, _generator, module = _sign_module(QQ)
    label = line.module_generating_set()[0]
    doubling = module.Mor(module)(
        {label: 2 * module.module_generator(label)}
    )
    underlying = doubling.underlying_module_morphism()

    assert doubling.domain() is module
    assert doubling.codomain() is module
    assert doubling.parent().base_ring() is QQ
    assert doubling.parent().underlying_homset() is Modules(QQ).Mor(line, line)
    assert underlying.domain() is line
    assert underlying.codomain() is line
    assert underlying(line.module_generator(label)) == 2 * line.module_generator(label)


def test_exact_additive_scalar_action_is_retained_as_the_defining_morphism() -> None:
    group = Groups.C(2)
    group_algebra = QQ[group]
    line = FreeModule(QQ, 1)
    additive_endomorphisms = AdditiveGroups().AdditiveCommutative().End(
        line.underlying_additive_group()
    )

    def scalar_image(scalar):
        coefficients = module_coefficients(scalar, group_algebra)

        def apply(vector):
            return sum(
                (
                    coefficient
                    * (vector if group_element == group.one() else -vector)
                    for group_element, coefficient in coefficients.items()
                ),
                line.zero(),
            )

        return additive_endomorphisms.elementwise(apply)

    rho = ring_morphism(group_algebra, additive_endomorphisms, scalar_image)
    module = Modules(group_algebra)(line, rho)

    assert module.scalar_action() is rho
    assert module.base_ring() is group_algebra
    assert module.scalar_restriction() is line


def test_selected_integral_presentation_belongs_to_the_scalar_restriction() -> None:
    group = Groups.C(2)
    group_algebra = ZZ[group]
    cyclic = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))
    module = Modules(group_algebra)(
        cyclic,
        lambda _group_element, vector: vector,
    )

    assert module.base_ring() is group_algebra
    assert module.scalar_restriction() is cyclic
    assert module.invariant_factors() == cyclic.invariant_factors()
    assert module.module_rank() == cyclic.module_rank()
    assert module.module_invariants() is cyclic
    assert module.module_coinvariants() is cyclic
