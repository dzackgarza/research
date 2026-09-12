r"""Complete linear systems represented by their section spaces."""

from itertools import product as cartesian_product
from math import comb

from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.free_algebras import PolynomialRing
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreshFreeModuleOn,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_embedding,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import VectorSpaces
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedFields,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    ProductProjectiveSpaces,
    ProjectiveSchemes,
    ProjectiveSpace,
    Schemes,
    refine_scheme,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


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

        def homogeneous_polynomial(self, section):
            r"""Return the homogeneous polynomial represented by ``section``."""
            section = self(section)
            coefficients = module_coefficients(section, self)
            ring = self.homogeneous_coordinate_ring()
            scalar_map = ring.algebra_structure_morphism()
            return sum(
                (
                    scalar_map(coefficient) * monomial
                    for monomial, coefficient in coefficients.items()
                ),
                ring.zero(),
            )


class MultihomogeneousPolynomialSectionSpaces(OwnedCategoryOverBaseRing):
    r"""Finite multihomogeneous section spaces on products of projective spaces."""

    @classmethod
    def _repr_object_names(cls):
        return "multihomogeneous polynomial section spaces"

    def super_categories(self):
        return [VectorSpaces(self.base_ring())]

    class ParentMethods:
        def section_scheme(self):
            return self._preamble_section_scheme

        def multidegree(self):
            return self._preamble_multihomogeneous_degree

        def homogeneous_coordinate_ring(self):
            return self._preamble_homogeneous_coordinate_ring


class ProjectiveLinearSystems(OwnedCategoryOverBaseRing):
    r"""Projective parameter spaces of represented section subspaces of ``O(d)``."""

    @classmethod
    def _repr_object_names(cls):
        return "projective linear systems"

    def super_categories(self):
        return [ProjectiveSchemes(self.base_ring())]

    class ParentMethods:
        def line_bundle(self):
            return self._preamble_linear_system_line_bundle

        def ambient_section_space(self):
            return self.line_bundle().global_sections()

        def projective_dimension(self):
            return self.relative_dimension()

        def selected_section_space(self):
            return self._preamble_selected_section_space

        def section_embedding(self):
            return self._preamble_section_embedding

        def selected_sections(self):
            embedding = self.section_embedding()
            source = self.selected_section_space()
            return indexed_family(
                source.module_generating_set(),
                lambda label: embedding(source.module_generator(label)),
                name="Selected sections of the linear system",
            )

        def base_locus(self):
            return self._preamble_base_locus

        def is_basepoint_free(self) -> bool:
            return self.base_locus().is_empty()

        @cached_method
        def domain_of_definition(self):
            if self.is_basepoint_free():
                return self.line_bundle().scheme()
            return self.base_locus().open_complement()

        @cached_method
        def associated_morphism(self):
            domain = self.domain_of_definition()
            source_sections = self.ambient_section_space()
            coordinates = tuple(
                source_sections.homogeneous_polynomial(section)
                for section in self.selected_sections()
            )
            return domain.projective_morphism_from_coordinates(self, coordinates)


class ProjectiveJetSpaces(OwnedCategoryOverBaseRing):
    r"""Finite local jet realizations ``O(d)_p / m_p^r O(d)_p`` on projective space."""

    @classmethod
    def _repr_object_names(cls):
        return "projective jet spaces"

    def super_categories(self):
        return [VectorSpaces(self.base_ring())]

    class ParentMethods:
        def jet_projective_space(self):
            return self._preamble_jet_projective_space

        def jet_line_bundle(self):
            return self._preamble_jet_line_bundle

        def jet_homogeneous_degree(self):
            return self.jet_line_bundle().degree()

        def jet_order(self):
            return self._preamble_jet_order

        def jet_point(self):
            return self._preamble_jet_point

        def jet_affine_chart(self):
            return self._preamble_jet_affine_chart

        def jet_spectrum_point(self):
            return self._preamble_jet_spectrum_point

        def jet_stalk(self):
            return self._preamble_jet_stalk

        def jet_maximal_ideal(self):
            return self._preamble_jet_maximal_ideal

        def jet_local_quotient(self):
            return self._preamble_jet_local_quotient

        def jet_residue_field(self):
            return self._preamble_jet_residue_field

        def jet_coordinate_index(self):
            index = getattr(self, "_preamble_jet_coordinate_index", None)
            if index is None:
                raise ValueError("this jet condition was not selected at a coordinate point")
            return index


