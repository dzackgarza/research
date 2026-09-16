r"""Complete linear systems represented by their section spaces."""

from itertools import product as cartesian_product
from math import comb

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.algebras import (
    AlgebrasWithChosenFinitePresentation,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
)
from dzack_research.preamble.categories.modules.pure.modules import VectorSpaces
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedFields,
    _engine_element,
    _engine_ring,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    ProductProjectiveSpaces,
    ProjectiveSchemes,
    ProjectiveSpaces,
    Schemes,
    _refine_scheme,
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


class _HomogeneousSectionSpaceConstruction:
    r"""The selected homogeneous-coordinate presentation of one section space."""

    def __init__(self, scheme, degree, coordinate_ring, monomial_exponents) -> None:
        self._scheme = scheme
        self._degree = degree
        self._coordinate_ring = coordinate_ring
        self._monomial_exponents = dict(monomial_exponents)

    def scheme(self):
        return self._scheme

    def degree(self):
        return self._degree

    def coordinate_ring(self):
        return self._coordinate_ring

    def exponents_of(self, monomial):
        return self._monomial_exponents[monomial]


class _MultihomogeneousSectionSpaceConstruction(_HomogeneousSectionSpaceConstruction):
    r"""The selected multiprojective coordinate presentation of one section space."""

    def __init__(
        self,
        scheme,
        degree,
        coordinate_ring,
        monomial_exponents,
        coordinate_blocks,
    ) -> None:
        super().__init__(scheme, degree, coordinate_ring, monomial_exponents)
        self._coordinate_blocks = coordinate_blocks

    def coordinate_block(self, position):
        return self._coordinate_blocks[position]


class _ProjectiveJetConstruction:
    r"""The selected local construction defining one projective jet space."""

    def __init__(
        self,
        line_bundle,
        order,
        point,
        affine_chart,
        spectrum_point,
        local_quotient,
    ) -> None:
        self._line_bundle = line_bundle
        self._order = order
        self._point = point
        self._affine_chart = affine_chart
        self._spectrum_point = spectrum_point
        self._local_quotient = local_quotient

    def projective_space(self):
        return self._line_bundle.projective_space()

    def line_bundle(self):
        return self._line_bundle

    def order(self):
        return self._order

    def point(self):
        return self._point

    def affine_chart(self):
        return self._affine_chart

    def spectrum_point(self):
        return self._spectrum_point

    def stalk(self):
        return self._local_quotient.quotient_source()

    def maximal_ideal(self):
        return self.stalk().maximal_ideal()

    def local_quotient(self):
        return self._local_quotient

    def residue_field(self):
        return self._spectrum_point.residue_field()


class _CompleteLinearSystemConstruction:
    r"""The represented scheme, divisor, and section space defining ``|D|``."""

    def __init__(self, scheme, divisor, section_space) -> None:
        self._scheme = scheme
        self._divisor = divisor
        self._section_space = section_space

    def scheme(self):
        return self._scheme

    def divisor(self):
        return self._divisor

    def section_space(self):
        return self._section_space


class _ProjectiveLinearSystemConstruction:
    r"""The selected section embedding defining one projective linear system."""

    def __init__(self, line_bundle, section_embedding, base_locus) -> None:
        self._line_bundle = line_bundle
        self._section_embedding = section_embedding
        self._base_locus = base_locus

    def line_bundle(self):
        return self._line_bundle

    def selected_section_space(self):
        return self._section_embedding.domain()

    def section_embedding(self):
        return self._section_embedding

    def base_locus(self):
        return self._base_locus


class _ImposedMultiplicityConstruction:
    r"""The jet-evaluation kernel defining an imposed-multiplicity system."""

    def __init__(self, evaluation) -> None:
        self._evaluation = evaluation

    def ambient_section_space(self):
        return self._evaluation.domain()

    def constrained_section_space(self):
        return self._evaluation.kernel()

    def evaluation(self):
        return self._evaluation


