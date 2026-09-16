r"""Presheaves, coverages, descent equalizers, and sheaves.

The category of presheaves on ``C`` with values in ``D`` is

.. MATH::

    \mathrm{Presh}(C, D) := [C^{\mathrm{op}}, D],

the functor category the tree already owns, reached from ``C`` by
``C.presheaves(D)`` (``D = Sets()`` when omitted).  No new category class is
introduced: ``C.presheaves(D)`` is ``Cat().Mor(C.opposite(), D)``, so a
presheaf is an object of a functor category and its morphisms are natural
transformations.  The value category is a parameter because that is what the
later passage to sheaves of modules, of algebras, and to stacks changes.

The construction is a bifunctor ``Cat^op x Cat -> Cat``.  ``Cat`` is not an
object of itself here, so the bifunctor is stated on ``Cat`` by its two
actions: on objects, ``Cat().presheaves(C, D)``; on morphisms
``F: C' -> C`` and ``G: D -> D'``, ``Cat().presheaf_transport(F, G)`` is the
functor ``[C^op, D] -> [C'^op, D']``, ``P |-> G o P o F^op`` on objects and
``eta |-> G eta F^op`` on natural transformations.

The Yoneda embedding ``y: C -> Presh(C)`` sends ``X`` to the representable
presheaf ``Mor_C(-, X)`` and ``h: X -> Y`` to postcomposition with ``h``
(Mac Lane, *Categories for the Working Mathematician*, III.2; nLab,
*Yoneda embedding*).  It is what distinguishes ``[C^op, Set]`` from a category
of maps: its objects are functors, and ``y`` is a functor into it.

A coverage is represented by a selected subcategory of finite covering
families.  For ``F: C^op -> D`` and a cover ``{U_i -> U}``, with ``D`` carrying
the selected finite products and equalizers used here, :class:`DescentEqualizer`
retains the canonical map

.. MATH::

    F(U) \longrightarrow
    \operatorname{Eq}\left(
      \prod_i F(U_i) \rightrightarrows \prod_{i<j} F(U_{ij})
    \right).

Sheafhood is represented by inverses to these canonical maps, not by a boolean
predicate.  Consequently :class:`Sheaves` is the full subcategory of the
presheaf category whose objects retain that descent data, while its morphisms
remain exactly natural transformations of the underlying presheaves.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
from itertools import combinations

from sage.categories.category import Category
from sage.categories.map import Map
from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function
from sage.misc.classcall_metaclass import typecall
from sage.structure.dynamic_class import DynamicMetaclass
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalIsomorphism,
    _category_homset,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    Objects,
    OwnedCategory,
)
from dzack_research.preamble.categories.functors.core import (
    Functor,
    NaturalTransformation,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    finite_indexed_family,
)
from dzack_research.preamble.owned_category_bases import Category as OwnedCategoryBase


class _OppositeFunctor(Functor):
    r"""``F^op: C^op -> D^op``, the functor ``F`` read on the opposite categories."""

    def __init__(self, functor: Functor) -> None:
        self._functor = functor
        super().__init__(functor.domain().opposite(), functor.codomain().opposite())

    def original(self) -> Functor:
        return self._functor

    def _apply_object(self, obj: Parent) -> Parent:
        return self.codomain()(self.original()(obj.underlying_object()))

    def _apply_morphism(self, morphism: Map) -> Map:
        # An arrow op(A) -> op(B) of C^op is an arrow B -> A of C; its image
        # is F(B) -> F(A), read as the arrow op(F(A)) -> op(F(B)) of D^op.
        return self.codomain().Mor(self(morphism.domain()), self(morphism.codomain()))(
            self.original()(morphism.underlying_arrow())
        )

    def _repr_(self) -> str:
        return f"({self.original()})^op"


class _RepresentablePresheaf(Functor):
    r"""``Mor_C(-, X): C^op -> Set`` for one object ``X`` of ``C``."""

    def __init__(self, category: Category, representing_object: Parent) -> None:
        from dzack_research.preamble.categories.sets.set_categories import Sets

        assert representing_object in category, (
            "a representable presheaf is represented by an object of its category"
        )
        self._category = category
        self._representing_object = representing_object
        super().__init__(category.opposite(), Sets())

    def representing_object(self) -> Parent:
        return self._representing_object

    def _apply_object(self, obj: Parent) -> Parent:
        return self._category.Mor(obj.underlying_object(), self.representing_object())

    def _apply_morphism(self, morphism: Map) -> Map:
        r"""Precomposition: an arrow ``u: B -> A`` of ``C`` gives ``g |-> g o u``."""
        from dzack_research.preamble.categories.sets.set_categories import Sets

        precompose = morphism.underlying_arrow()
        return Sets().Mor(self(morphism.domain()), self(morphism.codomain()))(
            lambda arrow: arrow * precompose
        )

    def _repr_(self) -> str:
        return f"Mor_{self._category}(-, {self.representing_object()})"


class _YonedaEmbedding(Functor):
    r"""``y: C -> [C^op, Set]``, ``X |-> Mor_C(-, X)``."""

    _faithful = True

    def __init__(self, category: Category) -> None:
        self._category = category
        super().__init__(category, category.presheaves())

    def _apply_object(self, obj: Parent) -> Parent:
        return self.codomain().object(_RepresentablePresheaf(self._category, obj))

    def _apply_morphism(self, morphism: Map) -> Map:
        r"""Postcomposition with ``h: X -> Y``, natural in the argument."""
        from dzack_research.preamble.categories.sets.set_categories import Sets

        source = self(morphism.domain())
        target = self(morphism.codomain())
        source_presheaf = source.functor()
        target_presheaf = target.functor()

        def component(obj):
            return Sets().Mor(source_presheaf(obj), target_presheaf(obj))(
                lambda arrow: morphism * arrow
            )

        return self.codomain().Mor(source, target)(
            NaturalTransformation(source_presheaf, target_presheaf, component)
        )

    def _repr_(self) -> str:
        return f"Yoneda embedding of {self._category}"


class _PresheafTransport(Functor):
    r"""``[C^op, D] -> [C'^op, D']`` along ``F: C' -> C`` and ``G: D -> D'``.

    This is the action of the presheaf bifunctor on a pair of arrows of
    ``Cat``: contravariant in the site through precomposition with ``F^op``,
    covariant in the values through postcomposition with ``G``.
    """

    def __init__(self, site_functor: Functor, value_functor: Functor) -> None:
        self._site_functor = site_functor
        self._value_functor = value_functor
        self._opposite_site_functor = _OppositeFunctor(site_functor)
        super().__init__(
            site_functor.codomain().presheaves(value_functor.domain()),
            site_functor.domain().presheaves(value_functor.codomain()),
        )

    def site_functor(self) -> Functor:
        return self._site_functor

    def value_functor(self) -> Functor:
        return self._value_functor

    def _transport_presheaf(self, presheaf: Functor) -> Functor:
        return self._opposite_site_functor.then(presheaf).then(self.value_functor())

    def _apply_object(self, obj: Parent) -> Parent:
        return self.codomain().object(self._transport_presheaf(obj.functor()))

    def _apply_morphism(self, morphism: Map) -> Map:
        transformation = morphism.transformation()
        source = self._transport_presheaf(transformation.source())
        target = self._transport_presheaf(transformation.target())
        opposite_site = self._opposite_site_functor
        value = self.value_functor()

        def component(obj):
            return value(transformation.component(opposite_site(obj)))

        return self.codomain().Mor(self(morphism.domain()), self(morphism.codomain()))(
            NaturalTransformation(source, target, component)
        )

    def _repr_(self) -> str:
        return f"Presh({self.site_functor()}, {self.value_functor()})"


def _finite_family(values, *, name: str) -> IndexedFamily:
    r"""Normalize finite labelled data without discarding its index set."""

    if isinstance(values, IndexedFamily):
        if not values.cardinality().is_finite():
            raise TypeError(f"{name} must be a finite indexed family")
        return values
    if isinstance(values, Mapping):
        labels = finite_ordered_set(tuple(values))
        return finite_indexed_family(labels, lambda label: values[label], name=name)
    entries = tuple(values)
    labels = finite_ordered_set(range(len(entries)))
    return finite_indexed_family(
        labels,
        lambda label: entries[int(labels.ranking_map()(label))],
        name=name,
    )


class CoveringOverlap(SageObject):
    r"""One represented overlap in a covering family.

    For cover arrows ``U_i -> U`` and ``U_j -> U`` this retains an object
    ``U_ij`` and its two arrows to ``U_i`` and ``U_j``.  The commuting
    triangle is verified when the datum is constructed; no later sheaf check
    has to reconstruct or guess the overlap.
    """

    def __init__(
        self,
        covering_family,
        left_index,
        right_index,
        overlap_object: Parent,
        left_map: Morphism,
        right_map: Morphism,
    ) -> None:
        self._covering_family = covering_family
        self._left_index = left_index
        self._right_index = right_index
        self._overlap_object = overlap_object
        self._left_map = left_map
        self._right_map = right_map
        category = covering_family.site_category()
        left = covering_family.member(left_index)
        right = covering_family.member(right_index)
        if overlap_object not in category:
            raise TypeError("a covering overlap must be an object of the site category")
        if (
            left_map.domain() is not overlap_object
            or left_map.codomain() is not left.domain()
            or left_map not in category.Mor(overlap_object, left.domain())
        ):
            raise ValueError("the left overlap map has the wrong site endpoints")
        if (
            right_map.domain() is not overlap_object
            or right_map.codomain() is not right.domain()
            or right_map not in category.Mor(overlap_object, right.domain())
        ):
            raise ValueError("the right overlap map has the wrong site endpoints")
        if (left * left_map == right * right_map) is not True:
            raise ValueError("the overlap maps do not commute with the two cover arrows")

    def covering_family(self):
        return self._covering_family

    def left_index(self):
        return self._left_index

    def right_index(self):
        return self._right_index

    def overlap_object(self) -> Parent:
        return self._overlap_object

    object = overlap_object

    def left_map(self) -> Morphism:
        return self._left_map

    def right_map(self) -> Morphism:
        return self._right_map


class CoveringFamily(Parent):
    r"""A finite family ``{U_i -> U}`` with represented pair overlaps."""

    def __init__(self, category, target: Parent, members, overlaps) -> None:
        self._target = target
        self._members = _finite_family(members, name="Cover arrows")
        site = category.site_category()
        if target not in site:
            raise TypeError("a covering family target must be an object of the site category")
        if int(self._members.cardinality().finite_value()) == 0:
            raise ValueError("the represented covering-family construction is nonempty")
        for arrow in self._members:
            if not isinstance(arrow, Morphism):
                raise TypeError("a covering family consists of site morphisms")
            if arrow.codomain() is not target or arrow.domain() not in site:
                raise ValueError("a cover arrow has the wrong target or leaves the site")
            if arrow not in site.Mor(arrow.domain(), target):
                raise ValueError("a cover arrow is not a morphism of the site category")

        ranking = self._members.index_set().ranking_map()
        expected_pairs = tuple(combinations(tuple(self._members.index_set()), 2))
        self._pair_index_set = finite_ordered_set(expected_pairs)
        raw_overlaps = dict(overlaps)
        normalized = {}
        for raw_pair, datum in raw_overlaps.items():
            left_index, right_index = raw_pair
            if ranking(left_index) > ranking(right_index):
                left_index, right_index = right_index, left_index
                overlap_object, right_map, left_map = datum
            else:
                overlap_object, left_map, right_map = datum
            normalized[left_index, right_index] = (
                overlap_object,
                left_map,
                right_map,
            )
        if set(normalized) != set(expected_pairs):
            raise ValueError("a covering family requires one represented overlap for each pair")
        Parent.__init__(self, category=category)
        self._overlaps = {
            pair: CoveringOverlap(self, pair[0], pair[1], *normalized[pair])
            for pair in expected_pairs
        }

    def covering_family_category(self):
        return self.category()

    def site_category(self) -> Category:
        return self.covering_family_category().site_category()

    def coverage(self):
        selected = getattr(self.covering_family_category(), "coverage", None)
        return None if selected is None else selected()

    def target(self) -> Parent:
        return self._target

    covered_object = target

    def members(self) -> IndexedFamily:
        return self._members

    def member(self, index) -> Morphism:
        return self.members()[index]

    def index_set(self) -> Parent:
        return self.members().index_set()

    def pair_index_set(self) -> Parent:
        return self._pair_index_set

    def overlap(self, left_index, right_index) -> CoveringOverlap:
        ranking = self.index_set().ranking_map()
        pair = (
            (left_index, right_index)
            if ranking(left_index) < ranking(right_index)
            else (right_index, left_index)
        )
        return self._overlaps[pair]

    overlap_datum = overlap

    def overlaps(self) -> IndexedFamily:
        return finite_indexed_family(
            self.pair_index_set(),
            lambda pair: self._overlaps[pair],
            name="Pair overlaps of a covering family",
        )

    def _repr_(self) -> str:
        return f"Covering family of {self.target()}"


class CoveringFamilies(OwnedCategory):
    r"""Represented finite covering families in one category ``C``."""

    @staticmethod
    def __classcall__(cls, site_category: Category):
        return Category.__classcall__(cls, site_category)

    def __init__(self, site_category: Category) -> None:
        self._site_category = site_category
        super().__init__()

    def site_category(self) -> Category:
        return self._site_category

    def super_categories(self):
        return [Objects()]

    def an_object(self) -> Parent:
        target = self.site_category().an_object()
        identity = _category_homset(self.site_category(), target, target).identity()
        return CoveringFamily(self, target, (identity,), {})

    def family(self, target: Parent, members, overlaps) -> CoveringFamily:
        return CoveringFamily(self, target, members, overlaps)

    def _repr_(self) -> str:
        return f"Covering families in {self.site_category()}"


class TrivialCoveringFamilies(OwnedCategoryBase):
    r"""Singleton identity covers, the trivial coverage on ``C``."""

    @staticmethod
    @cached_function(key=lambda cls, site_category: (cls, id(site_category)))
    def __classcall__(cls, site_category: Category):
        if isinstance(cls, DynamicMetaclass):
            return cls.__base__(site_category)
        return typecall(cls, site_category)

    def __init__(self, site_category: Category) -> None:
        self._site_category = site_category
        self._families = {}
        OwnedCategoryBase.__init__(self)

    def site_category(self) -> Category:
        return self._site_category

    def super_categories(self):
        return [CoveringFamilies(self.site_category())]

    def __contains__(self, candidate) -> bool:
        try:
            return candidate.category().is_subcategory(self)
        except (AttributeError, TypeError, ValueError):
            return False

    def family(self, target: Parent) -> CoveringFamily:
        if target not in self.site_category():
            raise TypeError("a trivial cover target must be an object of the site")
        key = id(target)
        cached = self._families.get(key)
        if cached is not None and cached.target() is target:
            return cached
        identity = _category_homset(self.site_category(), target, target).identity()
        cached = CoveringFamily(self, target, (identity,), {})
        self._families[key] = cached
        return cached

    def an_object(self) -> Parent:
        return self.family(self.site_category().an_object())

    def _repr_(self) -> str:
        return f"Trivial covering families in {self.site_category()}"


class Coverage(SageObject):
    r"""A selected category of covering families on a category ``C``.

    The second argument is the mathematical selection: it must be a
    subcategory of :class:`CoveringFamilies` on the same site.  Consequently
    the coverage never admits a family through an after-the-fact predicate or
    mutable registry; concrete theories construct their covers in the selected
    subcategory itself.
    """

    def __init__(
        self,
        site_category: Category,
        covering_families: Category,
        *,
        name: str | None = None,
    ) -> None:
        self._site_category = site_category
        self._name = name
        if not covering_families.is_subcategory(CoveringFamilies(site_category)):
            raise TypeError(
                "a coverage is selected by a subcategory of the site's covering families"
            )
        self._covering_families = covering_families

    def site_category(self) -> Category:
        return self._site_category

    def covering_families(self) -> Category:
        return self._covering_families

    @staticmethod
    def trivial(site_category: Category):
        return trivial_coverage(site_category)

    def sheaves(self, value_category: Category | None = None):
        if value_category is None:
            from dzack_research.preamble.categories.sets.set_categories import Sets

            value_category = Sets()
        return Sheaves(self, value_category)

    def _repr_(self) -> str:
        return self._name or f"Coverage on {self.site_category()}"


class DescentDataOnCover(OwnedCategoryBase):
    r"""Represented descent data relative to one covering family.

    This is the placement common to concrete descent theories: modules,
    algebras, or objects of another represented fibre theory may carry
    different local data and different Hom constructions, but they are all
    descent data on the same cover.  The concrete theory remains responsible
    for its transition maps, cocycle law, and morphisms; this category records
    the cover-relative mathematical placement instead of rediscovering it by
    inspecting the implementation class afterwards.
    """

    @staticmethod
    @cached_function(
        key=lambda cls, coverage, covering_family: (
            cls,
            id(coverage),
            id(covering_family),
        )
    )
    def __classcall__(cls, coverage: Coverage, covering_family):
        if isinstance(cls, DynamicMetaclass):
            return cls.__base__(coverage, covering_family)
        return typecall(cls, coverage, covering_family)

    def __init__(self, coverage: Coverage, covering_family) -> None:
        if covering_family not in coverage.covering_families():
            raise TypeError("descent data are attached to a covering family of the coverage")
        self._coverage = coverage
        self._covering_family = covering_family
        OwnedCategoryBase.__init__(self)

    def coverage(self) -> Coverage:
        return self._coverage

    def covering_family(self):
        return self._covering_family

    cover = covering_family

    def super_categories(self):
        return [Objects()]

    def __contains__(self, candidate) -> bool:
        try:
            return candidate.category().is_subcategory(self)
        except (AttributeError, TypeError, ValueError):
            return False

    def _repr_(self) -> str:
        return f"Descent data on {self.covering_family()}"


@cached_function(key=lambda site_category: id(site_category))
def trivial_coverage(site_category: Category) -> Coverage:
    r"""Return the trivial coverage consisting only of identity singleton covers."""

    return Coverage(
        site_category,
        TrivialCoveringFamilies(site_category),
        name=f"Trivial coverage on {site_category}",
    )


def _presheaf_functor(presheaf) -> Functor:
    if isinstance(presheaf, Functor):
        return presheaf
    selected = getattr(presheaf, "functor", None)
    if not callable(selected):
        raise TypeError("descent data requires a represented presheaf")
    functor = selected()
    if not isinstance(functor, Functor):
        raise TypeError("the represented presheaf does not retain a functor")
    return functor


def _opposite_arrow(site: Category, arrow: Morphism) -> Morphism:
    opposite = site.opposite()
    return opposite.Mor(
        opposite(arrow.codomain()),
        opposite(arrow.domain()),
    )(arrow)


def _identity_equalizer_construction(value_category: Category, obj: Parent):
    r"""The selected equalizer of ``id_obj`` with itself, without a backend."""

    from dzack_research.preamble.categories.abstract_categories.products import (
        SelectedLimitConstruction,
        _parallel_pair_diagram,
    )

    identity = _category_homset(value_category, obj, obj).identity()
    diagram = _parallel_pair_diagram(identity, identity, value_category)
    shape = diagram.domain()
    universal_cone = diagram.Cones().cone(
        obj,
        lambda _index: identity,
    )

    def factorizer(cone):
        return cone.structure_morphism(shape.source())

    return SelectedLimitConstruction(diagram, universal_cone, factorizer)


class DescentEqualizer(SageObject):
    r"""The canonical Čech equalizer comparison for one presheaf and cover."""

    def __init__(
        self,
        coverage: Coverage,
        presheaf,
        covering_family: CoveringFamily,
        *,
        equalizer_selector=None,
    ) -> None:
        self._coverage = coverage
        self._presheaf = _presheaf_functor(presheaf)
        self._covering_family = covering_family
        self._equalizer_selector = equalizer_selector
        if covering_family not in coverage.covering_families():
            raise TypeError("descent is stated only for a covering family of the coverage")
        site = coverage.site_category()
        if self._presheaf.domain() != site.opposite():
            raise ValueError("the presheaf has the wrong site for this coverage")
        self._value_category = self._presheaf.codomain()
        self._build()

    def coverage(self) -> Coverage:
        return self._coverage

    def presheaf(self) -> Functor:
        return self._presheaf

    def covering_family(self) -> CoveringFamily:
        return self._covering_family

    cover = covering_family

    def value_category(self) -> Category:
        return self._value_category

    def _value(self, obj: Parent) -> Parent:
        return self.presheaf()(self.coverage().site_category().opposite()(obj))

    def _restriction(self, arrow: Morphism) -> Morphism:
        return self.presheaf()(_opposite_arrow(self.coverage().site_category(), arrow))

    def _build(self) -> None:
        cover = self.covering_family()
        values = finite_indexed_family(
            cover.index_set(),
            lambda index: self._value(cover.member(index).domain()),
            name="Presheaf values on a cover",
        )
        self._local_product = self.value_category().product_construction(values)
        local_diagram = self._local_product.diagram()
        local_product = self._local_product.object()

        global_value = self._value(cover.target())
        global_cone = local_diagram.Cones().cone(
            global_value,
            lambda index: self._restriction(cover.member(index.value())),
        )
        self._restriction_to_product = self._local_product.factor(global_cone).apex_map()

        pairs = tuple(cover.pair_index_set())
        if not pairs:
            identity = _category_homset(
                self.value_category(), local_product, local_product
            ).identity()
            self._left = identity
            self._right = identity
            self._matching_product = None
        else:
            overlap_values = finite_indexed_family(
                cover.pair_index_set(),
                lambda pair: self._value(cover.overlap_datum(*pair).overlap_object()),
                name="Presheaf values on pair overlaps",
            )
            self._matching_product = self.value_category().product_construction(
                overlap_values
            )
            overlap_diagram = self._matching_product.diagram()

            def side_map(side: str):
                cone = overlap_diagram.Cones().cone(
                    local_product,
                    lambda index: self._overlap_leg(index.value(), side),
                )
                return self._matching_product.factor(cone).apex_map()

            self._left = side_map("left")
            self._right = side_map("right")
        if self._equalizer_selector is not None:
            self._equalizer = self._equalizer_selector(self)
        elif not pairs:
            self._equalizer = _identity_equalizer_construction(
                self.value_category(), local_product
            )
        else:
            self._equalizer = self.value_category().equalizer_construction(
                self._left,
                self._right,
            )

        equalizer_diagram = self._equalizer.diagram()
        shape = equalizer_diagram.domain()
        selected_inclusion = self._equalizer.structure_morphism(shape.source())
        if selected_inclusion is self._restriction_to_product:
            common = self._equalizer.structure_morphism(shape.target())
        else:
            common = self._left * self._restriction_to_product
            if (common == self._right * self._restriction_to_product) is not True:
                raise ValueError("presheaf restrictions do not form a cone over the Čech pair")
        global_equalizer_cone = equalizer_diagram.Cones().cone(
            global_value,
            lambda index: (
                self._restriction_to_product if index is shape.source() else common
            ),
        )
        if (
            global_value is self._equalizer.object()
            and selected_inclusion is self._restriction_to_product
        ):
            self._canonical_map = _category_homset(
                self.value_category(), global_value, global_value
            ).identity()
            return
        self._canonical_map = self._equalizer.factor(global_equalizer_cone).apex_map()

    def _overlap_leg(self, pair, side: str) -> Morphism:
        cover = self.covering_family()
        left_index, right_index = pair
        overlap = cover.overlap_datum(left_index, right_index)
        local_index = left_index if side == "left" else right_index
        overlap_map = overlap.left_map() if side == "left" else overlap.right_map()
        local_object = self._local_product.diagram().domain()(local_index)
        projection = self._local_product.structure_morphism(local_object)
        return self._restriction(overlap_map) * projection

    def local_product_construction(self):
        return self._local_product

    def restriction_to_product(self) -> Morphism:
        return self._restriction_to_product

    def matching_product_construction(self):
        return self._matching_product

    def parallel_maps(self) -> tuple[Morphism, Morphism]:
        return self._left, self._right

    def equalizer_construction(self):
        return self._equalizer

    def equalizer_object(self) -> Parent:
        return self.equalizer_construction().object()

    def canonical_map(self) -> Morphism:
        return self._canonical_map

    def comparison(self, inverse: Morphism) -> CategoricalIsomorphism:
        return self.value_category().Core().Mor(
            self.canonical_map().domain(),
            self.canonical_map().codomain(),
        )(self.canonical_map(), inverse)


class DescentEqualizerComparison(SageObject):
    r"""An actual isomorphism from ``F(U)`` to its selected descent equalizer."""

    def __init__(self, equalizer: DescentEqualizer, inverse: Morphism) -> None:
        self._equalizer = equalizer
        self._isomorphism = equalizer.comparison(inverse)

    def descent_equalizer(self) -> DescentEqualizer:
        return self._equalizer

    def covering_family(self) -> CoveringFamily:
        return self.descent_equalizer().covering_family()

    def presheaf(self) -> Functor:
        return self.descent_equalizer().presheaf()

    def isomorphism(self) -> CategoricalIsomorphism:
        return self._isomorphism

    comparison = isomorphism


class DescentData(SageObject):
    r"""Chosen equalizer-comparison data for every family of one coverage.

    ``inverse_for`` is proof data, not a predicate.  Given the canonical
    :class:`DescentEqualizer` for a represented cover it returns the inverse
    arrow to the canonical comparison.  The two inverse identities are then
    checked by :class:`CategoricalIsomorphism` when that cover is requested.
    Thus an unbounded coverage is represented by a rule for all of its covers,
    rather than by pretending they can be enumerated.

    Unverified separating specimen: the same presheaf fails descent for a
    two-member cover but has canonical descent data for the trivial coverage::

        sage: from dzack_research.preamble.categories.abstract_categories.products import PosetCategory
        sage: from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
        sage: from dzack_research.preamble.categories.sets.set_categories import Sets
        sage: labels = finite_ordered_set(("U", "U0", "U1", "U01"))
        sage: relations = {("U0", "U"), ("U1", "U"), ("U01", "U0"), ("U01", "U1"), ("U01", "U")}
        sage: site = PosetCategory(labels, le=lambda left, right: left == right or (left, right) in relations)
        sage: families = CoveringFamilies(site)
        sage: cover = families.family(
        ....:     site("U"),
        ....:     (
        ....:         site.Mor(site("U0"), site("U")).unique(),
        ....:         site.Mor(site("U1"), site("U")).unique(),
        ....:     ),
        ....:     {(0, 1): (
        ....:         site("U01"),
        ....:         site.Mor(site("U01"), site("U0")).unique(),
        ....:         site.Mor(site("U01"), site("U1")).unique(),
        ....:     )},
        ....: )
        sage: coverage = Coverage(site, families)
        sage: two = finite_ordered_set((0, 1)); one = finite_ordered_set((0,))
        sage: class FailingPresheaf(Functor):
        ....:     def __init__(self):
        ....:         super().__init__(site.opposite(), Sets())
        ....:     def _apply_object(self, obj):
        ....:         return two if obj.underlying_object() is site("U") else one
        ....:     def _apply_morphism(self, arrow):
        ....:         source, target = self(arrow.domain()), self(arrow.codomain())
        ....:         if source is target:
        ....:             return Sets().Mor(source, target).identity()
        ....:         return Sets().Mor(source, target)(lambda _point: target(0))
        sage: presheaf = FailingPresheaf()
        sage: bad = DescentData(
        ....:     coverage,
        ....:     presheaf,
        ....:     lambda equalizer: Sets().Mor(equalizer.equalizer_object(), two)(lambda _point: two(0)),
        ....: )
        sage: bad.comparison(cover)
        Traceback (most recent call last):
        ...
        ValueError: the supplied maps do not establish a left inverse
        sage: trivial = DescentData.trivial(presheaf)
        sage: identity_cover = trivial.coverage().covering_families().family(site("U"))
        sage: trivial.comparison(identity_cover).isomorphism().domain() is two
        True
    """

    def __init__(
        self,
        coverage: Coverage,
        presheaf,
        inverse_for: Callable[[DescentEqualizer], Morphism | DescentEqualizerComparison],
        *,
        equalizer_for=None,
    ) -> None:
        self._coverage = coverage
        self._presheaf = _presheaf_functor(presheaf)
        self._inverse_for = inverse_for
        self._equalizer_for = equalizer_for
        self._comparisons = {}
        if self._presheaf.domain() != coverage.site_category().opposite():
            raise ValueError("descent data and presheaf have different sites")

    @staticmethod
    def trivial(presheaf):
        r"""Return the canonical descent data for the trivial coverage.

        Every covering family in the trivial coverage is the singleton
        identity cover.  The presheaf value itself is selected as the
        equalizer object, with the canonical map into the one-factor product
        as its equalizer inclusion.  Hence the descent comparison is literally
        the identity even when equality of arbitrary maps in the value
        category is not decidable.
        """

        functor = _presheaf_functor(presheaf)
        site = functor.domain().base_category()
        coverage = trivial_coverage(site)

        def equalizer_for(equalizer: DescentEqualizer):
            from dzack_research.preamble.categories.abstract_categories.products import (
                SelectedLimitConstruction,
                _parallel_pair_diagram,
            )

            cover = equalizer.covering_family()
            label = next(iter(cover.index_set()))
            product = equalizer.local_product_construction()
            index = product.diagram().domain()(label)
            projection = product.structure_morphism(index)
            inclusion = equalizer.restriction_to_product()
            left, right = equalizer.parallel_maps()
            diagram = _parallel_pair_diagram(
                left,
                right,
                equalizer.value_category(),
            )
            shape = diagram.domain()
            global_value = inclusion.domain()
            universal_cone = diagram.Cones().cone(
                global_value,
                lambda position: (
                    inclusion
                    if position is shape.source()
                    else left * inclusion
                ),
            )

            def factorizer(cone):
                return projection * cone.structure_morphism(shape.source())

            return SelectedLimitConstruction(diagram, universal_cone, factorizer)

        def inverse_for(equalizer: DescentEqualizer):
            global_value = equalizer.canonical_map().domain()
            return _category_homset(
                equalizer.value_category(),
                global_value,
                global_value,
            ).identity()

        return DescentData(
            coverage,
            functor,
            inverse_for,
            equalizer_for=equalizer_for,
        )

    def coverage(self) -> Coverage:
        return self._coverage

    def presheaf(self) -> Functor:
        return self._presheaf

    def value_category(self) -> Category:
        return self.presheaf().codomain()

    def comparison(self, covering_family: CoveringFamily) -> DescentEqualizerComparison:
        if covering_family not in self.coverage().covering_families():
            raise TypeError("the requested family is outside this descent datum's coverage")
        key = id(covering_family)
        cached = self._comparisons.get(key)
        if cached is not None and cached.covering_family() is covering_family:
            return cached
        equalizer = DescentEqualizer(
            self.coverage(),
            self.presheaf(),
            covering_family,
            equalizer_selector=self._equalizer_for,
        )
        selected = self._inverse_for(equalizer)
        if isinstance(selected, DescentEqualizerComparison):
            if (
                selected.descent_equalizer().coverage() is not self.coverage()
                or selected.presheaf() is not self.presheaf()
                or selected.covering_family() is not covering_family
            ):
                raise ValueError("the supplied descent comparison belongs to different data")
            comparison = selected
        else:
            comparison = DescentEqualizerComparison(equalizer, selected)
        self._comparisons[key] = comparison
        return comparison


class SheafObject(Parent):
    r"""A presheaf equipped with descent data for a selected coverage."""

    def __init__(self, category, functor: Functor, descent_data: DescentData) -> None:
        self._functor = functor
        self._descent_data = descent_data
        Parent.__init__(self, category=category)

    def functor(self) -> Functor:
        return self._functor

    def descent_data(self) -> DescentData:
        return self._descent_data

    def arrow(self):
        return self.category().presheaf_category().category_of_categories().arrow(
            self.functor()
        )

    def _repr_(self) -> str:
        return f"Sheaf object ({self.functor()})"


class Sheaves(OwnedCategoryBase):
    r"""The full subcategory ``Sh(C,D)`` of presheaves satisfying descent."""

    @staticmethod
    @cached_function(
        key=lambda cls, coverage, value_category: (
            cls,
            id(coverage),
            id(value_category),
        )
    )
    def __classcall__(cls, coverage: Coverage, value_category: Category):
        if isinstance(cls, DynamicMetaclass):
            return cls.__base__(coverage, value_category)
        return typecall(cls, coverage, value_category)

    def __init__(self, coverage: Coverage, value_category: Category) -> None:
        self._coverage = coverage
        self._value_category = value_category
        self._objects = {}
        OwnedCategoryBase.__init__(self)

    def coverage(self) -> Coverage:
        return self._coverage

    def site_category(self) -> Category:
        return self.coverage().site_category()

    def value_category(self) -> Category:
        return self._value_category

    def presheaf_category(self) -> Category:
        return self.site_category().presheaves(self.value_category())

    def super_categories(self):
        return [self.presheaf_category()]

    def object(self, presheaf, descent_data: DescentData) -> SheafObject:
        functor = _presheaf_functor(presheaf)
        if functor.domain() != self.site_category().opposite():
            raise ValueError("the presheaf has the wrong site for this sheaf category")
        if functor.codomain() != self.value_category():
            raise ValueError("the presheaf has the wrong value category")
        if descent_data.coverage() is not self.coverage():
            raise ValueError("the descent datum belongs to a different coverage")
        if descent_data.presheaf() is not functor:
            raise ValueError("the descent datum belongs to a different presheaf")
        key = (id(functor), id(descent_data))
        cached = self._objects.get(key)
        if cached is not None:
            return cached
        result = SheafObject(self, functor, descent_data)
        self._objects[key] = result
        return result

    __call__ = object

    def __contains__(self, candidate) -> bool:
        try:
            return candidate.category().is_subcategory(self)
        except (AttributeError, TypeError, ValueError):
            return False

    def Mor(self, domain: Parent, codomain: Parent):
        if domain not in self or codomain not in self:
            raise TypeError("a sheaf Hom requires two sheaves for this coverage")
        return self.presheaf_category().Mor(domain, codomain)

    def identity(self, obj: Parent):
        return self.Mor(obj, obj).identity()

    def _repr_(self) -> str:
        return f"Sh({self.site_category()}, {self.value_category()}; {self.coverage()})"


__all__ = [
    "Coverage",
    "CoveringFamilies",
    "CoveringFamily",
    "CoveringOverlap",
    "DescentData",
    "DescentDataOnCover",
    "DescentEqualizer",
    "DescentEqualizerComparison",
    "SheafObject",
    "Sheaves",
    "TrivialCoveringFamilies",
    "trivial_coverage",
]
