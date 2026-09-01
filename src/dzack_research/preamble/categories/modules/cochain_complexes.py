r"""Cochain complexes of owned modules and their cohomology."""

from sage.categories.morphism import Morphism
from sage.categories.sets_cat import Sets

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)

from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumElement,
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    _initialize_module_hom_parent,
    module_homset,
)
from dzack_research.preamble.categories.rings import (
    OwnedCategoryOverBaseRing,
    engine_ring,
)
from dzack_research.preamble.categories.sets import finite_ordered_set
from dzack_research.preamble.refine import refine


class CochainComplexes(OwnedCategoryOverBaseRing):
    @classmethod
    def _repr_object_names(cls):
        return "cochain complexes"

    def super_categories(self):
        from dzack_research.preamble.categories.modules.graded_modules import GradedModules

        return [GradedModules(self.base_ring())]

    _HomCategory = None

    class ParentMethods:
        def differential(self):
            return self._preamble_differential

        def d(self, element):
            return self.differential()(element)

        def cohomology(self, degree):
            return Cohomology(self, degree)


class CohomologyModules(OwnedCategoryOverBaseRing):
    r"""Cohomology modules retaining their represented cycle quotient."""

    @classmethod
    def _repr_object_names(cls):
        return "cohomology modules"

    def super_categories(self):
        from dzack_research.preamble.categories.modules import FinitelyPresentedModules

        return [FinitelyPresentedModules(self.base_ring())]

    class ParentMethods:
        def cochain_complex(self):
            return self._preamble_cohomology_complex

        def cohomological_degree(self):
            return self._preamble_cohomology_degree

        degree = cohomological_degree

        def cycle_representative(self, cohomology_class):
            r"""Return the selected closed representative in ``C^p``."""
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_coefficients,
            )

            if cohomology_class.parent() is not self:
                cohomology_class = self(cohomology_class)
            coefficients = module_coefficients(cohomology_class, self)
            current = self._preamble_cohomology_current_module
            current_labels = self._preamble_cohomology_current_labels
            closed_basis = self._preamble_cohomology_closed_basis
            coordinate_values = [current.base_ring().zero()] * len(current_labels)
            for closed_label, coefficient in coefficients.items():
                row = closed_basis[int(closed_label)]
                for position, entry in enumerate(row):
                    coordinate_values[position] += current.base_ring()(coefficient * entry)
            return current.linear_combination(
                {
                    label: coefficient
                    for label, coefficient in zip(
                        current_labels, coordinate_values, strict=True
                    )
                    if coefficient
                }
            )

        def class_of_cycle(self, cycle):
            r"""Return the cohomology class of a closed element of ``C^p``."""
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                module_coefficients,
            )

            complex_ = self.cochain_complex()
            degree = self.cohomological_degree()
            current = self._preamble_cohomology_current_module
            if cycle.parent() is not current:
                cycle = current(cycle)
            target = complex_.graded_piece(degree + 1)
            if complex_.differential_component(degree)(cycle) != target.zero():
                raise ValueError("a cohomology class can only be formed from a cycle")

            coefficients = module_coefficients(cycle, current)
            current_labels = self._preamble_cohomology_current_labels
            engine = engine_ring(self.base_ring())
            vector = self._preamble_cohomology_free_cover(
                tuple(
                    engine(coefficients[label])
                    if label in coefficients
                    else engine.zero()
                    for label in current_labels
                )
            )
            closed_coordinates = self._preamble_cohomology_closed_submodule.coordinate_vector(
                vector
            )
            labels = tuple(self.module_generating_set())
            return self.linear_combination(
                {
                    label: self.base_ring()(coefficient)
                    for label, coefficient in zip(
                        labels, tuple(closed_coordinates), strict=True
                    )
                    if coefficient
                }
            )


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
    r"""A nonnegative represented cochain complex with selected finite pieces."""

    Element = CochainComplexElement

    def __init__(self, base_ring, pieces, differentials, name=None) -> None:
        self._selected_pieces = {int(degree): module for degree, module in pieces.items()}
        self._selected_differentials = {
            int(degree): morphism for degree, morphism in differentials.items()
        }
        if any(degree < 0 for degree in self._selected_pieces):
            raise NotImplementedError(
                "the live finite-support carrier currently materializes nonnegative cochain complexes"
            )

        from dzack_research.preamble.categories.modules import BasedFreeModule

        zero_module = BasedFreeModule(base_ring, finite_ordered_set(()))

        def piece(degree):
            return self._selected_pieces.get(int(degree), zero_module)

        GradedDirectSumModule.__init__(
            self,
            base_ring,
            piece,
            name=name or "Cochain complex",
        )
        self._zero_module = zero_module
        self._preamble_differential = CochainDifferential(self)
        self._validate_differentials()
        refine(self, CochainComplexes(self.base_ring()))

    def selected_degrees(self):
        return tuple(sorted(self._selected_pieces))

    def differential_component(self, degree):
        degree = int(degree)
        if degree < 0:
            target = self.graded_piece(0)
            return module_homset(self._zero_module, target)({})
        selected = self._selected_differentials.get(degree)
        source = self.graded_piece(degree)
        target = self.graded_piece(degree + 1)
        if selected is not None:
            if selected.domain() is not source or selected.codomain() is not target:
                raise ValueError(
                    f"the selected degree-{degree} differential has the wrong endpoints"
                )
            return selected
        return module_homset(source, target)(
            {label: target.zero() for label in source.module_generating_set()}
        )

    def _validate_differentials(self) -> None:
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
        self._components = dict(components)
        self._validate_components()

    def component(self, degree):
        degree = int(degree)
        source = self.domain().graded_piece(degree)
        target = self.codomain().graded_piece(degree)
        selected = self._components.get(degree)
        if selected is not None:
            if selected.domain() is not source or selected.codomain() is not target:
                raise ValueError(f"the degree-{degree} component has the wrong endpoints")
            return selected
        return module_homset(source, target)(
            {label: target.zero() for label in source.module_generating_set()}
        )

    def _validate_components(self) -> None:
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
        degrees = set(other.domain().selected_degrees()) | set(self.codomain().selected_degrees())
        return cochain_homset(other.domain(), self.codomain())(
            {
                degree: self.component(degree) * other.component(degree)
                for degree in degrees
            }
        )


