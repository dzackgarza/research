r"""Descent and gluing for represented schemes, modules, and algebras."""

from collections.abc import Mapping
from itertools import combinations, permutations

from sage.categories.category import Category
from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_method
from sage.misc.classcall_metaclass import typecall
from sage.schemes.generic.glue import GluedScheme as SageGluedScheme
from sage.schemes.generic.scheme import Scheme as SageScheme
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
    Isomorphism,
)
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoricalIsomorphism,
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    CommutativeAlgebras,
)
from dzack_research.preamble.categories.algebras.restricted_scalars import (
    restrict_algebra_scalars,
)
from dzack_research.preamble.categories.functors.algebra_modules import (
    algebra_underlying_module_functor,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
    restrict_scalars,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSchemes,
    OpenImmersions,
    SchemeMorCategory,
    SchemeMorphism,
    Spec,
    _fresh_affine_spectrum,
    refine_scheme,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


def _chart_pair(cover, left_index, right_index):
    r"""The two chart labels in the atlas order, which is how descent data is keyed."""

    labels = (cover.chart_label(left_index), cover.chart_label(right_index))
    if labels[0] == labels[1]:
        raise ValueError("descent data is keyed by two distinct charts")
    return tuple(sorted(labels, key=cover.atlas().ranking_map()))


def _family_on_finite_ordered_set(index_set, values, *, name, noun):
    r"""Normalize finite input to an indexed family on ``index_set``."""

    expected = int(index_set.cardinality().finite_value())
    if isinstance(values, IndexedFamily):
        if not values.cardinality().is_finite():
            raise TypeError(f"{noun} must be a finite indexed family")
        if int(values.cardinality().finite_value()) != expected:
            raise ValueError(f"{noun} has the wrong number of entries")
        try:
            entries = tuple(values[index] for index in index_set)
        except (IndexError, KeyError, TypeError, ValueError) as error:
            raise ValueError(f"{noun} is not indexed by the required labels") from error
    elif isinstance(values, Mapping):
        if len(values) != expected:
            raise ValueError(f"{noun} has the wrong number of entries")
        try:
            entries = tuple(values[index] for index in index_set)
        except (KeyError, TypeError) as error:
            raise ValueError(f"{noun} is not indexed by the required labels") from error
    else:
        entries = tuple(values)
        if len(entries) != expected:
            raise ValueError(f"{noun} has the wrong number of entries")

    return finite_indexed_family(
        index_set,
        lambda index: entries[int(index_set.ranking_map()(index))],
        name=name,
    )


def _finite_chart_family(charts):
    r"""Return one nonempty finite ordered family of chart candidates."""

    if isinstance(charts, IndexedFamily):
        if not charts.cardinality().is_finite():
            raise TypeError("scheme gluing requires a finite indexed family of affine charts")
        index_set = finite_ordered_set(charts.index_set())
        family = finite_indexed_family(
            index_set,
            lambda index: charts[index],
            name="Affine charts of a finite scheme gluing",
        )
    elif isinstance(charts, Mapping):
        index_set = finite_ordered_set(tuple(charts))
        family = finite_indexed_family(
            index_set,
            lambda index: charts[index],
            name="Affine charts of a finite scheme gluing",
        )
    else:
        entries = tuple(charts)
        index_set = finite_ordered_set(range(len(entries)))
        family = finite_indexed_family(
            index_set,
            lambda index: entries[int(index_set.ranking_map()(index))],
            name="Affine charts of a finite scheme gluing",
        )
    if int(family.cardinality().finite_value()) == 0:
        raise ValueError("scheme gluing requires at least one affine chart")
    return family


class _GluedSchemeOpenInclusion(SchemeMorphism):
    r"""The chosen inclusion of one chart image into the glued scheme."""

    def __init__(self, parent, gluing_datum, chart_index) -> None:
        Morphism.__init__(self, parent)
        self._preamble_domain_override = None
        self._preamble_codomain_override = None
        self._gluing_datum = gluing_datum
        self._chart_index = gluing_datum.normalize_chart_index(chart_index)

    def gluing_datum(self):
        return self._gluing_datum

    def chart_index(self):
        return self._chart_index

    def native_morphism(self):
        raise NotImplementedError(
            "the chart-image inclusion is represented by the glued-scheme construction, "
            "not by one affine native morphism"
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, _GluedSchemeOpenInclusion)
            and other.gluing_datum() is self.gluing_datum()
            and other.chart_index() == self.chart_index()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        position = self.gluing_datum().chart_index_set().ranking_map()(self.chart_index())
        return hash((id(self.gluing_datum()), int(position), "open-image"))

    def _repr_(self):
        return f"Open inclusion {self.domain()} -> {self.codomain()}"


class _GluedSchemeChartEmbedding(SchemeMorphism):
    r"""One canonical chart map into a represented two-chart glued scheme."""

    def __init__(
        self,
        parent,
        gluing_datum,
        chart_index,
        open_image,
        chart_isomorphism,
    ) -> None:
        Morphism.__init__(self, parent)
        self._preamble_domain_override = None
        self._preamble_codomain_override = None
        self._gluing_datum = gluing_datum
        self._chart_index = gluing_datum.normalize_chart_index(chart_index)
        self._preamble_open_image = open_image
        self._preamble_open_image_isomorphism = chart_isomorphism
        self._chart_isomorphism = chart_isomorphism

    def gluing_datum(self):
        return self._gluing_datum

    def chart_index(self):
        return self._chart_index

    def open_image(self):
        return self._preamble_open_image

    def chart_isomorphism(self):
        return self._chart_isomorphism

    def open_inclusion(self):
        return self.open_image().inclusion()

    def native_morphism(self):
        raise NotImplementedError(
            "the canonical chart embedding is represented by the glued-scheme construction, "
            "not by one affine native morphism"
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, _GluedSchemeChartEmbedding)
            and other.gluing_datum() is self.gluing_datum()
            and other.chart_index() == self.chart_index()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __hash__(self) -> int:
        position = self.gluing_datum().chart_index_set().ranking_map()(self.chart_index())
        return hash((id(self.gluing_datum()), int(position)))

    def _repr_(self):
        return (
            f"Open chart embedding {self.domain()} -> {self.codomain()} "
            f"(chart {self.chart_index()})"
        )


class _GluedSchemeMorphism(SchemeMorphism):
    r"""A morphism out of a glued scheme, represented by compatible chart maps."""

    def __init__(self, parent, local_maps, *, verify_compatibility=True) -> None:
        Morphism.__init__(self, parent)
        self._preamble_domain_override = None
        self._preamble_codomain_override = None
        datum = self.domain().gluing_datum()
        raw_local_maps = _family_on_finite_ordered_set(
            datum.chart_index_set(),
            local_maps,
            name="Raw local maps of a glued-scheme morphism",
            noun="a glued-scheme morphism",
        )
        self._local_maps = finite_indexed_family(
            datum.chart_index_set(),
            lambda index: datum.chart(index).Mor(self.codomain())(
                raw_local_maps[index]
            ),
            name="Local maps of a glued-scheme morphism",
        )
        if verify_compatibility:
            self._verify_overlap_compatibility()

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[
            self.domain().gluing_datum().normalize_chart_index(index)
        ]

    def native_morphism(self):
        raise NotImplementedError(
            "this morphism is represented by its compatible maps on the glued affine charts"
        )

    def _verify_overlap_compatibility(self) -> None:
        datum = self.domain().gluing_datum()
        for left_index, right_index in combinations(tuple(datum.chart_indices()), 2):
            left_overlap = datum.overlap(left_index, right_index)
            right_overlap = datum.overlap(right_index, left_index)
            transition = datum.transition_between(left_index, right_index).forward()
            left_restriction = self.local_map(left_index) * left_overlap.inclusion()
            right_restriction = (
                self.local_map(right_index)
                * right_overlap.inclusion()
                * transition
            )
            if left_restriction != right_restriction:
                raise ValueError(
                    "the local scheme morphisms do not agree through the overlap transition"
                )

    def _postcompose_with(self, after):
        if after.domain() is not self.codomain():
            return NotImplemented
        return self.domain().Mor(after.codomain())(
            tuple(after * local_map for local_map in self.local_maps())
        )

    def __mul__(self, other):
        if self._is_the_identity():
            return other
        if (
            isinstance(other, _GluedSchemeChartEmbedding)
            and other.codomain() is self.domain()
            and other.gluing_datum() is self.domain().gluing_datum()
        ):
            return self.local_map(other.chart_index())
        if other.codomain() is not self.domain():
            return NotImplemented
        if other._is_the_identity():
            return self
        return NotImplemented

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, _GluedSchemeMorphism)
            and other.domain() is self.domain()
            and other.codomain() is self.codomain()
            and all(
                self.local_map(index) == other.local_map(index)
                for index in self.domain().gluing_datum().chart_indices()
            )
        )

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None

    def _repr_(self):
        return f"Scheme morphism from glued charts: {self.domain()} -> {self.codomain()}"


