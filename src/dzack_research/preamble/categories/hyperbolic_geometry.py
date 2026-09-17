r"""Positive-cone components and their projectivized hyperbolic geometry."""

from sage.arith.misc import gcd
from sage.misc.cachefunc import cached_method
from sage.structure.element import Element
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of


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
            return _positive_cone_component(self.lattice(), -self.timelike_vector())

        @cached_method
        def projectivization(self):
            return _hyperbolic_space(self)

        def _repr_(self):
            return f"Positive-cone component of {self.lattice()} selected by {self.timelike_vector()}"


class HyperbolicSpaces(OwnedCategory):
    r"""Projectivizations of chosen positive-cone components."""

    @classmethod
    def _repr_object_names(cls):
        return "hyperbolic spaces"

    def super_categories(self):
        return [Sets()]

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

        def __call__(self, *args, **kwargs):
            r"""Construct a point through the owned element construction directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, datum):
            r"""Return the point on the ray of ``datum``, a positive vector of the component or a point of this space."""
            match datum:
                case _ if element_parent(datum) is self:
                    return datum
                case _:
                    assert datum in self._component, (
                        "a rational point of a hyperbolic space is the ray of a "
                        "positive vector in the selected component"
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
                "an ideal point is the ray of a nonzero isotropic vector in the closed component"
            )
            primitive = _primitive_on_selected_ray(
                lattice, vector, self._component.timelike_vector()
            )
            return RationalPolyhedralCones().from_rays(lattice, (primitive,))

        def projectivize_cone(self, cone):
            if cone.ambient_lattice() is not self.lattice():
                raise ValueError("a hyperbolic polyhedron cone must live in the space's lattice")
            if not cone.lies_in_closed_positive_cone(self._component.timelike_vector()):
                raise ValueError("the cone is not contained in the selected closed positive cone")
            return _object_of(HyperbolicPolyhedra(), space=self, cone=cone)

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


def _positive_cone_component(lattice, timelike):
    return _object_of(PositiveConeComponents(), lattice=lattice, timelike=timelike)


def _hyperbolic_space(component):
    return _object_of(HyperbolicSpaces(), component=component)


__all__ = [
    "HyperbolicPolyhedra",
    "HyperbolicSpaces",
    "PositiveConeComponents",
]