class CompleteLinearSystems(OwnedCategoryOverBaseRing):
    r"""Projective spaces ``|D| = P(H^0(X,O_X(D)))`` with their defining data."""

    @classmethod
    def _repr_object_names(cls):
        return "complete linear systems"

    def super_categories(self):
        return [ProjectiveSchemes(self.base_ring())]

    class ParentMethods:
        def complete_linear_system_construction(self):
            return self._complete_linear_system_construction

        def linear_system_scheme(self):
            return self.complete_linear_system_construction().scheme()

        def linear_system_divisor(self):
            return self.complete_linear_system_construction().divisor()

        def section_space(self):
            return self.complete_linear_system_construction().section_space()

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
        def __init__(self, _section_space_construction, **rest) -> None:
            if not isinstance(
                _section_space_construction,
                _HomogeneousSectionSpaceConstruction,
            ) or isinstance(
                _section_space_construction,
                _MultihomogeneousSectionSpaceConstruction,
            ):
                raise TypeError(
                    "a homogeneous section space requires homogeneous construction data"
                )
            self._section_space_construction = _section_space_construction
            super().__init__(**rest)

        def section_space_construction(self):
            r"""Return the selected coordinate presentation defining this section space."""
            return self._section_space_construction

        def section_scheme(self):
            return self.section_space_construction().scheme()

        def homogeneous_degree(self):
            return self.section_space_construction().degree()

        def homogeneous_coordinate_ring(self):
            return self.section_space_construction().coordinate_ring()

        def homogeneous_polynomial(self, section):
            r"""Return the homogeneous polynomial represented by ``section``."""
            section = self(section)
            coefficients = self.framing_coefficients(section)
            ring = self.homogeneous_coordinate_ring()
            scalar_map = ring.algebra_structure_morphism()
            return sum(
                (
                    scalar_map(coefficient) * monomial
                    for monomial, coefficient in coefficients.items()
                ),
                ring.zero(),
            )

        def section_from_homogeneous_polynomial(self, polynomial):
            r"""Return the section represented by one homogeneous polynomial of this degree."""
            ring = self.homogeneous_coordinate_ring()
            polynomial = ring(polynomial)
            backend = _engine_element(ring, polynomial)
            engine = _engine_ring(ring)
            base = self.base_ring()
            engine_base = _engine_ring(base)
            by_exponents = {
                tuple(exponents): monomial
                for monomial in self.module_generating_set()
                for exponents in (
                    self.section_space_construction().exponents_of(monomial),
                )
            }
            coefficients = {}
            for exponent, coefficient in engine(backend).monomial_coefficients().items():
                try:
                    powers = tuple(int(value) for value in exponent)
                except TypeError:
                    powers = (int(exponent),)
                if powers not in by_exponents:
                    raise ValueError("the polynomial is not homogeneous of this section-space degree")
                coefficients[by_exponents[powers]] = base._from_engine_element(
                    engine_base(coefficient)
                )
            return self.linear_combination(coefficients)

        def pullback(self, morphism):
            r"""Pull homogeneous sections back along a represented product projection.

            If ``pi_i : prod_j P_j -> P_i``, a degree-``d`` monomial keeps its
            exponent vector in the ``i``-th block and has exponent zero in all
            other blocks.  This is the section map underlying
            ``pi_i^* O(d) = O(0,...,d,...,0)``.
            """
            source_scheme = self.section_scheme()
            if morphism.codomain() is not source_scheme:
                raise ValueError("section pullback requires a morphism into the section scheme")
            pulled_bundle = source_scheme.O(self.homogeneous_degree()).pullback(morphism)
            target = pulled_bundle.global_sections()
            product = morphism.domain()
            label = product.projection_label(morphism)
            labels = tuple(product.factors().index_set())
            label = product.factors().index_set()(label)
            source_construction = self.section_space_construction()
            target_construction = target.section_space_construction()
            target_by_exponents = {
                tuple(tuple(block) for block in target_construction.exponents_of(monomial)): monomial
                for monomial in target.module_generating_set()
            }

            def target_exponents(monomial):
                selected = tuple(source_construction.exponents_of(monomial))
                blocks = []
                for factor_label in labels:
                    factor = product.factors()[factor_label]
                    width = int(factor.relative_dimension()) + 1
                    blocks.append(selected if factor_label == label else (0,) * width)
                return tuple(blocks)

            return self.module_category().Mor(self, target)(
                {
                    monomial: target.module_generator(
                        target_by_exponents[target_exponents(monomial)]
                    )
                    for monomial in self.module_generating_set()
                }
            )

        def pullback_by_projective_automorphism(self, morphism):
            r"""Return ``morphism^*:H^0(P,O(d))->H^0(P,O(d))`` by homogeneous substitution.

            The retained projective-coordinate morphism gives one linear
            homogeneous coordinate for each target coordinate.  Substitution
            is therefore an endomorphism of the owned homogeneous coordinate
            algebra, and restricting it to the degree-``d`` piece is the
            contravariant pullback on sections.
            """
            scheme = self.section_scheme()
            if morphism.domain() is not scheme or morphism.codomain() is not scheme:
                raise ValueError("section pullback here requires a projective automorphism of the section scheme")
            coordinates = tuple(morphism.homogeneous_coordinates())
            ring = self.homogeneous_coordinate_ring()
            labels = tuple(ring.algebra_generating_set())
            if len(coordinates) != len(labels):
                raise ValueError("a projective automorphism needs one homogeneous coordinate per variable")
            if any(getattr(coordinate, "parent", lambda: None)() is not ring for coordinate in coordinates):
                raise ValueError("projective automorphism coordinates must lie in the section homogeneous-coordinate ring")
            substitution = ring.Mor(ring)(
                {label: coordinate for label, coordinate in zip(labels, coordinates, strict=True)}
            )
            return self.module_category().Mor(self, self)(
                {
                    monomial: self.section_from_homogeneous_polynomial(
                        substitution(self.homogeneous_polynomial(self.module_generator(monomial)))
                    )
                    for monomial in self.module_generating_set()
                }
            )