class ImposedMultiplicityLinearSystems(OwnedCategoryOverBaseRing):
    r"""Projective parameter spaces of sections satisfying one jet condition."""

    @classmethod
    def _repr_object_names(cls):
        return "linear systems with imposed multiplicity"

    def super_categories(self):
        return [ProjectiveSchemes(self.base_ring())]

    class ParentMethods:
        def ambient_section_space(self):
            return self._preamble_ambient_section_space

        def constrained_section_space(self):
            return self._preamble_constrained_section_space

        def imposed_jet_evaluation(self):
            return self._preamble_imposed_jet_evaluation

        def imposed_vanishing_order(self):
            return self.imposed_jet_evaluation().codomain().jet_order()


def _weak_compositions(total, length):
    if length == 0:
        if total == 0:
            yield ()
        return
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


def MultiHomogeneousPolynomialSectionSpace(projective_product, degrees):
    r"""Return ``H^0(prod P^{n_i}, O(d_i))`` for nonnegative multidegree.

    Basis labels are the actual multihomogeneous monomials in one owned
    polynomial coordinate algebra.  The degree is retained on the exact factor
    index set, so repeated isomorphic factors keep distinct roles.
    """
    base = projective_product.scheme_base_ring()
    if projective_product not in ProductProjectiveSpaces(base):
        raise TypeError("a multihomogeneous section space requires a product of projective spaces")
    factors = projective_product.factors()
    factor_indices = factors.index_set()
    factor_labels = tuple(factor_indices)
    if isinstance(degrees, IndexedFamily):
        if degrees.index_set() is not factor_indices:
            raise ValueError("a multidegree is indexed by the product's exact factor index set")
        degree_values = tuple(
            _own_ring(SageZZ)(degrees[label]) for label in factor_labels
        )
    else:
        degree_values = tuple(_own_ring(SageZZ)(value) for value in degrees)
        if len(degree_values) != len(factor_labels):
            raise ValueError("a multidegree has one degree for every projective factor")
    if any(degree < 0 for degree in degree_values):
        raise ValueError("multihomogeneous polynomial degrees are nonnegative")
    multidegree = finite_indexed_family(
        factor_indices,
        lambda label: degree_values[
            next(
                position
                for position, known_label in enumerate(factor_labels)
                if known_label == label
            )
        ],
        name="Projective multidegree",
    )
    widths = tuple(
        int(factors[label].relative_dimension()) + 1
        for label in factor_labels
    )
    coordinate_names = tuple(
        f"x{factor_position}_{coordinate}"
        for factor_position, width in enumerate(widths)
        for coordinate in range(width)
    )
    ring = PolynomialRing(base, coordinate_names)
    ring_labels = tuple(ring.algebra_generating_set())
    block_offsets = []
    offset = 0
    for width in widths:
        block_offsets.append((offset, offset + width))
        offset += width

    monomials = []
    exponent_data = {}
    block_exponents = tuple(
        tuple(_weak_compositions(int(degree), width))
        for degree, width in zip(degree_values, widths, strict=True)
    )
    for blocks in cartesian_product(*block_exponents):
        flat = tuple(power for block in blocks for power in block)
        monomial = ring.one()
        for position, exponent in enumerate(flat):
            if exponent:
                monomial *= ring.algebra_generator(ring_labels[position]) ** exponent
        monomials.append(monomial)
        exponent_data[monomial] = tuple(tuple(block) for block in blocks)

    return FreshFreeModuleOn(
        base,
        finite_ordered_set(tuple(monomials)),
        _extra_categories=(MultihomogeneousPolynomialSectionSpaces(base),),
        _extra_construction_data=(
            ("_preamble_section_scheme", projective_product),
            ("_preamble_multihomogeneous_degree", multidegree),
            ("_preamble_homogeneous_coordinate_ring", ring),
            ("_preamble_multihomogeneous_exponents", exponent_data),
            ("_preamble_multihomogeneous_block_offsets", tuple(block_offsets)),
        ),
    )


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


def ProjectiveLinearSystem(line_bundle, sections):
    r"""Return the projective linear system spanned by independent sections of ``line_bundle``."""
    scheme = line_bundle.projective_space()
    ambient = line_bundle.global_sections()
    base = scheme.scheme_base_ring()
    sections = tuple(ambient(section) for section in sections)
    if not sections:
        raise ValueError("a projective linear system requires a nonzero section subspace")
    labels = Sets.Δ[len(sections) - 1]
    selected = FreshFreeModuleOn(base, labels)
    images = {
        label: sections[int(labels.ranking_map()(label))]
        for label in labels
    }
    selected_map = module_homset(selected, ambient)(images)
    if int(selected_map.kernel().dimension()) != 0:
        raise ValueError("the supplied sections must be a basis of their selected subspace")
    embedding = module_embedding(selected, ambient, images)
    polynomials = tuple(
        ambient.homogeneous_polynomial(section)
        for section in sections
    )
    base_locus = scheme.closed_subscheme(polynomials)
    system = ProjectiveSpace(len(sections) - 1, base)
    system._preamble_linear_system_line_bundle = line_bundle
    system._preamble_selected_section_space = selected
    system._preamble_section_embedding = embedding
    system._preamble_base_locus = base_locus
    return refine_scheme(system, base, [ProjectiveLinearSystems(base)])


