"""Owned ringed-space structure used by the scheme hierarchy."""

from itertools import combinations

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.categories.category_with_axiom import all_axioms
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.structure.element import parent as element_parent
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.abstract_categories.presheaves import (
    Coverage,
    CoveringFamilies,
    CoveringFamilyHomCategoryConstruction,
    CoveringFamilyHomset,
    CoveringFamilyMorphism,
    DescentData,
    _CechCoveringFamilies,
)
from dzack_research.preamble.categories.abstract_categories.products import PosetCategory
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom


if "Invertible" not in all_axioms:
    all_axioms.add("Invertible")


class _SchemeUnderlyingSpaceTopologyData(SageObject):
    r"""The topology of ``|X|`` retained by the represented ringed space ``X``.

    The public topology is the collection of open subsets of ``|X|``.  The
    ringed-space layer already owns open immersions and Zariski coverings, but
    it does not yet own a pointwise decision procedure turning an arbitrary
    subset of a non-affine scheme into an open immersion.  The topology is
    therefore represented as the exact subobject of the power set cut out by
    openness, with arbitrary membership assertion-gated until such a
    presentation is supplied.  The empty and whole opens are unconditional.
    """

    def __init__(self, ringed_space) -> None:
        self._ringed_space = ringed_space

    def ringed_space(self):
        return self._ringed_space

    def open_subsets(self, space):
        return space.power_set().condition_set(
            lambda subset: self.is_open_subset(space, subset)
        )

    def is_open_subset(self, space, subset) -> bool:
        power = space.power_set()
        selected = power(subset)
        match selected:
            case _ if selected == power.bottom():
                return True
            case _ if selected == power.top():
                return True
            case _:
                assert False, (
                    "openness of an arbitrary subset of a non-affine underlying "
                    "scheme space requires a represented open-immersion presentation"
                )


class _SchemeUnderlyingSpaceEngine:
    r"""Private realization of ``|X|`` as an object of ``TopologicalSpaces``."""

    def __init__(self, ringed_space, **rest) -> None:
        self._ringed_space = ringed_space
        super().__init__(**rest)

    def ringed_space(self):
        return self._ringed_space

    scheme = ringed_space

    def __contains__(self, point) -> bool:
        return element_parent(point) is self

    is_parent_of = __contains__

    def _element_constructor_(self, point):
        match element_parent(point) is self:
            case True:
                return point
            case False:
                assert False, (
                    "a point of a non-affine underlying scheme space requires a "
                    "represented affine-chart point and its gluing identification"
                )

    def _repr_(self) -> str:
        return f"Underlying topological space of {self.ringed_space()}"


@cached_function(key=lambda ringed_space: id(ringed_space))
def _scheme_underlying_space(ringed_space):
    return _object_of(
        TopologicalSpaces(),
        _engine=(TopologicalSpaces(), _SchemeUnderlyingSpaceEngine, None),
        topology_data=_SchemeUnderlyingSpaceTopologyData(ringed_space),
        ringed_space=ringed_space,
    )


class SheafObjects(OwnedParameterizedCategory):
    r"""Represented sheaves on one base space.

    This is the semantic placement shared by represented sheaves on one
    ringed space.  A sheaf that materializes a
    specific site/coverage additionally lies in the corresponding
    :class:`~dzack_research.preamble.categories.abstract_categories.presheaves.Sheaves`
    full subcategory; this base-space category does not replace that descent
    datum or pretend that every represented space currently exposes one common
    site presentation.
    """

    def parameter_category(self):
        return RingedSpaces()

    def space(self):
        return self.base()

    def _repr_object_names(self):
        return f"sheaves on {self.space()}"

    def super_categories(self):
        return [Objects()]

    def an_object(self):
        return self.space().structure_sheaf()


class SheafedSpaces(OwnedCategory):
    r"""Represented spaces equipped with a chosen sheaf.

    A sheafed-space object retains its underlying space as construction data;
    it is not identified with that underlying point-set parent.  Consequently
    this category remains an object-level owner, while ``underlying_space()``
    returns the actual object of ``TopologicalSpaces``.
    """

    @classmethod
    def _repr_object_names(cls):
        return "sheafed spaces"

    def super_categories(self):
        return [Objects()]

    def an_object(self):
        return RingedSpaces().an_object()




class ModuleSheaves(OwnedParameterizedCategory):
    r"""Sheaves of ``O_X``-modules on one represented ringed space ``X``."""

    def scheme(self):
        return self.base()

    ringed_space = scheme

    def _repr_object_names(self):
        return f"module sheaves on {self.scheme()}"

    def super_categories(self):
        return [SheafObjects(self.scheme())]

    def an_object(self):
        return self.scheme().structure_sheaf()

    def tensor_product(self, factors):
        r"""Return the tensor product of represented module sheaves.

        The currently selected affine implementation is transported through
        the existing equivalence ``QCoh(Spec A) ~= Modules(A)``.  Moving this
        operation here records its mathematical owner: quasi-coherence adds a
        condition on a module sheaf; it does not define a second tensor
        product.
        """

        quasi_coherent = QuasiCoherentSheaves(self.scheme())
        modules = tuple(quasi_coherent.global_sections(factor) for factor in factors)
        return quasi_coherent.associated_sheaf(
            quasi_coherent.module_category().tensor_product(modules)
        )

    def kernel(self, sheaf_morphism):
        r"""Return the represented kernel in sheaves of ``O_X``-modules."""

        quasi_coherent = QuasiCoherentSheaves(self.scheme())
        return quasi_coherent.associated_sheaf(sheaf_morphism.kernel())

    def cokernel(self, sheaf_morphism):
        r"""Return the represented cokernel in sheaves of ``O_X``-modules."""

        quasi_coherent = QuasiCoherentSheaves(self.scheme())
        return quasi_coherent.associated_sheaf(sheaf_morphism.cokernel())


class AlgebraSheaves(OwnedParameterizedCategory):
    r"""Sheaves of ``O_X``-algebras on one represented ringed space ``X``."""

    def scheme(self):
        return self.base()

    ringed_space = scheme

    def _repr_object_names(self):
        return f"algebra sheaves on {self.scheme()}"

    def super_categories(self):
        return [ModuleSheaves(self.scheme())]

    def an_object(self):
        return self.scheme().structure_sheaf()


