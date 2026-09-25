r"""Positive-cone components and their projectivized hyperbolic geometry."""

from itertools import count, product

from sage.arith.misc import gcd
from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import Element
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.objects import OwnedParameterizedCategory
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.rings.real import RR


def _real_ambient_vector(lattice, ambient, vector):
    match element_parent(vector):
        case parent if parent is ambient:
            return vector
        case parent if parent is lattice:
            coordinates = vector.to_vector()
            return ambient.linear_combination(
                {
                    label: RR(coordinates(label))
                    for label in coordinates.support().domain()
                }
            )
        case _:
            return ambient(vector)


def _real_pairing(lattice, ambient, left, right):
    left = _real_ambient_vector(lattice, ambient, left)
    right = _real_ambient_vector(lattice, ambient, right)
    labels = tuple(lattice.module_generating_set())
    left_coordinates = left.to_vector()
    right_coordinates = right.to_vector()
    zero = RR.zero()
    return sum(
        (
            left_coordinates(left_label)
            * right_coordinates(right_label)
            * RR(
                lattice.b(
                    lattice.module_generator(left_label),
                    lattice.module_generator(right_label),
                )
            )
            for left_label in labels
            for right_label in labels
        ),
        zero,
    )


def _positive_component_contains(lattice, ambient, timelike, vector, *, closure=False) -> bool:
    vector = _real_ambient_vector(lattice, ambient, vector)
    square = _real_pairing(lattice, ambient, vector, vector)
    pairing = _real_pairing(lattice, ambient, vector, timelike)
    match closure:
        case True:
            return square >= RR.zero() and pairing >= RR.zero()
        case False:
            return square > RR.zero() and pairing > RR.zero()


def _timelike_witness(lattice):
    r"""Find an integral vector in the nonempty positive cone of a ``(1,n)`` lattice."""
    assert lattice.module_rank().is_finite(), (
        f"cannot search {lattice} for a vector of positive square: the search needs a "
        f"lattice of finite rank, and {lattice} has rank {lattice.module_rank()}"
    )
    rank = int(lattice.module_rank())
    for height in count(1):
        for coordinates in product(range(-height, height + 1), repeat=rank):
            match max((abs(value) for value in coordinates), default=0) == height:
                case False:
                    continue
                case True:
                    vector = lattice(coordinates)
                    match lattice.q(vector) > lattice.base_ring().zero():
                        case True:
                            return vector
                        case False:
                            pass


class _HyperbolicTopologyData(SageObject):
    r"""Private standard topology of one represented hyperbolic projectivization."""

    def open_subsets(self, space):
        return space.power_set().condition_set(
            lambda subset: self.is_open_subset(space, subset)
        )

    def is_open_subset(self, space, subset) -> bool:
        power = space.power_set()
        selected = power(subset)
        match selected:
            case _ if selected == power.bottom():
                return True
            case _ if selected == power.top():
                return True
            case _:
                assert False, (
                    f"cannot decide whether {selected} is open in the hyperbolic space "
                    f"{space}: openness is decided only for the empty set and the whole "
                    f"space"
                )


