r"""Invertible sheaves represented by rank-one affine module descent data."""

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAffineAtlasPresentation,
    ModuleGluingDatum,
    _FiniteSchemeGluingDatum,
)


def _rank_one_generator(module):
    labels = module.module_generating_set()
    if not labels.cardinality().is_finite() or int(labels.cardinality()) != 1:
        raise TypeError("an invertible sheaf requires rank-one local modules")
    return module.module_generator(next(iter(labels)))


def _rank_one_transition(source, target, unit):
    unit = target.base_ring()(unit)
    if not unit.is_unit():
        raise ValueError("an invertible-sheaf transition scalar must be a unit")
    source_generator = _rank_one_generator(source)
    target_generator = _rank_one_generator(target)
    forward = source.module_category().Mor(source, target)(
        lambda _label: target.scalar_multiple(unit, target_generator)
    )
    inverse_unit = source.base_ring()(unit.inverse_of_unit())
    inverse = target.module_category().Mor(target, source)(
        lambda _label: source.scalar_multiple(inverse_unit, source_generator)
    )
    return source.module_category().Core().Mor(source, target)(forward, inverse)


class InvertibleSheaf(SageObject):
    r"""A line bundle represented by rank-one free descent on one affine cover."""

    def __init__(self, gluing_datum) -> None:
        if not isinstance(gluing_datum, ModuleGluingDatum):
            raise TypeError("an invertible sheaf requires represented module descent data")
        self._gluing_datum = gluing_datum
        self._transition_units = {}
        for module in gluing_datum.local_modules():
            ring = module.base_ring()
            if module not in FinitelyGeneratedFreeModules(ring) or int(module.module_rank()) != 1:
                raise TypeError(
                    "an invertible sheaf requires a rank-one finite free module on every chart"
                )
        for left in range(len(gluing_datum.local_modules())):
            for right in range(left + 1, len(gluing_datum.local_modules())):
                self._transition_units[left, right] = self._extract_transition_unit(
                    left,
                    right,
                )

    def gluing_datum(self):
        return self._gluing_datum

    def cover(self):
        return self.gluing_datum().cover()

    def scheme(self):
        return self.gluing_datum().scheme()

    ringed_space = scheme

    def sheaf(self):
        return self.gluing_datum().sheaf()

    def local_module(self, index):
        return self.gluing_datum().local_module(index)

    def local_trivialization(self, index):
        r"""Return the literal rank-one free chart module trivializing this sheaf."""

        module = self.local_module(index)
        identity = module.module_category().Mor(module, module).identity()
        return module.module_category().Core().Mor(module, module)(identity, identity)

    def _extract_transition_unit(self, source_index, target_index):
        transition = self.gluing_datum().transition(source_index, target_index).forward()
        source = transition.domain()
        target = transition.codomain()
        source_generator = _rank_one_generator(source)
        target_labels = target.module_generating_set()
        target_label = next(iter(target_labels))
        coefficients = target.framing_coefficients(transition(source_generator))
        unit = (
            coefficients[target_label]
            if target_label in coefficients
            else target.base_ring().zero()
        )
        if not unit.is_unit():
            raise ValueError(
                "a rank-one descent transition must multiply the local basis by a unit"
            )
        return unit

    def transition_unit(self, source_index, target_index):
        r"""Return the unit ``u_ij`` with ``e_i |-> u_ij e_j`` on the overlap."""

        source_index = int(source_index)
        target_index = int(target_index)
        if source_index == target_index:
            raise ValueError("a transition unit is attached to two distinct charts")
        if source_index < target_index:
            return self._transition_units[source_index, target_index]
        return self._transition_units[target_index, source_index].inverse_of_unit()

    def global_sections(self):
        return self.gluing_datum().compatible_sections()

    sections = global_sections

    def morphism_to(self, target, local_maps):
        r"""Return the descent morphism represented by the supplied chart maps."""

        if not isinstance(target, InvertibleSheaf):
            raise TypeError("an invertible-sheaf morphism requires an invertible-sheaf target")
        if target.cover() is not self.cover():
            raise ValueError("invertible-sheaf descent morphisms require one affine cover")
        return self.gluing_datum().Mor(target.gluing_datum())(local_maps)

    @classmethod
    def _from_transition_units(cls, cover, transition_units):
        local_modules = tuple(
            open_subscheme.coordinate_algebra().free_module(1)
            for open_subscheme in cover.opens()
        )
        transitions = {}
        for left in range(len(local_modules)):
            for right in range(left + 1, len(local_modules)):
                source = cover.restrict_module(local_modules[left], left, right)
                target = cover.restrict_module(local_modules[right], right, left)
                transitions[left, right] = _rank_one_transition(
                    source,
                    target,
                    transition_units[left, right],
                )
        return cls(cover.glue_modules(local_modules, transitions))

    @classmethod
    def trivial(cls, cover):
        r"""Return ``O_X`` represented as the rank-one trivial bundle on ``cover``."""

        units = {
            (left, right): cover.overlap(left, right).coordinate_algebra().one()
            for left in range(len(cover.opens()))
            for right in range(left + 1, len(cover.opens()))
        }
        return cls._from_transition_units(cover, units)

    def tensor_product(self, other):
        r"""Tensor two line bundles by multiplying their transition units."""

        if not isinstance(other, InvertibleSheaf):
            raise TypeError("line-bundle tensor product requires two invertible sheaves")
        if other.cover() is not self.cover():
            raise ValueError("line-bundle tensor product currently requires one affine cover")
        units = {
            (left, right): self.transition_unit(left, right)
            * other.transition_unit(left, right)
            for left in range(len(self.cover().opens()))
            for right in range(left + 1, len(self.cover().opens()))
        }
        return self._from_transition_units(self.cover(), units)

    def tensor_power(self, exponent):
        r"""Return ``self^tensor exponent`` using powers of the transition units."""

        exponent = int(exponent)
        units = {}
        for left in range(len(self.cover().opens())):
            for right in range(left + 1, len(self.cover().opens())):
                unit = self.transition_unit(left, right)
                units[left, right] = (
                    unit**exponent
                    if exponent >= 0
                    else unit.inverse_of_unit() ** (-exponent)
                )
        return self._from_transition_units(self.cover(), units)

    def dual_sheaf(self):
        r"""Return the dual line bundle, with transition units ``u_ij^{-1}``."""

        return self.tensor_power(-1)

    def _repr_(self):
        return f"Invertible sheaf on {self.scheme()} trivialized by {self.cover()}"


