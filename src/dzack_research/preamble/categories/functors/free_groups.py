r"""The free-group/underlying-set adjunction ``F ⊣ U``.

Sage's indexed free group is the actual free group on an arbitrary Sage set.
The corresponding Hom-set is supplied by the owned group morphism layer, so
this functor does not choose names, enumerate the source, or pass through a
finite-rank GAP presentation.
"""

from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from dzack_research.preamble.categories.sets import Sets
from sage.groups.indexed_free_group import IndexedFreeGroup
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.group.group_morphisms import group_homset
from dzack_research.preamble.categories.group.groups import Groups, OwnedGroups


class FreeGroupFunctor(Functor):
    r"""``F : Set -> Grp`` using Sage's indexed free group."""

    def __init__(self) -> None:
        super().__init__(Sets(), OwnedGroups())

    def _apply_object(self, set_object):
        return Groups.Free(index_set=set_object)

    def source_set(self, free_group):
        if not isinstance(free_group, IndexedFreeGroup):
            raise TypeError("a free-group transpose requires an indexed free group")
        return free_group.indices()

    def _apply_morphism(self, set_morphism):
        source = self(set_morphism.domain())
        target = self(set_morphism.codomain())
        return group_homset(source, target)(
            SetMorphism(
                Sets().hom(source.indices(), target),
                lambda index: target.gen(set_morphism(index)),
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
        return SetMorphism(
            Sets().hom(group_morphism.domain(), group_morphism.codomain()),
            group_morphism,
        )

    def _repr_(self):
        return "Underlying-set functor on groups"


class FreeGroupUnderlyingSetAdjunction(Adjunction):
    r"""The adjunction ``F : Set <-> Grp : U``."""

    def __init__(self) -> None:
        super().__init__(FreeGroupFunctor(), GroupUnderlyingSetFunctor())

    def unit(self, set_object):
        free_group = self.left_adjoint()(set_object)
        return SetMorphism(
            Sets().hom(set_object, free_group),
            free_group.gen,
        )

    def counit(self, group):
        free_group = self.left_adjoint()(self.right_adjoint()(group))
        return group_homset(free_group, group)(
            SetMorphism(
                Sets().hom(free_group.indices(), group),
                lambda group_element: group_element,
            )
        )

    def hom_set_isomorphism_forward(self, group_morphism):
        free_group = group_morphism.domain()
        source = self.left_adjoint().source_set(free_group)
        return SetMorphism(
            Sets().hom(source, group_morphism.codomain()),
            lambda point: group_morphism(free_group.gen(point)),
        )

    def hom_set_isomorphism_inverse(self, set_morphism, codomain=None):
        group = set_morphism.codomain() if codomain is None else codomain
        if set_morphism.codomain() is not group:
            raise ValueError("the set morphism must land in the underlying group")
        free_group = self.left_adjoint()(set_morphism.domain())
        return group_homset(free_group, group)(
            SetMorphism(
                Sets().hom(free_group.indices(), group),
                set_morphism,
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