class _StructureSheafEngine:
    r"""The represented structure sheaf ``O_X`` of a ringed space ``X``."""

    def __init__(self, ringed_space, **rest) -> None:
        self._ringed_space = ringed_space
        self._restriction_maps = {}
        super().__init__(**rest)

    def presheaf(self):
        r"""The actual module-valued presheaf underlying ``O_X`` on the represented affine site."""
        return self.functor()

    @cached_method(key=lambda self, cover: id(cover))
    def module_descent_datum(self, cover):
        r"""The rank-one module descent presentation of ``O_X`` on ``cover``."""
        if cover.ambient_scheme() is not self.ringed_space():
            raise ValueError("structure-sheaf descent requires a cover of this ringed space")
        from dzack_research.preamble.categories.schemes.gluing import ModuleGluingData

        return ModuleGluingData(cover).an_object()

    def cech_sheaf(self, cover):
        r"""The canonical module-valued sheaf object on the finite Čech site of ``cover``."""
        return self.module_descent_datum(cover).sheaf()

    def ringed_space(self):
        return self._ringed_space

    scheme = ringed_space

    def global_sections(self):
        r"""Return ``Gamma(X,O_X)=O(X)`` for the represented affine scheme."""
        return self.ringed_space().coordinate_algebra()

    sections = global_sections

    def sections_on_distinguished_open(self, distinguished_open):
        r"""Return ``O_X(D(f)) = O(D(f))`` for a represented distinguished open."""
        assert _is_distinguished_open_of(distinguished_open, self.ringed_space()), (
            "structure-sheaf sections are requested on a distinguished open of this affine scheme"
        )
        return distinguished_open.coordinate_algebra()

    def restriction_map(self, source_open, target_open):
        r"""Return the represented restriction ``O(source_open) -> O(target_open)``.

        The active basis consists of the affine scheme itself and its represented
        distinguished opens.  If both opens are proper, the target is accepted
        exactly when every selected denominator inverted on the source becomes a
        unit on the target.  This is the localization universal property, rather
        than a separate containment heuristic on points.
        """

        ambient = self.ringed_space()
        key = (id(source_open), id(target_open))
        cached = self._restriction_maps.get(key)
        if cached is not None:
            cached_source, cached_target, restriction = cached
            if cached_source is source_open and cached_target is target_open:
                return restriction

        def remember(restriction):
            self._restriction_maps[key] = (source_open, target_open, restriction)
            return restriction

        if source_open is ambient:
            source_sections = self.global_sections()
        elif _is_distinguished_open_of(source_open, ambient):
            source_sections = self.sections_on_distinguished_open(source_open)
        else:
            raise ValueError("the restriction source is not a represented distinguished open of this affine scheme")

        if target_open is ambient:
            if source_open is not ambient:
                raise ValueError("a restriction map is contravariant in open-set inclusion")


            return remember(source_sections.Mor(source_sections).identity())
        if not _is_distinguished_open_of(target_open, ambient):
            raise ValueError("the restriction target is not a represented distinguished open of this affine scheme")
        target_sections = self.sections_on_distinguished_open(target_open)

        if source_open is ambient:
            restriction = target_open.inclusion().coordinate_algebra_morphism()
            if restriction.domain() is not source_sections or restriction.codomain() is not target_sections:
                raise ArithmeticError("the distinguished-open inclusion has the wrong represented pullback")
            return remember(restriction)
        if source_open is target_open:


            return remember(source_sections.Mor(source_sections).identity())
        return remember(_localization_restriction_map(source_sections, target_sections))

    def associated_module_sheaf(self, module):
        r"""Return the represented affine sheaf ``M~`` on the distinguished-open basis."""

        return QuasiCoherentSheaves(self.ringed_space()).associated_sheaf(module)

    def stalk(self, point):
        r"""Return ``O_{X,p}`` for a represented affine prime point."""
        assert point.parent() is self.ringed_space().underlying_space(), (
            "a structure-sheaf stalk is taken at a point of this affine scheme"
        )
        return point.local_ring()

    def _repr_(self) -> str:
        return f"Structure sheaf O_{{{self.scheme()}}}"


def _structure_sheaf(ringed_space):
    r"""Construct ``O_X`` by the shared sheaf entry from its affine-site presheaf and descent rule."""
    from dzack_research.preamble.categories.modules.pure.modules import Modules

    coverage = distinguished_affine_coverage(ringed_space)
    value_category = Modules(ringed_space.coordinate_algebra())
    presheaf = _AffineStructurePresheaf(ringed_space)

    def inverse_for(equalizer):
        return equalizer.canonical_map().inverse()

    descent = DescentData(coverage, presheaf, inverse_for)
    return coverage.sheaves(value_category).object(
        presheaf,
        descent,
        categories=(
            AlgebraSheaves(ringed_space),
            QuasiCoherentSheaves(ringed_space),
            QuasiCoherentSheaves(ringed_space).Invertible(),
        ),
        construction_data={"ringed_space": ringed_space},
        _engine=_StructureSheafEngine,
    )


class _AffineStructurePresheaf(Functor):
    r"""``U -> Gamma(U,O_U)`` on the represented affine slice over an affine ``X``.

    Values are read as ``O(X)``-modules by restriction of scalars along the
    coordinate pullback ``O(X) -> O(U)``.  An arrow ``V -> U`` over ``X``
    acts by its affine coordinate pullback ``O(U) -> O(V)``, regarded as an
    ``O(X)``-linear map between those restricted modules.
    """

    def __init__(self, scheme) -> None:
        from dzack_research.preamble.categories.modules.pure.modules import Modules
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        base = scheme.scheme_base_ring()
        assert scheme in Schemes(base).Affine(), (
            "the represented structure presheaf currently uses the affine slice over X"
        )
        self._scheme = scheme
        self._scalar_ring = scheme.coordinate_algebra()
        site = distinguished_affine_coverage(scheme).site_category()
        Functor.__init__(self, site.opposite(), Modules(self._scalar_ring))

    def scheme(self):
        return self._scheme

    def scalar_ring(self):
        return self._scalar_ring

    def site_category(self):
        return self.domain().base_category()

    def _slice_object(self, opposite_object):
        return opposite_object.underlying_object()

    def _apply_object(self, opposite_object):
        slice_object = self._slice_object(opposite_object)
        affine = slice_object.arrow().domain()
        algebra = affine.coordinate_algebra()
        scalar_map = slice_object.arrow().coordinate_algebra_morphism()
        if affine is self.scheme():
            return self.scalar_ring().regular_module()
        return algebra.regular_module().restrict_scalars(scalar_map)

    def _apply_morphism(self, opposite_arrow):
        from dzack_research.preamble.categories.modules.pure.modules import RestrictedScalarsModules

        source = self(opposite_arrow.domain())
        target = self(opposite_arrow.codomain())
        triangle = opposite_arrow.underlying_arrow()
        pullback = triangle.left().coordinate_algebra_morphism()
        restricted = RestrictedScalarsModules(self.scalar_ring())

        def image(element):
            source_element = source(element)
            match source:
                case _ if source in restricted:
                    underlying = source_element.underlying_element()
                case _:
                    underlying = source_element
            pulled_back = pullback(underlying)
            match target:
                case _ if target in restricted:
                    return target.wrap(pulled_back)
                case _:
                    return target(pulled_back)

        return source.module_category().Mor(source, target)(
            image, verify_linearity=False
        )

    def _repr_(self):
        return f"Affine structure presheaf of {self.scheme()}"