class FiniteAtlasInvertibleSheaf(InvertibleSheaf):
    r"""A line bundle on a finite glued affine atlas via transition functions.

    Unlike :class:`InvertibleSheaf`, whose descent datum lives on one affine
    scheme's distinguished-open cover and hence has a literal common overlap
    ring, a finite glued atlas has two isomorphic presentations of every
    overlap.  A transition unit ``u_ij`` therefore lives on the source-side
    overlap, and the triple cocycle is

    ``u_ik = u_ij * phi_ij^*(u_jk)``

    after restriction to the source-side triple overlap.  The scheme gluing
    datum already owns ``phi_ij`` and its restrictions, so this class only
    adds the rank-one descent data rather than duplicating scheme descent.
    """

    def __init__(
        self,
        gluing_datum,
        transition_units,
        *,
        section_space=None,
        associated_divisor=None,
    ) -> None:
        if not isinstance(
            gluing_datum,
            (_FiniteSchemeGluingDatum, FiniteAffineAtlasPresentation),
        ):
            raise TypeError(
                "finite-atlas line-bundle descent requires a represented finite affine atlas"
            )
        self._finite_gluing_datum = gluing_datum
        self._section_space = section_space
        self._associated_divisor = associated_divisor
        self._local_modules = {
            index: gluing_datum.chart(index).coordinate_algebra().free_module(1)
            for index in gluing_datum.chart_indices()
        }
        expected = set(gluing_datum.transition_index_set())
        supplied = dict(transition_units)
        if set(supplied) != expected:
            raise ValueError("finite-atlas line-bundle descent requires one unit for each ordered atlas pair")
        self._transition_units = {}
        for source_index, target_index in expected:
            ring = gluing_datum.overlap(source_index, target_index).coordinate_algebra()
            unit = ring(supplied[source_index, target_index])
            if not unit.is_unit():
                raise ValueError("a finite-atlas line-bundle transition must be a unit on the overlap")
            self._transition_units[source_index, target_index] = unit
        self._verify_finite_atlas_cocycle()

    def gluing_datum(self):
        return self._finite_gluing_datum

    def cover(self):
        return self.gluing_datum()

    def scheme(self):
        return self.gluing_datum().scheme()

    ringed_space = scheme

    def chart_indices(self):
        return self.gluing_datum().chart_indices()

    def local_module(self, index):
        index = self.gluing_datum().normalize_chart_index(index)
        return self._local_modules[index]

    def local_trivialization(self, index):
        module = self.local_module(index)
        identity = module.module_category().Mor(module, module).identity()
        return module.module_category().Core().Mor(module, module)(identity, identity)

    def associated_divisor(self):
        if self._associated_divisor is None:
            raise TypeError("this line bundle was not constructed from a selected divisor")
        return self._associated_divisor

    def _stored_pair(self, source_index, target_index):
        datum = self.gluing_datum()
        source_index = datum.normalize_chart_index(source_index)
        target_index = datum.normalize_chart_index(target_index)
        if source_index == target_index:
            raise ValueError("a transition function belongs to two distinct charts")
        ranking = datum.chart_index_set().ranking_map()
        return (
            (source_index, target_index)
            if ranking(source_index) < ranking(target_index)
            else (target_index, source_index)
        )

    def transition_unit(self, source_index, target_index):
        datum = self.gluing_datum()
        source_index = datum.normalize_chart_index(source_index)
        target_index = datum.normalize_chart_index(target_index)
        pair = self._stored_pair(source_index, target_index)
        unit = self._transition_units[pair]
        if pair == (source_index, target_index):
            return unit
        reverse_transition = datum.transition_between(source_index, target_index).forward()
        return reverse_transition.coordinate_algebra_morphism()(
            unit.inverse_of_unit()
        )

    def _restrict_pair_unit_to_triple(
        self,
        source_index,
        target_index,
        third_index,
        unit,
    ):
        datum = self.gluing_datum()
        pair_overlap = datum.overlap(source_index, target_index)
        triple = datum.triple_overlap(source_index, target_index, third_index)
        into_pair = pair_overlap.corestriction(triple.inclusion())
        return into_pair.coordinate_algebra_morphism()(unit)

    def _verify_finite_atlas_cocycle(self) -> None:
        from itertools import combinations

        datum = self.gluing_datum()
        for left, middle, right in combinations(tuple(datum.chart_indices()), 3):
            left_middle = self._restrict_pair_unit_to_triple(
                left,
                middle,
                right,
                self.transition_unit(left, middle),
            )
            middle_right = self._restrict_pair_unit_to_triple(
                middle,
                right,
                left,
                self.transition_unit(middle, right),
            )
            pullback = datum.transition_on_triple(
                left,
                middle,
                right,
            ).coordinate_algebra_morphism()
            left_right = self._restrict_pair_unit_to_triple(
                left,
                right,
                middle,
                self.transition_unit(left, right),
            )
            if left_middle * pullback(middle_right) != left_right:
                raise ValueError("finite-atlas line-bundle transition functions fail the triple cocycle")

    @classmethod
    def _from_transition_units(cls, cover, transition_units):
        return cls(cover, transition_units)

    @classmethod
    def trivial(cls, gluing_datum):
        units = {
            pair: gluing_datum.overlap(*pair).coordinate_algebra().one()
            for pair in gluing_datum.transition_index_set()
        }
        return cls(gluing_datum, units)

    def tensor_product(self, other):
        if not isinstance(other, FiniteAtlasInvertibleSheaf):
            raise TypeError("finite-atlas tensor product requires two finite-atlas invertible sheaves")
        if other.gluing_datum() is not self.gluing_datum():
            raise ValueError("line-bundle tensor product requires one finite atlas")
        units = {
            pair: self.transition_unit(*pair) * other.transition_unit(*pair)
            for pair in self.gluing_datum().transition_index_set()
        }
        return type(self)(self.gluing_datum(), units)

    def tensor_power(self, exponent):
        exponent = int(exponent)
        units = {}
        for pair in self.gluing_datum().transition_index_set():
            unit = self.transition_unit(*pair)
            units[pair] = (
                unit**exponent
                if exponent >= 0
                else unit.inverse_of_unit() ** (-exponent)
            )
        return type(self)(self.gluing_datum(), units)

    def dual_sheaf(self):
        return self.tensor_power(-1)

    def global_sections(self):
        assert self._section_space is not None, (
            "global sections are represented here only when this finite-atlas line bundle "
            "carries a selected section-space computation"
        )
        return self._section_space

    sections = global_sections

    @cached_method
    def module_sheaf(self):
        from dzack_research.preamble.categories.schemes.gluing import (
            _finite_atlas_line_bundle_module_sheaf,
        )

        return _finite_atlas_line_bundle_module_sheaf(self)

    @cached_method
    def compatible_sections(self):
        sections = self.module_sheaf().global_sections()
        sections._preamble_line_bundle = self
        return sections

    def sheaf(self):
        return self

    def _repr_(self):
        return f"Invertible sheaf on finite affine atlas of {self.scheme()}"