class _GluedSchemeMorCategory(SchemeMorCategory):
    r"""Maps out of a finite glued scheme, represented by compatible local maps."""

    def _element_constructor_(self, datum):
        if isinstance(datum, _GluedSchemeMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the glued-scheme morphism has the wrong endpoints")
            if datum.parent() is self:
                return datum
            datum = datum.local_maps()
        if isinstance(datum, (tuple, list, IndexedFamily, Mapping)):
            return _GluedSchemeMorphism(self, datum)
        return super()._element_constructor_(datum)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on a glued-scheme endomorphism Hom")
        datum = self.domain().gluing_datum()
        return _GluedSchemeMorphism(
            self,
            tuple(
                datum.chart_embedding(index)
                for index in datum.chart_indices()
            ),
            verify_compatibility=False,
        )


def _install_glued_scheme_structure(datum, scheme) -> None:
    r"""Install the owned chart/open/Hom structure on one verified glued carrier."""

    datum._scheme = scheme
    scheme._preamble_scheme_homset_class = _GluedSchemeMorCategory
    refine_scheme(scheme, datum.base_ring())

    chart_images = []
    chart_isomorphisms = []
    chart_embeddings = []
    for index in datum.chart_indices():
        chart = datum.chart(index)
        algebra = chart.coordinate_algebra()
        chart_image = _fresh_affine_spectrum(
            algebra,
            datum.base_ring(),
            extra_categories=(OpenImmersions(scheme),),
        )
        open_inclusion = _GluedSchemeOpenInclusion(
            chart_image.Mor(scheme),
            datum,
            index,
        )
        chart_image._preamble_inclusion = open_inclusion
        identity_pullback = algebra.Mor(algebra).identity()
        chart_isomorphism = Isomorphism(
            chart.Mor(chart_image)(identity_pullback),
            chart_image.Mor(chart)(identity_pullback),
        )
        chart_embedding = _GluedSchemeChartEmbedding(
            chart.Mor(scheme),
            datum,
            index,
            chart_image,
            chart_isomorphism,
        )
        chart_images.append(chart_image)
        chart_isomorphisms.append(chart_isomorphism)
        chart_embeddings.append(chart_embedding)

    datum._chart_images = _family_on_finite_ordered_set(
        datum.chart_index_set(),
        chart_images,
        name="Open chart images in glued scheme",
        noun="open chart images",
    )
    datum._chart_isomorphisms = _family_on_finite_ordered_set(
        datum.chart_index_set(),
        chart_isomorphisms,
        name="Chart-to-image isomorphisms",
        noun="chart-to-image isomorphisms",
    )
    datum._chart_embeddings = _family_on_finite_ordered_set(
        datum.chart_index_set(),
        chart_embeddings,
        name="Scheme gluing chart embeddings",
        noun="scheme gluing chart embeddings",
    )
    scheme._preamble_identity_morphism = scheme.Mor(scheme).identity()
    base_scheme = Spec(datum.base_ring(), base_ring=datum.base_ring())
    scheme._preamble_structure_morphism = scheme.Mor(base_scheme)(
        tuple(chart.structure_morphism() for chart in datum.charts())
    )


class _OwnedTwoChartGluedScheme(SageGluedScheme):
    r"""A scheme obtained by gluing two affine charts along represented affine opens."""

    def __init__(self, gluing_datum, left_native, right_native) -> None:
        self._preamble_gluing_datum = gluing_datum
        SageGluedScheme.__init__(self, left_native, right_native, check=True)
        SageScheme.__init__(self, _engine_ring(gluing_datum.base_ring()))

    def gluing_datum(self):
        return self._preamble_gluing_datum

    def chart(self, index):
        return self.gluing_datum().chart(index)

    def charts(self):
        return self.gluing_datum().charts()

    def chart_index_set(self):
        return self.gluing_datum().chart_index_set()

    def chart_images(self):
        return self.gluing_datum().chart_images()

    def chart_image(self, index):
        return self.gluing_datum().chart_image(index)

    def chart_isomorphism(self, index):
        return self.gluing_datum().chart_isomorphism(index)

    def chart_embedding(self, index):
        return self.gluing_datum().chart_embedding(index)

    def overlap_transition(self):
        return self.gluing_datum().transition()


class _TwoChartSchemeGluingDatum(SageObject):
    r"""Two affine schemes glued along an isomorphism of represented affine opens."""

    def __init__(self, schemes, left_chart, right_chart, transition) -> None:
        base = schemes.base_ring()
        if left_chart not in AffineSchemes(base) or right_chart not in AffineSchemes(base):
            raise TypeError("the represented two-chart gluing currently requires affine charts")
        if not isinstance(transition, CategoricalIsomorphism):
            raise TypeError("scheme gluing requires a represented overlap isomorphism")
        forward = transition.forward()
        inverse = transition.inverse()
        if not isinstance(forward, SchemeMorphism) or not isinstance(inverse, SchemeMorphism):
            raise TypeError("the overlap transition must be an isomorphism of schemes")
        left_overlap = forward.domain()
        right_overlap = forward.codomain()
        if left_overlap not in OpenImmersions(left_chart):
            raise ValueError("the transition domain must be a represented open subscheme of the left chart")
        if right_overlap not in OpenImmersions(right_chart):
            raise ValueError("the transition codomain must be a represented open subscheme of the right chart")
        if inverse.domain() is not right_overlap or inverse.codomain() is not left_overlap:
            raise ValueError("the stated overlap inverse has the wrong endpoints")
        if inverse * forward != left_overlap.categorical_identity_morphism():
            raise ValueError("the overlap transition is not left-invertible")
        if forward * inverse != right_overlap.categorical_identity_morphism():
            raise ValueError("the overlap transition is not right-invertible")

        self._schemes = schemes
        self._charts = finite_family(
            (left_chart, right_chart),
            name="Scheme gluing charts",
        )
        self._transition = transition
        self._scheme = None
        self._chart_images = None
        self._chart_isomorphisms = None
        self._chart_embeddings = None
        self._construct_glued_scheme()

    def base_ring(self):
        return self._schemes.base_ring()

    def charts(self):
        return self._charts

    def chart(self, index):
        return self.charts()[self.normalize_chart_index(index)]

    def chart_index_set(self):
        return self.charts().index_set()

    def normalize_chart_index(self, index):
        return self.chart_index_set()(index)

    def number_of_charts(self):
        return 2

    def chart_indices(self):
        return self.chart_index_set()

    def transition(self):
        return self._transition

    def transition_between(self, source_index, target_index):
        source_index = int(self.normalize_chart_index(source_index))
        target_index = int(self.normalize_chart_index(target_index))
        if source_index == target_index:
            raise ValueError("a scheme-gluing transition is between distinct charts")
        if (source_index, target_index) == (0, 1):
            return self.transition()
        if (source_index, target_index) == (1, 0):
            return Isomorphism(self.transition().inverse(), self.transition().forward())
        raise IndexError("two-chart gluing has only chart indices 0 and 1")

    def overlap(self, source_index, target_index):
        return self.transition_between(source_index, target_index).forward().domain()

    def left_overlap(self):
        return self.transition().forward().domain()

    def right_overlap(self):
        return self.transition().forward().codomain()

    def _construct_glued_scheme(self) -> None:
        left_inclusion = self.left_overlap().inclusion()
        right_inclusion = self.right_overlap().inclusion()
        right_span = right_inclusion * self.transition().forward()
        scheme = _OwnedTwoChartGluedScheme(
            self,
            left_inclusion.native_morphism(),
            right_span.native_morphism(),
        )
        _install_glued_scheme_structure(self, scheme)

    def scheme(self):
        return self._scheme

    def chart_embedding(self, index):
        return self._chart_embeddings[self.normalize_chart_index(index)]

    def chart_images(self):
        return self._chart_images

    def chart_image(self, index):
        return self.chart_images()[self.normalize_chart_index(index)]

    def chart_isomorphisms(self):
        return self._chart_isomorphisms

    def chart_isomorphism(self, index):
        return self.chart_isomorphisms()[self.normalize_chart_index(index)]

    def _repr_(self):
        return f"Two-chart scheme gluing datum for {self.chart(0)} and {self.chart(1)}"


class _OwnedFiniteGluedScheme(SageScheme):
    r"""The owned carrier of a verified finite affine gluing datum."""

    def __init__(self, gluing_datum) -> None:
        self._preamble_gluing_datum = gluing_datum
        SageScheme.__init__(self, _engine_ring(gluing_datum.base_ring()))

    def gluing_datum(self):
        return self._preamble_gluing_datum

    def chart_index_set(self):
        return self.gluing_datum().chart_index_set()

    def chart_indices(self):
        return self.gluing_datum().chart_indices()

    def number_of_charts(self):
        return self.gluing_datum().number_of_charts()

    def charts(self):
        return self.gluing_datum().charts()

    def chart(self, index):
        return self.gluing_datum().chart(index)

    def transitions(self):
        return self.gluing_datum().transitions()

    def transition_between(self, source_index, target_index):
        return self.gluing_datum().transition_between(source_index, target_index)

    def overlap(self, source_index, target_index):
        return self.gluing_datum().overlap(source_index, target_index)

    def triple_overlap(self, source_index, middle_index, target_index):
        return self.gluing_datum().triple_overlap(
            source_index,
            middle_index,
            target_index,
        )

    def transition_on_triple(self, source_index, target_index, third_index):
        return self.gluing_datum().transition_on_triple(
            source_index,
            target_index,
            third_index,
        )

    def chart_images(self):
        return self.gluing_datum().chart_images()

    def chart_image(self, index):
        return self.gluing_datum().chart_image(index)

    def chart_isomorphism(self, index):
        return self.gluing_datum().chart_isomorphism(index)

    def chart_embedding(self, index):
        return self.gluing_datum().chart_embedding(index)

    def _repr_(self):
        return f"Scheme glued from affine atlas indexed by {self.chart_index_set()}"


class _FiniteSchemeGluingDatum(SageObject):
    r"""Finite affine charts with distinguished pair overlaps and a cocycle."""

    def __init__(self, schemes, charts, transitions) -> None:
        self._schemes = schemes
        self._charts = _finite_chart_family(charts)
        for chart in self.charts():
            if chart not in AffineSchemes(self.base_ring()):
                raise TypeError("finite scheme gluing currently requires affine charts")

        pair_indices = finite_ordered_set(
            tuple(combinations(tuple(self.chart_indices()), 2))
        )
        self._transitions = _family_on_finite_ordered_set(
            pair_indices,
            transitions,
            name="Pair transitions of a finite scheme gluing",
            noun="finite scheme-gluing transition data",
        )
        self._reverse_transitions = []
        self._triple_overlaps = []
        self._triple_transition_maps = []
        self._scheme = None
        self._chart_images = None
        self._chart_isomorphisms = None
        self._chart_embeddings = None

        self._verify_pairwise_transitions()
        self._verify_triple_domains_and_cocycle()
        self._construct_glued_scheme()

    def base_ring(self):
        return self._schemes.base_ring()

    def charts(self):
        return self._charts

    def chart_index_set(self):
        return self.charts().index_set()

    def chart_indices(self):
        return self.chart_index_set()

    def normalize_chart_index(self, index):
        return self.chart_index_set()(index)

    def number_of_charts(self):
        return int(self.chart_index_set().cardinality().finite_value())

    def chart(self, index):
        return self.charts()[self.normalize_chart_index(index)]

    def transition_index_set(self):
        return self.transitions().index_set()

    def transitions(self):
        return self._transitions

    def _ordered_pair(self, left_index, right_index):
        left_index = self.normalize_chart_index(left_index)
        right_index = self.normalize_chart_index(right_index)
        if left_index == right_index:
            raise ValueError("a scheme-gluing transition is between distinct charts")
        indices = self.chart_index_set()
        index_ranking = indices.ranking_map()
        if index_ranking(left_index) < index_ranking(right_index):
            return left_index, right_index
        return right_index, left_index

    def transition_between(self, source_index, target_index):
        source_index = self.normalize_chart_index(source_index)
        target_index = self.normalize_chart_index(target_index)
        pair = self._ordered_pair(source_index, target_index)
        transition = self.transitions()[pair]
        if pair == (source_index, target_index):
            return transition
        key = (source_index, target_index)
        for cached_key, cached in self._reverse_transitions:
            if cached_key == key:
                return cached
        reversed_transition = Isomorphism(
            transition.inverse(),
            transition.forward(),
        )
        self._reverse_transitions.append((key, reversed_transition))
        return reversed_transition

    def overlap(self, source_index, target_index):
        return self.transition_between(source_index, target_index).forward().domain()

    def _verify_pairwise_transitions(self) -> None:
        for source_index, target_index in self.transition_index_set():
            transition = self.transitions()[source_index, target_index]
            if not isinstance(transition, CategoricalIsomorphism):
                raise TypeError("scheme gluing requires represented overlap isomorphisms")
            forward = transition.forward()
            inverse = transition.inverse()
            if not isinstance(forward, SchemeMorphism) or not isinstance(
                inverse, SchemeMorphism
            ):
                raise TypeError("each finite-atlas transition must be an isomorphism of schemes")
            source_overlap = forward.domain()
            target_overlap = forward.codomain()
            source_chart = self.chart(source_index)
            target_chart = self.chart(target_index)
            if source_overlap not in OpenImmersions(source_chart):
                raise ValueError("a transition domain must be a represented open of its source chart")
            if target_overlap not in OpenImmersions(target_chart):
                raise ValueError("a transition codomain must be a represented open of its target chart")
            if not source_overlap.is_distinguished_open() or not target_overlap.is_distinguished_open():
                raise TypeError("finite scheme gluing currently requires distinguished affine pair overlaps")
            if inverse.domain() is not target_overlap or inverse.codomain() is not source_overlap:
                raise ValueError("a finite-atlas transition inverse has the wrong overlap endpoints")
            if inverse * forward != source_overlap.categorical_identity_morphism():
                raise ValueError("a finite-atlas transition is not left-invertible")
            if forward * inverse != target_overlap.categorical_identity_morphism():
                raise ValueError("a finite-atlas transition is not right-invertible")

    def _triple_key(self, source_index, middle_index, target_index):
        source_index = self.normalize_chart_index(source_index)
        middle_index = self.normalize_chart_index(middle_index)
        target_index = self.normalize_chart_index(target_index)
        chart_ranking = self.chart_index_set().ranking_map()
        if len({
            chart_ranking(source_index),
            chart_ranking(middle_index),
            chart_ranking(target_index),
        }) != 3:
            raise ValueError("a triple overlap requires three distinct chart indices")
        others = sorted(
            (middle_index, target_index),
            key=chart_ranking,
        )
        return source_index, others[0], others[1]

    def triple_overlap(self, source_index, middle_index, target_index):
        r"""Return ``U_ij cap U_ik = D(f_ij f_ik)`` inside ``X_i``."""

        key = self._triple_key(source_index, middle_index, target_index)
        for cached_key, cached in self._triple_overlaps:
            if cached_key == key:
                return cached
        source_index, middle_index, target_index = key
        source_chart = self.chart(source_index)
        left_element = self.overlap(
            source_index,
            middle_index,
        ).distinguished_open_element()
        right_element = self.overlap(
            source_index,
            target_index,
        ).distinguished_open_element()
        triple = source_chart.distinguished_open(left_element * right_element)
        self._triple_overlaps.append((key, triple))
        return triple

    def transition_on_triple(self, source_index, target_index, third_index):
        r"""Restrict ``phi_source,target`` to the represented triple overlap."""

        source_index = self.normalize_chart_index(source_index)
        target_index = self.normalize_chart_index(target_index)
        third_index = self.normalize_chart_index(third_index)
        self._triple_key(source_index, target_index, third_index)
        key = (source_index, target_index, third_index)
        for cached_key, cached in self._triple_transition_maps:
            if cached_key == key:
                return cached

        source_triple = self.triple_overlap(
            source_index,
            target_index,
            third_index,
        )
        source_overlap = self.overlap(source_index, target_index)
        into_source_overlap = source_overlap.corestriction(source_triple.inclusion())
        transition = self.transition_between(source_index, target_index).forward()
        through_target_overlap = transition * into_source_overlap
        target_chart_map = (
            self.overlap(target_index, source_index).inclusion()
            * through_target_overlap
        )
        target_triple = self.triple_overlap(
            target_index,
            source_index,
            third_index,
        )
        # A transition that does not preserve the triple overlap fails to land
        # in this distinguished open, and the corestriction says so.
        restricted = target_triple.corestriction(target_chart_map)
        self._triple_transition_maps.append((key, restricted))
        return restricted

    def _verify_triple_domains_and_cocycle(self) -> None:
        labels = tuple(self.chart_indices())
        for source_index, target_index, third_index in permutations(labels, 3):
            forward = self.transition_on_triple(
                source_index,
                target_index,
                third_index,
            )
            inverse = self.transition_on_triple(
                target_index,
                source_index,
                third_index,
            )
            source_triple = self.triple_overlap(
                source_index,
                target_index,
                third_index,
            )
            if inverse * forward != source_triple.categorical_identity_morphism():
                raise ValueError(
                    "finite-atlas transitions fail inverse compatibility on a triple overlap"
                )

        for left_index, middle_index, right_index in permutations(labels, 3):
            left_middle = self.transition_on_triple(
                left_index,
                middle_index,
                right_index,
            )
            middle_right = self.transition_on_triple(
                middle_index,
                right_index,
                left_index,
            )
            left_right = self.transition_on_triple(
                left_index,
                right_index,
                middle_index,
            )
            if middle_right * left_middle != left_right:
                raise ValueError("finite-atlas transition maps fail the triple cocycle")

    def _construct_glued_scheme(self) -> None:
        scheme = _OwnedFiniteGluedScheme(self)
        _install_glued_scheme_structure(self, scheme)

    def scheme(self):
        return self._scheme

    def chart_embedding(self, index):
        return self._chart_embeddings[self.normalize_chart_index(index)]

    def chart_images(self):
        return self._chart_images

    def chart_image(self, index):
        return self.chart_images()[self.normalize_chart_index(index)]

    def chart_isomorphisms(self):
        return self._chart_isomorphisms

    def chart_isomorphism(self, index):
        return self.chart_isomorphisms()[self.normalize_chart_index(index)]

    def _repr_(self):
        return f"Finite affine scheme gluing datum indexed by {self.chart_index_set()}"


def _finite_framing(module):
    if not module.is_framed():
        raise TypeError("affine module descent currently requires finitely framed local modules")
    labels = module.module_generating_set()
    if not labels.cardinality().is_finite():
        raise TypeError("affine module descent currently requires finitely framed local modules")
    return labels


def _change_coefficients(element, source, target, ring_map):
    r"""Base-change one framed module element along ``ring_map``."""

    coefficients = module_coefficients(source(element), source)
    return target.linear_combination(
        {
            label: ring_map(coefficient)
            for label, coefficient in coefficients.items()
            if ring_map(coefficient) != target.base_ring().zero()
        }
    )


def _maps_agree_on_framing(left, right) -> bool:
    if left.domain() is not right.domain() or left.codomain() is not right.codomain():
        return False
    labels = _finite_framing(left.domain())
    return all(
        left(left.domain().module_generator(label))
        == right(right.domain().module_generator(label))
        for label in labels
    )


_MODULE_GLUING_DATA_CATEGORIES = {}


class ModuleGluingHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return ModuleGluingHomset


class ModuleGluingData(CategoryPacketMethods, Category):
    r"""Module descent data on one represented distinguished affine cover."""

    @staticmethod
    def __classcall__(category_class, cover):
        key = id(cover)
        cached = _MODULE_GLUING_DATA_CATEGORIES.get(key)
        if cached is not None and cached.cover() is cover:
            return cached
        category = typecall(category_class, cover)
        _MODULE_GLUING_DATA_CATEGORIES[key] = category
        return category

    def __init__(self, cover) -> None:
        self._cover = cover
        Category.__init__(self)

    def cover(self):
        return self._cover

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, ModuleGluingDatum)
            and candidate.cover() is self.cover()
        )

    def _repr_object_names(self):
        return f"module descent data on {self.cover()}"

    _HomCategory = ModuleGluingHomCategoryConstruction