def _is_distinguished_open_of(open_subscheme, ambient) -> bool:
    from dzack_research.preamble.categories.schemes.schemes import OpenImmersions

    return (
        open_subscheme in OpenImmersions(ambient)
        and open_subscheme.is_distinguished_open() is True
    )


def _localization_restriction_map(source, target):
    r"""Return ``S^{-1}A -> T^{-1}A`` when the target inverts every element of ``S``."""

    from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
)

    if source is target:
        return source.Mor(source).identity()
    if source not in LocalizationRings() or target not in LocalizationRings():
        raise TypeError("principal-open restriction between proper opens requires represented localizations")
    if source.localization_source() is not target.localization_source():
        raise ValueError("principal-open restriction requires localizations of one affine coordinate ring")

    target_unit = target.localization_map()
    generators = tuple(source.localization_submonoid().monoid_generators())
    if any(not target_unit(generator).is_unit() for generator in generators):
        raise ValueError("the target distinguished open is not contained in the source distinguished open")

    def restrict(element):
        element = source(element)
        numerator = target_unit(element.numerator())
        denominator = target_unit(element.denominator())
        return numerator * denominator.inverse_of_unit()

    return source.Mor(target)(restrict)


class DistinguishedAffineCoverRefinement(CoveringFamilyMorphism):
    r"""A refinement morphism between distinguished affine covers of one affine scheme.

    This is a morphism in :class:`DistinguishedAffineCovers`, hence already a
    morphism of :class:`CoveringFamilies` in ``AffSch_R/X``.  Its component on
    a fine chart is the corresponding inclusion in that slice; geometric
    consumers can recover the underlying scheme inclusion with
    :meth:`inclusion`.
    """

    def fine_cover(self):
        return self.domain()

    def coarse_cover(self):
        return self.codomain()

    def ambient_scheme(self):
        return self.fine_cover().ambient_scheme()

    def inclusion(self, fine_index):
        fine_index = self.fine_cover().chart_label(fine_index)
        return self.component(fine_index).left()

    chart_map = inclusion

    def geometric_cochain_map(self, sheaf):
        from dzack_research.preamble.categories.schemes.geometric_cohomology import (
            _affine_cover_refinement_cochain_map,
        )

        return _affine_cover_refinement_cochain_map(self, sheaf)

    def geometric_cohomology_comparison(self, sheaf, degree):
        from dzack_research.preamble.categories.schemes.geometric_cohomology import (
            _affine_cover_refinement_cohomology_map,
        )

        return _affine_cover_refinement_cohomology_map(self, sheaf, degree)


class DistinguishedAffineCoverHomset(CoveringFamilyHomset):
    r"""The refinement Hom between two distinguished affine covers."""

    Element = DistinguishedAffineCoverRefinement


class DistinguishedAffineCoverHomCategoryConstruction(
    CoveringFamilyHomCategoryConstruction
):
    r"""The Hom family of distinguished affine covers."""

    def fixed_category_class(self):
        return DistinguishedAffineCoverHomset


class ZariskiCoveringFamilies(OwnedParameterizedCategory):
    r"""Finite covering families in the big Zariski site ``Sch_R/X``.

    For a scheme ``X`` over ``R`` the underlying site category is the slice
    ``Sch_R/X``.  This category is the represented Zariski coverage on that
    slice: its objects are finite covering families selected by Zariski-open
    cover constructions.  Specializations such as finite affine atlases build
    their objects here rather than using all covering families of the slice as
    though every family were a Zariski cover.

    The singleton identity family is the canonical specimen and is available
    for every scheme, affine or not::

        sage: from dzack_research.preamble.all import QQ, ProjectiveSpaces
        sage: line = ProjectiveSpaces(QQ)(1)
        sage: coverage = zariski_coverage(line)
        sage: coverage.site_category().base_object() is line
        True
        sage: identity_cover = coverage.an_object()
        sage: identity_cover in coverage
        True
        sage: identity_cover.target().arrow() == line.categorical_identity_morphism()
        True
    """

    def parameter_category(self):
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        return Schemes(self.scheme().scheme_base_ring())

    def scheme(self):
        return self.base()

    def site_category(self):
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        return Schemes(self.scheme().scheme_base_ring()).SliceCategory(self.scheme())

    @cached_method
    def slice_target(self):
        r"""The terminal object ``id_X`` of ``Sch_R/X``."""
        return self.site_category().an_object()

    def super_categories(self):
        return [CoveringFamilies(self.site_category())]

    def an_object(self):
        target = self.slice_target()
        identity = self.site_category().Mor(target, target).identity()
        return self.family(target, (identity,), {})

    class ParentMethods:
        r"""A finite family admitted by the represented Zariski coverage."""

        def __init__(self, **rest) -> None:
            super().__init__(**rest)
            target_arrow = self.target().arrow()
            scheme = target_arrow.codomain()
            match target_arrow == scheme.categorical_identity_morphism():
                case True:
                    pass
                case False:
                    raise ValueError(
                        "a Zariski covering family of X has target id_X in Sch_R/X"
                    )
            embeddings = tuple(
                self.member(index).left()
                for index in self.index_set()
            )
            match all(
                embedding.is_open_immersion() is True
                for embedding in embeddings
            ):
                case True:
                    pass
                case False:
                    raise TypeError(
                        "a Zariski covering family consists of open immersions"
                    )
            match scheme.is_covered_by_open_immersions(embeddings):
                case True:
                    pass
                case False:
                    raise ValueError(
                        "the represented open immersions do not jointly cover the scheme"
                    )

    def _repr_object_names(self):
        return f"finite Zariski covering families of {self.scheme()}"


@cached_function(key=lambda scheme: id(scheme))
def zariski_coverage(scheme) -> Category:
    r"""The represented finite Zariski coverage of ``Sch_R/X``."""

    category = ZariskiCoveringFamilies(scheme)
    return Coverage(category.site_category(), category)


