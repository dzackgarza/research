r"""Adjunctions for the represented finite category of ``G``-sets.

For a finitely generated group acting on finite represented sets this module
implements

``(-)/G ⊣ Triv_G ⊣ (-)^G``.

When ``G`` itself is finite, the represented finite category is also closed
under the standard free and cofree constructions, giving

``G × - ⊣ U ⊣ Map(G,-)``.
"""

from sage.categories.cartesian_product import cartesian_product
from sage.categories.finite_enumerated_sets import FiniteEnumeratedSets
from sage.categories.homset import Hom
from sage.categories.morphism import SetMorphism
from sage.categories.sets_cat import Sets
from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.group.g_sets import (
    FiniteGSets,
    OrbitSet,
    _finite_g_set_from_action,
    fixed_point_set,
    g_set_homset,
    trivial_g_set,
)
from dzack_research.preamble.categories.group.groups import refine_group
from dzack_research.preamble.categories.sets import finite_ordered_set


class TrivialGSetFunctor(Functor):
    r"""``Triv_G : FinSet -> FinGSet_G``."""

    def __init__(self, group) -> None:
        self._group = refine_group(group)
        super().__init__(FiniteEnumeratedSets(), FiniteGSets(self._group))

    def group(self):
        return self._group

    def _apply_object(self, set_object):
        image = trivial_g_set(set_object, self.group())
        image._preamble_trivial_g_set_source_set = set_object
        return image

    def source_set(self, trivial_g_set_object):
        source = getattr(
            trivial_g_set_object,
            "_preamble_trivial_g_set_source_set",
            None,
        )
        if source is None:
            raise ValueError("the G-set is not an object produced by this trivial-action functor")
        return source

    def _apply_morphism(self, set_morphism):
        source = self(set_morphism.domain())
        target = self(set_morphism.codomain())
        return g_set_homset(source, target)(set_morphism)

    def _repr_(self):
        return f"Trivial {self.group()}-action on finite sets"


class GSetOrbitsFunctor(Functor):
    r"""``(-)/G : FinGSet_G -> FinSet``."""

    def __init__(self, group) -> None:
        self._group = refine_group(group)
        super().__init__(FiniteGSets(self._group), FiniteEnumeratedSets())

    def group(self):
        return self._group

    def _apply_object(self, g_set):
        return OrbitSet(g_set)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return SetMorphism(
            Hom(source, target, Sets()),
            lambda orbit: target.orbit_of(morphism(orbit.representative())),
        )

    def _repr_(self):
        return f"{self.group()}-orbit functor on finite G-sets"


class GSetFixedPointsFunctor(Functor):
    r"""``(-)^G : FinGSet_G -> FinSet``."""

    def __init__(self, group) -> None:
        self._group = refine_group(group)
        super().__init__(FiniteGSets(self._group), FiniteEnumeratedSets())

    def group(self):
        return self._group

    def _apply_object(self, g_set):
        return fixed_point_set(g_set)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return SetMorphism(Hom(source, target, Sets()), morphism)

    def _repr_(self):
        return f"{self.group()}-fixed-point functor on finite G-sets"


