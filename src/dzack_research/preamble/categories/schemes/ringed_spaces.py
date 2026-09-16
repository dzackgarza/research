"""Owned ringed-space structure used by the scheme hierarchy."""

from itertools import combinations

from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.classcall_metaclass import typecall
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.abstract_categories.presheaves import (
    Coverage,
    CoveringFamilies,
    CoveringFamily,
)
from dzack_research.preamble.categories.abstract_categories.products import PosetCategory
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family


class SchemeUnderlyingSpace(SageObject):
    r"""The underlying topological space of a represented ringed space.

    Sage's scheme parents do not expose a separate topological-space parent.
    The owned API nevertheless keeps the mathematical structure explicit: this
    object remembers the represented scheme and is the space on which open
    and closed-subspace structure can later be attached.
    """

    def __init__(self, ringed_space) -> None:
        self._ringed_space = ringed_space

    def ringed_space(self):
        return self._ringed_space

    scheme = ringed_space

    def _repr_(self) -> str:
        return f"Underlying topological space of {self.ringed_space()}"


class SheafObjects(OwnedParameterizedCategory):
    r"""Represented sheaves on one base space.

    This is the semantic placement shared by the concrete sheaf carriers in
    the scheme, divisor, and monodromy subtrees.  A sheaf that materializes a
    specific site/coverage additionally lies in the corresponding
    :class:`~dzack_research.preamble.categories.abstract_categories.presheaves.Sheaves`
    full subcategory; this base-space category does not replace that descent
    datum or pretend that every represented space currently exposes one common
    site presentation.
    """

    def space(self):
        return self.base()

    def _repr_object_names(self):
        return f"sheaves on {self.space()}"

    def super_categories(self):
        return [Objects()]

    def an_object(self):
        return _TerminalSheaf(self.space())


class _TerminalSheaf(Parent):
    r"""The terminal one-section sheaf on a represented base space.

    This is the canonical inhabitant of :class:`SheafObjects`: it exists on
    every site/topological space and therefore does not assume that the base
    has ringed-space structure merely to witness that the sheaf category is
    inhabited.  Concrete sheaves retain their own section/stalk models.
    """

    def __init__(self, space) -> None:
        self._space = space
        Parent.__init__(self, category=SheafObjects(space))

    def base_space(self):
        return self._space

    space = base_space

    def _repr_(self) -> str:
        return f"Terminal sheaf on {self.base_space()}"


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


class StructureSheaf(Parent):
    r"""The represented structure sheaf ``O_X`` of a ringed space ``X``."""

    def __init__(self, ringed_space) -> None:
        self._ringed_space = ringed_space
        self._restriction_maps = {}
        from dzack_research.preamble.categories.abstract_categories.cat import Cat

        Parent.__init__(
            self,
            category=Cat().meet(
                (
                    AlgebraSheaves(ringed_space),
                    QuasiCoherentSheaves(ringed_space),
                )
            ),
        )

    def ringed_space(self):
        return self._ringed_space

    scheme = ringed_space

    def global_sections(self):
        r"""Return ``Gamma(X,O_X)`` in the exact cases represented live."""
        operation = getattr(self.ringed_space(), "_structure_sheaf_global_sections", None)
        assert callable(operation), (
            f"global sections of the structure sheaf of {self.ringed_space()} require a selected represented operation"
        )
        return operation()

    sections = global_sections

    def sections_on_distinguished_open(self, distinguished_open):
        r"""Return ``O_X(D(f)) = Gamma(X,O_X)_f`` for an affine scheme."""
        operation = getattr(
            self.ringed_space(),
            "_structure_sheaf_sections_on_distinguished_open",
            None,
        )
        assert callable(operation), (
            "distinguished-open structure-sheaf sections require a selected represented operation on this ringed space"
        )
        return operation(distinguished_open)

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

        return AffineModuleSheaf(self.ringed_space(), module)

    def stalk(self, point):
        r"""Return ``O_{X,p}`` for a represented affine prime point."""
        operation = getattr(self.ringed_space(), "_structure_sheaf_stalk", None)
        assert callable(operation), (
            "structure-sheaf stalks require a selected represented stalk operation on this ringed space"
        )
        return operation(point)

    def _repr_(self) -> str:
        return f"Structure sheaf O_{{{self.scheme()}}}"


