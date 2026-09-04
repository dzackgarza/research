r"""The free-group/underlying-set adjunction ``F ⊣ U``.

The free group on an arbitrary set is an owned group carrying its chosen free
basis.  The corresponding Hom-set is supplied by the owned group morphism
layer, so this functor does not choose names, enumerate the source, or pass
through a finite-rank GAP presentation.
"""

from sage.categories.morphism import SetMorphism
from dzack_research.preamble.categories.sets.set_categories import Sets
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.group.groups import group_homset
from dzack_research.preamble.categories.group.groups import (
    Groups,
    GroupsWithChosenFreeBasis,
    OwnedGroups,
)


class FreeGroupFunctor(Functor):
    r"""``F : Set -> Grp``."""

    def __init__(self) -> None:
        super().__init__(Sets(), OwnedGroups())

    def _apply_object(self, set_object):
        return Groups.Free(index_set=set_object)

    def source_set(self, free_group):
        if free_group not in GroupsWithChosenFreeBasis():
            raise TypeError("a free-group transpose requires a free group with a chosen basis")
        return free_group.free_basis()

    chosen_preimage = source_set

    def _apply_morphism(self, set_morphism):
        source = self(set_morphism.domain())
        target = self(set_morphism.codomain())
        return group_homset(source, target)(
            SetMorphism(
                Sets().hom(source.free_basis(), target),
                lambda index: target.free_generator(set_morphism(index)),
            )
        )

    def _repr_(self):
        return "Free-group functor"


class GroupUnderlyingSetFunctor(Functor):
    r"""``U : Grp -> Set``."""

    _faithful = True

    def __init__(self) -> None:
        super().__init__(OwnedGroups(), Sets())

    def _apply_object(self, group):
        return group

    def _apply_morphism(self, group_morphism):
        return Sets().hom(
            group_morphism.domain(),
            group_morphism.codomain(),
        )(group_morphism)

    def chosen_preimage(self, image):
        if image not in self.domain():
            raise ValueError("the underlying set is not an owned group")
        return image

    def _repr_(self):
        return "Underlying-set functor on groups"


class FreeGroupUnderlyingSetAdjunction(Adjunction):
    r"""The adjunction ``F : Set <-> Grp : U``."""

    def __init__(self) -> None:
        super().__init__(FreeGroupFunctor(), GroupUnderlyingSetFunctor())

    def unit(self, set_object):
        free_group = self.left_adjoint()(set_object)
        return Sets().hom(set_object, free_group)(free_group.free_generator)

    def counit(self, group):
        free_group = self.left_adjoint()(self.right_adjoint()(group))
        return group_homset(free_group, group)(
            SetMorphism(
                Sets().hom(free_group.free_basis(), group),
                lambda group_element: group_element,
            )
        )



@cached_function
def free_group_underlying_set_adjunction() -> FreeGroupUnderlyingSetAdjunction:
    return FreeGroupUnderlyingSetAdjunction()


__all__ = [
    "FreeGroupFunctor",
    "FreeGroupUnderlyingSetAdjunction",
    "GroupUnderlyingSetFunctor",
    "free_group_underlying_set_adjunction",
]