class GSetOrbitsTrivialAdjunction(Adjunction):
    r"""``(-)/G ⊣ Triv_G`` on represented finite ``G``-sets."""

    def __init__(self, group) -> None:
        group = refine_group(group)
        super().__init__(GSetOrbitsFunctor(group), TrivialGSetFunctor(group))

    def unit(self, g_set):
        orbit_set = self.left_adjoint()(g_set)
        trivial_orbits = self.right_adjoint()(orbit_set)
        return g_set_homset(g_set, trivial_orbits)(orbit_set.orbit_of)

    def counit(self, set_object):
        trivial = self.right_adjoint()(set_object)
        orbit_set = self.left_adjoint()(trivial)
        return SetMorphism(
            Hom(orbit_set, set_object, Sets()),
            lambda orbit: orbit.representative(),
        )

    def hom_set_isomorphism_forward(self, orbit_morphism):
        orbit_set = orbit_morphism.domain()
        g_set = orbit_set.g_set()
        trivial_target = self.right_adjoint()(orbit_morphism.codomain())
        return g_set_homset(g_set, trivial_target)(
            lambda point: orbit_morphism(orbit_set.orbit_of(point))
        )

    def hom_set_isomorphism_inverse(self, equivariant_morphism, codomain=None):
        trivial_target = equivariant_morphism.codomain()
        target = self.right_adjoint().source_set(trivial_target)
        if codomain is not None and codomain is not target:
            raise ValueError("the stated target is not the underlying trivial set")
        orbit_set = self.left_adjoint()(equivariant_morphism.domain())
        return SetMorphism(
            Hom(orbit_set, target, Sets()),
            lambda orbit: equivariant_morphism(orbit.representative()),
        )


class GSetTrivialFixedAdjunction(Adjunction):
    r"""``Triv_G ⊣ (-)^G`` on represented finite ``G``-sets."""

    def __init__(self, group) -> None:
        group = refine_group(group)
        super().__init__(TrivialGSetFunctor(group), GSetFixedPointsFunctor(group))

    def unit(self, set_object):
        trivial = self.left_adjoint()(set_object)
        fixed = self.right_adjoint()(trivial)
        return SetMorphism(Hom(set_object, fixed, Sets()), lambda point: point)

    def counit(self, g_set):
        fixed = self.right_adjoint()(g_set)
        trivial_fixed = self.left_adjoint()(fixed)
        return g_set_homset(trivial_fixed, g_set)(lambda point: point)

    def hom_set_isomorphism_forward(self, equivariant_morphism):
        source = self.left_adjoint().source_set(equivariant_morphism.domain())
        fixed = self.right_adjoint()(equivariant_morphism.codomain())
        return SetMorphism(
            Hom(source, fixed, Sets()),
            lambda point: equivariant_morphism(point),
        )

    def hom_set_isomorphism_inverse(self, fixed_morphism, codomain=None):
        if codomain is None:
            raise ValueError(
                "the acted codomain is required because a fixed-point set does not determine its source G-set"
            )
        g_set = codomain
        fixed = self.right_adjoint()(g_set)
        if fixed_morphism.codomain() is not fixed:
            raise ValueError("the set morphism must land in the fixed points of the stated G-set")
        trivial_source = self.left_adjoint()(fixed_morphism.domain())
        return g_set_homset(trivial_source, g_set)(fixed_morphism)


class FreeGSetFunctor(Functor):
    r"""``G × - : FinSet -> FinGSet_G`` with left translation on ``G``."""

    def __init__(self, group) -> None:
        self._group = refine_group(group)
        if self._group.is_finite() is not True:
            raise NotImplementedError(
                "the represented finite free G-set functor requires the acting group finite"
            )
        super().__init__(FiniteEnumeratedSets(), FiniteGSets(self._group))

    def group(self):
        return self._group

    def _apply_object(self, set_object):
        point_set = cartesian_product([self.group(), set_object])

        def action(group_element, point):
            return point_set((group_element * point[0], point[1]))

        image = _finite_g_set_from_action(self.group(), point_set, action)
        image._preamble_free_g_set_source_set = set_object
        return image

    def source_set(self, free_g_set):
        source = getattr(free_g_set, "_preamble_free_g_set_source_set", None)
        if source is None:
            raise ValueError("the G-set is not an object produced by this free G-set functor")
        return source

    def free_point(self, free_g_set, group_element, point):
        return free_g_set.point_set()((group_element, point))

    def _apply_morphism(self, set_morphism):
        source = self(set_morphism.domain())
        target = self(set_morphism.codomain())
        return g_set_homset(source, target)(
            lambda point: self.free_point(target, point[0], set_morphism(point[1]))
        )

    def _repr_(self):
        return f"Free finite {self.group()}-set functor"


