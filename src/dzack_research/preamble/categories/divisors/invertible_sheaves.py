r"""Invertible sheaves represented by rank-one affine module descent data."""

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ
from sage.categories.morphism import Morphism

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _combined_linearity_decision,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyGeneratedFreeModules,
)
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.schemes.gluing import (
    FiniteAffineAtlases,
    ModuleGluingData,
    _ModuleGluingSheafEngine,
)
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    InvertibleSheavesWithChosenTrivialization,
    QuasiCoherentSheaves,
)


class _CompatibleSectionMorphism(ModuleMorphism):
    r"""Map compatible sections chartwise through one represented sheaf morphism."""

    def __init__(self, parent, sheaf_morphism, source_datum, target_datum) -> None:
        self._sheaf_morphism = sheaf_morphism
        self._source_datum = source_datum
        self._target_datum = target_datum

        def image(section):
            return target_datum.compatible_section(
                {
                    index: sheaf_morphism.local_map(index)(
                        source_datum.compatible_section_component(section, index)
                    )
                    for index in source_datum.chart_index_set()
                }
            )

        super().__init__(parent, image, elementwise=True)

    def _elementwise_linearity_derivation(self):
        local_maps = tuple(
            self._sheaf_morphism.local_map(index)
            for index in self._source_datum.chart_index_set()
        )
        return _combined_linearity_decision(local_maps)


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


def _invertible_sheaf(gluing_datum):
    r"""Construct a rank-one distinguished-cover descent object through its sheaf owner."""
    return InvertibleSheavesWithChosenTrivialization(gluing_datum.scheme())(
        gluing_datum
    )


def _finite_atlas_invertible_sheaf(
    gluing_datum,
    transition_units,
    *,
    section_space=None,
    associated_divisor=None,
):
    r"""Construct finite-atlas rank-one descent through its sheaf owner."""
    return InvertibleSheavesWithChosenTrivialization(gluing_datum.scheme())(
        gluing_datum,
        transition_units,
        section_space=section_space,
        associated_divisor=associated_divisor,
    )


class _DistinguishedCoverInvertibleSheafEngine(_ModuleGluingSheafEngine):
    r"""A line bundle represented by rank-one free descent on one affine cover."""

    def __init__(self, gluing_datum, module_gluing_datum, **rest) -> None:
        match module_gluing_datum is gluing_datum:
            case True:
                pass
            case False:
                raise ValueError(
                    "the invertible-sheaf realization and its underlying module sheaf require one descent datum"
                )
        assert gluing_datum in ModuleGluingData(gluing_datum.cover()), (
            "an invertible sheaf requires module descent data on its distinguished affine cover"
        )
        self._gluing_datum = gluing_datum
        self._transition_units = {}
        for module in gluing_datum.local_modules():
            ring = module.base_ring()
            if module not in FinitelyGeneratedFreeModules(ring) or int(module.module_rank()) != 1:
                raise TypeError(
                    "an invertible sheaf requires a rank-one finite free module on every chart"
                )
        chart_count = int(gluing_datum.local_modules().cardinality())
        for left in range(chart_count):
            for right in range(left + 1, chart_count):
                self._transition_units[left, right] = self._extract_transition_unit(
                    left,
                    right,
                )
        super().__init__(module_gluing_datum=module_gluing_datum, **rest)

    def gluing_datum(self):
        return self._gluing_datum

    def cover(self):
        return self.gluing_datum().cover()

    def scheme(self):
        return self.gluing_datum().scheme()

    ringed_space = scheme

    def sheaf(self):
        return self

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
        r"""Return the sheaf morphism represented by the supplied chart maps."""
        return QuasiCoherentSheaves(self.scheme()).Mor(self, target)(local_maps)

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
        datum = ModuleGluingData(cover)(local_modules, transitions)
        return _invertible_sheaf(datum)

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
        if other not in InvertibleSheavesWithChosenTrivialization(self.scheme()):
            raise TypeError("line-bundle tensor product requires two represented trivialized invertible sheaves")
        if other.cover() is not self.cover():
            raise ValueError("line-bundle tensor product currently requires one affine cover")
        units = {
            (left, right): self.transition_unit(left, right)
            * other.transition_unit(left, right)
            for left in range(len(self.cover().opens()))
            for right in range(left + 1, len(self.cover().opens()))
        }
        return self._from_transition_units(self.cover(), units)

    @cached_method
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