class _LineBundleBaseChangeDatum:
    r"""The selected source and scalar map defining one line-bundle base change.

    The changed bundle owns this datum from construction time.  Its projection
    and section comparison are consequences of that defining datum together
    with the changed bundle itself, so they are derived rather than attached
    later as provenance.
    """

    def __init__(self, source_bundle, ring_map, exponent_attribute) -> None:
        self._source_bundle = source_bundle
        self._ring_map = ring_map
        self._exponent_attribute = exponent_attribute

    def source_bundle(self):
        return self._source_bundle

    def ring_map(self):
        return self._ring_map

    def projection(self, changed_bundle):
        return changed_bundle.scheme().left_projection()

    def section_comparison(self, changed_bundle):
        source_sections = self.source_bundle().global_sections()
        target_sections = changed_bundle.global_sections()
        return _section_base_change_comparison(
            source_sections,
            target_sections,
            self.ring_map(),
            self._exponent_attribute,
        )


def _section_base_change_comparison(source_sections, target_sections, ring_map, exponent_attribute):
    r"""Compare scalar extension of an exponent-framed section module with the target one."""
    changed_source = source_sections.base_change(ring_map)
    source_exponents = getattr(source_sections, exponent_attribute)
    target_exponents = getattr(target_sections, exponent_attribute)
    source_by_exponents = {
        exponents: label for label, exponents in source_exponents.items()
    }
    target_by_exponents = {
        exponents: label for label, exponents in target_exponents.items()
    }
    forward = changed_source.module_category().Mor(changed_source, target_sections)(
        lambda label: target_sections.module_generator(
            target_by_exponents[source_exponents[label]]
        )
    )
    inverse = target_sections.module_category().Mor(target_sections, changed_source)(
        lambda label: changed_source.module_generator(
            source_by_exponents[target_exponents[label]]
        )
    )
    return changed_source.module_category().Core().Mor(changed_source, target_sections)(
        forward, inverse
    )


def _base_change_datum(bundle):
    datum = bundle._base_change_datum
    if datum is None:
        raise ValueError("this line bundle was not selected as a scalar base change")
    return datum


def _base_change_source_bundle(bundle):
    return _base_change_datum(bundle).source_bundle()


def _base_change_projection(bundle):
    return _base_change_datum(bundle).projection(bundle)


def _section_base_change_comparison_of(bundle):
    try:
        return _base_change_datum(bundle).section_comparison(bundle)
    except NotImplementedError:
        raise NotImplementedError(
            "this line-bundle base change has no represented global-section comparison"
        ) from None