class ModuleGluingDatum(Parent):
    r"""Finitely framed modules with descent isomorphisms on an affine cover."""

    def __init__(self, cover, local_modules, transitions) -> None:
        self._cover = cover
        self._local_modules = tuple(local_modules)
        if cover.atlas().cardinality() != len(self._local_modules):
            raise ValueError("module gluing requires exactly one local module on each affine chart")
        for label, module in zip(cover.atlas(), self._local_modules, strict=True):
            if module.base_ring() is not cover.open(label).coordinate_algebra():
                raise ValueError("each local module must be defined over its chart section ring")
            _finite_framing(module)

        expected = set(combinations(tuple(cover.atlas()), 2))
        self._transitions = {
            _chart_pair(cover, left, right): transition
            for (left, right), transition in dict(transitions).items()
        }
        if set(self._transitions) != expected:
            raise ValueError(
                f"module gluing requires one transition isomorphism for each pair {sorted(expected)}"
            )
        self._restriction_maps = {}
        self._transition_restrictions = {}
        self._inverse_transitions = {}
        self._compatible_sections = None
        self._sheaf = None
        self._verify_pairwise_transitions()
        self._verify_cocycles()
        Parent.__init__(self, category=ModuleGluingData(cover))

    def cover(self):
        return self._cover

    def ringed_space(self):
        return self.cover().ambient_scheme()

    scheme = ringed_space

    def local_modules(self):
        return self._local_modules

    def local_module(self, index):
        return self.local_modules()[self.cover().chart_position(index)]

    def restricted_module(self, chart_index, *intersection_indices):
        return self.cover().restrict_module(
            self.local_module(chart_index),
            chart_index,
            *intersection_indices,
        )

    def transition(self, source_index, target_index):
        r"""Return the represented overlap isomorphism from one chart to another."""

        pair = _chart_pair(self.cover(), source_index, target_index)
        source_index = self.cover().chart_label(source_index)
        target_index = self.cover().chart_label(target_index)
        if pair == (source_index, target_index):
            return self._transitions[pair]
        key = (source_index, target_index)
        cached = self._inverse_transitions.get(key)
        if cached is not None:
            return cached
        original = self._transitions[pair]
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            Isomorphism,
        )

        cached = Isomorphism(original.inverse(), original.forward())
        self._inverse_transitions[key] = cached
        return cached

    def _verify_pairwise_transitions(self) -> None:
        for (left_index, right_index), transition in self._transitions.items():
            if not isinstance(transition, CategoricalIsomorphism):
                raise TypeError("module transition data must be represented categorical isomorphisms")
            source = self.restricted_module(left_index, left_index, right_index)
            target = self.restricted_module(right_index, left_index, right_index)
            forward = transition.forward()
            inverse = transition.inverse()
            if forward.domain() is not source or forward.codomain() is not target:
                raise ValueError("a module transition has the wrong overlap endpoints")
            if inverse.domain() is not target or inverse.codomain() is not source:
                raise ValueError("a module transition inverse has the wrong overlap endpoints")
            for label in _finite_framing(source):
                generator = source.module_generator(label)
                if inverse(forward(generator)) != generator:
                    raise ValueError("the stated module transition is not left-invertible on the overlap")
            for label in _finite_framing(target):
                generator = target.module_generator(label)
                if forward(inverse(generator)) != generator:
                    raise ValueError("the stated module transition is not right-invertible on the overlap")

    def restriction_map(self, chart_index, *intersection_indices):
        r"""Return ``M_i -> Res(M_i|U_I)`` over the chart restriction of scalars."""

        chart_index = int(chart_index)
        target_indices = self.cover().intersection_indices(
            chart_index,
            *intersection_indices,
        )
        return self.restriction_between_intersections(
            chart_index,
            (chart_index,),
            target_indices,
        )

    def restriction_between_intersections(
        self,
        chart_index,
        source_indices,
        target_indices,
    ):
        r"""Return ``M_i|U_I -> Res(M_i|U_J)`` for ``U_J subseteq U_I``."""

        chart_index = int(chart_index)
        source_indices = self.cover().intersection_indices(
            chart_index,
            *tuple(source_indices),
        )
        target_indices = self.cover().intersection_indices(
            chart_index,
            *tuple(target_indices),
        )
        if not set(source_indices).issubset(target_indices):
            raise ValueError("module restriction requires the target intersection to refine the source")
        key = (chart_index, source_indices, target_indices)
        cached = self._restriction_maps.get(key)
        if cached is not None:
            return cached
        source = self.restricted_module(chart_index, *source_indices)
        target = self.restricted_module(chart_index, *target_indices)
        if target is source:
            cached = module_homset(source, source).identity()
            self._restriction_maps[key] = cached
            return cached
        source_open = self.cover().intersection(*source_indices)
        target_open = self.cover().intersection(*target_indices)
        ring_map = self.scheme().structure_sheaf().restriction_map(source_open, target_open)
        restricted_target = restrict_scalars(target, ring_map)
        cached = module_homset(source, restricted_target)(
            lambda label: restricted_target.wrap(target.module_generator(label))
        )
        self._restriction_maps[key] = cached
        return cached

    def restrict_section(self, chart_index, section, *intersection_indices):
        r"""Restrict one local section to the selected cover intersection."""

        restriction = self.restriction_map(chart_index, *intersection_indices)
        image = restriction(self.local_module(chart_index)(section))
        underlying = getattr(image, "underlying_element", None)
        return image if underlying is None else underlying()

    def restrict_section_between_intersections(
        self,
        chart_index,
        section,
        source_indices,
        target_indices,
    ):
        r"""Restrict a section already living on one represented cover intersection."""

        restriction = self.restriction_between_intersections(
            chart_index,
            source_indices,
            target_indices,
        )
        source = self.restricted_module(chart_index, *tuple(source_indices))
        image = restriction(source(section))
        underlying = getattr(image, "underlying_element", None)
        return image if underlying is None else underlying()

    def transition_on_intersection(
        self,
        source_index,
        target_index,
        *intersection_indices,
    ):
        r"""Restrict a pairwise transition to a finer represented intersection."""

        source_index = int(source_index)
        target_index = int(target_index)
        indices = self.cover().intersection_indices(
            source_index,
            target_index,
            *intersection_indices,
        )
        key = (source_index, target_index, indices)
        cached = self._transition_restrictions.get(key)
        if cached is not None:
            return cached
        pair = tuple(sorted((source_index, target_index)))
        transition = self.transition(source_index, target_index).forward()
        if indices == pair:
            self._transition_restrictions[key] = transition
            return transition

        pair_open = self.cover().intersection(*pair)
        target_open = self.cover().intersection(*indices)
        ring_map = self.scheme().structure_sheaf().restriction_map(pair_open, target_open)
        pair_source = self.restricted_module(source_index, *pair)
        pair_target = self.restricted_module(target_index, *pair)
        source = self.restricted_module(source_index, *indices)
        target = self.restricted_module(target_index, *indices)

        def image(label):
            pair_image = transition(pair_source.module_generator(label))
            return _change_coefficients(pair_image, pair_target, target, ring_map)

        cached = module_homset(source, target)(image)
        self._transition_restrictions[key] = cached
        return cached

    def _verify_cocycles(self) -> None:
        for left_index, middle_index, right_index in combinations(
            range(len(self.local_modules())),
            3,
        ):
            indices = (left_index, middle_index, right_index)
            left_middle = self.transition_on_intersection(
                left_index,
                middle_index,
                *indices,
            )
            middle_right = self.transition_on_intersection(
                middle_index,
                right_index,
                *indices,
            )
            left_right = self.transition_on_intersection(
                left_index,
                right_index,
                *indices,
            )
            composite = middle_right * left_middle
            if not _maps_agree_on_framing(composite, left_right):
                raise ValueError("module transition isomorphisms fail the cocycle condition on a triple overlap")

    def compatible_sections(self):
        r"""Return the ``A``-module of local tuples agreeing under every transition."""

        if self._compatible_sections is None:
            self._compatible_sections = CompatibleLocalSectionsModule(self)
        return self._compatible_sections

    def sheaf(self):
        if self._sheaf is None:
            self._sheaf = GluedModuleSheaf(self)
        return self._sheaf

    def Mor(self, target):
        r"""Return the represented Hom category of descent morphisms to ``target``."""

        return self.category().Mor(self, target)

    def _repr_(self):
        return f"Module gluing datum on {self.cover()}"


