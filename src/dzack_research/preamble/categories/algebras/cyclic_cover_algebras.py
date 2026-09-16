r"""Cyclic-cover algebras from invertible sheaves and branch sections."""

from __future__ import annotations

from typing import TYPE_CHECKING

from sage.misc.cachefunc import cached_method
from sage.rings.integer import Integer
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.divisors.invertible_sheaves import (
    FiniteAtlasInvertibleSheaf,
    InvertibleSheaf,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)

if TYPE_CHECKING:
    from sage.structure.element import Element
    from sage.structure.parent import Parent

    from dzack_research.preamble.categories.abstract_categories.hom_categories import (
        CategoricalIsomorphism,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        ModuleMorphism,
    )
    from dzack_research.preamble.categories.schemes.gluing import (
        AlgebraGluingDatum,
        CompatibleLocalAlgebraSections,
        CompatibleLocalSectionElement,
        GluedAlgebraSheaf,
        ModuleGluingDatum,
    )
    from dzack_research.preamble.categories.schemes.ringed_spaces import (
        DistinguishedAffineCover,
    )


CYCLIC_COVER_VARIABLE = "z"


def _cyclic_cover_presentation(
    algebra: Parent,
    branch_coefficient: Element,
    degree: Integer,
) -> Parent:
    r"""Return ``R[z]/(z^n - f)``, the cover algebra of a trivialized chart.

    Where ``L`` is trivialized by ``e``, the branch section reads ``s = f e^n``
    and the summand ``L^{-i}`` is the free rank-one module ``R z^i``.  The
    multiplication ``L^{-i} ox L^{-j} -> L^{-(i+j)}`` is the identity when
    ``i + j < n`` and is multiplication by ``f`` when ``i + j >= n``, which is
    exactly the monic one-variable quotient returned here: its multiplication,
    its free rank-``n`` underlying module on ``1, z, ..., z^{n-1}``, its local
    equation ``z^n - f`` and its scalar changes are one construction.

    Both consumers call this one function.  The descent construction of a
    cover algebra for a nontrivial ``L`` builds it on every chart; the
    globally trivialized cyclic cover of an affine scheme builds it once.
    """

    presentation = algebra.polynomial_ring(CYCLIC_COVER_VARIABLE)
    variable = presentation.algebra_generator(CYCLIC_COVER_VARIABLE)
    return (presentation).quotient_by_relations((variable ** Integer(degree) - presentation(branch_coefficient),),
    )


def _rank_one_coefficient(module: Parent, element: Element) -> Element:
    labels = module.module_generating_set()
    if not labels.cardinality().is_finite() or int(labels.cardinality()) != 1:
        raise TypeError("a cyclic-cover branch trivialization requires rank-one local modules")
    label = next(iter(labels))
    coefficients = module.framing_coefficients(module(element))
    return coefficients[label] if label in coefficients else module.base_ring().zero()