class ProjectiveSpaceLineBundle(FiniteAtlasInvertibleSheaf):
    r"""The standard ``O(d)`` on one represented projective space.

    This is a specialization of finite-atlas invertible-sheaf descent.  Its
    local basis on ``U_i`` has transition ``(x_j/x_i)^d`` to ``U_j``; tensor
    product therefore adds degrees and duality negates them.
    """

    def __init__(self, projective_space, degree, *, base_change_datum=None) -> None:
        from dzack_research.preamble.categories.divisors.linear_systems import (
            _homogeneous_polynomial_section_space,
        )
        from dzack_research.preamble.categories.schemes.schemes import (
            ProjectiveSpaces,
        )

        base = projective_space.scheme_base_ring()
        if projective_space not in ProjectiveSpaces(base):
            raise TypeError("O(d) is constructed here on a represented projective space")
        self._projective_space = projective_space
        self._degree = _own_ring(SageZZ)(degree)
        self._base_change_datum = base_change_datum
        atlas = projective_space.standard_affine_atlas()
        units = {}
        for source_index, target_index in atlas.transition_index_set():
            overlap = atlas.overlap(source_index, target_index)
            restriction = overlap.inclusion().coordinate_algebra_morphism()
            ratio = restriction(
                projective_space._standard_chart_coordinate(
                    source_index,
                    target_index,
                )
            )
            units[source_index, target_index] = (
                ratio ** int(self._degree)
                if self._degree >= 0
                else ratio.inverse_of_unit() ** int(-self._degree)
            )
        section_space = (
            _homogeneous_polynomial_section_space(
                projective_space,
                self._degree,
                coordinate_names=projective_space.variable_names(),
            )
            if self._degree >= 0
            else None
        )
        super().__init__(atlas, units, section_space=section_space)

    def projective_space(self):
        return self._projective_space

    def degree(self):
        return self._degree

    def tensor_product(self, other):
        if isinstance(other, ProjectiveSpaceLineBundle):
            if other.projective_space() is not self.projective_space():
                raise ValueError("projective line-bundle tensor product requires one projective space")
            return type(self)(self.projective_space(), self.degree() + other.degree())
        return super().tensor_product(other)

    def tensor_power(self, exponent):
        exponent = _own_ring(SageZZ)(exponent)
        if exponent == 1:
            return self
        return type(self)(self.projective_space(), exponent * self.degree())

    def dual_sheaf(self):
        return type(self)(self.projective_space(), -self.degree())

    def is_ample(self) -> bool:
        return int(self.projective_space().relative_dimension()) == 0 or self.degree() > 0

    def is_basepoint_free(self) -> bool:
        return self.degree() >= 0

    is_globally_generated = is_basepoint_free

    def restriction_map(self, closed_subscheme):
        from dzack_research.preamble.categories.divisors.linear_systems import (
            _projective_section_restriction,
        )

        return _projective_section_restriction(self, closed_subscheme)

    def restrict_to(self, closed_subscheme):
        r"""Return ``i^* O(d)`` for a represented projective closed immersion ``i``."""
        return ProjectiveSubschemeLineBundle(closed_subscheme, self)

    def pullback(self, morphism):
        r"""Return ``f^*O(d)`` for a represented projective-product projection.

        For the projection ``pi_i : prod_j P_j -> P_i``, the pullback is the
        multiprojective line bundle with degree ``d`` in the selected factor
        and degree zero in every other factor.  The retained projection label,
        rather than equality of repeated factors, selects that role.
        """
        from dzack_research.preamble.categories.schemes.schemes import (
            ProductProjectiveSpaces,
        )

        if morphism.codomain() is not self.projective_space():
            raise ValueError("line-bundle pullback requires a morphism into the bundle's projective space")
        source = morphism.domain()
        base = source.scheme_base_ring()
        assert source in ProductProjectiveSpaces(base), (
            "projective-space line-bundle pullback is represented here for product projections"
        )
        label = getattr(morphism, "_preamble_product_projection_label", None)
        assert label is not None, (
            "projective-space line-bundle pullback requires the selected product-projection role"
        )
        labels = tuple(source.factors().index_set())
        label = source.factors().index_set()(label)
        if morphism is not source.projection(label):
            raise ValueError("the retained projection label does not identify this morphism")
        return source.O(
            tuple(self.degree() if factor_label == label else 0 for factor_label in labels)
        )

    def linearize(self, scheme_action_functor, character):
        from dzack_research.preamble.categories.divisors.linearizations import (
            _ProjectiveLineBundleLinearization,
        )

        return _ProjectiveLineBundleLinearization(
            self,
            scheme_action_functor,
            character,
        )

    def c2_coordinate_swap_linearization(self, twist=1):
        r"""Linearize this ``O(d)`` for coordinate swap with the selected C2 character."""
        from dzack_research.preamble.categories.group.groups import OwnedGroups

        base = self.projective_space().scheme_base_ring()
        group = OwnedGroups().C(2)
        scalar = base(twist)
        match scalar in (base.one(), -base.one()):
            case False:
                raise ValueError("a C2 character twist is +1 or -1")
            case True:
                pass
        action = self.projective_space().coordinate_swap_action(group)

        def character(element):
            match group(element) == group.one():
                case True:
                    return base.one()
                case False:
                    return scalar

        return self.linearize(action, character)

    def linear_system(self, sections=None):
        from dzack_research.preamble.categories.divisors.linear_systems import (
            _projective_linear_system,
        )

        selected = (
            tuple(self.global_sections().module_generators())
            if sections is None
            else tuple(sections)
        )
        return _projective_linear_system(self, selected)

    def jet_evaluation(self, point, order):
        from dzack_research.preamble.categories.divisors.linear_systems import (
            _projective_point_jet_evaluation,
        )

        return _projective_point_jet_evaluation(self, point, order)

    def sections_vanishing_to_order(self, point, order):
        return self.jet_evaluation(point, order).kernel()

    def imposed_multiplicity_linear_system(self, point, order):
        from dzack_research.preamble.categories.divisors.linear_systems import (
            _imposed_point_multiplicity_linear_system,
        )

        return _imposed_point_multiplicity_linear_system(self, point, order)

    def homogeneous_polynomial_sections(self):
        return self.global_sections()

    def homogeneous_polynomial_comparison(self):
        sections = self.global_sections()
        identity = sections.module_category().Mor(sections, sections).identity()
        return sections.module_category().Core().Mor(sections, sections)(
            identity, identity
        )

    def compatible_section(self, section):
        r"""Dehomogenize one global section on the standard affine atlas.

        On the chart where homogeneous coordinate ``x_{i,j_i}`` of each
        factor is nonzero, ``O(d_i)`` is trivialized by ``x_{i,j_i}^{d_i}``.
        Dividing a multihomogeneous monomial by those selected powers therefore
        replaces every selected coordinate by ``1`` and every other coordinate
        by the corresponding affine ratio.  The finite-atlas equalizer checks
        that these chart coefficients glue through the line-bundle transitions.
        """
        sections = self.global_sections()
        section = sections(section)
        coefficients = sections.framing_coefficients(section)
        exponent_data = sections._preamble_multihomogeneous_exponents
        atlas = self.gluing_datum()
        product = self.projective_product()
        factors = product.factors()
        factor_labels = tuple(factors.index_set())
        positions = {label: position for position, label in enumerate(factor_labels)}
        module_sheaf = self.module_sheaf()
        components = {}
        for choice in atlas.chart_indices():
            chart = atlas.chart(choice)
            chart_ring = chart.coordinate_algebra()
            scalar_map = chart_ring.algebra_structure_morphism()
            local_coefficient = chart_ring.zero()
            for monomial, coefficient in coefficients.items():
                term = scalar_map(coefficient)
                blocks = exponent_data[monomial]
                for label, block in zip(factor_labels, blocks, strict=True):
                    position = positions[label]
                    selected = choice[position]
                    factor = factors[label]
                    projection = chart.projection(label).coordinate_algebra_morphism()
                    for coordinate, exponent in enumerate(block):
                        if not exponent or coordinate == selected:
                            continue
                        term *= projection(
                            factor._standard_chart_coordinate(selected, coordinate)
                        ) ** int(exponent)
                local_coefficient += term
            module = module_sheaf.sections_on_chart(choice)
            generator = _rank_one_generator(module)
            components[choice] = module.scalar_multiple(local_coefficient, generator)
        return self.compatible_sections().from_global_section_components(
            components,
            section,
        )

    def section_multiplication(self, other):
        from dzack_research.preamble.categories.modules.pure.modules import BilinearMap

        if not isinstance(other, ProjectiveSpaceLineBundle):
            raise TypeError("section multiplication requires two projective-space line bundles")
        if other.projective_space() is not self.projective_space():
            raise ValueError("section multiplication requires one projective space")
        assert self.degree() >= 0 and other.degree() >= 0, (
            "homogeneous-polynomial section multiplication is represented here in nonnegative degrees"
        )
        target_bundle = self.tensor_product(other)
        left = self.global_sections()
        right = other.global_sections()
        target = target_bundle.global_sections()
        left_exponents = left._preamble_homogeneous_exponents
        right_exponents = right._preamble_homogeneous_exponents
        target_by_exponents = {
            exponents: monomial
            for monomial, exponents in target._preamble_homogeneous_exponents.items()
        }

        def product(left_monomial, right_monomial):
            exponents = tuple(
                left_power + right_power
                for left_power, right_power in zip(
                    left_exponents[left_monomial],
                    right_exponents[right_monomial],
                    strict=True,
                )
            )
            return target.module_generator(target_by_exponents[exponents])

        return BilinearMap(left, right, target, product)

    @cached_method
    def section_ring(self):
        from dzack_research.preamble.categories.divisors.section_rings import SectionRings

        return SectionRings(self.scheme().scheme_base_ring())(self)

    def base_change(self, ring_map):
        changed_space = self.projective_space().base_change(ring_map)
        datum = _LineBundleBaseChangeDatum(
            self,
            ring_map,
            "_preamble_homogeneous_exponents",
        )
        return type(self)(
            changed_space,
            self.degree(),
            base_change_datum=datum,
        )

    def base_change_source_bundle(self):
        return _base_change_source_bundle(self)

    def base_change_projection(self):
        return _base_change_projection(self)

    def section_base_change_comparison(self):
        return _section_base_change_comparison_of(self)

    def _repr_(self):
        return f"O({self.degree()}) on {self.projective_space()}"