class ModuleGluingMorphism(Morphism):
    r"""A morphism between module descent data on one represented affine cover."""

    def __init__(self, parent, local_maps) -> None:
        Morphism.__init__(self, parent)
        local_maps = tuple(local_maps)
        if len(local_maps) != len(self.domain().local_modules()):
            raise ValueError("a module descent morphism requires one local map on each affine chart")

        self._local_maps = tuple(
            module_homset(
                self.domain().local_module(index),
                self.codomain().local_module(index),
            )(local_map)
            for index, local_map in enumerate(local_maps)
        )
        self._restricted_local_maps = {}
        self._global_sections_map = None
        self._verify_overlap_compatibility()

    def cover(self):
        return self.domain().cover()

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[int(index)]

    def restricted_local_map(self, chart_index, *intersection_indices):
        r"""Restrict one chart map to the represented cover intersection."""

        chart_index = int(chart_index)
        indices = self.cover().intersection_indices(
            chart_index,
            *intersection_indices,
        )
        key = (chart_index, indices)
        cached = self._restricted_local_maps.get(key)
        if cached is not None:
            return cached

        local_map = self.local_map(chart_index)
        source = self.domain().restricted_module(chart_index, *indices)
        target = self.codomain().restricted_module(chart_index, *indices)
        if source is self.domain().local_module(chart_index):
            self._restricted_local_maps[key] = local_map
            return local_map

        source_open = self.cover().open(chart_index)
        target_open = self.cover().intersection(*indices)
        ring_map = self.domain().scheme().structure_sheaf().restriction_map(
            source_open,
            target_open,
        )
        local_source = self.domain().local_module(chart_index)
        local_target = self.codomain().local_module(chart_index)

        def image(label):
            local_image = local_map(local_source.module_generator(label))
            return _change_coefficients(local_image, local_target, target, ring_map)

        cached = module_homset(source, target)(image)
        self._restricted_local_maps[key] = cached
        return cached

    def _verify_overlap_compatibility(self) -> None:
        for left_index, right_index in combinations(
            range(len(self.domain().local_modules())),
            2,
        ):
            source_transition = self.domain().transition(left_index, right_index).forward()
            target_transition = self.codomain().transition(left_index, right_index).forward()
            left_restriction = self.restricted_local_map(
                left_index,
                left_index,
                right_index,
            )
            right_restriction = self.restricted_local_map(
                right_index,
                left_index,
                right_index,
            )
            via_left = target_transition * left_restriction
            via_right = right_restriction * source_transition
            if not _maps_agree_on_framing(via_left, via_right):
                raise ValueError(
                    "module descent morphism is incompatible with transition maps on an overlap"
                )

    def global_sections_map(self):
        r"""Return the induced ambient-ring linear map on compatible global sections."""

        if self._global_sections_map is None:
            source_sections = self.domain().compatible_sections()
            target_sections = self.codomain().compatible_sections()

            def image(section):
                section = source_sections(section)
                return target_sections(
                    tuple(
                        self.local_map(index)(section.component(index))
                        for index in range(len(self.local_maps()))
                    )
                )

            self._global_sections_map = module_homset(
                source_sections,
                target_sections,
            ).elementwise(
                image,
                verify_linearity=False,
            )
        return self._global_sections_map

    def then(self, other):
        r"""Return ``other after self``."""

        if other.domain() is not self.codomain():
            raise ValueError("the first descent-morphism target must equal the second source")
        return other * self

    def __mul__(self, other):
        if not isinstance(other, ModuleGluingMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            tuple(
                self.local_map(index) * other.local_map(index)
                for index in range(len(self.local_maps()))
            )
        )

    def _repr_(self):
        return f"Module descent morphism from {self.domain()} to {self.codomain()}"