class MultihomogeneousPolynomialSectionSpaces(OwnedCategoryOverBaseRing):
    r"""Finite multihomogeneous section spaces on products of projective spaces."""

    @classmethod
    def _repr_object_names(cls):
        return "multihomogeneous polynomial section spaces"

    def super_categories(self):
        return [VectorSpaces(self.base_ring())]

    class ParentMethods:
        def __init__(self, _section_space_construction, **rest) -> None:
            if not isinstance(
                _section_space_construction,
                _MultihomogeneousSectionSpaceConstruction,
            ):
                raise TypeError(
                    "a multihomogeneous section space requires multiprojective construction data"
                )
            self._section_space_construction = _section_space_construction
            super().__init__(**rest)

        def section_space_construction(self):
            r"""Return the selected coordinate presentation defining this section space."""
            return self._section_space_construction

        def section_scheme(self):
            return self.section_space_construction().scheme()

        def multidegree(self):
            return self.section_space_construction().degree()

        def homogeneous_coordinate_ring(self):
            return self.section_space_construction().coordinate_ring()

        @cached_method
        def factor_coordinate_embedding(self, factor_label):
            r"""Embed one factor's homogeneous coordinate algebra into the product algebra.

            This is the polynomial-algebra map induced by the inclusion of the
            factor's coordinate variables into its exact variable block.  The
            product's retained factor labels, rather than factor equality, select
            the block, so repeated projective factors keep distinct roles.
            """
            product = self.section_scheme()
            factors = product.factors()
            indices = factors.index_set()
            factor_label = indices(factor_label)
            labels = tuple(indices)
            position = next(
                index for index, known in enumerate(labels) if known == factor_label
            )
            factor = factors[factor_label]
            source = factor.O(1).global_sections().homogeneous_coordinate_ring()
            target = self.homogeneous_coordinate_ring()
            start, stop = self.section_space_construction().coordinate_block(position)
            source_labels = tuple(source.algebra_generating_set())
            target_labels = tuple(target.algebra_generating_set())
            if stop - start != len(source_labels):
                raise ArithmeticError(
                    "the retained multiprojective coordinate block has the wrong width"
                )
            return source.Mor(target)(
                {
                    source_label: target.algebra_generator(target_labels[start + offset])
                    for offset, source_label in enumerate(source_labels)
                }
            )