class ProjectiveSubschemeLineBundle(SageObject):
    r"""The pullback ``i^* O_P(d)`` along a projective closed immersion.

    The defining datum is the actual closed immersion together with the
    ambient projective line bundle.  No second projective-coordinate sheaf is
    built on the subscheme.  This is the line-bundle object needed by
    adjunction and strict-transform comparisons; computations of sections may
    use the existing image-valued restriction map separately.
    """

    def __init__(self, closed_subscheme, ambient_line_bundle) -> None:
        from dzack_research.preamble.categories.schemes.schemes import (
            ClosedSubschemes,
            ProjectiveSpaces,
        )

        base = closed_subscheme.scheme_base_ring()
        if closed_subscheme not in ClosedSubschemes(base):
            raise TypeError("a restricted projective line bundle requires a closed subscheme")
        ambient = closed_subscheme.inclusion().codomain()
        if ambient not in ProjectiveSpaces(base):
            raise TypeError("the selected O_X(d) construction requires projective-space ambient")
        if not isinstance(ambient_line_bundle, ProjectiveSpaceLineBundle):
            raise TypeError("the ambient bundle must be a represented projective O(d)")
        if ambient_line_bundle.projective_space() is not ambient:
            raise ValueError("the ambient line bundle belongs to a different projective space")
        self._scheme = closed_subscheme
        self._ambient_line_bundle = ambient_line_bundle
        self._pullback_morphism = closed_subscheme.inclusion()

    def scheme(self):
        return self._scheme

    def pullback_morphism(self):
        return self._pullback_morphism

    inclusion = pullback_morphism

    def ambient_line_bundle(self):
        return self._ambient_line_bundle

    def degree(self):
        return self.ambient_line_bundle().degree()

    def tensor_product(self, other):
        if not isinstance(other, ProjectiveSubschemeLineBundle):
            raise TypeError("restricted projective tensor product requires two O_X(d) bundles")
        if other.scheme() is not self.scheme():
            raise ValueError("restricted line-bundle tensor product requires one scheme")
        return type(self)(
            self.scheme(),
            self.ambient_line_bundle().tensor_product(other.ambient_line_bundle()),
        )

    def tensor_power(self, exponent):
        exponent = _own_ring(SageZZ)(exponent)
        if exponent == 1:
            return self
        return type(self)(
            self.scheme(),
            self.ambient_line_bundle().tensor_power(exponent),
        )

    def dual_sheaf(self):
        return type(self)(self.scheme(), self.ambient_line_bundle().dual_sheaf())

    def is_ample(self) -> bool:
        r"""Decide ampleness for restrictions of ``O(d)`` to projective subschemes."""
        if int(self.scheme().dimension()) == 0:
            return True
        return self.degree() > 0

    def section_restriction_map(self):
        return self.ambient_line_bundle().restriction_map(self.scheme())

    def represented_global_section_image(self):
        return self.section_restriction_map().codomain()

    def canonical_isomorphism_to(self, target):
        r"""Return the canonical comparison with an equal-degree presentation on this scheme."""
        return _ProjectiveSubschemeLineBundleIsomorphism(self, target)

    def _repr_(self):
        return f"O({self.degree()}) restricted to {self.scheme()}"


