r"""Finite represented ``G``-sets, their orbits, fixed points, and torsors.

A ``G``-set is an object of ``Sets()`` with a chosen ``G``-action, so its
category is ``GObjects(G, Sets())``.  The finite represented objects
additionally record the action as a group morphism ``G -> Sym(X)``, which is
the engine used to compute equivariance, fixed points, orbits, and the
standard finite free/cofree constructions.
"""

from sage.categories.category import Category
from sage.groups.perm_gps.permgroup_named import SymmetricGroup
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import parent as element_parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoryPacketMethods,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.group.g_objects import GObjectMor, GObjects
from dzack_research.preamble.categories.group.groups import (
    OwnedFiniteGroups,
    OwnedGroups,
    _engine_cosets,
    _engine_group,
    _engine_point,
    _integer_engine_point,
    _own_group,
    _owned_group,
    _owned_point,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
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
from dzack_research.preamble.logic import AtomicProposition, Unknown, ask
from dzack_research.preamble.owned_category import _object_of, owned_category_join
from dzack_research.preamble.validation import validator


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

    def underlying_category(self):
        r"""``FinSet``, the codomain of the forgetful functor."""
        return FiniteSets()

    # Functors out of finite G-sets, sited on their domain.

    @cached_method
    def forgetful_functor(self):
        r"""``U : FinGSet_G -> FinSet``, the underlying finite set of a finite ``G``-set."""
        from dzack_research.preamble.categories.functors.g_sets import (
            UnderlyingFiniteGSetFunctor,
        )

        return UnderlyingFiniteGSetFunctor(self.group())

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
            assert point_set in FiniteSets(), (
                f"cannot form a finite G-set on {point_set}: it is not a finite set, only "
                f"known to be in {point_set.category()}"
            )
            group = permutation_representation.domain()
            self._point_set = point_set
            self._permutation_representation = permutation_representation
            permutations = permutation_representation.codomain()

            def permute(group_element, point):
                permutation = permutations(permutation_representation(group_element))
                return _owned_point(permutation(_integer_engine_point(point)))

            def point_map(group_element):
                return lambda point: self(permute(group_element, point))

            super().__init__(
                acting_group=group,
                action=point_map,
                underlying_category=Sets(),
                facade=point_set,
                **rest,
            )
            self.validate_point_closure(check=False)

        @validator
        def validate_point_closure(self) -> None:
            r"""Raise ``ValueError`` unless ``G`` maps the point set into itself (``OWN-22``).

            The permutation representation ``G -> Sym(n)`` is a group
            morphism, so it restricts to an action on the point set ``X``
            exactly when ``X`` is stable under it.  Stability is decided on
            the chosen group generators, or on every element of a finite
            group without them.
            """
            group = self.acting_group()
            representation = self.permutation_representation()
            permutations = representation.codomain()
            match group:
                case _ if group.has_selected_group_resolution():
                    determining = group.group_generators()
                case _ if group.is_finite() is True:
                    determining = group
                case _:
                    assert False, (
                        f"cannot check that {representation} is an action of {group} on "
                        f"{self.point_set()}: {group} has no chosen group generators and is "
                        f"not known to be finite"
                    )
            for group_generator in determining:
                permutation = permutations(representation(group_generator))
                for point in self.point_set():
                    image = _owned_point(permutation(_integer_engine_point(point)))
                    if image not in self.point_set():
                        raise ValueError(
                            f"{representation} is not an action of {group} on "
                            f"{self.point_set()}: {group_generator} sends {point} outside it"
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

        def fixed_points(self):
            r"""The fixed-point set ``X^G``."""
            return FiniteGSets(self.acting_group()).fixed_points_functor()(self)

        @cached_method
        def _orbit_labels(self):
            r"""The rank of the first point of each point's orbit, keyed by the point's rank.

            The orbits are those of the image of ``G`` in ``Sym(X)``, which
            GAP computes from the images of the chosen group generators, or
            of every element of a finite group without them.
            """
            group = self.acting_group()
            match group:
                case _ if group.has_selected_group_resolution():
                    action_generators = group.group_generators()
                case _ if group.is_finite() is True:
                    action_generators = group
                case _:
                    assert False, (
                        f"cannot compute the orbits of {self}: the acting group {group} "
                        f"has no chosen group generators and is not known to be finite"
                    )
            ranking = self.ranking_map()
            representation = self.permutation_representation()
            image_group = representation.codomain().subgroup(
                tuple(representation(generator) for generator in action_generators)
            )
            image_engine = _engine_group(image_group)
            labels = {}
            for point in self:
                ranks = tuple(
                    int(ranking(_owned_point(image)))
                    for image in image_engine.orbit(_engine_point(image_engine, point))
                )
                labels[int(ranking(point))] = min(ranks)
            return labels

        def _orbit_relation_decision(self, source, target) -> bool:
            r"""Two points share an orbit exactly when their orbits have the same first point."""
            labels = self._orbit_labels()
            ranking = self.ranking_map()
            return labels[int(ranking(source))] == labels[int(ranking(target))]

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
                return AtomicProposition("is_free_action", self)
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
                raise ValueError(
                    f"no transporter from {source} to {target} in {self}: both must be "
                    f"points of {self.point_set()}"
                )
            group = self.acting_group()
            assert group.is_finite() is True, (
                f"cannot search for an element of {group} carrying {source} to {target}: "
                f"{group} is not known to be finite"
            )
            for group_element in group:
                if self.act(group_element, source) == target:
                    return group_element
            raise ValueError(
                f"{source} and {target} lie in different orbits of {self}: no element of "
                f"{group} carries {source} to {target}"
            )

        def transporter(self, source, target):
            r"""Return the unique transporter between two points of a torsor.

            A general action has a transporter *coset*, not a unique element.
            ``transporter_witness`` is the generic finite-action operation;
            this spelling is reserved for the torsor case.
            """
            if self.is_torsor() is not True:
                raise ValueError(
                    f"{self} is not known to be a torsor under {self.acting_group()} (a free "
                    f"transitive action), so the element carrying {source} to {target} is "
                    f"not unique; use transporter_witness() for one such element"
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


class LeftCosetGSets(OwnedParameterizedCategory):
    r"""The represented transitive left-coset ``G``-sets ``G/H``."""

    def parameter_category(self):
        from dzack_research.preamble.categories.group.groups import Subgroups

        subgroup = self.parameter()
        return Subgroups(subgroup.supergroup())

    def subgroup(self):
        return self.parameter()

    def super_categories(self):
        return [FiniteGSets(self.subgroup().supergroup())]

    def an_object(self):
        subgroup = self.subgroup()
        return _left_coset_g_set(subgroup.supergroup(), subgroup)

    class ParentMethods:
        def __init__(self, coset_subgroup, **rest) -> None:
            self._coset_subgroup = coset_subgroup
            super().__init__(**rest)

        def subgroup(self):
            r"""Return ``H <= G`` for this represented left-coset ``G/H``."""
            return self._coset_subgroup

        def coset_of(self, element):
            r"""Return the unique left coset containing ``element``."""
            group = self.acting_group()
            element = group(element)
            for coset in self.point_set():
                if element in coset:
                    return coset
            raise ArithmeticError(
                f"{element} belongs to no represented left coset of {self.subgroup()} in {group}"
            )

        def base_point(self):
            r"""Return the distinguished point ``H`` of ``G/H``."""
            return self.coset_of(self.acting_group().one())

        @cached_method
        def regular_g_set(self):
            r"""Return ``G`` with its left regular action."""
            group = self.acting_group()
            points = finite_ordered_set(tuple(group))
            return FiniteGSets(group)(
                points,
                lambda group_element, point: group_element * point,
            )

        @cached_method
        def projection(self):
            r"""Return the equivariant quotient map ``G -> G/H`` of left ``G``-sets."""
            regular = self.regular_g_set()
            return regular.Mor(self)(lambda element: self.coset_of(element))

        @cached_method
        def normal_quotient_comparison(self):
            r"""Return the canonical set isomorphism ``G/H ~= coker(H -> G)`` when ``H`` is normal."""
            inclusion = self.subgroup().inclusion()
            assert inclusion.is_normal(), (
                f"{self.subgroup()} is not normal in {self.acting_group()}, so {self} has no quotient-group structure"
            )
            quotient = inclusion.cokernel()
            quotient_projection = inclusion.cokernel_projection()
            forward = Sets().Mor(self, quotient)(
                lambda coset: quotient_projection(next(iter(coset)))
            )
            inverse = Sets().Mor(quotient, self)(
                lambda quotient_element: self.coset_of(
                    quotient_projection.lift(quotient_element)
                )
            )
            return Sets().Core().Mor(self, quotient)(forward, inverse)


class GSetMor(GObjectMor):
    r"""The equivariant Mor category between represented finite ``G``-sets.

    A morphism of finite ``G``-sets is a map of the underlying finite sets
    that commutes with the actions, so its arrow is the ``GObjects(G, Sets())``
    arrow threaded through the arrow of ``FiniteSets().Mor``.
    """


class _Orbit:
    r"""The orbit ``G . x`` of one point ``x``, a point of the orbit set ``X/G``.

    Two orbits are equal exactly when they meet, so the selected point
    ``x`` is a representative and not part of the orbit's identity.
    """

    def __init__(self, parent, representative) -> None:
        self._representative = representative
        super().__init__(parent)

    def representative(self):
        r"""The point this orbit was named by."""
        return self._representative

    def g_set(self):
        return self.parent().g_set()

    def acting_group(self):
        return self.g_set().acting_group()

    def _decided_orbit_relation(self, point) -> bool:
        r"""Whether ``point`` lies in this orbit, where the orbit relation of ``X`` decides it.

        Membership and equality of orbits answer ``True`` or ``False`` and
        nothing else, so they are exact operations on the relation, not
        predicates: where ``ask`` of the relation is ``Unknown`` they reach
        the assertion frontier (``CAT-01``, ``DEV-52``) and never answer
        ``False`` for a question no procedure decided.
        """
        g_set = self.g_set()
        relation = ask(g_set.in_same_orbit(self.representative(), point))
        assert relation is not Unknown, (
            f"whether {point} lies in the orbit of {self.representative()} under "
            f"{self.acting_group()} is defined, but no procedure supplied by {g_set} decides it"
        )
        return relation

    def __contains__(self, point) -> bool:
        return point in self.g_set() and self._decided_orbit_relation(point)

    @cached_method
    def points(self):
        r"""The subset ``G . x`` of ``X``, cut out by the orbit relation where it is decided."""
        return self.g_set().condition_set(self._decided_orbit_relation)

    def cardinality(self):
        r"""``|G . x| = [G : G_x]``, the index of the stabilizer of the representative.

        This is the orbit-stabilizer theorem.  On a finite set ``X`` the
        orbit is the subset of ``X`` cut out by the orbit relation, which
        the construction of a finite ``G``-set decides from the orbits of
        its chosen group generators, so its cardinality is read there.
        Otherwise it is the index of the stabilizer, which the category of
        the stabilizer computes (an open subgroup of a profinite group
        knows its index from the degree of its fixed field).
        """
        g_set = self.g_set()
        match g_set:
            case _ if g_set in FiniteSets():
                return self.points().cardinality()
            case _:
                return self.stabilizer().index()

    def stabilizer(self):
        r"""The stabilizer of the representative; other points have conjugate stabilizers."""
        return self.g_set().stabilizer(self.representative())

    def transporter_from(self, point):
        r"""One group element carrying ``point`` to the representative."""
        assert point in self, f"{point} is not a point of {self}"
        return self.g_set().transporter_witness(point, self.representative())

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        if element_parent(other) is not self.parent():
            return op == op_NE
        meet = self._decided_orbit_relation(other.representative())
        return meet if op == op_EQ else not meet

    def __hash__(self) -> int:
        # Equal orbits may have different representatives, and the orbit
        # set supplies no invariant of an orbit beyond its parent.
        return hash(id(self.parent()))

    def _repr_(self) -> str:
        return f"Orbit of {self.representative()} under {self.acting_group()}"


class _OrbitSet:
    r"""The orbit set ``X/G`` of a ``G``-set ``X``.

    It is the coequalizer in ``Sets()`` of the action and the projection
    ``G x X -> X``.  The datum is ``X``; a point is an orbit named by one of
    its points, and equality of orbits is the orbit relation of ``X``.
    """

    def __init__(self, g_set, **rest) -> None:
        self._g_set = g_set
        super().__init__(**rest)

    def g_set(self):
        return self._g_set

    def orbit_of(self, point):
        r"""The orbit ``G . point``, the image of ``point`` under the projection ``X -> X/G``."""
        assert point in self.g_set(), f"{point} is not a point of {self.g_set()}"
        return self.element_class(self, self.g_set()(point))

    @cached_method
    def projection(self):
        r"""The projection ``X -> X/G`` of the coequalizer."""
        return Sets().Mor(self.g_set(), self)(self.orbit_of)

    def __contains__(self, orbit) -> bool:
        return element_parent(orbit) is self

    def __call__(self, orbit):
        return self._element_constructor_(orbit)

    def _element_constructor_(self, orbit):
        assert orbit in self, f"{orbit} is not an orbit of {self}"
        return orbit

    @cached_method
    def _orbits(self):
        r"""One orbit through each point, the first time the points meet it."""
        g_set = self.g_set()
        assert g_set in FiniteSets(), (
            f"the orbits of {g_set} are listed only when it is a finite set"
        )
        found = []
        for point in g_set:
            orbit = self.orbit_of(point)
            if orbit not in found:
                found.append(orbit)
        return tuple(found)

    def __iter__(self):
        return iter(self._orbits())

    @cached_method
    def ranking_map(self):
        r"""The orbits in the order of their first points in the enumeration of ``X``."""
        orbits = self._orbits()
        return self._ranking_isomorphism(
            lambda orbit: orbits.index(self(orbit)),
            lambda position: orbits[position],
        )

    def _repr_(self) -> str:
        return f"Orbit set of {self.g_set()}"


def _orbit_set(g_set):
    r"""The orbit set ``X/G`` of the ``G``-set ``X``, finite and enumerated with ``X``."""
    match g_set:
        case _ if g_set in FiniteSets() and g_set in EnumeratedSets():
            category = owned_category_join((FiniteSets(), EnumeratedSets()))
        case _ if g_set in FiniteSets():
            category = FiniteSets()
        case _:
            category = Sets()
    return _object_of(category, _engine=(category, _OrbitSet, _Orbit), g_set=g_set)


class _GSetOnPoints:
    r"""A ``G``-set on a given set of points, with the procedure deciding its orbit relation.

    The data are the point set, the relation, a function of two points
    answering ``True``, ``False`` or ``Unknown``, and the stabilizer, a
    function naming the subgroup that fixes a point; the action is the
    ``GObjects`` datum.
    """

    def __init__(self, point_set, orbit_relation, stabilizer, **rest) -> None:
        self._point_set = point_set
        self._orbit_relation = orbit_relation
        self._stabilizer = stabilizer
        super().__init__(**rest)

    def point_set(self):
        return self._point_set

    def __contains__(self, point) -> bool:
        return point in self.point_set()

    is_parent_of = __contains__

    def __call__(self, point):
        return self._element_constructor_(point)

    def _element_constructor_(self, point):
        assert point in self.point_set(), f"{point!r} is not a point of {self}"
        return self.point_set()(point)

    def __iter__(self):
        return iter(self.point_set())

    def _orbit_relation_decision(self, source, target):
        return self._orbit_relation(source, target)

    def _named_stabilizer(self, point):
        return self._stabilizer(point)

    def _repr_(self) -> str:
        return f"{self.point_set()} with {self.acting_group()}-action"


def _g_set_on_points(group, point_set, action, orbit_relation, stabilizer):
    r"""The ``G``-set on ``point_set`` with the action ``action(g, x)``.

    ``orbit_relation(x, y)`` decides whether ``y in G . x``, answering
    ``Unknown`` where no procedure decides it.  ``stabilizer(x)`` is the
    subgroup ``G_x`` the action names: the centralizer of an element under
    conjugation, the normalizer of a subgroup under conjugation.
    """
    g_sets = GObjects(group, Sets())
    match point_set:
        case _ if point_set in FiniteSets():
            category = owned_category_join((g_sets, FiniteSets()))
        case _:
            category = g_sets
    return _object_of(
        category,
        _engine=(category, _GSetOnPoints, None),
        point_set=point_set,
        orbit_relation=orbit_relation,
        stabilizer=stabilizer,
        acting_group=group,
        action=lambda group_element: (lambda point: action(group_element, point)),
        underlying_category=Sets(),
        facade=point_set,
    )


def _permutation_from_point_map(permutation_group, point_set, mapping):
    images = [mapping(point) for point in point_set]
    for point in point_set:
        assert sum(image == point for image in images) == 1, (
            f"the map {mapping} on {point_set} is not a permutation: {point} has "
            f"{sum(image == point for image in images)} preimages, not exactly one"
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


def _finite_g_set_from_action(
    group,
    point_set,
    action,
    *,
    category=None,
    construction_data=None,
):
    r"""Construct a represented finite ``G``-set from a binary action.

    ``action(g, x)`` is read into the defining group morphism
    ``G -> Sym(X)``.  Chosen generators are used when present; otherwise a
    finite acting group is verified exhaustively.  The returned object stores
    that morphism rather than the temporary binary callback.
    """
    point_set = _owned_point_set(point_set)
    assert point_set in FiniteSets(), (
        f"cannot form a finite G-set on {point_set}: it is not a finite set, only "
        f"known to be in {point_set.category()}"
    )
    group = _owned_group(group)
    # Private finite backend serialization: Sage's SymmetricGroup constructor
    # requires a sliceable concrete domain of engine points, while the
    # mathematical point set remains the owned set above.
    backend_points = [_integer_engine_point(point) for point in point_set]
    permutations = _own_group(SymmetricGroup(backend_points))
    mor = group.Mor(permutations)
    match group:
        case _ if group.has_selected_group_resolution():
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
            permutation_representation = mor._from_elementwise_rule(
                lambda group_element: _permutation_from_point_map(
                    permutations,
                    point_set,
                    lambda point: action(group_element, point),
                )
            )
        case _:
            assert False, (
                f"cannot form the action of {group} on {point_set}: {group} has no chosen "
                f"group generators and is not known to be finite"
            )
    selected_category = (
        FiniteGSets(permutation_representation.domain())
        if category is None
        else category
    )
    return _object_of(
        selected_category,
        point_set=point_set,
        permutation_representation=permutation_representation,
        **dict(construction_data or {}),
    )


def _left_coset_g_set(group, subgroup):
    r"""Return ``G/H`` as its pointed transitive left ``G``-set."""
    group = _owned_group(group)
    if subgroup.supergroup() is not group:
        raise ValueError(
            f"cannot form left cosets of {subgroup} in {group}: the subgroup lies in {subgroup.supergroup()}"
        )
    cosets = _engine_cosets(group, subgroup, "left")

    def coset_of(element):
        element = group(element)
        for coset in cosets:
            if element in coset:
                return coset
        raise ArithmeticError(
            f"{element} belongs to no represented left coset of {subgroup} in {group}"
        )

    return _finite_g_set_from_action(
        group,
        cosets,
        lambda group_element, coset: coset_of(
            group_element * next(iter(coset))
        ),
        category=LeftCosetGSets(subgroup),
        construction_data={"coset_subgroup": subgroup},
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

    def an_object(self):
        r"""The regular torsor of a represented finite acting group."""
        group = self.group()
        assert group in OwnedFiniteGroups(), (
            f"a torsor under {group} exists for every group, but the current finite-G-set realization can "
            "exhibit the regular torsor only when the acting group is represented as finite"
        )
        points = finite_ordered_set(tuple(group))
        return self(
            FiniteGSets(group)(
                points,
                lambda group_element, point: group_element * point,
            )
        )

    def super_categories(self):
        return [GObjects(self.group(), Sets())]

    def _repr_object_names(self):
        return f"torsors under {self.group()}"

    def _call_(self, candidate):
        finite_g_sets = FiniteGSets(self.group())
        if candidate not in finite_g_sets or candidate.is_torsor() is not True:
            raise ValueError(
                f"{candidate} is not a torsor under {self.group()}: it must be a finite "
                f"{self.group()}-set whose action is free and transitive"
            )
        return _object_of(
            owned_category_join((candidate.category(), self)),
            point_set=candidate.point_set(),
            permutation_representation=candidate.permutation_representation(),
        )

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
    "LeftCosetGSets",
    "GSetMor",
    "Torsors",
]