class DistinguishedAffineCovers(OwnedCategory):
    r"""Represented distinguished affine covering families.

    With no parameter this is the catalogue containing every represented
    distinguished affine cover.  ``DistinguishedAffineCovers(X)`` is its fibre
    over one affine scheme ``X``; that fibre is a subcategory of covering
    families in the slice ``AffSch_R/X`` and is the selected family category
    for the distinguished-affine coverage of ``X``.
    """

    _HomCategory = DistinguishedAffineCoverHomCategoryConstruction

    @staticmethod
    @cached_function(
        key=lambda cls, scheme=None: (
            cls,
            None if scheme is None else id(scheme),
        )
    )
    def __classcall__(cls, scheme=None):
        match cls:
            case DynamicMetaclass():
                return cls.__base__(scheme)
            case _:
                return typecall(cls, scheme)

    def __init__(self, scheme=None) -> None:
        self._scheme = scheme
        super().__init__()

    def scheme(self):
        return self._scheme

    def site_category(self):
        scheme = self.scheme()
        if scheme is None:
            raise ValueError("the global cover catalogue has no single site category")
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        affine_schemes = Schemes(scheme.scheme_base_ring()).Affine()
        return affine_schemes.SliceCategory(scheme)

    def coverage(self):
        scheme = self.scheme()
        if scheme is None:
            raise ValueError("the global cover catalogue does not select one coverage")
        return distinguished_affine_coverage(scheme)

    @cached_method
    def slice_target(self):
        r"""The terminal slice object ``id_X`` shared by covers in this fibre."""
        return self.site_category().an_object()

    def super_categories(self):
        scheme = self.scheme()
        if scheme is None:
            return [Objects()]
        return [
            DistinguishedAffineCovers(),
            CoveringFamilies(self.site_category()),
        ]

    def an_object(self):
        scheme = self.scheme()
        if scheme is None:
            scheme = RingedSpaces().an_object()
        return scheme.distinguished_open_cover(scheme.coordinate_algebra().one())

    def _repr_object_names(self):
        scheme = self.scheme()
        if scheme is None:
            return "distinguished affine covers"
        return f"distinguished affine covering families of {scheme}"


    def _call_(self, elements):
        r"""Construct ``{D(f_i) -> X}`` through the covering-family entry."""
        scheme = self.scheme()
        assert scheme is not None, "a distinguished cover is constructed over its specified scheme"
        algebra = scheme.coordinate_algebra()
        values = tuple(algebra(element) for element in elements)
        assert values, "a represented distinguished cover has at least one open"
        assert algebra.ideal(*values).contains_ambient_element(algebra.one()), (
            "the defining elements of a distinguished affine cover generate the unit ideal"
        )
        labels = finite_ordered_set(range(len(values)))
        defining_elements = finite_indexed_family(
            labels, lambda label: values[int(labels.ranking_map()(label))],
            name="Defining elements of the distinguished opens",
        )
        site = self.site_category()
        target = self.slice_target()
        opens = finite_indexed_family(
            labels, lambda label: scheme.distinguished_open(defining_elements[label]),
            name="Distinguished opens",
        )
        charts = finite_indexed_family(
            labels, lambda label: site.object(opens[label].inclusion()),
            name="Affine charts over the covered scheme",
        )
        members = finite_indexed_family(
            labels, lambda label: site.Mor(charts[label], target)(opens[label].inclusion()),
            name="Distinguished affine cover arrows",
        )

        def overlap_data(left, right):
            overlap = scheme.distinguished_open(defining_elements[left] * defining_elements[right])
            apex = site.object(overlap.inclusion())
            return (
                apex,
                site.Mor(apex, charts[left])(overlap.inclusion_into(opens[left])),
                site.Mor(apex, charts[right])(overlap.inclusion_into(opens[right])),
            )

        overlaps = {pair: overlap_data(*pair) for pair in combinations(tuple(labels), 2)}
        return self.family(target, members, overlaps, defining_elements=defining_elements)

    class ParentMethods:
        r"""A cover whose defining elements refine its already constructed family.

        The family owns its target, index set, arrows and overlap spans.
        This level adds only the elements defining its distinguished opens;
        their corresponding family has already been checked at the entry.
        """

        def __init__(self, defining_elements, **rest) -> None:
            self._defining_elements = defining_elements
            super().__init__(**rest)
            scheme = self.ambient_scheme()
            algebra = scheme.coordinate_algebra()
            assert defining_elements.index_set() is self.index_set(), (
                "the defining elements and cover arrows have one indexing set"
            )
            assert self.target().arrow() == scheme.categorical_identity_morphism(), (
                "a distinguished cover of X has target id_X in the slice"
            )
            assert algebra.ideal(*defining_elements).contains_ambient_element(algebra.one()), (
                "the defining elements generate the unit ideal"
            )
            assert all(
                self.open(label) is scheme.distinguished_open(self.defining_element(label))
                for label in self.index_set()
            ), "each selected chart is the distinguished open of its defining element"

        def _cache_key(self) -> int:
            return id(self)

        def ambient_scheme(self):
            r"""The affine scheme ``X`` this is a cover of."""
            return self.target().arrow().codomain()

        def defining_elements(self):
            return self._defining_elements

        def defining_element(self, index):
            r"""``f_i``, the element whose distinguished open is the chart at ``index``."""
            return self._defining_elements[self.chart_label(index)]

        def opens(self):
            return tuple(self.open(index) for index in self.atlas())

        def atlas(self):
            r"""The set the charts are indexed by, and the only source of chart labels."""
            return self.index_set()

        def chart_label(self, index):
            r"""Read ``index`` as a label of this cover's atlas."""
            return self.atlas()(index)

        def chart_position(self, index):
            r"""Where the chart at ``index`` sits in the atlas order."""
            return int(self.atlas().ranking_map()(self.chart_label(index)))

        def open(self, index):
            r"""``D(f_i)``, the chart at ``index``."""
            return self.member(self.chart_label(index)).domain().arrow().domain()

        def intersection_indices(self, *indices):
            r"""Read the stated chart labels, deduplicated and in the atlas order."""
            labels = {self.chart_label(index) for index in indices}
            assert labels, "an affine-cover intersection requires at least one chart"
            return tuple(sorted(labels, key=self.atlas().ranking_map()))

        def intersection(self, *indices):
            r"""Return ``D(prod_i f_i)``, the intersection of the selected charts."""
            return self._intersection_of_labels(self.intersection_indices(*indices))

        @cached_method
        def _intersection_of_labels(self, labels):
            match len(labels):
                case 1:
                    return self.open(labels[0])
                case _:
                    element = self.ambient_scheme().coordinate_algebra().one()
                    for label in labels:
                        element *= self.defining_element(label)
                    return self.ambient_scheme().distinguished_open(element)

        def overlap(self, left_index, right_index):
            return self.intersection(left_index, right_index)

        @cached_method
        def cech_site(self):
            r"""The finite Čech site of this cover.

            Its objects are the whole scheme, the charts, and the pairwise
            intersections, ordered by reverse inclusion, so its arrows are the
            restriction directions of the cover equalizer.  It records the finite
            computation the descent data perform; it does not replace the
            Zariski site.
            """
            labels = [()]
            labels.extend((index,) for index in self.atlas())
            labels.extend(combinations(tuple(self.atlas()), 2))
            return PosetCategory(
                finite_ordered_set(tuple(labels)),
                le=lambda finer, coarser: set(coarser).issubset(set(finer)),
            )

        @cached_method
        def cech_covering_family(self):
            r"""The chart family as a covering family of :meth:`cech_site`."""
            site = self.cech_site()
            category = _CechCoveringFamilies(self)
            target = site(())
            members = finite_indexed_family(
                self.atlas(),
                lambda index: site.Mor(site((index,)), target).unique(),
                name="Čech cover arrows",
            )
            overlaps = {
                (left_index, right_index): (
                    site(self.intersection_indices(left_index, right_index)),
                    site.Mor(site(self.intersection_indices(left_index, right_index)), site((left_index,))).unique(),
                    site.Mor(site(self.intersection_indices(left_index, right_index)), site((right_index,))).unique(),
                )
                for left_index, right_index in combinations(tuple(self.atlas()), 2)
            }
            return category.family(target, members, overlaps)

        @cached_method
        def cech_coverage(self) -> Category:
            r"""Return the coverage generated by this cover's Čech family."""
            return Coverage(
                self.cech_site(),
                _CechCoveringFamilies(self),
            )

        def structure_sheaf_restriction(self, chart_index, other_index):
            r"""``O(U_i) -> O(U_i cap U_j)``."""
            return self.ambient_scheme().structure_sheaf().restriction_map(
                self.open(chart_index),
                self.overlap(chart_index, other_index),
            )

        @cached_method
        def restrict_module(self, module, chart_index, *intersection_indices):
            r"""Return ``M_i|_{U_I}`` by scalar extension along ``O(U_i) -> O(U_I)``.

            A local algebra restricted as a module is the restricted algebra, so
            forgetting algebra structure does not construct a second scalar
            extension.
            """
            from dzack_research.preamble.categories.algebras.algebras import Algebras

            chart = self.open(chart_index)
            chart_ring = chart.coordinate_algebra()
            assert module.base_ring() is chart_ring, "a local module is defined over the selected affine chart"
            target = self.intersection(chart_index, *intersection_indices)
            match module:
                case _ if target is chart:
                    return module
                case _ if module in Algebras(chart_ring).Associative().Unital():
                    return self.restrict_algebra(module, chart_index, *intersection_indices)
                case _:
                    ring_map = self.ambient_scheme().structure_sheaf().restriction_map(chart, target)
                    restricted = module.base_change(ring_map)
                    assert restricted.base_ring() is target.coordinate_algebra(), (
                        "module base change did not land over the intersection section ring"
                    )
                    return restricted

        @cached_method
        def restrict_algebra(self, algebra, chart_index, *intersection_indices):
            r"""Return ``A_i|_{U_I}`` by algebra scalar extension along ``O(U_i) -> O(U_I)``."""
            from dzack_research.preamble.categories.algebras.algebras import Algebras

            chart = self.open(chart_index)
            chart_ring = chart.coordinate_algebra()
            assert algebra in Algebras(chart_ring).Associative().Unital(), "a local algebra is defined over the selected affine chart"
            target = self.intersection(chart_index, *intersection_indices)
            if target is chart:
                return algebra
            ring_map = self.ambient_scheme().structure_sheaf().restriction_map(chart, target)
            restricted = Algebras(chart_ring).Associative().Unital().scalar_extension(ring_map)(algebra)
            assert restricted in Algebras(target.coordinate_algebra()).Associative().Unital(), (
                "algebra scalar extension did not land over the intersection section ring"
            )
            return restricted

        def glue_modules(self, local_modules, transitions):
            r"""Return the glued module sheaf on this affine cover."""

            from dzack_research.preamble.categories.schemes.gluing import ModuleGluingData

            return ModuleGluingData(self)(local_modules, transitions).sheaf()

        def glue_algebras(self, local_algebras, transitions):
            r"""Return the glued algebra sheaf on this affine cover."""
            from dzack_research.preamble.categories.schemes.gluing import AlgebraGluingData

            return AlgebraGluingData(self)(local_algebras, transitions).sheaf()

        def common_refinement(self, other):
            r"""The span of refinements from ``{D(f_i g_j)}`` to these two covers.

            The returned object is a categorical span in this cover category.
            Its apex is the common refinement; its two legs are actual
            :class:`DistinguishedAffineCoverRefinement` morphisms.
            """
            assert other.ambient_scheme() is self.ambient_scheme(), "covers of one scheme are refined together"
            category = self.category()
            index_pairs = tuple(
                (left, right)
                for left in self.atlas()
                for right in other.atlas()
            )
            fine = category(
                tuple(
                    self.defining_element(left) * other.defining_element(right)
                    for left, right in index_pairs
                )
            )
            site = self.site_category()

            def refinement_to(coarse, which):
                index_map = {
                    fine_index: index_pairs[fine.chart_position(fine_index)][which]
                    for fine_index in fine.atlas()
                }
                components = {}
                for fine_index in fine.atlas():
                    coarse_index = index_map[fine_index]
                    inclusion = fine.open(fine_index).inclusion_into(
                        coarse.open(coarse_index)
                    )
                    components[fine_index] = site.Mor(
                        fine.member(fine_index).domain(),
                        coarse.member(coarse_index).domain(),
                    )(inclusion)
                return category.Mor(fine, coarse)(index_map, components)

            return category.span(
                refinement_to(self, 0),
                refinement_to(other, 1),
            )

        def _repr_(self):
            return f"Distinguished affine cover of {self.ambient_scheme()} by {self.atlas().cardinality()} opens"