class ModuleGluingHomset(CategoricalHomset):
    r"""The fixed Hom category between two module descent data on one cover."""

    Element = ModuleGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.cover() is not codomain.cover():
            raise ValueError("a module descent Hom requires one common affine cover")
        CategoricalHomset.__init__(self, family, domain, codomain)

    def _element_constructor_(self, local_maps):
        if isinstance(local_maps, ModuleGluingMorphism):
            if (
                local_maps.domain() is not self.domain()
                or local_maps.codomain() is not self.codomain()
            ):
                raise ValueError("the module descent morphism has the wrong endpoints")
            if local_maps.parent() is self:
                return local_maps
            local_maps = local_maps.local_maps()
        return self.element_class(self, local_maps)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a descent endomorphism Hom")
        return self(
            tuple(
                module_homset(module, module).identity()
                for module in self.domain().local_modules()
            )
        )


_ALGEBRA_GLUING_DATA_CATEGORIES = {}


def _algebra_maps_agree_on_generators(left, right) -> bool:
    if left.domain() is not right.domain() or left.codomain() is not right.codomain():
        return False
    source = left.domain()
    labels = source.algebra_generating_set()
    if not labels.cardinality().is_finite():
        raise TypeError("affine algebra descent currently requires finite algebra framings")
    return all(
        left(source.algebra_generator(label)) == right(source.algebra_generator(label))
        for label in labels
    )


