r"""Finite-support direct sums of a represented family of graded modules."""

from typing import Any

from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.structure.element import ModuleElement, parent as element_parent
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.modules.graded_modules import (
    GradedModules,
    _grading_identity,
    _require_grading_monoid,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import ModuleMorphism
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    Modules,
    _fix_selected_module_framing,
)
from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring as _engine_ring
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.categories.sets.indexed_families import indexed_family
from dzack_research.preamble.categories.sets.set_categories import NN, Sets
from dzack_research.preamble.refine import realize_owned_category
from dzack_research.preamble.owned_category import _object_of


class _DirectSumInjectionMorphism(ModuleMorphism):
    r"""The canonical inclusion of one summand into a finite-support direct sum."""

    def __init__(self, parent, degree) -> None:
        self._degree = degree
        super().__init__(
            parent,
            lambda element: self.codomain().from_component(self._degree, element),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return True


class _DirectSumProjectionMorphism(ModuleMorphism):
    r"""The canonical projection from a finite-support direct sum."""

    def __init__(self, parent, degree) -> None:
        self._degree = degree
        super().__init__(
            parent,
            lambda element: self.domain()(element).homogeneous_component(self._degree),
            elementwise=True,
        )

    def _elementwise_linearity_derivation(self):
        return True


class _DirectSumFactorMorphism(ModuleMorphism):
    r"""The coproduct factor induced by a family of admitted linear maps."""

    def __init__(self, parent, maps) -> None:
        self._component_maps = maps

        def evaluate(element):
            source = self.domain()
            target = self.codomain()
            return sum(
                (
                    maps[degree](component)
                    for degree, component in source(element).homogeneous_components().items()
                ),
                target.zero(),
            )

        super().__init__(parent, evaluate, elementwise=True)

    def _elementwise_linearity_derivation(self):
        indices = self._component_maps.index_set()
        if not indices.cardinality().is_finite():
            return Unknown
        decision = True
        for degree in indices:
            morphism = self._component_maps[degree]
            current = getattr(morphism, "linearity_decision", lambda: Unknown)()
            if current is False:
                return False
            if current is not True:
                decision = Unknown
        return decision


class GradedDirectSumElement(ModuleElement):
    r"""A finite family of homogeneous components."""

    def __init__(self, parent, components) -> None:
        super().__init__(parent)
        normalized = {}
        for degree, component in components.items():
            degree = parent.normalize_degree(degree)
            piece = parent.graded_piece(degree)
            if component.parent() is not piece:
                component = piece(component)
            if (component == piece.zero()) is not True:
                normalized[degree] = component
        self._components = normalized

    def homogeneous_components(self):
        return dict(self._components)

    def homogeneous_component(self, degree):
        degree = self.parent().normalize_degree(degree)
        return self._components.get(degree, self.parent().graded_piece(degree).zero())

    def is_homogeneous(self) -> bool:
        return len(self._components) <= 1

    def degree(self):
        if not self._components:
            return _grading_identity(self.parent().grading_monoid())
        if len(self._components) != 1:
            raise ValueError("a nonhomogeneous element has no single degree")
        return next(iter(self._components))

    def monomial_coefficients(self):
        coefficients = {}
        labels = self.parent().module_generating_set()
        for degree, component in self._components.items():
            for label, coefficient in self.parent().graded_piece(degree).framing_coefficients(component).items():
                coefficients[
                    labels(self.parent().degree_index_set()(degree), label)
                ] = coefficient
        return coefficients

    def _add_(self, other):
        degrees = set(self._components) | set(other._components)
        return self.parent().from_components(
            {
                degree: self.homogeneous_component(degree)
                + other.homogeneous_component(degree)
                for degree in degrees
            }
        )

    def _neg_(self):
        return self.parent().from_components(
            {degree: -component for degree, component in self._components.items()}
        )

    def _lmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _rmul_(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def __rmul__(self, scalar):
        return self.parent().scalar_multiple(scalar, self)

    def _acted_upon_(self, actor, self_on_left):
        _ = self_on_left
        try:
            scalar = self.parent().base_ring()(actor)
        except (TypeError, ValueError):
            return None
        return self.parent().scalar_multiple(scalar, self)

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        if element_parent(other) is not self.parent():
            return op == op_NE
        decisions = tuple(
            self.homogeneous_component(degree) == other.homogeneous_component(degree)
            for degree in set(self._components) | set(other._components)
        )
        match (any(value is False for value in decisions), all(value is True for value in decisions)):
            case (True, _):
                equal = False
            case (_, True):
                equal = True
            case _:
                equal = Unknown
        return equal if op == op_EQ or equal is Unknown else not equal

    def _repr_(self):
        if not self._components:
            return "0"
        return " + ".join(
            f"[{degree}]({component})"
            for degree, component in self._components.items()
        )


class GradedDirectSumModule(Parent):
    r"""A represented graded direct sum with finite-support elements.

    The degree set is part of the defining data.  It defaults to ``NN`` for
    the ordinary nonnegative graded constructions, but callers such as
    cochain complexes may supply another owned indexing set, for example the
    owned integers.
    """

    Element = GradedDirectSumElement

    def __init__(
        self,
        base_ring,
        piece,
        name=None,
        realize_generator=None,
        realized_object=None,
        from_realization=None,
        degree_index_set=None,
        grading_monoid=None,
        extra_categories=(),
        extra_construction_data=None,
    ) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._preamble_base_ring = self._base_ring
        self._piece = piece
        self._name = name
        self._realize_generator = realize_generator
        self._realized_object = realized_object
        self._from_realization = from_realization
        self._degree_index_set = NN if degree_index_set is None else degree_index_set
        self._grading_monoid = _require_grading_monoid(grading_monoid)
        for key, value in dict(extra_construction_data or {}).items():
            setattr(self, f"_preamble_{key}", value)
        self._pieces: dict[Any, Any] = {}
        self._indices = None
        categories = [
            GradedModules(self._base_ring, self._grading_monoid),
            FramedModules(self._base_ring),
            *tuple(extra_categories),
        ]
        labels = self.module_generating_set()
        source = self._base_ring.free_module(labels)
        _fix_selected_module_framing(
            self,
            self._base_ring,
            labels,
            self.module_generator,
            source,
        )
        Parent.__init__(
            self,
            base=_engine_ring(self._base_ring),
            category=Cat().meet(categories),
        )
        realize_owned_category(self)

    def base_ring(self):
        return self._base_ring

    def grading_monoid(self):
        return self._grading_monoid

    def normalize_degree(self, degree):
        try:
            selected = self.degree_index_set()(degree)
            return self.grading_monoid()(selected)
        except (TypeError, ValueError) as error:
            raise ValueError(f"{degree} is not a degree of {self}") from error

    def graded_piece(self, degree):
        degree = self.normalize_degree(degree)
        cached = self._pieces.get(degree)
        if cached is not None:
            return cached
        piece = self._piece(degree)
        if _owned_ring(piece.base_ring()) is not self.base_ring():
            raise ValueError("all graded direct-sum pieces require one base ring")
        self._pieces[degree] = piece
        return piece

    def degree_index_set(self):
        return self._degree_index_set

    def module_generating_set(self):
        if self._indices is None:
            self._indices = Sets().coproduct(
                indexed_family(
                    self.degree_index_set(),
                    lambda degree: self.graded_piece(degree).module_generating_set(),
                )
            )
        return self._indices

    def module_generator(self, label):
        label = self.module_generating_set()(label)
        degree = self.normalize_degree(label.summand_index())
        piece_label = label.summand_element()
        return self.from_component(
            degree, self.graded_piece(degree).module_generator(piece_label)
        )

    def linear_combination(self, coefficients):
        by_degree = {}
        for raw_label, coefficient in coefficients.items():
            if not coefficient:
                continue
            label = self.module_generating_set()(raw_label)
            degree = self.normalize_degree(label.summand_index())
            piece_label = label.summand_element()
            piece = self.graded_piece(degree)
            contribution = piece.scalar_multiple(
                coefficient, piece.module_generator(piece_label)
            )
            by_degree[degree] = by_degree.get(degree, piece.zero()) + contribution
        return self.from_components(by_degree)

    def from_component(self, degree, component):
        return self.element_class(self, {self.normalize_degree(degree): component})

    def from_graded_piece(self, degree, component):
        r"""Include one homogeneous piece into the represented direct sum."""
        piece = self.graded_piece(degree)
        return self.from_component(degree, piece(component))

    def from_components(self, components):
        return self.element_class(self, components)

    def _element_constructor_(self, value):
        if isinstance(value, GradedDirectSumElement):
            if value.parent() is self:
                return value
            raise TypeError("the element belongs to a different graded direct sum")
        if isinstance(value, dict):
            return self.linear_combination(value)
        raise TypeError(f"{value!r} does not define an element of {self}")

    def zero(self):
        return self.from_components({})

    def scalar_multiple(self, scalar, element):
        if element.parent() is not self:
            element = self(element)
        scalar = self.base_ring()(scalar)
        return self.from_components(
            {
                degree: component.parent().scalar_multiple(scalar, component)
                for degree, component in element.homogeneous_components().items()
            }
        )

    def realize_module_generator(self, label):
        assert self._realize_generator is not None, (
            "realize_module_generator requires a selected realization of this direct sum"
        )
        label = self.module_generating_set()(label)
        return self._realize_generator(
            self.normalize_degree(label.summand_index()),
            label.summand_element(),
        )

    def realized_object(self):
        assert self._realized_object is not None, (
            "realized_object requires a selected realization of this direct sum"
        )
        return self._realized_object

    def realize(self, element):
        r"""Realize a finite family of homogeneous components in its target."""
        element = self(element)
        target = self.realized_object()
        return sum(
            (
                coefficient * self.realize_module_generator(label)
                for label, coefficient in element.monomial_coefficients().items()
            ),
            target.zero(),
        )

    def from_realization(self, element):
        r"""Decompose a realized element into its finite homogeneous support."""
        assert self._from_realization is not None, (
            "from_realization requires a selected inverse realization of this direct sum"
        )
        return self._from_realization(element)

    # A sparse free construction only needs to know which finite presented
    # component contains a selected generator.  Keeping this protocol here
    # prevents it from falsely treating the component labels as free.
    def module_component_key(self, label):
        label = self.module_generating_set()(label)
        return self.normalize_degree(label.summand_index())

    def module_component(self, key):
        return self.graded_piece(key)

    def module_component_generator_label(self, label):
        return self.module_generating_set()(label).summand_element()

    def module_label_from_component(self, key, component_label):
        return self.module_generating_set()(
            self.degree_index_set()(self.normalize_degree(key)),
            component_label,
        )

    def _repr_(self):
        return self._name or "Graded direct sum module"


__all__ = [
    "GradedDirectSumElement",
    "GradedDirectSumModule",
]


class _DirectSumOfModules:
    r"""Finite-support realization of a direct sum of arbitrary modules.

    The component elements and arithmetic are shared with the framed
    realization; no basis is claimed for the pieces.  The coproduct map is
    the finite sum of the component maps.  Further structure is constructed
    from this family at its module owner.
    """

    def __init__(self, summand_family, **rest) -> None:
        self._summand_family = summand_family
        super().__init__(**rest)

    def degree_index_set(self):
        return self._summand_family.index_set()

    def normalize_degree(self, degree):
        return self.degree_index_set()(degree)

    def graded_piece(self, degree):
        piece = self._summand_family[self.normalize_degree(degree)]
        assert piece in Modules(self.base_ring()), "every summand is a module over the common ring"
        return piece

    def from_components(self, components):
        return self.element_class(self, components)

    def from_component(self, degree, component):
        return self.from_components({self.normalize_degree(degree): component})

    from_graded_piece = from_component

    def _element_constructor_(self, value):
        source = element_parent(value)
        if source is self:
            return value
        if source in Modules(self.base_ring()) and self._built_on_the_same_data(source):
            return self.from_components(value.homogeneous_components())
        if isinstance(value, dict):
            return self.from_components(value)
        raise TypeError("a direct-sum element is a finite family of homogeneous components")

    def __call__(self, value):
        return self._element_constructor_(value)

    def zero(self):
        return self.from_components({})

    an_element = zero

    def _owned_scalar_multiple(self, scalar, element):
        scalar = self.base_ring()(scalar)
        return self.from_components({
            degree: self.graded_piece(degree).scalar_multiple(scalar, component)
            for degree, component in self(element).homogeneous_components().items()
        })

    @cached_method
    def injection(self, degree):
        degree = self.normalize_degree(degree)
        return _DirectSumInjectionMorphism(
            Modules(self.base_ring()).Mor(self.graded_piece(degree), self),
            degree,
        )

    @cached_method
    def projection(self, degree):
        degree = self.normalize_degree(degree)
        return _DirectSumProjectionMorphism(
            Modules(self.base_ring()).Mor(self, self.graded_piece(degree)),
            degree,
        )

    def from_maps(self, codomain, maps):
        r"""The unique linear map whose restrictions to the summands are ``maps``."""
        assert maps.index_set() is self.degree_index_set(), "the maps use the summand index set"

        for degree in maps.index_set() if maps.index_set().cardinality().is_finite() else ():
            morphism = maps[degree]
            assert morphism.domain() is self.graded_piece(degree) and morphism.codomain() is codomain, (
                "a coproduct cocone has the stated summands and common codomain"
            )
        return _DirectSumFactorMorphism(
            Modules(self.base_ring()).Mor(self, codomain),
            maps,
        )

    def _direct_sum_realization(self):
        r"""The private component engine retained when further structure is supplied."""
        return _DirectSumOfModules, GradedDirectSumElement

    def _module_with_structure(self, categories, construction_data):
        return _direct_sum_of_modules(
            self.base_ring(), self.grading_index_set(), self._summand_family,
            extra_categories=categories, construction_data=construction_data,
            _realization=self._direct_sum_realization(),
        )

    def _repr_(self):
        return f"Direct sum over {self.degree_index_set()}"


@cached_function(key=lambda ring, pieces: (id(ring), id(pieces)))
def _direct_sum_framing_source(ring, pieces):
    r"""The one chosen free source of the summed framings of this family."""
    labels = Sets().coproduct(pieces.map(lambda piece: piece.module_generating_set()))
    return ring.free_module(labels)


class _FramedDirectSumOfModules(_DirectSumOfModules):
    r"""The direct sum of chosen epimorphisms from free modules.

    If F(S_i) -> M_i are the framings, F(disjoint_union S_i) -> direct_sum M_i
    sends the generator (i,s) to the i-th inclusion of its image in M_i.
    Every finite-support element lifts term by term, so this is an epimorphism;
    no independence of the images is assumed.
    """

    def __init__(self, summand_family, **rest) -> None:
        ring = rest["base_ring"]
        source = _direct_sum_framing_source(ring, summand_family)
        super().__init__(
            summand_family=summand_family,
            module_generating_set=source.module_generating_set(),
            module_generator_function=lambda label: self.from_component(
                label.summand_index(),
                self.graded_piece(label.summand_index()).module_generator(label.summand_element()),
            ),
            framing_source=source,
            **rest,
        )

    def _element_constructor_(self, value):
        match value:
            case dict():
                return self.linear_combination(value)
            case _:
                return super()._element_constructor_(value)

    def _module_with_structure(self, categories, construction_data):
        return super()._module_with_structure(
            (FramedModules(self.base_ring()), *categories), construction_data,
        )

    def _direct_sum_realization(self):
        return _FramedDirectSumOfModules, GradedDirectSumElement

    def module_component_key(self, label):
        return self.module_generating_set()(label).summand_index()

    def module_component(self, degree):
        return self.graded_piece(degree)

    def module_component_generator_label(self, label):
        return self.module_generating_set()(label).summand_element()

    def module_label_from_component(self, degree, component_label):
        return self.module_generating_set()(self.normalize_degree(degree), component_label)


def _direct_sum_of_modules(
    ring, grading_monoid, pieces, *, extra_categories=(), construction_data=None,
    _realization=None,
):
    graded = GradedModules(ring, grading_monoid)
    assert pieces.index_set() is grading_monoid, "the grading indexes the summands"
    category = Cat().meet((graded, *extra_categories))
    match _realization:
        case None:
            match category.is_subcategory(FramedModules(ring)):
                case True:
                    realization = (_FramedDirectSumOfModules, GradedDirectSumElement)
                case False:
                    realization = (_DirectSumOfModules, GradedDirectSumElement)
        case realization:
            pass
    return _object_of(
        category, _engine=(graded, *realization),
        base_ring=ring, summand_family=pieces, **(construction_data or {}),
    )