@cached_function(key=lambda scheme: id(scheme))
def distinguished_affine_coverage(scheme) -> Category:
    r"""The distinguished-open coverage in ``AffSch_R/X``."""

    category = DistinguishedAffineCovers(scheme)
    return Coverage(
        category.site_category(),
        category,
    )


class _AffineModuleSheafEngine:
    r"""The quasi-coherent sheaf ``M~`` on the represented distinguished-open basis."""

    def __init__(self, scheme, module, **rest) -> None:
        algebra = scheme.coordinate_algebra()
        if module.base_ring() is not algebra:
            raise ValueError("an affine module sheaf requires a module over the scheme coordinate ring")
        self._scheme = scheme
        self._module = module
        self._local_sections = {}
        super().__init__(**rest)

    def ringed_space(self):
        return self._scheme

    scheme = ringed_space

    def module(self):
        return self._module

    def global_sections(self):
        return self.module()

    def geometric_cohomology_complex(self, cover=None):
        r"""Return the affine Čech complex computing this sheaf's cohomology."""
        from dzack_research.preamble.categories.schemes.geometric_cohomology import (
            _affine_geometric_cohomology_complex,
        )

        return _affine_geometric_cohomology_complex(self, cover=cover)

    def geometric_cohomology(self, degree):
        r"""Return the represented affine cohomology in ``degree``."""
        return self.geometric_cohomology_complex().cohomology(int(degree))

    def geometric_scalar_cohomology_map(self, degree, scalar, *, cover=None):
        r"""Return the cohomology map induced by scalar multiplication."""
        from dzack_research.preamble.categories.schemes.geometric_cohomology import (
            _affine_geometric_scalar_cohomology_map,
        )

        return _affine_geometric_scalar_cohomology_map(
            self,
            degree,
            scalar,
            cover=cover,
        )

    def stalk(self, point):
        r"""``M~_p = M_p``, the module localized at the prime of the point."""
        spectrum = self.scheme().underlying_space()
        assert point.parent() is spectrum, "a stalk is taken at a point of the scheme's own spectrum"
        return self.module().localize_at_prime(point.ideal())

    def sections_on_distinguished_open(self, distinguished_open):
        if not _is_distinguished_open_of(distinguished_open, self.scheme()):
            raise ValueError("module sections are requested on a different affine scheme")
        key = id(distinguished_open)
        selected = self._local_sections.get(key)
        if selected is not None and selected.base_ring() is distinguished_open.coordinate_algebra():
            return selected
        section_ring = self.scheme().structure_sheaf().sections_on_distinguished_open(
            distinguished_open
        )
        selected = section_ring.localize_module(self.module())
        self._local_sections[key] = selected
        return selected

    def restriction_map(self, source_open, target_open):
        r"""Return the module restriction, linear over the structure-sheaf restriction."""


        ambient = self.scheme()
        structure_restriction = ambient.structure_sheaf().restriction_map(
            source_open,
            target_open,
        )
        source_sections = (
            self.global_sections()
            if source_open is ambient
            else self.sections_on_distinguished_open(source_open)
        )
        if target_open is ambient:
            return source_sections.module_category().Mor(source_sections, source_sections).identity()
        target_sections = self.sections_on_distinguished_open(target_open)

        if source_open is ambient:
            localization = target_sections.localization_functor()
            if localization.ring_map() is not structure_restriction:
                raise ArithmeticError("module and function restriction selected different localization maps")
            return localization.unit(self.module(), localized=target_sections)
        if source_open is target_open:
            return source_sections.module_category().Mor(source_sections, source_sections).identity()

        restricted_target = target_sections.restrict_scalars(structure_restriction)
        source_ring = source_sections.base_ring()
        original_ring = source_ring.localization_source()

        def restrict(section):
            section = source_sections(section)
            inverse_denominator = structure_restriction(
                source_ring.fraction(original_ring.one(), section.denominator())
            )
            target_value = target_sections.scalar_multiple(
                inverse_denominator,
                target_sections.fraction(section.numerator()),
            )
            return restricted_target.wrap(target_value)

        return source_sections.module_category().Mor(source_sections, restricted_target).elementwise(
            restrict,
            verify_linearity=False,
        )

    def sheaf_category(self):
        r"""``QCoh(X)``, the category this sheaf is an object of."""
        return QuasiCoherentSheaves(self.scheme())

    def _repr_(self):
        return f"Affine module sheaf associated to {self.module()} on {self.scheme()}"


