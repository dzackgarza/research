r"""Finite-support direct sums of a represented family of graded modules."""

from dzack_research.preamble.categories.rings.ring_foundation import _engine_ring as _engine_ring
from typing import Any

from sage.categories.category import Category
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import ModuleElement
from sage.structure.parent import Parent
from sage.structure.richcmp import op_EQ, op_NE

from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
)
from dzack_research.preamble.categories.modules.graded_modules import GradedModules
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring
from dzack_research.preamble.categories.sets.set_categories import CoproductOfFamily
from dzack_research.preamble.categories.sets.set_categories import NN


class GradedDirectSumElement(ModuleElement):
    r"""A finite family of homogeneous components."""

    def __init__(self, parent, components) -> None:
        ModuleElement.__init__(self, parent)
        normalized = {}
        for degree, component in components.items():
            degree = int(degree)
            piece = parent.graded_piece(degree)
            if component.parent() is not piece:
                component = piece(component)
            if component != piece.zero():
                normalized[degree] = component
        self._components = normalized

    def homogeneous_components(self):
        return dict(self._components)

    def homogeneous_component(self, degree):
        degree = int(degree)
        return self._components.get(degree, self.parent().graded_piece(degree).zero())

    def is_homogeneous(self) -> bool:
        return len(self._components) <= 1

    def degree(self):
        if not self._components:
            return 0
        if len(self._components) != 1:
            raise ValueError("a nonhomogeneous element has no single degree")
        return next(iter(self._components))

    def monomial_coefficients(self):
        coefficients = {}
        labels = self.parent().module_generating_set()
        for degree, component in self._components.items():
            for label, coefficient in module_coefficients(
                component, self.parent().graded_piece(degree)
            ).items():
                coefficients[labels(degree, label)] = coefficient
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

    def _richcmp_(self, other, op):
        if op not in (op_EQ, op_NE):
            return NotImplemented
        equal = (
            isinstance(other, GradedDirectSumElement)
            and other.parent() is self.parent()
        )
        if equal:
            degrees = set(self._components) | set(other._components)
            equal = all(
                self.homogeneous_component(degree)
                == other.homogeneous_component(degree)
                for degree in degrees
            )
        return equal if op == op_EQ else not equal

    def _repr_(self):
        if not self._components:
            return "0"
        return " + ".join(
            f"[{degree}]({component})"
            for degree, component in sorted(self._components.items())
        )


class GradedDirectSumModule(Parent):
    r"""The module \(\bigoplus_{d\geq0} M_d\) with finite-support elements."""

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
    ) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._preamble_base_ring = self._base_ring
        self._piece = piece
        self._name = name
        self._realize_generator = realize_generator
        self._realized_object = realized_object
        self._from_realization = from_realization
        self._degree_index_set = NN if degree_index_set is None else degree_index_set
        self._pieces: dict[int, Any] = {}
        self._indices = None
        categories = [
            GradedModules(self._base_ring),
            FramedModules(self._base_ring),
        ]
        Parent.__init__(
            self,
            base=_engine_ring(self._base_ring),
            category=Category.join(tuple(categories)),
        )

    def base_ring(self):
        return self._base_ring

    def graded_piece(self, degree):
        degree = int(degree)
        if degree < 0:
            raise ValueError("a graded degree is nonnegative")
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
            self._indices = CoproductOfFamily(
                self.degree_index_set(),
                lambda degree: self.graded_piece(int(degree)).module_generating_set(),
            )
        return self._indices

    def module_generator(self, label):
        label = self.module_generating_set()(label)
        degree = int(label.summand_index())
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
            degree = int(label.summand_index())
            piece_label = label.summand_element()
            piece = self.graded_piece(degree)
            contribution = piece.scalar_multiple(
                coefficient, piece.module_generator(piece_label)
            )
            by_degree[degree] = by_degree.get(degree, piece.zero()) + contribution
        return self.from_components(by_degree)

    def from_component(self, degree, component):
        return self.element_class(self, {int(degree): component})

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
        if self._realize_generator is None:
            raise NotImplementedError("this direct sum has no selected realization")
        label = self.module_generating_set()(label)
        return self._realize_generator(
            int(label.summand_index()),
            label.summand_element(),
        )

    def realized_object(self):
        if self._realized_object is None:
            raise NotImplementedError("this direct sum has no selected realization")
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
        if self._from_realization is None:
            raise NotImplementedError(
                "this direct sum has no selected inverse realization"
            )
        return self._from_realization(element)

    # A sparse free construction only needs to know which finite presented
    # component contains a selected generator.  Keeping this protocol here
    # prevents it from falsely treating the component labels as free.
    def module_component_key(self, label):
        label = self.module_generating_set()(label)
        return int(label.summand_index())

    def module_component(self, key):
        return self.graded_piece(key)

    def module_component_generator_label(self, label):
        return self.module_generating_set()(label).summand_element()

    def module_label_from_component(self, key, component_label):
        return self.module_generating_set()(int(key), component_label)

    def _repr_(self):
        return self._name or "Graded direct sum module"


__all__ = [
    "GradedDirectSumElement",
    "GradedDirectSumModule",
]