def _is_distinguished_open_of(open_subscheme, ambient) -> bool:
    is_distinguished_open = getattr(open_subscheme, "is_distinguished_open", None)
    inclusion = getattr(open_subscheme, "inclusion", None)
    return (
        callable(is_distinguished_open)
        and is_distinguished_open()
        and callable(inclusion)
        and inclusion().codomain() is ambient
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


class DistinguishedAffineCovers(OwnedCategory):
    r"""Represented distinguished affine covering families.

    With no parameter this is the catalogue containing every represented
    distinguished affine cover.  ``DistinguishedAffineCovers(X)`` is its fibre
    over one affine scheme ``X``; that fibre is a subcategory of covering
    families in the slice ``AffSch_R/X`` and is the selected family category
    for the distinguished-affine coverage of ``X``.
    """

    @staticmethod
    @cached_function(
        key=lambda cls, scheme=None: (
            cls,
            None if scheme is None else id(scheme),
        )
    )
    def __classcall__(cls, scheme=None):
        if isinstance(cls, DynamicMetaclass):
            return cls.__base__(scheme)
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


@cached_function(key=lambda scheme: id(scheme))
def distinguished_affine_coverage(scheme) -> Coverage:
    r"""The distinguished-open coverage in ``AffSch_R/X``."""

    category = DistinguishedAffineCovers(scheme)
    return Coverage(
        category.site_category(),
        category,
        name=f"Distinguished-affine coverage of {scheme}",
    )


class _DistinguishedCechCoveringFamilies(OwnedCategory):
    r"""The chosen Čech family of one represented distinguished affine cover."""

    @staticmethod
    @cached_function(key=lambda cls, cover: (cls, id(cover)))
    def __classcall__(cls, cover):
        if isinstance(cls, DynamicMetaclass):
            return cls.__base__(cover)
        return typecall(cls, cover)

    def __init__(self, cover) -> None:
        self._cover = cover
        super().__init__()

    def cover(self):
        return self._cover

    def site_category(self):
        return self.cover().cech_site()

    def super_categories(self):
        return [CoveringFamilies(self.site_category())]

    def an_object(self):
        return self.cover().cech_covering_family()

    def _repr_object_names(self):
        return f"chosen Čech covering family of {self.cover()}"


class DistinguishedAffineCover(CoveringFamily):
    r"""A finite affine cover ``X = union_i D(f_i)`` on a represented affine scheme."""

    def _cache_key(self) -> int:
        r"""Use identity when this cover parametrizes a descent category."""
        return id(self)

    def __init__(self, scheme, elements) -> None:
        algebra = scheme.coordinate_algebra()
        elements = tuple(algebra(element) for element in elements)
        if not elements:
            raise ValueError("a distinguished affine cover requires at least one open")
        cover_ideal = algebra.ideal(*elements)
        if not cover_ideal.contains_ambient_element(algebra.one()):
            raise ValueError("the stated distinguished opens do not cover the affine scheme")
        self._scheme = scheme
        self._elements = elements
        self._opens = tuple(scheme.distinguished_open(element) for element in elements)
        self._atlas = finite_ordered_set(range(len(self._opens)))
        self._intersections = {
            (label,): self._opens[int(self._atlas.ranking_map()(label))]
            for label in self._atlas
        }
        self._restricted_modules = {}
        self._restricted_algebras = {}

        category = DistinguishedAffineCovers(scheme)
        site = category.site_category()
        target = site.an_object()
        chart_objects = {
            index: site.object(self.open(index).inclusion()) for index in self._atlas
        }
        members = finite_indexed_family(
            self._atlas,
            lambda index: site.Mor(chart_objects[index], target)(
                self.open(index).inclusion()
            ),
            name="Distinguished affine cover arrows",
        )
        overlaps = {}
        for left_index, right_index in combinations(tuple(self._atlas), 2):
            overlap = self.intersection(left_index, right_index)
            overlap_object = site.object(overlap.inclusion())
            overlaps[left_index, right_index] = (
                overlap_object,
                site.Mor(overlap_object, chart_objects[left_index])(
                    overlap.inclusion_into(self.open(left_index))
                ),
                site.Mor(overlap_object, chart_objects[right_index])(
                    overlap.inclusion_into(self.open(right_index))
                ),
            )
        CoveringFamily.__init__(self, category, target, members, overlaps)

    def ambient_scheme(self):
        return self._scheme

    def defining_elements(self):
        return self._elements

    def defining_element(self, index):
        r"""``f_i``, the element whose distinguished open is the chart at ``index``."""
        return self._elements[self.chart_position(index)]

    def opens(self):
        return self._opens

    def atlas(self):
        r"""The set the charts are indexed by, and the only source of chart labels.

        A cover has as many charts as it has defining elements, and each is
        addressed by its own label rather than by a position in a sequence, so
        a caller ranges over this set instead of counting the charts.
        """
        return self._atlas

    def chart_label(self, index):
        r"""Read ``index`` as a label of this cover's atlas."""
        return self.atlas()(index)

    def chart_position(self, index):
        r"""Where the chart at ``index`` sits in the atlas order.

        The charts and the defining elements are held in that order, so this
        is the one place a position is read, and it is read from the atlas
        rather than assumed of the label.
        """
        return int(self.atlas().ranking_map()(self.chart_label(index)))

    def open(self, index):
        return self._opens[self.chart_position(index)]

    def intersection_indices(self, *indices):
        r"""Read the stated chart labels, deduplicated and in the atlas order."""
        labels = {self.chart_label(index) for index in indices}
        if not labels:
            raise ValueError("an affine-cover intersection requires at least one chart")
        return tuple(sorted(labels, key=self.atlas().ranking_map()))

    def intersection(self, *indices):
        r"""Return ``D(prod_i f_i)``, the represented intersection of selected charts."""

        key = self.intersection_indices(*indices)
        selected = self._intersections.get(key)
        if selected is None:
            algebra = self.ambient_scheme().coordinate_algebra()
            element = algebra.one()
            for label in key:
                element *= self.defining_element(label)
            selected = self.ambient_scheme().distinguished_open(element)
            self._intersections[key] = selected
        return selected

    def overlap(self, left_index, right_index):
        return self.intersection(left_index, right_index)

    @cached_method
    def cech_site(self):
        r"""Return the finite Čech site used by this cover's represented descent computation.

        Its objects are the ambient affine, the charts, and the pairwise
        intersections.  The order is reverse inclusion, hence its arrows are
        precisely the restriction directions needed by the cover equalizer.
        This finite site records the computation already performed by the
        gluing datum; it does not claim to replace the full Zariski site.
        """

        labels = [()]
        labels.extend((index,) for index in self.atlas())
        labels.extend(combinations(tuple(self.atlas()), 2))
        label_set = finite_ordered_set(tuple(labels))
        return PosetCategory(
            label_set,
            le=lambda finer, coarser: set(coarser).issubset(set(finer)),
        )

    @cached_method
    def cech_covering_family(self):
        r"""The chart family as a covering family of :meth:`cech_site`."""

        site = self.cech_site()
        category = _DistinguishedCechCoveringFamilies(self)
        target = site(())
        members = finite_indexed_family(
            self.atlas(),
            lambda index: site.Mor(site((index,)), target).unique(),
            name="Čech cover arrows",
        )
        overlaps = {}
        for left_index, right_index in combinations(tuple(self.atlas()), 2):
            pair = self.intersection_indices(left_index, right_index)
            overlap = site(pair)
            overlaps[left_index, right_index] = (
                overlap,
                site.Mor(overlap, site((left_index,))).unique(),
                site.Mor(overlap, site((right_index,))).unique(),
            )
        return CoveringFamily(category, target, members, overlaps)

    @cached_method
    def cech_coverage(self) -> Coverage:
        r"""Return the coverage presentation generated by this cover's Čech family."""

        category = _DistinguishedCechCoveringFamilies(self)
        return Coverage(
            self.cech_site(),
            category,
            name=f"Čech coverage presentation of {self}",
        )

    def structure_sheaf_restriction(self, chart_index, other_index):
        overlap = self.overlap(chart_index, other_index)
        return self.ambient_scheme().structure_sheaf().restriction_map(
            self.open(chart_index),
            overlap,
        )

    def restrict_module(self, module, chart_index, *intersection_indices):
        r"""Return ``M_i|_{U_I}`` by scalar extension along ``O(U_i) -> O(U_I)``."""

        chart_index = self.chart_label(chart_index)
        chart = self.open(chart_index)
        if module.base_ring() is not chart.coordinate_algebra():
            raise ValueError("a local module must be defined over the selected affine chart")
        indices = self.intersection_indices(chart_index, *intersection_indices)
        target = self.intersection(*indices)
        if target is chart:
            return module
        key = (id(module), indices)
        cached = self._restricted_modules.get(key)
        if cached is not None:
            cached_module, restricted = cached
            if cached_module is module:
                return restricted
        ring_map = self.ambient_scheme().structure_sheaf().restriction_map(chart, target)
        restricted = module.base_change(ring_map)
        if restricted.base_ring() is not target.coordinate_algebra():
            raise ArithmeticError("module base change did not land over the intersection section ring")
        self._restricted_modules[key] = (module, restricted)
        return restricted

    def restrict_algebra(self, algebra, chart_index, *intersection_indices):
        r"""Return ``A_i|_{U_I}`` by algebra scalar extension along ``O(U_i) -> O(U_I)``."""

        from dzack_research.preamble.categories.algebras.algebras import Algebras
        chart_index = self.chart_label(chart_index)
        chart = self.open(chart_index)
        chart_ring = chart.coordinate_algebra()
        if algebra not in Algebras(chart_ring).Associative().Unital():
            raise ValueError("a local algebra must be defined over the selected affine chart")
        indices = self.intersection_indices(chart_index, *intersection_indices)
        target = self.intersection(*indices)
        if target is chart:
            return algebra
        key = (id(algebra), indices)
        cached = self._restricted_algebras.get(key)
        if cached is not None:
            cached_algebra, restricted = cached
            if cached_algebra is algebra:
                return restricted

        ring_map = self.ambient_scheme().structure_sheaf().restriction_map(chart, target)
        restricted = Algebras(chart_ring).Associative().Unital().scalar_extension(ring_map)(algebra)
        target_ring = target.coordinate_algebra()
        if restricted not in Algebras(target_ring).Associative().Unital():
            raise ArithmeticError(
                "algebra scalar extension did not land over the intersection section ring"
            )
        self._restricted_algebras[key] = (algebra, restricted)
        # Forgetting algebra structure must not manufacture a second copy of
        # the same scalar extension. Module descent therefore reuses this exact
        # restricted algebra as its underlying module object.
        self._restricted_modules[key] = (algebra, restricted)
        return restricted

    def glue_modules(self, local_modules, transitions):
        r"""Return the descent datum and glued module sheaf on this affine cover."""

        from dzack_research.preamble.categories.schemes.gluing import ModuleGluingDatum

        return ModuleGluingDatum(self, local_modules, transitions)

    def glue_algebras(self, local_algebras, transitions):
        r"""Return finite algebra descent data on this affine cover."""

        from dzack_research.preamble.categories.schemes.gluing import AlgebraGluingDatum

        return AlgebraGluingDatum(self, local_algebras, transitions)

    def common_refinement(self, other):
        r"""The refinement ``{D(f_i g_j)}`` of this cover and ``other``, with its comparison maps."""

        assert other.ambient_scheme() is self.ambient_scheme(), "covers of one scheme are refined together"
        return CoverRefinement(self, other)

    def _repr_(self):
        return f"Distinguished affine cover of {self.ambient_scheme()} by {self.atlas().cardinality()} opens"


class CoverRefinement(SageObject):
    r"""``{D(f_i g_j)}`` refining ``{D(f_i)}`` and ``{D(g_j)}`` on one affine scheme.

    A refinement of a cover ``U = {U_i}`` is a cover ``V = {V_k}`` with a map
    ``k |-> i(k)`` of index sets and inclusions ``V_k <= U_{i(k)}`` (Stacks,
    Tag 00VI).  The common refinement of two distinguished covers is indexed
    by pairs ``(i, j)``, refines both through the two projections, and its
    inclusions are open immersions whose pullbacks are the restriction maps of
    the structure sheaf, so restriction along ``X > U_i > V_{ij}`` composes
    to restriction along ``X > V_{ij}``.
    """

    def __init__(self, first_cover, second_cover) -> None:
        self._coarse_covers = (first_cover, second_cover)
        self._index_pairs = tuple(
            (left, right)
            for left in first_cover.atlas()
            for right in second_cover.atlas()
        )
        self._fine_cover = DistinguishedAffineCover(
            first_cover.ambient_scheme(),
            tuple(
                first_cover.defining_element(left) * second_cover.defining_element(right)
                for left, right in self._index_pairs
            ),
        )

    def ambient_scheme(self):
        return self._fine_cover.ambient_scheme()

    def coarse_cover(self, which):
        return self._coarse_covers[int(which)]

    def fine_cover(self):
        return self._fine_cover

    def geometric_cohomology_comparison(self, sheaf, degree):
        r"""Return this refinement's comparison on affine sheaf cohomology."""
        from dzack_research.preamble.categories.schemes.geometric_cohomology import (
            _AffineCoverRefinementCohomologyComparison,
        )

        return _AffineCoverRefinementCohomologyComparison(self, sheaf, degree)

    def index_map(self, which, fine_index):
        r"""``k |-> i(k)``: the coarse chart of cover ``which`` containing fine chart ``k``."""
        return self._index_pairs[int(fine_index)][int(which)]

    def inclusion(self, which, fine_index):
        r"""The open immersion ``V_k -> U_{i(k)}`` into the chosen coarse cover."""
        coarse_open = self.coarse_cover(which).open(self.index_map(which, fine_index))
        return self.fine_cover().open(fine_index).inclusion_into(coarse_open)

    def _repr_(self):
        return f"Common refinement of {self.coarse_cover(0)} and {self.coarse_cover(1)}"


class AffineModuleSheaf(Parent):
    r"""The quasi-coherent sheaf ``M~`` on the represented distinguished-open basis."""

    def __init__(self, scheme, module) -> None:
        algebra = scheme.coordinate_algebra()
        if module.base_ring() is not algebra:
            raise ValueError("an affine module sheaf requires a module over the scheme coordinate ring")
        self._scheme = scheme
        self._module = module
        self._local_sections = {}
        Parent.__init__(self, category=QuasiCoherentSheaves(scheme))

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


class QuasiCoherentSheaves(OwnedParameterizedCategory):
    r"""Quasi-coherent ``O_X``-modules on one scheme ``X``.

    On an affine ``X = Spec A`` the association ``M |-> M~`` is an equivalence
    onto this category, inverse to global sections (Stacks, Tag 01I8).  The
    represented affine operations are therefore read through ``Modules(A)``
    rather than defined a second time.  For the
    same reason a morphism of quasi-coherent sheaves on an affine scheme is a
    morphism of the two modules, so no separate arrow type is introduced.

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

    def associated_sheaf(self, module):
        r"""``M |-> M~``, the equivalence out of ``Modules(A)``."""
        assert module in self.module_category(), (
            "the associated sheaf is taken of a module over the coordinate algebra"
        )
        return self.scheme().associated_module_sheaf(module)

    def global_sections(self, sheaf):
        r"""``M~ |-> M``, the inverse equivalence."""
        assert sheaf in self, "global sections are taken of a sheaf on this scheme"
        return sheaf.global_sections()

    def sheaf_morphisms(self, source, target):
        r"""``Hom_{O_X}(M~, N~) = Hom_A(M, N)``, where morphisms of these sheaves live."""
        source_sections = self.global_sections(source)
        target_sections = self.global_sections(target)
        return source_sections.module_category().Mor(source_sections, target_sections)

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
        return [Objects()]

    def LocallyRinged(self):
        return LocallyRingedSpaces()

    class ParentMethods:
        @cached_method
        def structure_sheaf(self):
            return StructureSheaf(self)

        @cached_method
        def underlying_space(self):
            specialized = getattr(self, "_scheme_underlying_space", None)
            if specialized is not None:
                return specialized()
            return SchemeUnderlyingSpace(self)


class LocallyRingedSpaces(CategoryPacketMethods, OwnedCategory):
    r"""Ringed spaces whose stalks are local rings."""

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
            r"""Return a represented finite covering family of this ringed space.

            The currently verified regime contains this ambient space as one
            chart.  Non-affine overlaps remain spaces with their two embeddings;
            they are never replaced by spectra of global sections.
            """
            from dzack_research.preamble.categories.schemes.covering_families import (
                RingedCoveringFamily,
            )

            return RingedCoveringFamily(
                self,
                charts,
                embeddings,
                overlaps,
                ambient_chart_index=ambient_chart_index,
            )


__all__ = [
    "AlgebraSheaves",
    "AffineModuleSheaf",
    "CoverRefinement",
    "DistinguishedAffineCover",
    "DistinguishedAffineCovers",
    "distinguished_affine_coverage",
    "LocallyRingedSpaces",
    "ModuleSheaves",
    "QuasiCoherentSheaves",
    "RingedSpaces",
    "SchemeUnderlyingSpace",
    "SheafObjects",
    "StructureSheaf",
]
