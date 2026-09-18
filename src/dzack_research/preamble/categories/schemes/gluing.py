r"""Descent and gluing for represented schemes, modules, and algebras."""

from collections.abc import Mapping
from itertools import combinations, permutations

from sage.categories.category import Category
from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.abstract_categories.presheaves import (
    CoveringFamilyHomCategoryConstruction,
    CoveringFamilyHomset,
    CoveringFamilyMorphism,
    DescentData,
    DescentDataOnCover,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    SelectedLimitConstruction,
    _parallel_pair_diagram,
)
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    FramedAlgebras,
    _algebra_structure_view,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    Modules,
)
from dzack_research.preamble.categories.modules.base_change import _base_change_element
from dzack_research.preamble.categories.modules.fibered_modules import (
    ModulesOverCommutativeRings,
    SemilinearModuleMorphism,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
)
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    AlgebraSheaves,
    DistinguishedAffineCovers,
    QuasiCoherentSheaves,
    SheafObjects,
    ZariskiCoveringFamilies,
    zariski_coverage,
)
from dzack_research.preamble.categories.schemes.schemes import (
    OpenImmersions,
    SchemeMorCategory,
    SchemeMorphism,
    Schemes,
    _affine_scheme,
    _affine_structure_morphism_to_base,
    _scheme_composition_hom,
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
from dzack_research.preamble.owned_category import _object_of


def _chart_pair(cover, left_index, right_index):
    r"""The two chart labels in the atlas order, which is how descent data is keyed."""

    labels = (cover.chart_label(left_index), cover.chart_label(right_index))
    if labels[0] == labels[1]:
        raise ValueError("descent data is keyed by two distinct charts")
    return tuple(sorted(labels, key=cover.atlas().ranking_map()))


def _family_on_finite_ordered_set(index_set, values, *, name, noun):
    r"""Read finite labelled data as an indexed family on ``index_set``.

    This is the literal ingress of the gluing constructors, and the one place
    in this module that reads a Python container.  An indexed family is read
    at its labels, a mapping at its keys and any other finite collection at the
    positions of ``index_set``.  With ``index_set`` omitted the labels are the
    family's own, the mapping's keys, or the positions of the collection.
    """
    if isinstance(values, IndexedFamily):
        labels = finite_ordered_set(values.index_set()) if index_set is None else index_set
        family = finite_indexed_family(labels, values.__getitem__, name=name)
        supplied = values
    elif isinstance(values, Mapping):
        labels = finite_ordered_set(tuple(values)) if index_set is None else index_set
        family = finite_indexed_family(labels, values.__getitem__, name=name)
        supplied = finite_family(tuple(values))
    else:
        supplied = finite_family(values)
        labels = (
            finite_ordered_set(range(int(supplied.cardinality().finite_value())))
            if index_set is None
            else index_set
        )
        family = finite_indexed_family(
            labels,
            lambda label: supplied[int(labels.ranking_map()(label))],
            name=name,
        )
    assert supplied.cardinality().is_finite(), f"{noun} is finite data"
    if supplied.cardinality() != family.cardinality():
        raise ValueError(f"{noun} has the wrong number of entries")
    return family


def _lands_in_distinguished_open(morphism, distinguished_open):
    r"""Whether ``g: T -> U`` of affine schemes factors through ``D(f) <= U``.

    It does exactly when ``g^#(f)`` is a unit of ``O(T)``: that is the
    universal property of ``O(D(f)) = O(U)[1/f]`` (Stacks, Tag 01HR), and it
    is the hypothesis under which ``corestriction`` constructs the factor.
    """
    return distinguished_open.contains_image_of(morphism)


def _scheme_core_hom(isomorphism):
    r"""``Core(Sch_R)(U, V)``, the isomorphisms of ``R``-schemes an overlap transition ``U -> V`` lies in."""
    domain = isomorphism.domain()
    return Schemes(domain.scheme_base_ring()).Core().Mor(domain, isomorphism.codomain())


def _algebra_homset(source, target):
    r"""Return the algebra Hom selected by the scalar algebra structure.

    An engine-backed algebra is also an owned ring and often a module, so its
    bare parent-level ``Mor`` is not enough to identify which of those several
    mathematical Hom theories is intended.  Algebra descent always means
    morphisms of associative unital algebras over the declared scalar ring.
    """
    base = source.algebra_base_ring()
    if target.algebra_base_ring() is not base:
        raise ValueError("an algebra Hom requires one common scalar base ring")
    category = Algebras(base).Associative().Unital()
    if source not in category or target not in category:
        raise TypeError("algebra descent maps require associative unital algebra endpoints")
    return category.Mor(source, target)


def _finite_chart_family(charts):
    r"""Return one nonempty finite ordered family of chart candidates."""
    family = _family_on_finite_ordered_set(
        None,
        charts,
        name="Affine charts of a finite scheme gluing",
        noun="the affine charts of a finite scheme gluing",
    )
    if int(family.cardinality().finite_value()) == 0:
        raise ValueError("scheme gluing requires at least one affine chart")
    return family


class _GluedSchemeOpenInclusion(SchemeMorphism):
    r"""The chosen inclusion of one chart image into the glued scheme."""

    def __init__(self, parent, gluing_datum, chart_index) -> None:
        super().__init__(None, homset=parent)
        self._gluing_datum = gluing_datum
        self._chart_index = gluing_datum.normalize_chart_index(chart_index)

    def gluing_datum(self):
        return self._gluing_datum

    def chart_index(self):
        return self._chart_index

    def _in_homset(self, homset):
        return _GluedSchemeOpenInclusion(homset, self.gluing_datum(), self.chart_index())

    def is_open_immersion(self) -> bool:
        return True

    def __mul__(self, other):
        datum = self.gluing_datum()
        chart = datum.chart_isomorphism(self.chart_index())
        return datum.chart_embedding(self.chart_index()) * (chart.inverse() * other)

    def _postcompose_with(self, after):
        chart = self.gluing_datum().chart_isomorphism(self.chart_index())
        return after.local_map(self.chart_index()) * chart.inverse()

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
        super().__init__(None, homset=parent)
        self._gluing_datum = gluing_datum
        self._chart_index = gluing_datum.normalize_chart_index(chart_index)
        self._open_image = open_image
        self._chart_isomorphism = chart_isomorphism

    def gluing_datum(self):
        return self._gluing_datum

    def chart_index(self):
        return self._chart_index

    def open_image(self):
        return self._open_image

    def chart_isomorphism(self):
        return self._chart_isomorphism

    def open_inclusion(self):
        return self.open_image().inclusion()

    def _in_homset(self, homset):
        return _GluedSchemeChartEmbedding(
            homset, self.gluing_datum(), self.chart_index(),
            self.open_image(), self.chart_isomorphism(),
        )

    def is_open_immersion(self) -> bool:
        r"""True: ``e_i`` is the chart isomorphism onto its open image followed by that image's inclusion."""
        return True

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        chart_map = other
        return _GluedSchemeChartMap(
            _scheme_composition_hom(self, other),
            self.gluing_datum().chart_embedding(self.chart_index()),
            chart_map,
        )

    def _postcompose_with(self, after):
        r"""``after o e_i`` is the local map of ``after`` on chart ``i``."""
        if after.domain() is not self.codomain():
            return NotImplemented
        return after.local_map(self.chart_index())

    def __eq__(self, other) -> bool:
        if isinstance(other, _GluedSchemeChartMap):
            return (
                other.codomain() is self.codomain()
                and other.gluing_datum() is self.gluing_datum()
                and other.chart_index() == self.chart_index()
                and other.chart_map()
                == self.domain().categorical_identity_morphism()
            )
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


class _GluedSchemeChartMap(SchemeMorphism):
    r"""A map into a glued scheme factoring through one selected affine chart."""

    def __init__(self, parent, chart_embedding, chart_map) -> None:
        super().__init__(None, homset=parent)
        if chart_embedding is not chart_embedding.gluing_datum().chart_embedding(chart_embedding.chart_index()):
            raise TypeError("a glued chart-factor map factors through a chart embedding selected by the gluing datum")
        if chart_map.codomain() is not chart_embedding.domain():
            raise ValueError("the affine factor must land in the selected glued chart")
        if chart_map.domain() is not self.domain() or chart_embedding.codomain() is not self.codomain():
            raise ValueError("the glued chart-factor map has the wrong Hom endpoints")
        self._chart_embedding = chart_embedding
        self._chart_map = chart_map

    def chart_embedding(self):
        return self._chart_embedding

    def chart_index(self):
        return self.chart_embedding().chart_index()

    def chart_map(self):
        return self._chart_map

    def gluing_datum(self):
        return self.chart_embedding().gluing_datum()

    def _in_homset(self, homset):
        chart_map = homset.homset_category().Mor(self.domain(), self.chart_embedding().domain())(self.chart_map())
        return _GluedSchemeChartMap(homset, self.chart_embedding(), chart_map)

    def __mul__(self, other):
        composite = self.chart_map() * other
        if composite is NotImplemented:
            return NotImplemented
        return _GluedSchemeChartMap(
            _scheme_composition_hom(self, other), self.chart_embedding(), composite,
        )

    def _postcompose_with(self, after):
        r"""``after o e_i o g`` is the local map of ``after`` on chart ``i`` after ``g``."""
        if after.domain() is not self.codomain():
            return NotImplemented
        return after.local_map(self.chart_index()) * self.chart_map()

    def __eq__(self, other) -> bool:
        if isinstance(other, _GluedSchemeChartEmbedding):
            return (
                other.codomain() is self.codomain()
                and other.gluing_datum() is self.gluing_datum()
                and other.chart_index() == self.chart_index()
                and self.chart_map()
                == other.domain().categorical_identity_morphism()
            )
        if not isinstance(other, _GluedSchemeChartMap) or other.codomain() is not self.codomain():
            return False
        if self.chart_index() == other.chart_index():
            return self.chart_map() == other.chart_map()
        datum = self.gluing_datum()
        if other.gluing_datum() is not datum:
            return False
        left_overlap = datum.overlap(self.chart_index(), other.chart_index())
        right_overlap = datum.overlap(other.chart_index(), self.chart_index())
        if not _lands_in_distinguished_open(self.chart_map(), left_overlap):
            return False
        if not _lands_in_distinguished_open(other.chart_map(), right_overlap):
            return False
        left = left_overlap.corestriction(self.chart_map())
        right = right_overlap.corestriction(other.chart_map())
        transition = datum.transition_between(
            self.chart_index(), other.chart_index()
        ).forward()
        return transition * left == right

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None


class _GluedSchemeMorphism(SchemeMorphism):
    r"""A morphism out of a glued scheme, represented by compatible chart maps."""

    def __init__(self, parent, local_maps, *, verify_compatibility=True, cone_construction=None) -> None:
        super().__init__(None, homset=parent, cone_construction=cone_construction)
        datum = self.parent().gluing_datum()
        raw_local_maps = _family_on_finite_ordered_set(
            datum.chart_index_set(),
            local_maps,
            name="Raw local maps of a glued-scheme morphism",
            noun="a glued-scheme morphism",
        )
        schemes = self.parent().homset_category()
        self._local_maps = finite_indexed_family(
            datum.chart_index_set(),
            lambda index: schemes.Mor(datum.chart(index), self.codomain())(
                raw_local_maps[index]
            ),
            name="Local maps of a glued-scheme morphism",
        )
        if verify_compatibility:
            self._verify_overlap_compatibility()

    def with_cone_construction(self, construction):
        r"""Retain the inducing cone without discarding the compatible chart maps."""
        return _GluedSchemeMorphism(
            self.parent(), self.local_maps(), cone_construction=construction,
        )

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[
            self.parent().gluing_datum().normalize_chart_index(index)
        ]

    def _verify_overlap_compatibility(self) -> None:
        datum = self.parent().gluing_datum()
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
        return _scheme_composition_hom(after, self)(
            tuple(after * local_map for local_map in self.local_maps())
        )

    def __mul__(self, other):
        r"""``self o other``, asked of ``other``, which knows how it reaches the glued scheme.

        A morphism into the glued scheme through chart ``i`` composes with the
        local map on chart ``i``; a morphism out of another glued scheme
        composes chart by chart.  Both are its ``_postcompose_with``.
        """
        if other.codomain() is not self.domain():
            return NotImplemented
        if self._is_the_identity():
            return other
        if other._is_the_identity():
            return self
        return other._postcompose_with(self)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, _GluedSchemeMorphism)
            and other.domain() is self.domain()
            and other.codomain() is self.codomain()
            and all(
                self.local_map(index) == other.local_map(index)
                for index in self.parent().gluing_datum().chart_indices()
            )
        )

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None

    def _repr_(self):
        return f"Scheme morphism from glued charts: {self.domain()} -> {self.codomain()}"