def _exact_algebra_map(source, target, morphism):
    homset = source.Mor(target)
    if (
        isinstance(morphism, Morphism)
        and morphism.domain() is source
        and morphism.codomain() is target
        and morphism.parent() is homset
    ):
        return morphism
    return homset(morphism)


class AlgebraGluingHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return AlgebraGluingHomset


class AlgebraGluingData(CategoryPacketMethods, Category):
    r"""Finite algebra descent data on one represented distinguished affine cover."""

    @staticmethod
    def __classcall__(category_class, cover):
        key = id(cover)
        cached = _ALGEBRA_GLUING_DATA_CATEGORIES.get(key)
        if cached is not None and cached.cover() is cover:
            return cached
        category = typecall(category_class, cover)
        _ALGEBRA_GLUING_DATA_CATEGORIES[key] = category
        return category

    def __init__(self, cover) -> None:
        self._cover = cover
        Category.__init__(self)

    def cover(self):
        return self._cover

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, AlgebraGluingDatum)
            and candidate.cover() is self.cover()
        )

    def _repr_object_names(self):
        return f"algebra descent data on {self.cover()}"

    _HomCategory = AlgebraGluingHomCategoryConstruction


class AlgebraGluingDatum(Parent):
    r"""Finite local algebras with algebra isomorphisms satisfying descent."""

    def __init__(self, cover, local_algebras, transitions) -> None:
        self._cover = cover
        self._local_algebras = tuple(local_algebras)
        if cover.atlas().cardinality() != len(self._local_algebras):
            raise ValueError("algebra gluing requires exactly one local algebra on each affine chart")
        for label, algebra in zip(cover.atlas(), self._local_algebras, strict=True):
            ring = cover.open(label).coordinate_algebra()
            if algebra.base_ring() is not ring:
                raise ValueError("each local algebra must be defined over its chart section ring")
            if algebra not in AlgebrasWithChosenFinitePresentation(ring):
                raise TypeError(
                    "affine algebra descent currently requires local algebras with chosen finite presentations"
                )
            _finite_framing(algebra)

        expected = set(combinations(tuple(cover.atlas()), 2))
        self._transitions = {
            _chart_pair(cover, left, right): transition
            for (left, right), transition in dict(transitions).items()
        }
        if set(self._transitions) != expected:
            raise ValueError(
                f"algebra gluing requires one transition isomorphism for each pair {sorted(expected)}"
            )
        self._inverse_transitions = {}
        self._restriction_maps = {}
        self._transition_restrictions = {}
        self._compatible_sections = None
        self._sheaf = None
        self._verify_pairwise_transitions()
        self._verify_cocycles()
        self._module_gluing_datum = self._build_underlying_module_datum()
        Parent.__init__(self, category=AlgebraGluingData(cover))

    def cover(self):
        return self._cover

    def ringed_space(self):
        return self.cover().ambient_scheme()

    scheme = ringed_space

    def local_algebras(self):
        return self._local_algebras

    def local_algebra(self, index):
        return self.local_algebras()[self.cover().chart_position(index)]

    def restricted_algebra(self, chart_index, *intersection_indices):
        chart_index = int(chart_index)
        restricted = self.cover().restrict_algebra(
            self.local_algebra(chart_index),
            chart_index,
            *intersection_indices,
        )
        target = self.cover().intersection(
            chart_index,
            *intersection_indices,
        ).coordinate_algebra()
        if restricted not in Algebras(target):
            raise TypeError("algebra scalar extension did not preserve the algebra structure")
        if restricted not in AlgebrasWithChosenFinitePresentation(target):
            raise TypeError("algebra scalar extension did not preserve the chosen finite presentation")
        _finite_framing(restricted)
        return restricted

    def transition(self, source_index, target_index):
        source_index = int(source_index)
        target_index = int(target_index)
        if source_index == target_index:
            raise ValueError("an algebra transition isomorphism is requested between two distinct charts")
        if source_index < target_index:
            return self._transitions[source_index, target_index]
        key = (source_index, target_index)
        cached = self._inverse_transitions.get(key)
        if cached is not None:
            return cached
        original = self._transitions[target_index, source_index]
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            Isomorphism,
        )

        cached = Isomorphism(original.inverse(), original.forward())
        self._inverse_transitions[key] = cached
        return cached

    def _verify_pairwise_transitions(self) -> None:
        for (left_index, right_index), transition in self._transitions.items():
            if not isinstance(transition, CategoricalIsomorphism):
                raise TypeError("algebra transition data must be represented categorical isomorphisms")
            source = self.restricted_algebra(left_index, left_index, right_index)
            target = self.restricted_algebra(right_index, left_index, right_index)
            forward = transition.forward()
            inverse = transition.inverse()
            if forward.domain() is not source or forward.codomain() is not target:
                raise ValueError("an algebra transition has the wrong overlap endpoints")
            if inverse.domain() is not target or inverse.codomain() is not source:
                raise ValueError("an algebra transition inverse has the wrong overlap endpoints")
            if forward.parent() is not source.Mor(target):
                raise TypeError("an algebra transition forward map must lie in the overlap algebra Hom")
            if inverse.parent() is not target.Mor(source):
                raise TypeError("an algebra transition inverse map must lie in the overlap algebra Hom")
            if not _algebra_maps_agree_on_generators(inverse * forward, source.Mor(source).identity()):
                raise ValueError("the stated algebra transition is not left-invertible on the overlap")
            if not _algebra_maps_agree_on_generators(forward * inverse, target.Mor(target).identity()):
                raise ValueError("the stated algebra transition is not right-invertible on the overlap")

    def restriction_between_intersections(
        self,
        chart_index,
        source_indices,
        target_indices,
    ):
        r"""Return the algebra restriction to a finer represented intersection."""

        chart_index = int(chart_index)
        source_indices = self.cover().intersection_indices(
            chart_index,
            *tuple(source_indices),
        )
        target_indices = self.cover().intersection_indices(
            chart_index,
            *tuple(target_indices),
        )
        if not set(source_indices).issubset(target_indices):
            raise ValueError("algebra restriction requires the target intersection to refine the source")
        key = (chart_index, source_indices, target_indices)
        cached = self._restriction_maps.get(key)
        if cached is not None:
            return cached
        source = self.restricted_algebra(chart_index, *source_indices)
        target = self.restricted_algebra(chart_index, *target_indices)
        if target is source:
            cached = source.Mor(source).identity()
            self._restriction_maps[key] = cached
            return cached
        source_open = self.cover().intersection(*source_indices)
        target_open = self.cover().intersection(*target_indices)
        ring_map = self.scheme().structure_sheaf().restriction_map(source_open, target_open)
        restricted_target = restrict_algebra_scalars(target, ring_map)
        cached = source.Mor(restricted_target)(
            lambda label: restricted_target(target.algebra_generator(label))
        )
        self._restriction_maps[key] = cached
        return cached

    def restriction_map(self, chart_index, *intersection_indices):
        chart_index = int(chart_index)
        target_indices = self.cover().intersection_indices(
            chart_index,
            *intersection_indices,
        )
        return self.restriction_between_intersections(
            chart_index,
            (chart_index,),
            target_indices,
        )

    def restrict_section_between_intersections(
        self,
        chart_index,
        section,
        source_indices,
        target_indices,
    ):
        source = self.restricted_algebra(chart_index, *tuple(source_indices))
        target = self.restricted_algebra(chart_index, *tuple(target_indices))
        image = self.restriction_between_intersections(
            chart_index,
            source_indices,
            target_indices,
        )(source(section))
        return target(image)

    def transition_on_intersection(
        self,
        source_index,
        target_index,
        *intersection_indices,
    ):
        r"""Restrict an algebra transition to a finer represented intersection."""

        source_index = int(source_index)
        target_index = int(target_index)
        indices = self.cover().intersection_indices(
            source_index,
            target_index,
            *intersection_indices,
        )
        key = (source_index, target_index, indices)
        cached = self._transition_restrictions.get(key)
        if cached is not None:
            return cached
        pair = tuple(sorted((source_index, target_index)))
        transition = self.transition(source_index, target_index).forward()
        if indices == pair:
            self._transition_restrictions[key] = transition
            return transition

        pair_source = self.restricted_algebra(source_index, *pair)
        source = self.restricted_algebra(source_index, *indices)
        target = self.restricted_algebra(target_index, *indices)
        target_restriction = self.restriction_between_intersections(
            target_index,
            pair,
            indices,
        )

        def image(label):
            pair_image = transition(pair_source.algebra_generator(label))
            return target(target_restriction(pair_image))

        cached = source.Mor(target)(image)
        self._transition_restrictions[key] = cached
        return cached

    def _verify_cocycles(self) -> None:
        for left_index, middle_index, right_index in combinations(
            range(len(self.local_algebras())),
            3,
        ):
            indices = (left_index, middle_index, right_index)
            left_middle = self.transition_on_intersection(
                left_index,
                middle_index,
                *indices,
            )
            middle_right = self.transition_on_intersection(
                middle_index,
                right_index,
                *indices,
            )
            left_right = self.transition_on_intersection(
                left_index,
                right_index,
                *indices,
            )
            if not _algebra_maps_agree_on_generators(
                middle_right * left_middle,
                left_right,
            ):
                raise ValueError("algebra transition isomorphisms fail the cocycle condition on a triple overlap")

    def _build_underlying_module_datum(self):
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import (
            Isomorphism,
        )

        transitions = {}
        for (left_index, right_index), transition in self._transitions.items():
            ring = self.cover().overlap(left_index, right_index).coordinate_algebra()
            forget = algebra_underlying_module_functor(ring)
            transitions[left_index, right_index] = Isomorphism(
                forget(transition.forward()),
                forget(transition.inverse()),
            )
        return ModuleGluingDatum(
            self.cover(),
            self.local_algebras(),
            transitions,
        )

    def underlying_module_datum(self):
        return self._module_gluing_datum

    def compatible_sections(self):
        if self._compatible_sections is None:
            self._compatible_sections = CompatibleLocalAlgebraSections(self)
        return self._compatible_sections

    def sheaf(self):
        if self._sheaf is None:
            self._sheaf = GluedAlgebraSheaf(self)
        return self._sheaf

    def Mor(self, target):
        return self.category().Mor(self, target)

    def _repr_(self):
        return f"Algebra gluing datum on {self.cover()}"