class CyclicCoverAlgebra(SageObject):
    r"""The algebra ``oplus_{i=0}^{n-1} L^{-i}`` attached to ``(L,s,n)``.

    On a chart trivializing ``L`` by ``e_i``, write
    ``s = f_i e_i^n``.  The local algebra is the selected finite-free quotient
    ``R_i[z_i]/(z_i^n-f_i)``.  If ``e_i = u_ij e_j`` on an overlap, the algebra
    transition is ``z_i -> u_ij^{-1} z_j``.  The supplied branch section is
    required to carry exactly the ``u_ij^n`` transition data of ``L^n``.
    """

    def __init__(
        self,
        line_bundle: InvertibleSheaf,
        branch_section: CompatibleLocalSectionElement,
        degree: Integer,
    ) -> None:
        if not isinstance(line_bundle, InvertibleSheaf):
            raise TypeError("cyclic-cover data requires an invertible sheaf")
        degree = Integer(degree)
        if degree < 2:
            raise ValueError("a cyclic cover has degree at least two")

        try:
            branch_parent = branch_section.parent()
            branch_datum = branch_parent.gluing_datum()
        except AttributeError as error:
            raise TypeError(
                "the branch section must be a represented compatible section of L^n"
            ) from error

        if isinstance(line_bundle, FiniteAtlasInvertibleSheaf):
            try:
                branch_power = branch_datum.line_bundle()
            except AttributeError as error:
                raise ValueError(
                    "a finite-atlas cyclic branch must come from a represented line-bundle power"
                ) from error
            if not isinstance(branch_power, FiniteAtlasInvertibleSheaf):
                raise ValueError(
                    "a finite-atlas cyclic branch must come from a represented line-bundle power"
                )
            if branch_power.gluing_datum() is not line_bundle.gluing_datum():
                raise ValueError("the branch section and line bundle require one affine atlas")
            charts = line_bundle.gluing_datum().chart_index_set()
            for left, right in line_bundle.gluing_datum().transition_index_set():
                expected = line_bundle.transition_unit(left, right) ** degree
                actual = branch_power.transition_unit(left, right)
                if actual != expected:
                    raise ValueError(
                        "the branch section is not represented as a section of the stated L^n"
                    )
        else:
            if branch_datum.cover() is not line_bundle.cover():
                raise ValueError("the branch section and line bundle require one affine cover")
            branch_power = InvertibleSheaf(branch_datum)
            charts = line_bundle.cover().atlas()
            for left in charts:
                for right in charts:
                    if left >= right:
                        continue
                    expected = line_bundle.transition_unit(left, right) ** degree
                    actual = branch_power.transition_unit(left, right)
                    if actual != expected:
                        raise ValueError(
                            "the branch section is not represented as a section of the stated L^n"
                        )

        self._line_bundle = line_bundle
        self._branch_power = branch_power
        self._branch_section = branch_parent(branch_section)
        self._degree = degree
        self._chart_index_set = charts
        self._local_branch_coefficients = indexed_family(
            charts,
            lambda index: _rank_one_coefficient(
                branch_power.local_module(index),
                self._branch_section.component(index),
            ),
            name="Cyclic-cover local branch coefficients",
        )
        self._local_algebra_family = indexed_family(
            charts,
            self._build_local_algebra,
            name="Cyclic cover chart algebras",
        )
        self._gluing_datum = self._build_algebra_gluing_datum()

    def line_bundle(self) -> InvertibleSheaf:
        return self._line_bundle

    def branch_power(self) -> InvertibleSheaf:
        return self._branch_power

    def branch_section(self) -> CompatibleLocalSectionElement:
        return self._branch_section

    def degree(self) -> Integer:
        return self._degree

    def cover(self) -> DistinguishedAffineCover:
        return self.line_bundle().cover()

    def chart_index_set(self) -> Parent:
        r"""Return the exact finite index set labelling the cyclic-cover atlas."""

        return self._chart_index_set

    def scheme(self) -> Parent:
        return self.line_bundle().scheme()

    def _chart_scheme(self, index):
        cover = self.cover()
        if isinstance(self.line_bundle(), FiniteAtlasInvertibleSheaf):
            return cover.chart(index)
        return cover.open(index)

    def local_branch_coefficient(self, index: Integer) -> Element:
        return self._local_branch_coefficients[self.chart_index_set()(index)]

    def _build_local_algebra(self, index: Integer) -> Parent:
        algebra = self._chart_scheme(index).coordinate_algebra()
        return algebra.cyclic_cover_presentation(
            self.local_branch_coefficient(index),
            self.degree(),
        )

    def local_algebra(self, index: Integer) -> Parent:
        return self._local_algebra_family[self.chart_index_set()(index)]

    def local_algebras(self) -> IndexedFamily:
        r"""Return the chart algebras as the family they are, labelled by the atlas."""

        return self._local_algebra_family

    def local_underlying_module(self, index: Integer) -> Parent:
        r"""Return the same local algebra object, carrying its rank-``n`` module basis."""

        return self.local_algebra(index)

    def local_multiplication(self, index: Integer) -> ModuleMorphism:
        return self.local_algebra(index).multiplication_morphism()

    def local_presentation(self, index: Integer) -> tuple[Parent, IndexedFamily]:
        return self.local_algebra(index).presentation()

    def local_equation(self, index: Integer) -> Element:
        relations = self.local_algebra(index).relations()
        return relations.value(next(iter(relations.index_set())))

    def _transition(
        self,
        source_index: Integer,
        target_index: Integer,
    ) -> CategoricalIsomorphism:
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        source = self.cover().restrict_algebra(
            self.local_algebra(source_index),
            source_index,
            target_index,
        )
        target = self.cover().restrict_algebra(
            self.local_algebra(target_index),
            target_index,
            source_index,
        )
        unit = self.line_bundle().transition_unit(source_index, target_index)
        source_z = source.algebra_generator(CYCLIC_COVER_VARIABLE)
        target_z = target.algebra_generator(CYCLIC_COVER_VARIABLE)
        algebras = Algebras(source.algebra_base_ring()).Associative().Unital()
        forward = algebras.Mor(source, target)(
            {
                CYCLIC_COVER_VARIABLE: target(unit.inverse_of_unit()) * target_z,
            }
        )
        inverse = algebras.Mor(target, source)(
            {
                CYCLIC_COVER_VARIABLE: source(unit) * source_z,
            }
        )
        return algebras.Core().Mor(source, target)(forward, inverse)

    def _build_algebra_gluing_datum(self) -> AlgebraGluingDatum:
        charts = self.chart_index_set()
        if isinstance(self.line_bundle(), FiniteAtlasInvertibleSheaf):
            from dzack_research.preamble.categories.schemes.gluing import (
                FiniteAtlasAlgebraGluingDatum,
            )

            transitions = {}
            for left, right in self.cover().transition_index_set():
                left_unit = self.line_bundle().transition_unit(left, right)
                right_unit = self.line_bundle().transition_unit(right, left)

                def forward(label, _domain, codomain, unit=left_unit):
                    return codomain(unit.inverse_of_unit()) * codomain.algebra_generator(label)

                def inverse(label, _domain, codomain, unit=right_unit):
                    return codomain(unit.inverse_of_unit()) * codomain.algebra_generator(label)

                transitions[left, right] = (forward, inverse)
            return FiniteAtlasAlgebraGluingDatum(
                self.cover(),
                self.local_algebras(),
                transitions,
            )

        transitions = {
            (int(left), int(right)): self._transition(left, right)
            for left in charts
            for right in charts
            if left < right
        }
        return self.cover().glue_algebras(
            tuple(self.local_algebra(index) for index in charts),
            transitions,
        )

    def gluing_datum(self) -> AlgebraGluingDatum:
        return self._gluing_datum

    def sheaf(self) -> GluedAlgebraSheaf:
        return self.gluing_datum().sheaf()

    def underlying_module_datum(self) -> ModuleGluingDatum:
        return self.gluing_datum().underlying_module_datum()

    def global_sections(self) -> CompatibleLocalAlgebraSections:
        return self.gluing_datum().compatible_sections()

    sections = global_sections

    @cached_method
    def relative_spectrum(self):
        r"""Return the finite cover as the relative spectrum of this descended algebra."""
        from dzack_research.preamble.categories.schemes.cyclic_covers import (
            _relative_cyclic_cover,
        )

        return _relative_cyclic_cover(self)

    def local_deck_group_scheme_action(self, chart_index):
        r"""Return the canonical ``mu_n`` action on one affine cover chart."""
        from dzack_research.preamble.categories.schemes.cyclic_covers import (
            _local_relative_cyclic_deck_action,
        )

        return _local_relative_cyclic_deck_action(self, chart_index)

    def local_deck_transformation(self, chart_index, root_of_unity):
        from dzack_research.preamble.categories.schemes.cyclic_covers import (
            _relative_cyclic_local_deck_transformation,
        )

        return _relative_cyclic_local_deck_transformation(
            self, chart_index, root_of_unity
        )

    def deck_transformation(self, root_of_unity):
        r"""Return the global deck automorphism ``z_i -> root*z_i`` when ``root^n=1``."""
        from dzack_research.preamble.categories.schemes.cyclic_covers import (
            _relative_cyclic_deck_transformation,
        )

        return _relative_cyclic_deck_transformation(self, root_of_unity)

    def base_change(self, ring_map):
        from dzack_research.preamble.categories.schemes.cyclic_covers import (
            _cyclic_cover_base_change,
        )

        return _cyclic_cover_base_change(self, ring_map)

    def lift_linearized_group_element(self, linearization, group_element):
        r"""Lift ``group_element`` through the selected line-bundle linearization."""
        from dzack_research.preamble.categories.schemes.cyclic_covers import (
            _relative_cyclic_cover_lift,
        )

        return _relative_cyclic_cover_lift(self, linearization, group_element)

    def constant_deck_transformation(self):
        r"""Return the deck generator when the scalar base contains a primitive ``n``-th root."""
        from dzack_research.preamble.categories.schemes.cyclic_covers import (
            _primitive_root_of_unity,
        )

        root = _primitive_root_of_unity(
            self.scheme().scheme_base_ring(),
            self.degree(),
        )
        return self.deck_transformation(root)

    def restricted_algebra(
        self,
        chart_index: Integer,
        *intersection_indices: Integer,
    ) -> Parent:
        return self.gluing_datum().restricted_algebra(
            chart_index,
            *intersection_indices,
        )

    def transition(
        self,
        source_index: Integer,
        target_index: Integer,
    ) -> CategoricalIsomorphism:
        return self.gluing_datum().transition(source_index, target_index)

    def _repr_(self) -> str:
        return (
            f"Degree-{self.degree()} cyclic-cover algebra on {self.scheme()} "
            f"from {self.line_bundle()}"
        )


__all__ = [
    "CYCLIC_COVER_VARIABLE",
    "CyclicCoverAlgebra",
]