class _GluedSchemeMorCategory(SchemeMorCategory):
    r"""Maps out of a glued scheme, represented by compatible local maps on its charts.

    The gluing datum of the domain is retained by this Hom: a map out of the
    glued scheme is a family of maps out of its charts agreeing through the
    transitions, so every element reads the charts from it.
    """

    def __init__(self, hom_family, domain, codomain) -> None:
        self._gluing_datum = domain.gluing_datum()
        super().__init__(hom_family, domain, codomain)

    def gluing_datum(self):
        return self._gluing_datum

    def _element_constructor_(self, datum):
        if isinstance(datum, _GluedSchemeMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the glued-scheme morphism has the wrong endpoints")
            if datum.parent() is self:
                return datum
            return _GluedSchemeMorphism(
                self, datum.local_maps(), cone_construction=datum.cone_construction(),
            )
        if isinstance(datum, (tuple, list, IndexedFamily, Mapping)):
            return _GluedSchemeMorphism(self, datum)
        return super()._element_constructor_(datum)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on a glued-scheme endomorphism Hom")
        datum = self.gluing_datum()
        return _GluedSchemeMorphism(
            self,
            tuple(
                datum.chart_embedding(index)
                for index in datum.chart_indices()
            ),
            verify_compatibility=False,
        )


def _glued_chart_image(datum, index):
    r"""The open image of chart ``index`` in the glued scheme, an open subscheme with its inclusion."""
    chart = datum.chart(index)
    scheme = datum.scheme()
    return _affine_scheme(
        chart.coordinate_algebra(),
        datum.base_ring(),
        (OpenImmersions(scheme),),
        inclusion_codomain=scheme,
        inclusion_datum=lambda hom: _GluedSchemeOpenInclusion(hom, datum, index),
    )


def _glued_chart_isomorphism(datum, index):
    r"""``U_i -> image(U_i)``, the identity of the chart's coordinate algebra read between the two."""
    chart = datum.chart(index)
    chart_image = datum.chart_image(index)
    algebra = chart.coordinate_algebra()
    schemes = Schemes(datum.base_ring())
    identity_pullback = algebra.Mor(algebra).identity()
    return schemes.Core().Mor(chart, chart_image)(
        schemes.Mor(chart, chart_image)(identity_pullback),
        schemes.Mor(chart_image, chart)(identity_pullback),
    )


def _glued_chart_embedding(datum, index):
    r"""``e_i : U_i -> X``, the chart isomorphism onto its open image followed by that image's inclusion."""
    chart = datum.chart(index)
    return _GluedSchemeChartEmbedding(
        Schemes(datum.base_ring()).Mor(chart, datum.scheme()),
        datum,
        index,
        datum.chart_image(index),
        datum.chart_isomorphism(index),
    )


def _glued_scheme(datum, placements, level_data):
    r"""The scheme glued from ``datum``: an object of ``Schemes(R)``, built by its entry.

    ``placements`` are further categories the scheme is an object of by its
    construction, with the level data they declare.  The scheme is realized
    privately by :class:`_GluedScheme`, which holds the gluing datum.
    """
    base = datum.base_ring()
    category = Schemes(base)
    if placements:
        category = Category.join((category, *placements))
    data = dict(level_data)
    native = data.pop("scheme_engine", None)
    object_engine = data.pop("_object_engine", None)
    return _object_of(
        category,
        _engine=None if object_engine is None else (category, object_engine, None),
        scheme_base_ring=base,
        scheme_engine=_GluedScheme(datum, native),
        **data,
    )


class _GluedScheme(SageObject):
    r"""The private realization of a scheme glued from an affine gluing datum (``OWN-06``).

    A gluing datum -- affine charts ``U_i``, open subschemes ``U_ij <= U_i`` and
    isomorphisms ``phi_ij : U_ij -> U_ji`` satisfying the cocycle condition on
    triple overlaps -- determines a scheme ``X`` with open immersions
    ``U_i -> X`` (Stacks, Tag 01JA).  ``X`` is an object of ``Schemes(R)``.  This
    realization is its ``scheme_engine``: it holds the gluing datum, the chosen
    presentation of ``X`` (``CON-05``), and computes what that datum
    determines.

    Its consumer is the engine adapter of the ``Schemes(R)`` level, which reads
    the datum through :meth:`gluing_datum` and asks this realization for the Hom
    out of ``X`` (:meth:`scheme_homset_class`), the structure morphism
    (:meth:`structure_morphism`) and the chartwise constructions.
    """

    def __init__(self, gluing_datum, native_realization=None) -> None:
        self._gluing_datum = gluing_datum
        self._native_realization = native_realization

    def gluing_datum(self):
        return self._gluing_datum

    def native_realization(self):
        r"""The optional native scheme of this same atlas, supplied by its construction."""
        assert self._native_realization is not None, (
            "this gluing datum has no additional native scheme realization"
        )
        return self._native_realization

    def scheme_homset_class(self):
        r"""The compatible-chart-map realization of the Hom chosen by its family."""
        return _GluedSchemeMorCategory

    def structure_morphism(self, scheme):
        r"""``X -> Spec R``, glued from the structure morphisms of the charts."""
        datum = self.gluing_datum()
        base = datum.base_ring()
        base_scheme = base.affine_spectrum(base_ring=base)
        return scheme.Mor(base_scheme)(
            datum.charts().map(lambda chart: _affine_structure_morphism_to_base(chart, base))
        )

    def chartwise_closed_subscheme(
        self,
        local_closed_subschemes,
        *,
        name="Chartwise closed subscheme",
        _engine=None,
        construction_data=None,
    ):
        return _chartwise_closed_subscheme(
            self.gluing_datum(),
            local_closed_subschemes,
            name=name,
            _engine=_engine,
            construction_data=construction_data,
        )

    def chartwise_fixed_subscheme(self, local_automorphisms):
        return _chartwise_fixed_subscheme(self.gluing_datum(), local_automorphisms)

    def c2_chartwise_invariant_quotient(
        self,
        scheme,
        acting_group,
        local_actions,
        *,
        _engine=None,
        construction_data=None,
    ):
        r"""The glued scheme ``scheme`` modulo a chart-preserving ``C2`` action."""
        from dzack_research.preamble.categories.schemes.invariant_quotient_gluing import (
            _c2_chartwise_glued_invariant_quotient,
        )

        return _c2_chartwise_glued_invariant_quotient(
            scheme,
            acting_group,
            local_actions,
            quotient_scheme_engine=_engine,
            quotient_scheme_data=construction_data,
        )

    def _repr_(self):
        return f"Gluing realization over the affine atlas indexed by {self.gluing_datum().chart_index_set()}"


class _TwoChartSchemeGluingDatum(SageObject):
    r"""Two affine schemes glued along an isomorphism of represented affine opens."""

    def __init__(self, schemes, left_chart, right_chart, transition) -> None:
        base = schemes.base_ring()
        if left_chart not in Schemes(base).Affine() or right_chart not in Schemes(base).Affine():
            raise TypeError("the represented two-chart gluing currently requires affine charts")
        if transition not in _scheme_core_hom(transition):
            raise TypeError("scheme gluing requires an isomorphism of schemes between the two overlaps")
        forward = transition.forward()
        inverse = transition.inverse()
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
        self._scheme = _glued_scheme(self, (), {})

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
        return self._reversed_transition()

    @cached_method
    def _reversed_transition(self):
        r"""``phi^{-1}``, the isomorphism from the right overlap to the left one."""
        transition = self.transition()
        return Schemes(self.base_ring()).Core().Mor(transition.codomain(), transition.domain())(
            transition.inverse(),
            transition.forward(),
        )

    def overlap(self, source_index, target_index):
        return self.transition_between(source_index, target_index).forward().domain()

    def left_overlap(self):
        return self.transition().forward().domain()

    def right_overlap(self):
        return self.transition().forward().codomain()

    def scheme(self):
        return self._scheme

    def chart_image(self, index):
        return self._chart_image(self.normalize_chart_index(index))

    @cached_method
    def _chart_image(self, label):
        return _glued_chart_image(self, label)

    def chart_isomorphism(self, index):
        return self._chart_isomorphism(self.normalize_chart_index(index))

    @cached_method
    def _chart_isomorphism(self, label):
        return _glued_chart_isomorphism(self, label)

    def chart_embedding(self, index):
        return self._chart_embedding(self.normalize_chart_index(index))

    @cached_method
    def _chart_embedding(self, label):
        return _glued_chart_embedding(self, label)

    def chart_images(self):
        return finite_indexed_family(self.chart_index_set(), self.chart_image, name="Open chart images in glued scheme")

    def chart_isomorphisms(self):
        return finite_indexed_family(self.chart_index_set(), self.chart_isomorphism, name="Chart-to-image isomorphisms")

    def _repr_(self):
        return f"Two-chart scheme gluing datum for {self.chart(0)} and {self.chart(1)}"


class _FiniteSchemeGluingDatum(SageObject):
    r"""Finite affine charts with distinguished pair overlaps and a cocycle."""

    def __init__(self, schemes, charts, transitions, *, placements=(), level_data=None) -> None:
        self._schemes = schemes
        self._charts = _finite_chart_family(charts)
        for chart in self.charts():
            if chart not in Schemes(self.base_ring()).Affine():
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

        self._verify_pairwise_transitions()
        self._verify_triple_domains_and_cocycle()
        self._scheme = _glued_scheme(self, placements, {} if level_data is None else level_data)

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
        reversed_transition = transition.parent().core_category().Mor(
            transition.codomain(),
            transition.domain(),
        )(
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
            if transition not in _scheme_core_hom(transition):
                raise TypeError("each finite-atlas transition is an isomorphism of schemes between its two overlaps")
            forward = transition.forward()
            inverse = transition.inverse()
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
        if not _lands_in_distinguished_open(target_chart_map, target_triple):
            raise ValueError(
                "finite-atlas transition does not preserve the represented triple-overlap domain"
            )
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

    def scheme(self):
        return self._scheme

    def chart_image(self, index):
        return self._chart_image(self.normalize_chart_index(index))

    @cached_method
    def _chart_image(self, label):
        return _glued_chart_image(self, label)

    def chart_isomorphism(self, index):
        return self._chart_isomorphism(self.normalize_chart_index(index))

    @cached_method
    def _chart_isomorphism(self, label):
        return _glued_chart_isomorphism(self, label)

    def chart_embedding(self, index):
        return self._chart_embedding(self.normalize_chart_index(index))

    @cached_method
    def _chart_embedding(self, label):
        return _glued_chart_embedding(self, label)

    def chart_images(self):
        return finite_indexed_family(self.chart_index_set(), self.chart_image, name="Open chart images in glued scheme")

    def chart_isomorphisms(self):
        return finite_indexed_family(self.chart_index_set(), self.chart_isomorphism, name="Chart-to-image isomorphisms")

    def _repr_(self):
        return f"Finite affine scheme gluing datum indexed by {self.chart_index_set()}"


class _FiniteAffineAtlasEngine:
    r"""Private realization retaining the chart-transition presentation of an owned atlas."""

    def __init__(self, gluing_presentation, **rest) -> None:
        self._gluing_presentation = gluing_presentation
        super().__init__(**rest)

    def presentation(self):
        return self._gluing_presentation

    def base_ring(self):
        return self.scheme().scheme_base_ring()

    def scheme(self):
        return self.target().arrow().codomain()

    def charts(self):
        return self.members().map(
            lambda member: member.domain().arrow().domain(),
            name="Affine charts",
        )

    def chart_index_set(self):
        return self.index_set()

    def chart_indices(self):
        return self.chart_index_set()

    def normalize_chart_index(self, index):
        return self.presentation().normalize_chart_index(index)

    def number_of_charts(self):
        return self.presentation().number_of_charts()

    def chart(self, index):
        return self.member(self.normalize_chart_index(index)).domain().arrow().domain()

    def transition_index_set(self):
        return self.presentation().transition_index_set()

    def transitions(self):
        return self.presentation().transitions()

    def transition_between(self, source_index, target_index):
        return self.presentation().transition_between(source_index, target_index)

    def overlap(self, source_index, target_index):
        return self.presentation().overlap(source_index, target_index)

    def triple_overlap(self, source_index, middle_index, target_index):
        return self.presentation().triple_overlap(source_index, middle_index, target_index)

    def transition_on_triple(self, source_index, target_index, third_index):
        return self.presentation().transition_on_triple(
            source_index,
            target_index,
            third_index,
        )

    def chart_embedding(self, index):
        return self.member(self.normalize_chart_index(index)).domain().arrow()

    def _repr_(self):
        return f"Finite affine atlas of {self.scheme()} indexed by {self.chart_index_set()}"


class FiniteAtlasRefinement(CoveringFamilyMorphism):
    r"""A represented refinement of one finite affine atlas by another.

    A refinement consists of a map from fine chart labels to coarse chart
    labels together with actual chart morphisms ``V_a -> U_i``.  The chart
    maps are required to commute with every pairwise transition.  Consequently
    they glue to a comparison morphism from the scheme presented by the fine
    atlas to the scheme presented by the coarse atlas.

    Both atlases cover the same scheme ``X``.  The refinement is therefore a
    morphism of covering families in the slice ``Sch_R/X``; its target edge is
    the identity of ``id_X``.  ``chart_map`` and ``comparison_morphism`` expose
    the underlying scheme arrows of those slice morphisms to geometric
    consumers.
    """

    def __init__(self, parent, index_map, chart_maps, *, target_map=None) -> None:
        fine_datum = parent.domain()
        coarse_datum = parent.codomain()
        if coarse_datum.scheme() is not fine_datum.scheme():
            raise ValueError("a finite-atlas refinement compares covers of one scheme")
        fine_indices = fine_datum.chart_index_set()
        raw_index_map = _family_on_finite_ordered_set(
            fine_indices,
            index_map,
            name="Fine-to-coarse chart labels",
            noun="finite-atlas refinement index data",
        )
        normalized_index_map = finite_indexed_family(
            fine_indices,
            lambda index: coarse_datum.normalize_chart_index(raw_index_map[index]),
            name="Fine-to-coarse chart map",
        )
        supplied_chart_maps = _family_on_finite_ordered_set(
            fine_indices,
            chart_maps,
            name="Chart morphisms of a finite-atlas refinement",
            noun="finite-atlas refinement chart maps",
        )
        site = fine_datum.site_category()
        scheme_category = Schemes(fine_datum.base_ring())
        normalized_chart_maps = {}
        for fine_index in fine_indices:
            chart_map = supplied_chart_maps[fine_index]
            coarse_index = normalized_index_map[fine_index]
            fine_chart = fine_datum.chart(fine_index)
            coarse_chart = coarse_datum.chart(coarse_index)
            fine_member = fine_datum.member(fine_index).domain()
            coarse_member = coarse_datum.member(coarse_index).domain()
            slice_hom = site.Mor(fine_member, coarse_member)
            match chart_map in slice_hom:
                case True:
                    normalized_chart_maps[fine_index] = chart_map
                case False:
                    if chart_map not in scheme_category.Mor(fine_chart, coarse_chart):
                        raise TypeError(
                            "a finite-atlas refinement chart map is a scheme morphism from its fine chart to its coarse chart"
                        )
                    normalized_chart_maps[fine_index] = slice_hom(chart_map)
        normalized_chart_maps = finite_indexed_family(
            fine_indices,
            normalized_chart_maps.__getitem__,
            name="Slice morphisms of a finite-atlas refinement",
        )
        if target_map is None:
            target_map = site.Mor(fine_datum.target(), coarse_datum.target()).identity()
        super().__init__(
            parent,
            normalized_index_map,
            normalized_chart_maps,
            target_map=target_map,
        )
        self._verify_overlap_compatibility()

    def coarse_datum(self):
        return self.codomain()

    def fine_datum(self):
        return self.domain()

    def coarse_scheme(self):
        return self.coarse_datum().scheme()

    def fine_scheme(self):
        return self.fine_datum().scheme()

    def coarse_index(self, fine_index):
        fine_index = self.fine_datum().normalize_chart_index(fine_index)
        return self.index_map(fine_index)

    def chart_map(self, fine_index):
        fine_index = self.fine_datum().normalize_chart_index(fine_index)
        return self.component(fine_index).left()

    def comparison_morphism(self):
        return self.target_map().left()

    def overlap_map(self, source_index, target_index):
        r"""Map one fine overlap to the corresponding coarse overlap or chart."""
        fine = self.fine_datum()
        coarse = self.coarse_datum()
        source_index = fine.normalize_chart_index(source_index)
        target_index = fine.normalize_chart_index(target_index)
        source_overlap = fine.overlap(source_index, target_index)
        into_coarse_chart = self.chart_map(source_index) * source_overlap.inclusion()
        coarse_source = self.coarse_index(source_index)
        coarse_target = self.coarse_index(target_index)
        if coarse_source == coarse_target:
            return into_coarse_chart
        return coarse.overlap(coarse_source, coarse_target).corestriction(
            into_coarse_chart
        )

    def _verify_overlap_compatibility(self) -> None:
        fine = self.fine_datum()
        coarse = self.coarse_datum()
        for source_index, target_index in fine.transition_index_set():
            fine_transition = fine.transition_between(source_index, target_index).forward()
            source_overlap = fine.overlap(source_index, target_index)
            target_overlap = fine.overlap(target_index, source_index)
            coarse_source = self.coarse_index(source_index)
            coarse_target = self.coarse_index(target_index)
            if coarse_source == coarse_target:
                left = self.chart_map(source_index) * source_overlap.inclusion()
                right = (
                    self.chart_map(target_index)
                    * target_overlap.inclusion()
                    * fine_transition
                )
            else:
                left = (
                    coarse.transition_between(coarse_source, coarse_target).forward()
                    * self.overlap_map(source_index, target_index)
                )
                right = self.overlap_map(target_index, source_index) * fine_transition
            if left != right:
                raise ValueError(
                    "finite-atlas refinement chart maps do not commute with an overlap transition"
                )

    @cached_method
    def inverse_image_functor(self):
        r"""Return ``f^{-1}`` on the represented module sheaves of the coarse atlas."""
        return _FiniteAtlasInverseImageModuleFunctor(self)

    @cached_method
    def inverse_image_scalar_extension_functor(self):
        r"""Return extension of scalars from ``f^{-1}O_Y`` to ``O_X``."""
        inverse_image = self.inverse_image_functor()
        return _FiniteAtlasInverseImageScalarExtensionFunctor(
            self,
            inverse_image.codomain(),
        )

    @cached_method
    def module_pullback_functor(self):
        r"""Return ``f^* = O_X tensor_{f^{-1}O_Y} f^{-1}(-)``.

        The two factors are retained as the actual functors whose composite is
        pullback: inverse image first, then extension of scalars along the
        represented structural ring maps on the fine charts.
        """
        return self.inverse_image_functor().then(
            self.inverse_image_scalar_extension_functor()
        )

    def pullback_module_datum(self, descent):
        r"""Pull a finite-atlas module descent datum to the fine atlas.

        Distinct coarse overlap rings remain distinct.  When two fine charts
        refine one coarse chart, the transition is the canonical scalar-change
        identification.  Otherwise the coarse semilinear transition is
        restricted through the represented map of fine overlaps.
        """
        if descent.gluing_datum() is not self.coarse_datum():
            raise ValueError("module descent is pulled back from this refinement's coarse atlas")
        fine = self.fine_datum()
        local_modules = {
            fine_index: descent.local_module(self.coarse_index(fine_index)).base_change(
                self.chart_map(fine_index).coordinate_algebra_morphism()
            )
            for fine_index in fine.chart_indices()
        }
        transition_data = {}
        for source_index, target_index in fine.transition_index_set():
            coarse_source = self.coarse_index(source_index)
            coarse_target = self.coarse_index(target_index)
            if coarse_source == coarse_target:
                def forward_identity(label, _domain, codomain):
                    return codomain.module_generator(label)

                def inverse_identity(label, _domain, codomain):
                    return codomain.module_generator(label)

                transition_data[source_index, target_index] = (
                    forward_identity,
                    inverse_identity,
                )
                continue

            coarse_transition = descent.transition(coarse_source, coarse_target)
            coarse_source_pair = coarse_transition.source_module()
            coarse_target_pair = coarse_transition.target_module()
            source_ring_map = self.overlap_map(
                source_index, target_index
            ).coordinate_algebra_morphism()
            target_ring_map = self.overlap_map(
                target_index, source_index
            ).coordinate_algebra_morphism()

            def forward_images(
                label,
                _domain,
                codomain,
                coarse_transition=coarse_transition,
                coarse_target_pair=coarse_target_pair,
                coarse_source_pair=coarse_source_pair,
                source_ring_map=source_ring_map,
            ):
                image = coarse_transition.pullback()(
                    coarse_target_pair.module_generator(label)
                )
                return _base_change_element(
                    coarse_source_pair,
                    codomain,
                    source_ring_map,
                    image,
                )

            def inverse_images(
                label,
                _domain,
                codomain,
                coarse_transition=coarse_transition,
                coarse_source_pair=coarse_source_pair,
                coarse_target_pair=coarse_target_pair,
                target_ring_map=target_ring_map,
            ):
                image = coarse_transition.inverse_pullback()(
                    coarse_source_pair.module_generator(label)
                )
                return _base_change_element(
                    coarse_target_pair,
                    codomain,
                    target_ring_map,
                    image,
                )

            transition_data[source_index, target_index] = (
                forward_images,
                inverse_images,
            )
        return FiniteAtlasModuleGluingData(fine)(local_modules, transition_data)

    def pullback_invertible_sheaf(self, line_bundle):
        r"""Pull a finite-atlas line bundle across this atlas refinement.

        The returned comparison retains the refined line bundle and the actual
        local module isomorphisms from the chartwise scalar pullbacks.
        """
        from dzack_research.preamble.categories.divisors.invertible_sheaves import (
            _finite_atlas_invertible_sheaf,
        )

        if line_bundle.gluing_datum() is not self.coarse_datum():
            raise ValueError("the line bundle belongs to this refinement's coarse atlas")
        fine = self.fine_datum()
        units = {}
        for source_index, target_index in fine.transition_index_set():
            coarse_source = self.coarse_index(source_index)
            coarse_target = self.coarse_index(target_index)
            source_overlap_ring = fine.overlap(
                source_index, target_index
            ).coordinate_algebra()
            if coarse_source == coarse_target:
                units[source_index, target_index] = source_overlap_ring.one()
            else:
                ring_map = self.overlap_map(
                    source_index, target_index
                ).coordinate_algebra_morphism()
                units[source_index, target_index] = ring_map(
                    line_bundle.transition_unit(coarse_source, coarse_target)
                )
        refined = _finite_atlas_invertible_sheaf(fine, units)
        return FiniteAtlasInvertibleSheafRefinement(self, line_bundle, refined)

    def compare_line_bundle_pullback(self, line_bundle):
        r"""Compare generic and specialized line-bundle pullback along this refinement."""
        return FiniteAtlasLineBundlePullbackComparison(self, line_bundle)


class FiniteAtlasHomset(CoveringFamilyHomset):
    r"""Refinements/comparisons between two finite affine atlases."""

    Element = FiniteAtlasRefinement

    def _element_constructor_(self, index_map, chart_maps=None, *, target_map=None):
        match index_map:
            case FiniteAtlasRefinement() if chart_maps is None and target_map is None:
                if index_map.parent() is self:
                    return index_map
                if index_map.domain() is not self.domain() or index_map.codomain() is not self.codomain():
                    raise ValueError("the finite-atlas refinement has the wrong endpoints")
                target_map = index_map.target_map()
                chart_maps = {
                    label: index_map.chart_map(label)
                    for label in index_map.domain().chart_indices()
                }
                index_map = {
                    label: index_map.coarse_index(label)
                    for label in self.domain().chart_indices()
                }
        if chart_maps is None:
            raise TypeError("a finite-atlas refinement requires one chart map on each fine chart")
        return self.element_class(
            self,
            index_map,
            chart_maps,
            target_map=target_map,
        )


class FiniteAtlasHomCategoryConstruction(CoveringFamilyHomCategoryConstruction):
    r"""The Hom family of finite affine atlases."""

    def fixed_category_class(self):
        return FiniteAtlasHomset


class FiniteAffineAtlases(OwnedParameterizedCategory):
    r"""Finite affine covering atlases of one scheme ``X``.

    For ``X`` over ``R``, an object is a finite covering family in the Zariski
    coverage of the slice ``Sch_R/X``.  Its members are the slice objects
    ``U_i -> X`` for affine ``U_i`` with represented open-immersion structure,
    and the family arrows land in the terminal slice object ``id_X``.  The
    selected pair overlaps and their cocycle are retained by the finite gluing
    presentation.  Morphisms are refinements in that same slice, specialized
    to chart maps compatible with the selected overlap transitions.

    The covering/refinement convention is Stacks Project, Tag 00VI; the gluing
    presentation uses the finite affine gluing convention already cited at the
    scheme owner (Tag 01JA).

    Unverified specimen: the standard atlas of projective space is constructed
    here, and its identity refinement is a morphism of this category::

        sage: from dzack_research.preamble.all import QQ, ProjectiveSpaces
        sage: from dzack_research.preamble.categories.schemes.gluing import FiniteAffineAtlases
        sage: line = ProjectiveSpaces(QQ)(1)
        sage: atlas = line.standard_affine_atlas()
        sage: atlas in FiniteAffineAtlases(line)
        True
        sage: atlas in zariski_coverage(line)
        True
        sage: atlas.coverage() is zariski_coverage(line)
        True
        sage: atlas.site_category().base_object() is line
        True
        sage: atlas.target().arrow() == line.categorical_identity_morphism()
        True
        sage: identity = FiniteAffineAtlases(line).Mor(atlas, atlas).identity()
        sage: identity.domain() is atlas and identity.codomain() is atlas
        True
    """

    _HomCategory = FiniteAtlasHomCategoryConstruction

    @staticmethod
    def __classcall__(cls, scheme):
        return OwnedParameterizedCategory.__classcall__(cls, scheme)

    def __init__(self, scheme) -> None:
        OwnedParameterizedCategory.__init__(self, scheme)

    def parameter_category(self):
        return Schemes(self.scheme().scheme_base_ring())

    def scheme(self):
        return self.base()

    def base_ring(self):
        return self.scheme().scheme_base_ring()

    def coverage(self):
        return zariski_coverage(self.scheme())

    def site_category(self):
        return self.coverage().site_category()

    @cached_method
    def slice_target(self):
        r"""The terminal object ``id_X`` of ``Sch_R/X`` used by every atlas here."""
        return self.coverage().slice_target()

    def super_categories(self):
        return [ZariskiCoveringFamilies(self.scheme())]

    class ParentMethods:
        def coverage(self):
            r"""The Zariski coverage of ``Sch_R/X`` containing this atlas."""
            return self.category().coverage()

    def _call_(self, charts, transitions, chart_embeddings):
        presentation = _FiniteSchemeGluingDatum(
            Schemes(self.base_ring()),
            charts,
            transitions,
        )
        return self._from_gluing_presentation(
            presentation,
            chart_embeddings,
        )

    def _from_gluing_presentation(self, presentation, chart_embeddings=None):
        if presentation.base_ring() is not self.base_ring():
            raise ValueError("an affine-atlas presentation uses the category's base ring")
        scheme = self.scheme()
        indices = presentation.chart_index_set()
        if chart_embeddings is None:
            if presentation.scheme() is not scheme:
                raise ValueError("a foreign gluing presentation needs explicit chart embeddings")
            chart_embeddings = finite_indexed_family(
                indices,
                presentation.chart_embedding,
                name="Affine-atlas chart embeddings",
            )
        raw_embeddings = _family_on_finite_ordered_set(
            indices,
            chart_embeddings,
            name="Affine-atlas chart embeddings",
            noun="finite affine-atlas chart embeddings",
        )
        scheme_category = Schemes(self.base_ring())
        embeddings = finite_indexed_family(
            indices,
            lambda index: scheme_category.Mor(
                presentation.chart(index),
                scheme,
            )(raw_embeddings[index]),
            name="Affine-atlas chart embeddings",
        )
        affine = Schemes(self.base_ring()).Affine()
        for index in indices:
            chart = presentation.chart(index)
            embedding = embeddings[index]
            if chart not in affine:
                raise TypeError("every chart of a finite affine atlas is affine")
            if embedding.is_open_immersion() is not True:
                raise TypeError("every chart map of a finite affine atlas is an open immersion")
        site = self.site_category()
        target = self.slice_target()
        chart_objects = finite_indexed_family(
            indices,
            lambda index: site.object(embeddings[index]),
            name="Affine charts in the scheme slice",
        )
        members = finite_indexed_family(
            indices,
            lambda index: site.Mor(chart_objects[index], target)(embeddings[index]),
            name="Affine-atlas cover arrows in the scheme slice",
        )
        overlaps = {}
        for left, right in presentation.transition_index_set():
            source_overlap = presentation.overlap(left, right)
            target_overlap = presentation.overlap(right, left)
            forward = presentation.transition_between(left, right).forward()
            left_leg = source_overlap.inclusion()
            right_leg = target_overlap.inclusion() * forward
            overlap_object = site.object(embeddings[left] * left_leg)
            overlaps[left, right] = (
                overlap_object,
                site.Mor(overlap_object, chart_objects[left])(left_leg),
                site.Mor(overlap_object, chart_objects[right])(right_leg),
            )
        return self.family(
            target,
            members,
            overlaps,
            _engine=(self, _FiniteAffineAtlasEngine, None),
            gluing_presentation=presentation,
        )

    def an_object(self):
        scheme = self.scheme()
        assert scheme in Schemes(self.base_ring()).Affine(), (
            "the automatic finite-atlas witness is currently available for an affine scheme parameter"
        )
        identity = scheme.Mor(scheme).identity()
        return self(
            (scheme,),
            {},
            (identity,),
        )


class FiniteAtlasInvertibleSheafRefinement(SageObject):
    r"""The chartwise pullback comparison for a finite-atlas line bundle."""

    def __init__(self, refinement, coarse_bundle, refined_bundle) -> None:
        self._refinement = refinement
        self._coarse_bundle = coarse_bundle
        self._refined_bundle = refined_bundle
        fine = refinement.fine_datum()
        local_isomorphisms = {}
        for fine_index in fine.chart_indices():
            coarse_index = refinement.coarse_index(fine_index)
            pulled = coarse_bundle.local_module(coarse_index).base_change(
                refinement.chart_map(fine_index).coordinate_algebra_morphism()
            )
            refined = refined_bundle.local_module(fine_index)
            pulled_labels = tuple(pulled.module_generating_set())
            refined_labels = tuple(refined.module_generating_set())
            if len(pulled_labels) != len(refined_labels):
                raise ArithmeticError("line-bundle refinement changed the local rank")
            forward = pulled.module_category().Mor(pulled, refined)(
                {
                    source_label: refined.module_generator(target_label)
                    for source_label, target_label in zip(
                        pulled_labels, refined_labels, strict=True
                    )
                }
            )
            inverse = refined.module_category().Mor(refined, pulled)(
                {
                    target_label: pulled.module_generator(source_label)
                    for source_label, target_label in zip(
                        pulled_labels, refined_labels, strict=True
                    )
                }
            )
            local_isomorphisms[fine_index] = pulled.module_category().Core().Mor(
                pulled,
                refined,
            )(forward, inverse)
        self._local_isomorphisms = finite_indexed_family(
            fine.chart_index_set(),
            lambda index: local_isomorphisms[index],
            name="Local line-bundle isomorphisms under atlas refinement",
        )

    def refinement(self):
        return self._refinement

    def coarse_bundle(self):
        return self._coarse_bundle

    def refined_bundle(self):
        return self._refined_bundle

    def scheme_comparison(self):
        return self.refinement().comparison_morphism()

    def local_isomorphisms(self):
        return self._local_isomorphisms

    def local_isomorphism(self, fine_index):
        fine_index = self.refinement().fine_datum().normalize_chart_index(fine_index)
        return self.local_isomorphisms()[fine_index]


def _finite_framing(module):
    if not module.is_framed_module():
        raise TypeError("affine module descent currently requires finitely framed local modules")
    labels = module.module_generating_set()
    if not labels.cardinality().is_finite():
        raise TypeError("affine module descent currently requires finitely framed local modules")
    return labels


def _maps_agree_on_framing(left, right) -> bool:
    if left.domain() is not right.domain() or left.codomain() is not right.codomain():
        return False
    labels = _finite_framing(left.domain())
    return all(
        left(left.domain().module_generator(label))
        == right(right.domain().module_generator(label))
        for label in labels
    )


class SemilinearAlgebraMorphism(SageObject):
    r"""A semilinear algebra morphism over a represented scalar map.

    For ``sigma : R -> S`` this is the algebra morphism
    ``A -> Res_sigma(B)`` written as a map from the original ``R``-algebra
    ``A`` to the original ``S``-algebra ``B``.  Multiplication and the unit are
    therefore checked by the existing algebra-Hom owner, while composition
    retains the composed scalar map.
    """

    def __init__(self, source, target, scalar_map, images) -> None:
        if scalar_map.domain() is not source.base_ring():
            raise ValueError("a semilinear algebra scalar map starts at the source base ring")
        if scalar_map.codomain() is not target.base_ring():
            raise ValueError("a semilinear algebra scalar map ends at the target base ring")
        labels = source.algebra_generating_set()
        if not labels.cardinality().is_finite():
            raise TypeError("finite-atlas algebra descent requires finite algebra framings")
        self._source = source
        self._target = target
        self._scalar_map = scalar_map
        self._restricted_target = target.restrict_scalars(scalar_map)
        supplied = (
            {label: images(label) for label in labels}
            if callable(images)
            else dict(images)
        )
        self._morphism = _algebra_homset(source, self._restricted_target)(
            {
                label: self._restricted_target(target(supplied[label]))
                for label in labels
            }
        )

    def source(self):
        return self._source

    domain = source

    def target(self):
        return self._target

    codomain = target

    def scalar_map(self):
        return self._scalar_map

    def restricted_target(self):
        return self._restricted_target

    def algebra_morphism(self):
        return self._morphism

    def __call__(self, element):
        return self.target()(self.algebra_morphism()(self.source()(element)))

    def induced_morphism(self, morphism):
        r"""Factor ``morphism`` through this scalar-extension target.

        For ``sigma:R->S`` and ``B = S tensor_R A``, a ring map ``g:A->T``
        factors through ``B`` once its scalar restriction ``R->T`` factors
        through ``S``.  The scalar factor supplies the ``S``-algebra structure
        on ``T`` and the images of the selected algebra generators determine
        the unique algebra map ``B->T``.
        """

        if morphism.domain() is not self.source():
            raise ValueError("a scalar-extension factor extends a map from the original algebra")
        source_structure = self.source().algebra_structure_morphism()
        scalar_restriction = self.source().base_ring().Mor(morphism.codomain())(
            lambda scalar: morphism(source_structure(scalar)),
        )
        target_scalars = self.target().base_ring()
        assert target_scalars in LocalizationRings(), (
            "semilinear algebra factorization is represented here when the target scalars are a localization"
        )
        localization_source = target_scalars.localization_source()
        source_scalars = self.source().base_ring()
        localization_steps = []
        current = source_scalars
        while current is not localization_source:
            if current not in LocalizationRings():
                raise ValueError(
                    "the scalar-extension source is not represented as a localization tower over the target localization source"
                )
            localization_steps.append(current.localization_map())
            current = current.localization_source()
        source_map = localization_source.Mor(localization_source).identity()
        for step in reversed(localization_steps):
            source_map = step * source_map
        scalar_factor = target_scalars.induced_morphism(
            scalar_restriction * source_map
        )
        target_view = _algebra_structure_view(morphism.codomain(), scalar_factor)
        source_labels = self.source().algebra_generating_set()
        target_labels = self.target().algebra_generating_set()
        if source_labels != target_labels:
            raise ValueError("scalar extension must retain the selected algebra generating set")
        algebra_factor = _algebra_homset(self.target(), target_view)(
            {
                label: target_view(morphism(self.source().algebra_generator(label)))
                for label in target_labels
            }
        )
        return self.target().Mor(morphism.codomain())(
            lambda element: morphism.codomain()(algebra_factor(self.target()(element))),
        )

    def __mul__(self, other):
        if other.target() is not self.source():
            return NotImplemented
        scalar_map = self.scalar_map() * other.scalar_map()
        return SemilinearAlgebraMorphism(
            other.source(),
            self.target(),
            scalar_map,
            {
                label: self(other(other.source().algebra_generator(label)))
                for label in other.source().algebra_generating_set()
            },
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, SemilinearAlgebraMorphism)
            and other.source() is self.source()
            and other.target() is self.target()
            and other.scalar_map() == self.scalar_map()
            and all(
                other(self.source().algebra_generator(label))
                == self(self.source().algebra_generator(label))
                for label in self.source().algebra_generating_set()
            )
        )

    def __ne__(self, other) -> bool:
        return not self == other

    @classmethod
    def identity(cls, algebra):
        return cls(
            algebra,
            algebra,
            algebra.base_ring().Mor(algebra.base_ring()).identity(),
            {
                label: algebra.algebra_generator(label)
                for label in algebra.algebra_generating_set()
            },
        )

    @classmethod
    def from_linear(cls, morphism):
        source = morphism.domain()
        target = morphism.codomain()
        if source.base_ring() is not target.base_ring():
            raise ValueError("an algebra morphism has one scalar base")
        return cls(
            source,
            target,
            source.base_ring().Mor(source.base_ring()).identity(),
            {
                label: morphism(source.algebra_generator(label))
                for label in source.algebra_generating_set()
            },
        )


class FiniteAtlasAlgebraTransition(SageObject):
    r"""One semilinear algebra-descent isomorphism across two affine overlaps."""

    def __init__(self, scheme_transition, source_algebra, target_algebra, pullback, inverse_pullback) -> None:
        if scheme_transition not in _scheme_core_hom(scheme_transition):
            raise TypeError("an algebra overlap transition lies over a represented scheme isomorphism")
        self._scheme_transition = scheme_transition
        self._source_algebra = source_algebra
        self._target_algebra = target_algebra
        self._pullback = pullback
        self._inverse_pullback = inverse_pullback
        forward_scalar = scheme_transition.forward().coordinate_algebra_morphism()
        reverse_scalar = scheme_transition.inverse().coordinate_algebra_morphism()
        if (
            pullback.source() is not target_algebra
            or pullback.target() is not source_algebra
            or pullback.scalar_map() != forward_scalar
        ):
            raise ValueError("the algebra pullback has the wrong semilinear endpoints")
        if (
            inverse_pullback.source() is not source_algebra
            or inverse_pullback.target() is not target_algebra
            or inverse_pullback.scalar_map() != reverse_scalar
        ):
            raise ValueError("the inverse algebra pullback has the wrong semilinear endpoints")
        if pullback * inverse_pullback != SemilinearAlgebraMorphism.identity(source_algebra):
            raise ValueError("the finite-atlas algebra transition is not left-invertible")
        if inverse_pullback * pullback != SemilinearAlgebraMorphism.identity(target_algebra):
            raise ValueError("the finite-atlas algebra transition is not right-invertible")

    def scheme_transition(self):
        return self._scheme_transition

    def source_algebra(self):
        return self._source_algebra

    def target_algebra(self):
        return self._target_algebra

    def pullback(self):
        return self._pullback

    def inverse_pullback(self):
        return self._inverse_pullback


class FiniteAtlasModuleTransition(SageObject):
    r"""One semilinear module-descent isomorphism across two affine overlaps.

    If ``phi : U_i -> U_j`` is the represented overlap isomorphism then
    ``phi^# : B_j -> B_i`` acts contravariantly on modules: the stored
    ``pullback`` is therefore a ``phi^#``-semilinear map ``M_j -> M_i``.
    The inverse scheme arrow supplies the reverse semilinear map.
    """

    def __init__(
        self,
        scheme_transition,
        source_module,
        target_module,
        pullback,
        inverse_pullback,
    ) -> None:
        if scheme_transition not in _scheme_core_hom(scheme_transition):
            raise TypeError("a module overlap transition lies over a represented scheme isomorphism")
        self._scheme_transition = scheme_transition
        self._source_module = source_module
        self._target_module = target_module
        self._pullback = pullback
        self._inverse_pullback = inverse_pullback
        forward_scalar = scheme_transition.forward().coordinate_algebra_morphism()
        reverse_scalar = scheme_transition.inverse().coordinate_algebra_morphism()
        if (
            pullback.source() is not target_module
            or pullback.target() is not source_module
            or pullback.scalar_map() != forward_scalar
        ):
            raise ValueError("the module pullback has the wrong semilinear endpoints")
        if (
            inverse_pullback.source() is not source_module
            or inverse_pullback.target() is not target_module
            or inverse_pullback.scalar_map() != reverse_scalar
        ):
            raise ValueError("the inverse module pullback has the wrong semilinear endpoints")
        if pullback * inverse_pullback != SemilinearModuleMorphism.identity(source_module):
            raise ValueError("the finite-atlas module transition is not left-invertible")
        if inverse_pullback * pullback != SemilinearModuleMorphism.identity(target_module):
            raise ValueError("the finite-atlas module transition is not right-invertible")

    def scheme_transition(self):
        return self._scheme_transition

    def source_module(self):
        return self._source_module

    def target_module(self):
        return self._target_module

    def pullback(self):
        return self._pullback

    def inverse_pullback(self):
        return self._inverse_pullback


class _FiniteAtlasModuleGluingDatumEngine:
    r"""Module descent on a finite affine atlas with distinct overlap rings.

    Pair ``(i,j)`` transition data are supplied as two generator-image
    families: the pullback ``M_j|U_ji -> M_i|U_ij`` over ``phi_ij^#`` and its
    inverse over ``phi_ji^#``.  The two overlap modules are not identified.
    Triple restrictions are rebuilt directly from each chart module and the
    represented triple open, so the cocycle is an equality of semilinear maps
    on canonical source/target parents rather than on iterated base changes.
    """

    def __init__(self, gluing_datum, local_modules, transitions, **rest) -> None:
        self._gluing_datum = gluing_datum
        indices = gluing_datum.chart_index_set()
        self._local_modules = _family_on_finite_ordered_set(
            indices,
            local_modules,
            name="Local modules of finite-atlas descent",
            noun="finite-atlas local module data",
        )
        for index in indices:
            module = self._local_modules[index]
            if module.base_ring() is not gluing_datum.chart(index).coordinate_algebra():
                raise ValueError("each finite-atlas local module is defined over its chart ring")
            _finite_framing(module)
        self._transition_data = _family_on_finite_ordered_set(
            gluing_datum.transition_index_set(),
            transitions,
            name="Semilinear transition data of a finite atlas",
            noun="finite-atlas module transition data",
        )
        self._pair_modules = []
        self._triple_modules = []
        self._transitions = []
        self._triple_transitions = []
        super().__init__(**rest)
        for pair in gluing_datum.transition_index_set():
            self.transition(*pair)
        self._verify_cocycle()

    def gluing_datum(self):
        return self._gluing_datum

    def scheme(self):
        return self.gluing_datum().scheme()

    def chart_indices(self):
        return self.gluing_datum().chart_indices()

    def local_modules(self):
        return self._local_modules

    def local_module(self, index):
        index = self.gluing_datum().normalize_chart_index(index)
        return self.local_modules()[index]

    def pair_module(self, chart_index, other_index):
        datum = self.gluing_datum()
        chart_index = datum.normalize_chart_index(chart_index)
        other_index = datum.normalize_chart_index(other_index)
        key = (chart_index, other_index)
        for cached_key, cached in self._pair_modules:
            if cached_key == key:
                return cached
        overlap = datum.overlap(chart_index, other_index)
        ring_map = overlap.inclusion().coordinate_algebra_morphism()
        module = self.local_module(chart_index).base_change(ring_map)
        self._pair_modules.append((key, module))
        return module

    def triple_module(self, chart_index, first_other, second_other):
        datum = self.gluing_datum()
        chart_index = datum.normalize_chart_index(chart_index)
        ranking = datum.chart_index_set().ranking_map()
        others = tuple(
            sorted(
                (
                    datum.normalize_chart_index(first_other),
                    datum.normalize_chart_index(second_other),
                ),
                key=ranking,
            )
        )
        key = (chart_index, *others)
        for cached_key, cached in self._triple_modules:
            if cached_key == key:
                return cached
        triple = datum.triple_overlap(chart_index, *others)
        ring_map = triple.inclusion().coordinate_algebra_morphism()
        module = self.local_module(chart_index).base_change(ring_map)
        self._triple_modules.append((key, module))
        return module

    def _transition_images(self, source_index, target_index):
        datum = self.gluing_datum()
        pair = datum._ordered_pair(source_index, target_index)
        pullback_images, inverse_images = self._transition_data[pair]
        if pair == (
            datum.normalize_chart_index(source_index),
            datum.normalize_chart_index(target_index),
        ):
            return pullback_images, inverse_images
        return inverse_images, pullback_images

    @staticmethod
    def _images_from_coordinates(domain, codomain, specification):
        r"""Turn generator-coordinate data into elements of ``codomain``.

        A mapping value may already be a codomain element or may itself be a
        mapping from codomain framing labels to scalar coefficients.  The
        latter is the public finite-atlas ingress: callers need not construct
        elements of the internally cached overlap modules.
        """
        if callable(specification):
            return {
                label: specification(label, domain, codomain)
                for label in domain.module_generating_set()
            }
        supplied = dict(specification)
        if set(supplied) != set(domain.module_generating_set()):
            raise ValueError("module transition coordinates require one image per source generator")
        images = {}
        for label in domain.module_generating_set():
            value = supplied[label]
            if value in codomain:
                images[label] = codomain(value)
            else:
                images[label] = codomain.linear_combination(
                    {
                        target_label: codomain.base_ring()(coefficient)
                        for target_label, coefficient in dict(value).items()
                        if codomain.base_ring()(coefficient) != codomain.base_ring().zero()
                    }
                )
        return images

    def transition(self, source_index, target_index):
        datum = self.gluing_datum()
        source_index = datum.normalize_chart_index(source_index)
        target_index = datum.normalize_chart_index(target_index)
        key = (source_index, target_index)
        for cached_key, cached in self._transitions:
            if cached_key == key:
                return cached
        scheme_transition = datum.transition_between(source_index, target_index)
        source = self.pair_module(source_index, target_index)
        target = self.pair_module(target_index, source_index)
        pullback_images, inverse_images = self._transition_images(
            source_index, target_index
        )
        fibered_modules = ModulesOverCommutativeRings()
        pullback = fibered_modules.Mor(target, source)(
            scheme_transition.forward().coordinate_algebra_morphism(),
            self._images_from_coordinates(target, source, pullback_images),
        )
        inverse_pullback = fibered_modules.Mor(source, target)(
            scheme_transition.inverse().coordinate_algebra_morphism(),
            self._images_from_coordinates(source, target, inverse_images),
        )
        transition = FiniteAtlasModuleTransition(
            scheme_transition,
            source,
            target,
            pullback,
            inverse_pullback,
        )
        self._transitions.append((key, transition))
        return transition

    def transition_on_triple(self, source_index, target_index, third_index):
        datum = self.gluing_datum()
        source_index = datum.normalize_chart_index(source_index)
        target_index = datum.normalize_chart_index(target_index)
        third_index = datum.normalize_chart_index(third_index)
        key = (source_index, target_index, third_index)
        for cached_key, cached in self._triple_transitions:
            if cached_key == key:
                return cached
        pair_transition = self.transition(source_index, target_index)
        source_pair = pair_transition.source_module()
        target_pair = pair_transition.target_module()
        source_triple = self.triple_module(source_index, target_index, third_index)
        target_triple = self.triple_module(target_index, source_index, third_index)
        source_pair_open = datum.overlap(source_index, target_index)
        target_pair_open = datum.overlap(target_index, source_index)
        source_triple_open = datum.triple_overlap(
            source_index, target_index, third_index
        )
        target_triple_open = datum.triple_overlap(
            target_index, source_index, third_index
        )
        source_restriction = source_pair_open.corestriction(
            source_triple_open.inclusion()
        ).coordinate_algebra_morphism()
        target_restriction = target_pair_open.corestriction(
            target_triple_open.inclusion()
        ).coordinate_algebra_morphism()
        triple_scheme_transition = datum.transition_on_triple(
            source_index, target_index, third_index
        )
        fibered_modules = ModulesOverCommutativeRings()
        pullback = fibered_modules.Mor(target_triple, source_triple)(
            triple_scheme_transition.coordinate_algebra_morphism(),
            {
                label: _base_change_element(
                    source_pair,
                    source_triple,
                    source_restriction,
                    pair_transition.pullback()(target_pair.module_generator(label)),
                )
                for label in target_pair.module_generating_set()
            },
        )
        inverse_scheme_transition = datum.transition_on_triple(
            target_index, source_index, third_index
        )
        inverse_pullback = fibered_modules.Mor(source_triple, target_triple)(
            inverse_scheme_transition.coordinate_algebra_morphism(),
            {
                label: _base_change_element(
                    target_pair,
                    target_triple,
                    target_restriction,
                    pair_transition.inverse_pullback()(source_pair.module_generator(label)),
                )
                for label in source_pair.module_generating_set()
            },
        )
        transition = FiniteAtlasModuleTransition(
            triple_scheme_transition.parent().base_category().Core().Mor(
                triple_scheme_transition.domain(),
                triple_scheme_transition.codomain(),
            )(triple_scheme_transition, inverse_scheme_transition),
            source_triple,
            target_triple,
            pullback,
            inverse_pullback,
        )
        self._triple_transitions.append((key, transition))
        return transition

    def _verify_cocycle(self) -> None:
        labels = tuple(self.chart_indices())
        for left, middle, right in combinations(labels, 3):
            left_middle = self.transition_on_triple(left, middle, right).pullback()
            middle_right = self.transition_on_triple(middle, right, left).pullback()
            left_right = self.transition_on_triple(left, right, middle).pullback()
            if left_middle * middle_right != left_right:
                raise ValueError("finite-atlas module transitions fail the triple cocycle")

    def restricted_local_map(self, target_datum, chart_index, other_index, local_map):
        r"""Restrict one chart-linear map to the source-side pair overlap."""
        if target_datum.gluing_datum() is not self.gluing_datum():
            raise ValueError("finite-atlas module maps require one underlying affine atlas")
        chart_index = self.gluing_datum().normalize_chart_index(chart_index)
        other_index = self.gluing_datum().normalize_chart_index(other_index)
        if (
            local_map.domain() is not self.local_module(chart_index)
            or local_map.codomain() is not target_datum.local_module(chart_index)
        ):
            raise ValueError("a local descent map has the wrong chart-module endpoints")
        source_pair = self.pair_module(chart_index, other_index)
        target_pair = target_datum.pair_module(chart_index, other_index)
        overlap = self.gluing_datum().overlap(chart_index, other_index)
        ring_map = overlap.inclusion().coordinate_algebra_morphism()
        return source_pair.module_category().Mor(source_pair, target_pair)(
            {
                label: _base_change_element(
                    target_datum.local_module(chart_index),
                    target_pair,
                    ring_map,
                    local_map(self.local_module(chart_index).module_generator(label)),
                )
                for label in self.local_module(chart_index).module_generating_set()
            }
        )

    def morphism_to(self, target, local_maps):
        return QuasiCoherentSheavesWithChosenDescentDatum(self.scheme()).Mor(
            self.sheaf(),
            target.sheaf(),
        )(local_maps)

    def identity_morphism(self):
        r"""Return the identity morphism of this finite-atlas descent datum."""
        def identity_at(index):
            module = self.local_module(index)
            return module.module_category().Mor(module, module).identity()

        return self.morphism_to(
            self,
            {index: identity_at(index) for index in self.chart_indices()},
        )

    @cached_method
    def sheaf(self):
        r"""Return the quasi-coherent module sheaf represented by this descent datum."""
        return QuasiCoherentSheavesWithChosenDescentDatum(self.scheme())(self)

    def chart_index_set(self):
        return self.gluing_datum().chart_index_set()

    def restrict_scalar_to_chart(self, chart_index, scalar):
        r"""The image of a scalar of the scheme's base ring in the section ring of one chart."""
        ring = self.local_module(chart_index).base_ring()
        return ring.algebra_structure_morphism()(scalar)

    def compatible_local_sections(self, sections):
        r"""Read an indexed family of local sections, checking agreement on every overlap.

        On an overlap ``U_ij`` the target-chart section is transported through
        the semilinear pullback and compared with the source-chart restriction,
        so the comparison uses the two distinct overlap rings rather than
        identifying their presentations.
        """
        atlas = self.gluing_datum()
        components = finite_indexed_family(
            atlas.chart_index_set(),
            lambda index: self.local_module(index)(sections[index]),
            name="Compatible finite-atlas section components",
        )
        for source_index, target_index in atlas.transition_index_set():
            source_value = _base_change_element(
                self.local_module(source_index),
                self.pair_module(source_index, target_index),
                atlas.overlap(source_index, target_index).inclusion().coordinate_algebra_morphism(),
                components[source_index],
            )
            target_value = _base_change_element(
                self.local_module(target_index),
                self.pair_module(target_index, source_index),
                atlas.overlap(target_index, source_index).inclusion().coordinate_algebra_morphism(),
                components[target_index],
            )
            if self.transition(source_index, target_index).pullback()(target_value) != source_value:
                raise ValueError("the finite-atlas local sections do not agree on an overlap")
        return components

    @cached_method
    def local_section_product_construction(self):
        r"""Return the product of chart modules after restriction to the scheme base ring."""
        base = self.scheme().scheme_base_ring()
        factors = finite_indexed_family(
            self.chart_index_set(),
            lambda index: self.local_module(index).restrict_scalars(
                self.gluing_datum().chart(index).coordinate_algebra().algebra_structure_morphism()
            ),
            name="Finite-atlas chart modules over the scheme base ring",
        )
        return Modules(base).product_construction(factors)

    @cached_method
    def matching_section_product_construction(self):
        r"""Return the product of source-side overlap modules over the scheme base ring."""
        base = self.scheme().scheme_base_ring()
        factors = finite_indexed_family(
            self.gluing_datum().transition_index_set(),
            lambda pair: self.pair_module(*pair).restrict_scalars(
                self.gluing_datum().overlap(*pair).coordinate_algebra().algebra_structure_morphism()
            ),
            name="Finite-atlas overlap modules over the scheme base ring",
        )
        return Modules(base).product_construction(factors)

    def _matching_section_leg(self, pair, side):
        r"""One finite-atlas Čech leg from chart sections to a source-side overlap."""
        source_index, target_index = tuple(pair)
        local_product = self.local_section_product_construction()
        matching_product = self.matching_section_product_construction()
        local_factors = local_product.diagram().diagram_objects()
        matching_factor = matching_product.diagram().diagram_objects().value(pair)

        match side:
            case "left":
                chart_index = source_index
                local_module = self.local_module(source_index)
                pair_module = self.pair_module(source_index, target_index)
                ring_map = self.gluing_datum().overlap(
                    source_index,
                    target_index,
                ).inclusion().coordinate_algebra_morphism()

                def image(element):
                    return matching_factor.wrap(
                        _base_change_element(
                            local_module,
                            pair_module,
                            ring_map,
                            element.underlying_element(),
                        )
                    )

            case "right":
                chart_index = target_index
                local_module = self.local_module(target_index)
                pair_module = self.pair_module(target_index, source_index)
                ring_map = self.gluing_datum().overlap(
                    target_index,
                    source_index,
                ).inclusion().coordinate_algebra_morphism()
                transition = self.transition(source_index, target_index).pullback()

                def image(element):
                    target_value = _base_change_element(
                        local_module,
                        pair_module,
                        ring_map,
                        element.underlying_element(),
                    )
                    return matching_factor.wrap(transition(target_value))

            case _:
                raise ValueError("a finite-atlas Čech side is left or right")

        local_factor = local_factors.value(chart_index)
        restriction = local_factor.module_category().Mor(
            local_factor,
            matching_factor,
        ).elementwise(image, verify_linearity=False)
        projection = local_product.structure_morphism(
            local_product.diagram().domain()(chart_index)
        )
        return restriction * projection

    @cached_method
    def compatible_sections_construction(self):
        r"""Return the selected equalizer defining finite-atlas global sections over the base ring."""
        base = self.scheme().scheme_base_ring()
        modules = Modules(base)
        local_product = self.local_section_product_construction()
        matching_product = self.matching_section_product_construction()
        matching_diagram = matching_product.diagram()

        def side_map(side):
            cone = matching_diagram.Cones().cone(
                local_product.object(),
                lambda index: self._matching_section_leg(index.value(), side),
            )
            return matching_product.factor(cone).apex_map()

        return modules.equalizer_construction(
            side_map("left"),
            side_map("right"),
        )

    @cached_method
    def compatible_sections(self):
        r"""Return ``Gamma(X, F)`` over the base ring of the glued scheme."""
        return self.compatible_sections_construction().object()

    def compatible_section(self, sections):
        r"""Construct a finite-atlas global section from compatible chart components."""
        components = self.compatible_local_sections(sections)
        base = self.scheme().scheme_base_ring()
        modules = Modules(base)
        local_product = self.local_section_product_construction()
        factors = local_product.diagram().diagram_objects()
        restricted_components = finite_indexed_family(
            self.chart_index_set(),
            lambda index: factors.value(index)(components[index]),
            name="Finite-atlas section components over the scheme base ring",
        )
        product_element = modules.product_element(local_product, restricted_components)
        return modules.equalizer_element(
            self.compatible_sections_construction(),
            product_element,
        )

    def compatible_section_component(self, section, chart_index):
        r"""Project a finite-atlas global section to one chart component."""
        chart_index = self.gluing_datum().normalize_chart_index(chart_index)
        construction = self.compatible_sections_construction()
        shape = construction.diagram().domain()
        local_element = construction.structure_morphism(shape.source())(section)
        component = Modules(self.scheme().scheme_base_ring()).product_component(
            self.local_section_product_construction(),
            local_element,
            chart_index,
        )
        return self.local_module(chart_index)(component.underlying_element())

    def tensor_product(self, other):
        r"""Return the descent datum for the chartwise tensor product with ``other``."""
        if other.gluing_datum() is not self.gluing_datum():
            raise ValueError("finite-atlas tensor products require one underlying atlas")
        datum = self.gluing_datum()
        local_modules = {
            index: Modules(self.local_module(index).base_ring()).tensor_product(
                (self.local_module(index), other.local_module(index))
            )
            for index in datum.chart_indices()
        }

        def tensor_transition(left_datum, right_datum, source_index, target_index):
            left_transition = left_datum.transition(source_index, target_index).pullback()
            right_transition = right_datum.transition(source_index, target_index).pullback()
            left_source = left_datum.pair_module(target_index, source_index)
            right_source = right_datum.pair_module(target_index, source_index)
            left_target = left_datum.pair_module(source_index, target_index)
            right_target = right_datum.pair_module(source_index, target_index)

            def images(label, _domain, codomain):
                left_label = label.component(0)
                right_label = label.component(1)
                left_image = left_transition(left_source.module_generator(left_label))
                right_image = right_transition(right_source.module_generator(right_label))
                left_coefficients = left_target.framing_coefficients(left_image)
                right_coefficients = right_target.framing_coefficients(right_image)
                coefficients = {}
                for tensor_label in codomain.module_generating_set():
                    coefficient = (
                        left_coefficients.get(tensor_label.component(0), codomain.base_ring().zero())
                        * right_coefficients.get(tensor_label.component(1), codomain.base_ring().zero())
                    )
                    if coefficient:
                        coefficients[tensor_label] = coefficient
                return codomain.linear_combination(coefficients)

            return images

        transitions = {}
        for source_index, target_index in datum.transition_index_set():
            transitions[source_index, target_index] = (
                tensor_transition(self, other, source_index, target_index),
                tensor_transition(self, other, target_index, source_index),
            )
        return FiniteAtlasModuleGluingData(datum)(local_modules, transitions)


class FiniteAtlasModuleGluingMorphism(Morphism):
    r"""A morphism of finite-atlas module descent data.

    One linear map is supplied on every affine chart.  On each pair overlap
    the target pullback after the target-chart map must equal the source-chart
    map after the source pullback as semilinear maps ``M_j -> N_i``.
    """

    def __init__(self, parent, local_maps) -> None:
        Morphism.__init__(self, parent)
        source = self.source_datum()
        target = self.target_datum()
        if source.gluing_datum() is not target.gluing_datum():
            raise ValueError("finite-atlas module morphisms require one underlying affine atlas")
        self._local_maps = _family_on_finite_ordered_set(
            source.gluing_datum().chart_index_set(),
            local_maps,
            name="Local maps of a finite-atlas module morphism",
            noun="finite-atlas local map data",
        )
        for index in source.chart_indices():
            local_map = self._local_maps[index]
            if (
                local_map.domain() is not source.local_module(index)
                or local_map.codomain() is not target.local_module(index)
            ):
                raise ValueError("a finite-atlas local map has the wrong chart-module endpoints")
        self._verify_overlap_compatibility()

    def source_datum(self):
        return self.domain()

    def target_datum(self):
        return self.codomain()

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        index = self.source_datum().gluing_datum().normalize_chart_index(index)
        return self.local_maps()[index]

    def __mul__(self, other):
        match other:
            case FiniteAtlasModuleGluingMorphism() if other.codomain() is self.domain():
                return self.domain().category().Mor(other.domain(), self.codomain())(
                    {
                        index: self.local_map(index) * other.local_map(index)
                        for index in other.source_datum().chart_indices()
                    }
                )
            case _:
                return NotImplemented

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, FiniteAtlasModuleGluingMorphism)
            and other.parent() is self.parent()
            and all(
                other.local_map(index) == self.local_map(index)
                for index in self.source_datum().chart_indices()
            )
        )

    def __ne__(self, other) -> bool:
        return not self == other

    @staticmethod
    def _base_changed_map(local_map, ring_map, source, target):
        r"""Transport ``local_map`` to already selected scalar-extension parents."""
        if source.base_ring() is not ring_map.codomain() or target.base_ring() is not ring_map.codomain():
            raise ValueError("the selected base-changed map endpoints have the wrong scalar ring")
        return source.module_category().Mor(source, target)(
            {
                label: target.linear_combination(
                    {
                        target_label: ring_map(coefficient)
                        for target_label, coefficient in local_map.codomain()
                        .framing_coefficients(
                            local_map(local_map.domain().module_generator(label))
                        )
                        .items()
                        if ring_map(coefficient) != target.base_ring().zero()
                    }
                )
                for label in local_map.domain().module_generating_set()
            }
        )

    def kernel_datum(self):
        r"""Return the finite-atlas descent datum of the sheaf kernel.

        Localization is exact, so the chart kernel restricts to the overlap
        kernel.  The current module-level factorization through a represented
        kernel inclusion is constructive when that kernel has a selected free
        framing; the general finitely presented factorization belongs to the
        common local-module-map owner rather than to sheaf descent.
        """
        datum = self.source_datum().gluing_datum()
        local_kernels = {
            index: self.local_map(index).kernel()
            for index in datum.chart_indices()
        }
        assert all(kernel.is_free() is True for kernel in local_kernels.values()), (
            "finite-atlas kernel descent requires locally free represented kernels; "
            "general finitely presented kernel factorization belongs to local-module-maps"
        )

        def kernel_transition(source_index, target_index):
            source_kernel = local_kernels[source_index]
            target_kernel = local_kernels[target_index]
            source_pair = self.source_datum().pair_module(source_index, target_index)
            target_pair = self.source_datum().pair_module(target_index, source_index)
            source_ring_map = datum.overlap(source_index, target_index).inclusion().coordinate_algebra_morphism()
            target_ring_map = datum.overlap(target_index, source_index).inclusion().coordinate_algebra_morphism()
            ambient_transition = self.source_datum().transition(source_index, target_index).pullback()

            def images(label, domain, codomain):
                target_inclusion = self._base_changed_map(
                    target_kernel.inclusion(),
                    target_ring_map,
                    domain,
                    target_pair,
                )
                source_inclusion = self._base_changed_map(
                    source_kernel.inclusion(),
                    source_ring_map,
                    codomain,
                    source_pair,
                )
                ambient_image = ambient_transition(
                    target_inclusion(domain.module_generator(label))
                )
                return source_inclusion.lift(ambient_image)

            return images

        transitions = {}
        for source_index, target_index in datum.transition_index_set():
            transitions[source_index, target_index] = (
                kernel_transition(source_index, target_index),
                kernel_transition(target_index, source_index),
            )
        return FiniteAtlasModuleGluingData(datum)(local_kernels, transitions)

    def cokernel_datum(self):
        r"""Return the finite-atlas descent datum of the sheaf cokernel."""
        datum = self.target_datum().gluing_datum()
        local_projections = {
            index: self.local_map(index).cokernel_projection()
            for index in datum.chart_indices()
        }
        local_cokernels = {
            index: local_projections[index].codomain()
            for index in datum.chart_indices()
        }

        def cokernel_transition(source_index, target_index):
            source_pair = self.target_datum().pair_module(source_index, target_index)
            target_pair = self.target_datum().pair_module(target_index, source_index)
            source_ring_map = datum.overlap(source_index, target_index).inclusion().coordinate_algebra_morphism()
            ambient_transition = self.target_datum().transition(source_index, target_index).pullback()

            def images(label, domain, codomain):
                source_projection = self._base_changed_map(
                    local_projections[source_index],
                    source_ring_map,
                    source_pair,
                    codomain,
                )
                representative = target_pair.module_generator(label)
                return source_projection(ambient_transition(representative))

            return images

        transitions = {}
        for source_index, target_index in datum.transition_index_set():
            transitions[source_index, target_index] = (
                cokernel_transition(source_index, target_index),
                cokernel_transition(target_index, source_index),
            )
        return FiniteAtlasModuleGluingData(datum)(local_cokernels, transitions)

    def stalk_map(self, chart_index, point):
        r"""Return the induced map on the stalk at ``point`` of one affine chart."""
        chart_index = self.source_datum().gluing_datum().normalize_chart_index(chart_index)
        chart = self.source_datum().gluing_datum().chart(chart_index)
        spectrum = chart.underlying_space()
        if point.parent() is not spectrum:
            raise ValueError("a finite-atlas stalk point belongs to the selected affine chart")
        localization = point.local_ring().localization_functor()
        return localization(self.local_map(chart_index))

    def kernel_sheaf(self):
        return self.kernel_datum().sheaf()

    def cokernel_sheaf(self):
        return self.cokernel_datum().sheaf()

    def _verify_overlap_compatibility(self) -> None:
        source = self.source_datum()
        target = self.target_datum()
        for source_index, target_index in source.gluing_datum().transition_index_set():
            source_transition = source.transition(source_index, target_index)
            target_transition = target.transition(source_index, target_index)
            source_side = source.restricted_local_map(
                target,
                source_index,
                target_index,
                self.local_map(source_index),
            )
            target_side = source.restricted_local_map(
                target,
                target_index,
                source_index,
                self.local_map(target_index),
            )
            left = target_transition.pullback() * SemilinearModuleMorphism.from_linear(
                target_side
            )
            right = SemilinearModuleMorphism.from_linear(source_side) * source_transition.pullback()
            if left != right:
                raise ValueError(
                    "finite-atlas local module maps are incompatible with an overlap transition"
                )