class ProjectiveLinearSystems(OwnedCategoryOverBaseRing):
    r"""Projective parameter spaces of represented section subspaces of ``O(d)``."""

    @classmethod
    def _repr_object_names(cls):
        return "projective linear systems"

    def super_categories(self):
        return [ProjectiveSchemes(self.base_ring())]

    class ParentMethods:
        def projective_linear_system_construction(self):
            return self._projective_linear_system_construction

        def line_bundle(self):
            return self.projective_linear_system_construction().line_bundle()

        def ambient_section_space(self):
            return self.line_bundle().global_sections()

        def projective_dimension(self):
            return self.relative_dimension()

        def selected_section_space(self):
            return self.projective_linear_system_construction().selected_section_space()

        def section_embedding(self):
            return self.projective_linear_system_construction().section_embedding()

        def selected_sections(self):
            embedding = self.section_embedding()
            source = self.selected_section_space()
            return indexed_family(
                source.module_generating_set(),
                lambda label: embedding(source.module_generator(label)),
                name="Selected sections of the linear system",
            )

        def restriction_map(self, closed_subscheme):
            return _projective_section_restriction(
                self.line_bundle(),
                closed_subscheme,
                source=self.selected_section_space(),
                into_complete=self.section_embedding(),
            )

        def base_locus(self):
            return self.projective_linear_system_construction().base_locus()

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
        def __init__(self, _projective_jet_construction, **rest) -> None:
            if not isinstance(_projective_jet_construction, _ProjectiveJetConstruction):
                raise TypeError("a projective jet space requires selected local construction data")
            self._projective_jet_construction = _projective_jet_construction
            super().__init__(**rest)

        def projective_jet_construction(self):
            r"""Return the selected local datum defining this jet realization."""
            return self._projective_jet_construction

        def jet_projective_space(self):
            return self.projective_jet_construction().projective_space()

        def jet_line_bundle(self):
            return self.projective_jet_construction().line_bundle()

        def jet_homogeneous_degree(self):
            return self.jet_line_bundle().degree()

        def jet_order(self):
            return self.projective_jet_construction().order()

        def jet_point(self):
            return self.projective_jet_construction().point()

        def jet_affine_chart(self):
            return self.projective_jet_construction().affine_chart()

        def jet_spectrum_point(self):
            return self.projective_jet_construction().spectrum_point()

        def jet_stalk(self):
            return self.projective_jet_construction().stalk()

        def jet_maximal_ideal(self):
            return self.projective_jet_construction().maximal_ideal()

        def jet_local_quotient(self):
            return self.projective_jet_construction().local_quotient()

        def jet_residue_field(self):
            return self.projective_jet_construction().residue_field()

        def jet_coordinate_index(self):
            coordinates = tuple(self.jet_point().point_coordinates())
            nonzero = tuple(
                index
                for index, coordinate in enumerate(coordinates)
                if coordinate != self.base_ring().zero()
            )
            if len(nonzero) != 1:
                raise ValueError("this jet condition was not selected at a coordinate point")
            return nonzero[0]


class ImposedMultiplicityLinearSystems(OwnedCategoryOverBaseRing):
    r"""Projective parameter spaces of sections satisfying one jet condition."""

    @classmethod
    def _repr_object_names(cls):
        return "linear systems with imposed multiplicity"

    def super_categories(self):
        return [ProjectiveSchemes(self.base_ring())]

    class ParentMethods:
        def imposed_multiplicity_construction(self):
            return self._imposed_multiplicity_construction

        def ambient_section_space(self):
            return self.imposed_multiplicity_construction().ambient_section_space()

        def constrained_section_space(self):
            return self.imposed_multiplicity_construction().constrained_section_space()

        def imposed_jet_evaluation(self):
            return self.imposed_multiplicity_construction().evaluation()

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


def _homogeneous_polynomial_section_space(projective_scheme, degree, *, coordinate_names=None):
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
    ring = base.polynomial_ring(names)
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
    space = base._fresh_free_module_on(
        finite_ordered_set(tuple(monomials)),
        _extra_categories=(HomogeneousPolynomialSectionSpaces(base),),
        _extra_construction_data=(
            (
                "_section_space_construction",
                _HomogeneousSectionSpaceConstruction(
                    projective_scheme,
                    degree,
                    ring,
                    exponent_data,
                ),
            ),
        ),
    )
    return space


def _multihomogeneous_polynomial_section_space(projective_product, degrees):
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
    ring = base.polynomial_ring(coordinate_names)
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

    return base._fresh_free_module_on(
        finite_ordered_set(tuple(monomials)),
        _extra_categories=(MultihomogeneousPolynomialSectionSpaces(base),),
        _extra_construction_data=(
            (
                "_section_space_construction",
                _MultihomogeneousSectionSpaceConstruction(
                    projective_product,
                    multidegree,
                    ring,
                    exponent_data,
                    tuple(block_offsets),
                ),
            ),
        ),
    )


