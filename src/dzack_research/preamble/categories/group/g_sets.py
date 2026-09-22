r"""Finite represented ``G``-sets, their orbits, fixed points, and torsors.

A ``G``-set is an object of ``Sets()`` with a chosen ``G``-action, so its
category is ``GObjects(G, Sets())``.  The finite represented objects
additionally record the action as a group morphism ``G -> Sym(X)``, which is
the engine used to compute equivariance, fixed points, orbits, and the
standard finite free/cofree constructions.
"""

from sage.categories.morphism import SetMorphism
from sage.groups.perm_gps.permgroup_named import SymmetricGroup
from sage.misc.cachefunc import cached_method
from sage.misc.unknown import Unknown
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import Element

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoryPacketMethods,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.functors.core import NaturalTransformation
from dzack_research.preamble.categories.group.g_objects import GObjectMor, GObjects
from dzack_research.preamble.categories.group.groups import (
    OwnedGroups,
    _integer_engine_point,
    _own_group,
    _owned_group,
    _owned_point,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    FiniteOrderedSets,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import (
    EnumeratedSets,
    FiniteSets,
    Sets,
)
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.refine import refine


class GSetMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return GSetMor


class FiniteGSets(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""The represented finite objects of ``GObjects(G, Sets())``."""

    def parameter_category(self):
        r"""A finite ``G``-set is indexed by the acting group ``G``."""
        return OwnedGroups()

    def an_object(self):
        r"""The three-point set with the trivial action of the group."""
        from dzack_research.preamble.categories.sets.set_categories import (
            finite_ordinal_set,
        )

        return self.trivial(finite_ordinal_set(3))

    @staticmethod
    def __classcall__(cls, group):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(group))

    def __init__(self, group):
        OwnedParameterizedCategory.__init__(self, group)

    def _make_named_class_key(self, name):
        return self.group()

    def group(self):
        return self.parameter()

    acting_group = group

    def super_categories(self):
        return [GObjects(self.group(), Sets()), FiniteSets(), EnumeratedSets()]

    def _repr_object_names(self):
        return f"finite {self.group()}-sets"

    def _call_(self, point_set, action):
        r"""The finite ``G``-set on ``point_set`` with the action ``action(g, x)``."""
        return _finite_g_set_from_action(self.group(), point_set, action)

    def trivial(self, point_set):
        r"""Equip ``point_set`` with the trivial action of this category's group."""
        return self(point_set, lambda _group_element, point: point)

    # Functors out of finite G-sets, sited on their domain.

    @cached_method
    def orbits_functor(self):
        r"""``X |-> X/G : FinGSet_G -> FinSet``."""
        from dzack_research.preamble.categories.functors.g_sets import GSetOrbitsFunctor

        return GSetOrbitsFunctor(self.group())

    @cached_method
    def fixed_points_functor(self):
        r"""``X |-> X^G : FinGSet_G -> FinSet``."""
        from dzack_research.preamble.categories.functors.g_sets import (
            GSetFixedPointsFunctor,
        )

        return GSetFixedPointsFunctor(self.group())

    @cached_method
    def orbits_trivial_adjunction(self):
        r"""``(-)/G -| Triv_G``."""
        from dzack_research.preamble.categories.functors.g_sets import (
            _g_set_orbits_trivial_adjunction,
        )

        return _g_set_orbits_trivial_adjunction(self.group())

    @cached_method
    def underlying_cofree_adjunction(self):
        r"""``U -| Map(G, -)``: the underlying set is left adjoint to the cofree ``G``-set."""
        from dzack_research.preamble.categories.functors.g_sets import (
            _underlying_cofree_g_set_adjunction,
        )

        return _underlying_cofree_g_set_adjunction(self.group())

    _MorCategory = GSetMorCategoryConstruction

    class ParentMethods:
        _derived_construction_parameters = frozenset(
            {"acting_group", "action", "underlying_category"}
        )

        def __init__(self, point_set, permutation_representation, **rest) -> None:
            assert point_set in FiniteSets(), "a represented G-set is on a finite point set"
            group = permutation_representation.domain()
            self._point_set = point_set
            self._permutation_representation = permutation_representation
            permutations = permutation_representation.codomain()

            def permute(group_element, point):
                permutation = permutations(permutation_representation(group_element))
                return permutation(point)

            match group:
                case _ if group in OwnedGroups().Framed():
                    determining = group.group_generators()
                case _ if group.is_finite() is True:
                    determining = group
                case _:
                    assert False, (
                        "a represented finite G-set requires either selected group generators "
                        "or an exhaustively enumerable finite acting group"
                    )
            for group_generator in determining:
                for point in point_set:
                    assert permute(group_generator, point) in point_set, (
                        "the action morphism does not preserve the stated point set"
                    )

            def point_map(group_element):
                return lambda point: self(permute(group_element, point))

            super().__init__(
                acting_group=group,
                action=point_map,
                underlying_category=Sets(),
                facade=point_set,
                **rest,
            )

        def permutation_representation(self):
            r"""Return the chosen action as the group morphism ``G -> Sym(X)``."""
            return self._permutation_representation

        def point_set(self):
            r"""Return the finite set used to present the points of this ``G``-set."""
            return self._point_set

        def __iter__(self):
            return iter(self.point_set())

        def __contains__(self, point) -> bool:
            return point in self.point_set()

        is_parent_of = __contains__

        def __call__(self, point):
            return self._element_constructor_(point)

        def _element_constructor_(self, point):
            assert point in self.point_set(), f"{point!r} is not a point of {self}"
            return self.point_set()(point)

        def Mor(self, codomain):
            r"""Return the equivariant Mor from this G-set to ``codomain``."""
            return FiniteGSets(self.acting_group()).Mor(self, codomain)

        def orbits(self):
            r"""The orbit set ``X / G``."""
            return FiniteGSets(self.acting_group()).orbits_functor()(self)

        def fixed_points(self):
            r"""The fixed-point set ``X^G``."""
            return FiniteGSets(self.acting_group()).fixed_points_functor()(self)

        def stabilizer(self, point):
            r"""The subgroup ``G_point = {g in G : g.point = point}``.

            This is a predicate subgroup of the acting group.  Membership is
            exact from the represented action and does not require choosing
            generators for the stabilizer.
            """
            if point not in self:
                raise ValueError(f"{point} is not a point of {self}")
            from dzack_research.preamble.categories.group.predicate_subgroups import (
                StabilizerSubgroups,
            )

            group = self.acting_group()
            return StabilizerSubgroups(group)(
                point,
                "pointwise",
                lambda group_element: self.act(group_element, point) == point,
                description=f"stabilizer of {point} in {self}",
            )

        def orbit_stabilizers(self):
            r"""The family of point stabilizers indexed by the orbit classes."""
            orbits = self.orbits()
            return finite_indexed_family(
                orbits,
                lambda orbit: self.stabilizer(orbit.representative()),
                name=f"Orbit stabilizers of {self}",
            )

        def is_transitive_action(self) -> bool:
            r"""Whether the action has one orbit."""
            return bool(self.orbits().cardinality() == cardinal(1))

        def is_free_action(self):
            r"""Whether every point stabilizer is trivial, when decidable.

            A nonempty finite set cannot carry a free action of an infinite
            group.  For a finite acting group, direct finite enumeration is an
            exact decision procedure for the point-stabilizer condition.
            """
            group = self.acting_group()
            if group.is_finite() is False:
                return False
            if group.is_finite() is not True:
                return Unknown
            identity = group.one()
            return all(
                self.act(group_element, point) != point
                for point in self
                for group_element in group
                if group_element != identity
            )

        def is_torsor(self):
            r"""Whether this finite represented action is free and transitive."""
            free = self.is_free_action()
            if free is not True:
                return free
            return self.is_transitive_action()

        def transporter_witness(self, source, target):
            r"""Return one ``g`` with ``g.source = target`` when one exists."""
            if source not in self or target not in self:
                raise ValueError("a transporter requires two points of the G-set")
            group = self.acting_group()
            assert group.is_finite() is True, (
                "represented transporter search requires a finite acting group"
            )
            for group_element in group:
                if self.act(group_element, source) == target:
                    return group_element
            raise ValueError(f"no group element moves {source} to {target}")

        def transporter(self, source, target):
            r"""Return the unique transporter between two points of a torsor.

            A general action has a transporter *coset*, not a unique element.
            ``transporter_witness`` is the generic finite-action operation;
            this spelling is reserved for the torsor case.
            """
            if self.is_torsor() is not True:
                raise ValueError(
                    "a unique transporter is defined here only for a torsor; "
                    "use transporter_witness() for a general action"
                )
            return self.transporter_witness(source, target)

        @cached_method
        def ranking_map(self):
            r"""The point set's own enumeration, read on this $G$-set.

            An enumeration of the points is a bijection of sets and nothing
            more: it is not equivariant, since a group element moves a point
            to one of another position.
            """
            points = self.point_set().ranking_map()
            return self._ranking_isomorphism(points, points.inverse())

        def _repr_(self):
            return f"{self.point_set()} with {self.acting_group()}-action"


class GSetMorphism(SetMorphism):
    r"""A set map checked to commute with the represented group actions."""

    def __init__(self, parent, function) -> None:
        SetMorphism.__init__(self, parent, function)
        if parent.is_equivariant(self) is not True:
            raise ValueError("the stated set map is not G-equivariant")

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            lambda point: self(other(point))
        )

    def _as_set_map(self):
        r"""The same function read in ``Sets``, between the finite point sets."""
        return Sets().Mor(self.domain().point_set(), self.codomain().point_set())(
            lambda point: self(point)
        )

    def natural_transformation(self):
        r"""Return this equivariant map as the corresponding transformation ``BG => Set``."""
        source = self.domain().action_functor()
        target = self.codomain().action_functor()
        component = Sets().Mor(self.domain(), self.codomain())(
            lambda point: self(point)
        )
        return NaturalTransformation(
            source, target, lambda _obj: component
        ).morphism()

    def is_injective(self) -> bool:
        return self._as_set_map().is_injective()

    def is_surjective(self) -> bool:
        return self._as_set_map().is_surjective()


class GSetMor(GObjectMor):
    r"""The equivariant Mor category between represented finite ``G``-sets."""

    Element = GSetMorphism

    def _element_constructor_(self, function):
        return self.element_class(self, function)

    def identity(self):
        assert self.domain() is self.codomain(), "identity is defined on an endomorphism Mor object"
        return self(lambda point: point)


class OrbitSets(OwnedCategory):
    r"""The finite orbit quotients \(X/G\) of a finite \(G\)-set."""

    def an_object(self):
        r"""The orbits of a trivial action on three points."""
        from dzack_research.preamble.categories.group.groups import Groups

        group = Groups.S(3)
        return FiniteGSets(group).orbits_trivial_adjunction().left_adjoint()(
            FiniteGSets(group).trivial(Sets.Δ[2])
        )

    def super_categories(self):
        return [FiniteSets()]

    class ElementMethods(Element):
        r"""What an orbit is."""

        def __init__(self, parent, index) -> None:
            Element.__init__(self, parent)
            self._index = index

        def representative(self):
            return self.parent().orbit_points(self)[0]

        def points(self):
            return self.parent().orbit_points(self)

        elements = points
        members = points

        def acting_group(self):
            return self.parent().g_set().acting_group()

        group = acting_group
        supergroup = acting_group

        def __contains__(self, point) -> bool:
            return point in self.points()

        def stabilizer(self):
            r"""Return the stabilizer of the selected representative."""
            return self.parent().g_set().stabilizer(self.representative())

        def transporter_from(self, point):
            r"""Return one group element carrying ``point`` to the representative."""
            if point not in self:
                return None
            return self.parent().g_set().transporter_witness(
                point,
                self.representative(),
            )

        def __eq__(self, other) -> bool:
            return other in self.parent() and other._index == self._index

        def __ne__(self, other) -> bool:
            return not self == other

        def __hash__(self):
            return hash((id(self.parent()), self._index))

        def _repr_(self):
            return "Orbit(" + ", ".join(repr(point) for point in self.points()) + ")"

    class ParentMethods:
        def __init__(self, g_set, **rest) -> None:
            self._g_set = g_set
            group = g_set.acting_group()
            match group:
                case _ if group in OwnedGroups().Framed():
                    action_generators = group.group_generators()
                case _ if group.is_finite() is True:
                    action_generators = group
                case _:
                    assert False, (
                        "constructing finite orbits requires selected generators or an exhaustively enumerable finite acting group"
                    )

            point_set = finite_ordered_set(g_set)
            point_ranking = point_set.ranking_map()
            point_at = point_ranking.inverse()
            representation = g_set.permutation_representation()
            permutation_group = representation.codomain()
            image_group = permutation_group.subgroup(
                tuple(representation(generator) for generator in action_generators)
            )
            orbit_rank_sets = sorted(
                {
                    tuple(
                        sorted(
                            int(point_ranking(image))
                            for image in image_group.orbit(point)
                        )
                    )
                    for point in point_set
                },
                key=lambda orbit: orbit[0],
            )
            orbit_families = {
                orbit_index: FiniteOrderedSets().from_indexed(
                    Sets.Δ[len(orbit_ranks) - 1],
                    lambda position, orbit_ranks=orbit_ranks: point_at(
                        orbit_ranks[int(position)]
                    ),
                    name=f"Orbit {orbit_index}",
                )
                for orbit_index, orbit_ranks in enumerate(orbit_rank_sets)
            }
            orbit_count = len(orbit_rank_sets)

            self._orbit_indices = Sets.Δ[orbit_count - 1]
            self._orbit_points = finite_indexed_family(
                self._orbit_indices,
                lambda index: orbit_families[int(index)],
                name="Orbit point families",
            )
            super().__init__(**rest)
            self._orbit_classes = FiniteOrderedSets().from_indexed(
                self._orbit_indices,
                lambda index: self.element_class(self, index),
                name="Orbit classes",
            )

        def g_set(self):
            return self._g_set

        def __iter__(self):
            return iter(self._orbit_classes)

        def __contains__(self, orbit) -> bool:
            return isinstance(orbit, Element) and orbit.parent() is self

        def _element_constructor_(self, orbit):
            assert orbit in self, f"{orbit} is not an orbit of {self}"
            return orbit

        @cached_method
        def ranking_map(self):
            r"""The enumeration the orbit classes were built with."""

            def position_of(orbit):
                assert orbit in self, f"{orbit} is not an orbit of {self}"
                return int(orbit._index)

            return self._ranking_isomorphism(
                position_of, self._orbit_classes.ranking_map().inverse()
            )

        def orbit_points(self, orbit):
            assert orbit in self, "the orbit class belongs to a different quotient"
            return self._orbit_points[orbit._index]

        def orbit_of(self, point):
            assert point in self.g_set(), f"{point} is not a point of {self.g_set()}"
            for orbit in self:
                if point in self.orbit_points(orbit):
                    return orbit
            raise AssertionError("every point of a finite G-set belongs to an orbit")

        def _repr_(self):
            return f"Orbit set of {self.g_set()}"


def _permutation_from_point_map(permutation_group, point_set, mapping):
    images = [mapping(point) for point in point_set]
    for point in point_set:
        assert sum(image == point for image in images) == 1, (
            "a group action must send each group element to a permutation"
        )

    return permutation_group(
        [_integer_engine_point(image) for image in images]
    )


def _owned_point_set(point_set):
    r"""Read a literal family of points as an owned finite ordered set.

    Literal ingress adapter: an owned set is already the point set; a Python
    tuple or list is read entry by entry, and a point written as a Python
    ``int`` is the owned integer, the same point a permutation group's
    elements return.
    """
    if point_set in FiniteSets():
        return point_set
    integers = _own_ring(SageZZ)
    def own_point(point):
        match point:
            case int():
                return integers(point)
            case _:
                return point

    return finite_ordered_set(tuple(own_point(point) for point in point_set))


def _finite_g_set_from_action(group, point_set, action):
    r"""Construct a represented finite ``G``-set from a binary action.

    ``action(g, x)`` is read into the defining group morphism
    ``G -> Sym(X)``.  Chosen generators are used when present; otherwise a
    finite acting group is verified exhaustively.  The returned object stores
    that morphism rather than the temporary binary callback.
    """
    point_set = _owned_point_set(point_set)
    assert point_set in FiniteSets(), (
        "the represented G-set constructor requires a finite point set"
    )
    group = _owned_group(group)
    # Private finite backend serialization: Sage's SymmetricGroup constructor
    # requires a sliceable concrete domain of engine points, while the
    # mathematical point set remains the owned set above.
    backend_points = [_integer_engine_point(point) for point in point_set]
    permutations = _own_group(SymmetricGroup(backend_points))
    mor = group.Mor(permutations)
    match group:
        case _ if group in OwnedGroups().Framed():
            permutation_representation = mor(
                {
                    group_generator: _permutation_from_point_map(
                        permutations,
                        point_set,
                        lambda point, group_generator=group_generator: action(group_generator, point),
                    )
                    for group_generator in group.group_generators()
                }
            )
        case _ if group.is_finite() is True:
            permutation_representation = mor._from_finite_elementwise_rule(
                lambda group_element: _permutation_from_point_map(
                    permutations,
                    point_set,
                    lambda point: action(group_element, point),
                )
            )
        case _:
            assert False, (
                "a represented finite G-set requires selected generators or an exhaustively enumerable finite acting group"
            )
    return _object_of(
        FiniteGSets(permutation_representation.domain()),
        point_set=point_set,
        permutation_representation=permutation_representation,
    )


def _fixed_point_set(g_set):
    r"""Return the finite fixed-point set ``X^G``."""
    return finite_ordered_set(g_set).filtered(g_set.is_invariant)


class Torsors(OwnedParameterizedCategory):
    r"""The owned category of free transitive ``G``-sets."""

    @staticmethod
    def __classcall__(cls, group):
        return OwnedParameterizedCategory.__classcall__(cls, _owned_group(group))

    def parameter_category(self):
        r"""A torsor is parameterized by its actual acting group ``G``."""
        return OwnedGroups()

    def group(self):
        return self.base()

    acting_group = group

    def super_categories(self):
        return [GObjects(self.group(), Sets())]

    def _repr_object_names(self):
        return f"torsors under {self.group()}"

    def __contains__(self, candidate) -> bool:
        if candidate not in FiniteGSets(self.group()):
            return False
        return candidate.is_torsor() is True

    def _call_(self, candidate):
        if candidate not in self:
            raise ValueError(f"{candidate} is not a torsor under {self.group()}")
        return refine(candidate, self)

    class ParentMethods:
        def an_element(self):
            r"""Return the selected point trivializing this represented torsor.

            A torsor has no canonical point.  The represented finite ``G``-set
            already carries an ordered point set, so its first point is the
            presentation's selected trivializing choice.
            """
            return next(iter(self.point_set()))

        def __iter__(self):
            r"""Enumerate through a chosen point and the free transitive action."""
            chosen = self.an_element()
            return (
                self.act(group_element, chosen)
                for group_element in self.acting_group()
            )

        def cardinality(self):
            r"""``|T| = |G|`` for a ``G``-torsor."""
            return self.acting_group().cardinality()


__all__ = [
    "FiniteGSets",
    "GSetMor",
    "GSetMorphism",
    "OrbitSets",
    "Torsors",
]