class CochainHomset(CategoricalHomset):
    Element = CochainMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        if domain.base_ring() is not codomain.base_ring():
            raise ValueError("cochain morphisms require one common base ring")
        _initialize_module_hom_parent(self, hom_family, domain, codomain)

    def _degrees(self):
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
            components = {
                degree: components.component(degree)
                for degree in self._degrees()
            }
        elif isinstance(components, Morphism):
            if components.domain() is not self.domain() or components.codomain() is not self.codomain():
                raise ValueError("the morphism has the wrong cochain endpoints")
            component = getattr(components, "component", None)
            if component is not None:
                components = {
                    degree: component(degree)
                    for degree in self._degrees()
                }
            else:
                return self.elementwise(lambda element: components(element))
        return self.element_class(self, components)

    def elementwise(self, function):
        if not callable(function):
            raise TypeError("an elementwise cochain map must be callable")
        components = {}
        for degree in self._degrees():
            source = self.domain().graded_piece(degree)
            target = self.codomain().graded_piece(degree)

            def on_piece(element, degree=degree, target=target):
                total = self.domain().from_component(degree, element)
                image = self.codomain()(function(total))
                return image.homogeneous_component(degree)

            components[degree] = module_homset(source, target).elementwise(on_piece)
        return self.element_class(self, components)

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
        return self(
            {
                degree: module_homset(
                    self.domain().graded_piece(degree),
                    self.domain().graded_piece(degree),
                ).identity()
                for degree in self.domain().selected_degrees()
            }
        )


class CochainHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return CochainHomset


# The declaration is placed after the concrete fixed-Hom class to avoid a
# module-level forward-reference helper or a second registration mechanism.
CochainComplexes._HomCategory = CochainHomCategoryConstruction


def cochain_homset(domain, codomain):
    ring = domain.base_ring()
    if codomain.base_ring() is not ring:
        raise ValueError("cochain morphisms require one common base ring")
    category = CochainComplexes(ring)
    if domain not in category or codomain not in category:
        raise TypeError("cochain Hom endpoints must lie in one cochain-complex category")
    return category.Hom(domain, codomain)


def CochainComplex(base_ring, pieces, differentials, name=None):
    return CochainComplexObject(base_ring, pieces, differentials, name=name)


def Cycles(complex_, degree):
    r"""Return ``ker(d^degree)`` as a subobject of ``C^degree``."""
    return complex_.differential_component(degree).kernel()


def Boundaries(complex_, degree):
    r"""Return ``im(d^(degree-1))`` as a subobject of ``C^degree``."""
    return complex_.differential_component(int(degree) - 1).image()


_COHOMOLOGY_CACHE = {}


