r"""Cochain complexes of owned modules and their cohomology."""

from sage.categories.morphism import Morphism
from sage.misc.cachefunc import cached_function
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
    _presented_module_from_morphism,
)
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    _initialize_module_hom_parent,
)
from dzack_research.preamble.categories.modules.pure.modules import (
    FinitelyPresentedModules,
    LinearEndCategoryConstruction,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import (
    IndexedFamily,
    indexed_family,
)


class CochainComplexes(OwnedCategoryOverBaseRing):
    def an_object(self):
        r"""The free module of rank one in degree zero, with zero differential."""
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        ring = self.base_ring()
        free = Modules(ring).an_object()
        return self({0: free}, {})

    def _call_(
        self,
        pieces,
        differentials,
        name=None,
        *,
        extra_categories=(),
        extra_construction_data=None,
    ):
        r"""Construct a finite-support cochain complex from its defining data.

        A dictionary of pieces is a declaration that every unlisted integer
        degree is the zero module.  The differentials are the selected maps
        ``C^p -> C^(p+1)``; omitted maps between represented zero pieces are
        zero.  This category constructor is the authoritative finite-support
        construction and the public construction route.
        """
        if not isinstance(pieces, dict) or not isinstance(differentials, dict):
            raise TypeError(
                "the ordinary cochain-complex constructor requires dictionaries; "
                "use CochainComplexes(R).from_family for a lazy integer family"
            )
        return CochainComplexObject(
            self.base_ring(),
            pieces,
            differentials,
            name=name,
            extra_categories=extra_categories,
            extra_construction_data=extra_construction_data,
        )

    def from_family(self, pieces, differentials, name=None):
        r"""Construct a lazy integer-graded complex from two indexed families.

        Unlike :meth:`_call_`, this construction does not assert that degrees
        absent from a finite dictionary are zero: the supplied families define
        the piece and outgoing differential in every owned integer degree.
        """
        if not isinstance(pieces, IndexedFamily) or not isinstance(
            differentials, IndexedFamily
        ):
            raise TypeError(
                "a family cochain complex requires indexed families of pieces and differentials"
            )
        if pieces.index_set() is not differentials.index_set():
            raise ValueError(
                "the piece and differential families require one degree index set"
            )
        return CochainComplexObject(
            self.base_ring(),
            pieces,
            differentials,
            name=name,
            degree_index_set=pieces.index_set(),
        )

    @classmethod
    def _repr_object_names(cls):
        return "cochain complexes"

    def super_categories(self):

        return [GradedModules(self.base_ring())]

    _HomCategory = None

    def underlying_graded_module(self):
        r"""Return the forgetful functor from cochain complexes to graded modules."""
        from dzack_research.preamble.categories.functors.cochain_complexes import (
            _cochain_underlying_graded_module_functor,
        )

        return _cochain_underlying_graded_module_functor(self.base_ring())

    def cohomology(self, degree):
        r"""Return the degree-``degree`` cohomology functor on this category."""
        from dzack_research.preamble.categories.functors.cohomology import (
            _cohomology_functor,
        )

        return _cohomology_functor(self.base_ring(), degree)

    class ParentMethods:
        def differential(self):
            return self._preamble_differential

        def d(self, element):
            return self.differential()(element)

        def cycles(self, degree):
            r"""Return ``ker(d^degree)`` as a subobject of ``C^degree``."""
            return self.differential_component(degree).kernel()

        def boundaries(self, degree):
            r"""Return ``im(d^(degree-1))`` as a subobject of ``C^degree``."""
            return self.differential_component(int(degree) - 1).image()

        def cohomology(self, degree):
            return _cohomology(self, degree)


class CohomologyModules(OwnedCategoryOverBaseRing):
    r"""Cohomology modules retaining their represented cycle quotient."""

    def an_object(self):
        r"""The degree-zero cohomology of a one-term complex."""
        return CochainComplexes(self.base_ring()).an_object().cohomology(0)

    @classmethod
    def _repr_object_names(cls):
        return "cohomology modules"

    def super_categories(self):

        return [FinitelyPresentedModules(self.base_ring())]

    class ParentMethods:
        def __init__(
            self,
            cohomology_complex,
            cohomology_degree,
            cohomology_current_module,
            cohomology_cycles,
            cohomology_boundaries,
            cohomology_boundary_in_cycles,
            **rest,
        ) -> None:
            self._preamble_cohomology_complex = cohomology_complex
            self._preamble_cohomology_degree = cohomology_degree
            self._preamble_cohomology_current_module = cohomology_current_module
            self._preamble_cohomology_cycles = cohomology_cycles
            self._preamble_cohomology_boundaries = cohomology_boundaries
            self._preamble_cohomology_boundary_in_cycles = cohomology_boundary_in_cycles
            super().__init__(**rest)

        def cochain_complex(self):
            return self._preamble_cohomology_complex

        def cohomological_degree(self):
            return self._preamble_cohomology_degree

        degree = cohomological_degree

        def cycle_representative(self, cohomology_class):
            r"""Return the selected closed representative in ``C^p``."""

            if cohomology_class.parent() is not self:
                cohomology_class = self(cohomology_class)
            coefficients = self.framing_coefficients(cohomology_class)
            projection = self.cokernel_projection()
            cycles = projection.domain()
            representative = cycles.linear_combination(
                {
                    label: coefficients[label]
                    for label in cycles.module_generating_set()
                    if label in coefficients and coefficients[label]
                }
            )
            return cycles.inclusion()(representative)

        def class_of_cycle(self, cycle):
            r"""Return the cohomology class of a closed element of ``C^p``."""

            complex_ = self.cochain_complex()
            degree = self.cohomological_degree()
            current = self._preamble_cohomology_current_module
            if cycle.parent() is not current:
                cycle = current(cycle)
            outgoing = complex_.differential_component(degree)
            target = outgoing.codomain()
            if outgoing(cycle) != target.zero():
                raise ValueError("a cohomology class can only be formed from a cycle")

            cycles = self._preamble_cohomology_cycles
            cycle_in_cycles = cycles.inclusion().lift(cycle)
            return self.cokernel_projection()(cycle_in_cycles)


class CochainDifferential:
    r"""The degree-``+1`` differential of a represented cochain complex."""

    def __init__(self, complex_) -> None:
        self._complex = complex_

    def complex(self):
        return self._complex

    def degree_shift(self):
        return 1

    def component(self, degree):
        return self.complex().differential_component(degree)

    def __call__(self, element):
        complex_ = self.complex()
        element = complex_(element)
        components = {}
        for degree, component in element.homogeneous_components().items():
            image = self.component(degree)(component)
            target = complex_.graded_piece(degree + 1)
            if image != target.zero():
                components[degree + 1] = image
        return complex_.from_components(components)


class CochainComplexElement(GradedDirectSumElement):
    pass


class CochainComplexObject(GradedDirectSumModule):
    r"""A represented integer-graded cochain complex.

    A dictionary presentation has finite support and therefore declares every
    unlisted degree to be the zero module.  An indexed-family presentation is
    lazy over all integer degrees and does not identify an unrequested degree
    with zero.
    """

    Element = CochainComplexElement

    def __init__(
        self,
        base_ring,
        pieces,
        differentials,
        name=None,
        *,
        degree_index_set=None,
        extra_categories=(),
        extra_construction_data=None,
    ) -> None:
        integer_degrees = _own_ring(SageZZ)
        self._finite_support = isinstance(pieces, dict)
        if self._finite_support:
            self._selected_pieces = {
                int(degree): module for degree, module in pieces.items()
            }
            self._selected_differentials = {
                int(degree): morphism for degree, morphism in differentials.items()
            }
            self._degree_family = None
            self._differential_family = None
            degree_index_set = integer_degrees
        else:
            if not isinstance(pieces, IndexedFamily):
                raise TypeError(
                    "an infinite represented cochain complex requires an indexed family of pieces"
                )
            if not isinstance(differentials, IndexedFamily):
                raise TypeError(
                    "an infinite represented cochain complex requires an indexed family of differentials"
                )
            if pieces.index_set() is not differentials.index_set():
                raise ValueError(
                    "the piece and differential families require one degree index set"
                )
            if degree_index_set is None:
                degree_index_set = pieces.index_set()
            if degree_index_set is not pieces.index_set():
                raise ValueError("the selected degree set does not index the piece family")
            if degree_index_set is not integer_degrees:
                raise ValueError(
                    "a represented cochain complex is indexed by the owned integers"
                )
            self._selected_pieces = None
            self._selected_differentials = None
            self._degree_family = pieces
            self._differential_family = differentials
        zero_module = base_ring.free_module(finite_ordered_set(()))

        def piece(degree):
            if self._finite_support:
                return self._selected_pieces.get(int(degree), zero_module)
            return self._degree_family(degree)

        GradedDirectSumModule.__init__(
            self,
            base_ring,
            piece,
            name=name or "Cochain complex",
            degree_index_set=degree_index_set,
            extra_categories=(CochainComplexes(base_ring), *tuple(extra_categories)),
            extra_construction_data=extra_construction_data,
        )
        self._zero_module = zero_module
        self._preamble_differential = CochainDifferential(self)
        self._validate_differentials()

    def selected_degrees(self):
        if not self._finite_support:
            raise TypeError(
                "an infinite represented complex has no finite selected-degree list; use degree_index_set()"
            )
        return tuple(sorted(self._selected_pieces))

    def has_finite_support(self) -> bool:
        return self._finite_support

    def cohomological_degree_set(self):
        return self.degree_index_set()

    def degree_convention(self):
        return "cohomological"

    def _raw_differential_component(self, degree):
        degree = int(degree)
        source = self.graded_piece(degree)
        target = self.graded_piece(degree + 1)
        if self._finite_support:
            selected = self._selected_differentials.get(degree)
            if selected is None:
                return source.module_category().Mor(source, target)(
                    {label: target.zero() for label in source.module_generating_set()}
                )
            return selected
        return self._differential_family(self.degree_index_set()(degree))

    def differential_component(self, degree):
        degree = int(degree)
        source = self.graded_piece(degree)
        target = self.graded_piece(degree + 1)
        selected = self._raw_differential_component(degree)
        if selected.domain() is not source or selected.codomain() is not target:
            raise ValueError(
                f"the selected degree-{degree} differential has the wrong endpoints"
            )
        if not self._finite_support:
            following = self._raw_differential_component(degree + 1)
            following_source = self.graded_piece(degree + 1)
            following_target = self.graded_piece(degree + 2)
            if (
                following.domain() is not following_source
                or following.codomain() is not following_target
            ):
                raise ValueError(
                    f"the selected degree-{degree + 1} differential has the wrong endpoints"
                )
            labels = source.module_generating_set()
            if labels.cardinality().is_finite():
                for label in labels:
                    generator = source.module_generator(label)
                    if following(selected(generator)) != following.codomain().zero():
                        raise ValueError(f"d^2 is nonzero in degree {degree}")
        return selected

    def _validate_differentials(self) -> None:
        if not self._finite_support:
            return
        for degree in self.selected_degrees():
            first = self.differential_component(degree)
            second = self.differential_component(degree + 1)
            for label in first.domain().module_generating_set():
                generator = first.domain().module_generator(label)
                if second(first(generator)) != second.codomain().zero():
                    raise ValueError(f"d^2 is nonzero in degree {degree}")


class CochainMorphism(Morphism):
    r"""A degree-zero morphism commuting with the selected differentials."""

    def __init__(self, parent, components) -> None:
        Morphism.__init__(self, parent)
        self._components = components
        self._validate_components()

    def _raw_component(self, degree):
        degree = int(degree)
        return self._components(self.domain().degree_index_set()(degree))

    def component(self, degree):
        degree = int(degree)
        source = self.domain().graded_piece(degree)
        target = self.codomain().graded_piece(degree)
        selected = self._raw_component(degree)
        if selected.domain() is not source or selected.codomain() is not target:
            raise ValueError(f"the degree-{degree} component has the wrong endpoints")
        if not self.domain().has_finite_support() or not self.codomain().has_finite_support():
            following = self._raw_component(degree + 1)
            following_source = self.domain().graded_piece(degree + 1)
            following_target = self.codomain().graded_piece(degree + 1)
            if (
                following.domain() is not following_source
                or following.codomain() is not following_target
            ):
                raise ValueError(
                    f"the degree-{degree + 1} component has the wrong endpoints"
                )
            left = self.codomain().differential_component(degree)
            right = self.domain().differential_component(degree)
            labels = source.module_generating_set()
            if labels.cardinality().is_finite():
                for label in labels:
                    generator = source.module_generator(label)
                    if left(selected(generator)) != following(right(generator)):
                        raise ValueError(
                            f"the cochain square does not commute in degree {degree}"
                        )
        return selected

    def _validate_components(self) -> None:
        if not self.domain().has_finite_support() or not self.codomain().has_finite_support():
            return
        degrees = set(self.domain().selected_degrees()) | set(self.codomain().selected_degrees())
        for degree in degrees:
            left = self.codomain().differential_component(degree)
            component = self.component(degree)
            right_component = self.component(degree + 1)
            right = self.domain().differential_component(degree)
            for label in component.domain().module_generating_set():
                generator = component.domain().module_generator(label)
                if left(component(generator)) != right_component(right(generator)):
                    raise ValueError(f"the cochain square does not commute in degree {degree}")

    def _call_(self, element):
        element = self.domain()(element)
        return self.codomain().from_components(
            {
                degree: self.component(degree)(component)
                for degree, component in element.homogeneous_components().items()
            }
        )

    def __call__(self, element):
        return self._call_(element)

    def __add__(self, other):
        other = self.parent()(other)
        return self.parent().elementwise(lambda element: self(element) + other(element))

    def __neg__(self):
        return self.parent().elementwise(lambda element: -self(element))

    def __sub__(self, other):
        return self + (-self.parent()(other))

    def __rmul__(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def __mul__(self, other):
        if not isinstance(other, CochainMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        return CochainComplexes(self.domain().base_ring()).Mor(
            other.domain(), self.codomain()
        )(
            indexed_family(
                other.domain().degree_index_set(),
                lambda degree: self.component(degree) * other.component(degree),
                name="Composite cochain-morphism components",
            )
        )


class CochainHomset(CategoricalHomset):
    Element = CochainMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("cochain morphisms require one common base ring")
        if domain.degree_index_set() is not codomain.degree_index_set():
            raise ValueError("cochain morphisms require one common degree index set")
        _initialize_module_hom_parent(self, hom_family, domain, codomain)

    def _degrees(self):
        if not self.domain().has_finite_support() or not self.codomain().has_finite_support():
            raise TypeError(
                "an infinite represented cochain Hom has no finite degree list"
            )
        return tuple(
            sorted(
                set(self.domain().selected_degrees())
                | set(self.codomain().selected_degrees())
            )
        )

    def _element_constructor_(self, components):
        if isinstance(components, CochainMorphism):
            if components.domain() is not self.domain() or components.codomain() is not self.codomain():
                raise ValueError("the cochain morphism has the wrong endpoints")
            if components.parent() is self:
                return components
            components = indexed_family(
                self.domain().degree_index_set(),
                components.component,
                name="Reparented cochain-morphism components",
            )
        elif isinstance(components, Morphism):
            if components.domain() is not self.domain() or components.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong cochain endpoints")
            component = getattr(components, "component", None)
            if component is not None:
                components = indexed_family(
                    self.domain().degree_index_set(),
                    component,
                    name="Cochain-morphism components",
                )
            else:
                return self.elementwise(lambda element: components(element))
        elif isinstance(components, dict):
            selected = {int(degree): morphism for degree, morphism in components.items()}

            def component_at(degree):
                degree = int(degree)
                source = self.domain().graded_piece(degree)
                target = self.codomain().graded_piece(degree)
                chosen = selected.get(degree)
                if chosen is not None:
                    return chosen
                return source.module_category().Mor(source, target)(
                    {label: target.zero() for label in source.module_generating_set()}
                )

            components = indexed_family(
                self.domain().degree_index_set(),
                component_at,
                name="Finite-support cochain-morphism components",
            )
        elif callable(components):
            components = indexed_family(
                self.domain().degree_index_set(),
                components,
                name="Declared cochain-morphism components",
            )
        if not isinstance(components, IndexedFamily):
            raise TypeError("a cochain morphism is specified by a degree-indexed family")
        if components.index_set() is not self.domain().degree_index_set():
            raise ValueError("the cochain-morphism family has the wrong degree index set")
        return self.element_class(self, components)

    def elementwise(self, function):
        if not callable(function):
            raise TypeError("an elementwise cochain map must be callable")
        def component_at(degree):
            degree = int(degree)
            source = self.domain().graded_piece(degree)
            target = self.codomain().graded_piece(degree)

            def on_piece(element):
                total = self.domain().from_component(degree, element)
                image = self.codomain()(function(total))
                return image.homogeneous_component(degree)

            return source.module_category().Mor(source, target).elementwise(on_piece)

        return self.element_class(
            self,
            indexed_family(
                self.domain().degree_index_set(),
                component_at,
                name="Elementwise cochain-morphism components",
            ),
        )

    def zero(self):
        return self.elementwise(lambda _element: self.codomain().zero())

    def linear_combination(self, coefficients):
        result = self.zero()
        for morphism, coefficient in coefficients.items():
            if coefficient:
                result += self.scalar_multiple(coefficient, morphism)
        return result

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a cochain endomorphism homset")
        domain = self.domain()

        def identity_component(degree):
            piece = domain.graded_piece(degree)
            return piece.module_category().Mor(piece, piece).identity()

        return self(
            indexed_family(
                domain.degree_index_set(),
                identity_component,
                name="Identity cochain-morphism components",
            )
        )


class CochainHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return CochainHomset


# The declaration is placed after the concrete fixed-Hom class to avoid a
# module-level forward-reference helper or a second registration mechanism.
CochainComplexes._HomCategory = CochainHomCategoryConstruction
CochainComplexes._EndCategory = LinearEndCategoryConstruction


@cached_function(key=lambda complex_, degree: (id(complex_), int(degree)))
def _cohomology(complex_, degree):
    r"""Return ``H^degree = ker(d^degree) / im(d^(degree-1))``."""
    degree = int(degree)
    ring = complex_.base_ring()
    cycles = complex_.cycles(degree)
    boundaries = complex_.boundaries(degree)
    boundary_in_cycles = boundaries.inclusion().factor_through(cycles.inclusion())
    result = _presented_module_from_morphism(
        boundary_in_cycles,
        _cokernel_morphism=boundary_in_cycles,
        _extra_categories=(CohomologyModules(ring),),
        _extra_construction_data={
            "cohomology_complex": complex_,
            "cohomology_degree": degree,
            "cohomology_current_module": cycles.inclusion().codomain(),
            "cohomology_cycles": cycles,
            "cohomology_boundaries": boundaries,
            "cohomology_boundary_in_cycles": boundary_in_cycles,
        },
    )
    return result


__all__ = [
    "CochainComplexElement",
    "CochainComplexObject",
    "CochainComplexes",
    "CochainDifferential",
    "CochainHomset",
    "CochainMorphism",
    "CohomologyModules",
]