def _centered_jet_basis(base, dimension, jet_order):
    names = tuple(f"v{index}" for index in range(dimension))
    ring = PolynomialRing(base, names)
    labels = tuple(ring.algebra_generating_set())
    monomials = []
    by_exponents = {}
    for total in range(jet_order):
        for exponents in _weak_compositions(total, dimension):
            monomial = ring.one()
            for position, exponent in enumerate(exponents):
                if exponent:
                    monomial *= ring.algebra_generator(labels[position]) ** exponent
            monomials.append(monomial)
            by_exponents[tuple(exponents)] = monomial
    return ring, tuple(monomials), by_exponents


def ProjectivePointJetEvaluation(line_bundle, point, jet_order):
    r"""Return ``H^0(P,L) -> L_p / m_p^r L_p`` at a represented rational point.

    The local quotient is the defining object: choose a standard affine chart
    containing ``p``, form its spectrum point, localize to ``O_{P,p}``, and
    quotient by the ``r``-th power of its maximal ideal.  Centered affine
    monomials of total degree below ``r`` give the finite free realization used
    by the section map.  Thus a non-coordinate point changes the evaluation
    coefficients without changing the mathematical jet object.
    """
    projective_space = line_bundle.projective_space()
    base = projective_space.scheme_base_ring()
    if base not in OwnedFields():
        raise TypeError("the represented projective point-jet realization requires a field base")
    if point.codomain() is not projective_space:
        raise ValueError("a projective jet is evaluated at a point of its line bundle's scheme")
    if point.domain() is not projective_space.base_scheme():
        raise NotImplementedError("the represented projective jet currently requires a rational point")
    jet_order = int(jet_order)
    if jet_order < 1:
        raise ValueError("a jet order is positive")

    coordinates = tuple(point.point_coordinates())
    dimension = int(projective_space.relative_dimension())
    if len(coordinates) != dimension + 1:
        raise ValueError("a projective point has dimension plus one homogeneous coordinates")
    pivot = next(
        (index for index, coordinate in enumerate(coordinates) if coordinate != base.zero()),
        None,
    )
    if pivot is None:
        raise ValueError("projective point coordinates cannot all vanish")
    pivot_inverse = coordinates[pivot].inverse_of_unit()
    affine_values = tuple(
        coordinates[index] * pivot_inverse
        for index in range(dimension + 1)
        if index != pivot
    )

    chart = projective_space.standard_affine_chart(pivot)
    chart_algebra = chart.coordinate_algebra()
    chart_coordinates = tuple(
        projective_space._standard_chart_coordinate(pivot, index)
        for index in range(dimension + 1)
        if index != pivot
    )
    scalar_map = chart_algebra.algebra_structure_morphism()
    point_ideal = chart_algebra.ideal(
        *(
            coordinate - scalar_map(value)
            for coordinate, value in zip(chart_coordinates, affine_values, strict=True)
        )
    )
    spectrum_point = chart.underlying_space()(point_ideal)
    stalk = spectrum_point.local_ring()
    maximal_ideal = stalk.maximal_ideal()
    local_quotient = stalk.quotient_ring(maximal_ideal.power(jet_order))
    residue_field = spectrum_point.residue_field()

    _centered_ring, local_monomials, local_by_exponents = _centered_jet_basis(
        base,
        dimension,
        jet_order,
    )
    source = line_bundle.global_sections()
    target = FreshFreeModuleOn(
        base,
        finite_ordered_set(local_monomials),
        _extra_categories=(ProjectiveJetSpaces(base),),
        _extra_construction_data=(
            ("_preamble_jet_projective_space", projective_space),
            ("_preamble_jet_line_bundle", line_bundle),
            ("_preamble_jet_order", _own_ring(SageZZ)(jet_order)),
            ("_preamble_jet_point", point),
            ("_preamble_jet_affine_chart", chart),
            ("_preamble_jet_spectrum_point", spectrum_point),
            ("_preamble_jet_stalk", stalk),
            ("_preamble_jet_maximal_ideal", maximal_ideal),
            ("_preamble_jet_local_quotient", local_quotient),
            ("_preamble_jet_residue_field", residue_field),
        ),
    )
    source_exponents = source._preamble_homogeneous_exponents
    nonpivot = tuple(index for index in range(dimension + 1) if index != pivot)

    def image(monomial):
        homogeneous_exponents = source_exponents[monomial]
        local_powers = tuple(homogeneous_exponents[index] for index in nonpivot)
        coefficients = {}
        choices = tuple(
            range(power + 1)
            for power in local_powers
        )
        for centered_exponents in cartesian_product(*choices):
            if sum(centered_exponents) >= jet_order:
                continue
            coefficient = base.one()
            for power, centered_power, value in zip(
                local_powers,
                centered_exponents,
                affine_values,
                strict=True,
            ):
                coefficient *= base(comb(power, centered_power)) * value ** (
                    power - centered_power
                )
            if coefficient != base.zero():
                coefficients[local_by_exponents[tuple(centered_exponents)]] = coefficient
        return target.linear_combination(coefficients)

    evaluation = module_homset(source, target)(
        {
            monomial: image(monomial)
            for monomial in source.module_generating_set()
        }
    )
    evaluation._preamble_projective_point = point
    evaluation._preamble_projective_point_chart_index = pivot
    return evaluation