class AlgebraGluingMorphism(Morphism):
    r"""A compatible family of local algebra morphisms between descent data."""

    def __init__(self, parent, local_maps) -> None:
        Morphism.__init__(self, parent)
        local_maps = tuple(local_maps)
        if len(local_maps) != len(self.domain().local_algebras()):
            raise ValueError("an algebra descent morphism requires one local map on each affine chart")
        self._local_maps = tuple(
            _exact_algebra_map(
                self.domain().local_algebra(index),
                self.codomain().local_algebra(index),
                local_map,
            )
            for index, local_map in enumerate(local_maps)
        )
        module_maps = tuple(
            algebra_underlying_module_functor(
                self.cover().open(index).coordinate_algebra()
            )(local_map)
            for index, local_map in enumerate(self._local_maps)
        )
        self._underlying_module_morphism = self.domain().underlying_module_datum().Mor(
            self.codomain().underlying_module_datum()
        )(module_maps)
        self._global_sections_map = None

    def cover(self):
        return self.domain().cover()

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[int(index)]

    def underlying_module_morphism(self):
        return self._underlying_module_morphism

    def global_sections_map(self):
        if self._global_sections_map is None:
            source = self.domain().compatible_sections()
            target = self.codomain().compatible_sections()

            def image(section):
                section = source(section)
                return target(
                    tuple(
                        self.local_map(index)(section.component(index))
                        for index in range(len(self.local_maps()))
                    )
                )

            set_map = SetMorphism(Sets().Mor(source, target), image)
            self._global_sections_map = source.Mor(target)(set_map)
        return self._global_sections_map

    def then(self, other):
        if other.domain() is not self.codomain():
            raise ValueError("the first algebra descent-morphism target must equal the second source")
        return other * self

    def __mul__(self, other):
        if not isinstance(other, AlgebraGluingMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            tuple(
                self.local_map(index) * other.local_map(index)
                for index in range(len(self.local_maps()))
            )
        )

    def _repr_(self):
        return f"Algebra descent morphism from {self.domain()} to {self.codomain()}"


class AlgebraGluingHomset(CategoricalHomset):
    Element = AlgebraGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.cover() is not codomain.cover():
            raise ValueError("an algebra descent Hom requires one common affine cover")
        CategoricalHomset.__init__(self, family, domain, codomain)

    def _element_constructor_(self, local_maps):
        if isinstance(local_maps, AlgebraGluingMorphism):
            if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                raise ValueError("the algebra descent morphism has the wrong endpoints")
            if local_maps.parent() is self:
                return local_maps
            local_maps = local_maps.local_maps()
        return self.element_class(self, local_maps)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an algebra descent endomorphism Hom")
        return self(
            tuple(
                algebra.Mor(algebra).identity()
                for algebra in self.domain().local_algebras()
            )
        )


class CompatibleLocalSectionElement(ModuleElement):
    def __init__(self, parent, components) -> None:
        ModuleElement.__init__(self, parent)
        self._components = tuple(components)

    def components(self):
        return self._components

    def component(self, index):
        return self.components()[int(index)]

    def _add_(self, other):
        return self.parent()(
            tuple(
                left + right
                for left, right in zip(self.components(), other.components(), strict=True)
            )
        )

    def _neg_(self):
        return self.parent()(tuple(-component for component in self.components()))

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _acted_upon_(self, actor, self_on_left):
        try:
            scalar = self.parent().base_ring()(actor)
        except (TypeError, ValueError):
            return None
        return self.parent().scalar_multiple(scalar, self)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, CompatibleLocalSectionElement)
            and other.parent() is self.parent()
            and all(
                left == right
                for left, right in zip(self.components(), other.components(), strict=True)
            )
        )
        return equal if op == op_EQ else not equal

    def _repr_(self):
        return f"compatible local sections {self.components()}"