class UnderlyingFiniteGSetFunctor(Functor):
    r"""``U : FinGSet_G -> FinSet``."""

    _faithful = True

    def __init__(self, group) -> None:
        self._group = refine_group(group)
        super().__init__(FiniteGSets(self._group), FiniteEnumeratedSets())

    def group(self):
        return self._group

    def _apply_object(self, g_set):
        return g_set

    def _apply_morphism(self, morphism):
        return SetMorphism(Hom(morphism.domain(), morphism.codomain(), Sets()), morphism)

    def _repr_(self):
        return f"Underlying finite-set functor on {self.group()}-sets"


class CofreeGSetFunctor(Functor):
    r"""``Map(G,-) : FinSet -> FinGSet_G`` with ``(a f)(h)=f(h a)``."""

    def __init__(self, group) -> None:
        self._group = refine_group(group)
        if self._group.is_finite() is not True:
            raise NotImplementedError(
                "the represented finite cofree G-set functor requires the acting group finite"
            )
        self._group_points = finite_ordered_set(self._group)
        super().__init__(FiniteEnumeratedSets(), FiniteGSets(self._group))

    def group(self):
        return self._group

    def group_points(self):
        return self._group_points

    def _function_value_in_point_set(self, function_point, group_element):
        return function_point[self.group_points().position(group_element)]

    def _function_point_in_point_set(self, point_set, function):
        return point_set(tuple(function(group_element) for group_element in self.group_points()))

    def _apply_object(self, set_object):
        point_set = cartesian_product(
            [set_object for _group_element in self.group_points()]
        )

        def action(group_element, function_point):
            return self._function_point_in_point_set(
                point_set,
                lambda argument: self._function_value_in_point_set(
                    function_point, argument * group_element
                ),
            )

        image = _finite_g_set_from_action(self.group(), point_set, action)
        image._preamble_cofree_g_set_source_set = set_object
        return image

    def source_set(self, cofree_g_set):
        source = getattr(cofree_g_set, "_preamble_cofree_g_set_source_set", None)
        if source is None:
            raise ValueError("the G-set is not an object produced by this cofree G-set functor")
        return source

    def function_value(self, cofree_g_set, function_point, group_element):
        if function_point not in cofree_g_set:
            raise TypeError("the function point belongs to a different cofree G-set")
        return self._function_value_in_point_set(function_point, group_element)

    def function_point(self, cofree_g_set, function):
        return self._function_point_in_point_set(cofree_g_set.point_set(), function)

    def _apply_morphism(self, set_morphism):
        source = self(set_morphism.domain())
        target = self(set_morphism.codomain())
        return g_set_homset(source, target)(
            lambda function_point: self.function_point(
                target,
                lambda group_element: set_morphism(
                    self.function_value(source, function_point, group_element)
                ),
            )
        )

    def _repr_(self):
        return f"Cofree finite {self.group()}-set functor"


class FreeGSetUnderlyingAdjunction(Adjunction):
    r"""``G × - ⊣ U`` on finite sets and represented finite ``G``-sets."""

    def __init__(self, group) -> None:
        group = refine_group(group)
        super().__init__(FreeGSetFunctor(group), UnderlyingFiniteGSetFunctor(group))

    def unit(self, set_object):
        free = self.left_adjoint()(set_object)
        return SetMorphism(
            Hom(set_object, free, Sets()),
            lambda point: self.left_adjoint().free_point(
                free, self.left_adjoint().group().one(), point
            ),
        )

    def counit(self, g_set):
        free = self.left_adjoint()(self.right_adjoint()(g_set))
        return g_set_homset(free, g_set)(
            lambda point: g_set.act(point[0], point[1])
        )

    def hom_set_isomorphism_forward(self, equivariant_morphism):
        free = equivariant_morphism.domain()
        source = self.left_adjoint().source_set(free)
        return SetMorphism(
            Hom(source, equivariant_morphism.codomain(), Sets()),
            lambda point: equivariant_morphism(
                self.left_adjoint().free_point(
                    free, self.left_adjoint().group().one(), point
                )
            ),
        )

    def hom_set_isomorphism_inverse(self, set_morphism, codomain=None):
        g_set = set_morphism.codomain() if codomain is None else codomain
        if set_morphism.codomain() is not g_set:
            raise ValueError("the set morphism must land in the underlying G-set")
        free = self.left_adjoint()(set_morphism.domain())
        return g_set_homset(free, g_set)(
            lambda point: g_set.act(point[0], set_morphism(point[1]))
        )