def _coordinate_hyperplane_section_restriction(projective_space, degree, coordinate_index):
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
    source = _homogeneous_polynomial_section_space(
        projective_space,
        degree,
        coordinate_names=source_names,
    )
    native_ring = projective_space.coordinate_ring()
    hyperplane = projective_space.closed_subscheme(native_ring.gen(coordinate_index))
    target_names = tuple(
        name for index, name in enumerate(source_names) if index != coordinate_index
    )
    target = _homogeneous_polynomial_section_space(
        hyperplane,
        degree,
        coordinate_names=target_names,
    )
    source_construction = source.section_space_construction()
    target_construction = target.section_space_construction()
    target_by_exponents = {
        tuple(target_construction.exponents_of(monomial)): monomial
        for monomial in target.module_generating_set()
    }

    def image(monomial):
        exponents = source_construction.exponents_of(monomial)
        if exponents[coordinate_index]:
            return target.zero()
        restricted = exponents[:coordinate_index] + exponents[coordinate_index + 1 :]
        return target.module_generator(target_by_exponents[restricted])

    restriction = source.module_category().Mor(source, target)(
        {
            monomial: image(monomial)
            for monomial in source.module_generating_set()
        }
    )
    return restriction


class ProjectiveSectionRestrictionMap(ModuleMorphism):
    r"""The exact image-valued restriction of a represented projective section space."""

    def __init__(
        self,
        parent,
        images,
        *,
        line_bundle,
        closed_subscheme,
        coordinate_quotient,
        ambient_normal_form_space,
        image_inclusion,
    ) -> None:
        self._line_bundle = line_bundle
        self._closed_subscheme = closed_subscheme
        self._coordinate_quotient = coordinate_quotient
        self._ambient_normal_form_space = ambient_normal_form_space
        self._image_inclusion = image_inclusion
        ModuleMorphism.__init__(self, parent, images)

    def line_bundle(self):
        return self._line_bundle

    def closed_subscheme(self):
        return self._closed_subscheme

    def coordinate_quotient(self):
        return self._coordinate_quotient

    def ambient_normal_form_space(self):
        return self._ambient_normal_form_space

    def restriction_image_inclusion(self):
        return self._image_inclusion


def _projective_section_restriction(
    line_bundle,
    closed_subscheme,
    *,
    source=None,
    into_complete=None,
):
    r"""Restrict a represented section space to a projective closed subscheme.

    The codomain is the exact image of the selected source under restriction,
    not an assertion that the homogeneous coordinate quotient computes all of
    ``H^0(Z,L|_Z)``.  The closed subscheme's homogeneous equations define a
    chosen quotient of the homogeneous coordinate algebra.  Canonical normal
    forms in that quotient supply a finite ambient monomial space, and the
    module image construction corestricts to the true restriction image.
    """
    scheme = line_bundle.projective_space()
    if closed_subscheme.inclusion().codomain() is not scheme:
        raise ValueError("a section restriction is taken to a closed subscheme of its projective space")
    base = scheme.scheme_base_ring()
    if base not in OwnedFields():
        raise TypeError("the represented projective restriction-image computation requires a field base")
    complete = line_bundle.global_sections()
    source = complete if source is None else source
    if source is complete:
        into_complete = complete.module_category().Mor(complete, complete).identity()
    elif into_complete is None:
        raise ValueError("a selected section source requires its embedding into the complete section space")
    if into_complete.domain() is not source or into_complete.codomain() is not complete:
        raise ValueError("the selected section embedding has the wrong endpoints")

    coordinate_ring = complete.homogeneous_coordinate_ring()
    equations = closed_subscheme.homogeneous_defining_equations(coordinate_ring)
    quotient = AlgebrasWithChosenFinitePresentation(base)(
        coordinate_ring,
        tuple(equations),
    )

    normal_forms = {}
    monomials = []
    for label in source.module_generating_set():
        section = into_complete(source.module_generator(label))
        polynomial = complete.homogeneous_polynomial(section)
        terms = quotient.presentation_normal_form_terms(quotient(polynomial))
        normal_forms[label] = terms
        for monomial in terms:
            if not any(monomial == known for known in monomials):
                monomials.append(monomial)

    ambient = base._fresh_free_module_on(
        finite_ordered_set(tuple(monomials)),
    )
    ambient_map = source.module_category().Mor(source, ambient)(
        {
            label: ambient.linear_combination(normal_forms[label])
            for label in source.module_generating_set()
        }
    )
    image = ambient_map.image()
    restriction_images = {
        label: image.inclusion().lift(
            ambient_map(source.module_generator(label))
        )
        for label in source.module_generating_set()
    }
    return ProjectiveSectionRestrictionMap(
        source.module_category().Mor(source, image),
        restriction_images,
        line_bundle=line_bundle,
        closed_subscheme=closed_subscheme,
        coordinate_quotient=quotient,
        ambient_normal_form_space=ambient,
        image_inclusion=image.inclusion(),
    )