class _ProjectiveSubschemeLineBundleIsomorphism(SageObject):
    r"""The selected identity of two represented ``O_X(d)`` pullback presentations.

    Two objects here carry the same closed immersion and the same integer
    degree but may have arisen by different tensor constructions.  Their
    canonical comparison is induced by the identity of ``O_P(d)`` before
    pullback.  The source and target remain distinct construction objects.
    """

    def __init__(self, source, target) -> None:
        if not isinstance(source, ProjectiveSubschemeLineBundle) or not isinstance(
            target, ProjectiveSubschemeLineBundle
        ):
            raise TypeError("this line-bundle isomorphism compares two represented O_X(d) bundles")
        if source.scheme() is not target.scheme():
            raise ValueError("a line-bundle isomorphism lies over one scheme")
        if source.degree() != target.degree():
            raise ValueError("the selected projective line-bundle comparison requires equal degrees")
        self._source = source
        self._target = target

    def domain(self):
        return self._source

    source = domain

    def codomain(self):
        return self._target

    target = codomain

    def inverse(self):
        return type(self)(self.codomain(), self.domain())

    def __mul__(self, other):
        if not isinstance(other, _ProjectiveSubschemeLineBundleIsomorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return type(self)(other.domain(), self.codomain())

    def _repr_(self):
        return f"Line-bundle isomorphism {self.domain()} ~= {self.codomain()}"

def _projective_o(projective_space, degree):
    r"""Return the standard line bundle ``O(d)`` on ``P^n``."""
    return ProjectiveSpaceLineBundle(projective_space, degree)


class ProductProjectiveLineBundle(FiniteAtlasInvertibleSheaf):
    r"""The standard ``O(d_1,...,d_r)`` on a product of projective spaces."""

    def __init__(self, projective_product, degrees, *, base_change_datum=None) -> None:
        from dzack_research.preamble.categories.divisors.linear_systems import (
            _multihomogeneous_polynomial_section_space,
        )
        from dzack_research.preamble.categories.schemes.schemes import (
            ProductProjectiveSpaces,
        )
        from dzack_research.preamble.categories.sets.indexed_families import (
            IndexedFamily,
            finite_indexed_family,
        )

        base = projective_product.scheme_base_ring()
        if projective_product not in ProductProjectiveSpaces(base):
            raise TypeError("O(d_1,...,d_r) requires a product of projective spaces")
        factors = projective_product.factors()
        factor_indices = factors.index_set()
        factor_labels = tuple(factor_indices)
        if isinstance(degrees, IndexedFamily):
            if degrees.index_set() is not factor_indices:
                raise ValueError("a line-bundle multidegree uses the exact factor index set")
            degree_values = tuple(
                _own_ring(SageZZ)(degrees[label]) for label in factor_labels
            )
        else:
            degree_values = tuple(_own_ring(SageZZ)(degree) for degree in degrees)
            if len(degree_values) != len(factor_labels):
                raise ValueError("a line-bundle multidegree has one degree per projective factor")
        self._projective_product = projective_product
        self._base_change_datum = base_change_datum
        self._multidegree = finite_indexed_family(
            factor_indices,
            lambda label: degree_values[
                next(
                    position
                    for position, known_label in enumerate(factor_labels)
                    if known_label == label
                )
            ],
            name="Line-bundle multidegree",
        )
        atlas = projective_product.standard_affine_atlas()
        positions = {label: position for position, label in enumerate(factor_labels)}
        units = {}
        for source_choice, target_choice in atlas.transition_index_set():
            overlap = atlas.overlap(source_choice, target_choice)
            overlap_restriction = overlap.inclusion().coordinate_algebra_morphism()
            chart = atlas.chart(source_choice)
            unit = overlap.coordinate_algebra().one()
            for label in factor_labels:
                position = positions[label]
                source_index = source_choice[position]
                target_index = target_choice[position]
                if source_index == target_index:
                    continue
                factor = factors[label]
                chart_pullback = chart.projection(label).coordinate_algebra_morphism()
                ratio = overlap_restriction(
                    chart_pullback(
                        factor._standard_chart_coordinate(source_index, target_index)
                    )
                )
                degree = self.multidegree()[label]
                unit *= (
                    ratio ** int(degree)
                    if degree >= 0
                    else ratio.inverse_of_unit() ** int(-degree)
                )
            units[source_choice, target_choice] = unit
        section_space = (
            _multihomogeneous_polynomial_section_space(
                projective_product,
                self.multidegree(),
            )
            if all(self.multidegree()[label] >= 0 for label in factor_labels)
            else None
        )
        super().__init__(atlas, units, section_space=section_space)

    def projective_product(self):
        return self._projective_product

    def multidegree(self):
        return self._multidegree

    def tensor_product(self, other):
        if isinstance(other, ProductProjectiveLineBundle):
            if other.projective_product() is not self.projective_product():
                raise ValueError("multiprojective line-bundle tensor product requires one scheme")
            labels = tuple(self.multidegree().index_set())
            return type(self)(
                self.projective_product(),
                tuple(
                    self.multidegree()[label] + other.multidegree()[label]
                    for label in labels
                ),
            )
        return super().tensor_product(other)

    def tensor_power(self, exponent):
        exponent = _own_ring(SageZZ)(exponent)
        if exponent == 1:
            return self
        return type(self)(
            self.projective_product(),
            tuple(
                exponent * self.multidegree()[label]
                for label in self.multidegree().index_set()
            ),
        )

    def dual_sheaf(self):
        return self.tensor_power(-1)

    def is_ample(self) -> bool:
        factors = self.projective_product().factors()
        return all(
            int(factors[label].relative_dimension()) == 0
            or self.multidegree()[label] > 0
            for label in factors.index_set()
        )

    def is_basepoint_free(self) -> bool:
        return all(
            self.multidegree()[label] >= 0
            for label in self.multidegree().index_set()
        )

    is_globally_generated = is_basepoint_free

    def restrict_to(self, closed_subscheme):
        r"""Return the restricted multiprojective line bundle on ``closed_subscheme``."""
        return ProductProjectiveSubschemeLineBundle(closed_subscheme, self)

    def linearize(self, scheme_action_functor, character):
        from dzack_research.preamble.categories.divisors.linearizations import (
            _ProductProjectiveLineBundleLinearization,
        )

        return _ProductProjectiveLineBundleLinearization(
            self,
            scheme_action_functor,
            character,
        )

    def c2_diagonal_sign_linearization(self, twist=1):
        r"""Linearize this multidegree for the diagonal sign action and selected C2 character."""
        from dzack_research.preamble.categories.group.groups import OwnedGroups

        base = self.projective_product().scheme_base_ring()
        group = OwnedGroups().C(2)
        scalar = base(twist)
        match scalar in (base.one(), -base.one()):
            case False:
                raise ValueError("a C2 character twist is +1 or -1")
            case True:
                pass
        action = self.projective_product().c2_diagonal_sign_action(group)

        def character(element):
            match group(element) == group.one():
                case True:
                    return base.one()
                case False:
                    return scalar

        return self.linearize(action, character)

    def homogeneous_polynomial_sections(self):
        return self.global_sections()

    def homogeneous_polynomial_comparison(self):
        sections = self.global_sections()
        identity = sections.module_category().Mor(sections, sections).identity()
        return sections.module_category().Core().Mor(sections, sections)(
            identity, identity
        )

    def section_multiplication(self, other):
        from dzack_research.preamble.categories.modules.pure.modules import BilinearMap

        if not isinstance(other, ProductProjectiveLineBundle):
            raise TypeError("multihomogeneous section multiplication requires two multiprojective line bundles")
        if other.projective_product() is not self.projective_product():
            raise ValueError("multihomogeneous section multiplication requires one scheme")
        target_bundle = self.tensor_product(other)
        left = self.global_sections()
        right = other.global_sections()
        target = target_bundle.global_sections()
        left_exponents = left._preamble_multihomogeneous_exponents
        right_exponents = right._preamble_multihomogeneous_exponents
        target_by_exponents = {
            exponents: monomial
            for monomial, exponents in target._preamble_multihomogeneous_exponents.items()
        }

        def product(left_monomial, right_monomial):
            exponents = tuple(
                tuple(a + b for a, b in zip(left_block, right_block, strict=True))
                for left_block, right_block in zip(
                    left_exponents[left_monomial],
                    right_exponents[right_monomial],
                    strict=True,
                )
            )
            return target.module_generator(target_by_exponents[exponents])

        return BilinearMap(left, right, target, product)

    @cached_method
    def section_ring(self):
        from dzack_research.preamble.categories.divisors.section_rings import SectionRings

        return SectionRings(self.scheme().scheme_base_ring())(self)

    def base_change(self, ring_map):
        changed_product = self.projective_product().base_change(ring_map)
        datum = _LineBundleBaseChangeDatum(
            self,
            ring_map,
            "_preamble_multihomogeneous_exponents",
        )
        return type(self)(
            changed_product,
            tuple(
                self.multidegree()[label]
                for label in self.multidegree().index_set()
            ),
            base_change_datum=datum,
        )

    def base_change_source_bundle(self):
        return _base_change_source_bundle(self)

    def base_change_projection(self):
        return _base_change_projection(self)

    def section_base_change_comparison(self):
        return _section_base_change_comparison_of(self)

    def _repr_(self):
        degrees = tuple(self.multidegree()[label] for label in self.multidegree().index_set())
        return f"O{degrees} on {self.projective_product()}"



class ProductProjectiveSubschemeLineBundle(SageObject):
    r"""The pullback of ``O(d_1,...,d_r)`` to a closed multiprojective subscheme."""

    def __init__(self, closed_subscheme, ambient_line_bundle) -> None:
        from dzack_research.preamble.categories.schemes.schemes import (
            ClosedSubschemes,
            ProductProjectiveSpaces,
        )

        base = closed_subscheme.scheme_base_ring()
        if closed_subscheme not in ClosedSubschemes(base):
            raise TypeError("a restricted multiprojective bundle requires a closed subscheme")
        ambient = closed_subscheme.inclusion().codomain()
        if ambient not in ProductProjectiveSpaces(base):
            raise TypeError("this restricted bundle requires a product-projective ambient")
        if not isinstance(ambient_line_bundle, ProductProjectiveLineBundle):
            raise TypeError("the ambient bundle must be a represented multiprojective O(d_1,...,d_r)")
        if ambient_line_bundle.projective_product() is not ambient:
            raise ValueError("the ambient line bundle belongs to a different projective product")
        self._scheme = closed_subscheme
        self._ambient_line_bundle = ambient_line_bundle
        self._pullback_morphism = closed_subscheme.inclusion()

    def scheme(self):
        return self._scheme

    def pullback_morphism(self):
        return self._pullback_morphism

    inclusion = pullback_morphism

    def ambient_line_bundle(self):
        return self._ambient_line_bundle

    def multidegree(self):
        return self.ambient_line_bundle().multidegree()

    def tensor_product(self, other):
        if not isinstance(other, ProductProjectiveSubschemeLineBundle):
            raise TypeError("restricted multiprojective tensor product requires two line bundles")
        if other.scheme() is not self.scheme():
            raise ValueError("restricted line-bundle tensor product requires one scheme")
        return type(self)(
            self.scheme(),
            self.ambient_line_bundle().tensor_product(other.ambient_line_bundle()),
        )

    def tensor_power(self, exponent):
        exponent = _own_ring(SageZZ)(exponent)
        if exponent == 1:
            return self
        return type(self)(
            self.scheme(),
            self.ambient_line_bundle().tensor_power(exponent),
        )

    def dual_sheaf(self):
        return type(self)(self.scheme(), self.ambient_line_bundle().dual_sheaf())

    def is_ample(self) -> bool:
        r"""Return a theorem-backed positive ampleness decision from the ambient product."""
        assert self.ambient_line_bundle().is_ample(), (
            "the represented restriction ampleness criterion requires an ample ambient multiprojective bundle"
        )
        return True

    def canonical_isomorphism_to(self, target):
        r"""Return the canonical comparison with an equal-multidegree presentation on this scheme."""
        return _ProductProjectiveSubschemeLineBundleIsomorphism(self, target)

    def _repr_(self):
        degrees = tuple(
            self.multidegree()[label] for label in self.multidegree().index_set()
        )
        return f"O{degrees} restricted to {self.scheme()}"


class _ProductProjectiveSubschemeLineBundleIsomorphism(SageObject):
    r"""The canonical comparison of equal-multidegree restricted line bundles."""

    def __init__(self, source, target) -> None:
        if not isinstance(source, ProductProjectiveSubschemeLineBundle) or not isinstance(
            target, ProductProjectiveSubschemeLineBundle
        ):
            raise TypeError("this comparison requires restricted multiprojective line bundles")
        if source.scheme() is not target.scheme():
            raise ValueError("a line-bundle comparison lies over one scheme")
        source_degrees = source.multidegree()
        target_degrees = target.multidegree()
        if source_degrees.index_set() is not target_degrees.index_set():
            raise ValueError("the two line bundles use different factor index sets")
        if any(
            source_degrees[label] != target_degrees[label]
            for label in source_degrees.index_set()
        ):
            raise ValueError("the selected line-bundle comparison requires equal multidegrees")
        self._source = source
        self._target = target

    def domain(self):
        return self._source

    source = domain

    def codomain(self):
        return self._target

    target = codomain

    def inverse(self):
        return type(self)(self.codomain(), self.domain())

    def __mul__(self, other):
        if not isinstance(other, _ProductProjectiveSubschemeLineBundleIsomorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return type(self)(other.domain(), self.codomain())

    def _repr_(self) -> str:
        return f"Line-bundle isomorphism {self.domain()} ~= {self.codomain()}"


__all__ = [
    "FiniteAtlasInvertibleSheaf",
    "InvertibleSheaf",
    "ProductProjectiveLineBundle",
    "ProductProjectiveSubschemeLineBundle",
    "ProjectiveSubschemeLineBundle",
    "ProjectiveSpaceLineBundle",
]