class UnderlyingCofreeGSetAdjunction(Adjunction):
    r"""``U ⊣ Map(G,-)`` on represented finite ``G``-sets."""

    def __init__(self, group) -> None:
        group = refine_group(group)
        super().__init__(UnderlyingFiniteGSetFunctor(group), CofreeGSetFunctor(group))

    def unit(self, g_set):
        cofree = self.right_adjoint()(self.left_adjoint()(g_set))
        return g_set_homset(g_set, cofree)(
            lambda point: self.right_adjoint().function_point(
                cofree,
                lambda group_element: g_set.act(group_element, point),
            )
        )

    def counit(self, set_object):
        cofree = self.right_adjoint()(set_object)
        return SetMorphism(
            Hom(cofree, set_object, Sets()),
            lambda function_point: self.right_adjoint().function_value(
                cofree,
                function_point,
                self.right_adjoint().group().one(),
            ),
        )

    def hom_set_isomorphism_forward(self, set_morphism):
        g_set = set_morphism.domain()
        cofree = self.right_adjoint()(set_morphism.codomain())
        return g_set_homset(g_set, cofree)(
            lambda point: self.right_adjoint().function_point(
                cofree,
                lambda group_element: set_morphism(
                    g_set.act(group_element, point)
                ),
            )
        )

    def hom_set_isomorphism_inverse(self, equivariant_morphism, codomain=None):
        cofree = equivariant_morphism.codomain()
        target = self.right_adjoint().source_set(cofree)
        if codomain is not None and codomain is not target:
            raise ValueError("the stated set is not the cofree construction target")
        return SetMorphism(
            Hom(equivariant_morphism.domain(), target, Sets()),
            lambda point: self.right_adjoint().function_value(
                cofree,
                equivariant_morphism(point),
                self.right_adjoint().group().one(),
            ),
        )


@cached_function
def g_set_orbits_trivial_adjunction(group) -> GSetOrbitsTrivialAdjunction:
    return GSetOrbitsTrivialAdjunction(group)


@cached_function
def g_set_trivial_fixed_adjunction(group) -> GSetTrivialFixedAdjunction:
    return GSetTrivialFixedAdjunction(group)


@cached_function
def free_g_set_underlying_adjunction(group) -> FreeGSetUnderlyingAdjunction:
    return FreeGSetUnderlyingAdjunction(group)


@cached_function
def underlying_cofree_g_set_adjunction(group) -> UnderlyingCofreeGSetAdjunction:
    return UnderlyingCofreeGSetAdjunction(group)


__all__ = [
    "CofreeGSetFunctor",
    "FreeGSetFunctor",
    "FreeGSetUnderlyingAdjunction",
    "GSetFixedPointsFunctor",
    "GSetOrbitsFunctor",
    "GSetOrbitsTrivialAdjunction",
    "GSetTrivialFixedAdjunction",
    "TrivialGSetFunctor",
    "UnderlyingCofreeGSetAdjunction",
    "UnderlyingFiniteGSetFunctor",
    "free_g_set_underlying_adjunction",
    "g_set_orbits_trivial_adjunction",
    "g_set_trivial_fixed_adjunction",
    "underlying_cofree_g_set_adjunction",
]