def _projective_linear_system(line_bundle, sections):
    r"""Return the projective linear system spanned by independent sections of ``line_bundle``."""
    scheme = line_bundle.projective_space()
    ambient = line_bundle.global_sections()
    base = scheme.scheme_base_ring()
    sections = tuple(ambient(section) for section in sections)
    if not sections:
        raise ValueError("a projective linear system requires a nonzero section subspace")
    labels = Sets.Δ[len(sections) - 1]
    selected = base._fresh_free_module_on(labels)
    images = {
        label: sections[int(labels.ranking_map()(label))]
        for label in labels
    }
    selected_map = selected.module_category().Mor(selected, ambient)(images)
    if int(selected_map.kernel().dimension()) != 0:
        raise ValueError("the supplied sections must be a basis of their selected subspace")
    embedding = selected.Mono(ambient)(images)
    polynomials = tuple(
        ambient.homogeneous_polynomial(section)
        for section in sections
    )
    base_locus = scheme.closed_subscheme(polynomials)
    system = ProjectiveSpaces(base)(len(sections) - 1)
    system._projective_linear_system_construction = _ProjectiveLinearSystemConstruction(
        line_bundle,
        embedding,
        base_locus,
    )
    return _refine_scheme(system, base, [ProjectiveLinearSystems(base)])


def _centered_jet_basis(base, dimension, jet_order):
    names = tuple(f"v{index}" for index in range(dimension))
    ring = base.polynomial_ring(names)
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


def _projective_point_jet_evaluation(line_bundle, point, jet_order):
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

    _centered_ring, local_monomials, local_by_exponents = _centered_jet_basis(
        base,
        dimension,
        jet_order,
    )
    source = line_bundle.global_sections()
    target = base._fresh_free_module_on(
        finite_ordered_set(local_monomials),
        _extra_categories=(ProjectiveJetSpaces(base),),
        _extra_construction_data=(
            (
                "_projective_jet_construction",
                _ProjectiveJetConstruction(
                    line_bundle,
                    _own_ring(SageZZ)(jet_order),
                    point,
                    chart,
                    spectrum_point,
                    local_quotient,
                ),
            ),
        ),
    )
    source_construction = source.section_space_construction()
    nonpivot = tuple(index for index in range(dimension + 1) if index != pivot)

    def image(monomial):
        homogeneous_exponents = source_construction.exponents_of(monomial)
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

    evaluation = source.module_category().Mor(source, target)(
        {
            monomial: image(monomial)
            for monomial in source.module_generating_set()
        }
    )
    return evaluation


def _coordinate_point_jet_evaluation(projective_space, degree, coordinate_index, jet_order):
    r"""Coordinate-point realization of the projective point-jet evaluation."""
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
    evaluation = _projective_point_jet_evaluation(
        projective_space.O(degree),
        point,
        jet_order,
    )
    return evaluation


def _imposed_point_multiplicity_linear_system(line_bundle, point, vanishing_order):
    r"""Projectivize sections vanishing to order at least ``r`` at ``point``."""
    evaluation = _projective_point_jet_evaluation(line_bundle, point, vanishing_order)
    constrained = evaluation.kernel()
    dimension = int(constrained.dimension())
    if dimension == 0:
        raise ValueError("the imposed condition leaves no nonzero section to projectivize")
    base = line_bundle.projective_space().scheme_base_ring()
    parameter_space = ProjectiveSpaces(base)(dimension - 1)
    parameter_space._imposed_multiplicity_construction = _ImposedMultiplicityConstruction(
        evaluation
    )
    return _refine_scheme(
        parameter_space,
        base,
        [ImposedMultiplicityLinearSystems(base)],
    )


def _coordinate_imposed_multiplicity_linear_system(projective_space, degree, coordinate_index, vanishing_order):
    r"""Coordinate-point realization of the imposed-multiplicity linear system."""
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
    result = _imposed_point_multiplicity_linear_system(
        projective_space.O(degree),
        point,
        vanishing_order,
    )
    return result


def _complete_linear_system(scheme, divisor, section_space):
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
    system = ProjectiveSpaces(base)(dimension - 1)
    system._complete_linear_system_construction = _CompleteLinearSystemConstruction(
        scheme,
        divisor,
        section_space,
    )
    return _refine_scheme(system, base, [CompleteLinearSystems(base)])


__all__ = [
    "CompleteLinearSystems",
    "HomogeneousPolynomialSectionSpaces",
    "ImposedMultiplicityLinearSystems",
    "ProjectiveJetSpaces",
    "ProjectiveLinearSystems",
]
