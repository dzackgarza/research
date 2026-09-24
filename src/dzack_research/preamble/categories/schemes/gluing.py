r"""Descent and gluing for represented schemes, modules, and algebras."""

from collections.abc import Mapping
from itertools import combinations, permutations

from sage.categories.category import Category
from sage.categories.morphism import Morphism, SetMorphism
from sage.misc.cachefunc import cached_method
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    CategoryPacketMethods,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.abstract_categories.presheaves import (
    Coverage,
    CoveringFamilies,
    CoveringFamilyMorCategoryConstruction,
    CoveringFamilyMor,
    CoveringFamilyMorphism,
    DescentData,
    DescentDataOnCover,
    Sheaves,
    _CechCoveringFamilies,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    PosetCategory,
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
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    _combined_linearity_decision,
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
    _scheme_composition_mor,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
    finite_indexed_family_from_values,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import _object_of


class _CanonicalDescentRestrictionMorphism(ModuleMorphism):
    r"""A canonical linear restriction/base-change map in represented descent data."""

    def __init__(self, parent, action) -> None:
        super().__init__(parent, action, elementwise=True)

    def _elementwise_linearity_derivation(self):
        return True


class _DescentGlobalSectionsMorphism(ModuleMorphism):
    r"""The compatible-section map induced chartwise by one descent morphism."""

    def __init__(self, parent, descent_morphism, source_datum, target_datum) -> None:
        self._descent_morphism = descent_morphism
        self._source_datum = source_datum
        self._target_datum = target_datum

        def image(section):
            return target_datum.compatible_section(
                finite_indexed_family(
                    descent_morphism.cover().atlas(),
                    lambda label: descent_morphism.local_map(label)(
                        source_datum.compatible_section_component(section, label)
                    ),
                    name="Components of an induced global section",
                )
            )

        super().__init__(parent, image, elementwise=True)

    def _elementwise_linearity_derivation(self):
        local_maps = tuple(
            self._descent_morphism.local_map(label)
            for label in self._descent_morphism.cover().atlas()
        )
        return _combined_linearity_decision(local_maps)


def _chart_pair(cover, left_index, right_index):
    r"""The two chart labels in the atlas order, which is how descent data is keyed."""

    labels = (cover.chart_label(left_index), cover.chart_label(right_index))
    if labels[0] == labels[1]:
        raise ValueError(
            f"cannot index descent data by the charts {left_index} and {right_index} of {cover}: they "
            f"are the same chart {labels[0]}, and descent data is indexed by pairs of distinct charts"
        )
    return tuple(sorted(labels, key=cover.atlas().ranking_map()))


def _family_on_finite_ordered_set(index_set, values, *, name, noun):
    r"""Read finite labelled data through the indexed-family literal owner."""
    family = finite_indexed_family_from_values(index_set, values, name=name)
    assert family.cardinality().is_finite(), (
        f"{noun} must form a finite family, but {family} is not finite"
    )
    return family


def _lands_in_distinguished_open(morphism, distinguished_open):
    r"""Whether ``g: T -> U`` of affine schemes factors through ``D(f) <= U``.

    It does exactly when ``g^#(f)`` is a unit of ``O(T)``: that is the
    universal property of ``O(D(f)) = O(U)[1/f]`` (Stacks, Tag 01HR), and it
    is the hypothesis under which ``corestriction`` constructs the factor.
    """
    return distinguished_open.contains_image_of(morphism)


def _scheme_core_mor(isomorphism):
    r"""``Core(Sch_R)(U, V)``, the isomorphisms of ``R``-schemes an overlap transition ``U -> V`` lies in."""
    domain = isomorphism.domain()
    return Schemes(domain.scheme_base_ring()).Core().Mor(domain, isomorphism.codomain())


def _algebra_mor(source, target):
    r"""Return the algebra Mor selected by the scalar algebra structure.

    An engine-backed algebra is also an owned ring and often a module, so its
    bare parent-level ``Mor`` is not enough to identify which of those several
    mathematical Mor theories is intended.  Algebra descent always means
    morphisms of associative unital algebras over the declared scalar ring.
    """
    base = source.algebra_base_ring()
    if target.algebra_base_ring() is not base:
        raise ValueError(
            f"cannot form the algebra morphisms from {source} to {target}: they must be algebras over "
            f"one base ring, but their base rings are {base} and {target.algebra_base_ring()}"
        )
    category = Algebras(base).Associative().Unital()
    if source not in category or target not in category:
        raise TypeError(
            f"cannot form the algebra morphisms from {source} to {target}: both must be associative "
            f"unital algebras over {base}, but they are objects of {source.category()} and "
            f"{target.category()}"
        )
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
        raise ValueError(
            f"cannot glue a scheme from {charts}: at least one affine chart is required, but none was "
            "given"
        )
    return family


class _GluedSchemeOpenInclusion(SchemeMorphism):
    r"""The chosen inclusion of one chart image into the glued scheme."""

    def __init__(self, parent, gluing_datum, chart_index) -> None:
        super().__init__(None, mor=parent)
        self._gluing_datum = gluing_datum
        self._chart_index = gluing_datum.normalize_chart_index(chart_index)

    def gluing_datum(self):
        return self._gluing_datum

    def chart_index(self):
        return self._chart_index

    def _in_mor(self, mor):
        return _GluedSchemeOpenInclusion(mor, self.gluing_datum(), self.chart_index())

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
        super().__init__(None, mor=parent)
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

    def _in_mor(self, mor):
        return _GluedSchemeChartEmbedding(
            mor, self.gluing_datum(), self.chart_index(),
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
            _scheme_composition_mor(self, other),
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
        super().__init__(None, mor=parent)
        if chart_embedding is not chart_embedding.gluing_datum().chart_embedding(chart_embedding.chart_index()):
            raise TypeError(
                f"cannot build a morphism through the chart embedding {chart_embedding}: it is not the "
                f"embedding of chart {chart_embedding.chart_index()} chosen when the scheme was glued"
            )
        if chart_map.codomain() is not chart_embedding.domain():
            raise ValueError(
                f"cannot build a morphism through the chart embedding {chart_embedding}: the map "
                f"{chart_map} must land in the chart {chart_embedding.domain()}, but it lands in "
                f"{chart_map.codomain()}"
            )
        if chart_map.domain() is not self.domain() or chart_embedding.codomain() is not self.codomain():
            raise ValueError(
                f"cannot make the composite of {chart_map} and {chart_embedding} a morphism "
                f"{self.domain()} -> {self.codomain()}: it is a morphism {chart_map.domain()} -> "
                f"{chart_embedding.codomain()}"
            )
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

    def _in_mor(self, mor):
        chart_map = mor.mor_category().Mor(self.domain(), self.chart_embedding().domain())(self.chart_map())
        return _GluedSchemeChartMap(mor, self.chart_embedding(), chart_map)

    def __mul__(self, other):
        composite = self.chart_map() * other
        if composite is NotImplemented:
            return NotImplemented
        return _GluedSchemeChartMap(
            _scheme_composition_mor(self, other), self.chart_embedding(), composite,
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
        super().__init__(None, mor=parent, cone_construction=cone_construction)
        datum = self.parent().gluing_datum()
        raw_local_maps = _family_on_finite_ordered_set(
            datum.chart_index_set(),
            local_maps,
            name="Raw local maps of a glued-scheme morphism",
            noun="a glued-scheme morphism",
        )
        schemes = self.parent().mor_category()
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
                    f"the local morphisms of a morphism {self.domain()} -> {self.codomain()} do not glue: on "
                    f"the overlap of charts {left_index} and {right_index} they disagree after the chart change"
                )

    def _postcompose_with(self, after):
        if after.domain() is not self.codomain():
            return NotImplemented
        return _scheme_composition_mor(after, self)(
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


class _FiniteAtlasSchemeMorphism(SchemeMorphism):
    r"""A morphism glued from compatible maps on a selected finite affine atlas.

    Unlike :class:`_GluedSchemeMorphism`, the domain need not itself use the
    gluing realization privately.  This is the descent statement for maps out
    of any represented scheme carrying a finite affine atlas, such as a
    projective or multiprojective scheme with its standard atlas.
    """

    def __init__(self, parent, atlas, local_maps) -> None:
        super().__init__(None, mor=parent)
        match atlas.scheme() is self.domain():
            case True:
                pass
            case False:
                raise ValueError(
                    f"cannot build a morphism out of {self.domain()} from local maps on {atlas}: the atlas must "
                    f"cover {self.domain()}, but it covers {atlas.scheme()}"
                )
        self._atlas = atlas
        raw = _family_on_finite_ordered_set(
            atlas.chart_index_set(),
            local_maps,
            name="Raw local maps of a finite-atlas scheme morphism",
            noun="a finite-atlas scheme morphism",
        )
        schemes = self.parent().mor_category()
        self._local_maps = finite_indexed_family(
            atlas.chart_index_set(),
            lambda index: schemes.Mor(atlas.chart(index), self.codomain())(
                raw[index]
            ),
            name="Local maps of a finite-atlas scheme morphism",
        )
        self._verify_overlap_compatibility()

    def atlas(self):
        return self._atlas

    def local_maps(self):
        return self._local_maps

    def local_map(self, index):
        return self.local_maps()[self.atlas().normalize_chart_index(index)]

    def _verify_overlap_compatibility(self) -> None:
        atlas = self.atlas()
        for left_index, right_index in atlas.transition_index_set():
            left_overlap = atlas.overlap(left_index, right_index)
            right_overlap = atlas.overlap(right_index, left_index)
            transition = atlas.transition_between(left_index, right_index).forward()
            left = self.local_map(left_index) * left_overlap.inclusion()
            right = self.local_map(right_index) * right_overlap.inclusion() * transition
            match left == right:
                case True:
                    pass
                case False:
                    raise ValueError(
                        f"the local morphisms of a morphism {self.domain()} -> {self.codomain()} do not glue: on "
                        f"the overlap of charts {left_index} and {right_index} they disagree after the chart change"
                    )

    def _postcompose_with(self, after):
        match after.domain() is self.codomain():
            case True:
                pass
            case False:
                return NotImplemented
        return _FiniteAtlasSchemeMorphism(
            _scheme_composition_mor(after, self),
            self.atlas(),
            self.local_maps().map(lambda local_map: after * local_map),
        )

    def __mul__(self, other):
        match other:
            case SchemeMorphism():
                pass
            case _:
                return NotImplemented
        match (
            other.codomain() is self.domain(),
            self._is_the_identity(),
            other._is_the_identity(),
        ):
            case (False, _, _):
                return NotImplemented
            case (True, True, _):
                return other
            case (True, False, True):
                return self
            case _:
                pass
        return other._postcompose_with(self)

    def __eq__(self, other) -> bool:
        match other:
            case _ if self is other:
                return True
            case SchemeMorphism() if (
                other.domain() is self.domain()
                and other.codomain() is self.codomain()
            ):
                pass
            case _:
                return False
        match other:
            case _FiniteAtlasSchemeMorphism() if other.atlas() is self.atlas():
                return all(
                    self.local_map(index) == other.local_map(index)
                    for index in self.atlas().chart_indices()
                )
            case _ if other._is_the_identity():
                return all(
                    self.local_map(index) == self.atlas().chart_embedding(index)
                    for index in self.atlas().chart_indices()
                )
            case _:
                pass
        try:
            return all(
                self.local_map(index)
                == other * self.atlas().chart_embedding(index)
                for index in self.atlas().chart_indices()
            )
        except (AttributeError, TypeError, ValueError):
            return False

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None


def _finite_atlas_scheme_morphism(domain, codomain, atlas, local_maps):
    r"""Construct a scheme morphism by descent from compatible atlas maps."""
    return _FiniteAtlasSchemeMorphism(
        Schemes(domain.scheme_base_ring()).Mor(domain, codomain),
        atlas,
        local_maps,
    )


class _GluedSchemeMorCategory(SchemeMorCategory):
    r"""Maps out of a glued scheme, represented by compatible local maps on its charts.

    The gluing datum of the domain is retained by this Mor: a map out of the
    glued scheme is a family of maps out of its charts agreeing through the
    transitions, so every element reads the charts from it.
    """

    def __init__(self, mor_family, domain, codomain) -> None:
        self._gluing_datum = domain.gluing_datum()
        super().__init__(mor_family, domain, codomain)

    def gluing_datum(self):
        return self._gluing_datum

    def _element_constructor_(self, datum):
        if isinstance(datum, _GluedSchemeMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError(
                    f"cannot make {datum} a morphism {self.domain()} -> {self.codomain()}: it is a morphism "
                    f"{datum.domain()} -> {datum.codomain()}"
                )
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
            raise ValueError(
                f"{self} has no identity: its domain {self.domain()} is not its codomain {self.codomain()}"
            )
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
        inclusion_datum=lambda mor: _GluedSchemeOpenInclusion(mor, datum, index),
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
    the datum through :meth:`gluing_datum` and asks this realization for the Mor
    out of ``X`` (:meth:`scheme_mor_class`), the structure morphism
    (:meth:`structure_morphism`) and the chartwise constructions.
    """

    def __init__(self, gluing_datum, native_realization=None) -> None:
        self._gluing_datum = gluing_datum
        self._native_realization = native_realization

    def gluing_datum(self):
        return self._gluing_datum

    def _native_realization_for_scheme_adapter(self):
        r"""The optional native scheme of this same atlas, supplied by its construction."""
        assert self._native_realization is not None, (
            f"{self} has no Sage scheme: the scheme glued from it was not constructed with one"
        )
        return self._native_realization

    def scheme_mor_class(self):
        r"""The compatible-chart-map realization of the Mor chosen by its family."""
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
            raise TypeError(
                f"cannot glue {left_chart} and {right_chart}: gluing two charts is computed here only for "
                f"affine charts over {base}, but they are objects of {left_chart.category()} and "
                f"{right_chart.category()}"
            )
        if transition not in _scheme_core_mor(transition):
            raise TypeError(
                f"cannot glue {left_chart} and {right_chart} along {transition}: it must be an isomorphism "
                "of schemes between the two overlaps"
            )
        forward = transition.forward()
        inverse = transition.inverse()
        left_overlap = forward.domain()
        right_overlap = forward.codomain()
        if left_overlap not in OpenImmersions(left_chart):
            raise ValueError(
                f"cannot glue {left_chart} and {right_chart}: the domain {left_overlap} of the chart change "
                f"must be an open subscheme of {left_chart}"
            )
        if right_overlap not in OpenImmersions(right_chart):
            raise ValueError(
                f"cannot glue {left_chart} and {right_chart}: the codomain {right_overlap} of the chart "
                f"change must be an open subscheme of {right_chart}"
            )
        if inverse.domain() is not right_overlap or inverse.codomain() is not left_overlap:
            raise ValueError(
                f"cannot glue {left_chart} and {right_chart}: the inverse chart change must be "
                f"{right_overlap} -> {left_overlap}, but it is {inverse.domain()} -> {inverse.codomain()}"
            )
        if inverse * forward != left_overlap.categorical_identity_morphism():
            raise ValueError(
                f"cannot glue {left_chart} and {right_chart}: the chart change {forward} followed by its "
                f"stated inverse {inverse} is not the identity of {left_overlap}"
            )
        if forward * inverse != right_overlap.categorical_identity_morphism():
            raise ValueError(
                f"cannot glue {left_chart} and {right_chart}: the stated inverse {inverse} followed by the "
                f"chart change {forward} is not the identity of {right_overlap}"
            )

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
        return self.chart_index_set().cardinality()

    def chart_indices(self):
        return self.chart_index_set()

    def transition(self):
        return self._transition

    def transition_between(self, source_index, target_index):
        source_index = int(self.normalize_chart_index(source_index))
        target_index = int(self.normalize_chart_index(target_index))
        if source_index == target_index:
            raise ValueError(
                f"there is no chart change from chart {source_index} of {self} to itself: a chart change "
                "joins two distinct charts"
            )
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
                raise TypeError(
                    f"cannot glue a scheme from the charts {self._charts}: gluing is computed here only for "
                    f"affine charts over {self.base_ring()}, but {chart} is an object of {chart.category()}"
                )

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
        return self.chart_index_set().cardinality()

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
            raise ValueError(
                f"there is no chart change from chart {left_index} of {self} to itself: a chart change "
                "joins two distinct charts"
            )
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
            if transition not in _scheme_core_mor(transition):
                raise TypeError(
                    f"cannot glue along {transition} from chart {source_index} to chart {target_index}: it "
                    "must be an isomorphism of schemes between the two overlaps"
                )
            forward = transition.forward()
            inverse = transition.inverse()
            source_overlap = forward.domain()
            target_overlap = forward.codomain()
            source_chart = self.chart(source_index)
            target_chart = self.chart(target_index)
            if source_overlap not in OpenImmersions(source_chart):
                raise ValueError(
                    f"cannot glue along the chart change from chart {source_index} to chart {target_index}: "
                    f"its domain {source_overlap} must be an open subscheme of the chart {source_chart}"
                )
            if target_overlap not in OpenImmersions(target_chart):
                raise ValueError(
                    f"cannot glue along the chart change from chart {source_index} to chart {target_index}: "
                    f"its codomain {target_overlap} must be an open subscheme of the chart {target_chart}"
                )
            if not source_overlap.is_distinguished_open() or not target_overlap.is_distinguished_open():
                raise TypeError(
                    f"cannot glue along the chart change from chart {source_index} to chart {target_index}: "
                    "gluing is computed here only when both overlaps are distinguished open subschemes D(f) "
                    f"of their charts, and {source_overlap} or {target_overlap} is not known to be one"
                )
            if inverse.domain() is not target_overlap or inverse.codomain() is not source_overlap:
                raise ValueError(
                    f"cannot glue along the chart change from chart {source_index} to chart {target_index}: "
                    f"the inverse chart change must be {target_overlap} -> {source_overlap}, but it is "
                    f"{inverse.domain()} -> {inverse.codomain()}"
                )
            if inverse * forward != source_overlap.categorical_identity_morphism():
                raise ValueError(
                    f"cannot glue along the chart change from chart {source_index} to chart {target_index}: "
                    f"{forward} followed by its stated inverse {inverse} is not the identity of {source_overlap}"
                )
            if forward * inverse != target_overlap.categorical_identity_morphism():
                raise ValueError(
                    f"cannot glue along the chart change from chart {source_index} to chart {target_index}: "
                    f"the stated inverse {inverse} followed by {forward} is not the identity of {target_overlap}"
                )

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
            raise ValueError(
                f"there is no triple overlap of the charts {source_index}, {middle_index} and "
                f"{target_index} of {self}: a triple overlap needs three distinct charts"
            )
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
                f"the chart change from chart {source_index} to chart {target_index} of {self} does not map "
                f"the triple overlap with chart {third_index} into the triple overlap {target_triple}"
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
                    f"the chart changes between charts {source_index} and {target_index} of {self} are not "
                    f"mutually inverse on the triple overlap with chart {third_index}"
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
                raise ValueError(
                    f"the chart changes of {self} fail the cocycle condition on the triple overlap of charts "
                    f"{left_index}, {middle_index} and {right_index}"
                )

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

    @cached_method
    def cech_site(self):
        r"""The finite Čech site of this represented affine atlas.

        Objects are the covered-scheme label ``()``, chart labels ``(i,)``,
        and one selected pair-overlap label ``(i,j)`` for each atlas pair.
        The pair is an abstract site object: its module value uses the retained
        source-side overlap presentation and the right restriction composes
        with the atlas transition, so distinct overlap rings are not identified.
        """
        labels = [()]
        labels.extend((index,) for index in self.chart_index_set())
        labels.extend(tuple(pair) for pair in self.transition_index_set())
        return PosetCategory(
            finite_ordered_set(tuple(labels)),
            le=lambda finer, coarser: set(coarser).issubset(set(finer)),
        )

    @cached_method
    def cech_covering_family(self):
        r"""The atlas chart family as the selected cover of :meth:`cech_site`."""
        site = self.cech_site()
        category = _CechCoveringFamilies(self)
        target = site(())
        members = finite_indexed_family(
            self.chart_index_set(),
            lambda index: site.Mor(site((index,)), target).unique(),
            name="Finite-atlas Čech cover arrows",
        )
        overlaps = {
            tuple(pair): (
                site(tuple(pair)),
                site.Mor(site(tuple(pair)), site((pair[0],))).unique(),
                site.Mor(site(tuple(pair)), site((pair[1],))).unique(),
            )
            for pair in self.transition_index_set()
        }
        return category.family(target, members, overlaps)

    @cached_method
    def cech_coverage(self):
        r"""The coverage generated by this atlas's finite Čech family."""
        return Coverage(
            self.cech_site(),
            _CechCoveringFamilies(self),
        )

    @cached_method
    def structure_module_datum(self):
        r"""The rank-one module descent datum presenting ``O_X`` on this atlas."""
        return FiniteAtlasModuleGluingData(self).structure_module_datum()

    @staticmethod
    def _rank_one_coefficient(module, element):
        r"""The coefficient of ``element`` in a represented rank-one free module."""
        labels = _finite_framing(module)
        assert labels.cardinality().finite_value() == 1, (
            f"cannot read the coefficient of {element} in {module}: the module must be free of rank "
            f"one, but it has {labels.cardinality()} chosen module generators"
        )
        label = next(iter(labels))
        return module.framing_coefficients(module(element)).get(
            label,
            module.base_ring().zero(),
        )

    @cached_method
    def global_function_algebra(self):
        r"""Return ``O(X)=Gamma(X,O_X)`` with its chartwise algebra structure.

        The underlying ``R``-module is the selected Čech equalizer of the
        rank-one structure-module datum.  Multiplication and the unit are
        induced componentwise from the chart coordinate rings, so the result
        enters the ordinary commutative ``R``-algebra constructor rather than
        becoming a second global-section parent.
        """
        datum = self.structure_module_datum()
        module = datum.base_restricted_sections()
        base = self.scheme().scheme_base_ring()
        tensor_square = Modules(base).tensor_product((module, module))

        def product(left, right):
            components = {}
            for index in self.chart_index_set():
                local = datum.local_module(index)
                label = next(iter(_finite_framing(local)))
                left_component = datum.base_restricted_section_component(left, index)
                right_component = datum.base_restricted_section_component(right, index)
                coefficient = (
                    self._rank_one_coefficient(local, left_component)
                    * self._rank_one_coefficient(local, right_component)
                )
                components[index] = local.scalar_multiple(
                    coefficient,
                    local.module_generator(label),
                )
            return datum.base_restricted_section(components)

        multiplication = tensor_square.from_bilinear_map(module, product)
        unit = datum.base_restricted_section(
            {
                index: datum.local_module(index).module_generator(
                    next(iter(_finite_framing(datum.local_module(index))))
                )
                for index in self.chart_index_set()
            }
        )
        return Algebras(base).Associative().Unital().Commutative()(
            module,
            multiplication,
            unit,
        )

    @cached_method
    def global_function_restriction(self, index):
        r"""Return ``O(X) -> O(U_i)`` for one chart of this finite atlas."""
        index = self.normalize_chart_index(index)
        functions = self.global_function_algebra()
        underlying = functions.unformed_module()
        datum = self.structure_module_datum()
        target = self.chart(index).coordinate_algebra()
        base = self.scheme().scheme_base_ring()

        def image(section):
            component = datum.base_restricted_section_component(
                underlying(section),
                index,
            )
            return target(self._rank_one_coefficient(datum.local_module(index), component))

        linear = _CanonicalDescentRestrictionMorphism(
            Modules(base).Mor(functions, target),
            image,
        )
        return _algebra_mor(functions, target)(linear)

    @cached_method
    def global_function_overlap_restriction(self, source_index, target_index):
        r"""Return ``O(X) -> O(U_ij)`` in the source-chart overlap presentation."""
        source_index = self.normalize_chart_index(source_index)
        target_index = self.normalize_chart_index(target_index)
        overlap = self.overlap(source_index, target_index)
        functions = self.global_function_algebra()
        chart_restriction = self.global_function_restriction(source_index)
        overlap_restriction = overlap.inclusion().coordinate_algebra_morphism()
        target = overlap.coordinate_algebra()
        base = self.scheme().scheme_base_ring()
        linear = _CanonicalDescentRestrictionMorphism(
            Modules(base).Mor(functions, target),
            lambda section: target(overlap_restriction(chart_restriction(section))),
        )
        return _algebra_mor(functions, target)(linear)

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
            raise ValueError(
                f"cannot build a refinement of {coarse_datum} by {fine_datum}: they must be atlases of one "
                f"scheme, but they cover {coarse_datum.scheme()} and {fine_datum.scheme()}"
            )
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
            slice_mor = site.Mor(fine_member, coarse_member)
            match chart_map in slice_mor:
                case True:
                    normalized_chart_maps[fine_index] = chart_map
                case False:
                    if chart_map not in scheme_category.Mor(fine_chart, coarse_chart):
                        raise TypeError(
                            f"cannot build a refinement of {coarse_datum} by {fine_datum}: the map {chart_map} given "
                            f"on the fine chart {fine_index} must be a morphism of schemes {fine_chart} -> {coarse_chart}"
                        )
                    normalized_chart_maps[fine_index] = slice_mor(chart_map)
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
                    f"the chart maps of the refinement {self} do not commute with the chart changes on the "
                    f"overlap of the fine charts {source_index} and {target_index}"
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
            raise ValueError(
                f"cannot pull {descent} back along the refinement {self}: it is descent data on "
                f"{descent.gluing_datum()}, not on the coarse atlas {self.coarse_datum()}"
            )
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
            raise ValueError(
                f"cannot pull {line_bundle} back along the refinement {self}: it is a line bundle on "
                f"{line_bundle.gluing_datum()}, not on the coarse atlas {self.coarse_datum()}"
            )
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


class FiniteAtlasMor(CoveringFamilyMor):
    r"""Refinements/comparisons between two finite affine atlases."""

    Element = FiniteAtlasRefinement

    def _element_constructor_(self, index_map, chart_maps=None, *, target_map=None):
        match index_map:
            case FiniteAtlasRefinement() if chart_maps is None and target_map is None:
                if index_map.parent() is self:
                    return index_map
                if index_map.domain() is not self.domain() or index_map.codomain() is not self.codomain():
                    raise ValueError(
                        f"cannot make {index_map} a refinement {self.domain()} -> {self.codomain()}: it is a "
                        f"refinement {index_map.domain()} -> {index_map.codomain()}"
                    )
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
            raise TypeError(
                f"cannot build a refinement {self.domain()} -> {self.codomain()} from {index_map}: a map "
                "from each fine chart to its coarse chart must be given"
            )
        return self.element_class(
            self,
            index_map,
            chart_maps,
            target_map=target_map,
        )


class FiniteAtlasMorCategoryConstruction(CoveringFamilyMorCategoryConstruction):
    r"""The Mor family of finite affine atlases."""

    def fixed_category_class(self):
        return FiniteAtlasMor


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

    _MorCategory = FiniteAtlasMorCategoryConstruction

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
            raise ValueError(
                f"cannot read the gluing {presentation} as an affine atlas in {self}: it is over "
                f"{presentation.base_ring()}, but {self} is over {self.base_ring()}"
            )
        scheme = self.scheme()
        indices = presentation.chart_index_set()
        if chart_embeddings is None:
            if presentation.scheme() is not scheme:
                raise ValueError(
                    f"cannot read the gluing {presentation} as an affine atlas of {scheme}: it glues "
                    f"{presentation.scheme()}, so the embeddings of its charts into {scheme} must be given"
                )
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
                raise TypeError(
                    f"cannot read the gluing {presentation} as an affine atlas of {scheme}: its chart {index} "
                    f"is {chart}, which is not affine; it is an object of {chart.category()}"
                )
            if embedding.is_open_immersion() is not True:
                raise TypeError(
                    f"cannot read the gluing {presentation} as an affine atlas of {scheme}: the embedding "
                    f"{embedding} of chart {index} is not known to be an open immersion"
                )
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
            f"{self} has no example object: an example atlas is chosen here only for an affine "
            f"scheme, but {scheme} is an object of {scheme.category()}"
        )
        identity = scheme.Mor(scheme).identity()
        return self(
            (scheme,),
            {},
            (identity,),
        )


def _finite_atlas_quasi_coherent_sheaves(atlas):
    r"""The concrete sheaf/QCoh intersection for one finite-atlas presentation."""
    scheme = atlas.scheme()
    return Category.join(
        (
            atlas.cech_coverage().sheaves(Modules(atlas.global_function_algebra())),
            QuasiCoherentSheaves(scheme),
        )
    )


def _finite_atlas_of_sheaf_placement(sheaf):
    r"""Read the selected finite atlas from the sheaf's concrete category placement."""
    for placement in sheaf.category().all_super_categories(proper=False):
        match placement:
            case Sheaves():
                match placement.coverage():
                    case _CechCoveringFamilies() as coverage:
                        return coverage.presentation()
                    case _:
                        pass
            case _:
                pass
    raise TypeError(
        f"cannot find the finite affine atlas of {sheaf}: it is not a sheaf for the Čech coverage "
        f"of a finite affine atlas; it is an object of {sheaf.category()}"
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
                raise ArithmeticError(
                    f"the refinement {refinement} changes the rank of the line bundle {coarse_bundle} on the "
                    f"fine chart {fine_index}: the pulled-back module has {len(pulled_labels)} module "
                    f"generators, but the refined module has {len(refined_labels)}"
                )
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
        raise TypeError(
            f"cannot glue the module {module} as local data on an affine chart: descent is computed "
            "here only for modules with a chosen finite set of module generators, and "
            f"{module} has no chosen module generators"
        )
    labels = module.module_generating_set()
    if not labels.cardinality().is_finite():
        raise TypeError(
            f"cannot glue the module {module} as local data on an affine chart: descent is computed "
            "here only for modules with a chosen finite set of module generators, but "
            f"{module} has {labels.cardinality()}"
        )
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
    therefore checked by the existing algebra-Mor owner, while composition
    retains the composed scalar map.
    """

    def __init__(self, source, target, scalar_map, images) -> None:
        if scalar_map.domain() is not source.base_ring():
            raise ValueError(
                f"cannot build a semilinear map {source} -> {target} over {scalar_map}: the ring map must "
                f"start at the base ring {source.base_ring()} of {source}, but it starts at "
                f"{scalar_map.domain()}"
            )
        if scalar_map.codomain() is not target.base_ring():
            raise ValueError(
                f"cannot build a semilinear map {source} -> {target} over {scalar_map}: the ring map must "
                f"end at the base ring {target.base_ring()} of {target}, but it ends at "
                f"{scalar_map.codomain()}"
            )
        labels = source.algebra_generating_set()
        if not labels.cardinality().is_finite():
            raise TypeError(
                f"cannot build a semilinear map {source} -> {target}: {source} must have finitely many "
                f"chosen algebra generators, but it has {labels.cardinality()}"
            )
        self._source = source
        self._target = target
        self._scalar_map = scalar_map
        self._restricted_target = target.restrict_scalars(scalar_map)
        supplied = (
            {label: images(label) for label in labels}
            if callable(images)
            else dict(images)
        )
        self._morphism = _algebra_mor(source, self._restricted_target)(
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
            raise ValueError(
                f"cannot factor {morphism} through the scalar extension {self.target()} of "
                f"{self.source()}: it must be a map out of {self.source()}, but it starts at "
                f"{morphism.domain()}"
            )
        source_structure = self.source().algebra_structure_morphism()
        scalar_restriction = self.source().base_ring().Mor(morphism.codomain())(
            lambda scalar: morphism(source_structure(scalar)),
        )
        target_scalars = self.target().base_ring()
        assert target_scalars in LocalizationRings(), (
            f"cannot factor {morphism} through the scalar extension {self.target()}: this is computed "
            f"here only when the new base ring is a localization, but {target_scalars} is an object "
            f"of {target_scalars.category()}"
        )
        localization_source = target_scalars.localization_source()
        source_scalars = self.source().base_ring()
        localization_steps = []
        current = source_scalars
        while current is not localization_source:
            if current not in LocalizationRings():
                raise ValueError(
                    f"cannot factor {morphism} through the scalar extension {self.target()}: the base ring "
                    f"{source_scalars} of {self.source()} must be an iterated localization of "
                    f"{localization_source}, but {current} is not a localization"
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
            raise ValueError(
                f"cannot factor {morphism} through the scalar extension {self.target()} of "
                f"{self.source()}: the two algebras must have the same chosen algebra generators, but "
                f"they have {source_labels} and {target_labels}"
            )
        algebra_factor = _algebra_mor(self.target(), target_view)(
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
            raise ValueError(
                f"cannot read {morphism} as a semilinear algebra map: {source} and {target} must have one "
                f"base ring, but their base rings are {source.base_ring()} and {target.base_ring()}"
            )
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
        if scheme_transition not in _scheme_core_mor(scheme_transition):
            raise TypeError(
                f"cannot build an algebra chart change over {scheme_transition}: it must be an isomorphism "
                "of schemes between the two overlaps"
            )
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
            raise ValueError(
                f"cannot build an algebra chart change over {scheme_transition}: the pullback {pullback} "
                f"must be a map {target_algebra} -> {source_algebra} over {forward_scalar}, but it is a "
                f"map {pullback.source()} -> {pullback.target()} over {pullback.scalar_map()}"
            )
        if (
            inverse_pullback.source() is not source_algebra
            or inverse_pullback.target() is not target_algebra
            or inverse_pullback.scalar_map() != reverse_scalar
        ):
            raise ValueError(
                f"cannot build an algebra chart change over {scheme_transition}: the inverse pullback "
                f"{inverse_pullback} must be a map {source_algebra} -> {target_algebra} over "
                f"{reverse_scalar}, but it is a map {inverse_pullback.source()} -> "
                f"{inverse_pullback.target()} over {inverse_pullback.scalar_map()}"
            )
        if pullback * inverse_pullback != SemilinearAlgebraMorphism.identity(source_algebra):
            raise ValueError(
                f"cannot build an algebra chart change over {scheme_transition}: the stated inverse "
                f"{inverse_pullback} followed by the pullback {pullback} is not the identity of "
                f"{source_algebra}"
            )
        if inverse_pullback * pullback != SemilinearAlgebraMorphism.identity(target_algebra):
            raise ValueError(
                f"cannot build an algebra chart change over {scheme_transition}: the pullback {pullback} "
                f"followed by its stated inverse {inverse_pullback} is not the identity of {target_algebra}"
            )

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
        if scheme_transition not in _scheme_core_mor(scheme_transition):
            raise TypeError(
                f"cannot build a module chart change over {scheme_transition}: it must be an isomorphism "
                "of schemes between the two overlaps"
            )
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
            raise ValueError(
                f"cannot build a module chart change over {scheme_transition}: the pullback {pullback} "
                f"must be a map {target_module} -> {source_module} over {forward_scalar}, but it is a map "
                f"{pullback.source()} -> {pullback.target()} over {pullback.scalar_map()}"
            )
        if (
            inverse_pullback.source() is not source_module
            or inverse_pullback.target() is not target_module
            or inverse_pullback.scalar_map() != reverse_scalar
        ):
            raise ValueError(
                f"cannot build a module chart change over {scheme_transition}: the inverse pullback "
                f"{inverse_pullback} must be a map {source_module} -> {target_module} over "
                f"{reverse_scalar}, but it is a map {inverse_pullback.source()} -> "
                f"{inverse_pullback.target()} over {inverse_pullback.scalar_map()}"
            )
        if pullback * inverse_pullback != SemilinearModuleMorphism.identity(source_module):
            raise ValueError(
                f"cannot build a module chart change over {scheme_transition}: the stated inverse "
                f"{inverse_pullback} followed by the pullback {pullback} is not the identity of "
                f"{source_module}"
            )
        if inverse_pullback * pullback != SemilinearModuleMorphism.identity(target_module):
            raise ValueError(
                f"cannot build a module chart change over {scheme_transition}: the pullback {pullback} "
                f"followed by its stated inverse {inverse_pullback} is not the identity of {target_module}"
            )

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
                raise ValueError(
                    f"cannot glue the local modules over {gluing_datum}: the module {module} on chart {index} "
                    f"must be a module over the coordinate algebra "
                    f"{gluing_datum.chart(index).coordinate_algebra()} of that chart, but its base ring is "
                    f"{module.base_ring()}"
                )
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
            raise ValueError(
                f"cannot build a map {domain} -> {codomain} from the images {supplied}: exactly one image "
                f"must be given for each chosen module generator of {domain}"
            )
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
                raise ValueError(
                    f"the module chart changes of {self} fail the cocycle condition on the triple overlap of "
                    f"charts {left}, {middle} and {right}"
                )

    def restricted_local_map(self, target_datum, chart_index, other_index, local_map):
        r"""Restrict one chart-linear map to the source-side pair overlap."""
        if target_datum.gluing_datum() is not self.gluing_datum():
            raise ValueError(
                f"cannot restrict a local map into {target_datum}: it is glued over "
                f"{target_datum.gluing_datum()}, but {self} is glued over {self.gluing_datum()}; both must "
                "use one affine atlas"
            )
        chart_index = self.gluing_datum().normalize_chart_index(chart_index)
        other_index = self.gluing_datum().normalize_chart_index(other_index)
        if (
            local_map.domain() is not self.local_module(chart_index)
            or local_map.codomain() is not target_datum.local_module(chart_index)
        ):
            raise ValueError(
                f"cannot restrict {local_map} on chart {chart_index}: it must be a map "
                f"{self.local_module(chart_index)} -> {target_datum.local_module(chart_index)}, but it is "
                f"{local_map.domain()} -> {local_map.codomain()}"
            )
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
        return QuasiCoherentSheaves(self.scheme()).Mor(
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
    def descent_presheaf(self):
        r"""Return this finite-atlas datum as a presheaf on its Čech site."""
        return _FiniteAtlasModuleCechPresheaf(self)

    @cached_method
    def descent_data(self) -> DescentData:
        r"""Return the selected descent comparison for the finite Čech cover."""
        presheaf = self.descent_presheaf()
        selected_cover = self.gluing_datum().cech_covering_family()

        def inverse_for(equalizer):
            match equalizer.covering_family() is selected_cover:
                case True:
                    pass
                case False:
                    raise ValueError(
                        f"cannot compare {self} with the equalizer {equalizer}: it is taken over the covering "
                        f"family {equalizer.covering_family()}, not over the Čech cover {selected_cover} of "
                        f"{self.gluing_datum()}"
                    )
            global_sections = self.compatible_sections()
            return global_sections.Mor(global_sections).identity()

        return DescentData(
            self.gluing_datum().cech_coverage(),
            presheaf,
            inverse_for,
            equalizer_for=presheaf.selected_equalizer_construction,
        )

    def _construct_sheaf(
        self,
        *,
        categories=(),
        construction_data=None,
        _engine,
    ):
        r"""Construct the represented sheaf through the concrete Čech sheaf owner."""
        atlas = self.gluing_datum()
        sheaves = atlas.cech_coverage().sheaves(Modules(atlas.global_function_algebra()))
        data = dict(construction_data or {})
        match "module_gluing_datum" in data:
            case True:
                raise ValueError(
                    f"cannot construct the sheaf glued from {self}: its module gluing data are determined by "
                    f"{self} and must not be given again"
                )
            case False:
                pass
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
        return self._construct_sheaf(_engine=_FiniteAtlasModuleSheafEngine)

    def sheaf(self, *, categories=(), construction_data=None, _engine=None):
        r"""Return the quasi-coherent sheaf represented by this finite-atlas descent datum.

        Construction passes through the actual sheaf category of the finite
        Čech coverage and adds ``QuasiCoherentSheaves(X)`` as semantic
        placement.  The chosen atlas datum remains first-class construction
        data rather than defining another category of sheaves.
        """
        match (bool(categories), construction_data is None, _engine is None):
            case (False, True, True):
                return self._canonical_sheaf()
            case _:
                pass
        match _engine:
            case None:
                selected_engine = _FiniteAtlasModuleSheafEngine
            case _:
                selected_engine = _engine
        return self._construct_sheaf(
            categories=categories,
            construction_data=construction_data,
            _engine=selected_engine,
        )

    def chart_index_set(self):
        return self.gluing_datum().chart_index_set()

    def restrict_scalar_to_chart(self, chart_index, scalar):
        r"""The image of a global function in the section ring of one chart."""
        return self.gluing_datum().global_function_restriction(chart_index)(scalar)

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
                raise ValueError(
                    f"the local sections {sections} do not glue: on the overlap of charts {source_index} and "
                    f"{target_index} they disagree after the chart change"
                )
        return components

    @cached_method
    def base_restricted_local_section_product_construction(self):
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
    def base_restricted_matching_section_product_construction(self):
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

    def _base_restricted_matching_section_leg(self, pair, side):
        r"""One finite-atlas Čech leg from chart sections to a source-side overlap."""
        source_index, target_index = tuple(pair)
        local_product = self.base_restricted_local_section_product_construction()
        matching_product = self.base_restricted_matching_section_product_construction()
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
                raise ValueError(
                    f"cannot form the leg of the Čech diagram at the pair {pair}: the side must be 'left' or "
                    f"'right', but it is {side!r}"
                )

        local_factor = local_factors.value(chart_index)
        restriction = _CanonicalDescentRestrictionMorphism(
            local_factor.module_category().Mor(
                local_factor,
                matching_factor,
            ),
            image,
        )
        projection = local_product.structure_morphism(
            local_product.diagram().domain()(chart_index)
        )
        return restriction * projection

    @cached_method
    def base_restricted_sections_construction(self):
        r"""Return the selected equalizer defining finite-atlas global sections over the base ring."""
        base = self.scheme().scheme_base_ring()
        modules = Modules(base)
        local_product = self.base_restricted_local_section_product_construction()
        matching_product = self.base_restricted_matching_section_product_construction()
        matching_diagram = matching_product.diagram()

        def side_map(side):
            cone = matching_diagram.Cones().cone(
                local_product.object(),
                lambda index: self._base_restricted_matching_section_leg(index.value(), side),
            )
            return matching_product.factor(cone).apex_map()

        return modules.equalizer_construction(
            side_map("left"),
            side_map("right"),
        )

    @cached_method
    def base_restricted_sections(self):
        r"""Return ``Gamma(X, F)`` over the base ring of the glued scheme."""
        return self.base_restricted_sections_construction().object()

    def base_restricted_section(self, sections):
        r"""Construct a finite-atlas global section from compatible chart components."""
        components = self.compatible_local_sections(sections)
        base = self.scheme().scheme_base_ring()
        modules = Modules(base)
        local_product = self.base_restricted_local_section_product_construction()
        factors = local_product.diagram().diagram_objects()
        restricted_components = finite_indexed_family(
            self.chart_index_set(),
            lambda index: factors.value(index)(components[index]),
            name="Finite-atlas section components over the scheme base ring",
        )
        product_element = modules.product_element(local_product, restricted_components)
        return modules.equalizer_element(
            self.base_restricted_sections_construction(),
            product_element,
        )

    def base_restricted_section_component(self, section, chart_index):
        r"""Project a finite-atlas global section to one chart component."""
        chart_index = self.gluing_datum().normalize_chart_index(chart_index)
        construction = self.base_restricted_sections_construction()
        shape = construction.diagram().domain()
        local_element = construction.structure_morphism(shape.source())(section)
        component = Modules(self.scheme().scheme_base_ring()).product_component(
            self.base_restricted_local_section_product_construction(),
            local_element,
            chart_index,
        )
        return self.local_module(chart_index)(component.underlying_element())

    @cached_method
    def local_section_product_construction(self):
        r"""Return ``prod_i F(U_i)`` in ``Modules(O(X))``."""
        atlas = self.gluing_datum()
        functions = atlas.global_function_algebra()
        factors = finite_indexed_family(
            self.chart_index_set(),
            lambda index: self.local_module(index).restrict_scalars(
                atlas.global_function_restriction(index)
            ),
            name="Finite-atlas chart modules over O(X)",
        )
        return Modules(functions).product_construction(factors)

    @cached_method
    def matching_section_product_construction(self):
        r"""Return ``prod_{i<j} F(U_ij)`` in ``Modules(O(X))``."""
        atlas = self.gluing_datum()
        functions = atlas.global_function_algebra()
        factors = finite_indexed_family(
            atlas.transition_index_set(),
            lambda pair: self.pair_module(*pair).restrict_scalars(
                atlas.global_function_overlap_restriction(*pair)
            ),
            name="Finite-atlas overlap modules over O(X)",
        )
        return Modules(functions).product_construction(factors)

    def _matching_section_leg(self, pair, side):
        r"""One Čech leg ``prod_i F(U_i) -> F(U_ij)`` over ``O(X)``."""
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
                raise ValueError(
                    f"cannot form the leg of the Čech diagram at the pair {pair}: the side must be 'left' or "
                    f"'right', but it is {side!r}"
                )

        local_factor = local_factors.value(chart_index)
        restriction = _CanonicalDescentRestrictionMorphism(
            local_factor.module_category().Mor(
                local_factor,
                matching_factor,
            ),
            image,
        )
        projection = local_product.structure_morphism(
            local_product.diagram().domain()(chart_index)
        )
        return restriction * projection

    @cached_method
    def compatible_sections_construction(self):
        r"""Return the selected Čech equalizer defining ``Gamma(X,F)`` in ``Modules(O(X))``."""
        functions = self.gluing_datum().global_function_algebra()
        modules = Modules(functions)
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
        r"""Return ``Gamma(X,F)`` as an ``O(X)``-module."""
        return self.compatible_sections_construction().object()

    def compatible_section(self, sections):
        r"""Construct a global section from one compatible family of chart sections."""
        components = self.compatible_local_sections(sections)
        functions = self.gluing_datum().global_function_algebra()
        modules = Modules(functions)
        local_product = self.local_section_product_construction()
        factors = local_product.diagram().diagram_objects()
        restricted_components = finite_indexed_family(
            self.chart_index_set(),
            lambda index: factors.value(index)(components[index]),
            name="Finite-atlas section components over O(X)",
        )
        product_element = modules.product_element(local_product, restricted_components)
        return modules.equalizer_element(
            self.compatible_sections_construction(),
            product_element,
        )

    def compatible_section_component(self, section, chart_index):
        r"""Project a global section to one affine-chart component."""
        chart_index = self.gluing_datum().normalize_chart_index(chart_index)
        construction = self.compatible_sections_construction()
        shape = construction.diagram().domain()
        local_element = construction.structure_morphism(shape.source())(section)
        functions = self.gluing_datum().global_function_algebra()
        component = Modules(functions).product_component(
            self.local_section_product_construction(),
            local_element,
            chart_index,
        )
        return self.local_module(chart_index)(component.underlying_element())

    def tensor_product(self, other):
        r"""Return the descent datum for the chartwise tensor product with ``other``."""
        if other.gluing_datum() is not self.gluing_datum():
            raise ValueError(
                f"cannot form the tensor product of {self} and {other}: they must be glued over one affine "
                f"atlas, but they are glued over {self.gluing_datum()} and {other.gluing_datum()}"
            )
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
            raise ValueError(
                f"cannot build a morphism of glued modules {source} -> {target}: they must be glued over "
                f"one affine atlas, but they are glued over {source.gluing_datum()} and "
                f"{target.gluing_datum()}"
            )
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
                raise ValueError(
                    f"cannot build a morphism of glued modules {source} -> {target}: the local map "
                    f"{local_map} on chart {index} must be {source.local_module(index)} -> "
                    f"{target.local_module(index)}, but it is {local_map.domain()} -> {local_map.codomain()}"
                )
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
            raise ValueError(
                f"cannot base change {local_map} along {ring_map}: {source} and {target} must be modules "
                f"over {ring_map.codomain()}, but they are modules over {source.base_ring()} and "
                f"{target.base_ring()}"
            )
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
            f"cannot glue the kernel of {self}: the kernels of its local maps must be free modules, "
            "and the kernel on chart "
            f"{next(index for index, kernel in local_kernels.items() if kernel.is_free() is not True)} "
            "is not known to be free"
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
            raise ValueError(
                f"cannot form the stalk map of {self} at {point}: the point must be a point of the chart "
                f"{chart_index}, {chart}, but it lies in {point.parent()}"
            )
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
                    f"the local maps of {self} do not glue: on the overlap of charts {source_index} and "
                    f"{target_index} they do not commute with the chart changes"
                )


class FiniteAtlasModuleSheafMorphism(FiniteAtlasModuleGluingMorphism):
    r"""The sheaf-endpoint realization of a finite-atlas descent morphism."""

    def source_datum(self):
        return self.domain().gluing_datum()

    def target_datum(self):
        return self.codomain().gluing_datum()

    def projectivization_map(self):
        r"""Return the induced map of projectivizations on the quotient-surjectivity locus."""
        from dzack_research.preamble.categories.schemes.relative_proj import (
            _projectivization_map,
        )

        return _projectivization_map(self)


class FiniteAtlasModuleSheafMor(CategoricalMor):
    r"""The represented Mor between two finite-atlas module sheaves."""

    Element = FiniteAtlasModuleSheafMorphism

    def _element_constructor_(self, local_maps):
        match local_maps:
            case FiniteAtlasModuleSheafMorphism() if local_maps.parent() is self:
                return local_maps
            case FiniteAtlasModuleSheafMorphism():
                if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                    raise ValueError(
                        f"cannot make {local_maps} a morphism {self.domain()} -> {self.codomain()}: it is a "
                        f"morphism {local_maps.domain()} -> {local_maps.codomain()}"
                    )
                local_maps = local_maps.local_maps()
            case _:
                pass
        return self.element_class(self, local_maps)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no identity: its domain {self.domain()} is not its codomain {self.codomain()}"
            )
        datum = self.domain().gluing_datum()
        return self(
            {
                index: datum.local_module(index).module_category()
                .Mor(datum.local_module(index), datum.local_module(index))
                .identity()
                for index in datum.chart_indices()
            }
        )


class FiniteAtlasModuleGluingMor(CategoricalMor):
    r"""Compatible local maps between two module descent data on one finite atlas."""

    Element = FiniteAtlasModuleGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.gluing_datum() is not codomain.gluing_datum():
            raise ValueError(
                f"cannot form the morphisms of glued modules from {domain} to {codomain}: they must be "
                f"glued over one affine atlas, but they are glued over {domain.gluing_datum()} and "
                f"{codomain.gluing_datum()}"
            )
        super().__init__(family, domain, codomain)

    def _element_constructor_(self, local_maps):
        match local_maps:
            case FiniteAtlasModuleGluingMorphism() if local_maps.parent() is self:
                return local_maps
            case FiniteAtlasModuleGluingMorphism():
                if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                    raise ValueError(
                        f"cannot make {local_maps} a morphism {self.domain()} -> {self.codomain()}: it is a "
                        f"morphism {local_maps.domain()} -> {local_maps.codomain()}"
                    )
                local_maps = local_maps.local_maps()
            case _:
                pass
        return self.element_class(self, local_maps)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no identity: its domain {self.domain()} is not its codomain {self.codomain()}"
            )
        datum = self.domain()
        return self(
            {
                index: datum.local_module(index).module_category()
                .Mor(datum.local_module(index), datum.local_module(index))
                .identity()
                for index in datum.chart_indices()
            }
        )


class FiniteAtlasModuleGluingMorCategoryConstruction(MorCategoryConstruction):
    r"""The Mor family of finite-atlas module descent data."""

    def fixed_category_class(self):
        return FiniteAtlasModuleGluingMor


class FiniteAtlasModuleGluingData(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""Module descent data on one owned finite affine atlas.

    The atlas is the cover parameter.  Objects retain finitely framed local
    modules and semilinear transition isomorphisms satisfying the represented
    triple-overlap cocycle; morphisms are compatible local linear maps.  Thus
    this is the finite-atlas specialization of ``DescentDataOnCover`` rather
    than a host record carrying a private gluing presentation.
    """

    _MorCategory = FiniteAtlasModuleGluingMorCategoryConstruction

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

    @cached_method
    def structure_module_datum(self):
        r"""The rank-one descent datum presenting ``O_X`` on this atlas."""
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

    def an_object(self):
        return self.structure_module_datum()


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
                raise ValueError(
                    f"cannot glue the local algebras over {gluing_datum}: the algebra {algebra} on chart "
                    f"{index} must be an algebra over the coordinate algebra {ring} of that chart, but its "
                    f"base ring is {algebra.base_ring()}"
                )
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
            raise ValueError(
                f"cannot build an algebra map {domain} -> {codomain} from the images {supplied}: exactly "
                f"one image must be given for each chosen algebra generator of {domain}"
            )
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
                raise ValueError(
                    f"the algebra chart changes of {self} fail the cocycle condition on the triple overlap of "
                    f"charts {left}, {middle} and {right}"
                )

    def restricted_local_map(self, target_datum, chart_index, other_index, local_map):
        if target_datum.gluing_datum() is not self.gluing_datum():
            raise ValueError(
                f"cannot restrict a local map into {target_datum}: it is glued over "
                f"{target_datum.gluing_datum()}, but {self} is glued over {self.gluing_datum()}; both must "
                "use one affine atlas"
            )
        datum = self.gluing_datum()
        chart_index = datum.normalize_chart_index(chart_index)
        other_index = datum.normalize_chart_index(other_index)
        if (
            local_map.domain() is not self.local_algebra(chart_index)
            or local_map.codomain() is not target_datum.local_algebra(chart_index)
        ):
            raise ValueError(
                f"cannot restrict {local_map} on chart {chart_index}: it must be a map "
                f"{self.local_algebra(chart_index)} -> {target_datum.local_algebra(chart_index)}, but it "
                f"is {local_map.domain()} -> {local_map.codomain()}"
            )
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
        return _algebra_mor(source_pair, target_pair)(
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
            raise ValueError(
                f"cannot build a morphism of glued algebras {source} -> {target}: they must be glued over "
                f"one affine atlas, but they are glued over {source.gluing_datum()} and "
                f"{target.gluing_datum()}"
            )
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
                raise ValueError(
                    f"cannot build a morphism of glued algebras {source} -> {target}: the local map "
                    f"{local_map} on chart {index} must be {source.local_algebra(index)} -> "
                    f"{target.local_algebra(index)}, but it is {local_map.domain()} -> {local_map.codomain()}"
                )
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
                    f"the local maps of {self} do not glue: on the overlap of charts {source_index} and "
                    f"{target_index} they do not commute with the chart changes"
                )


class FiniteAtlasAlgebraGluingMor(CategoricalMor):
    r"""Compatible local algebra maps between two descent data on one finite atlas."""

    Element = FiniteAtlasAlgebraGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.gluing_datum() is not codomain.gluing_datum():
            raise ValueError(
                f"cannot form the morphisms of glued algebras from {domain} to {codomain}: they must be "
                f"glued over one affine atlas, but they are glued over {domain.gluing_datum()} and "
                f"{codomain.gluing_datum()}"
            )
        super().__init__(family, domain, codomain)

    def _element_constructor_(self, local_maps):
        match local_maps:
            case FiniteAtlasAlgebraGluingMorphism() if local_maps.parent() is self:
                return local_maps
            case FiniteAtlasAlgebraGluingMorphism():
                if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                    raise ValueError(
                        f"cannot make {local_maps} a morphism {self.domain()} -> {self.codomain()}: it is a "
                        f"morphism {local_maps.domain()} -> {local_maps.codomain()}"
                    )
                local_maps = local_maps.local_maps()
            case _:
                pass
        return self.element_class(self, local_maps)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no identity: its domain {self.domain()} is not its codomain {self.codomain()}"
            )
        datum = self.domain()
        return self(
            {
                index: _algebra_mor(
                    datum.local_algebra(index),
                    datum.local_algebra(index),
                ).identity()
                for index in datum.chart_indices()
            }
        )


class FiniteAtlasAlgebraGluingMorCategoryConstruction(MorCategoryConstruction):
    r"""The Mor family of finite-atlas algebra descent data."""

    def fixed_category_class(self):
        return FiniteAtlasAlgebraGluingMor


class FiniteAtlasAlgebraGluingData(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""Unital associative algebra descent data on one finite affine atlas."""

    _MorCategory = FiniteAtlasAlgebraGluingMorCategoryConstruction

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
        raise ValueError(
            f"{name} must have exactly one entry on each affine chart of {cover}, but "
            f"{supplied.cardinality()} entries were given for {family.cardinality()} charts"
        )
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
            f"{noun} must have one chart change for each pair of distinct charts {expected}, but chart "
            f"changes were given for the pairs {tuple(normalized)}"
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


class ModuleGluingMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return ModuleGluingMor


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

    _MorCategory = ModuleGluingMorCategoryConstruction

    class ParentMethods:
        def __init__(self, local_modules, transitions, **rest) -> None:
            self._local_modules = local_modules
            self._transitions = transitions
            super().__init__(**rest)
            for label in self.chart_index_set():
                if self.local_module(label).base_ring() is not self.cover().open(label).coordinate_algebra():
                    raise ValueError(
                        f"cannot glue the local modules on {self.cover()}: the module {self.local_module(label)} "
                        f"on chart {label} must be a module over the coordinate algebra "
                        f"{self.cover().open(label).coordinate_algebra()} of that chart, but its base ring is "
                        f"{self.local_module(label).base_ring()}"
                    )
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
                        f"cannot glue along {transition} on the overlap of charts {left} and {right}: it must be "
                        f"an isomorphism of modules {source} -> {target} between the restrictions of the two "
                        "local modules to the overlap"
                    )
                forward = transition.forward()
                inverse = transition.inverse()
                for label in _finite_framing(source):
                    generator = source.module_generator(label)
                    if inverse(forward(generator)) != generator:
                        raise ValueError(
                            f"cannot glue along {transition} on the overlap of charts {left} and {right}: its stated "
                            f"inverse does not send the image of the module generator {generator} back to it"
                        )
                for label in _finite_framing(target):
                    generator = target.module_generator(label)
                    if forward(inverse(generator)) != generator:
                        raise ValueError(
                            f"cannot glue along {transition} on the overlap of charts {left} and {right}: it does not "
                            f"send the image of the module generator {generator} under the stated inverse back to it"
                        )

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
                raise ValueError(
                    f"cannot restrict the module on chart {chart} from the intersection of the charts "
                    f"{source_labels} to the intersection of the charts {target_labels}: the second "
                    "intersection must lie in the first, so its charts must include those of the first"
                )
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
                    raise ValueError(
                        f"the module chart changes of {self} fail the cocycle condition on the triple overlap of "
                        f"charts {left}, {middle} and {right}"
                    )

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
                    raise ValueError(
                        f"the local sections {sections} do not glue: on the overlap of charts {left} and {right} "
                        "they disagree after the chart change"
                    )
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
                    raise ValueError(
                        f"cannot form the leg of the Čech diagram at the pair {pair}: the side must be 'left' or "
                        f"'right', but it is {side!r}"
                    )
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
                    raise ValueError(
                        f"cannot compare {self} with the equalizer {equalizer}: it is taken over the covering "
                        f"family {equalizer.covering_family()}, not over the Čech cover {selected_cover} of "
                        f"{self.cover()}"
                    )
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
                raise ValueError(
                    f"cannot construct the sheaf glued from {self}: its module gluing data are determined by "
                    f"{self} and must not be given again"
                )
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
            r"""Return the represented Mor category of descent morphisms to ``target``."""
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
        assert False, (
            f"{label} is not an object of the Čech site of {self.cover()}: its objects are the covered "
            "scheme, the charts and the overlaps of pairs of charts"
        )

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
        assert False, (
            f"there is no restriction from {source_label} to {target_label} in the Čech site of "
            f"{self.cover()}: an overlap of two charts has no arrows out of it"
        )

    def restriction_between_labels(self, source_label, target_label):
        r"""Return the represented restriction between two Čech-labelled module values."""
        source_label = tuple(source_label)
        target_label = tuple(target_label)
        source = self.value_on_label(source_label)
        target = self.value_on_label(target_label)
        mor = source.module_category().Mor(source, target)
        match source_label == target_label:
            case True:
                return mor.identity()
            case False:
                return _CanonicalDescentRestrictionMorphism(
                    mor,
                    lambda element: self._restriction_value(
                        source_label,
                        target_label,
                        element,
                    ),
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
                raise ValueError(
                    f"cannot read {equalizer} as the global sections of {self}: it is taken over the covering "
                    f"family {equalizer.covering_family()}, not over the Čech cover {selected_cover} of "
                    f"{self.cover()}"
                )
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
                    raise ArithmeticError(
                        f"the equalizer {equalizer} computing the global sections of {self} does not start at "
                        f"the product {owner_diagram(owner_shape.source())} of the local sections: the leg of "
                        f"the cone {cone} lands in {source_leg.codomain()}"
                    )

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


class _FiniteAtlasModuleCechPresheaf(_ModuleGluingCechPresheaf):
    r"""The finite-atlas module datum as a presheaf on its represented Čech site."""

    def __init__(self, gluing_datum) -> None:
        self._gluing_datum = gluing_datum
        atlas = gluing_datum.gluing_datum()
        Functor.__init__(
            self,
            atlas.cech_site().opposite(),
            Modules(atlas.global_function_algebra()),
        )

    def cover(self):
        return self.gluing_datum().gluing_datum()

    @cached_method
    def _value(self, label):
        datum = self.gluing_datum()
        atlas = self.cover()
        match label:
            case ():
                return datum.compatible_sections()
            case (chart,):
                return datum.local_module(chart).restrict_scalars(
                    atlas.global_function_restriction(chart)
                )
            case (owner, other):
                return datum.pair_module(owner, other).restrict_scalars(
                    atlas.global_function_overlap_restriction(owner, other)
                )
        raise ValueError(
            f"{label} is not an object of the Čech site of {self.cover()}: its objects are the covered "
            "scheme, the charts and the overlaps of pairs of charts"
        )

    def _restriction_value(self, source_label, target_label, element):
        datum = self.gluing_datum()
        atlas = self.cover()
        target = self._value(target_label)
        owner = target_label[0]
        match source_label:
            case ():
                local = datum.compatible_section_component(element, owner)
                match target_label:
                    case (_chart,):
                        return target.wrap(local)
                    case (left, right):
                        pair = datum.pair_module(left, right)
                        ring_map = atlas.overlap(left, right).inclusion().coordinate_algebra_morphism()
                        return target.wrap(
                            _base_change_element(
                                datum.local_module(left),
                                pair,
                                ring_map,
                                local,
                            )
                        )
            case (chart,):
                assert len(target_label) == 2 and chart in target_label, (
                    f"there is no restriction from the chart {chart} to {target_label} in the Čech site of "
                    f"{atlas}: a chart restricts only to an overlap of two charts containing it"
                )
                left, right = target_label
                match chart == left:
                    case True:
                        other = right
                    case False:
                        other = left
                pair = datum.pair_module(chart, other)
                ring_map = atlas.overlap(chart, other).inclusion().coordinate_algebra_morphism()
                restricted = _base_change_element(
                    datum.local_module(chart),
                    pair,
                    ring_map,
                    element.underlying_element(),
                )
                match chart == owner:
                    case True:
                        return target.wrap(restricted)
                    case False:
                        return target.wrap(datum.transition(owner, chart).pullback()(restricted))
        raise ValueError(
            f"there is no restriction from {source_label} to {target_label} in the Čech site of "
            f"{self.cover()}: an overlap of two charts has no arrows out of it"
        )

    def _repr_(self):
        return f"Finite-atlas Čech presheaf of {self.gluing_datum()}"


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
                    f"{self} does not glue: on the overlap of charts {left} and {right} its local maps do not "
                    "commute with the chart changes"
                )

    @cached_method
    def global_sections_map(self):
        r"""Return the induced ``O(X)``-linear map on compatible global sections."""
        source_datum = self.domain()
        target_datum = self.codomain()
        source_sections = self.domain().compatible_sections()
        target_sections = self.codomain().compatible_sections()

        return _DescentGlobalSectionsMorphism(
            source_sections.module_category().Mor(source_sections, target_sections),
            self,
            source_datum,
            target_datum,
        )

    def then(self, other):
        r"""Return ``other after self``."""
        if other.domain() is not self.codomain():
            raise ValueError(
                f"cannot compose {self} and then {other}: the codomain {self.codomain()} of the first is "
                f"not the domain {other.domain()} of the second"
            )
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


class ModuleGluingMor(CategoricalMor):
    r"""The fixed Mor category between two module descent data on one cover."""

    Element = ModuleGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.cover() is not codomain.cover():
            raise ValueError(
                f"cannot form the morphisms of glued modules from {domain} to {codomain}: they must be "
                f"glued over one affine cover, but they are glued over {domain.cover()} and "
                f"{codomain.cover()}"
            )
        super().__init__(family, domain, codomain)

    def _element_constructor_(self, local_maps):
        if isinstance(local_maps, ModuleGluingMorphism):
            if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                raise ValueError(
                    f"cannot make {local_maps} a morphism {self.domain()} -> {self.codomain()}: it is a "
                    f"morphism {local_maps.domain()} -> {local_maps.codomain()}"
                )
            if local_maps.parent() is self:
                return local_maps
            local_maps = local_maps.local_maps()
        return self.element_class(self, local_maps)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no identity: its domain {self.domain()} is not its codomain {self.codomain()}"
            )
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
        raise TypeError(
            f"cannot compare the algebra maps {left} and {right} on generators: {source} must have "
            f"finitely many chosen algebra generators, but it has {labels.cardinality()}"
        )
    return all(
        left(source.algebra_generator(label)) == right(source.algebra_generator(label))
        for label in labels
    )


def _finite_algebra_framing(algebra):
    if algebra not in FramedAlgebras(algebra.base_ring()):
        raise TypeError(
            f"cannot glue the algebra {algebra} as local data on an affine chart: descent is computed "
            "here only for algebras with a chosen finite set of algebra generators, but "
            f"{algebra} is an object of {algebra.category()}"
        )
    labels = algebra.algebra_generating_set()
    if not labels.cardinality().is_finite():
        raise TypeError(
            f"cannot glue the algebra {algebra} as local data on an affine chart: descent is computed "
            "here only for algebras with a chosen finite set of algebra generators, but "
            f"{algebra} has {labels.cardinality()}"
        )
    return labels


class AlgebraGluingMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return AlgebraGluingMor


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

    _MorCategory = AlgebraGluingMorCategoryConstruction

    class ParentMethods:
        def __init__(self, local_algebras, transitions, **rest) -> None:
            self._local_algebras = local_algebras
            self._transitions = transitions
            super().__init__(**rest)
            for label in self.chart_index_set():
                if self.local_algebra(label).base_ring() is not self.cover().open(label).coordinate_algebra():
                    raise ValueError(
                        f"cannot glue the local algebras on {self.cover()}: the algebra "
                        f"{self.local_algebra(label)} on chart {label} must be an algebra over the coordinate "
                        f"algebra {self.cover().open(label).coordinate_algebra()} of that chart, but its base "
                        f"ring is {self.local_algebra(label).base_ring()}"
                    )
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
                raise TypeError(
                    f"the base change {restricted} of the algebra {self.local_algebra(chart_index)} on chart "
                    f"{chart_index} to the intersection with the charts {intersection_indices} is not an "
                    f"associative unital algebra over {target}; it is an object of {restricted.category()}"
                )
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
                        f"cannot glue along {transition} on the overlap of charts {left} and {right}: it must be "
                        f"an isomorphism of algebras {source} -> {target} between the restrictions of the two "
                        "local algebras to the overlap"
                    )
                if not _algebra_maps_agree_on_generators(
                    transition.inverse() * transition.forward(),
                    _algebra_mor(source, source).identity(),
                ):
                    raise ValueError(
                        f"cannot glue along {transition} on the overlap of charts {left} and {right}: it followed "
                        f"by its stated inverse is not the identity of {source}"
                    )
                if not _algebra_maps_agree_on_generators(
                    transition.forward() * transition.inverse(),
                    _algebra_mor(target, target).identity(),
                ):
                    raise ValueError(
                        f"cannot glue along {transition} on the overlap of charts {left} and {right}: its stated "
                        f"inverse followed by it is not the identity of {target}"
                    )

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
                raise ValueError(
                    f"cannot restrict the algebra on chart {chart} from the intersection of the charts "
                    f"{source_labels} to the intersection of the charts {target_labels}: the second "
                    "intersection must lie in the first, so its charts must include those of the first"
                )
            source = self.restricted_algebra(chart, *source_labels)
            target = self.restricted_algebra(chart, *target_labels)
            if target is source:
                return _algebra_mor(source, source).identity()
            source_open = self.cover().intersection(*source_labels)
            target_open = self.cover().intersection(*target_labels)
            ring_map = self.scheme().structure_sheaf().restriction_map(source_open, target_open)
            restricted_target = target.restrict_scalars(ring_map)
            return _algebra_mor(source, restricted_target)(
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
            return _algebra_mor(source, target)(
                lambda label: target(target_restriction(transition(pair_source.algebra_generator(label))))
            )

        def restricted_local_map(self, target_datum, chart_index, other_index, local_map):
            r"""Base-change one local algebra map to a represented pair overlap."""
            if target_datum.cover() is not self.cover():
                raise ValueError(
                    f"cannot restrict a local map into {target_datum}: it is glued over the cover "
                    f"{target_datum.cover()}, but {self} is glued over {self.cover()}; both must use one "
                    "affine cover"
                )
            chart = self.cover().chart_label(chart_index)
            other = self.cover().chart_label(other_index)
            if (
                local_map.domain() is not self.local_algebra(chart)
                or local_map.codomain() is not target_datum.local_algebra(chart)
            ):
                raise ValueError(
                    f"cannot restrict {local_map} on chart {chart}: it must be a map "
                    f"{self.local_algebra(chart)} -> {target_datum.local_algebra(chart)}, but it is "
                    f"{local_map.domain()} -> {local_map.codomain()}"
                )
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
            return _algebra_mor(source, target)(
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
                    raise ValueError(
                        f"the algebra chart changes of {self} fail the cocycle condition on the triple overlap of "
                        f"charts {left}, {middle} and {right}"
                    )

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
                    raise ValueError(
                        f"cannot compare {self} with the equalizer {equalizer}: it is taken over the covering "
                        f"family {equalizer.covering_family()}, not over the Čech cover {selected_cover} of "
                        f"{self.cover()}"
                    )
                global_sections = self.compatible_sections()
                return _algebra_mor(global_sections, global_sections).identity()

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
        assert False, (
            f"{label} is not an object of the Čech site of {self.cover()}: its objects are the covered "
            "scheme, the charts and the overlaps of pairs of charts"
        )

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
        assert False, (
            f"there is no restriction from {source_label} to {target_label} in the Čech site of "
            f"{self.cover()}: an overlap of two charts has no arrows out of it"
        )

    def _apply_morphism(self, opposite_arrow):
        underlying = opposite_arrow.underlying_arrow()
        source_label = tuple(underlying.codomain().value())
        target_label = tuple(underlying.domain().value())
        source = self(opposite_arrow.domain())
        target = self(opposite_arrow.codomain())
        mor = _algebra_mor(source, target)
        if source_label == target_label:
            return mor.identity()
        return mor(
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
            lambda label: _algebra_mor(
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
                    f"{self} does not glue: on the overlap of charts {left} and {right} its local maps do not "
                    "commute with the chart changes"
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

        return _algebra_mor(source, target)(SetMorphism(Sets().Mor(source, target), image))

    def relative_spectrum_morphism(self):
        r"""Return the contravariant morphism of relative spectra induced by this algebra map."""
        from dzack_research.preamble.categories.schemes.relative_spec import (
            _relative_spectrum_morphism,
        )

        return _relative_spectrum_morphism(self)

    def then(self, other):
        if other.domain() is not self.codomain():
            raise ValueError(
                f"cannot compose {self} and then {other}: the codomain {self.codomain()} of the first is "
                f"not the domain {other.domain()} of the second"
            )
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


class AlgebraGluingMor(CategoricalMor):
    Element = AlgebraGluingMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.cover() is not codomain.cover():
            raise ValueError(
                f"cannot form the morphisms of glued algebras from {domain} to {codomain}: they must be "
                f"glued over one affine cover, but they are glued over {domain.cover()} and "
                f"{codomain.cover()}"
            )
        super().__init__(family, domain, codomain)

    def _element_constructor_(self, local_maps):
        if isinstance(local_maps, AlgebraGluingMorphism):
            if local_maps.domain() is not self.domain() or local_maps.codomain() is not self.codomain():
                raise ValueError(
                    f"cannot make {local_maps} a morphism {self.domain()} -> {self.codomain()}: it is a "
                    f"morphism {local_maps.domain()} -> {local_maps.codomain()}"
                )
            if local_maps.parent() is self:
                return local_maps
            local_maps = local_maps.local_maps()
        return self.element_class(self, local_maps)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no identity: its domain {self.domain()} is not its codomain {self.codomain()}"
            )
        return self(
            self.domain().local_algebras().map(
                lambda algebra: _algebra_mor(algebra, algebra).identity()
            )
        )


class _FiniteAtlasModuleSheafEngine:
    r"""Private realization of a quasi-coherent sheaf by finite-atlas descent.

    The sheaf itself is constructed by ``Sheaves.object`` for the atlas Čech
    coverage and is placed in ``QuasiCoherentSheaves(X)``.  This engine retains
    the selected local-module presentation needed by chartwise computations; it
    does not define another category of sheaves.
    """

    def __init__(self, module_gluing_datum, **rest) -> None:
        self._module_gluing_datum = module_gluing_datum
        super().__init__(**rest)

    def gluing_datum(self):
        r"""The finite-atlas module descent datum presenting this sheaf."""
        return self._module_gluing_datum

    def atlas_datum(self):
        return self.gluing_datum().gluing_datum()

    def ringed_space(self):
        return self.gluing_datum().scheme()

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
        match point.parent() is chart.underlying_space():
            case True:
                pass
            case False:
                raise ValueError(
                    f"cannot form the stalk of {self} at {point}: the point must be a point of the chart "
                    f"{chart_index}, {chart}, but it lies in {point.parent()}"
                )
        return self.sections_on_chart(chart_index).localize_at_prime(point.ideal())

    def tensor_product(self, other):
        r"""Return ``self tensor O_X other`` by chartwise tensor descent."""
        match other in self.category():
            case True:
                pass
            case False:
                raise TypeError(
                    f"cannot form the tensor product of {self} and {other}: both must be sheaves on the same "
                    f"finite affine atlas, and {other} is not an object of {self.category()}"
                )
        return self.gluing_datum().tensor_product(other.gluing_datum()).sheaf()

    def morphism_to(self, other, local_maps):
        r"""Return the sheaf morphism represented by compatible chart maps."""
        match other in self.category():
            case True:
                pass
            case False:
                raise TypeError(
                    f"cannot build a morphism {self} -> {other} from local maps: both must be sheaves on the "
                    f"same finite affine atlas, and {other} is not an object of {self.category()}"
                )
        return QuasiCoherentSheaves(self.scheme()).Mor(self, other)(local_maps)

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
            raise ValueError(
                f"cannot pull {source_sheaf} back along the refinement {refinement}: it is a sheaf on "
                f"{source_sheaf.atlas_datum()}, not on the coarse atlas {refinement.coarse_datum()}"
            )
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
            raise ValueError(
                f"cannot pull {source_morphism} back to a morphism {self.domain()} -> {self.codomain()}: "
                f"it must start at {self.domain().source_sheaf()}, but it starts at "
                f"{source_morphism.domain()}"
            )
        if source_morphism.codomain() is not self.codomain().source_sheaf():
            raise ValueError(
                f"cannot pull {source_morphism} back to a morphism {self.domain()} -> {self.codomain()}: "
                f"it must end at {self.codomain().source_sheaf()}, but it ends at "
                f"{source_morphism.codomain()}"
            )
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


class _FiniteAtlasInverseImageModuleMor(CategoricalMor):
    r"""Mor in ``Mod(f^{-1}O_Y)`` for one represented finite-atlas refinement."""

    Element = _FiniteAtlasInverseImageModuleMorphism

    def _element_constructor_(self, source_morphism):
        match source_morphism:
            case _FiniteAtlasInverseImageModuleMorphism() if source_morphism.parent() is self:
                return source_morphism
            case _FiniteAtlasInverseImageModuleMorphism():
                source_morphism = source_morphism.source_morphism()
            case _:
                pass
        source_mor = self.base_category().source_category().Mor(
            self.domain().source_sheaf(),
            self.codomain().source_sheaf(),
        )
        if source_morphism not in source_mor:
            raise TypeError(
                f"cannot pull {source_morphism} back to a morphism {self.domain()} -> {self.codomain()}: "
                f"it must be a morphism {self.domain().source_sheaf()} -> "
                f"{self.codomain().source_sheaf()}"
            )
        return self.element_class(self, source_morphism)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"{self} has no identity: its domain {self.domain()} is not its codomain {self.codomain()}"
            )
        source = self.domain().source_sheaf()
        return self(self.base_category().source_category().Mor(source, source).identity())


class _FiniteAtlasInverseImageModuleMorCategoryConstruction(MorCategoryConstruction):
    r"""Mor family for finite-atlas presentations of ``f^{-1}O_Y``-modules."""

    def fixed_category_class(self):
        return _FiniteAtlasInverseImageModuleMor


class _FiniteAtlasInverseImageModuleSheaves(OwnedCategory):
    r"""Represented ``f^{-1}O_Y``-modules for one finite-atlas refinement ``f:X->Y``."""

    _MorCategory = _FiniteAtlasInverseImageModuleMorCategoryConstruction

    def __init__(self, refinement) -> None:
        self._refinement = refinement
        super().__init__()

    def _make_named_class_key(self, name):
        return id(self._refinement)

    def refinement(self):
        return self._refinement

    def source_category(self):
        return _finite_atlas_quasi_coherent_sheaves(
            self.refinement().coarse_datum()
        )

    def super_categories(self):
        return [SheafObjects(self.refinement().fine_scheme())]

    def an_object(self):
        return self(self.source_category().an_object())

    @cached_method(key=lambda self, sheaf: id(sheaf))
    def object(self, sheaf):
        if sheaf not in self.source_category():
            raise TypeError(
                f"cannot pull back {sheaf}: it must be an object of {self.source_category()}, but it is "
                f"an object of {sheaf.category()}"
            )
        if sheaf.atlas_datum() is not self.refinement().coarse_datum():
            raise ValueError(
                f"cannot pull {sheaf} back along the refinement {self.refinement()}: it is a sheaf on "
                f"{sheaf.atlas_datum()}, not on the coarse atlas {self.refinement().coarse_datum()}"
            )
        return _object_of(
            self,
            source_sheaf=sheaf,
            _engine=_FiniteAtlasInverseImageModuleSheafEngine,
        )

    def __call__(self, *args, **kwargs):
        return self.object(*args, **kwargs)

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError(
                f"cannot form the morphisms from {domain} to {codomain} in {self}: both must be objects "
                f"of {self}"
            )
        return self.MorCategory().Of(domain, codomain)

    def _repr_(self):
        return f"Modules over the inverse-image structure sheaf along {self.refinement().comparison_morphism()}"


class _FiniteAtlasInverseImageModuleFunctor(Functor):
    r"""``f^{-1}`` on represented finite-atlas module sheaves."""

    def __init__(self, refinement) -> None:
        self._refinement = refinement
        super().__init__(
            _finite_atlas_quasi_coherent_sheaves(refinement.coarse_datum()),
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
            _finite_atlas_quasi_coherent_sheaves(refinement.fine_datum()),
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
            raise ValueError(
                f"cannot glue the module of the line bundle {line_bundle} over {gluing_datum}: it must be "
                f"glued over the atlas {line_bundle.gluing_datum()} of the line bundle"
            )
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
                    f"the pullbacks of the line bundle along {refinement} have different ranks on the fine "
                    f"chart {index}: the generic pullback has {len(generic_labels)} module generators and the "
                    f"specialized pullback has {len(specialized_labels)}"
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
                f"the comparison {self._forward} of the generic and specialized pullbacks of the line "
                f"bundle along {refinement} is not invertible: it followed by the stated inverse is not "
                f"the identity of {generic}"
            )
        if self._forward * self._inverse != specialized.identity_morphism():
            raise ArithmeticError(
                f"the comparison {self._forward} of the generic and specialized pullbacks of the line "
                f"bundle along {refinement} is not invertible: the stated inverse followed by it is not "
                f"the identity of {specialized}"
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
            raise ValueError(
                f"cannot glue a closed subscheme from the charts of {datum}: the closed subscheme "
                f"{local_closed[index]} given on chart {index} must lie in {datum.chart(index)}, but it "
                f"lies in {local_closed[index].inclusion().codomain()}"
            )
    return _glued_chartwise_subscheme(
        datum,
        local_closed,
        (ClosedEmbeddings(datum.scheme()), ClosedSubschemes(datum.base_ring())),
        _engine=_engine,
        construction_data=construction_data,
    )


def _glued_chartwise_distinguished_open(
    datum,
    fine_indices,
    coarse_indices,
    local_opens,
    *,
    name="Chartwise distinguished open",
):
    r"""Glue distinguished opens of the charts of one finite affine atlas.

    Several fine charts may lie over one coarse chart.  For a fine chart
    ``V_a = D(f_a) <= U_i`` and ``V_b = D(f_b) <= U_j``, their overlap inside
    ``V_a`` is the locus where the coarse overlap ``U_ij`` and the pullback of
    ``f_b`` through the coarse transition are both invertible.  Since the
    coarse overlaps are distinguished, clearing the localization denominator
    gives one distinguished open of ``V_a``.  The coarse transition then
    restricts to an isomorphism between the two fine presentations.

    The glued scheme is placed in ``OpenImmersions(X)`` and its inclusion is
    the morphism obtained by gluing ``V_a -> U_i -> X``.  Thus callers retain
    an actual open subobject rather than only a chartwise predicate.
    """
    fine_indices = finite_ordered_set(tuple(fine_indices))
    coarse_index = _family_on_finite_ordered_set(
        fine_indices,
        coarse_indices,
        name="Fine-to-coarse labels of a chartwise open",
        noun="chartwise-open coarse-index data",
    )
    opens = _family_on_finite_ordered_set(
        fine_indices,
        local_opens,
        name=f"Affine pieces of {name}",
        noun="a chartwise distinguished open",
    )
    for fine_index in fine_indices:
        coarse = datum.normalize_chart_index(coarse_index[fine_index])
        selected = opens[fine_index]
        match (
            selected.inclusion().codomain() is datum.chart(coarse),
            selected.is_distinguished_open() is True,
        ):
            case (True, True):
                pass
            case (False, _):
                raise ValueError(
                    f"cannot glue an open subscheme from the charts of {datum}: the open subscheme "
                    f"{selected} given on the fine chart {fine_index} must lie in the chart "
                    f"{datum.chart(coarse)}, but it lies in {selected.inclusion().codomain()}"
                )
            case (_, False):
                raise TypeError(
                    f"cannot glue an open subscheme from the charts of {datum}: gluing is computed here only "
                    f"for distinguished open subschemes D(f), and {selected} on the fine chart {fine_index} "
                    "is not known to be one"
                )

    def normalized_coarse(fine_index):
        return datum.normalize_chart_index(coarse_index[fine_index])

    def fine_overlap(source_index, target_index):
        source_open = opens[source_index]
        target_open = opens[target_index]
        source_coarse = normalized_coarse(source_index)
        target_coarse = normalized_coarse(target_index)
        source_restriction = source_open.inclusion().coordinate_algebra_morphism()
        match source_coarse == target_coarse:
            case True:
                target_element = target_open.distinguished_open_element()
                return source_open.distinguished_open(
                    source_restriction(target_element)
                )
            case False:
                coarse_overlap = datum.overlap(source_coarse, target_coarse)
                target_overlap = datum.overlap(target_coarse, source_coarse)
                coarse_element = coarse_overlap.distinguished_open_element()
                target_element = target_open.distinguished_open_element()
                target_on_overlap = target_overlap.inclusion().coordinate_algebra_morphism()(
                    target_element
                )
                pulled_target = datum.transition_between(
                    source_coarse, target_coarse
                ).forward().coordinate_algebra_morphism()(target_on_overlap)
                numerator, _denominator = coarse_overlap.coordinate_algebra().localization_fraction_data(
                    pulled_target
                )
                return source_open.distinguished_open(
                    source_restriction(coarse_element * numerator)
                )

    def fine_transition(source_index, target_index):
        source = fine_overlap(source_index, target_index)
        target = fine_overlap(target_index, source_index)
        source_open = opens[source_index]
        target_open = opens[target_index]
        source_coarse = normalized_coarse(source_index)
        target_coarse = normalized_coarse(target_index)
        into_source_chart = source_open.inclusion() * source.inclusion()
        match source_coarse == target_coarse:
            case True:
                into_target_open = target_open.corestriction(into_source_chart)
            case False:
                coarse_overlap = datum.overlap(source_coarse, target_coarse)
                into_coarse_overlap = coarse_overlap.corestriction(into_source_chart)
                across = datum.transition_between(
                    source_coarse, target_coarse
                ).forward() * into_coarse_overlap
                into_target_chart = (
                    datum.overlap(target_coarse, source_coarse).inclusion() * across
                )
                into_target_open = target_open.corestriction(into_target_chart)
        return target.corestriction(into_target_open)

    schemes = Schemes(datum.base_ring())
    transitions = {}
    fine_labels = tuple(fine_indices)
    for position, source_index in enumerate(fine_labels):
        for target_index in fine_labels[position + 1 :]:
            forward = fine_transition(source_index, target_index)
            inverse = fine_transition(target_index, source_index)
            transitions[source_index, target_index] = schemes.Core().Mor(
                forward.domain(), forward.codomain()
            )(forward, inverse)
    return schemes.glue_affine_atlas(
        opens,
        transitions,
        placements=(OpenImmersions(datum.scheme()),),
        inclusion_codomain=datum.scheme(),
        inclusion_datum=finite_indexed_family(
            fine_indices,
            lambda index: datum.chart_embedding(normalized_coarse(index))
            * opens[index].inclusion(),
            name="Local inclusions of a glued chartwise open",
        ),
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
            raise ValueError(
                f"cannot form the fixed locus chart by chart on {datum}: the automorphism "
                f"{automorphism} given on chart {index} must be an endomorphism of {chart}, but it is "
                f"{automorphism.domain()} -> {automorphism.codomain()}"
            )
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
    "AlgebraGluingMor",
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
    "FiniteAtlasModuleTransition",
    "ModuleGluingData",
    "ModuleGluingMor",
    "ModuleGluingMorphism",
    "SemilinearAlgebraMorphism",
    "SemilinearModuleMorphism",
]
