r"""Actual ``R[G]`` module parents and their retained coefficient restrictions.

These assertions distinguish a module whose scalar ring is literally ``R[G]``
from an ``R``-module carrying an extra category annotation.  They are committed
unverified under the repository's terminal-T execution policy.
"""

import pytest

from dzack_research.preamble.all import (
    GF,
    QQ,
    ZZ,
    AdditiveGroups,
    FinitelyPresentedTorsionModules,
    Groups,
    Modules,
    Sets,
)
from dzack_research.preamble.categories.functors.group_actions import GroupActionFunctor
ARCHIVE_RECONCILIATION = {
    "archive_module": "preamble/categories/modules/group_modules/group_modules.sage",
    "live_owner": "src/dzack_research/preamble/categories/modules/group_modules/group_modules.py",
    "disposition": "reconciled-live-owner",
}


def _sign_module(ring):
    group = Groups.C(2)
    group_algebra = ring[group]
    line = ring.free_module(1)
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
    assert module.unformed_module() is line

    scalar_action = module.scalar_action()
    assert scalar_action.domain() is group_algebra
    assert scalar_action.codomain() is AdditiveGroups().AdditiveCommutative().End(
        line.underlying_additive_group()
    )
    group_scalar = group_algebra.module_generator(generator)
    assert module.scalar_multiple(group_scalar, vector) == module.act(generator, vector)

    assert line(vector) == line.module_generator(label)
    assert module(line(vector)) == vector
    assert module.module_rank() == line.module_rank()


def test_regular_representation_linearizes_left_multiplication_on_the_exact_carrier() -> None:
    group = Groups.S(3)
    group_algebra = QQ[group]
    regular = group_algebra.regular_representation()
    carrier = group_algebra.underlying_module()
    left, right = tuple(group.group_generators())[:2]

    assert regular in Modules(group_algebra)
    assert regular.unformed_module() is carrier
    assert regular.module_rank() == carrier.module_rank() == 6
    assert regular.action_of(left)(carrier.module_generator(right)) == (
        carrier.module_generator(left * right)
    )
    equipped_right = regular(carrier.module_generator(right))
    assert regular.act(left, equipped_right) == regular(
        carrier.module_generator(left * right)
    )


def test_group_module_retains_its_owned_set_carrier() -> None:
    _group, _group_algebra, line, _generator, module = _sign_module(QQ)
    label = line.module_generating_set()[0]
    assert module in Sets()
    equipped = module(line.module_generator(label))
    assert equipped.parent() is module
    assert line(equipped) == line.module_generator(label)


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
    line = QQ.free_module(1)
    additive_endomorphisms = AdditiveGroups().AdditiveCommutative().End(
        line.underlying_additive_group()
    )

    def scalar_image(scalar):
        coefficients = group_algebra.framing_coefficients(scalar)

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

    rho = group_algebra.Mor(additive_endomorphisms)(scalar_image)
    module = Modules(group_algebra)(line, rho)

    assert module.scalar_action() is rho
    assert module.base_ring() is group_algebra
    assert module.unformed_module() is line


def test_selected_integral_presentation_belongs_to_the_scalar_restriction() -> None:
    group = Groups.C(2)
    group_algebra = ZZ[group]
    cyclic = FinitelyPresentedTorsionModules(ZZ).direct_sum_of_cyclics((4,))
    module = Modules(group_algebra)(
        cyclic,
        lambda _group_element, vector: vector,
    )

    assert module.base_ring() is group_algebra
    assert module.unformed_module() is cyclic
    assert module.invariant_factors() == cyclic.invariant_factors()
    assert module.module_rank() == cyclic.module_rank()
    assert module.module_invariants() is cyclic
    assert module.module_coinvariants() is cyclic


def test_archived_action_matrix_and_splitting_field_are_owned_group_module_data() -> None:
    group, group_algebra, line, generator, module = _sign_module(QQ)
    category = Modules(group_algebra)

    assert module.action_matrix(generator).nrows() == 1
    assert module.action_matrix(generator).ncols() == 1
    assert module.action_matrix(generator)[0, 0] == QQ(-1)
    assert category.splitting_field() is QQ
    assert category.is_split()

    cubic_group = Groups.C(3)
    cubic_category = Modules(QQ[cubic_group])
    assert cubic_category.splitting_field().degree() == 2
    assert not cubic_category.is_split()


def test_nontrivial_sign_module_invariants_use_the_retained_action() -> None:
    _group, _group_algebra, line, _generator, module = _sign_module(QQ)
    label = line.module_generating_set()[0]
    vector = module.module_generator(label)
    invariants = module.module_invariants()

    assert not module.is_invariant(vector)
    assert module.is_invariant(module.zero())
    assert invariants.module_rank() == 0
    assert module.module_coinvariants().module_rank() == 0


def test_group_module_retains_one_supplied_action_functor() -> None:
    group = Groups.C(2)
    line = QQ.free_module(("e",))
    endomorphisms = Modules(QQ).Mor(line, line)
    identity = endomorphisms.identity()
    sign = endomorphisms({"e": -line.module_generator("e")})
    generator = group.group_generators()[0]
    action = GroupActionFunctor(
        group,
        Modules(QQ),
        line,
        lambda group_element: identity if group_element == group.one() else sign,
    )

    represented = Modules(QQ[group])(line, action)

    assert represented.action_functor() is action
    assert represented.action_of(generator) == sign


def test_group_module_rejects_generator_images_that_fail_the_group_relation() -> None:
    group = Groups.C(3)
    line = ZZ.free_module(("e",))

    def invalid_action(group_element, vector):
        return vector if group_element == group.one() else -vector

    with pytest.raises(AssertionError, match="relator"):
        Modules(ZZ[group])(line, invalid_action)


def test_nonequivariant_underlying_linear_map_is_not_a_group_module_morphism() -> None:
    group = Groups.C(2)
    line = ZZ.free_module(("e",))
    trivial = Modules(ZZ[group])(line, lambda _group_element, vector: vector)
    sign = Modules(ZZ[group])(
        line,
        lambda group_element, vector: (
            vector if group_element == group.one() else -vector
        ),
    )

    with pytest.raises(ValueError, match="not G-equivariant"):
        trivial.Mor(sign)({"e": sign.module_generator("e")})


def test_sign_and_trivial_actions_coincide_after_base_change_to_characteristic_two() -> None:
    group = Groups.C(2)
    generator = group.group_generators()[0]
    line = ZZ.free_module(("e",))
    trivial = Modules(ZZ[group])(line, lambda _group_element, vector: vector)
    sign = Modules(ZZ[group])(
        line,
        lambda group_element, vector: (
            vector if group_element == group.one() else -vector
        ),
    )
    assert trivial.action_of(generator) != sign.action_of(generator)

    field = GF(2)
    ring_map = ZZ.Mor(field)(lambda integer: field(integer))
    extension = Modules(ZZ[group]).coefficient_base_change_adjunction(
        ring_map
    ).left_adjoint()
    changed_trivial = extension(trivial)
    changed_sign = extension(sign)
    changed_module = changed_trivial.unformed_module()
    probe = changed_module.module_generator("e")

    assert changed_sign.unformed_module() is changed_module
    assert changed_trivial.action_of(generator) == changed_sign.action_of(generator)
    assert changed_trivial.is_trivial_action()
    assert changed_sign.is_trivial_action()
    assert changed_trivial.action_of(generator)(probe) == probe
    assert changed_sign.action_of(generator)(probe) == probe