class _FiniteAtlasInvertibleSheafEngine:
    r"""A line bundle on a finite glued affine atlas via transition functions.

    Unlike the distinguished-cover realization, whose descent datum lives on one affine
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
        **rest,
    ) -> None:
        if gluing_datum not in FiniteAffineAtlases(gluing_datum.scheme()):
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
        super().__init__(**rest)

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
        return _finite_atlas_invertible_sheaf(cover, transition_units)

    @classmethod
    def trivial(cls, atlas):
        units = {
            pair: atlas.overlap(*pair).coordinate_algebra().one()
            for pair in atlas.transition_index_set()
        }
        return _finite_atlas_invertible_sheaf(atlas, units)

    def tensor_product(self, other):
        if other not in InvertibleSheavesWithChosenTrivialization(self.scheme()):
            raise TypeError("finite-atlas tensor product requires two represented trivialized invertible sheaves")
        if other.gluing_datum() is not self.gluing_datum():
            raise ValueError("line-bundle tensor product requires one finite atlas")
        units = {
            pair: self.transition_unit(*pair) * other.transition_unit(*pair)
            for pair in self.gluing_datum().transition_index_set()
        }
        return _finite_atlas_invertible_sheaf(self.gluing_datum(), units)

    @cached_method
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
        return _finite_atlas_invertible_sheaf(self.gluing_datum(), units)

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
        return self.module_sheaf().global_sections()

    def sheaf(self):
        return self

    def _repr_(self):
        return f"Invertible sheaf on finite affine atlas of {self.scheme()}"


class _LineBundleBaseChangeImage:
    r"""The chosen preimage of a line bundle under scalar base change along a ring map.

    For \(f\colon R \to S\) and a bundle \(L\) on \(X\), the base-changed
    bundle \(f^* L\) on \(X_S\) retains \(L\) and \(f\).  Two later operations
    read this preimage: ``base_change_source_bundle`` and
    ``section_base_change_comparison``, the isomorphism
    \(H^0(X, L) \otimes_R S \cong H^0(X_S, f^* L)\) of polynomial section spaces.
    The changed bundle owns it from construction time.
    """

    def __init__(self, source_bundle, ring_map) -> None:
        self._source_bundle = source_bundle
        self._ring_map = ring_map

    def source_bundle(self):
        return self._source_bundle

    def ring_map(self):
        return self._ring_map

    def projection(self, changed_bundle):
        return changed_bundle.scheme().left_projection()

    def compatible_section(self, changed_bundle, section):
        r"""Pull a compatible section back in the standard local trivializations.

        The selected basis of each standard O(d) chart pulls back to the
        selected basis of the corresponding changed chart.  Thus a section
        a_i e_i pulls back to p_i^#(a_i) e_i'.  The transition equations are
        preserved by these ring maps; the target descent constructor checks
        them without retaining an unrelated homogeneous presentation.
        """
        from dzack_research.preamble.categories.sets.indexed_families import (
            finite_indexed_family,
        )

        source = self.source_bundle()
        source_sections = source.compatible_sections()
        if section.parent() is not source_sections:
            raise ValueError("the section belongs to a different line-bundle power")
        source_atlas = source.gluing_datum()
        source_module_datum = source.module_sheaf().gluing_datum()
        target_atlas = changed_bundle.gluing_datum()
        target_module_datum = changed_bundle.module_sheaf().gluing_datum()
        projection = self.projection(changed_bundle)

        def component(index):
            source_index = source_atlas.normalize_chart_index(index)
            target_index = target_atlas.normalize_chart_index(index)
            chart_projection = source_atlas.chart(source_index).corestriction(
                projection * target_atlas.chart_embedding(target_index)
            )
            pullback = chart_projection.coordinate_algebra_morphism()
            source_module = source.local_module(source_index)
            target_module = changed_bundle.local_module(target_index)
            label = next(iter(source_module.module_generating_set()))
            coefficient = source_module.framing_coefficients(
                source_module_datum.compatible_section_component(section, source_index)
            ).get(label, source_module.base_ring().zero())
            return target_module.scalar_multiple(
                pullback(coefficient), _rank_one_generator(target_module)
            )

        return target_module_datum.compatible_section(
            finite_indexed_family(target_atlas.chart_index_set(), component)
        )

    def section_comparison(self, changed_bundle):
        return _section_base_change_comparison(
            self.source_bundle().global_sections(),
            changed_bundle.global_sections(),
            self.ring_map(),
        )


def _section_base_change_comparison(source_sections, target_sections, ring_map):
    r"""Compare scalar extension of two polynomial section spaces monomial by monomial."""
    changed_source = source_sections.base_change(ring_map)
    source_by_exponents = {
        source_sections.monomial_exponents(label): label
        for label in source_sections.module_generating_set()
    }
    target_by_exponents = {
        target_sections.monomial_exponents(label): label
        for label in target_sections.module_generating_set()
    }
    forward = changed_source.module_category().Mor(changed_source, target_sections)(
        lambda label: target_sections.module_generator(
            target_by_exponents[source_sections.monomial_exponents(label)]
        )
    )
    inverse = target_sections.module_category().Mor(target_sections, changed_source)(
        lambda label: changed_source.module_generator(
            source_by_exponents[target_sections.monomial_exponents(label)]
        )
    )
    return changed_source.module_category().Core().Mor(changed_source, target_sections)(
        forward, inverse
    )


def _base_change_image(bundle):
    image = bundle._base_change_image
    assert image is not None, "this line bundle was not constructed as a scalar base change"
    return image


def _base_change_source_bundle(bundle):
    return _base_change_image(bundle).source_bundle()


def _base_change_projection(bundle):
    return _base_change_image(bundle).projection(bundle)


def _section_base_change_comparison_of(bundle):
    return _base_change_image(bundle).section_comparison(bundle)


def _tensor_power_base_change_image(bundle, exponent):
    r"""Return the scalar-change provenance inherited by one tensor power."""
    match bundle._base_change_image:
        case None:
            return None
        case image:
            return _LineBundleBaseChangeImage(
                image.source_bundle().tensor_power(exponent),
                image.ring_map(),
            )


def _chosen_trivialization_object(
    scheme,
    engine,
    *,
    placements=(),
    **construction_data,
):
    r"""Realize one line-bundle engine in the chosen-trivialization owner."""
    category = InvertibleSheavesWithChosenTrivialization(scheme)
    return QuasiCoherentSheaves(scheme).object(
        categories=(category, *placements),
        construction_data=construction_data,
        _engine=engine,
    )


def _invertible_sheaf_object(
    scheme,
    engine,
    *,
    placements=(),
    **construction_data,
):
    r"""Realize one line-bundle engine directly in ``QCoh(scheme).Invertible()``."""
    category = QuasiCoherentSheaves(scheme).Invertible()
    return QuasiCoherentSheaves(scheme).object(
        categories=(category, *placements),
        construction_data=construction_data,
        _engine=engine,
    )


class _ProjectiveSpaceLineBundleEngine(_FiniteAtlasInvertibleSheafEngine):
    r"""The standard ``O(d)`` on one represented projective space.

    This is a specialization of finite-atlas invertible-sheaf descent.  Its
    local basis on ``U_i`` has transition ``(x_j/x_i)^d`` to ``U_j``; tensor
    product therefore adds degrees and duality negates them.
    """

    def __init__(
        self,
        projective_space,
        degree,
        *,
        base_change_image=None,
        **rest,
    ) -> None:
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
        self._base_change_image = base_change_image
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
        super().__init__(atlas, units, section_space=section_space, **rest)

    def projective_space(self):
        return self._projective_space

    def degree(self):
        return self._degree

    def tensor_product(self, other):
        match other:
            case _ProjectiveSpaceLineBundleEngine() if other.projective_space() is self.projective_space():
                return _projective_o(
                    self.projective_space(),
                    self.degree() + other.degree(),
                )
            case _ProjectiveSpaceLineBundleEngine():
                raise ValueError("projective line-bundle tensor product requires one projective space")
            case _:
                return super().tensor_product(other)

    @cached_method
    def tensor_power(self, exponent):
        exponent = _own_ring(SageZZ)(exponent)
        match exponent == 1:
            case True:
                return self
            case False:
                return _projective_o(
                    self.projective_space(),
                    exponent * self.degree(),
                    base_change_image=_tensor_power_base_change_image(self, exponent),
                )

    def dual_sheaf(self):
        return _projective_o(self.projective_space(), -self.degree())

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
        r"""Return the pullback of O(d) along a represented projective closed immersion."""
        return closed_subscheme.inclusion().module_pullback(self)

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
        label = source.projection_label(morphism)
        labels = tuple(source.factors().index_set())
        label = source.factors().index_set()(label)
        return source.O(
            tuple(self.degree() if factor_label == label else 0 for factor_label in labels)
        )

    def linearize(self, scheme_action_functor, character):
        from dzack_research.preamble.categories.divisors.linearizations import (
            _line_bundle_linearization,
        )

        return _line_bundle_linearization(self, scheme_action_functor, character)

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

    def section_multiplication(self, other):
        from dzack_research.preamble.categories.modules.pure.modules import BilinearMap

        match other:
            case _ProjectiveSpaceLineBundleEngine() if other.projective_space() is self.projective_space():
                pass
            case _ProjectiveSpaceLineBundleEngine():
                raise ValueError("section multiplication requires one projective space")
            case _:
                raise TypeError("section multiplication requires two projective-space line bundles")
        assert self.degree() >= 0 and other.degree() >= 0, (
            "homogeneous-polynomial section multiplication is represented here in nonnegative degrees"
        )
        target_bundle = self.tensor_product(other)
        left = self.global_sections()
        right = other.global_sections()
        target = target_bundle.global_sections()
        target_by_exponents = {
            target.monomial_exponents(monomial): monomial
            for monomial in target.module_generating_set()
        }

        def product(left_monomial, right_monomial):
            exponents = tuple(
                left_power + right_power
                for left_power, right_power in zip(
                    left.monomial_exponents(left_monomial),
                    right.monomial_exponents(right_monomial),
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
        return _projective_o(
            self.projective_space().base_change(ring_map),
            self.degree(),
            base_change_image=_LineBundleBaseChangeImage(self, ring_map),
        )

    def base_change_source_bundle(self):
        return _base_change_source_bundle(self)

    def base_change_projection(self):
        return _base_change_projection(self)

    def section_base_change_comparison(self):
        return _section_base_change_comparison_of(self)

    def pullback_compatible_section(self, section):
        r"""Pull a section of the source bundle back along this base change."""
        return _base_change_image(self).compatible_section(self, section)

    def _repr_(self):
        return f"O({self.degree()}) on {self.projective_space()}"



class _ProjectiveSubschemeLineBundleEngine:
    r"""The pullback ``i^* O_P(d)`` along a projective closed immersion.

    The defining datum is the actual closed immersion together with the
    ambient projective line bundle.  No second projective-coordinate sheaf is
    built on the subscheme.  This is the line-bundle object needed by
    adjunction and strict-transform comparisons; computations of sections may
    use the existing image-valued restriction map separately.
    """

    def __init__(
        self,
        closed_subscheme,
        ambient_line_bundle,
        *,
        pullback_morphism=None,
        **rest,
    ) -> None:
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
        match ambient_line_bundle:
            case _ProjectiveSpaceLineBundleEngine() if ambient_line_bundle.projective_space() is ambient:
                pass
            case _ProjectiveSpaceLineBundleEngine():
                raise ValueError("the ambient line bundle belongs to a different projective space")
            case _:
                raise TypeError("the ambient bundle must be a represented projective O(d)")
        match pullback_morphism:
            case None:
                selected_pullback = closed_subscheme.inclusion()
            case _:
                selected_pullback = pullback_morphism
        match (
            selected_pullback.domain() is closed_subscheme,
            selected_pullback.codomain() is ambient,
        ):
            case (True, True):
                pass
            case _:
                raise ValueError("the selected pullback morphism is not this closed immersion")
        self._scheme = closed_subscheme
        self._ambient_line_bundle = ambient_line_bundle
        self._pullback_morphism = selected_pullback
        super().__init__(**rest)

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
        match other:
            case _ProjectiveSubschemeLineBundleEngine() if other.scheme() is self.scheme():
                pass
            case _ProjectiveSubschemeLineBundleEngine():
                raise ValueError("restricted line-bundle tensor product requires one scheme")
            case _:
                raise TypeError("restricted projective tensor product requires two O_X(d) bundles")
        return self.pullback_morphism().module_pullback(
            self.ambient_line_bundle().tensor_product(other.ambient_line_bundle())
        )

    def tensor_power(self, exponent):
        exponent = _own_ring(SageZZ)(exponent)
        if exponent == 1:
            return self
        return self.pullback_morphism().module_pullback(
            self.ambient_line_bundle().tensor_power(exponent)
        )

    def dual_sheaf(self):
        return self.pullback_morphism().module_pullback(
            self.ambient_line_bundle().dual_sheaf()
        )

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
        match target:
            case _ProjectiveSubschemeLineBundleEngine() if target.scheme() is self.scheme():
                pass
            case _ProjectiveSubschemeLineBundleEngine():
                raise ValueError("a line-bundle isomorphism lies over one scheme")
            case _:
                raise TypeError("this line-bundle isomorphism compares two represented O_X(d) bundles")
        if self.degree() != target.degree():
            raise ValueError("the selected projective line-bundle comparison requires equal degrees")
        ambient = _chosen_trivialization_isomorphism(
            self.ambient_line_bundle(),
            target.ambient_line_bundle(),
        )
        sheaves = QuasiCoherentSheaves(self.scheme())
        forward = sheaves.Mor(self, target)(ambient.forward())
        inverse = sheaves.Mor(target, self)(ambient.inverse())
        return sheaves.Core().Mor(self, target)(forward, inverse)

    def _repr_(self):
        return f"O({self.degree()}) restricted to {self.scheme()}"


def _projective_o(projective_space, degree, *, base_change_image=None):
    r"""Return the standard line bundle ``O(d)`` on ``P^n``."""
    return _chosen_trivialization_object(
        projective_space,
        _ProjectiveSpaceLineBundleEngine,
        projective_space=projective_space,
        degree=degree,
        base_change_image=base_change_image,
    )


def _projective_subscheme_line_bundle(
    closed_subscheme,
    ambient_line_bundle,
    *,
    pullback_morphism=None,
):
    r"""Return the invertible pullback of ``ambient_line_bundle`` to ``closed_subscheme``."""
    return _invertible_sheaf_object(
        closed_subscheme,
        _ProjectiveSubschemeLineBundleEngine,
        closed_subscheme=closed_subscheme,
        ambient_line_bundle=ambient_line_bundle,
        pullback_morphism=pullback_morphism,
    )


class _ProductProjectiveLineBundleEngine(_FiniteAtlasInvertibleSheafEngine):
    r"""The standard ``O(d_1,...,d_r)`` on a product of projective spaces."""

    def __init__(
        self,
        projective_product,
        degrees,
        *,
        base_change_image=None,
        **rest,
    ) -> None:
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
        match degrees:
            case IndexedFamily():
                if degrees.index_set() is not factor_indices:
                    raise ValueError("a line-bundle multidegree uses the exact factor index set")
                degree_values = tuple(
                    _own_ring(SageZZ)(degrees[label]) for label in factor_labels
                )
            case _:
                degree_values = tuple(_own_ring(SageZZ)(degree) for degree in degrees)
                if len(degree_values) != len(factor_labels):
                    raise ValueError("a line-bundle multidegree has one degree per projective factor")
        self._projective_product = projective_product
        self._base_change_image = base_change_image
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
        super().__init__(atlas, units, section_space=section_space, **rest)

    def projective_product(self):
        return self._projective_product

    def multidegree(self):
        return self._multidegree

    def tensor_product(self, other):
        match other:
            case _ProductProjectiveLineBundleEngine() if other.projective_product() is self.projective_product():
                labels = tuple(self.multidegree().index_set())
                return _product_projective_o(
                    self.projective_product(),
                    tuple(
                        self.multidegree()[label] + other.multidegree()[label]
                        for label in labels
                    ),
                )
            case _ProductProjectiveLineBundleEngine():
                raise ValueError("multiprojective line-bundle tensor product requires one scheme")
            case _:
                return super().tensor_product(other)

    @cached_method
    def tensor_power(self, exponent):
        exponent = _own_ring(SageZZ)(exponent)
        match exponent == 1:
            case True:
                return self
            case False:
                return _product_projective_o(
                    self.projective_product(),
                    tuple(
                        exponent * self.multidegree()[label]
                        for label in self.multidegree().index_set()
                    ),
                    base_change_image=_tensor_power_base_change_image(self, exponent),
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
        return _product_projective_subscheme_line_bundle(closed_subscheme, self)

    def linearize(self, scheme_action_functor, character):
        from dzack_research.preamble.categories.divisors.linearizations import (
            _line_bundle_linearization,
        )

        return _line_bundle_linearization(self, scheme_action_functor, character)

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

        match other:
            case _ProductProjectiveLineBundleEngine() if other.projective_product() is self.projective_product():
                pass
            case _ProductProjectiveLineBundleEngine():
                raise ValueError("multihomogeneous section multiplication requires one scheme")
            case _:
                raise TypeError("multihomogeneous section multiplication requires two multiprojective line bundles")
        target_bundle = self.tensor_product(other)
        left = self.global_sections()
        right = other.global_sections()
        target = target_bundle.global_sections()
        target_by_exponents = {
            target.monomial_exponents(monomial): monomial
            for monomial in target.module_generating_set()
        }

        def product(left_monomial, right_monomial):
            exponents = tuple(
                tuple(a + b for a, b in zip(left_block, right_block, strict=True))
                for left_block, right_block in zip(
                    left.monomial_exponents(left_monomial),
                    right.monomial_exponents(right_monomial),
                    strict=True,
                )
            )
            return target.module_generator(target_by_exponents[exponents])

        return BilinearMap(left, right, target, product)

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
        atlas = self.gluing_datum()
        factors = self.projective_product().factors()
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
                blocks = sections.monomial_exponents(monomial)
                for label, block in zip(factor_labels, blocks, strict=True):
                    selected = choice[positions[label]]
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
        return module_sheaf.gluing_datum().compatible_section(components)

    @cached_method
    def section_ring(self):
        from dzack_research.preamble.categories.divisors.section_rings import SectionRings

        return SectionRings(self.scheme().scheme_base_ring())(self)

    def base_change(self, ring_map):
        return _product_projective_o(
            self.projective_product().base_change(ring_map),
            tuple(
                self.multidegree()[label]
                for label in self.multidegree().index_set()
            ),
            base_change_image=_LineBundleBaseChangeImage(self, ring_map),
        )

    def base_change_source_bundle(self):
        return _base_change_source_bundle(self)

    def base_change_projection(self):
        return _base_change_projection(self)

    def section_base_change_comparison(self):
        return _section_base_change_comparison_of(self)

    def pullback_compatible_section(self, section):
        r"""Pull a section of the source bundle back along this base change."""
        return _base_change_image(self).compatible_section(self, section)

    def _repr_(self):
        degrees = tuple(self.multidegree()[label] for label in self.multidegree().index_set())
        return f"O{degrees} on {self.projective_product()}"



class _ProductProjectiveSubschemeLineBundleEngine:
    r"""The pullback of ``O(d_1,...,d_r)`` to a closed multiprojective subscheme."""

    def __init__(self, closed_subscheme, ambient_line_bundle, **rest) -> None:
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
        match ambient_line_bundle:
            case _ProductProjectiveLineBundleEngine() if ambient_line_bundle.projective_product() is ambient:
                pass
            case _ProductProjectiveLineBundleEngine():
                raise ValueError("the ambient line bundle belongs to a different projective product")
            case _:
                raise TypeError("the ambient bundle must be a represented multiprojective O(d_1,...,d_r)")
        self._scheme = closed_subscheme
        self._ambient_line_bundle = ambient_line_bundle
        self._pullback_morphism = closed_subscheme.inclusion()
        super().__init__(**rest)

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
        match other:
            case _ProductProjectiveSubschemeLineBundleEngine() if other.scheme() is self.scheme():
                pass
            case _ProductProjectiveSubschemeLineBundleEngine():
                raise ValueError("restricted line-bundle tensor product requires one scheme")
            case _:
                raise TypeError("restricted multiprojective tensor product requires two line bundles")
        return _product_projective_subscheme_line_bundle(
            self.scheme(),
            self.ambient_line_bundle().tensor_product(other.ambient_line_bundle()),
        )

    def tensor_power(self, exponent):
        exponent = _own_ring(SageZZ)(exponent)
        if exponent == 1:
            return self
        return _product_projective_subscheme_line_bundle(
            self.scheme(),
            self.ambient_line_bundle().tensor_power(exponent),
        )

    def dual_sheaf(self):
        return _product_projective_subscheme_line_bundle(
            self.scheme(),
            self.ambient_line_bundle().dual_sheaf(),
        )

    def is_ample(self) -> bool:
        r"""Return a theorem-backed positive ampleness decision from the ambient product."""
        assert self.ambient_line_bundle().is_ample(), (
            "the represented restriction ampleness criterion requires an ample ambient multiprojective bundle"
        )
        return True

    def canonical_isomorphism_to(self, target):
        r"""Return the canonical comparison with an equal-multidegree presentation on this scheme."""
        match target:
            case _ProductProjectiveSubschemeLineBundleEngine() if target.scheme() is self.scheme():
                pass
            case _ProductProjectiveSubschemeLineBundleEngine():
                raise ValueError("a line-bundle comparison lies over one scheme")
            case _:
                raise TypeError("this comparison requires restricted multiprojective line bundles")
        source_degrees = self.multidegree()
        target_degrees = target.multidegree()
        if source_degrees.index_set() is not target_degrees.index_set():
            raise ValueError("the two line bundles use different factor index sets")
        if any(
            source_degrees[label] != target_degrees[label]
            for label in source_degrees.index_set()
        ):
            raise ValueError("the selected line-bundle comparison requires equal multidegrees")
        ambient = _chosen_trivialization_isomorphism(
            self.ambient_line_bundle(),
            target.ambient_line_bundle(),
        )
        sheaves = QuasiCoherentSheaves(self.scheme())
        forward = sheaves.Mor(self, target)(ambient.forward())
        inverse = sheaves.Mor(target, self)(ambient.inverse())
        return sheaves.Core().Mor(self, target)(forward, inverse)

    def _repr_(self):
        degrees = tuple(
            self.multidegree()[label] for label in self.multidegree().index_set()
        )
        return f"O{degrees} restricted to {self.scheme()}"


def _line_bundle_identity_local_maps(source, target):
    r"""Return the chartwise basis identifications of two line bundles on one trivialization."""
    if source.gluing_datum() is not target.gluing_datum():
        raise ValueError("the represented line-bundle Hom requires one chosen trivializing cover")
    return {
        index: source.local_module(index).module_category().Mor(
            source.local_module(index),
            target.local_module(index),
        )(
            {
                next(iter(source.local_module(index).module_generating_set())):
                    _rank_one_generator(target.local_module(index))
            }
        )
        for index in source.gluing_datum().chart_index_set()
    }


class _ChosenTrivializationQuasiCoherentMorphism(Morphism):
    r"""A line-bundle sheaf morphism represented by compatible maps in one trivialization."""

    def __init__(self, parent, local_maps) -> None:
        Morphism.__init__(self, parent)
        source = self.domain()
        target = self.codomain()
        if source.gluing_datum() is not target.gluing_datum():
            raise ValueError("line-bundle sheaf morphisms require one represented trivializing cover")
        match (source, target):
            case (_DistinguishedCoverInvertibleSheafEngine(), _DistinguishedCoverInvertibleSheafEngine()):
                self._descent_morphism = source.gluing_datum().Mor(
                    target.gluing_datum()
                )(local_maps)
            case (_FiniteAtlasInvertibleSheafEngine(), _FiniteAtlasInvertibleSheafEngine()):
                source_sheaf = source.module_sheaf()
                target_sheaf = target.module_sheaf()
                self._descent_morphism = QuasiCoherentSheaves(source.scheme()).Mor(
                    source_sheaf,
                    target_sheaf,
                )(local_maps)
            case _:
                raise TypeError("the selected trivialization has no represented descent Hom")

    def descent_morphism(self):
        return self._descent_morphism

    def local_map(self, index):
        return self.descent_morphism().local_map(index)

    @cached_method
    def global_sections_map(self):
        r"""Return the induced map on the compatible-section modules of the trivializations."""
        match self.domain():
            case _DistinguishedCoverInvertibleSheafEngine():
                source_datum = self.domain().gluing_datum()
                target_datum = self.codomain().gluing_datum()
            case _FiniteAtlasInvertibleSheafEngine():
                source_datum = self.domain().module_sheaf().gluing_datum()
                target_datum = self.codomain().module_sheaf().gluing_datum()
            case _:
                raise TypeError("the selected trivialization has no represented section descent")
        source_sections = source_datum.compatible_sections()
        target_sections = target_datum.compatible_sections()

        return _CompatibleSectionMorphism(
            source_sections.module_category().Mor(
                source_sections,
                target_sections,
            ),
            self,
            source_datum,
            target_datum,
        )

    def __eq__(self, other) -> bool:
        match other:
            case _ChosenTrivializationQuasiCoherentMorphism() if other.parent() is self.parent():
                return all(
                    self.local_map(index) == other.local_map(index)
                    for index in self.domain().gluing_datum().chart_index_set()
                )
            case _:
                return False

    def __ne__(self, other) -> bool:
        return not self == other

    def __mul__(self, other):
        match other:
            case _ChosenTrivializationQuasiCoherentMorphism():
                pass
            case _:
                return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().homset_category().Mor(
            other.domain(),
            self.codomain(),
        )(
            {
                index: self.local_map(index) * other.local_map(index)
                for index in other.domain().gluing_datum().chart_index_set()
            }
        )


class _ChosenTrivializationQuasiCoherentHomset(CategoricalHomset):
    r"""The QCoh Hom of line bundles carrying one represented trivializing cover."""

    Element = _ChosenTrivializationQuasiCoherentMorphism

    def _element_constructor_(self, local_maps):
        match local_maps:
            case _ChosenTrivializationQuasiCoherentMorphism() if local_maps.parent() is self:
                return local_maps
            case _ChosenTrivializationQuasiCoherentMorphism():
                if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                    raise ValueError("the line-bundle morphism has the wrong endpoints")
                local_maps = {
                    index: local_maps.local_map(index)
                    for index in self.domain().gluing_datum().chart_index_set()
                }
            case _:
                pass
        return self.element_class(self, local_maps)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom")
        return self(_line_bundle_identity_local_maps(self.domain(), self.domain()))


def _chosen_trivialization_isomorphism(source, target):
    r"""Return the basis-preserving isomorphism of equal represented line-bundle trivializations."""
    sheaves = QuasiCoherentSheaves(source.scheme())
    forward = sheaves.Mor(source, target)(_line_bundle_identity_local_maps(source, target))
    inverse = sheaves.Mor(target, source)(_line_bundle_identity_local_maps(target, source))
    return sheaves.Core().Mor(source, target)(forward, inverse)


class _PullbackLineBundleQuasiCoherentMorphism(Morphism):
    r"""The pullback of a represented ambient line-bundle morphism along one closed immersion."""

    def __init__(self, parent, ambient_morphism) -> None:
        Morphism.__init__(self, parent)
        source = self.domain()
        target = self.codomain()
        if source.pullback_morphism() is not target.pullback_morphism():
            raise ValueError("pullback line-bundle morphisms require one selected scheme morphism")
        ambient_source = source.ambient_line_bundle()
        ambient_target = target.ambient_line_bundle()
        ambient_sheaves = QuasiCoherentSheaves(ambient_source.scheme())
        self._ambient_morphism = ambient_sheaves.Mor(
            ambient_source,
            ambient_target,
        )(ambient_morphism)

    def ambient_morphism(self):
        return self._ambient_morphism

    def __eq__(self, other) -> bool:
        match other:
            case _PullbackLineBundleQuasiCoherentMorphism() if other.parent() is self.parent():
                return other.ambient_morphism() == self.ambient_morphism()
            case _:
                return False

    def __ne__(self, other) -> bool:
        return not self == other

    def __mul__(self, other):
        match other:
            case _PullbackLineBundleQuasiCoherentMorphism():
                pass
            case _:
                return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().homset_category().Mor(
            other.domain(),
            self.codomain(),
        )(self.ambient_morphism() * other.ambient_morphism())


class _PullbackLineBundleQuasiCoherentHomset(CategoricalHomset):
    r"""The QCoh Hom represented by pullback from ambient line-bundle morphisms."""

    Element = _PullbackLineBundleQuasiCoherentMorphism

    def _element_constructor_(self, ambient_morphism):
        match ambient_morphism:
            case _PullbackLineBundleQuasiCoherentMorphism() if ambient_morphism.parent() is self:
                return ambient_morphism
            case _PullbackLineBundleQuasiCoherentMorphism():
                if ambient_morphism.domain() is not self.domain() or ambient_morphism.codomain() is not self.codomain():
                    raise ValueError("the pullback line-bundle morphism has the wrong endpoints")
                ambient_morphism = ambient_morphism.ambient_morphism()
            case _:
                pass
        return self.element_class(self, ambient_morphism)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom")
        ambient = self.domain().ambient_line_bundle()
        return self(QuasiCoherentSheaves(ambient.scheme()).Mor(ambient, ambient).identity())


def _product_projective_o(projective_product, degrees, *, base_change_image=None):
    r"""Return ``O(degrees)`` on one represented product of projective spaces."""
    return _chosen_trivialization_object(
        projective_product,
        _ProductProjectiveLineBundleEngine,
        projective_product=projective_product,
        degrees=degrees,
        base_change_image=base_change_image,
    )


def _product_projective_subscheme_line_bundle(closed_subscheme, ambient_line_bundle):
    r"""Return the invertible pullback of a multiprojective line bundle."""
    return _invertible_sheaf_object(
        closed_subscheme,
        _ProductProjectiveSubschemeLineBundleEngine,
        closed_subscheme=closed_subscheme,
        ambient_line_bundle=ambient_line_bundle,
    )


__all__ = [
    # Realization engines are intentionally private; public objects are placed
    # through the quasi-coherent/invertible sheaf owners.
]