class AffineQuasiCoherentSheafMorphism(Morphism):
    r"""A morphism of affine quasi-coherent sheaves, represented by its module map."""

    def __init__(self, parent, module_morphism) -> None:
        Morphism.__init__(self, parent)
        source_module = self.domain().module()
        target_module = self.codomain().module()
        self._underlying_module_morphism = source_module.module_category().Mor(
            source_module,
            target_module,
        )(module_morphism)

    def underlying_module_morphism(self):
        return self._underlying_module_morphism

    def kernel(self):
        return self.underlying_module_morphism().kernel()

    def cokernel(self):
        return self.underlying_module_morphism().cokernel()

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, AffineQuasiCoherentSheafMorphism)
            and other.parent() is self.parent()
            and other.underlying_module_morphism() == self.underlying_module_morphism()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __mul__(self, other):
        if not isinstance(other, AffineQuasiCoherentSheafMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return self.parent().homset_category().Mor(
            other.domain(),
            self.codomain(),
        )(
            self.underlying_module_morphism()
            * other.underlying_module_morphism()
        )


class AffineQuasiCoherentSheafHomset(CategoricalHomset):
    r"""``Hom_{O_X}(M~,N~)`` on affine ``X``, with sheaf endpoints."""

    Element = AffineQuasiCoherentSheafMorphism

    def _element_constructor_(self, module_morphism):
        match module_morphism:
            case AffineQuasiCoherentSheafMorphism() if module_morphism.parent() is self:
                return module_morphism
            case AffineQuasiCoherentSheafMorphism():
                if (
                    module_morphism.domain() is not self.domain()
                    or module_morphism.codomain() is not self.codomain()
                ):
                    raise ValueError("the quasi-coherent sheaf morphism has the wrong endpoints")
                module_morphism = module_morphism.underlying_module_morphism()
            case _:
                pass
        return self.element_class(self, module_morphism)

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on an endomorphism Hom")
        module = self.domain().module()
        return self(module.module_category().Mor(module, module).identity())


class QuasiCoherentSheafHomCategoryConstruction(HomCategoryConstruction):
    r"""Choose the represented Hom realization from the sheaves' defining presentations."""

    def fixed_category_class_for(self, domain, codomain):
        category = self.base_category()
        scheme = category.scheme()

        trivialized = category.Invertible().WithChosenTrivialization()
        match (domain in trivialized, codomain in trivialized):
            case (True, True):
                from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                    _ChosenTrivializationQuasiCoherentHomset,
                )

                return _ChosenTrivializationQuasiCoherentHomset
            case _:
                pass

        invertible = category.Invertible()
        match (domain in invertible, codomain in invertible):
            case (True, True):
                from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                    _PullbackLineBundleQuasiCoherentHomset,
                )

                return _PullbackLineBundleQuasiCoherentHomset
            case _:
                pass

        from dzack_research.preamble.categories.schemes.schemes import Schemes

        affine = Schemes(scheme.scheme_base_ring()).Affine()
        match scheme in affine:
            case True:
                return AffineQuasiCoherentSheafHomset
            case False:
                from dzack_research.preamble.categories.schemes.gluing import (
                    FiniteAtlasModuleSheafHomset,
                    _finite_atlas_of_sheaf_placement,
                    _finite_atlas_quasi_coherent_sheaves,
                )

                atlas = _finite_atlas_of_sheaf_placement(domain)
                represented = _finite_atlas_quasi_coherent_sheaves(atlas)
                assert domain.category().is_subcategory(represented), (
                    "a represented non-affine quasi-coherent source must carry its concrete sheaf placement"
                )
                assert codomain.category().is_subcategory(represented), (
                    "a finite-atlas quasi-coherent Hom requires endpoints on the same represented Čech site"
                )
                return FiniteAtlasModuleSheafHomset