def _primitive_on_selected_ray(lattice, vector, timelike):
    vector = lattice(vector)
    vector_coordinates = vector.to_vector()
    coordinates = tuple(
        int(vector_coordinates(label))
        for label in lattice.module_generating_set()
    )
    nonzero_coordinates = tuple(abs(entry) for entry in coordinates if entry)
    if not nonzero_coordinates:
        raise ValueError(
            f"the zero vector of {lattice} spans no ray: a point of a projective space is "
            f"the ray of a nonzero vector"
        )
    content = gcd(nonzero_coordinates)
    primitive = lattice(tuple(entry // content for entry in coordinates))
    if lattice.b(primitive, timelike) < 0:
        primitive = -primitive
    return primitive


class PositiveConeComponents(OwnedParameterizedCategory):
    r"""Chosen components of ``{x : q(x)>0}`` for lattices of signature ``(1,n)``."""

    def __init__(self, lattice) -> None:
        signature = lattice.signature_pair()
        assert int(signature.first()) == 1 and int(signature.second()) >= 1, (
            f"{lattice} has no category of positive-cone components: it must have "
            f"signature (1, n) with n >= 1, but its signature is {signature}"
        )
        super().__init__(lattice)

    def parameter_category(self):
        from dzack_research.preamble.categories.lattices import Lattices

        return Lattices(_own_ring(SageZZ))

    def lattice(self):
        return self.base()

    @cached_method
    def ambient_space(self):
        return RR.free_module(self.lattice().module_generating_set())

    @classmethod
    def _repr_object_names(cls):
        return "positive-cone components"

    def super_categories(self):
        return [Sets().Subobjects(self.ambient_space())]

    def an_object(self):
        return _positive_cone_component(self.lattice(), _timelike_witness(self.lattice()))

    class ParentMethods:
        def __init__(self, lattice, timelike, **rest) -> None:
            signature = lattice.signature_pair()
            if int(signature.first()) != 1 or int(signature.second()) < 1:
                raise ValueError(
                    f"cannot select a component of the positive cone of {lattice}: the "
                    f"lattice must have signature (1, n) with n >= 1, but its signature "
                    f"is {signature}"
                )
            timelike = lattice(timelike)
            if lattice.q(timelike) <= 0:
                raise ValueError(
                    f"{timelike} cannot select a component of the positive cone of "
                    f"{lattice}: it must have positive square, but q = {lattice.q(timelike)}"
                )
            self._lattice = lattice
            self._timelike = timelike
            super().__init__(**rest)

        def lattice(self):
            return self._lattice

        def ambient_space(self):
            return self.codomain()

        def timelike_vector(self):
            return self._timelike

        def contains(self, vector) -> bool:
            return _positive_component_contains(
                self.lattice(),
                self.ambient_space(),
                self.timelike_vector(),
                vector,
            )

        def closure_contains(self, vector) -> bool:
            return _positive_component_contains(
                self.lattice(),
                self.ambient_space(),
                self.timelike_vector(),
                vector,
                closure=True,
            )

        def opposite(self):
            return _positive_cone_component(self.lattice(), -self.timelike_vector())

        @cached_method
        def projectivization(self):
            return _hyperbolic_space(self)

        def _repr_(self):
            return f"Positive-cone component of {self.lattice()} selected by {self.timelike_vector()}"


class HyperbolicSpaces(OwnedParameterizedCategory):
    r"""Projectivizations of chosen positive-cone components."""

    def parameter_category(self):
        component = self.parameter()
        return PositiveConeComponents(component.lattice())

    def positive_cone_component(self):
        return self.base()

    @classmethod
    def _repr_object_names(cls):
        return "hyperbolic spaces"

    def super_categories(self):
        return [TopologicalSpaces()]

    def an_object(self):
        return _hyperbolic_space(self.positive_cone_component())

    class ElementMethods(Element):
        r"""A rational point of a hyperbolic space: the ray of a positive vector of the component."""

        def __init__(self, parent: Parent, representative) -> None:
            Element.__init__(self, parent)
            self._representative = representative

        def representative(self):
            r"""Return the primitive lattice vector on the ray, pairing positively with the timelike vector."""
            return self._representative

        def __eq__(self, other) -> bool:
            return (
                element_parent(other) is self.parent()
                and other.representative() == self.representative()
            )

        def __ne__(self, other) -> bool:
            return not self == other

        def __hash__(self) -> int:
            return hash((id(self.parent()), self.representative()))

        def _repr_(self) -> str:
            return f"hyperbolic point [{self.representative()}]"

    class ParentMethods:
        def __init__(self, component, **rest) -> None:
            self._component = component
            super().__init__(**rest)

        def positive_cone_component(self):
            return self._component

        def lattice(self):
            return self._component.lattice()

        def __contains__(self, datum) -> bool:
            match element_parent(datum):
                case parent if parent is self:
                    return True
                case parent if parent is self.lattice():
                    return self._component.contains(datum)
                case _:
                    return False

        is_parent_of = __contains__

        def __call__(self, *args, **kwargs):
            r"""Construct a point through the owned element construction directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, datum):
            r"""Return the point on the ray of ``datum``, a positive vector of the component or a point of this space."""
            match datum:
                case _ if element_parent(datum) is self:
                    return datum
                case _:
                    assert self._component.contains(datum), (
                        f"{datum} does not define a point of {self}: a rational point is "
                        f"the ray of a vector of positive square in {self._component}, "
                        f"and {datum} is not in that component"
                    )
                    return self.element_class(
                        self,
                        _primitive_on_selected_ray(
                            self.lattice(), datum, self._component.timelike_vector()
                        ),
                    )

        def rational_point(self, vector):
            return self(vector)

        def ideal_point(self, vector):
            r"""Return the point at infinity on the ray of the isotropic ``vector``.

            An ideal point of the projectivized component is an isotropic ray
            of its closure, which is the one-dimensional rational polyhedral
            cone it spans.
            """
            from dzack_research.preamble.categories.polyhedral_cones import (
                RationalPolyhedralCones,
            )

            lattice = self.lattice()
            vector = lattice(vector)
            assert lattice.q(vector) == 0 and self._component.closure_contains(vector) and vector != lattice.zero(), (
                f"{vector} does not define an ideal point of {self}: an ideal point is the "
                f"ray of a nonzero isotropic vector in the closure of {self._component}, "
                f"and {vector} has square {lattice.q(vector)}"
            )
            primitive = _primitive_on_selected_ray(
                lattice, vector, self._component.timelike_vector()
            )
            return RationalPolyhedralCones(lattice).from_rays((primitive,))

        def projectivize_cone(self, cone):
            if cone.ambient_lattice() is not self.lattice():
                raise ValueError(
                    f"cannot projectivize {cone} into {self}: the cone lies in "
                    f"{cone.ambient_lattice()}, not in {self.lattice()}"
                )
            if not cone.lies_in_closed_positive_cone(self._component.timelike_vector()):
                raise ValueError(
                    f"cannot projectivize {cone} into {self}: a hyperbolic polyhedron comes "
                    f"from a cone in the closure of {self._component}, and {cone} is not "
                    f"contained in it"
                )
            category = HyperbolicPolyhedra(self)
            subset = self.condition_set(
                lambda point: cone.contains(point.representative())
            )
            return Sets().Subobjects(self).object(
                subset.inclusion(),
                categories=(category,),
                construction_data={"space": self, "cone": cone},
            )

        def _repr_(self):
            return f"Hyperbolic projectivization of {self._component}"


class HyperbolicPolyhedra(OwnedParameterizedCategory):
    r"""Projectivized rational polyhedral cones in a chosen hyperbolic space."""

    def parameter_category(self):
        space = self.parameter()
        return HyperbolicSpaces(space.positive_cone_component())

    def hyperbolic_space(self):
        return self.base()

    @classmethod
    def _repr_object_names(cls):
        return "hyperbolic polyhedra"

    def super_categories(self):
        return [Sets().Subobjects(self.hyperbolic_space())]

    def an_object(self):
        from dzack_research.preamble.categories.polyhedral_cones import (
            RationalPolyhedralCones,
        )

        space = self.hyperbolic_space()
        ray = RationalPolyhedralCones(space.lattice()).from_rays(
            (space.positive_cone_component().timelike_vector(),)
        )
        return space.projectivize_cone(ray)

    class ParentMethods:
        def __init__(self, space, cone, **rest) -> None:
            self._space = space
            self._cone = cone
            super().__init__(**rest)

        def hyperbolic_space(self):
            return self._space

        def cone(self):
            return self._cone

        def ordinary_vertices(self):
            space = self.hyperbolic_space()
            lattice = space.lattice()
            return finite_ordered_set(
                tuple(space.rational_point(ray) for ray in self.cone().primitive_rays() if lattice.q(ray) > 0)
            )

        def ideal_vertices(self):
            space = self.hyperbolic_space()
            lattice = space.lattice()
            return finite_ordered_set(
                tuple(space.ideal_point(ray) for ray in self.cone().primitive_rays() if lattice.q(ray) == 0)
            )

        def wall_roots(self):
            return self.cone().wall_roots()

        def weyl_group(self):
            return self.cone().weyl_group()

        def coxeter_diagram(self):
            return self.cone().coxeter_diagram()

        def is_compact(self) -> bool:
            if self.cone().is_complete_wall_set() is not True:
                raise ValueError(
                    f"cannot decide whether {self} is compact: compactness is read from the "
                    f"ideal vertices, which requires every wall of {self.cone()} to be known, "
                    f"and its wall set is not known to be complete"
                )
            return self.ideal_vertices().cardinality() == 0

        def _repr_(self):
            return f"Hyperbolic polyhedron from {self.cone()}"


def _positive_cone_component(lattice, timelike):
    category = PositiveConeComponents(lattice)
    ambient = category.ambient_space()
    timelike = lattice(timelike)
    subset = ambient.condition_set(
        lambda vector: _positive_component_contains(
            lattice,
            ambient,
            timelike,
            vector,
        )
    )
    return Sets().Subobjects(ambient).object(
        subset.inclusion(),
        categories=(category,),
        construction_data={"lattice": lattice, "timelike": timelike},
    )


def _hyperbolic_space(component):
    return _object_of(
        HyperbolicSpaces(component),
        topology_data=_HyperbolicTopologyData(),
        component=component,
    )


__all__ = [
    "HyperbolicPolyhedra",
    "HyperbolicSpaces",
    "PositiveConeComponents",
]
