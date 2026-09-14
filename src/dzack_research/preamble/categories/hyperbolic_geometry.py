r"""Positive-cone components and their projectivized hyperbolic geometry."""

from sage.arith.misc import gcd
from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import object_of


def _primitive_on_selected_ray(lattice, vector, timelike):
    vector = lattice(vector)
    coordinates = tuple(int(entry) for entry in vector.to_tuple())
    nonzero_coordinates = tuple(abs(entry) for entry in coordinates if entry)
    if not nonzero_coordinates:
        raise ValueError("a projective ray is represented by a nonzero vector")
    content = gcd(nonzero_coordinates)
    primitive = lattice(tuple(entry // content for entry in coordinates))
    if lattice.b(primitive, timelike) < 0:
        primitive = -primitive
    return primitive


class PositiveConeComponents(OwnedCategory):
    r"""Chosen components of ``{x : q(x)>0}`` for lattices of signature ``(1,n)``."""

    @classmethod
    def _repr_object_names(cls):
        return "positive-cone components"

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def __init__(self, lattice, timelike, **rest) -> None:
            signature = lattice.signature_pair()
            if int(signature.first()) != 1 or int(signature.second()) < 1:
                raise ValueError("a positive-cone component is selected here in signature (1,n)")
            timelike = lattice(timelike)
            if lattice.q(timelike) <= 0:
                raise ValueError("the selected component requires a positive-square vector")
            self._lattice = lattice
            self._timelike = timelike
            super().__init__(**rest)

        def lattice(self):
            return self._lattice

        def timelike_vector(self):
            return self._timelike

        def __contains__(self, vector) -> bool:
            lattice = self.lattice()
            vector = lattice(vector)
            return lattice.q(vector) > 0 and lattice.b(vector, self.timelike_vector()) > 0

        def closure_contains(self, vector) -> bool:
            lattice = self.lattice()
            vector = lattice(vector)
            return lattice.q(vector) >= 0 and lattice.b(vector, self.timelike_vector()) >= 0

        def opposite(self):
            return positive_cone_component(self.lattice(), -self.timelike_vector())

        @cached_method
        def projectivization(self):
            return hyperbolic_space(self)

        def _repr_(self):
            return f"Positive-cone component of {self.lattice()} selected by {self.timelike_vector()}"


class HyperbolicRay(SageObject):
    r"""One rational projective ray in the hyperbolic space or its ideal boundary."""

    def __init__(self, space, representative, *, ideal) -> None:
        self._space = space
        self._representative = representative
        self._ideal = bool(ideal)

    def space(self):
        return self._space

    def representative(self):
        return self._representative

    def is_ideal(self) -> bool:
        return self._ideal

    def is_interior(self) -> bool:
        return not self._ideal

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, HyperbolicRay)
            and other.space() is self.space()
            and other.representative() == self.representative()
            and other.is_ideal() == self.is_ideal()
        )

    def __hash__(self) -> int:
        return hash((id(self.space()), tuple(self.representative().to_tuple()), self.is_ideal()))

    def _repr_(self):
        nature = "ideal boundary ray" if self.is_ideal() else "hyperbolic ray"
        return f"{nature} [{self.representative()}]"


class HyperbolicSpaces(OwnedCategory):
    r"""Projectivizations of chosen positive-cone components."""

    @classmethod
    def _repr_object_names(cls):
        return "hyperbolic spaces"

    def super_categories(self):
        return [Sets()]

    class ParentMethods:
        def __init__(self, component, **rest) -> None:
            self._component = component
            super().__init__(**rest)

        def positive_cone_component(self):
            return self._component

        def lattice(self):
            return self._component.lattice()

        def rational_point(self, vector):
            if vector not in self._component:
                raise ValueError("a rational hyperbolic point needs a positive vector in the selected component")
            primitive = _primitive_on_selected_ray(
                self.lattice(), vector, self._component.timelike_vector()
            )
            return HyperbolicRay(self, primitive, ideal=False)

        def ideal_point(self, vector):
            lattice = self.lattice()
            vector = lattice(vector)
            if lattice.q(vector) != 0 or lattice.b(vector, self._component.timelike_vector()) <= 0:
                raise ValueError("an ideal point needs a nonzero isotropic vector in the selected closed component")
            primitive = _primitive_on_selected_ray(
                lattice, vector, self._component.timelike_vector()
            )
            return HyperbolicRay(self, primitive, ideal=True)

        def projectivize_cone(self, cone):
            if cone.ambient_lattice() is not self.lattice():
                raise ValueError("a hyperbolic polyhedron cone must live in the space's lattice")
            if not cone.lies_in_closed_positive_cone(self._component.timelike_vector()):
                raise ValueError("the cone is not contained in the selected closed positive cone")
            return object_of(HyperbolicPolyhedra(), space=self, cone=cone)

        def _repr_(self):
            return f"Hyperbolic projectivization of {self._component}"


class HyperbolicPolyhedra(OwnedCategory):
    r"""Projectivized rational polyhedral cones in a chosen hyperbolic space."""

    @classmethod
    def _repr_object_names(cls):
        return "hyperbolic polyhedra"

    def super_categories(self):
        return [Sets()]

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
                raise ValueError("compactness of a chamber requires a complete wall set")
            return self.ideal_vertices().cardinality() == 0

        def _repr_(self):
            return f"Hyperbolic polyhedron from {self.cone()}"


def positive_cone_component(lattice, timelike):
    return object_of(PositiveConeComponents(), lattice=lattice, timelike=timelike)


def hyperbolic_space(component):
    return object_of(HyperbolicSpaces(), component=component)


__all__ = [
    "HyperbolicPolyhedra",
    "HyperbolicRay",
    "HyperbolicSpaces",
    "PositiveConeComponents",
    "hyperbolic_space",
    "positive_cone_component",
]
