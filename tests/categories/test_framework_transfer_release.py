r"""Released ``sage-categories`` supplies the transferred generic constructions.

This is the downstream acceptance edge for ``framework-transfer``: the pinned
Git dependency owns the selected sequential colimit and its morphism action.
The preamble does not rebuild that construction or its CAP polynomial-kernel
codec locally.
"""

from sympy import Q

from sage_categories import omega
from sage_categories.all import Fun, Mor, Sets, ask


def _integer_translation_diagram():
    integers = Sets.from_membership(lambda value: Q.integer(value))

    def stage(vertex):
        return vertex.point().datum()

    def transition(arrow):
        offset = stage(arrow.codomain()) - stage(arrow.domain())
        return Mor(Sets)(integers, integers)(
            lambda value, offset=offset: value + offset
        )

    return integers, Fun(omega, Sets)(lambda _vertex: integers, transition)


def test_released_indexed_colimit_carries_nonidentity_stagewise_shift() -> None:
    integers, diagram = _integer_translation_diagram()
    family = Sets.Colimits(omega)
    colimit = family(diagram)
    universal = family.universal_data(diagram)
    shift = Mor(Fun(omega, Sets))(diagram, diagram)(
        lambda _vertex: Mor(Sets)(integers, integers)(lambda value: value + 1)
    )

    induced = family.defining_functor().on_morphism(shift)

    assert induced.domain() is colimit
    assert induced.codomain() is colimit
    for stage_index, value in ((4, 9), (7, 12)):
        vertex = omega(stage_index)
        leg = universal.leg(vertex)
        representative = leg(integers.point(value))
        shifted = leg(integers.point(value + 1))
        assert ask(induced(representative) == shifted) is True
        assert ask(induced * leg == leg * shift.component(vertex)) is True
