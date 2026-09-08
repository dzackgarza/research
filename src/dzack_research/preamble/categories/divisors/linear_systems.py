r"""Complete linear systems represented by their section spaces."""

from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import VectorSpaces
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
)
from dzack_research.preamble.categories.schemes.schemes import (
    ProjectiveSchemes,
    ProjectiveSpace,
    Schemes,
    refine_scheme,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)


class CompleteLinearSystems(OwnedCategoryOverBaseRing):
    r"""Projective spaces ``|D| = P(H^0(X,O_X(D)))`` with their defining data."""

    @classmethod
    def _repr_object_names(cls):
        return "complete linear systems"

    def super_categories(self):
        return [ProjectiveSchemes(self.base_ring())]

    class ParentMethods:
        def linear_system_scheme(self):
            return self._preamble_linear_system_scheme

        def linear_system_divisor(self):
            return self._preamble_linear_system_divisor

        def section_space(self):
            return self._preamble_linear_system_section_space

        def projective_dimension(self):
            return self.relative_dimension()

        def associated_morphism(self):
            r"""Return the map defined by this complete linear system when basepoint-free."""
            return self.linear_system_scheme().associated_projective_morphism(
                self.linear_system_divisor()
            )


class HomogeneousPolynomialSectionSpaces(OwnedCategoryOverBaseRing):
    r"""Finite homogeneous-polynomial section spaces on represented projective schemes."""

    @classmethod
    def _repr_object_names(cls):
        return "homogeneous polynomial section spaces"

    def super_categories(self):
        return [VectorSpaces(self.base_ring())]

    class ParentMethods:
        def section_scheme(self):
            return self._preamble_section_scheme

        def homogeneous_degree(self):
            return self._preamble_homogeneous_degree

        def homogeneous_coordinate_ring(self):
            return self._preamble_homogeneous_coordinate_ring


def _weak_compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in _weak_compositions(total - first, length - 1):
            yield (first, *tail)


def HomogeneousPolynomialSectionSpace(projective_scheme, degree, *, coordinate_names=None):
    r"""Return the degree-``d`` homogeneous polynomial space on ``P^n``.

    Basis labels are the actual monomials in an owned homogeneous-coordinate
    polynomial algebra, not anonymous positions.
    """
    base = projective_scheme.scheme_base_ring()
    degree = int(degree)
    if degree < 0:
        raise ValueError("a homogeneous polynomial degree is nonnegative")
    width = int(projective_scheme.relative_dimension()) + 1
    names = (
        tuple(f"x{index}" for index in range(width))
        if coordinate_names is None
        else tuple(coordinate_names)
    )
    if len(names) != width:
        raise ValueError("projective homogeneous coordinates have dimension plus one names")
    ring = PolynomialRing(base, names)
    labels = tuple(ring.algebra_generating_set())
    monomials = []
    exponent_data = {}
    for exponents in _weak_compositions(degree, width):
        monomial = ring.one()
        for position, exponent in enumerate(exponents):
            if exponent:
                monomial *= ring.algebra_generator(labels[position]) ** exponent
        monomials.append(monomial)
        exponent_data[monomial] = exponents
    space = FreshFreeModuleOn(
        base,
        finite_ordered_set(tuple(monomials)),
        _extra_categories=(HomogeneousPolynomialSectionSpaces(base),),
        _extra_construction_data=(
            ("_preamble_section_scheme", projective_scheme),
            ("_preamble_homogeneous_degree", degree),
            ("_preamble_homogeneous_coordinate_ring", ring),
            ("_preamble_homogeneous_exponents", exponent_data),
        ),
    )
    return space


def CoordinateHyperplaneSectionRestriction(projective_space, degree, coordinate_index):
    r"""Restrict degree-``d`` sections of ``P^n`` to ``x_i=0``.

    This is the exact map ``H^0(P^n,O(d)) -> H^0(P^{n-1},O(d))`` for the
    coordinate hyperplane.  The kernel is the forms divisible by ``x_i`` and
    the map is surjective for ``d >= 0``.
    """
    degree = int(degree)
    coordinate_index = int(coordinate_index)
    dimension = int(projective_space.relative_dimension())
    if dimension < 1:
        raise ValueError("a coordinate hyperplane requires positive projective dimension")
    if coordinate_index < 0 or coordinate_index > dimension:
        raise ValueError("the coordinate index is outside the projective coordinate range")
    source_names = tuple(f"x{index}" for index in range(dimension + 1))
    source = HomogeneousPolynomialSectionSpace(
        projective_space,
        degree,
        coordinate_names=source_names,
    )
    native_ring = projective_space.coordinate_ring()
    hyperplane = projective_space.closed_subscheme(native_ring.gen(coordinate_index))
    target_names = tuple(
        name for index, name in enumerate(source_names) if index != coordinate_index
    )
    target = HomogeneousPolynomialSectionSpace(
        hyperplane,
        degree,
        coordinate_names=target_names,
    )
    source_exponents = source._preamble_homogeneous_exponents
    target_by_exponents = {
        exponents: monomial
        for monomial, exponents in target._preamble_homogeneous_exponents.items()
    }

    def image(monomial):
        exponents = source_exponents[monomial]
        if exponents[coordinate_index]:
            return target.zero()
        restricted = exponents[:coordinate_index] + exponents[coordinate_index + 1 :]
        return target.module_generator(target_by_exponents[restricted])

    restriction = module_homset(source, target)(
        {
            monomial: image(monomial)
            for monomial in source.module_generating_set()
        }
    )
    restriction._preamble_closed_subscheme = hyperplane
    return restriction


def CompleteLinearSystem(scheme, divisor, section_space):
    r"""Return the complete linear system of ``divisor`` on ``scheme``.

    The represented convention is the projective space of nonzero global
    sections modulo scalars.  Hence a section space of dimension ``r`` gives
    ``P^(r-1)``; the empty section space has no projectivization and is refused.
    """
    base = scheme.scheme_base_ring()
    if scheme not in Schemes(base):
        raise TypeError("a complete linear system requires a represented scheme")
    if section_space.base_ring() is not base:
        raise ValueError("the section space must be over the scheme base field")
    dimension = int(section_space.dimension())
    if dimension == 0:
        raise ValueError("the empty linear system has no represented projective space")
    system = ProjectiveSpace(dimension - 1, base)
    system._preamble_linear_system_scheme = scheme
    system._preamble_linear_system_divisor = divisor
    system._preamble_linear_system_section_space = section_space
    return refine_scheme(system, base, [CompleteLinearSystems(base)])


__all__ = [
    "CompleteLinearSystem",
    "CompleteLinearSystems",
    "CoordinateHyperplaneSectionRestriction",
    "HomogeneousPolynomialSectionSpace",
    "HomogeneousPolynomialSectionSpaces",
]