class FiniteAtlasModuleSheafMorphism(FiniteAtlasModuleGluingMorphism):
    r"""The sheaf-endpoint realization of a finite-atlas descent morphism."""

    def source_datum(self):
        return self.domain().gluing_datum()

    def target_datum(self):
        return self.codomain().gluing_datum()


class FiniteAtlasModuleSheafHomset(CategoricalHomset):
    r"""The represented Hom between two finite-atlas module sheaves."""

    Element = FiniteAtlasModuleSheafMorphism

    def _element_constructor_(self, local_maps):
        match local_maps:
            case FiniteAtlasModuleSheafMorphism() if local_maps.parent() is self:
                return local_maps
            case FiniteAtlasModuleSheafMorphism():
                if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                    raise ValueError("a finite-atlas sheaf morphism keeps its represented endpoints")
                local_maps = local_maps.local_maps()
            case _:
                pass
        return self.element_class(self, local_maps)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom")
        datum = self.domain().gluing_datum()
        return self(
            {
                index: datum.local_module(index).module_category()
                .Mor(datum.local_module(index), datum.local_module(index))
                .identity()
                for index in datum.chart_indices()
            }
        )


class FiniteAtlasModuleSheafHomCategoryConstruction(HomCategoryConstruction):
    r"""Hom family for finite-atlas module sheaves with chosen descent data."""

    def fixed_category_class(self):
        return FiniteAtlasModuleSheafHomset


