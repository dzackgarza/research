r"""One category of ``G``-objects in ``C``; ``G``-sets specialize it, and ``R[G]``-modules reach it by restriction along ``G -> R[G]``.

A ``G``-action on ``X`` in ``C`` is a group morphism ``G -> Aut_C(X)``; an
equivariant morphism is a morphism of ``C`` commuting with the actions.  The
specimens are the swap of two of three points and the regular representation
of ``S_3``.
"""

import pytest

from dzack_research.preamble.all import (
    QQ,
    Groups,
    Modules,
)




def _regular_representation(ring):
    r"""The free module on the elements of ``S_3``, acted on by left translation."""
    group = Groups.S(3)
    module = ring.free_module(tuple(group))

    def act(group_element, vector):
        return module.Mor(module)(
            {label: module.module_generator(group_element * label) for label in group}
        )(vector)

    return group, Modules(ring[group])(module, act)








def test_equivariant_module_maps_commute_with_the_actions() -> None:
    group, representation = _regular_representation(QQ)
    equivariant = Modules(QQ[group]).Mor(representation, representation)
    unit = representation.module_generator(group.one())
    total = sum(representation.module_generator(label) for label in group)
    averaging = equivariant({label: total for label in group})
    translate = representation.action_of(group.group_generators()[0])
    assert averaging(unit - translate(unit)) == representation.zero()
    assert averaging * averaging == 6 * averaging.underlying_arrow()
    with pytest.raises(ValueError):
        equivariant(
            {
                label: (2 if label == group.one() else 1) * representation.module_generator(label)
                for label in group
            }
        )
    assert representation.Mor(representation).identity() in equivariant
