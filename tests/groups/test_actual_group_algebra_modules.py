r"""Actual ``R[G]`` module parents and their retained coefficient restrictions.

These assertions distinguish a module whose scalar ring is literally ``R[G]``
from an ``R``-module carrying an extra category annotation.  They are committed
unverified under the repository's terminal-T execution policy.
"""


from dzack_research.preamble.all import (
    GF,
    QQ,
    ZZ,
    Groups,
    Modules,
)
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
















def test_archived_action_matrix_and_splitting_field_are_owned_group_module_data() -> None:
    group, group_algebra, line, generator, module = _sign_module(QQ)
    category = Modules(group_algebra)

    action = module.action_of(generator)
    assert action.nrows() == 1
    assert action.ncols() == 1
    assert action[0, 0] == QQ(-1)
    assert category.splitting_field() is QQ
    assert category.is_split()

    cubic_group = Groups.C(3)
    cubic_category = Modules(QQ[cubic_group])
    assert cubic_category.splitting_field().degree() == 2
    assert not cubic_category.is_split()










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