class FiniteAtlasModuleGluingHomset(CategoricalHomset):
    r"""Compatible local maps between two module descent data on one finite atlas."""

    Element = FiniteAtlasModuleGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.gluing_datum() is not codomain.gluing_datum():
            raise ValueError("a finite-atlas module descent Hom uses one atlas")
        super().__init__(family, domain, codomain)

    def _element_constructor_(self, local_maps):
        match local_maps:
            case FiniteAtlasModuleGluingMorphism() if local_maps.parent() is self:
                return local_maps
            case FiniteAtlasModuleGluingMorphism():
                if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                    raise ValueError("the module descent morphism has the wrong endpoints")
                local_maps = local_maps.local_maps()
            case _:
                pass
        return self.element_class(self, local_maps)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a descent endomorphism Hom")
        datum = self.domain()
        return self(
            {
                index: datum.local_module(index).module_category()
                .Mor(datum.local_module(index), datum.local_module(index))
                .identity()
                for index in datum.chart_indices()
            }
        )


class FiniteAtlasModuleGluingHomCategoryConstruction(HomCategoryConstruction):
    r"""The Hom family of finite-atlas module descent data."""

    def fixed_category_class(self):
        return FiniteAtlasModuleGluingHomset


class FiniteAtlasModuleGluingData(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""Module descent data on one owned finite affine atlas.

    The atlas is the cover parameter.  Objects retain finitely framed local
    modules and semilinear transition isomorphisms satisfying the represented
    triple-overlap cocycle; morphisms are compatible local linear maps.  Thus
    this is the finite-atlas specialization of ``DescentDataOnCover`` rather
    than a host record carrying a private gluing presentation.
    """

    _HomCategory = FiniteAtlasModuleGluingHomCategoryConstruction

    @staticmethod
    def __classcall__(cls, atlas):
        return OwnedParameterizedCategory.__classcall__(cls, atlas)

    def __init__(self, atlas) -> None:
        OwnedParameterizedCategory.__init__(self, atlas)

    def parameter_category(self):
        return FiniteAffineAtlases(self.atlas().scheme())

    def atlas(self):
        return self.base()

    cover = atlas

    def super_categories(self):
        return [DescentDataOnCover(self.atlas().coverage(), self.atlas())]

    def object(self, local_modules, transitions):
        return _object_of(
            self,
            _engine=(self, _FiniteAtlasModuleGluingDatumEngine, None),
            gluing_datum=self.atlas(),
            local_modules=local_modules,
            transitions=transitions,
        )

    __call__ = object

    def an_object(self):
        atlas = self.atlas()
        local_modules = {
            index: atlas.chart(index).coordinate_algebra().free_module(1)
            for index in atlas.chart_indices()
        }

        def identity_images(label, _domain, codomain):
            return codomain.module_generator(label)

        transitions = {
            pair: (identity_images, identity_images)
            for pair in atlas.transition_index_set()
        }
        return self(local_modules, transitions)


class _FiniteAtlasAlgebraGluingDatumEngine:
    r"""Algebra descent on a finite affine atlas with distinct overlap rings."""

    def __init__(self, gluing_datum, local_algebras, transitions, **rest) -> None:
        self._gluing_datum = gluing_datum
        indices = gluing_datum.chart_index_set()
        self._local_algebras = _family_on_finite_ordered_set(
            indices, local_algebras,
            name="Local algebras of finite-atlas descent",
            noun="finite-atlas local algebra data",
        )
        for index in indices:
            algebra = self._local_algebras[index]
            ring = gluing_datum.chart(index).coordinate_algebra()
            if algebra.base_ring() is not ring:
                raise ValueError("each finite-atlas local algebra must be defined over its chart coordinate algebra")
            _finite_algebra_framing(algebra)
        self._transition_data = _family_on_finite_ordered_set(
            gluing_datum.transition_index_set(), transitions,
            name="Semilinear algebra transition data of a finite atlas",
            noun="finite-atlas algebra transition data",
        )
        self._pair_algebras = []
        self._triple_algebras = []
        self._transitions = []
        self._triple_transitions = []
        super().__init__(**rest)
        for pair in gluing_datum.transition_index_set():
            self.transition(*pair)
        self._verify_cocycle()

    def gluing_datum(self):
        return self._gluing_datum

    def scheme(self):
        return self.gluing_datum().scheme()

    def chart_indices(self):
        return self.gluing_datum().chart_indices()

    def local_algebras(self):
        return self._local_algebras

    def local_algebra(self, index):
        return self.local_algebras()[self.gluing_datum().normalize_chart_index(index)]

    def pair_algebra(self, chart_index, other_index):
        datum = self.gluing_datum()
        chart_index = datum.normalize_chart_index(chart_index)
        other_index = datum.normalize_chart_index(other_index)
        key = (chart_index, other_index)
        for cached_key, cached in self._pair_algebras:
            if cached_key == key:
                return cached
        overlap = datum.overlap(chart_index, other_index)
        ring_map = overlap.inclusion().coordinate_algebra_morphism()
        algebra = (
            Algebras(ring_map.domain())
            .Associative()
            .Unital()
            .scalar_extension(ring_map)(self.local_algebra(chart_index))
        )
        self._pair_algebras.append((key, algebra))
        return algebra

    def triple_algebra(self, chart_index, first_other, second_other):
        datum = self.gluing_datum()
        chart_index = datum.normalize_chart_index(chart_index)
        ranking = datum.chart_index_set().ranking_map()
        others = tuple(sorted((datum.normalize_chart_index(first_other), datum.normalize_chart_index(second_other)), key=ranking))
        key = (chart_index, *others)
        for cached_key, cached in self._triple_algebras:
            if cached_key == key:
                return cached
        triple = datum.triple_overlap(chart_index, *others)
        ring_map = triple.inclusion().coordinate_algebra_morphism()
        algebra = (
            Algebras(ring_map.domain())
            .Associative()
            .Unital()
            .scalar_extension(ring_map)(self.local_algebra(chart_index))
        )
        self._triple_algebras.append((key, algebra))
        return algebra

    def _transition_images(self, source_index, target_index):
        datum = self.gluing_datum()
        pair = datum._ordered_pair(source_index, target_index)
        pullback_images, inverse_images = self._transition_data[pair]
        if pair == (datum.normalize_chart_index(source_index), datum.normalize_chart_index(target_index)):
            return pullback_images, inverse_images
        return inverse_images, pullback_images

    @staticmethod
    def _images(domain, codomain, specification):
        labels = domain.algebra_generating_set()
        if callable(specification):
            return {label: specification(label, domain, codomain) for label in labels}
        supplied = dict(specification)
        if set(supplied) != set(labels):
            raise ValueError("algebra transition coordinates require one image per source generator")
        return {label: codomain(supplied[label]) for label in labels}

    def transition(self, source_index, target_index):
        datum = self.gluing_datum()
        source_index = datum.normalize_chart_index(source_index)
        target_index = datum.normalize_chart_index(target_index)
        key = (source_index, target_index)
        for cached_key, cached in self._transitions:
            if cached_key == key:
                return cached
        scheme_transition = datum.transition_between(source_index, target_index)
        source = self.pair_algebra(source_index, target_index)
        target = self.pair_algebra(target_index, source_index)
        pullback_images, inverse_images = self._transition_images(source_index, target_index)
        pullback = SemilinearAlgebraMorphism(
            target, source, scheme_transition.forward().coordinate_algebra_morphism(),
            self._images(target, source, pullback_images),
        )
        inverse_pullback = SemilinearAlgebraMorphism(
            source, target, scheme_transition.inverse().coordinate_algebra_morphism(),
            self._images(source, target, inverse_images),
        )
        transition = FiniteAtlasAlgebraTransition(scheme_transition, source, target, pullback, inverse_pullback)
        self._transitions.append((key, transition))
        return transition

    def _restriction(self, chart_index, first_other, second_other):
        pair = self.pair_algebra(chart_index, first_other)
        triple = self.triple_algebra(chart_index, first_other, second_other)
        pair_open = self.gluing_datum().overlap(chart_index, first_other)
        triple_open = self.gluing_datum().triple_overlap(chart_index, first_other, second_other)
        ring_map = pair_open.corestriction(triple_open.inclusion()).coordinate_algebra_morphism()
        return SemilinearAlgebraMorphism(
            pair, triple, ring_map,
            {label: triple.algebra_generator(label) for label in pair.algebra_generating_set()},
        )

    def transition_on_triple(self, source_index, target_index, third_index):
        datum = self.gluing_datum()
        source_index = datum.normalize_chart_index(source_index)
        target_index = datum.normalize_chart_index(target_index)
        third_index = datum.normalize_chart_index(third_index)
        key = (source_index, target_index, third_index)
        for cached_key, cached in self._triple_transitions:
            if cached_key == key:
                return cached
        pair_transition = self.transition(source_index, target_index)
        source_pair = pair_transition.source_algebra()
        target_pair = pair_transition.target_algebra()
        source_triple = self.triple_algebra(source_index, target_index, third_index)
        target_triple = self.triple_algebra(target_index, source_index, third_index)
        source_restriction = self._restriction(source_index, target_index, third_index)
        target_restriction = self._restriction(target_index, source_index, third_index)
        triple_scheme_transition = datum.transition_on_triple(source_index, target_index, third_index)
        pullback = SemilinearAlgebraMorphism(
            target_triple, source_triple, triple_scheme_transition.coordinate_algebra_morphism(),
            {
                label: source_restriction(pair_transition.pullback()(target_pair.algebra_generator(label)))
                for label in target_triple.algebra_generating_set()
            },
        )
        inverse_scheme_transition = datum.transition_on_triple(target_index, source_index, third_index)
        inverse_pullback = SemilinearAlgebraMorphism(
            source_triple, target_triple, inverse_scheme_transition.coordinate_algebra_morphism(),
            {
                label: target_restriction(pair_transition.inverse_pullback()(source_pair.algebra_generator(label)))
                for label in source_triple.algebra_generating_set()
            },
        )
        transition = FiniteAtlasAlgebraTransition(
            triple_scheme_transition.parent().base_category().Core().Mor(
                triple_scheme_transition.domain(),
                triple_scheme_transition.codomain(),
            )(triple_scheme_transition, inverse_scheme_transition),
            source_triple, target_triple, pullback, inverse_pullback,
        )
        self._triple_transitions.append((key, transition))
        return transition

    def _verify_cocycle(self) -> None:
        labels = tuple(self.chart_indices())
        for left, middle, right in combinations(labels, 3):
            left_middle = self.transition_on_triple(left, middle, right).pullback()
            middle_right = self.transition_on_triple(middle, right, left).pullback()
            left_right = self.transition_on_triple(left, right, middle).pullback()
            if left_middle * middle_right != left_right:
                raise ValueError("finite-atlas algebra transitions fail the triple cocycle")

    def restricted_local_map(self, target_datum, chart_index, other_index, local_map):
        if target_datum.gluing_datum() is not self.gluing_datum():
            raise ValueError("finite-atlas algebra maps require one underlying affine atlas")
        datum = self.gluing_datum()
        chart_index = datum.normalize_chart_index(chart_index)
        other_index = datum.normalize_chart_index(other_index)
        if (
            local_map.domain() is not self.local_algebra(chart_index)
            or local_map.codomain() is not target_datum.local_algebra(chart_index)
        ):
            raise ValueError("a local algebra-descent map has the wrong chart endpoints")
        source_pair = self.pair_algebra(chart_index, other_index)
        target_pair = target_datum.pair_algebra(chart_index, other_index)
        overlap = datum.overlap(chart_index, other_index)
        ring_map = overlap.inclusion().coordinate_algebra_morphism()
        extended_map = (
            Algebras(ring_map.domain())
            .Associative()
            .Unital()
            .scalar_extension(ring_map)(local_map)
        )
        extended_source = extended_map.domain()
        return _algebra_homset(source_pair, target_pair)(
            {
                label: target_pair(
                    extended_map(extended_source.algebra_generator(label))
                )
                for label in source_pair.algebra_generating_set()
            }
        )

    def morphism_to(self, target, local_maps):
        return self.category().Mor(self, target)(local_maps)

    def relative_spectrum(self, *, _engine=None, construction_data=None):
        from dzack_research.preamble.categories.schemes.relative_spec import (
            _finite_atlas_relative_spectrum,
        )

        return _finite_atlas_relative_spectrum(
            self,
            _engine=_engine,
            construction_data=construction_data,
        )


class FiniteAtlasAlgebraGluingMorphism(Morphism):
    r"""A morphism of finite-atlas algebra descent data."""

    def __init__(self, parent, local_maps) -> None:
        Morphism.__init__(self, parent)
        source = self.domain()
        target = self.codomain()
        if source.gluing_datum() is not target.gluing_datum():
            raise ValueError("finite-atlas algebra morphisms require one underlying affine atlas")
        self._local_maps = _family_on_finite_ordered_set(
            source.gluing_datum().chart_index_set(),
            local_maps,
            name="Local maps of a finite-atlas algebra morphism",
            noun="finite-atlas local algebra map data",
        )
        for index in source.chart_indices():
            local_map = self._local_maps[index]
            if (
                local_map.domain() is not source.local_algebra(index)
                or local_map.codomain() is not target.local_algebra(index)
            ):
                raise ValueError("a finite-atlas local algebra map has the wrong chart endpoints")
        self._verify_overlap_compatibility()

    def source(self):
        return self.domain()

    def target(self):
        return self.codomain()

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[self.source().gluing_datum().normalize_chart_index(index)]

    def __mul__(self, other):
        match other:
            case FiniteAtlasAlgebraGluingMorphism() if other.codomain() is self.domain():
                return self.domain().category().Mor(other.domain(), self.codomain())(
                    {
                        index: self.local_map(index) * other.local_map(index)
                        for index in other.source().chart_indices()
                    }
                )
            case _:
                return NotImplemented

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, FiniteAtlasAlgebraGluingMorphism)
            and other.parent() is self.parent()
            and all(
                other.local_map(index) == self.local_map(index)
                for index in self.source().chart_indices()
            )
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def _verify_overlap_compatibility(self) -> None:
        for source_index, target_index in self.source().gluing_datum().transition_index_set():
            source_transition = self.source().transition(source_index, target_index)
            target_transition = self.target().transition(source_index, target_index)
            source_side = self.source().restricted_local_map(
                self.target(), source_index, target_index, self.local_map(source_index)
            )
            target_side = self.source().restricted_local_map(
                self.target(), target_index, source_index, self.local_map(target_index)
            )
            left = target_transition.pullback() * SemilinearAlgebraMorphism.from_linear(
                target_side
            )
            right = SemilinearAlgebraMorphism.from_linear(source_side) * source_transition.pullback()
            if left != right:
                raise ValueError(
                    "finite-atlas local algebra maps are incompatible with an overlap transition"
                )


class FiniteAtlasAlgebraGluingHomset(CategoricalHomset):
    r"""Compatible local algebra maps between two descent data on one finite atlas."""

    Element = FiniteAtlasAlgebraGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.gluing_datum() is not codomain.gluing_datum():
            raise ValueError("a finite-atlas algebra descent Hom uses one atlas")
        super().__init__(family, domain, codomain)

    def _element_constructor_(self, local_maps):
        match local_maps:
            case FiniteAtlasAlgebraGluingMorphism() if local_maps.parent() is self:
                return local_maps
            case FiniteAtlasAlgebraGluingMorphism():
                if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                    raise ValueError("the algebra descent morphism has the wrong endpoints")
                local_maps = local_maps.local_maps()
            case _:
                pass
        return self.element_class(self, local_maps)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a descent endomorphism Hom")
        datum = self.domain()
        return self(
            {
                index: _algebra_homset(
                    datum.local_algebra(index),
                    datum.local_algebra(index),
                ).identity()
                for index in datum.chart_indices()
            }
        )


class FiniteAtlasAlgebraGluingHomCategoryConstruction(HomCategoryConstruction):
    r"""The Hom family of finite-atlas algebra descent data."""

    def fixed_category_class(self):
        return FiniteAtlasAlgebraGluingHomset


class FiniteAtlasAlgebraGluingData(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""Unital associative algebra descent data on one finite affine atlas."""

    _HomCategory = FiniteAtlasAlgebraGluingHomCategoryConstruction

    @staticmethod
    def __classcall__(cls, atlas):
        return OwnedParameterizedCategory.__classcall__(cls, atlas)

    def __init__(self, atlas) -> None:
        OwnedParameterizedCategory.__init__(self, atlas)

    def parameter_category(self):
        return FiniteAffineAtlases(self.atlas().scheme())

    def atlas(self):
        return self.base()

    cover = atlas

    def super_categories(self):
        return [DescentDataOnCover(self.atlas().coverage(), self.atlas())]

    def object(self, local_algebras, transitions):
        return _object_of(
            self,
            _engine=(self, _FiniteAtlasAlgebraGluingDatumEngine, None),
            gluing_datum=self.atlas(),
            local_algebras=local_algebras,
            transitions=transitions,
        )

    __call__ = object

    def an_object(self):
        r"""Polynomial-algebra descent with identity transition on the selected atlas."""
        atlas = self.atlas()
        local_algebras = {
            index: atlas.chart(index)
            .coordinate_algebra()
            .free_module(("z",))
            .symmetric_algebra()
            for index in atlas.chart_indices()
        }

        def identity_images(label, _domain, codomain):
            return codomain.algebra_generator(label)

        transitions = {
            pair: (identity_images, identity_images)
            for pair in atlas.transition_index_set()
        }
        return self(local_algebras, transitions)


def _cover_chart_family(cover, values, *, name):
    r"""Read finite chart data on ``cover`` as the family ``i |-> values_i`` on its atlas.

    The charts of a distinguished affine cover are labelled by their
    positions, so a finite sequence of values and a family already indexed by
    the atlas are both read at the position of each label.
    """
    supplied = finite_family(values, name=name)
    family = finite_indexed_family(
        cover.atlas(),
        lambda label: supplied[cover.chart_position(label)],
        name=name,
    )
    if supplied.cardinality() != family.cardinality():
        raise ValueError(f"{name} needs exactly one entry on each affine chart")
    return family


def _cover_pair_family(cover, transitions, *, noun):
    r"""Read transition data on ``cover`` as a family on its unordered pairs of charts."""
    normalized = {
        _chart_pair(cover, left, right): transition
        for (left, right), transition in dict(transitions).items()
    }
    expected = tuple(combinations(tuple(cover.atlas()), 2))
    if set(normalized) != set(expected):
        raise ValueError(
            f"{noun} requires one transition isomorphism for each pair of charts {expected}"
        )
    return finite_indexed_family(
        finite_ordered_set(expected),
        lambda pair: normalized[pair],
        name=f"Transition isomorphisms of {noun}",
    )


def _restriction_scalar_map(cover, labels):
    r"""``O(X) -> O(U_I)``, the structure-sheaf restriction to a cover intersection."""
    scheme = cover.ambient_scheme()
    return scheme.structure_sheaf().restriction_map(scheme, cover.intersection(*labels))


class ModuleGluingHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return ModuleGluingHomset


class _ModuleGluingSheafEngine:
    r"""Private realization of a module sheaf with one chosen affine descent presentation."""

    def __init__(self, module_gluing_datum, **rest) -> None:
        self._module_gluing_datum = module_gluing_datum
        super().__init__(**rest)

    def gluing_datum(self):
        return self._module_gluing_datum

    def cover(self):
        return self.gluing_datum().cover()

    def ringed_space(self):
        return self.gluing_datum().scheme()

    scheme = ringed_space

    def sections_on_chart(self, index):
        return self.gluing_datum().local_module(index)

    local_module = sections_on_chart

    def sections_on_intersection(self, chart_index, *intersection_indices):
        return self.gluing_datum().restricted_module(
            chart_index, *intersection_indices
        )

    def transition(self, source_index, target_index):
        return self.gluing_datum().transition(source_index, target_index)

    def global_sections(self):
        return self.gluing_datum().compatible_sections()


class ModuleGluingData(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""Descent data for modules on one distinguished affine cover.

    For ``X = Spec A`` covered by ``U_i = D(f_i)``, an object is a family of
    ``O(U_i)``-modules ``M_i`` with isomorphisms of ``O(U_ij)``-modules
    ``phi_ij : M_i|_{U_ij} -> M_j|_{U_ij}`` satisfying
    ``phi_jk phi_ij = phi_ik`` on every triple overlap ``U_ijk``.  A morphism
    is a family of ``O(U_i)``-linear maps commuting with the transitions.

    ``ModuleGluingData(cover)(local_modules, transitions)`` is the one entry.
    Each ``M_i`` is required to carry a finite framing, which is the
    hypothesis under which the transition identities and the cocycle are
    decided on generators.
    """

    @staticmethod
    def __classcall__(cls, cover):
        return OwnedParameterizedCategory.__classcall__(cls, cover)

    def __init__(self, cover) -> None:
        OwnedParameterizedCategory.__init__(self, cover)

    def parameter_category(self):
        return DistinguishedAffineCovers()

    def cover(self):
        return self.base()

    def super_categories(self):
        return [DescentDataOnCover(self.cover().coverage(), self.cover())]

    def an_object(self):
        r"""The descent datum of ``O_X``: each ``O(U_i)`` as a free module of rank one."""
        cover = self.cover()
        local_modules = finite_indexed_family(
            cover.atlas(),
            lambda label: cover.open(label).coordinate_algebra().free_module(1),
            name="Rank-one free chart modules",
        )

        def identity_transition(left, right):
            source = cover.restrict_module(local_modules[left], left, right)
            target = cover.restrict_module(local_modules[right], right, left)
            forward = source.module_category().Mor(source, target)(target.module_generator)
            inverse = target.module_category().Mor(target, source)(source.module_generator)
            return source.module_category().Core().Mor(source, target)(forward, inverse)

        return self(
            local_modules,
            {
                (left, right): identity_transition(left, right)
                for left, right in combinations(tuple(cover.atlas()), 2)
            },
        )

    def object(self, local_modules, transitions):
        r"""The module descent datum ``(M_i, phi_ij)`` on this cover."""
        cover = self.cover()
        return _object_of(
            self,
            local_modules=_cover_chart_family(
                cover,
                local_modules,
                name="Local modules of module descent",
            ),
            transitions=_cover_pair_family(cover, transitions, noun="module gluing"),
        )

    __call__ = object

    def _repr_object_names(self):
        return f"module descent data on {self.cover()}"

    _HomCategory = ModuleGluingHomCategoryConstruction

    class ParentMethods:
        def __init__(self, local_modules, transitions, **rest) -> None:
            self._local_modules = local_modules
            self._transitions = transitions
            super().__init__(**rest)
            for label in self.chart_index_set():
                if self.local_module(label).base_ring() is not self.cover().open(label).coordinate_algebra():
                    raise ValueError("each local module must be defined over its chart section ring")
                _finite_framing(self.local_module(label))
            self._verify_pairwise_transitions()
            self._verify_cocycles()

        def cover(self):
            return self.category().cover()

        def ringed_space(self):
            return self.cover().ambient_scheme()

        scheme = ringed_space

        def chart_index_set(self):
            r"""The atlas of the cover, which labels the charts of this datum."""
            return self.cover().atlas()

        def local_modules(self):
            return self._local_modules

        def local_module(self, index):
            return self.local_modules()[self.cover().chart_label(index)]

        def restricted_module(self, chart_index, *intersection_indices):
            return self.cover().restrict_module(
                self.local_module(chart_index),
                chart_index,
                *intersection_indices,
            )

        def transition(self, source_index, target_index):
            r"""Return the represented overlap isomorphism from one chart to another."""
            pair = _chart_pair(self.cover(), source_index, target_index)
            if pair == (self.cover().chart_label(source_index), self.cover().chart_label(target_index)):
                return self._transitions[pair]
            return self._reversed_transition(pair)

        @cached_method
        def _reversed_transition(self, pair):
            r"""``phi_ij^{-1}``, the isomorphism of the pair read from ``j`` to ``i``."""
            original = self._transitions[pair]
            source = original.codomain()
            target = original.domain()
            return source.module_category().Core().Mor(source, target)(
                original.inverse(),
                original.forward(),
            )

        def _verify_pairwise_transitions(self) -> None:
            for pair in self._transitions.index_set():
                left, right = pair
                transition = self._transitions[pair]
                source = self.restricted_module(left, left, right)
                target = self.restricted_module(right, left, right)
                if transition not in source.module_category().Core().Mor(source, target):
                    raise TypeError(
                        "a module transition is an isomorphism between the restrictions of its two local modules to the overlap"
                    )
                forward = transition.forward()
                inverse = transition.inverse()
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
            chart = self.cover().chart_label(chart_index)
            return self.restriction_between_intersections(
                chart,
                (chart,),
                self.cover().intersection_indices(chart, *intersection_indices),
            )

        def restriction_between_intersections(self, chart_index, source_indices, target_indices):
            r"""Return ``M_i|U_I -> Res(M_i|U_J)`` for ``U_J subseteq U_I``."""
            cover = self.cover()
            chart = cover.chart_label(chart_index)
            return self._restriction_between(
                chart,
                cover.intersection_indices(chart, *tuple(source_indices)),
                cover.intersection_indices(chart, *tuple(target_indices)),
            )

        @cached_method
        def _restriction_between(self, chart, source_labels, target_labels):
            if not set(source_labels).issubset(target_labels):
                raise ValueError("module restriction requires the target intersection to refine the source")
            source = self.restricted_module(chart, *source_labels)
            target = self.restricted_module(chart, *target_labels)
            if target is source:
                return source.module_category().Mor(source, source).identity()
            source_open = self.cover().intersection(*source_labels)
            target_open = self.cover().intersection(*target_labels)
            ring_map = self.scheme().structure_sheaf().restriction_map(source_open, target_open)
            restricted_target = target.restrict_scalars(ring_map)
            return source.module_category().Mor(source, restricted_target)(
                lambda label: restricted_target.wrap(target.module_generator(label))
            )

        def restrict_section(self, chart_index, section, *intersection_indices):
            r"""Restrict one local section to the selected cover intersection."""
            chart = self.cover().chart_label(chart_index)
            return self.restrict_section_between_intersections(
                chart,
                section,
                (chart,),
                self.cover().intersection_indices(chart, *intersection_indices),
            )

        def restrict_section_between_intersections(self, chart_index, section, source_indices, target_indices):
            r"""Restrict a section living on one represented cover intersection to a smaller one.

            The restriction lands in the restriction of scalars of the smaller
            intersection's module; the section is read back in that module
            itself.  When the two intersections are one open, the restriction
            is the identity of its module.
            """
            cover = self.cover()
            chart = cover.chart_label(chart_index)
            source_labels = cover.intersection_indices(chart, *tuple(source_indices))
            target_labels = cover.intersection_indices(chart, *tuple(target_indices))
            source = self.restricted_module(chart, *source_labels)
            target = self.restricted_module(chart, *target_labels)
            image = self._restriction_between(chart, source_labels, target_labels)(source(section))
            if target is source:
                return image
            return image.underlying_element()

        def transition_on_intersection(self, source_index, target_index, *intersection_indices):
            r"""Restrict a pairwise transition to a finer represented intersection."""
            cover = self.cover()
            source = cover.chart_label(source_index)
            target = cover.chart_label(target_index)
            return self._transition_on(
                source,
                target,
                cover.intersection_indices(source, target, *intersection_indices),
            )

        @cached_method
        def _transition_on(self, source_label, target_label, labels):
            cover = self.cover()
            pair = cover.intersection_indices(source_label, target_label)
            transition = self.transition(source_label, target_label).forward()
            if labels == pair:
                return transition
            pair_open = cover.intersection(*pair)
            target_open = cover.intersection(*labels)
            ring_map = self.scheme().structure_sheaf().restriction_map(pair_open, target_open)
            pair_source = self.restricted_module(source_label, *pair)
            pair_target = self.restricted_module(target_label, *pair)
            source = self.restricted_module(source_label, *labels)
            target = self.restricted_module(target_label, *labels)
            return source.module_category().Mor(source, target)(
                lambda label: _base_change_element(
                    pair_target,
                    target,
                    ring_map,
                    transition(pair_source.module_generator(label)),
                )
            )

        def _verify_cocycles(self) -> None:
            for left, middle, right in combinations(tuple(self.chart_index_set()), 3):
                labels = (left, middle, right)
                composite = self.transition_on_intersection(middle, right, *labels) * self.transition_on_intersection(left, middle, *labels)
                if not _maps_agree_on_framing(composite, self.transition_on_intersection(left, right, *labels)):
                    raise ValueError("module transition isomorphisms fail the cocycle condition on a triple overlap")

        def restrict_scalar_to_chart(self, chart_index, scalar):
            r"""The image of ``scalar in O(X)`` in the section ring ``O(U_i)`` of one chart."""
            chart = self.cover().chart_label(chart_index)
            return _restriction_scalar_map(self.cover(), (chart,))(scalar)

        def compatible_local_sections(self, sections):
            r"""Read an indexed family of local sections, checking agreement on every overlap.

            ``(s_i)`` is a global section exactly when
            ``phi_ij(s_i|_{U_ij}) = s_j|_{U_ij}`` for every pair of charts.
            """
            components = finite_indexed_family(
                self.chart_index_set(),
                lambda label: self.local_module(label)(sections[label]),
                name="Compatible local sections",
            )
            for left, right in combinations(tuple(self.chart_index_set()), 2):
                restricted_left = self.restrict_section(left, components[left], left, right)
                restricted_right = self.restrict_section(right, components[right], left, right)
                if self.transition(left, right).forward()(restricted_left) != restricted_right:
                    raise ValueError("the local sections do not agree under the overlap transition")
            return components

        @cached_method
        def local_section_product_construction(self):
            r"""Return ``prod_i F(U_i)`` in ``Modules(O(X))`` with its projections."""
            presheaf = self.descent_presheaf()
            values = finite_indexed_family(
                self.chart_index_set(),
                lambda label: presheaf.value_on_label((label,)),
                name="Čech chart modules over O(X)",
            )
            return Modules(self.scheme().coordinate_algebra()).product_construction(values)

        @cached_method
        def matching_section_product_construction(self):
            r"""Return ``prod_{i<j} F(U_ij)`` in ``Modules(O(X))``."""
            pair_indices = self.cover().cech_covering_family().pair_index_set()
            presheaf = self.descent_presheaf()
            values = finite_indexed_family(
                pair_indices,
                lambda pair: presheaf.value_on_label(tuple(pair)),
                name="Čech overlap modules over O(X)",
            )
            return Modules(self.scheme().coordinate_algebra()).product_construction(values)

        def _local_overlap_leg(self, pair, side):
            r"""One leg ``prod_i F(U_i) -> F(U_ij)`` of the Čech parallel pair."""
            pair = tuple(pair)
            match side:
                case "left":
                    chart = pair[0]
                case "right":
                    chart = pair[1]
                case _:
                    raise ValueError("a Čech overlap side is left or right")
            presheaf = self.descent_presheaf()
            local_product = self.local_section_product_construction()
            projection = local_product.structure_morphism(
                local_product.diagram().domain()(chart)
            )
            return presheaf.restriction_between_labels((chart,), pair) * projection

        @cached_method
        def compatible_sections_construction(self):
            r"""Return the selected Čech equalizer defining ``Gamma(X,F)`` in ``Modules(O(X))``."""
            modules = Modules(self.scheme().coordinate_algebra())
            local_product = self.local_section_product_construction()
            local_object = local_product.object()
            matching_product = self.matching_section_product_construction()
            matching_diagram = matching_product.diagram()

            def side_map(side):
                cone = matching_diagram.Cones().cone(
                    local_object,
                    lambda index: self._local_overlap_leg(index.value(), side),
                )
                return matching_product.factor(cone).apex_map()

            return modules.equalizer_construction(
                side_map("left"),
                side_map("right"),
            )

        @cached_method
        def compatible_sections(self):
            r"""Return ``Gamma(X, F)``, the ``O(X)``-module of compatible local sections."""
            return self.compatible_sections_construction().object()

        def compatible_section(self, sections):
            r"""Construct a global section from one compatible family of local sections."""
            components = self.compatible_local_sections(sections)
            modules = Modules(self.scheme().coordinate_algebra())
            local_product = self.local_section_product_construction()
            factors = local_product.diagram().diagram_objects()
            restricted_components = finite_indexed_family(
                self.chart_index_set(),
                lambda label: factors.value(label)(components[label]),
                name="Restricted-scalar components of a global section",
            )
            product_element = modules.product_element(
                local_product,
                restricted_components,
            )
            return modules.equalizer_element(
                self.compatible_sections_construction(),
                product_element,
            )

        def compatible_section_component(self, section, chart_index):
            r"""Project a global section to its component on one affine chart."""
            chart = self.cover().chart_label(chart_index)
            construction = self.compatible_sections_construction()
            shape = construction.diagram().domain()
            local_element = construction.structure_morphism(shape.source())(section)
            component = Modules(self.scheme().coordinate_algebra()).product_component(
                self.local_section_product_construction(),
                local_element,
                chart,
            )
            return self.local_module(chart)(component.underlying_element())

        @cached_method
        def descent_presheaf(self):
            r"""Return the presheaf of ``O(X)``-modules on this cover's finite Čech site."""
            return _ModuleGluingCechPresheaf(self)

        @cached_method
        def descent_data(self) -> DescentData:
            r"""Return the descent datum selecting ``Gamma(X, F)`` as the Čech equalizer.

            The inverse of the canonical comparison is the identity of the
            module of compatible sections, because that module is selected as
            the equalizer.  The comparison itself is formed when a consumer
            asks for it; forming it needs the product of the chart values in
            ``Modules(O(X))``.
            """
            presheaf = self.descent_presheaf()
            selected_cover = self.cover().cech_covering_family()

            def inverse_for(equalizer):
                if equalizer.covering_family() is not selected_cover:
                    raise ValueError("this affine descent datum belongs to a different Čech family")
                global_sections = self.compatible_sections()
                return global_sections.Mor(global_sections).identity()

            return DescentData(
                self.cover().cech_coverage(),
                presheaf,
                inverse_for,
                equalizer_for=presheaf.selected_equalizer_construction,
            )

        def _construct_sheaf(
            self,
            *,
            categories=(),
            construction_data=None,
            _engine=_ModuleGluingSheafEngine,
        ):
            r"""Construct this descent datum's sheaf with optional stronger placement."""
            sheaves = self.cover().cech_coverage().sheaves(
                Modules(self.scheme().coordinate_algebra())
            )
            data = dict(construction_data or {})
            if "module_gluing_datum" in data:
                raise ValueError("module_gluing_datum is fixed by this descent datum")
            data["module_gluing_datum"] = self
            return sheaves.object(
                self.descent_presheaf(),
                self.descent_data(),
                categories=(QuasiCoherentSheaves(self.scheme()), *tuple(categories)),
                construction_data=data,
                _engine=_engine,
            )

        @cached_method
        def _canonical_sheaf(self):
            return self._construct_sheaf()

        def sheaf(self, *, categories=(), construction_data=None, _engine=None):
            r"""Return the glued sheaf, optionally placed in stronger sheaf categories.

            With no additional placement this is the canonical cached sheaf
            represented by the datum.  A specialization may add semantic
            categories and a private engine, but construction still passes
            through the same ``Sheaves.object`` entry.
            """
            if not categories and construction_data is None and _engine is None:
                return self._canonical_sheaf()
            return self._construct_sheaf(
                categories=categories,
                construction_data=construction_data,
                _engine=_ModuleGluingSheafEngine if _engine is None else _engine,
            )

        def Mor(self, target):
            r"""Return the represented Hom category of descent morphisms to ``target``."""
            return self.category().Mor(self, target)

        def _repr_(self):
            return f"Module gluing datum on {self.cover()}"


class _ModuleGluingCechPresheaf(Functor):
    r"""The presheaf of ``O(X)``-modules computed by affine module gluing.

    On the Čech site of the cover its value at a chart or a pair overlap
    ``U_I`` is the local module over ``O(U_I)`` read over ``O(X)`` by
    restriction of scalars along ``O(X) -> O(U_I)``; its value at ``X`` is
    ``Gamma(X, F)``.  Restriction from ``U_i`` to ``U_ij`` lands in the module
    of the chart that owns the overlap presentation, through the inverse
    transition when that chart is the other one.
    """

    def __init__(self, gluing_datum) -> None:
        self._gluing_datum = gluing_datum
        cover = gluing_datum.cover()
        super().__init__(
            cover.cech_site().opposite(),
            Modules(cover.ambient_scheme().coordinate_algebra()),
        )

    def gluing_datum(self):
        return self._gluing_datum

    def cover(self):
        return self.gluing_datum().cover()

    def site(self):
        return self.cover().cech_site()

    def _label(self, opposite_object):
        return tuple(opposite_object.underlying_object().value())

    def _apply_object(self, opposite_object):
        return self.value_on_label(self._label(opposite_object))

    def value_on_label(self, label):
        r"""Return the presheaf value at one represented Čech label."""
        return self._value(tuple(label))

    @cached_method
    def _value(self, label):
        datum = self.gluing_datum()
        match label:
            case ():
                return datum.compatible_sections()
            case (chart,):
                return datum.local_module(chart).restrict_scalars(
                    _restriction_scalar_map(self.cover(), label)
                )
            case (owner, _other):
                return datum.restricted_module(owner, *label).restrict_scalars(
                    _restriction_scalar_map(self.cover(), label)
                )
        assert False, "the Čech site of a cover has the covered scheme, the charts and the pair overlaps as objects"

    def _restriction_value(self, source_label, target_label, element):
        datum = self.gluing_datum()
        target = self._value(target_label)
        owner = target_label[0]
        match source_label:
            case ():
                local = datum.compatible_section_component(element, owner)
                match target_label:
                    case (_chart,):
                        return target.wrap(local)
                    case _:
                        return target.wrap(datum.restrict_section(owner, local, *target_label))
            case (chart,):
                restricted = datum.restrict_section(chart, element.underlying_element(), *target_label)
                if chart != owner:
                    restricted = datum.transition(owner, chart).inverse()(restricted)
                return target.wrap(restricted)
        assert False, "the Čech site of a cover has no arrow out of a pair overlap"

    def restriction_between_labels(self, source_label, target_label):
        r"""Return the represented restriction between two Čech-labelled module values."""
        source_label = tuple(source_label)
        target_label = tuple(target_label)
        source = self.value_on_label(source_label)
        target = self.value_on_label(target_label)
        homset = source.module_category().Mor(source, target)
        match source_label == target_label:
            case True:
                return homset.identity()
            case False:
                return homset.elementwise(
                    lambda element: self._restriction_value(
                        source_label,
                        target_label,
                        element,
                    ),
                    verify_linearity=False,
                )

    def _apply_morphism(self, opposite_arrow):
        underlying = opposite_arrow.underlying_arrow()
        source_label = tuple(underlying.codomain().value())
        target_label = tuple(underlying.domain().value())
        return self.restriction_between_labels(source_label, target_label)

    def selected_equalizer_construction(self, equalizer):
        r"""Read the owner-built ``Gamma(X,F)`` through this Čech family's exact inclusion."""
        selected_cover = self.cover().cech_covering_family()
        match equalizer.covering_family() is selected_cover:
            case True:
                pass
            case False:
                raise ValueError("the selected affine equalizer belongs to a different Čech family")
        compatible_construction = self.gluing_datum().compatible_sections_construction()
        compatible = compatible_construction.object()
        inclusion = equalizer.restriction_to_product()
        left, right = equalizer.parallel_maps()
        diagram = _parallel_pair_diagram(left, right, self.codomain())
        shape = diagram.domain()

        def universal_leg(index):
            match index is shape.source():
                case True:
                    return inclusion
                case False:
                    return left * inclusion

        universal_cone = diagram.Cones().cone(
            compatible,
            universal_leg,
        )

        def factorizer(cone):
            source = cone.apex()
            source_leg = cone.structure_morphism(shape.source())
            owner_diagram = compatible_construction.diagram()
            owner_shape = owner_diagram.domain()

            match owner_diagram(owner_shape.source()) is source_leg.codomain():
                case True:
                    pass
                case False:
                    raise ArithmeticError("the Čech equalizer changed its local product object")

            def owner_leg(index):
                match index is owner_shape.source():
                    case True:
                        return source_leg
                    case False:
                        return owner_diagram(owner_shape.left()) * source_leg

            owner_cone = owner_diagram.Cones().cone(
                source,
                owner_leg,
            )
            return compatible_construction.factor(owner_cone).apex_map()

        return SelectedLimitConstruction(diagram, universal_cone, factorizer)

    def _repr_(self):
        return f"Čech presheaf of {self.gluing_datum()}"


class ModuleGluingMorphism(Morphism):
    r"""A morphism between module descent data on one represented affine cover."""

    def __init__(self, parent, local_maps) -> None:
        super().__init__(parent)
        supplied = _cover_chart_family(
            self.cover(),
            local_maps,
            name="Local maps of a module descent morphism",
        )

        def owned_local_map(label):
            source = self.domain().local_module(label)
            target = self.codomain().local_module(label)
            return source.module_category().Mor(source, target)(supplied[label])

        self._local_maps = finite_indexed_family(
            self.cover().atlas(),
            owned_local_map,
            name="Local maps of a module descent morphism",
        )
        self._verify_overlap_compatibility()

    def cover(self):
        return self.domain().cover()

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[self.cover().chart_label(index)]

    def restricted_local_map(self, chart_index, *intersection_indices):
        r"""Restrict one chart map to the represented cover intersection."""
        chart = self.cover().chart_label(chart_index)
        return self._restricted_local_map(
            chart,
            self.cover().intersection_indices(chart, *intersection_indices),
        )

    @cached_method
    def _restricted_local_map(self, chart, labels):
        local_map = self.local_map(chart)
        source = self.domain().restricted_module(chart, *labels)
        target = self.codomain().restricted_module(chart, *labels)
        if source is self.domain().local_module(chart):
            return local_map
        ring_map = self.domain().scheme().structure_sheaf().restriction_map(
            self.cover().open(chart),
            self.cover().intersection(*labels),
        )
        local_source = self.domain().local_module(chart)
        local_target = self.codomain().local_module(chart)
        return source.module_category().Mor(source, target)(
            lambda label: _base_change_element(
                local_target,
                target,
                ring_map,
                local_map(local_source.module_generator(label)),
            )
        )

    def _verify_overlap_compatibility(self) -> None:
        for left, right in combinations(tuple(self.cover().atlas()), 2):
            source_transition = self.domain().transition(left, right).forward()
            target_transition = self.codomain().transition(left, right).forward()
            via_left = target_transition * self.restricted_local_map(left, left, right)
            via_right = self.restricted_local_map(right, left, right) * source_transition
            if not _maps_agree_on_framing(via_left, via_right):
                raise ValueError(
                    "module descent morphism is incompatible with transition maps on an overlap"
                )

    @cached_method
    def global_sections_map(self):
        r"""Return the induced ``O(X)``-linear map on compatible global sections."""
        source_datum = self.domain()
        target_datum = self.codomain()
        source_sections = self.domain().compatible_sections()
        target_sections = self.codomain().compatible_sections()

        def image(section):
            return target_datum.compatible_section(
                finite_indexed_family(
                    self.cover().atlas(),
                    lambda label: self.local_map(label)(
                        source_datum.compatible_section_component(section, label)
                    ),
                    name="Components of an induced global section",
                )
            )

        return source_sections.module_category().Mor(source_sections, target_sections).elementwise(
            image,
            verify_linearity=False,
        )

    def then(self, other):
        r"""Return ``other after self``."""
        if other.domain() is not self.codomain():
            raise ValueError("the first descent-morphism target must equal the second source")
        return other * self

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            finite_indexed_family(
                self.cover().atlas(),
                lambda label: self.local_map(label) * other.local_map(label),
                name="Local maps of a composite module descent morphism",
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
        super().__init__(family, domain, codomain)

    def _element_constructor_(self, local_maps):
        if isinstance(local_maps, ModuleGluingMorphism):
            if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                raise ValueError("the module descent morphism has the wrong endpoints")
            if local_maps.parent() is self:
                return local_maps
            local_maps = local_maps.local_maps()
        return self.element_class(self, local_maps)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a descent endomorphism Hom")
        return self(
            self.domain().local_modules().map(
                lambda module: module.module_category().Mor(module, module).identity()
            )
        )


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


def _finite_algebra_framing(algebra):
    if algebra not in FramedAlgebras(algebra.base_ring()):
        raise TypeError("affine algebra descent currently requires finitely framed local algebras")
    labels = algebra.algebra_generating_set()
    if not labels.cardinality().is_finite():
        raise TypeError("affine algebra descent currently requires finitely framed local algebras")
    return labels


class AlgebraGluingHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return AlgebraGluingHomset


class _AlgebraGluingSheafEngine:
    r"""Private realization of an algebra sheaf with one chosen affine descent presentation."""

    def __init__(self, algebra_gluing_datum, **rest) -> None:
        self._algebra_gluing_datum = algebra_gluing_datum
        super().__init__(**rest)

    def gluing_datum(self):
        return self._algebra_gluing_datum

    def cover(self):
        return self.gluing_datum().cover()

    def ringed_space(self):
        return self.gluing_datum().scheme()

    scheme = ringed_space

    def sections_on_chart(self, index):
        return self.gluing_datum().local_algebra(index)

    local_algebra = sections_on_chart

    def sections_on_intersection(self, chart_index, *intersection_indices):
        return self.gluing_datum().restricted_algebra(
            chart_index, *intersection_indices
        )

    def restriction_map(self, chart_index, *intersection_indices):
        return self.gluing_datum().restriction_map(
            chart_index, *intersection_indices
        )

    def transition(self, source_index, target_index, *intersection_indices):
        match intersection_indices:
            case ():
                return self.gluing_datum().transition(source_index, target_index)
            case _:
                return self.gluing_datum().transition_on_intersection(
                    source_index, target_index, *intersection_indices
                )

    def global_sections(self):
        return self.gluing_datum().compatible_sections()

    def underlying_module_sheaf(self):
        return self.gluing_datum().underlying_module_datum().sheaf()

    def relative_spectrum(self):
        return self.gluing_datum().relative_spectrum()


class AlgebraGluingData(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""Descent data for unital associative algebras on one distinguished affine cover.

    For ``X = Spec A`` covered by ``U_i = D(f_i)``, an object is a family of
    finitely framed ``O(U_i)``-algebras ``B_i`` with algebra isomorphisms
    ``phi_ij : B_i|_{U_ij} -> B_j|_{U_ij}`` satisfying the cocycle condition
    on triple overlaps.  Forgetting the multiplications gives module descent
    data on the same local objects.

    ``AlgebraGluingData(cover)(local_algebras, transitions)`` is the one entry.
    """

    @staticmethod
    def __classcall__(cls, cover):
        return OwnedParameterizedCategory.__classcall__(cls, cover)

    def __init__(self, cover) -> None:
        OwnedParameterizedCategory.__init__(self, cover)

    def parameter_category(self):
        return DistinguishedAffineCovers()

    def cover(self):
        return self.base()

    def super_categories(self):
        return [DescentDataOnCover(self.cover().coverage(), self.cover())]

    def an_object(self):
        r"""The descent datum of the relative affine line: ``O(U_i)[z]`` with ``z |-> z``."""
        cover = self.cover()
        local_algebras = finite_indexed_family(
            cover.atlas(),
            lambda label: cover.open(label).coordinate_algebra().free_module(("z",)).symmetric_algebra(),
            name="Polynomial chart algebras",
        )

        def identity_transition(left, right):
            source = cover.restrict_algebra(local_algebras[left], left, right)
            target = cover.restrict_algebra(local_algebras[right], right, left)
            algebras = Algebras(source.algebra_base_ring()).Associative().Unital()
            forward = algebras.Mor(source, target)({"z": target.algebra_generator("z")})
            inverse = algebras.Mor(target, source)({"z": source.algebra_generator("z")})
            return algebras.Core().Mor(source, target)(forward, inverse)

        return self(
            local_algebras,
            {
                (left, right): identity_transition(left, right)
                for left, right in combinations(tuple(cover.atlas()), 2)
            },
        )

    def object(self, local_algebras, transitions):
        r"""The algebra descent datum ``(B_i, phi_ij)`` on this cover."""
        cover = self.cover()
        return _object_of(
            self,
            local_algebras=_cover_chart_family(
                cover,
                local_algebras,
                name="Local algebras of algebra descent",
            ),
            transitions=_cover_pair_family(cover, transitions, noun="algebra gluing"),
        )

    __call__ = object

    def _repr_object_names(self):
        return f"algebra descent data on {self.cover()}"

    _HomCategory = AlgebraGluingHomCategoryConstruction

    class ParentMethods:
        def __init__(self, local_algebras, transitions, **rest) -> None:
            self._local_algebras = local_algebras
            self._transitions = transitions
            super().__init__(**rest)
            for label in self.chart_index_set():
                if self.local_algebra(label).base_ring() is not self.cover().open(label).coordinate_algebra():
                    raise ValueError("each local algebra must be defined over its chart section ring")
                _finite_algebra_framing(self.local_algebra(label))
            self._verify_pairwise_transitions()
            self._verify_cocycles()

        def cover(self):
            return self.category().cover()

        def ringed_space(self):
            return self.cover().ambient_scheme()

        scheme = ringed_space

        def chart_index_set(self):
            r"""The atlas of the cover, which labels the charts of this datum."""
            return self.cover().atlas()

        def local_algebras(self):
            return self._local_algebras

        def local_algebra(self, index):
            return self.local_algebras()[self.cover().chart_label(index)]

        def restricted_algebra(self, chart_index, *intersection_indices):
            restricted = self.cover().restrict_algebra(
                self.local_algebra(chart_index),
                chart_index,
                *intersection_indices,
            )
            target = self.cover().intersection(chart_index, *intersection_indices).coordinate_algebra()
            if restricted not in Algebras(target).Associative().Unital():
                raise TypeError("algebra scalar extension did not preserve the algebra structure")
            _finite_algebra_framing(restricted)
            return restricted

        def transition(self, source_index, target_index):
            pair = _chart_pair(self.cover(), source_index, target_index)
            if pair == (self.cover().chart_label(source_index), self.cover().chart_label(target_index)):
                return self._transitions[pair]
            return self._reversed_transition(pair)

        @cached_method
        def _reversed_transition(self, pair):
            r"""``phi_ij^{-1}``, the algebra isomorphism of the pair read from ``j`` to ``i``."""
            original = self._transitions[pair]
            source = original.codomain()
            target = original.domain()
            return Algebras(source.algebra_base_ring()).Associative().Unital().Core().Mor(source, target)(
                original.inverse(),
                original.forward(),
            )

        def _verify_pairwise_transitions(self) -> None:
            for pair in self._transitions.index_set():
                left, right = pair
                transition = self._transitions[pair]
                source = self.restricted_algebra(left, left, right)
                target = self.restricted_algebra(right, left, right)
                core = Algebras(source.algebra_base_ring()).Associative().Unital().Core()
                if transition not in core.Mor(source, target):
                    raise TypeError(
                        "an algebra transition is an algebra isomorphism between the restrictions of its two local algebras to the overlap"
                    )
                if not _algebra_maps_agree_on_generators(
                    transition.inverse() * transition.forward(),
                    _algebra_homset(source, source).identity(),
                ):
                    raise ValueError("the stated algebra transition is not left-invertible on the overlap")
                if not _algebra_maps_agree_on_generators(
                    transition.forward() * transition.inverse(),
                    _algebra_homset(target, target).identity(),
                ):
                    raise ValueError("the stated algebra transition is not right-invertible on the overlap")

        def restriction_between_intersections(self, chart_index, source_indices, target_indices):
            r"""Return the algebra restriction to a finer represented intersection."""
            cover = self.cover()
            chart = cover.chart_label(chart_index)
            return self._restriction_between(
                chart,
                cover.intersection_indices(chart, *tuple(source_indices)),
                cover.intersection_indices(chart, *tuple(target_indices)),
            )

        @cached_method
        def _restriction_between(self, chart, source_labels, target_labels):
            if not set(source_labels).issubset(target_labels):
                raise ValueError("algebra restriction requires the target intersection to refine the source")
            source = self.restricted_algebra(chart, *source_labels)
            target = self.restricted_algebra(chart, *target_labels)
            if target is source:
                return _algebra_homset(source, source).identity()
            source_open = self.cover().intersection(*source_labels)
            target_open = self.cover().intersection(*target_labels)
            ring_map = self.scheme().structure_sheaf().restriction_map(source_open, target_open)
            restricted_target = target.restrict_scalars(ring_map)
            return _algebra_homset(source, restricted_target)(
                lambda label: restricted_target(target.algebra_generator(label))
            )

        def restriction_map(self, chart_index, *intersection_indices):
            chart = self.cover().chart_label(chart_index)
            return self.restriction_between_intersections(
                chart,
                (chart,),
                self.cover().intersection_indices(chart, *intersection_indices),
            )

        def restrict_section_between_intersections(self, chart_index, section, source_indices, target_indices):
            source = self.restricted_algebra(chart_index, *tuple(source_indices))
            target = self.restricted_algebra(chart_index, *tuple(target_indices))
            image = self.restriction_between_intersections(
                chart_index,
                source_indices,
                target_indices,
            )(source(section))
            return target(image)

        def transition_on_intersection(self, source_index, target_index, *intersection_indices):
            r"""Restrict an algebra transition to a finer represented intersection."""
            cover = self.cover()
            source = cover.chart_label(source_index)
            target = cover.chart_label(target_index)
            return self._transition_on(
                source,
                target,
                cover.intersection_indices(source, target, *intersection_indices),
            )

        @cached_method
        def _transition_on(self, source_label, target_label, labels):
            pair = self.cover().intersection_indices(source_label, target_label)
            transition = self.transition(source_label, target_label).forward()
            if labels == pair:
                return transition
            pair_source = self.restricted_algebra(source_label, *pair)
            source = self.restricted_algebra(source_label, *labels)
            target = self.restricted_algebra(target_label, *labels)
            target_restriction = self.restriction_between_intersections(target_label, pair, labels)
            return _algebra_homset(source, target)(
                lambda label: target(target_restriction(transition(pair_source.algebra_generator(label))))
            )

        def restricted_local_map(self, target_datum, chart_index, other_index, local_map):
            r"""Base-change one local algebra map to a represented pair overlap."""
            if target_datum.cover() is not self.cover():
                raise ValueError("algebra descent maps require one underlying affine cover")
            chart = self.cover().chart_label(chart_index)
            other = self.cover().chart_label(other_index)
            if (
                local_map.domain() is not self.local_algebra(chart)
                or local_map.codomain() is not target_datum.local_algebra(chart)
            ):
                raise ValueError("a local algebra-descent map has the wrong chart endpoints")
            source = self.restricted_algebra(chart, chart, other)
            target = target_datum.restricted_algebra(chart, chart, other)
            ring_map = self.cover().structure_sheaf_restriction(chart, other)
            extended_map = (
                Algebras(ring_map.domain())
                .Associative()
                .Unital()
                .scalar_extension(ring_map)(local_map)
            )
            extended_source = extended_map.domain()
            return _algebra_homset(source, target)(
                {
                    label: target(extended_map(extended_source.algebra_generator(label)))
                    for label in source.algebra_generating_set()
                }
            )

        def _verify_cocycles(self) -> None:
            for left, middle, right in combinations(tuple(self.chart_index_set()), 3):
                labels = (left, middle, right)
                if not _algebra_maps_agree_on_generators(
                    self.transition_on_intersection(middle, right, *labels)
                    * self.transition_on_intersection(left, middle, *labels),
                    self.transition_on_intersection(left, right, *labels),
                ):
                    raise ValueError("algebra transition isomorphisms fail the cocycle condition on a triple overlap")

        @cached_method
        def underlying_module_datum(self):
            r"""The module descent datum on the same local objects, multiplications forgotten."""
            transitions = {}
            for pair in self._transitions.index_set():
                transition = self._transitions[pair]
                forget = Algebras(self.cover().intersection(*pair).coordinate_algebra()).underlying_module()
                forward = forget(transition.forward())
                inverse = forget(transition.inverse())
                transitions[pair] = forward.domain().module_category().Core().Mor(
                    forward.domain(),
                    forward.codomain(),
                )(forward, inverse)
            return ModuleGluingData(self.cover())(self.local_algebras(), transitions)

        @cached_method
        def compatible_sections_multiplication(self):
            r"""Return the chartwise product ``Gamma(X,A) tensor Gamma(X,A) -> Gamma(X,A)``."""
            module_datum = self.underlying_module_datum()
            sections = module_datum.compatible_sections()
            tensor_square = Modules(self.scheme().coordinate_algebra()).tensor_product(
                (sections, sections)
            )

            def product(left, right):
                return module_datum.compatible_section(
                    finite_indexed_family(
                        self.chart_index_set(),
                        lambda label: self.local_algebra(label)(
                            module_datum.compatible_section_component(left, label)
                        )
                        * self.local_algebra(label)(
                            module_datum.compatible_section_component(right, label)
                        ),
                        name="Components of a product of compatible algebra sections",
                    )
                )

            return tensor_square.from_bilinear_map(sections, product)

        @cached_method
        def compatible_sections_unit(self):
            r"""Return the compatible family of local algebra units in ``Gamma(X,U(A))``."""
            module_datum = self.underlying_module_datum()
            return module_datum.compatible_section(
                self.local_algebras().map(lambda algebra: algebra.one())
            )

        @cached_method
        def compatible_sections(self):
            r"""Return ``Gamma(X,A)`` through its module, tensor multiplication, and unit."""
            ring = self.scheme().coordinate_algebra()
            module = self.underlying_module_datum().compatible_sections()
            multiplication = self.compatible_sections_multiplication()
            unit = self.compatible_sections_unit()
            algebras = Algebras(ring).Associative().Unital()
            commutative = algebras.Commutative()
            match all(
                algebra in Algebras(algebra.base_ring()).Associative().Unital().Commutative()
                for algebra in self.local_algebras()
            ):
                case True:
                    return commutative(module, multiplication, unit)
                case False:
                    return algebras(module, multiplication, unit)

        def compatible_section(self, sections):
            r"""Construct a global algebra section from compatible chart components."""
            module_section = self.underlying_module_datum().compatible_section(sections)
            return self.compatible_sections()(module_section)

        def compatible_section_component(self, section, chart_index):
            r"""Project a global algebra section to one chart component."""
            module_datum = self.underlying_module_datum()
            return module_datum.compatible_section_component(
                module_datum.compatible_sections()(section),
                chart_index,
            )

        @cached_method
        def descent_presheaf(self):
            r"""Return the presheaf of ``O(X)``-algebras on this cover's finite Čech site."""
            return _AlgebraGluingCechPresheaf(self)

        @cached_method
        def descent_data(self) -> DescentData:
            r"""Return the descent datum selecting ``Gamma(X, A)`` as the Čech equalizer.

            The inverse of the canonical comparison is the identity of the
            algebra of compatible sections.  The comparison itself is formed
            when a consumer asks for it; forming it needs the product of the
            chart values among ``O(X)``-algebras.
            """
            presheaf = self.descent_presheaf()
            selected_cover = self.cover().cech_covering_family()

            def inverse_for(equalizer):
                if equalizer.covering_family() is not selected_cover:
                    raise ValueError("this affine descent datum belongs to a different Čech family")
                global_sections = self.compatible_sections()
                return _algebra_homset(global_sections, global_sections).identity()

            return DescentData(self.cover().cech_coverage(), presheaf, inverse_for)

        @cached_method
        def sheaf(self):
            r"""Return the glued sheaf, an object of ``Sh(Čech site, unital associative O(X)-algebras)``."""
            sheaves = self.cover().cech_coverage().sheaves(
                Algebras(self.scheme().coordinate_algebra()).Associative().Unital()
            )
            return sheaves.object(
                self.descent_presheaf(),
                self.descent_data(),
                categories=(
                    AlgebraSheaves(self.scheme()),
                    QuasiCoherentSheaves(self.scheme()),
                ),
                construction_data={"algebra_gluing_datum": self},
                _engine=_AlgebraGluingSheafEngine,
            )

        def Mor(self, target):
            return self.category().Mor(self, target)

        def relative_spectrum(self, *, _engine=None, construction_data=None):
            r"""Return ``Spec_X(A)`` for this represented quasi-coherent algebra datum."""
            from dzack_research.preamble.categories.schemes.relative_spec import (
                _relative_spectrum,
            )

            return _relative_spectrum(
                self,
                _engine=_engine,
                construction_data=construction_data,
            )

        def _repr_(self):
            return f"Algebra gluing datum on {self.cover()}"


class _AlgebraGluingCechPresheaf(Functor):
    r"""The presheaf of unital associative ``O(X)``-algebras computed by affine algebra gluing.

    Its value at a chart or pair overlap ``U_I`` is the local algebra over
    ``O(U_I)`` read over ``O(X)`` by restriction of scalars; its value at
    ``X`` is ``Gamma(X, A)``.  Restriction maps are the algebra restrictions
    of the descent datum, read through the inverse transition when the target
    overlap is presented by the other chart.
    """

    def __init__(self, gluing_datum) -> None:
        self._gluing_datum = gluing_datum
        cover = gluing_datum.cover()
        super().__init__(
            cover.cech_site().opposite(),
            Algebras(cover.ambient_scheme().coordinate_algebra()).Associative().Unital(),
        )

    def gluing_datum(self):
        return self._gluing_datum

    def cover(self):
        return self.gluing_datum().cover()

    def _label(self, opposite_object):
        return tuple(opposite_object.underlying_object().value())

    def _apply_object(self, opposite_object):
        return self._value(self._label(opposite_object))

    @cached_method
    def _value(self, label):
        datum = self.gluing_datum()
        match label:
            case ():
                return datum.compatible_sections()
            case (chart,):
                return datum.local_algebra(chart).restrict_scalars(
                    _restriction_scalar_map(self.cover(), label)
                )
            case (owner, _other):
                return datum.restricted_algebra(owner, *label).restrict_scalars(
                    _restriction_scalar_map(self.cover(), label)
                )
        assert False, "the Čech site of a cover has the covered scheme, the charts and the pair overlaps as objects"

    def _restriction_value(self, source_label, target_label, element):
        datum = self.gluing_datum()
        target = self._value(target_label)
        owner = target_label[0]
        match source_label:
            case ():
                local = datum.compatible_section_component(element, owner)
                match target_label:
                    case (_chart,):
                        return target(local)
                    case _:
                        return target(
                            datum.restrict_section_between_intersections(owner, local, (owner,), target_label)
                        )
            case (chart,):
                restricted = datum.restrict_section_between_intersections(
                    chart,
                    datum.local_algebra(chart)(element),
                    (chart,),
                    target_label,
                )
                if chart != owner:
                    restricted = datum.transition(owner, chart).inverse()(restricted)
                return target(restricted)
        assert False, "the Čech site of a cover has no arrow out of a pair overlap"

    def _apply_morphism(self, opposite_arrow):
        underlying = opposite_arrow.underlying_arrow()
        source_label = tuple(underlying.codomain().value())
        target_label = tuple(underlying.domain().value())
        source = self(opposite_arrow.domain())
        target = self(opposite_arrow.codomain())
        homset = _algebra_homset(source, target)
        if source_label == target_label:
            return homset.identity()
        return homset(
            SetMorphism(
                Sets().Mor(source, target),
                lambda element: self._restriction_value(source_label, target_label, element),
            )
        )

    def _repr_(self):
        return f"Čech presheaf of {self.gluing_datum()}"


class AlgebraGluingMorphism(Morphism):
    r"""A compatible family of local algebra morphisms between descent data."""

    def __init__(self, parent, local_maps) -> None:
        super().__init__(parent)
        supplied = _cover_chart_family(
            self.cover(),
            local_maps,
            name="Local maps of an algebra descent morphism",
        )
        self._local_maps = finite_indexed_family(
            self.cover().atlas(),
            lambda label: _algebra_homset(
                self.domain().local_algebra(label),
                self.codomain().local_algebra(label),
            )(supplied[label]),
            name="Local maps of an algebra descent morphism",
        )
        self._verify_overlap_compatibility()

    def cover(self):
        return self.domain().cover()

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[self.cover().chart_label(index)]

    def _verify_overlap_compatibility(self) -> None:
        for left, right in combinations(tuple(self.cover().atlas()), 2):
            source_transition = self.domain().transition(left, right).forward()
            target_transition = self.codomain().transition(left, right).forward()
            left_restriction = self.domain().restricted_local_map(
                self.codomain(), left, right, self.local_map(left)
            )
            right_restriction = self.domain().restricted_local_map(
                self.codomain(), right, left, self.local_map(right)
            )
            if not _algebra_maps_agree_on_generators(
                target_transition * left_restriction,
                right_restriction * source_transition,
            ):
                raise ValueError(
                    "algebra descent morphism is incompatible with transition maps on an overlap"
                )

    @cached_method
    def underlying_module_morphism(self):
        return self.domain().underlying_module_datum().Mor(
            self.codomain().underlying_module_datum()
        )(
            finite_indexed_family(
                self.cover().atlas(),
                lambda label: Algebras(self.cover().open(label).coordinate_algebra()).underlying_module()(
                    self.local_map(label)
                ),
                name="Local module maps underlying an algebra descent morphism",
            )
        )

    @cached_method
    def global_sections_map(self):
        source_datum = self.domain()
        target_datum = self.codomain()
        source = self.domain().compatible_sections()
        target = self.codomain().compatible_sections()

        def image(section):
            return target_datum.compatible_section(
                finite_indexed_family(
                    self.cover().atlas(),
                    lambda label: self.local_map(label)(
                        source_datum.compatible_section_component(section, label)
                    ),
                    name="Components of an induced global algebra section",
                )
            )

        return _algebra_homset(source, target)(SetMorphism(Sets().Mor(source, target), image))

    def relative_spectrum_morphism(self):
        r"""Return the contravariant morphism of relative spectra induced by this algebra map."""
        from dzack_research.preamble.categories.schemes.relative_spec import (
            _relative_spectrum_morphism,
        )

        return _relative_spectrum_morphism(self)

    def then(self, other):
        if other.domain() is not self.codomain():
            raise ValueError("the first algebra descent-morphism target must equal the second source")
        return other * self

    def __mul__(self, other):
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            finite_indexed_family(
                self.cover().atlas(),
                lambda label: self.local_map(label) * other.local_map(label),
                name="Local maps of a composite algebra descent morphism",
            )
        )

    def _repr_(self):
        return f"Algebra descent morphism from {self.domain()} to {self.codomain()}"


class AlgebraGluingHomset(CategoricalHomset):
    Element = AlgebraGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.cover() is not codomain.cover():
            raise ValueError("an algebra descent Hom requires one common affine cover")
        super().__init__(family, domain, codomain)

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
            self.domain().local_algebras().map(
                lambda algebra: _algebra_homset(algebra, algebra).identity()
            )
        )


class QuasiCoherentSheavesWithChosenDescentDatum(OwnedParameterizedCategory):
    r"""Quasi-coherent sheaves on ``X`` with a chosen descent datum on a finite affine atlas.

    An object is a quasi-coherent ``O_X``-module ``F`` together with the
    module descent datum ``(M_i, phi_ij)`` presenting it on a finite affine
    atlas ``{U_i}`` of ``X``: ``F(U_i) = M_i``, and ``phi_ij`` identifies the
    two presentations of each overlap, which may have distinct coordinate
    rings.  The descent datum is a choice beyond the sheaf; forgetting it
    lands in ``QuasiCoherentSheaves(X)``.

    ``QuasiCoherentSheavesWithChosenDescentDatum(X)(F)`` is the one entry, and
    every restriction and transition is read from the retained datum.
    """

    _HomCategory = FiniteAtlasModuleSheafHomCategoryConstruction

    def scheme(self):
        return self.base()

    ringed_space = scheme

    def super_categories(self):
        return [QuasiCoherentSheaves(self.scheme())]

    def an_object(self):
        r"""``O_X`` presented by rank-one free chart modules on the atlas ``X`` was glued from."""
        atlas = self.scheme().finite_affine_atlas()

        def identity(label, _domain, codomain):
            return codomain.module_generator(label)

        return FiniteAtlasModuleGluingData(atlas)(
            {
                index: atlas.chart(index).coordinate_algebra().free_module(1)
                for index in atlas.chart_indices()
            },
            {pair: (identity, identity) for pair in atlas.transition_index_set()},
        ).sheaf()

    def object(
        self,
        module_gluing_datum,
        *,
        categories=(),
        construction_data=None,
        _engine=None,
    ):
        r"""The quasi-coherent sheaf presented by ``module_gluing_datum``."""
        if module_gluing_datum.scheme() is not self.scheme():
            raise ValueError("the descent datum presents a sheaf on a different scheme")
        category = (
            self
            if not categories
            else Category.join((self, *tuple(categories)))
        )
        data = dict(construction_data or {})
        if "module_gluing_datum" in data:
            raise ValueError("module_gluing_datum is fixed by this descent datum")
        data["module_gluing_datum"] = module_gluing_datum
        engine = None if _engine is None else (self, _engine, None)
        return _object_of(category, _engine=engine, **data)

    __call__ = object

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a finite-atlas sheaf Hom requires two sheaves with chosen descent data on this scheme")
        return self.HomCategory().Of(domain, codomain)

    def _repr_object_names(self):
        return f"quasi-coherent sheaves on {self.scheme()} with a chosen finite-atlas descent datum"

    class ParentMethods:
        def __init__(self, module_gluing_datum, **rest) -> None:
            self._module_gluing_datum = module_gluing_datum
            super().__init__(**rest)

        def gluing_datum(self):
            r"""The module descent datum presenting this sheaf."""
            return self._module_gluing_datum

        def atlas_datum(self):
            return self.gluing_datum().gluing_datum()

        def ringed_space(self):
            return self.category().scheme()

        scheme = ringed_space

        def sections_on_chart(self, index):
            return self.gluing_datum().local_module(index)

        def sections_on_intersection(self, chart_index, other_index):
            return self.gluing_datum().pair_module(chart_index, other_index)

        def transition(self, source_index, target_index):
            return self.gluing_datum().transition(source_index, target_index)

        def global_sections(self):
            return self.gluing_datum().compatible_sections()

        def stalk_on_chart(self, chart_index, point):
            r"""Return the stalk of this sheaf at a point of the selected chart."""
            chart_index = self.atlas_datum().normalize_chart_index(chart_index)
            chart = self.atlas_datum().chart(chart_index)
            if point.parent() is not chart.underlying_space():
                raise ValueError("the stalk point belongs to the selected affine chart")
            return self.sections_on_chart(chart_index).localize_at_prime(point.ideal())

        def tensor_product(self, other):
            r"""Return ``self tensor O_X other`` by chartwise tensor descent."""
            if other not in self.category():
                raise TypeError("a finite-atlas tensor product is taken with a sheaf presented on the same scheme")
            return self.gluing_datum().tensor_product(other.gluing_datum()).sheaf()

        def morphism_to(self, other, local_maps):
            r"""Return the sheaf morphism represented by compatible chart maps."""
            if other not in self.category():
                raise TypeError("a finite-atlas sheaf morphism ends at a sheaf presented on the same scheme")
            return self.category().Mor(self, other)(local_maps)

        def pullback_to_refinement(self, refinement):
            r"""Return this sheaf on the selected finer affine atlas."""
            return refinement.pullback_module_datum(self.gluing_datum()).sheaf()

        def _repr_(self):
            return f"Finite-atlas module sheaf on {self.scheme()}"


class _FiniteAtlasInverseImageModuleSheafEngine:
    r"""The inverse image ``f^{-1} F`` before extension to ``O_X``-modules.

    The object lives on the fine atlas but retains the coarse local modules and
    the structural scalar maps ``O_Y(U_i) -> O_X(V_a)`` separately.  In
    particular it is not represented as an ``O_X``-module sheaf: that extra
    scalar extension is :meth:`module_pullback`.
    """

    def __init__(self, source_sheaf, **rest) -> None:
        refinement = self.refinement()
        if source_sheaf.atlas_datum() is not refinement.coarse_datum():
            raise ValueError("the inverse-image sheaf belongs to the refinement's coarse atlas")
        self._source_sheaf = source_sheaf
        super().__init__(**rest)

    def source_sheaf(self):
        return self._source_sheaf

    def refinement(self):
        return self.category().refinement()

    def scheme_morphism(self):
        return self.refinement().comparison_morphism()

    def ringed_space(self):
        return self.refinement().fine_scheme()

    scheme = ringed_space

    def coarse_index(self, fine_index):
        return self.refinement().coarse_index(fine_index)

    def source_local_module(self, fine_index):
        return self.source_sheaf().sections_on_chart(self.coarse_index(fine_index))

    def structural_ring_map(self, fine_index):
        return self.refinement().chart_map(
            fine_index
        ).coordinate_algebra_morphism()

    def module_pullback(self):
        r"""Return ``O_X tensor_{f^{-1}O_Y} f^{-1}F`` as an ``O_X``-module sheaf."""
        return self.refinement().inverse_image_scalar_extension_functor()(self)


class _FiniteAtlasInverseImageModuleMorphism(Morphism):
    r"""Inverse image of one finite-atlas module-sheaf morphism."""

    def __init__(self, parent, source_morphism) -> None:
        Morphism.__init__(self, parent)
        if source_morphism.domain() is not self.domain().source_sheaf():
            raise ValueError("the source inverse image has the wrong original sheaf")
        if source_morphism.codomain() is not self.codomain().source_sheaf():
            raise ValueError("the target inverse image has the wrong original sheaf")
        self._source_morphism = source_morphism

    def source_morphism(self):
        return self._source_morphism

    def local_map(self, fine_index):
        return self.source_morphism().local_map(
            self.domain().coarse_index(fine_index)
        )

    def __mul__(self, other):
        match other:
            case _FiniteAtlasInverseImageModuleMorphism() if other.codomain() is self.domain():
                return self.domain().category().Mor(other.domain(), self.codomain())(
                    self.source_morphism() * other.source_morphism()
                )
            case _:
                return NotImplemented


class _FiniteAtlasInverseImageModuleHomset(CategoricalHomset):
    r"""Hom in ``Mod(f^{-1}O_Y)`` for one represented finite-atlas refinement."""

    Element = _FiniteAtlasInverseImageModuleMorphism

    def _element_constructor_(self, source_morphism):
        match source_morphism:
            case _FiniteAtlasInverseImageModuleMorphism() if source_morphism.parent() is self:
                return source_morphism
            case _FiniteAtlasInverseImageModuleMorphism():
                source_morphism = source_morphism.source_morphism()
            case _:
                pass
        source_hom = self.base_category().source_category().Mor(
            self.domain().source_sheaf(),
            self.codomain().source_sheaf(),
        )
        if source_morphism not in source_hom:
            raise TypeError("an inverse-image module arrow comes from a morphism of the source sheaves")
        return self.element_class(self, source_morphism)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom")
        source = self.domain().source_sheaf()
        return self(self.base_category().source_category().Mor(source, source).identity())


class _FiniteAtlasInverseImageModuleHomCategoryConstruction(HomCategoryConstruction):
    r"""Hom family for finite-atlas presentations of ``f^{-1}O_Y``-modules."""

    def fixed_category_class(self):
        return _FiniteAtlasInverseImageModuleHomset


class _FiniteAtlasInverseImageModuleSheaves(OwnedCategory):
    r"""Represented ``f^{-1}O_Y``-modules for one finite-atlas refinement ``f:X->Y``."""

    _HomCategory = _FiniteAtlasInverseImageModuleHomCategoryConstruction

    def __init__(self, refinement) -> None:
        self._refinement = refinement
        super().__init__()

    def _make_named_class_key(self, name):
        return id(self._refinement)

    def refinement(self):
        return self._refinement

    def source_category(self):
        return QuasiCoherentSheavesWithChosenDescentDatum(
            self.refinement().coarse_scheme()
        )

    def super_categories(self):
        return [SheafObjects(self.refinement().fine_scheme())]

    def an_object(self):
        return self(self.source_category().an_object())

    @cached_method(key=lambda self, sheaf: id(sheaf))
    def object(self, sheaf):
        if sheaf not in self.source_category():
            raise TypeError("an inverse-image module starts from a sheaf in the represented source category")
        if sheaf.atlas_datum() is not self.refinement().coarse_datum():
            raise ValueError("the inverse-image sheaf belongs to the refinement's coarse atlas")
        return _object_of(
            self,
            source_sheaf=sheaf,
            _engine=_FiniteAtlasInverseImageModuleSheafEngine,
        )

    __call__ = object

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("an inverse-image module Hom requires two objects over the same refinement")
        return self.HomCategory().Of(domain, codomain)

    def _repr_(self):
        return f"Modules over the inverse-image structure sheaf along {self.refinement().comparison_morphism()}"


class _FiniteAtlasInverseImageModuleFunctor(Functor):
    r"""``f^{-1}`` on represented finite-atlas module sheaves."""

    def __init__(self, refinement) -> None:
        self._refinement = refinement
        super().__init__(
            QuasiCoherentSheavesWithChosenDescentDatum(refinement.coarse_scheme()),
            _FiniteAtlasInverseImageModuleSheaves(refinement),
        )

    def refinement(self):
        return self._refinement

    def scheme_morphism(self):
        return self.refinement().comparison_morphism()

    def _apply_object(self, sheaf):
        return self.codomain()(sheaf)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return self.codomain().Mor(source, target)(morphism)

    def _repr_(self):
        return f"Inverse image of module sheaves along {self.scheme_morphism()}"


class _FiniteAtlasInverseImageScalarExtensionFunctor(Functor):
    r"""Extend ``f^{-1}O_Y``-modules to ``O_X`` on a finite-atlas refinement."""

    def __init__(self, refinement, inverse_image_modules) -> None:
        self._refinement = refinement
        super().__init__(
            inverse_image_modules,
            QuasiCoherentSheavesWithChosenDescentDatum(refinement.fine_scheme()),
        )

    def refinement(self):
        return self._refinement

    def scheme_morphism(self):
        return self.refinement().comparison_morphism()

    @cached_method
    def _datum_image(self, source_sheaf):
        return self.refinement().pullback_module_datum(source_sheaf.gluing_datum())

    def _apply_object(self, inverse_image_sheaf):
        return self._datum_image(inverse_image_sheaf.source_sheaf()).sheaf()

    def _apply_morphism(self, inverse_image_morphism):
        source_sheaf = inverse_image_morphism.domain().source_sheaf()
        target_sheaf = inverse_image_morphism.codomain().source_sheaf()
        source = self._datum_image(source_sheaf)
        target = self._datum_image(target_sheaf)
        source_morphism = inverse_image_morphism.source_morphism()
        local_maps = {}
        for fine_index in self.refinement().fine_datum().chart_indices():
            coarse_index = self.refinement().coarse_index(fine_index)
            ring_map = self.refinement().chart_map(
                fine_index
            ).coordinate_algebra_morphism()
            local_maps[fine_index] = FiniteAtlasModuleGluingMorphism._base_changed_map(
                source_morphism.local_map(coarse_index),
                ring_map,
                source.local_module(fine_index),
                target.local_module(fine_index),
            )
        return source.morphism_to(target, local_maps)

    def _repr_(self):
        return f"Extension of inverse-image module scalars along {self.scheme_morphism()}"


class _FiniteAtlasLineBundleModuleGluingDatumEngine(_FiniteAtlasModuleGluingDatumEngine):
    r"""Module descent whose defining source is one finite-atlas line bundle."""

    def __init__(self, line_bundle, gluing_datum, local_modules, transitions, **rest) -> None:
        if gluing_datum is not line_bundle.gluing_datum():
            raise ValueError("the line-bundle module datum uses the line bundle's selected atlas")
        self._line_bundle = line_bundle
        super().__init__(gluing_datum, local_modules, transitions, **rest)

    def line_bundle(self):
        r"""Return the line bundle whose rank-one descent this datum represents."""
        return self._line_bundle


def _line_bundle_transition_images(line_bundle, source_index, target_index):
    unit = line_bundle.transition_unit(source_index, target_index)

    def images(label, domain, codomain):
        position = int(domain.module_generating_set().ranking_map()(label))
        target_label = codomain.module_generating_set()[position]
        return codomain.scalar_multiple(
            codomain.base_ring()(unit),
            codomain.module_generator(target_label),
        )

    return images


def _finite_atlas_line_bundle_module_sheaf(line_bundle):
    r"""Return the rank-one module sheaf underlying a finite-atlas line bundle."""
    datum = line_bundle.gluing_datum()
    local_modules = {
        index: line_bundle.local_module(index)
        for index in datum.chart_indices()
    }
    transitions = {
        (source_index, target_index): (
            _line_bundle_transition_images(
                line_bundle, source_index, target_index
            ),
            _line_bundle_transition_images(
                line_bundle, target_index, source_index
            ),
        )
        for source_index, target_index in datum.transition_index_set()
    }
    category = FiniteAtlasModuleGluingData(datum)
    descent = _object_of(
        category,
        _engine=(category, _FiniteAtlasLineBundleModuleGluingDatumEngine, None),
        line_bundle=line_bundle,
        gluing_datum=datum,
        local_modules=local_modules,
        transitions=transitions,
    )
    return descent.sheaf()


class FiniteAtlasLineBundlePullbackComparison(SageObject):
    r"""Compare generic module pullback with transition-unit line-bundle pullback."""

    def __init__(self, refinement, line_bundle) -> None:
        self._refinement = refinement
        self._line_bundle = line_bundle
        self._pullback_functor = refinement.module_pullback_functor()
        coarse_module_sheaf = line_bundle.module_sheaf()
        self._generic_pullback = self._pullback_functor.on_object(
            coarse_module_sheaf
        )
        self._line_bundle_refinement = refinement.pullback_invertible_sheaf(
            line_bundle
        )
        self._specialized_module_sheaf = (
            self._line_bundle_refinement.refined_bundle().module_sheaf()
        )
        generic = self._generic_pullback.gluing_datum()
        specialized = self._specialized_module_sheaf.gluing_datum()

        forward_maps = {}
        inverse_maps = {}
        for index in refinement.fine_datum().chart_indices():
            generic_module = generic.local_module(index)
            specialized_module = specialized.local_module(index)
            generic_labels = tuple(generic_module.module_generating_set())
            specialized_labels = tuple(specialized_module.module_generating_set())
            if len(generic_labels) != len(specialized_labels):
                raise ArithmeticError(
                    "generic and specialized line-bundle pullbacks have different local ranks"
                )
            forward_maps[index] = generic_module.module_category().Mor(generic_module, specialized_module)(
                {
                    source_label: specialized_module.module_generator(target_label)
                    for source_label, target_label in zip(
                        generic_labels, specialized_labels, strict=True
                    )
                }
            )
            inverse_maps[index] = specialized_module.module_category().Mor(specialized_module, generic_module)(
                {
                    target_label: generic_module.module_generator(source_label)
                    for source_label, target_label in zip(
                        generic_labels, specialized_labels, strict=True
                    )
                }
            )
        self._forward = generic.morphism_to(specialized, forward_maps)
        self._inverse = specialized.morphism_to(generic, inverse_maps)
        if self._inverse * self._forward != generic.identity_morphism():
            raise ArithmeticError(
                "the line-bundle pullback comparison is not left-invertible"
            )
        if self._forward * self._inverse != specialized.identity_morphism():
            raise ArithmeticError(
                "the line-bundle pullback comparison is not right-invertible"
            )

    def refinement(self):
        return self._refinement

    def line_bundle(self):
        return self._line_bundle

    def generic_pullback(self):
        return self._generic_pullback

    def line_bundle_refinement(self):
        return self._line_bundle_refinement

    def specialized_module_sheaf(self):
        return self._specialized_module_sheaf

    def forward(self):
        return self._forward

    def inverse(self):
        return self._inverse



def _chartwise_closed_subscheme(
    datum,
    local_closed_subschemes,
    *,
    name="Chartwise closed subscheme",
    _engine=None,
    construction_data=None,
):
    r"""Glue compatible closed subschemes of one finite affine atlas.

    A closed immersion is local on the target.  Each supplied ``Z_i -> U_i``
    is therefore restricted to the represented pair overlap and transported
    through the atlas transition of the glued scheme.  Corestriction into
    ``Z_j`` is the compatibility check; once every pair passes, the local
    closed schemes glue, and their inclusions glue to one closed immersion into
    the glued scheme of ``datum``, which is placed at construction.
    """
    from dzack_research.preamble.categories.schemes.schemes import (
        ClosedEmbeddings,
        ClosedSubschemes,
    )

    indices = datum.chart_index_set()
    local_closed = _family_on_finite_ordered_set(
        indices,
        local_closed_subschemes,
        name=f"Affine pieces of {name}",
        noun="a chartwise closed subscheme",
    )
    for index in indices:
        if local_closed[index].inclusion().codomain() is not datum.chart(index):
            raise ValueError("each chartwise closed subscheme lies in its selected chart of the glued scheme")
    return _glued_chartwise_subscheme(
        datum,
        local_closed,
        (ClosedEmbeddings(datum.scheme()), ClosedSubschemes(datum.base_ring())),
        _engine=_engine,
        construction_data=construction_data,
    )


def _chartwise_fixed_subscheme(datum, local_automorphisms):
    r"""Glue the fixed subschemes of a chart-preserving automorphism.

    Each local automorphism is an endomorphism of the corresponding affine
    chart.  Its equalizer with the identity is closed.  On every pair overlap
    the gluing transition carries one local equalizer to the other;
    restricting that transition therefore supplies the fixed-locus gluing.
    The resulting global inclusion is a closed immersion because closedness is
    local on the target for this finite affine cover.
    """
    from dzack_research.preamble.categories.schemes.schemes import (
        ClosedEmbeddings,
        ClosedSubschemes,
    )

    indices = datum.chart_index_set()
    automorphisms = _family_on_finite_ordered_set(
        indices,
        local_automorphisms,
        name="Local automorphisms defining a glued fixed subscheme",
        noun="a chart-preserving automorphism",
    )
    for index in indices:
        automorphism = automorphisms[index]
        chart = datum.chart(index)
        if automorphism.domain() is not chart or automorphism.codomain() is not chart:
            raise ValueError("a chartwise fixed locus requires endomorphisms of the selected charts")
    local_fixed = finite_indexed_family(
        indices,
        lambda index: automorphisms[index].fixed_subscheme(),
        name="Affine charts of the glued fixed subscheme",
    )
    return _glued_chartwise_subscheme(datum, local_fixed, (ClosedEmbeddings(datum.scheme()), ClosedSubschemes(datum.base_ring())))


def _glued_chartwise_subscheme(
    datum,
    local_closed,
    placements,
    *,
    _engine=None,
    construction_data=None,
):
    r"""Glue closed subschemes ``Z_i <= U_i`` that agree through the atlas transitions.

    ``Z_i cap U_ij`` is the distinguished open of ``Z_i`` cut out by the
    restriction of the overlap's defining element, and the transition of the
    glued scheme, restricted to it, lands in ``Z_j cap U_ji``.  Those
    restrictions are the gluing transitions of the ``Z_i``, and the inclusions
    ``Z_i -> U_i -> X`` are the local maps of the inclusion of the glued
    subscheme into ``X``.
    """

    def local_overlap(source_index, target_index):
        closed = local_closed[source_index]
        element = datum.overlap(source_index, target_index).distinguished_open_element()
        return closed.distinguished_open(closed.inclusion().coordinate_algebra_morphism()(element))

    def local_transition(source_index, target_index):
        source = local_overlap(source_index, target_index)
        target = local_overlap(target_index, source_index)
        into_source_chart = local_closed[source_index].inclusion() * source.inclusion()
        into_source_overlap = datum.overlap(source_index, target_index).corestriction(into_source_chart)
        across = datum.transition_between(source_index, target_index).forward() * into_source_overlap
        into_target_chart = datum.overlap(target_index, source_index).inclusion() * across
        into_target_closed = local_closed[target_index].corestriction(into_target_chart)
        return target.corestriction(into_target_closed)

    schemes = Schemes(datum.base_ring())
    transitions = {}
    for left, right in datum.transition_index_set():
        forward = local_transition(left, right)
        inverse = local_transition(right, left)
        transitions[left, right] = schemes.Core().Mor(forward.domain(), forward.codomain())(forward, inverse)
    return schemes.glue_affine_atlas(
        local_closed,
        transitions,
        placements=placements,
        inclusion_codomain=datum.scheme(),
        inclusion_datum=finite_indexed_family(
            datum.chart_index_set(),
            lambda index: datum.chart_embedding(index) * local_closed[index].inclusion(),
            name="Local inclusions of a glued closed subscheme",
        ),
        _object_engine=_engine,
        **dict(construction_data or {}),
    )


__all__ = [
    "AlgebraGluingData",
    "AlgebraGluingHomset",
    "AlgebraGluingMorphism",
    "FiniteAtlasAlgebraGluingData",
    "FiniteAtlasAlgebraGluingMorphism",
    "FiniteAtlasAlgebraTransition",
    "FiniteAffineAtlases",
    "FiniteAtlasInvertibleSheafRefinement",
    "FiniteAtlasLineBundlePullbackComparison",
    "FiniteAtlasRefinement",
    "FiniteAtlasModuleGluingData",
    "FiniteAtlasModuleGluingMorphism",
    "QuasiCoherentSheavesWithChosenDescentDatum",
    "FiniteAtlasModuleTransition",
    "ModuleGluingData",
    "ModuleGluingHomset",
    "ModuleGluingMorphism",
    "SemilinearAlgebraMorphism",
    "SemilinearModuleMorphism",
]