def CoordinatePointJetEvaluation(projective_space, degree, coordinate_index, jet_order):
    r"""Coordinate-point spelling of :func:`ProjectivePointJetEvaluation`."""
    coordinate_index = int(coordinate_index)
    dimension = int(projective_space.relative_dimension())
    if coordinate_index < 0 or coordinate_index > dimension:
        raise ValueError("the coordinate index is outside the projective coordinate range")
    base = projective_space.scheme_base_ring()
    coordinates = tuple(
        base.one() if index == coordinate_index else base.zero()
        for index in range(dimension + 1)
    )
    point = projective_space.point_morphism(coordinates)
    evaluation = ProjectivePointJetEvaluation(
        projective_space.O(degree),
        point,
        jet_order,
    )
    evaluation._preamble_projective_point_coordinate_index = coordinate_index
    evaluation.codomain()._preamble_jet_coordinate_index = coordinate_index
    return evaluation


def SectionsVanishingAtPoint(line_bundle, point, vanishing_order):
    r"""Sections whose germ lies in ``m_p^r L_p``."""
    return ProjectivePointJetEvaluation(
        line_bundle,
        point,
        vanishing_order,
    ).kernel()


def ImposedPointMultiplicityLinearSystem(line_bundle, point, vanishing_order):
    r"""Projectivize sections vanishing to order at least ``r`` at ``point``."""
    evaluation = ProjectivePointJetEvaluation(line_bundle, point, vanishing_order)
    constrained = evaluation.kernel()
    dimension = int(constrained.dimension())
    if dimension == 0:
        raise ValueError("the imposed condition leaves no nonzero section to projectivize")
    base = line_bundle.projective_space().scheme_base_ring()
    parameter_space = ProjectiveSpace(dimension - 1, base)
    parameter_space._preamble_ambient_section_space = evaluation.domain()
    parameter_space._preamble_constrained_section_space = constrained
    parameter_space._preamble_imposed_jet_evaluation = evaluation
    return refine_scheme(
        parameter_space,
        base,
        [ImposedMultiplicityLinearSystems(base)],
    )


def SectionsVanishingToOrder(projective_space, degree, coordinate_index, vanishing_order):
    r"""Return degree-``d`` sections vanishing to order at least ``r`` at a coordinate point."""
    return CoordinatePointJetEvaluation(
        projective_space,
        degree,
        coordinate_index,
        vanishing_order,
    ).kernel()


def ImposedMultiplicityLinearSystem(projective_space, degree, coordinate_index, vanishing_order):
    r"""Coordinate-point spelling of :func:`ImposedPointMultiplicityLinearSystem`."""
    coordinate_index = int(coordinate_index)
    dimension = int(projective_space.relative_dimension())
    if coordinate_index < 0 or coordinate_index > dimension:
        raise ValueError("the coordinate index is outside the projective coordinate range")
    base = projective_space.scheme_base_ring()
    point = projective_space.point_morphism(
        tuple(
            base.one() if index == coordinate_index else base.zero()
            for index in range(dimension + 1)
        )
    )
    result = ImposedPointMultiplicityLinearSystem(
        projective_space.O(degree),
        point,
        vanishing_order,
    )
    result.imposed_jet_evaluation()._preamble_projective_point_coordinate_index = coordinate_index
    result.imposed_jet_evaluation().codomain()._preamble_jet_coordinate_index = coordinate_index
    return result


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
    "CoordinatePointJetEvaluation",
    "HomogeneousPolynomialSectionSpace",
    "HomogeneousPolynomialSectionSpaces",
    "ImposedMultiplicityLinearSystem",
    "ImposedMultiplicityLinearSystems",
    "ImposedPointMultiplicityLinearSystem",
    "ProjectiveJetSpaces",
    "ProjectiveLinearSystem",
    "ProjectiveLinearSystems",
    "ProjectivePointJetEvaluation",
    "SectionsVanishingAtPoint",
    "SectionsVanishingToOrder",
]