class QuasiCoherentSheaves(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""Quasi-coherent ``O_X``-modules on one scheme ``X``.

    On an affine ``X = Spec A`` the association ``M |-> M~`` is an equivalence
    onto this category, inverse to global sections (Stacks, Tag 01I8).  The
    represented affine operations are therefore read through ``Modules(A)``
    rather than defined a second time.  For the
    same reason a morphism of quasi-coherent sheaves on an affine scheme is
    determined by a morphism of the two modules.  The represented sheaf arrow
    retains the sheaves themselves as categorical endpoints and stores that
    module map as its affine realization.

    On a non-affine represented scheme, quasi-coherent sheaves are carried by
    the finite-atlas/descent objects in ``schemes.gluing``.  The affine
    equivalence methods below deliberately retain their affine assertion;
    placement in this category no longer means that every object has one
    global coordinate-algebra presentation.
    """

    def scheme(self):
        return self.base()

    def _repr_object_names(self):
        return f"quasi-coherent sheaves on {self.scheme()}"

    def super_categories(self):
        return [ModuleSheaves(self.scheme())]

    def an_object(self):
        return self.scheme().structure_sheaf()

    _HomCategory = QuasiCoherentSheafHomCategoryConstruction

    def object(self, *, categories=(), construction_data=None, _engine):
        r"""Construct one represented quasi-coherent sheaf through this owner.

        ``_engine`` is the private realization of the sheaf in the represented
        regime selected by the caller.  Stronger semantic placement is joined
        here so specializations do not initialize a second ``Parent`` shell.
        """
        category = (
            self
            if not categories
            else Category.join((self, *tuple(categories)))
        )
        return _object_of(
            category,
            _engine=(self, _engine, None),
            **dict(construction_data or {}),
        )

    class SubcategoryMethods:
        def Invertible(self):
            r"""Return the full subcategory of invertible ``O_X``-modules."""
            return self._with_axiom("Invertible")

    class Invertible(CategoryWithAxiom):
        r"""Invertible quasi-coherent sheaves on ``X``.

        Schemes are locally ringed spaces, so an invertible ``O_X``-module is
        equivalently a locally free ``O_X``-module of rank one (Stacks,
        Tag 0B8M).  A particular trivializing cover is additional data and is
        recorded separately by the line-bundle descent category.
        """

        class ParentMethods:
            def is_invertible(self) -> bool:
                return True

        def WithChosenTrivialization(self):
            r"""Return invertible sheaves carrying one selected trivializing cover."""
            return InvertibleSheavesWithChosenTrivialization(self.base_category().scheme())

    def module_category(self):
        r"""``Modules(A)``: the category this one is equivalent to, for affine ``X``."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules
        from dzack_research.preamble.categories.schemes.schemes import Schemes

        scheme = self.scheme()
        assert scheme in Schemes(scheme.scheme_base_ring()).Affine(), (
            "the equivalence with a module category is stated on an affine scheme; on a glued "
            "scheme a quasi-coherent sheaf is gluing data over an affine cover"
        )
        return Modules(scheme.coordinate_algebra())

    @cached_method(key=lambda self, module: id(module))
    def associated_sheaf(self, module):
        r"""``M |-> M~``, the equivalence out of ``Modules(A)``."""
        assert module in self.module_category(), (
            "the associated sheaf is taken of a module over the coordinate algebra"
        )
        return self.object(
            construction_data={"scheme": self.scheme(), "module": module},
            _engine=_AffineModuleSheafEngine,
        )

    def global_sections(self, sheaf):
        r"""``M~ |-> M``, the inverse equivalence."""
        assert sheaf in self, "global sections are taken of a sheaf on this scheme"
        return sheaf.global_sections()

    def local_presentation(self, sheaf):
        r"""``O_X^m -> O_X^n``, the presentation whose cokernel is ``F``.

        A finitely presented module has a chosen relation morphism between
        free modules, and the equivalence reads it as a morphism of free
        ``O_X``-modules; the hypothesis is exactly that chosen presentation,
        which is what makes the sheaf coherent on this affine chart.
        """
        from dzack_research.preamble.categories.modules.pure.modules import (
            ModulesWithChosenFinitePresentation,
        )

        module = self.global_sections(sheaf)
        assert module in ModulesWithChosenFinitePresentation(module.base_ring()), (
            "a local presentation of a quasi-coherent sheaf requires a chosen finite "
            "presentation of the module it comes from"
        )
        return module.presentation()


class InvertibleSheavesWithChosenTrivialization(OwnedParameterizedCategory):
    r"""Invertible sheaves on ``X`` with one selected trivializing affine cover.

    The choice of cover is structure on an invertible sheaf, not part of the
    invertibility property.  Forgetting that choice lands in
    ``QuasiCoherentSheaves(X).Invertible()``.
    """

    def scheme(self):
        return self.base()

    def super_categories(self):
        return [QuasiCoherentSheaves(self.scheme()).Invertible()]

    def _repr_object_names(self):
        return f"invertible sheaves on {self.scheme()} with a chosen trivialization"

    def _realize(self, engine, **construction_data):
        r"""Realize one represented trivialization through the quasi-coherent sheaf owner."""
        return QuasiCoherentSheaves(self.scheme()).object(
            categories=(self,),
            construction_data=construction_data,
            _engine=engine,
        )

    def _call_(
        self,
        gluing_datum,
        transition_units=None,
        *,
        section_space=None,
        associated_divisor=None,
    ):
        r"""Construct an invertible sheaf from rank-one affine descent data.

        A distinguished-cover module descent datum already contains its
        transition isomorphisms.  A finite affine atlas supplies the equivalent
        rank-one datum by its transition units.
        """
        assert gluing_datum.scheme() is self.scheme(), (
            "a chosen trivialization belongs to an invertible sheaf on this scheme"
        )
        match transition_units:
            case None:
                assert section_space is None and associated_divisor is None, (
                    "section-space and divisor data belong to finite-atlas trivializations"
                )
                from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                    _DistinguishedCoverInvertibleSheafEngine,
                )

                return gluing_datum.sheaf(
                    categories=(self,),
                    construction_data={"gluing_datum": gluing_datum},
                    _engine=_DistinguishedCoverInvertibleSheafEngine,
                )
            case _:
                from dzack_research.preamble.categories.divisors.invertible_sheaves import (
                    _FiniteAtlasInvertibleSheafEngine,
                )

                return self._realize(
                    _FiniteAtlasInvertibleSheafEngine,
                    gluing_datum=gluing_datum,
                    transition_units=transition_units,
                    section_space=section_space,
                    associated_divisor=associated_divisor,
                )

    def trivial(self, cover):
        r"""Return ``O_X`` with the selected distinguished affine trivialization ``cover``."""
        from dzack_research.preamble.categories.schemes.gluing import ModuleGluingData

        assert cover.ambient_scheme() is self.scheme(), (
            "a trivialized structure sheaf uses a cover of this scheme"
        )
        return self(ModuleGluingData(cover).an_object())

    class ParentMethods:
        def trivializing_cover(self):
            r"""Return the selected affine cover on which this line bundle is trivialized."""
            return self.cover()


