"""Owned ringed-space structure used by the scheme hierarchy."""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.sets.set_categories import Sets


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


class StructureSheaf(SageObject):
    r"""The represented structure sheaf ``O_X`` of a ringed space ``X``."""

    def __init__(self, ringed_space) -> None:
        self._ringed_space = ringed_space
        self._restriction_maps = {}

    def ringed_space(self):
        return self._ringed_space

    scheme = ringed_space

    def global_sections(self):
        r"""Return ``Gamma(X,O_X)`` in the exact cases represented live."""
        operation = getattr(self.ringed_space(), "_structure_sheaf_global_sections", None)
        if operation is None:
            raise NotImplementedError(
                f"global sections of the structure sheaf of {self.ringed_space()} are not represented"
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
        if operation is None:
            raise NotImplementedError(
                "distinguished-open structure-sheaf sections are not represented for this ringed space"
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
            from dzack_research.preamble.categories.rings.ring_foundation import (
                ring_homset,
            )

            return remember(ring_homset(source_sections, source_sections).identity())
        if not _is_distinguished_open_of(target_open, ambient):
            raise ValueError("the restriction target is not a represented distinguished open of this affine scheme")
        target_sections = self.sections_on_distinguished_open(target_open)

        if source_open is ambient:
            restriction = target_open.inclusion().coordinate_algebra_morphism()
            if restriction.domain() is not source_sections or restriction.codomain() is not target_sections:
                raise ArithmeticError("the distinguished-open inclusion has the wrong represented pullback")
            return remember(restriction)
        if source_open is target_open:
            from dzack_research.preamble.categories.rings.ring_foundation import (
                ring_homset,
            )

            return remember(ring_homset(source_sections, source_sections).identity())
        return remember(_localization_restriction_map(source_sections, target_sections))

    def associated_module_sheaf(self, module):
        r"""Return the represented affine sheaf ``M~`` on the distinguished-open basis."""

        return AffineModuleSheaf(self.ringed_space(), module)

    def stalk(self, point):
        r"""Return ``O_{X,p}`` for a represented affine prime point."""
        operation = getattr(self.ringed_space(), "_structure_sheaf_stalk", None)
        if operation is None:
            raise NotImplementedError(
                "structure-sheaf stalks are not represented for this ringed space"
            )
        return operation(point)

    def _repr_(self) -> str:
        return f"Structure sheaf O_{{{self.scheme()}}}"


def _is_distinguished_open_of(open_subscheme, ambient) -> bool:
    return getattr(open_subscheme, "_preamble_distinguished_open_ambient", None) is ambient


def _localization_restriction_map(source, target):
    r"""Return ``S^{-1}A -> T^{-1}A`` when the target inverts every element of ``S``."""

    from dzack_research.preamble.categories.rings.ring_foundation import (
        LocalizationRings,
        ring_homset,
        ring_morphism,
    )

    if source is target:
        return ring_homset(source, source).identity()
    if source not in LocalizationRings() or target not in LocalizationRings():
        raise TypeError("principal-open restriction between proper opens requires represented localizations")
    if source.localization_source() is not target.localization_source():
        raise ValueError("principal-open restriction requires localizations of one affine coordinate ring")

    target_unit = target.localization_map()
    try:
        generators = tuple(source.localization_submonoid().monoid_generators())
    except NotImplementedError as error:
        raise NotImplementedError(
            "principal-open restriction currently requires a chosen finite denominator family"
        ) from error
    if any(not target_unit(generator).is_unit() for generator in generators):
        raise ValueError("the target distinguished open is not contained in the source distinguished open")

    def restrict(element):
        element = source(element)
        numerator = target_unit(element.numerator())
        denominator = target_unit(element.denominator())
        return numerator * denominator.inverse_of_unit()

    return ring_morphism(source, target, restrict)


class DistinguishedAffineCover(SageObject):
    r"""A finite affine cover ``X = union_i D(f_i)`` on a represented affine scheme."""

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
        self._intersections = {
            (index,): open_subscheme
            for index, open_subscheme in enumerate(self._opens)
        }
        self._restricted_modules = {}

    def ambient_scheme(self):
        return self._scheme

    def defining_elements(self):
        return self._elements

    def opens(self):
        return self._opens

    def open(self, index):
        return self.opens()[int(index)]

    def intersection_indices(self, *indices):
        if len(indices) == 1 and isinstance(indices[0], (tuple, list)):
            indices = tuple(indices[0])
        normalized = tuple(sorted({int(index) for index in indices}))
        if not normalized:
            raise ValueError("an affine-cover intersection requires at least one chart")
        if normalized[0] < 0 or normalized[-1] >= len(self.opens()):
            raise IndexError("affine-cover chart index is out of range")
        return normalized

    def intersection(self, *indices):
        r"""Return ``D(prod_i f_i)``, the represented intersection of selected charts."""

        key = self.intersection_indices(*indices)
        selected = self._intersections.get(key)
        if selected is None:
            algebra = self.ambient_scheme().coordinate_algebra()
            element = algebra.one()
            for index in key:
                element *= self.defining_elements()[index]
            selected = self.ambient_scheme().distinguished_open(element)
            self._intersections[key] = selected
        return selected

    def overlap(self, left_index, right_index):
        return self.intersection(left_index, right_index)

    def structure_sheaf_restriction(self, chart_index, other_index):
        overlap = self.overlap(chart_index, other_index)
        return self.ambient_scheme().structure_sheaf().restriction_map(
            self.open(chart_index),
            overlap,
        )

    def restrict_module(self, module, chart_index, *intersection_indices):
        r"""Return ``M_i|_{U_I}`` by scalar extension along ``O(U_i) -> O(U_I)``."""

        chart_index = int(chart_index)
        chart = self.open(chart_index)
        if module.base_ring() is not chart.coordinate_algebra():
            raise ValueError("a local module must be defined over the selected affine chart")
        indices = self.intersection_indices(chart_index, *intersection_indices)
        target = self.intersection(indices)
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

    def glue_modules(self, local_modules, transitions):
        r"""Return the descent datum and glued module sheaf on this affine cover."""

        from dzack_research.preamble.categories.schemes.gluing import ModuleGluingDatum

        return ModuleGluingDatum(self, local_modules, transitions)

    def glue_invertible_module(self, transition_units):
        r"""Return the rank-one locally free sheaf glued by a 1-cocycle of units."""

        from dzack_research.preamble.categories.schemes.gluing import (
            glue_invertible_module,
        )

        return glue_invertible_module(self, transition_units)

    def common_refinement(self, other):
        r"""The refinement ``{D(f_i g_j)}`` of this cover and ``other``, with its comparison maps."""

        assert other.ambient_scheme() is self.ambient_scheme(), "covers of one scheme are refined together"
        return CoverRefinement(self, other)

    def _repr_(self):
        return f"Distinguished affine cover of {self.ambient_scheme()} by {len(self.opens())} opens"


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
        first = first_cover.defining_elements()
        second = second_cover.defining_elements()
        self._index_pairs = tuple(
            (left, right) for left in range(len(first)) for right in range(len(second))
        )
        self._fine_cover = DistinguishedAffineCover(
            first_cover.ambient_scheme(),
            tuple(first[left] * second[right] for left, right in self._index_pairs),
        )

    def ambient_scheme(self):
        return self._fine_cover.ambient_scheme()

    def coarse_cover(self, which):
        return self._coarse_covers[int(which)]

    def fine_cover(self):
        return self._fine_cover

    def index_map(self, which, fine_index):
        r"""``k |-> i(k)``: the coarse chart of cover ``which`` containing fine chart ``k``."""
        return self._index_pairs[int(fine_index)][int(which)]

    def inclusion(self, which, fine_index):
        r"""The open immersion ``V_k -> U_{i(k)}`` into the chosen coarse cover."""
        coarse_open = self.coarse_cover(which).open(self.index_map(which, fine_index))
        return self.fine_cover().open(fine_index).inclusion_into(coarse_open)

    def _repr_(self):
        return f"Common refinement of {self.coarse_cover(0)} and {self.coarse_cover(1)}"


class AffineModuleSheaf(SageObject):
    r"""The quasi-coherent sheaf ``M~`` on the represented distinguished-open basis."""

    def __init__(self, scheme, module) -> None:
        algebra = scheme.coordinate_algebra()
        if module.base_ring() is not algebra:
            raise ValueError("an affine module sheaf requires a module over the scheme coordinate ring")
        self._scheme = scheme
        self._module = module
        self._local_sections = {}

    def ringed_space(self):
        return self._scheme

    scheme = ringed_space

    def module(self):
        return self._module

    def global_sections(self):
        return self.module()

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

        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_homset,
        )
        from dzack_research.preamble.categories.modules.pure.modules import (
            restrict_scalars,
        )

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
            return module_homset(source_sections, source_sections).identity()
        target_sections = self.sections_on_distinguished_open(target_open)

        if source_open is ambient:
            localization = target_sections.localization_functor()
            if localization.ring_map() is not structure_restriction:
                raise ArithmeticError("module and function restriction selected different localization maps")
            return localization.unit(self.module(), localized=target_sections)
        if source_open is target_open:
            return module_homset(source_sections, source_sections).identity()

        restricted_target = restrict_scalars(target_sections, structure_restriction)
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

        return module_homset(source_sections, restricted_target).elementwise(
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
    category is therefore abelian and monoidal exactly because ``Modules(A)``
    is, and every operation below is the module operation read through that
    equivalence rather than a second definition of the same thing.  For the
    same reason a morphism of quasi-coherent sheaves on an affine scheme is a
    morphism of the two modules, so no separate arrow type is introduced.

    On a scheme that is not affine no object of this category is represented:
    a quasi-coherent sheaf there is gluing data, which
    :meth:`DistinguishedAffineCover.glue_modules` assembles from modules on
    the charts and transition isomorphisms on the overlaps.
    """

    def scheme(self):
        return self.base()

    def _repr_object_names(self):
        return f"quasi-coherent sheaves on {self.scheme()}"

    def super_categories(self):
        return [Sets()]

    def __contains__(self, candidate) -> bool:
        # Deciding about an arbitrary argument is this method's whole job, and
        # the represented sheaves are not parents carrying a placement, so the
        # question is asked of the space each one names.
        ringed_space = getattr(candidate, "ringed_space", None)
        return ringed_space is not None and ringed_space() is self.scheme()

    def module_category(self):
        r"""``Modules(A)``: the category this one is equivalent to, for affine ``X``."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules
        from dzack_research.preamble.categories.schemes.schemes import AffineSchemes

        scheme = self.scheme()
        assert scheme in AffineSchemes(scheme.scheme_base_ring()), (
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
        from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
            module_homset,
        )

        return module_homset(self.global_sections(source), self.global_sections(target))

    def tensor_product(self, factors):
        r"""``(M tensor_A N)~``: the equivalence carries the monoidal structure."""
        modules = tuple(self.global_sections(factor) for factor in factors)
        return self.associated_sheaf(self.module_category().tensor_product(modules))

    def kernel(self, sheaf_morphism):
        r"""``(ker f)~``, the kernel of the module morphism underlying ``f``.

        Taking ``~`` is exact, so the kernel of the sheaf morphism is the
        sheaf of the kernel; the subobject the module kernel returns is a
        module over the same algebra and is the object here.
        """
        return self.associated_sheaf(sheaf_morphism.kernel())

    def cokernel(self, sheaf_morphism):
        r"""``(coker f)~``, carried by the same exactness."""
        return self.associated_sheaf(sheaf_morphism.cokernel())

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


class RingedSpaces(CategoryPacketMethods, Category):
    r"""Ringed spaces ``(X,O_X)``."""

    @classmethod
    def _repr_object_names(cls):
        return "ringed spaces"

    def super_categories(self):
        return [Sets()]

    def __contains__(self, candidate) -> bool:
        return hasattr(candidate, "_preamble_scheme_base_ring")

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


class LocallyRingedSpaces(CategoryPacketMethods, Category):
    r"""Ringed spaces whose stalks are local rings."""

    @classmethod
    def _repr_object_names(cls):
        return "locally ringed spaces"

    def super_categories(self):
        return [RingedSpaces()]

    def __contains__(self, candidate) -> bool:
        return candidate in RingedSpaces()

    class ParentMethods:
        def stalk(self, point):
            return self.structure_sheaf().stalk(point)


__all__ = [
    "AffineModuleSheaf",
    "CoverRefinement",
    "DistinguishedAffineCover",
    "LocallyRingedSpaces",
    "QuasiCoherentSheaves",
    "RingedSpaces",
    "SchemeUnderlyingSpace",
    "StructureSheaf",
]
