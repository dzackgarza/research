r"""Finite glued quotients assembled from represented affine invariant quotients."""

from __future__ import annotations

from collections.abc import Hashable
from itertools import combinations
from types import NotImplementedType

from sage.categories.morphism import Morphism, SetMorphism
from sage.schemes.generic.scheme import Scheme
from sage.structure.element import Element
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoricalIsomorphism,
)
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.group.groups import (
    FiniteGroups,
    GroupsWithChosenFiniteGeneratingSet,
)

from dzack_research.preamble.categories.schemes.schemes import (
    AffineGSchemes,
    AffineSchemes,
    OpenImmersions,
    SchemeMorphism,
    Schemes,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


class _ChartMapIntoGluedScheme(SchemeMorphism):
    r"""A map whose image is represented inside one named chart of a glued target."""

    def __init__(
        self,
        parent: CategoricalHomset,
        target_chart: Scheme,
        local_affine_map: SchemeMorphism,
    ) -> None:
        Morphism.__init__(self, parent)
        self._preamble_domain_override = None
        self._preamble_codomain_override = None
        self._target_chart = target_chart
        self._local_affine_map = local_affine_map
        if local_affine_map.domain() is not self.domain():
            raise ValueError("the chart map has the wrong source")
        if local_affine_map.codomain() is not target_chart:
            raise ValueError("the chart map has the wrong target chart")

    def target_chart(self) -> Scheme:
        return self._target_chart

    def local_affine_map(self) -> SchemeMorphism:
        return self._local_affine_map

    def __mul__(self, other: SchemeMorphism) -> SchemeMorphism | NotImplementedType:
        if other.codomain() is not self.domain():
            return NotImplemented
        if other is self.domain().categorical_identity_morphism():
            return self
        composite: SchemeMorphism = self.local_affine_map() * other
        parent: CategoricalHomset = other.domain().Mor(self.codomain())
        return _ChartMapIntoGluedScheme(parent, self.target_chart(), composite)


class _ChartwiseGluedSchemeMorphism(SchemeMorphism):
    r"""A map out of a finite gluing, determined by one map on each named chart."""

    def __init__(
        self,
        parent: CategoricalHomset,
        source_charts: IndexedFamily,
        local_maps: IndexedFamily,
    ) -> None:
        Morphism.__init__(self, parent)
        self._preamble_domain_override = None
        self._preamble_codomain_override = None
        if source_charts.index_set() != local_maps.index_set():
            raise ValueError("a chartwise scheme morphism requires one local map on each source chart")
        for index in source_charts.index_set():
            local_map: SchemeMorphism = local_maps[index]
            if local_map.domain() is not source_charts[index]:
                raise ValueError("a chartwise scheme morphism has a local map with the wrong source")
            if local_map.codomain() is not self.codomain():
                raise ValueError("a chartwise scheme morphism has a local map with the wrong target")
        self._source_charts = source_charts
        self._local_maps = local_maps

    def source_charts(self) -> IndexedFamily:
        return self._source_charts

    def local_maps(self) -> IndexedFamily:
        return self._local_maps

    def local_map(self, index: Hashable) -> SchemeMorphism:
        local_map: SchemeMorphism = self.local_maps()[index]
        return local_map

    def _postcompose_with(self, after: SchemeMorphism) -> SchemeMorphism | NotImplementedType:
        if after.domain() is not self.codomain():
            return NotImplemented
        local_maps = self.local_maps().map(
            lambda local_map: after * local_map,
            name="Postcomposed local maps of a glued-scheme morphism",
        )
        parent: CategoricalHomset = self.domain().Mor(after.codomain())
        return _ChartwiseGluedSchemeMorphism(parent, self.source_charts(), local_maps)


class _GluedGroupActionMorphism(_ChartwiseGluedSchemeMorphism):
    r"""One chartwise automorphism in the glued group action."""

    def __init__(
        self,
        parent: CategoricalHomset,
        source_charts: IndexedFamily,
        local_maps: IndexedFamily,
        quotient_data: FiniteGluedInvariantQuotient,
        group_element: Element,
    ) -> None:
        self._quotient_data = quotient_data
        self._group_element = group_element
        super().__init__(parent, source_charts, local_maps)

    def quotient_data(self) -> FiniteGluedInvariantQuotient:
        return self._quotient_data

    def group_element(self) -> Element:
        return self._group_element

    def __mul__(self, other: SchemeMorphism) -> SchemeMorphism | NotImplementedType:
        if other.codomain() is not self.domain():
            return NotImplemented
        if other is self.domain().categorical_identity_morphism():
            return self
        for group_element, action_morphism in self.quotient_data()._action_morphisms.items():
            if other is action_morphism:
                product: Element = self.group_element() * group_element
                return self.quotient_data().action_of(product)
        return NotImplemented


class _GluedInvariantQuotientMorphism(_ChartwiseGluedSchemeMorphism):
    r"""The quotient map assembled from the affine quotient maps."""

    def __init__(
        self,
        parent: CategoricalHomset,
        source_charts: IndexedFamily,
        local_maps: IndexedFamily,
        quotient_data: FiniteGluedInvariantQuotient,
    ) -> None:
        self._quotient_data = quotient_data
        super().__init__(parent, source_charts, local_maps)

    def quotient_data(self) -> FiniteGluedInvariantQuotient:
        return self._quotient_data

    def __mul__(self, other: SchemeMorphism) -> SchemeMorphism | NotImplementedType:
        if other.codomain() is not self.domain():
            return NotImplemented
        if other is self.domain().categorical_identity_morphism():
            return self
        for action_morphism in self.quotient_data()._action_morphisms.values():
            if other is action_morphism:
                return self
        return NotImplemented


class _InvariantAffineFactorMorphism(_ChartwiseGluedSchemeMorphism):
    r"""The affine-target factor through one glued invariant quotient."""

    def __init__(
        self,
        parent: CategoricalHomset,
        source_charts: IndexedFamily,
        local_maps: IndexedFamily,
        quotient_data: FiniteGluedInvariantQuotient,
        original_morphism: SchemeMorphism,
    ) -> None:
        self._quotient_data = quotient_data
        self._original_morphism = original_morphism
        super().__init__(parent, source_charts, local_maps)

    def quotient_data(self) -> FiniteGluedInvariantQuotient:
        return self._quotient_data

    def original_morphism(self) -> SchemeMorphism:
        return self._original_morphism

    def __mul__(self, other: SchemeMorphism) -> SchemeMorphism | NotImplementedType:
        if other is self.quotient_data().quotient_morphism():
            return self.original_morphism()
        if other is self.domain().categorical_identity_morphism():
            return self
        return NotImplemented


class FiniteGluedInvariantQuotient(SageObject):
    r"""The quotient of a finite equivariant affine gluing by a finite group.

    The input is a finite indexed family of affine ``G``-schemes, one indexed
    family of source-overlap isomorphisms, and one indexed family of their
    descended quotient-overlap isomorphisms.  The construction verifies that
    every source transition is ``G``-equivariant, checks the quotient descent
    squares, glues the source and quotient atlases, and retains the induced
    global action and quotient morphism.

    For a represented affine target, an invariant map out of the glued source
    factors uniquely through the quotient: existence is obtained chartwise from
    the affine invariant quotient, and uniqueness follows chartwise from that
    same universal property and globally from finite-gluing maps-out.
    """

    def __init__(
        self,
        base_ring: Parent,
        acting_group: Parent,
        acted_charts: IndexedFamily,
        source_transitions: IndexedFamily,
        quotient_transitions: IndexedFamily,
        source_scheme: Scheme | None = None,
    ) -> None:
        assert acting_group in FiniteGroups(), (
            "glued invariant quotients are represented here for a finite acting group"
        )
        assert acting_group in GroupsWithChosenFiniteGeneratingSet(), (
            "glued invariant quotients require a chosen finite group generating set"
        )
        if acted_charts.cardinality().is_finite() is not True:
            raise TypeError("a glued invariant quotient requires finitely many affine charts")
        if int(acted_charts.cardinality().finite_value()) == 0:
            raise ValueError("a glued invariant quotient requires at least one affine chart")

        self._base_ring = base_ring
        self._group = acting_group
        self._acted_charts = acted_charts
        self._chart_index_set = finite_ordered_set(acted_charts.index_set())
        acted_schemes = GObjects(acting_group, Schemes(base_ring))
        for index in self.chart_index_set():
            acted_chart = self.acted_charts()[index]
            if acted_chart not in acted_schemes or acted_chart not in AffineSchemes(base_ring):
                raise TypeError("every quotient chart must be an affine G-scheme over the stated base")
            source_chart = acted_chart.unacted_scheme()
            if source_chart not in AffineSchemes(base_ring):
                raise TypeError("every acted chart must retain its affine source scheme")

        self._source_charts = finite_indexed_family(
            self.chart_index_set(),
            lambda index: self.acted_charts()[index].unacted_scheme(),
            name="Affine source charts of a finite glued invariant quotient",
        )
        pair_index_set = finite_ordered_set(
            tuple(combinations(tuple(self.chart_index_set()), 2))
        )
        if source_transitions.index_set() != pair_index_set:
            raise ValueError("source transitions must be indexed by the unordered chart pairs")
        if quotient_transitions.index_set() != pair_index_set:
            raise ValueError("quotient transitions must be indexed by the unordered chart pairs")
        self._pair_index_set = pair_index_set
        self._source_transitions = source_transitions
        self._quotient_transitions = quotient_transitions
        self._reverse_source_transitions: dict[
            tuple[Hashable, Hashable], CategoricalIsomorphism
        ] = {}
        self._reverse_quotient_transitions: dict[
            tuple[Hashable, Hashable], CategoricalIsomorphism
        ] = {}
        self._source_chart_actions: dict[
            tuple[Hashable, Element], SchemeMorphism
        ] = {}
        self._source_overlap_actions: dict[
            tuple[Hashable, Hashable, Element], SchemeMorphism
        ] = {}
        self._quotient_overlap_factors: dict[
            tuple[Hashable, Hashable], SchemeMorphism
        ] = {}
        self._action_morphisms: dict[Element, SchemeMorphism] = {}
        self._action: SetMorphism | None = None
        self._quotient_morphism: SchemeMorphism | None = None

        self._verify_source_transition_equivariance()
        if source_scheme is None:
            self._source_scheme = Schemes(base_ring).glue_affine_atlas(
                self.source_charts(),
                self.source_transitions(),
            )
        else:
            datum = source_scheme.gluing_datum()
            if tuple(datum.chart_indices()) != tuple(self.chart_index_set()):
                raise ValueError("the supplied glued source has a different chart index set")
            for index in self.chart_index_set():
                if datum.chart(index) is not self.source_chart(index):
                    raise ValueError("the supplied glued source does not use the acted affine charts")
            for left, right in self.pair_index_set():
                if (
                    datum.transition_between(left, right).forward()
                    != self.source_transition_between(left, right).forward()
                ):
                    raise ValueError("the supplied glued source has different overlap transitions")
            self._source_scheme = source_scheme
        self._local_quotients = finite_indexed_family(
            self.chart_index_set(),
            lambda index: self.acted_charts()[index].affine_quotient(),
            name="Affine quotient charts of a finite glued invariant quotient",
        )
        self._quotient_scheme = Schemes(base_ring).glue_affine_atlas(
            self.local_quotients(),
            self.quotient_transitions(),
        )
        self._verify_quotient_descent_squares()
        self.action()
        self.quotient_morphism()

    def base_ring(self) -> Parent:
        return self._base_ring

    def acting_group(self) -> Parent:
        return self._group

    def chart_index_set(self) -> Parent:
        return self._chart_index_set

    chart_indices = chart_index_set

    def pair_index_set(self) -> Parent:
        return self._pair_index_set

    def normalize_chart_index(self, index: Hashable) -> Hashable:
        normalized: Hashable = self.chart_index_set()(index)
        return normalized

    def acted_charts(self) -> IndexedFamily:
        return self._acted_charts

    def acted_chart(self, index: Hashable) -> Scheme:
        acted_chart: Scheme = self.acted_charts()[self.normalize_chart_index(index)]
        return acted_chart

    def source_charts(self) -> IndexedFamily:
        return self._source_charts

    def source_chart(self, index: Hashable) -> Scheme:
        source_chart: Scheme = self.source_charts()[self.normalize_chart_index(index)]
        return source_chart

    def source_transitions(self) -> IndexedFamily:
        return self._source_transitions

    def quotient_transitions(self) -> IndexedFamily:
        return self._quotient_transitions

    def local_quotients(self) -> IndexedFamily:
        return self._local_quotients

    def local_quotient(self, index: Hashable) -> Scheme:
        quotient_chart: Scheme = self.local_quotients()[self.normalize_chart_index(index)]
        return quotient_chart

    def source_scheme(self) -> Scheme:
        source: Scheme = self._source_scheme
        return source

    source = source_scheme

    def quotient_scheme(self) -> Scheme:
        quotient: Scheme = self._quotient_scheme
        return quotient

    quotient = quotient_scheme

    def _ordered_pair(
        self,
        left_index: Hashable,
        right_index: Hashable,
    ) -> tuple[Hashable, Hashable]:
        left_index = self.normalize_chart_index(left_index)
        right_index = self.normalize_chart_index(right_index)
        if left_index == right_index:
            raise ValueError("an overlap transition is between two distinct charts")
        chart_ranking = self.chart_index_set().ranking_map()
        if chart_ranking(left_index) < chart_ranking(right_index):
            return left_index, right_index
        return right_index, left_index

    def source_transition_between(
        self,
        source_index: Hashable,
        target_index: Hashable,
    ) -> CategoricalIsomorphism:
        source_index = self.normalize_chart_index(source_index)
        target_index = self.normalize_chart_index(target_index)
        pair = self._ordered_pair(source_index, target_index)
        transition: CategoricalIsomorphism = self.source_transitions()[pair]
        if pair == (source_index, target_index):
            return transition
        key = (source_index, target_index)
        try:
            return self._reverse_source_transitions[key]
        except KeyError:
            reverse: CategoricalIsomorphism = Schemes(self.base_ring()).Core().Mor(
                transition.codomain(), transition.domain()
            )(transition.inverse(), transition.forward())
            self._reverse_source_transitions[key] = reverse
            return reverse

    def quotient_transition_between(
        self,
        source_index: Hashable,
        target_index: Hashable,
    ) -> CategoricalIsomorphism:
        source_index = self.normalize_chart_index(source_index)
        target_index = self.normalize_chart_index(target_index)
        pair = self._ordered_pair(source_index, target_index)
        transition: CategoricalIsomorphism = self.quotient_transitions()[pair]
        if pair == (source_index, target_index):
            return transition
        key = (source_index, target_index)
        try:
            return self._reverse_quotient_transitions[key]
        except KeyError:
            reverse: CategoricalIsomorphism = Schemes(self.base_ring()).Core().Mor(
                transition.codomain(), transition.domain()
            )(transition.inverse(), transition.forward())
            self._reverse_quotient_transitions[key] = reverse
            return reverse

    def _factor_through_distinguished_open(
        self,
        morphism: SchemeMorphism,
        open_subscheme: Scheme,
    ) -> SchemeMorphism:
        target_scheme: Scheme = morphism.codomain()
        if open_subscheme not in OpenImmersions(target_scheme):
            raise TypeError("the target must be a represented open subscheme")
        if not open_subscheme.is_distinguished_open():
            raise TypeError("the target open must be represented by one distinguished element")
        if morphism.domain() not in AffineSchemes(self.base_ring()):
            raise TypeError("distinguished-open factorization requires an affine source")

        target_algebra = target_scheme.coordinate_algebra()
        source_algebra = morphism.domain().coordinate_algebra()
        open_algebra = open_subscheme.coordinate_algebra()
        pullback = morphism.coordinate_algebra_morphism()
        defining_element = target_algebra(open_subscheme.distinguished_open_element())
        pulled_element = source_algebra(pullback(defining_element))
        if not pulled_element.is_unit():
            raise ValueError("the scheme morphism does not land in the stated distinguished open")

        def factor_pullback(element: Element) -> Element:
            numerator, denominator = open_algebra.localization_fraction_data(element)
            numerator_image: Element = source_algebra(pullback(numerator))
            denominator_image: Element = source_algebra(pullback(denominator))
            result: Element = numerator_image * denominator_image.inverse_of_unit()
            return result

        factor: SchemeMorphism = morphism.domain().Mor(open_subscheme)(
            open_algebra.Mor(source_algebra)(factor_pullback)
        )
        return factor

    def source_chart_action(
        self,
        index: Hashable,
        group_element: Element,
    ) -> SchemeMorphism:
        index = self.normalize_chart_index(index)
        assert group_element in self.acting_group(), (
            f"{group_element} is not an element of {self.acting_group()}"
        )
        normalized: Element = self.acting_group()(group_element)
        key = (index, normalized)
        try:
            return self._source_chart_actions[key]
        except KeyError:
            acted_action: SchemeMorphism = self.acted_charts()[index].action_of(normalized)
            source_chart = self.source_chart(index)
            transported: SchemeMorphism = Schemes(self.base_ring()).Mor(
                source_chart,
                source_chart,
            )(acted_action.coordinate_algebra_morphism())
            self._source_chart_actions[key] = transported
            return transported

    def _restricted_source_action(
        self,
        source_index: Hashable,
        target_index: Hashable,
        group_element: Element,
    ) -> SchemeMorphism:
        source_index = self.normalize_chart_index(source_index)
        target_index = self.normalize_chart_index(target_index)
        normalized: Element = self.acting_group()(group_element)
        key = (source_index, target_index, normalized)
        try:
            return self._source_overlap_actions[key]
        except KeyError:
            overlap: Scheme = self.source_transition_between(
                source_index,
                target_index,
            ).forward().domain()
            chart_map: SchemeMorphism = (
                self.source_chart_action(source_index, normalized) * overlap.inclusion()
            )
            try:
                restricted = self._factor_through_distinguished_open(chart_map, overlap)
            except ValueError as error:
                raise ValueError(
                    "the source group action does not preserve a represented gluing overlap"
                ) from error
            self._source_overlap_actions[key] = restricted
            return restricted

    def source_overlap_action(
        self,
        source_index: Hashable,
        target_index: Hashable,
        group_element: Element,
    ) -> SchemeMorphism:
        return self._restricted_source_action(source_index, target_index, group_element)

    def _verify_source_transition_equivariance(self) -> None:
        for source_index, target_index in self.pair_index_set():
            transition: SchemeMorphism = self.source_transition_between(
                source_index,
                target_index,
            ).forward()
            for group_generator in self.acting_group().group_generators():
                source_action = self._restricted_source_action(
                    source_index,
                    target_index,
                    group_generator,
                )
                target_action = self._restricted_source_action(
                    target_index,
                    source_index,
                    group_generator,
                )
                if transition * source_action != target_action * transition:
                    raise ValueError("a source overlap transition is not G-equivariant")

    def local_quotient_morphism(self, index: Hashable) -> SchemeMorphism:
        quotient_map: SchemeMorphism = self.acted_charts()[
            self.normalize_chart_index(index)
        ].quotient_morphism()
        return quotient_map

    def local_source_quotient_morphism(self, index: Hashable) -> SchemeMorphism:
        r"""Return the affine quotient pullback on the corresponding source chart."""

        index = self.normalize_chart_index(index)
        source_chart = self.source_chart(index)
        quotient_map = self.local_quotient_morphism(index)
        transported: SchemeMorphism = Schemes(self.base_ring()).Mor(
            source_chart,
            self.local_quotient(index),
        )(quotient_map.coordinate_algebra_morphism())
        return transported

    def _quotient_overlap_factor(
        self,
        source_index: Hashable,
        target_index: Hashable,
    ) -> SchemeMorphism:
        source_index = self.normalize_chart_index(source_index)
        target_index = self.normalize_chart_index(target_index)
        key = (source_index, target_index)
        try:
            return self._quotient_overlap_factors[key]
        except KeyError:
            source_overlap: Scheme = self.source_transition_between(
                source_index,
                target_index,
            ).forward().domain()
            quotient_overlap: Scheme = self.quotient_transition_between(
                source_index,
                target_index,
            ).forward().domain()
            restricted_quotient: SchemeMorphism = (
                self.local_source_quotient_morphism(source_index)
                * source_overlap.inclusion()
            )
            try:
                factor = self._factor_through_distinguished_open(
                    restricted_quotient,
                    quotient_overlap,
                )
            except ValueError as error:
                raise ValueError(
                    "a local quotient map does not land in the stated descended quotient overlap"
                ) from error
            self._quotient_overlap_factors[key] = factor
            return factor

    def quotient_overlap_factor(
        self,
        source_index: Hashable,
        target_index: Hashable,
    ) -> SchemeMorphism:
        return self._quotient_overlap_factor(source_index, target_index)

    def _verify_quotient_descent_squares(self) -> None:
        for source_index, target_index in self.pair_index_set():
            source_transition: SchemeMorphism = self.source_transition_between(
                source_index,
                target_index,
            ).forward()
            quotient_transition: SchemeMorphism = self.quotient_transition_between(
                source_index,
                target_index,
            ).forward()
            source_factor = self._quotient_overlap_factor(source_index, target_index)
            target_factor = self._quotient_overlap_factor(target_index, source_index)
            if quotient_transition * source_factor != target_factor * source_transition:
                raise ValueError("a descended quotient-overlap map fails its quotient descent square")

    def _chart_map_into_source(
        self,
        index: Hashable,
        local_affine_map: SchemeMorphism,
    ) -> SchemeMorphism:
        source_chart = self.source_chart(index)
        parent: CategoricalHomset = source_chart.Mor(self.source_scheme())
        return _ChartMapIntoGluedScheme(parent, source_chart, local_affine_map)

    def _chart_map_into_quotient(
        self,
        index: Hashable,
        local_affine_map: SchemeMorphism,
    ) -> SchemeMorphism:
        quotient_chart = self.local_quotient(index)
        parent: CategoricalHomset = self.source_chart(index).Mor(self.quotient_scheme())
        return _ChartMapIntoGluedScheme(parent, quotient_chart, local_affine_map)

    def _action_morphism(self, group_element: Element) -> SchemeMorphism:
        assert group_element in self.acting_group(), (
            f"{group_element} is not an element of {self.acting_group()}"
        )
        normalized: Element = self.acting_group()(group_element)
        if normalized == self.acting_group().one():
            return self.source_scheme().categorical_identity_morphism()
        try:
            return self._action_morphisms[normalized]
        except KeyError:
            local_maps = finite_indexed_family(
                self.chart_index_set(),
                lambda index: self._chart_map_into_source(
                    index,
                    self.source_chart_action(index, normalized),
                ),
                name="Chart maps of one glued group action morphism",
            )
            parent: CategoricalHomset = self.source_scheme().Mor(self.source_scheme())
            morphism = _GluedGroupActionMorphism(
                parent,
                self.source_charts(),
                local_maps,
                self,
                normalized,
            )
            self._action_morphisms[normalized] = morphism
            return morphism

    def action(self) -> SetMorphism:
        if self._action is None:
            endomorphisms = self.source_scheme().Mor(self.source_scheme())
            action: SetMorphism = Sets().Mor(self.acting_group(), endomorphisms)(
                lambda group_element: self._action_morphism(group_element)
            )
            self._action = action
        return self._action

    global_action = action

    def action_of(self, group_element: Element) -> SchemeMorphism:
        action_morphism: SchemeMorphism = self.action()(group_element)
        return action_morphism

    def fixed_locus_is_empty(self, group_element) -> bool:
        r"""Decide emptiness of ``X^g`` on the invariant affine atlas.

        The source atlas is preserved by the global action, so the fixed locus
        is empty exactly when its intersection with every affine chart is
        empty.  Each chart computes the full scheme-theoretic fixed ideal; no
        reduction is taken here.
        """
        normalized = self.acting_group()(group_element)
        return all(
            self.acted_chart(index).fixed_subobject_of(normalized).is_empty()
            for index in self.chart_index_set()
        )

    def common_fixed_locus_is_empty(self) -> bool:
        r"""Decide whether ``X^G`` is empty by the represented invariant atlas."""
        return all(
            self.acted_chart(index).fixed_subscheme().is_empty()
            for index in self.chart_index_set()
        )

    def nontrivial_stabilizer_locus_is_empty(self) -> bool:
        r"""Decide whether every nonidentity stabilizer locus misses every chart."""
        return all(
            self.acted_chart(index).nontrivial_stabilizer_subscheme().is_empty()
            for index in self.chart_index_set()
        )

    def action_is_free(self):
        r"""Decide freeness locally on the represented invariant affine cover.

        Freeness is local on the source.  This deliberately tests the union of
        all nonidentity fixed loci chartwise, rather than the common fixed
        locus ``X^G``.
        """
        return self.nontrivial_stabilizer_locus_is_empty()

    def quotient_morphism(self) -> SchemeMorphism:
        if self._quotient_morphism is None:
            local_maps = finite_indexed_family(
                self.chart_index_set(),
                lambda index: self._chart_map_into_quotient(
                    index,
                    self.local_source_quotient_morphism(index),
                ),
                name="Chart maps of the glued invariant quotient morphism",
            )
            parent: CategoricalHomset = self.source_scheme().Mor(self.quotient_scheme())
            self._quotient_morphism = _GluedInvariantQuotientMorphism(
                parent,
                self.source_charts(),
                local_maps,
                self,
            )
        return self._quotient_morphism

    def factor_invariant_affine_morphism(
        self,
        morphism: SchemeMorphism,
    ) -> SchemeMorphism:
        r"""Return the unique affine-target factor of an invariant source morphism."""

        if morphism.domain() is not self.source_scheme():
            raise ValueError("the invariant morphism must start at the glued quotient source")
        target: Scheme = morphism.codomain()
        assert target in AffineSchemes(self.base_ring()), (
            "the represented glued-quotient universal property is the affine-target factorization"
        )
        represented = self.source_scheme().Mor(target)(morphism)
        local_maps = finite_indexed_family(
            self.chart_index_set(),
            lambda index: represented.local_map(index),
            name="Local maps of an invariant morphism from the glued source",
        )

        for index in self.chart_index_set():
            local_map: SchemeMorphism = local_maps[index]
            for group_generator in self.acting_group().group_generators():
                if local_map * self.source_chart_action(index, group_generator) != local_map:
                    raise ValueError("the glued morphism is not invariant under the source G-action")

        def local_factor(index: Hashable) -> SchemeMorphism:
            local_map: SchemeMorphism = local_maps[index]
            acted_chart = self.acted_charts()[index]
            acted_local_map: SchemeMorphism = Schemes(self.base_ring()).Mor(
                acted_chart,
                target,
            )(local_map.coordinate_algebra_morphism())
            factor: SchemeMorphism = acted_chart.factor_through_affine_quotient(
                acted_local_map
            )
            return factor

        local_factors = finite_indexed_family(
            self.chart_index_set(),
            local_factor,
            name="Local affine factors through the glued invariant quotient",
        )
        for source_index, target_index in self.pair_index_set():
            transition: SchemeMorphism = self.quotient_transition_between(
                source_index,
                target_index,
            ).forward()
            source_overlap: Scheme = transition.domain()
            target_overlap: Scheme = transition.codomain()
            source_restriction: SchemeMorphism = (
                local_factors[source_index] * source_overlap.inclusion()
            )
            target_restriction: SchemeMorphism = (
                local_factors[target_index]
                * target_overlap.inclusion()
                * transition
            )
            if source_restriction != target_restriction:
                raise ArithmeticError(
                    "the local affine quotient factors do not descend through the quotient overlaps"
                )

        parent: CategoricalHomset = self.quotient_scheme().Mor(target)
        factor = _InvariantAffineFactorMorphism(
            parent,
            self.local_quotients(),
            local_factors,
            self,
            morphism,
        )
        for index in self.chart_index_set():
            local_map: SchemeMorphism = local_maps[index]
            if (
                factor.local_map(index) * self.local_source_quotient_morphism(index)
                != local_map
            ):
                raise ArithmeticError("an affine quotient factor failed its defining local triangle")
        return factor

    factor_through_quotient = factor_invariant_affine_morphism

    def descend_invariant_family(self, family_morphism: SchemeMorphism) -> SchemeMorphism:
        r"""Descend an invariant family map from the glued source to an affine base.

        The local factors are the affine quotient universal maps and their
        compatibility on overlaps is already verified by
        :meth:`factor_invariant_affine_morphism`.  Thus this is the family
        spelling of the same universal quotient, not an additional descent
        algorithm.
        """
        return self.factor_invariant_affine_morphism(family_morphism)

    def _repr_(self) -> str:
        return (
            f"Finite glued invariant quotient over {self.base_ring()} "
            f"by {self.acting_group()}"
        )


def _c2_invariant_localization_lift(
    acted_chart,
    source_overlap,
    quotient_overlap,
    element,
):
    r"""Lift one invariant of ``A[d^-1]`` to ``A^G[N(d)^-1]`` for C2.

    If ``element=n/e`` is invariant and ``g`` is the nonidentity element, then
    ``n g(e)`` and ``e g(e)`` are invariant.  The latter is a power/unit
    multiple of the norm defining the quotient principal open, so its image is
    invertible there.  This avoids choosing a semi-invariant sign for ``d``.
    """
    group = acted_chart.acting_group()
    assert int(group.order()) == 2, (
        "the represented stable-principal-open invariant descent is the C2 specialization"
    )
    generator = next(iter(group.group_generators()))
    overlap_ring = source_overlap.coordinate_algebra()
    numerator, denominator = overlap_ring.localization_fraction_data(element)
    source_algebra = acted_chart.coordinate_algebra()
    action_pullback = acted_chart.action_of(generator).coordinate_algebra_morphism()
    numerator = source_algebra(numerator)
    denominator = source_algebra(denominator)
    conjugate_denominator = action_pullback(denominator)
    invariant_numerator = numerator * conjugate_denominator
    invariant_denominator = denominator * conjugate_denominator
    numerator_lift = acted_chart.invariant_algebra_element(invariant_numerator)
    denominator_lift = acted_chart.invariant_algebra_element(invariant_denominator)
    quotient_ring = quotient_overlap.coordinate_algebra()
    localization = quotient_ring.localization_map()
    denominator_image = localization(denominator_lift)
    if not denominator_image.is_unit():
        raise ArithmeticError(
            "the norm of an overlap denominator is not invertible on the descended quotient open"
        )
    return localization(numerator_lift) * denominator_image.inverse_of_unit()


def _c2_quotient_overlap_transition(
    datum,
    acted_charts,
    quotient_opens,
    source_index,
    target_index,
):
    source_overlap = datum.overlap(source_index, target_index)
    target_overlap = datum.overlap(target_index, source_index)
    transition = datum.transition_between(source_index, target_index).forward()
    transition_pullback = transition.coordinate_algebra_morphism()
    source_acted = acted_charts[source_index]
    target_acted = acted_charts[target_index]
    source_quotient_open = quotient_opens[source_index, target_index]
    target_quotient_open = quotient_opens[target_index, source_index]
    target_inclusion = target_acted.invariant_algebra_inclusion()
    target_localization = target_overlap.coordinate_algebra().localization_map()
    target_quotient_ring = target_quotient_open.coordinate_algebra()
    source_quotient_ring = source_quotient_open.coordinate_algebra()

    def pullback(element):
        numerator, denominator = target_quotient_ring.localization_fraction_data(element)

        def map_invariant(value):
            target_value = target_localization(target_inclusion(value))
            source_value = transition_pullback(target_value)
            return _c2_invariant_localization_lift(
                source_acted,
                source_overlap,
                source_quotient_open,
                source_value,
            )

        numerator_image = map_invariant(numerator)
        denominator_image = map_invariant(denominator)
        if not denominator_image.is_unit():
            raise ArithmeticError(
                "a descended quotient-overlap denominator is not invertible"
            )
        return numerator_image * denominator_image.inverse_of_unit()

    return source_quotient_open.Mor(target_quotient_open)(
        target_quotient_ring.Mor(source_quotient_ring)(pullback)
    )


def _c2_chartwise_glued_invariant_quotient(
    source_scheme: Scheme,
    acting_group: Parent,
    local_actions: IndexedFamily,
) -> FiniteGluedInvariantQuotient:
    r"""Quotient a glued scheme by a chart-preserving C2 action.

    Every source overlap is a stable distinguished open.  Its defining element
    ``d`` need only be semi-invariant: the norm ``d g(d)`` is invariant and
    defines the descended principal open in the affine quotient chart.  The
    quotient transition is obtained by transporting invariant rational
    functions through the source transition and expressing them in the source
    invariant algebra via the common invariant-ring certificate.
    """
    assert int(acting_group.order()) == 2, (
        "automatic chartwise invariant-quotient descent is represented here for C2"
    )
    datum = source_scheme.gluing_datum()
    indices = datum.chart_index_set()
    if tuple(local_actions.index_set()) != tuple(indices):
        raise ValueError("the local action family must use the source chart labels")
    base = source_scheme.scheme_base_ring()
    group_generator = next(iter(acting_group.group_generators()))
    acted_charts = finite_indexed_family(
        indices,
        lambda index: AffineGSchemes(acting_group, base)(
            datum.chart(index),
            lambda element, index=index: (
                datum.chart(index).categorical_identity_morphism()
                if acting_group(element) == acting_group.one()
                else local_actions[index]
            ),
        ),
        name="Acted affine charts of a chartwise C2 quotient",
    )
    pair_indices = finite_ordered_set(tuple(datum.transition_index_set()))
    source_transitions = finite_indexed_family(
        pair_indices,
        lambda pair: datum.transition_between(*pair),
        name="Source transitions of a chartwise C2 quotient",
    )
    quotient_opens = {}
    for source_index, target_index in datum.transition_index_set():
        for left, right in ((source_index, target_index), (target_index, source_index)):
            source_overlap = datum.overlap(left, right)
            source_algebra = datum.chart(left).coordinate_algebra()
            defining = source_algebra(source_overlap.distinguished_open_element())
            action_pullback = acted_charts[left].action_of(
                group_generator
            ).coordinate_algebra_morphism()
            norm = defining * action_pullback(defining)
            invariant_norm = acted_charts[left].invariant_algebra_element(norm)
            quotient_opens[left, right] = acted_charts[left].affine_quotient().distinguished_open(
                invariant_norm
            )
    quotient_transitions_by_pair = {}
    for left, right in datum.transition_index_set():
        forward = _c2_quotient_overlap_transition(
            datum, acted_charts, quotient_opens, left, right
        )
        inverse = _c2_quotient_overlap_transition(
            datum, acted_charts, quotient_opens, right, left
        )
        quotient_transitions_by_pair[left, right] = Schemes(base).Core().Mor(
            forward.domain(), forward.codomain()
        )(forward, inverse)
    quotient_transitions = finite_indexed_family(
        pair_indices,
        lambda pair: quotient_transitions_by_pair[pair],
        name="Descended quotient transitions of a chartwise C2 quotient",
    )
    return FiniteGluedInvariantQuotient(
        base,
        acting_group,
        acted_charts,
        source_transitions,
        quotient_transitions,
        source_scheme=source_scheme,
    )



__all__ = [
    "FiniteGluedInvariantQuotient",
]