class CompatibleLocalSectionsModule(Parent):
    r"""The equalizer module of local sections satisfying the descent equations."""

    Element = CompatibleLocalSectionElement

    def __init__(self, gluing_datum) -> None:
        self._gluing_datum = gluing_datum
        self._preamble_base_ring = gluing_datum.scheme().coordinate_algebra()
        Parent.__init__(self, category=Modules(self._preamble_base_ring))

    def gluing_datum(self):
        return self._gluing_datum

    def base_ring(self):
        return self._preamble_base_ring

    def base(self):
        return self.base_ring()

    def _element_constructor_(self, value):
        if isinstance(value, CompatibleLocalSectionElement) and value.parent() is self:
            return value
        components = tuple(value)
        datum = self.gluing_datum()
        if len(components) != len(datum.local_modules()):
            raise ValueError("a compatible section tuple needs one component on each affine chart")
        components = tuple(
            module(component)
            for module, component in zip(datum.local_modules(), components, strict=True)
        )
        for left_index, right_index in combinations(range(len(components)), 2):
            left = datum.restrict_section(
                left_index,
                components[left_index],
                left_index,
                right_index,
            )
            right = datum.restrict_section(
                right_index,
                components[right_index],
                left_index,
                right_index,
            )
            transition = datum.transition(left_index, right_index).forward()
            if transition(left) != right:
                raise ValueError("the local sections do not agree under the overlap transition")
        return self.element_class(self, components)

    def __call__(self, value):
        return self._element_constructor_(value)

    def __contains__(self, value) -> bool:
        return isinstance(value, CompatibleLocalSectionElement) and value.parent() is self

    def zero(self):
        return self(tuple(module.zero() for module in self.gluing_datum().local_modules()))

    def scalar_multiple(self, scalar, section):
        datum = self.gluing_datum()
        scalar = self.base_ring()(scalar)
        section = self(section)
        structure_sheaf = datum.scheme().structure_sheaf()
        components = []
        for index, module in enumerate(datum.local_modules()):
            local_scalar = structure_sheaf.restriction_map(
                datum.scheme(),
                datum.cover().open(index),
            )(scalar)
            components.append(module.scalar_multiple(local_scalar, section.component(index)))
        return self(tuple(components))

    def an_element(self):
        return self.zero()

    def _repr_(self):
        return f"Compatible local sections of {self.gluing_datum()}"


class CompatibleLocalAlgebraSectionElement(CompatibleLocalSectionElement):
    def _mul_(self, other):
        return self.parent().multiply(self, other)


class CompatibleLocalAlgebraSections(CompatibleLocalSectionsModule):
    r"""The ambient-ring algebra of compatible local algebra sections.

    The equalizer module need not carry a selected finite framing.  Its unit
    and multiplication are nevertheless exact componentwise operations; a
    represented tensor-product multiplication morphism is only available when
    the module layer can materialize that tensor product.
    """

    Element = CompatibleLocalAlgebraSectionElement

    def __init__(self, gluing_datum) -> None:
        self._algebra_gluing_datum = gluing_datum
        self._gluing_datum = gluing_datum.underlying_module_datum()
        self._preamble_base_ring = gluing_datum.scheme().coordinate_algebra()
        self._preamble_algebra_base_ring = self._preamble_base_ring
        self._preamble_is_commutative = all(
            algebra in CommutativeAlgebras(algebra.base_ring())
            for algebra in gluing_datum.local_algebras()
        )
        category = (
            CommutativeAlgebras(self._preamble_base_ring)
            if self._preamble_is_commutative
            else Algebras(self._preamble_base_ring)
        )
        Parent.__init__(self, category=category)

    def algebra_gluing_datum(self):
        return self._algebra_gluing_datum

    def is_commutative(self) -> bool:
        return self._preamble_is_commutative

    def one(self):
        return self(
            tuple(
                algebra.one()
                for algebra in self.algebra_gluing_datum().local_algebras()
            )
        )

    def multiply(self, left, right):
        left = self(left)
        right = self(right)
        return self(
            tuple(
                left_component * right_component
                for left_component, right_component in zip(
                    left.components(),
                    right.components(),
                    strict=True,
                )
            )
        )

    def _repr_(self):
        return f"Compatible local algebra sections of {self.algebra_gluing_datum()}"


class GluedModuleSheaf(SageObject):
    r"""The module sheaf represented by one finite affine descent datum."""

    def __init__(self, gluing_datum) -> None:
        self._gluing_datum = gluing_datum

    def gluing_datum(self):
        return self._gluing_datum

    def ringed_space(self):
        return self.gluing_datum().scheme()

    scheme = ringed_space

    def cover(self):
        return self.gluing_datum().cover()

    def sections_on_chart(self, index):
        return self.gluing_datum().local_module(index)

    def sections_on_intersection(self, chart_index, *intersection_indices):
        return self.gluing_datum().restricted_module(
            chart_index,
            *intersection_indices,
        )

    def restriction_map(self, chart_index, *intersection_indices):
        return self.gluing_datum().restriction_map(chart_index, *intersection_indices)

    def restriction_between_intersections(
        self,
        chart_index,
        source_indices,
        target_indices,
    ):
        return self.gluing_datum().restriction_between_intersections(
            chart_index,
            source_indices,
            target_indices,
        )

    def transition(self, source_index, target_index, *intersection_indices):
        return self.gluing_datum().transition_on_intersection(
            source_index,
            target_index,
            *intersection_indices,
        )

    def global_sections(self):
        return self.gluing_datum().compatible_sections()

    sections = global_sections

    def _repr_(self):
        return f"Glued module sheaf on {self.scheme()} from {self.cover()}"


class GluedAlgebraSheaf(SageObject):
    r"""The algebra sheaf represented by finite affine algebra descent data."""

    def __init__(self, gluing_datum) -> None:
        self._gluing_datum = gluing_datum

    def gluing_datum(self):
        return self._gluing_datum

    def ringed_space(self):
        return self.gluing_datum().scheme()

    scheme = ringed_space

    def cover(self):
        return self.gluing_datum().cover()

    def sections_on_chart(self, index):
        return self.gluing_datum().local_algebra(index)

    def sections_on_intersection(self, chart_index, *intersection_indices):
        return self.gluing_datum().restricted_algebra(
            chart_index,
            *intersection_indices,
        )

    def restriction_map(self, chart_index, *intersection_indices):
        return self.gluing_datum().restriction_map(chart_index, *intersection_indices)

    def restriction_between_intersections(
        self,
        chart_index,
        source_indices,
        target_indices,
    ):
        return self.gluing_datum().restriction_between_intersections(
            chart_index,
            source_indices,
            target_indices,
        )

    def transition(self, source_index, target_index, *intersection_indices):
        return self.gluing_datum().transition_on_intersection(
            source_index,
            target_index,
            *intersection_indices,
        )

    def global_sections(self):
        return self.gluing_datum().compatible_sections()

    sections = global_sections

    def underlying_module_sheaf(self):
        return self.gluing_datum().underlying_module_datum().sheaf()

    def _repr_(self):
        return f"Glued algebra sheaf on {self.scheme()} from {self.cover()}"


__all__ = [
    "AlgebraGluingData",
    "AlgebraGluingDatum",
    "AlgebraGluingHomset",
    "AlgebraGluingMorphism",
    "CompatibleLocalAlgebraSections",
    "CompatibleLocalSectionsModule",
    "GluedAlgebraSheaf",
    "GluedModuleSheaf",
    "ModuleGluingData",
    "ModuleGluingDatum",
    "ModuleGluingHomset",
    "ModuleGluingMorphism",
]