class RingedSpaces(CategoryPacketMethods, OwnedCategory):
    r"""Ringed spaces ``(X,O_X)``."""

    def an_object(self):
        r"""The affine ringed space ``Spec(ZZ)``."""
        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
        return (_own_ring(SageZZ)).affine_spectrum()

    @classmethod
    def _repr_object_names(cls):
        return "ringed spaces"

    def super_categories(self):
        return [SheafedSpaces()]

    def LocallyRinged(self):
        return LocallyRingedSpaces()

    class ParentMethods:
        @cached_method
        def structure_sheaf(self):
            return _structure_sheaf(self)

        @cached_method
        def cartier_divisor_sheaf(self):
            r"""Return the quotient sheaf ``K_X^*/O_X^*``.

            Here ``K_X`` is the sheaf of total quotient rings.  Cartier
            divisors are the global sections of this quotient sheaf (Stacks
            Project, Tag 02AQ).
            """
            from dzack_research.preamble.categories.divisors.cartier_divisor_groups import (
                _cartier_divisor_quotient_sheaf,
            )

            return _cartier_divisor_quotient_sheaf(self)

        @cached_method
        def cartier_divisor_group(self):
            r"""Return ``CDiv(X)=Gamma(X,K_X^*/O_X^*)``."""
            return self.cartier_divisor_sheaf().global_sections()

        @cached_method
        def underlying_space(self):
            return _scheme_underlying_space(self)


class LocallyRingedHomCategoryConstruction(HomCategoryConstruction):
    r"""The Hom of locally ringed spaces, realized by the domain's presentation.

    An affine scheme is determined by its ring, and maps out of a glued
    scheme by compatible maps out of its charts (Stacks, Tags 01I1, 01JA).
    Those presentations choose the arrow engine, not another Hom object.
    """

    def fixed_category_class_for(self, domain, codomain):
        return domain._locally_ringed_homset_class()


class LocallyRingedSpaces(CategoryPacketMethods, OwnedCategory):
    r"""Ringed spaces whose stalks are local rings."""

    _HomCategory = LocallyRingedHomCategoryConstruction

    def an_object(self):
        r"""The locally ringed affine scheme ``Spec(ZZ)``."""
        return RingedSpaces().an_object()

    @classmethod
    def _repr_object_names(cls):
        return "locally ringed spaces"

    def super_categories(self):
        return [RingedSpaces()]

    class ParentMethods:
        def stalk(self, point):
            return self.structure_sheaf().stalk(point)

        def covering_family(
            self,
            charts,
            embeddings,
            overlaps,
            *,
            ambient_chart_index,
        ):
            r"""Return the represented covering family in ``LRS/X``.

            The currently represented covering certificate contains this
            ambient space as one chart embedded by ``id_X``.  Non-affine
            overlaps remain slice objects with both overlap legs; they are not
            replaced by spectra of global sections.

            Unverified specimen: the overlap itself is the apex of the owned
            overlap span, not a private overlap record::

                sage: from dzack_research.preamble.all import QQ, AffineSpaces
                sage: plane = AffineSpaces(QQ)(2, names=("x", "y"))
                sage: x, y = plane.coordinate_algebra().algebra_generators()
                sage: punctured = plane.closed_subscheme(x, y).open_complement()
                sage: cover = plane.covering_family(
                ....:     {"whole": plane, "punctured": punctured},
                ....:     {"whole": plane.categorical_identity_morphism(), "punctured": punctured.inclusion()},
                ....:     {("whole", "punctured"): (punctured, punctured.inclusion(), punctured.categorical_identity_morphism())},
                ....:     ambient_chart_index="whole",
                ....: )
                sage: overlap = cover.overlap_span("whole", "punctured")
                sage: overlap.apex().arrow().domain() is punctured
                True
            """
            from dzack_research.preamble.categories.schemes.covering_families import (
                _ringed_covering_family,
            )

            site = LocallyRingedSpaces().SliceCategory(self)
            return _ringed_covering_family(
                self,
                site,
                charts,
                embeddings,
                overlaps,
                ambient_chart_index=ambient_chart_index,
            )


__all__ = [
    "AlgebraSheaves",
    "DistinguishedAffineCoverRefinement",
    "DistinguishedAffineCovers",
    "distinguished_affine_coverage",
    "LocallyRingedSpaces",
    "ModuleSheaves",
    "QuasiCoherentSheaves",
    "RingedSpaces",
    "SheafObjects",
    "SheafedSpaces",
    "ZariskiCoveringFamilies",
    "zariski_coverage",
]