def Cohomology(complex_, degree):
    r"""Return ``H^degree = ker(d)/im(d)`` from finite presentations.

    Let ``C^p = R^n/P`` and ``C^(p+1) = R^m/Q`` and let ``F`` be the matrix
    of ``d^p`` on the selected generators.  Closed classes are represented by
    the projection to ``R^n`` of

    ``ker [ F  -Q^t ]``.

    Inside that free module of closed lifts, the denominator is generated by
    the relation rows ``P`` and the columns of ``d^(p-1)``.  Expressing those
    generators in a basis of the closed-lift module gives an ordinary finite
    presentation of cohomology.  Thus the same construction works for free
    complexes and for restricted-scalar de Rham pieces carrying relations.
    """
    degree = int(degree)
    if degree < 0:
        raise ValueError("cohomology degree is nonnegative")
    cache_key = (id(complex_), degree)
    cached = _COHOMOLOGY_CACHE.get(cache_key)
    if (
        cached is not None
        and cached.cochain_complex() is complex_
        and cached.cohomological_degree() == degree
    ):
        return cached

    from sage.categories.principal_ideal_domains import PrincipalIdealDomains
    from sage.modules.free_module import FreeModule as SageFreeModule
    from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_presented_modules import (
        FinitelyPresentedModule,
        _presentation_from_relation_rows,
        _presentation_matrix,
    )
    from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
        ModuleMorphism,
    )
    from dzack_research.preamble.categories.rings import engine_ring
    from dzack_research.preamble.tensors import tensor

    ring = complex_.base_ring()
    engine = engine_ring(ring)
    if engine not in PrincipalIdealDomains():
        raise NotImplementedError(
            "the active cohomology presentation backend requires a principal ideal domain"
        )

    current = complex_.graded_piece(degree)
    following = complex_.graded_piece(degree + 1)
    current_labels = tuple(current.module_generating_set())
    following_labels = tuple(following.module_generating_set())
    current_relations = _presentation_matrix(current).change_ring(engine)
    following_relations = _presentation_matrix(following).change_ring(engine)

    def represented_differential(index):
        component = complex_.differential_component(index)
        if isinstance(component, ModuleMorphism):
            return component
        if hasattr(component, "represented_module_morphism"):
            return component.represented_module_morphism()
        raise NotImplementedError(
            "this differential component has no selected finite module presentation"
        )

    differential = represented_differential(degree)
    matrix = differential.tensor().change_ring(engine)
    target_relation_count = int(following_relations.nrows())
    block_entries = []
    for row in range(len(following_labels)):
        block_entries.extend(matrix[row, column] for column in range(len(current_labels)))
        block_entries.extend(
            -following_relations[relation, row]
            for relation in range(target_relation_count)
        )
    block = tensor.matrix(
        engine,
        len(following_labels),
        len(current_labels) + target_relation_count,
        block_entries,
    )
    kernel_rows = tuple(block.right_kernel().basis_matrix().rows())
    projected = [tuple(row[: len(current_labels)]) for row in kernel_rows]
    free_cover = SageFreeModule(engine, len(current_labels))
    closed_submodule = (
        free_cover.submodule(projected)
        if projected
        else free_cover.zero_submodule()
    )
    closed_basis_engine = closed_submodule.basis_matrix()
    closed_basis = tensor.matrix(engine, closed_basis_engine)
    closed_rank = int(closed_basis.nrows())

    denominator_rows = [tuple(row) for row in current_relations.rows()]
    if degree > 0:
        previous = represented_differential(degree - 1).tensor().change_ring(engine)
        denominator_rows.extend(
            tuple(previous[row, column] for row in range(len(current_labels)))
            for column in range(int(previous.ncols()))
        )

    relation_coordinates = []
    for row in denominator_rows:
        if not any(row):
            continue
        coordinates = closed_submodule.coordinate_vector(free_cover(row))
        relation_coordinates.append(tuple(coordinates))

    labels = finite_ordered_set(range(closed_rank))
    relation_labels = finite_ordered_set(range(len(relation_coordinates)))
    relations = tensor.matrix(
        engine,
        len(relation_coordinates),
        closed_rank,
        [entry for row in relation_coordinates for entry in row],
    )
    presentation = _presentation_from_relation_rows(
        ring,
        labels,
        relation_labels,
        relations,
    )
    result = FinitelyPresentedModule(presentation)
    result._preamble_cohomology_complex = complex_
    result._preamble_cohomology_degree = degree
    result._preamble_cohomology_current_module = current
    result._preamble_cohomology_current_labels = current_labels
    result._preamble_cohomology_free_cover = free_cover
    result._preamble_cohomology_closed_submodule = closed_submodule
    result._preamble_cohomology_closed_basis = tuple(closed_basis_engine.rows())
    result = refine(result, CohomologyModules(ring))
    _COHOMOLOGY_CACHE[cache_key] = result
    return result


__all__ = [
    "Boundaries",
    "CochainComplex",
    "CochainComplexElement",
    "CochainComplexObject",
    "CochainComplexes",
    "CochainDifferential",
    "CochainHomset",
    "CochainMorphism",
    "Cohomology",
    "CohomologyModules",
    "Cycles",
    "cochain_homset",
]
