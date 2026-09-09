r"""Owned topological, finite-``C^k`` and smooth manifolds and atlas maps.

SageManifolds is the private chart/transition engine.  The public object keeps
the manifold's dimension and differentiability degree, an owned finite family
of labelled charts, and exact forward/inverse coordinate expressions for each
represented atlas transition.
"""

from sage.manifolds.manifold import Manifold as _SageManifold
from sage.rings.infinity import Infinity
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import Sets
from dzack_research.preamble.owned_category import object_of


class ManifoldAtlasChart(SageObject):
    r"""One labelled chart of an owned manifold."""

    def __init__(self, manifold, label, engine_chart) -> None:
        self._manifold = manifold
        self._label = label
        self._engine = engine_chart

    def manifold(self):
        return self._manifold

    def label(self):
        return self._label

    def coordinates(self):
        return tuple(self._engine[:])

    def coordinate(self, index):
        return self._engine[int(index)]

    def _engine_chart(self):
        return self._engine

    def transition_to(self, other, forward_expressions, inverse_expressions):
        return self.manifold().transition_map(
            self.label(),
            other.label(),
            forward_expressions,
            inverse_expressions,
        )

    def _repr_(self):
        return f"Chart {self.label()} of {self.manifold()}"


class ManifoldAtlasTransition(SageObject):
    r"""An invertible atlas coordinate change with retained regularity."""

    def __init__(
        self,
        source,
        target,
        engine_transition,
        forward_expressions,
        inverse_expressions,
    ) -> None:
        self._source = source
        self._target = target
        self._engine = engine_transition
        self._forward = tuple(forward_expressions)
        self._inverse_expressions = tuple(inverse_expressions)
        self._inverse_transition = None

    def source(self):
        return self._source

    def target(self):
        return self._target

    def manifold(self):
        return self.source().manifold()

    def forward_expressions(self):
        return self._forward

    def inverse_expressions(self):
        return self._inverse_expressions

    def regularity(self):
        return self.manifold().regularity()

    def inverse(self):
        if self._inverse_transition is None:
            inverse = ManifoldAtlasTransition(
                self.target(),
                self.source(),
                self._engine.inverse(),
                self.inverse_expressions(),
                self.forward_expressions(),
            )
            inverse._inverse_transition = self
            self._inverse_transition = inverse
        return self._inverse_transition

    def __call__(self, *coordinates):
        return self._engine(*coordinates)

    def _repr_(self):
        return (
            f"{self.regularity()} atlas transition "
            f"{self.source().label()} -> {self.target().label()}"
        )


class TopologicalManifolds(OwnedCategory):
    r"""Owned finite-dimensional topological manifolds."""

    def super_categories(self):
        return [Sets()]

    @classmethod
    def _repr_object_names(cls):
        return "topological manifolds"

    def an_object(self):
        return self(1, "M_top")

    def _call_(self, dimension, name):
        dimension = int(dimension)
        if dimension <= 0:
            raise ValueError("a represented manifold here has positive dimension")
        engine = _SageManifold(
            dimension,
            str(name),
            structure="topological",
            unique_tag=object(),
        )
        return object_of(
            self,
            engine_manifold=engine,
            manifold_dimension=dimension,
            manifold_name=str(name),
            manifold_structure="topological",
            differentiability_degree=None,
        )

    class ParentMethods:
        def __init__(
            self,
            engine_manifold,
            manifold_dimension,
            manifold_name,
            manifold_structure,
            differentiability_degree,
            **rest,
        ) -> None:
            self._preamble_engine_manifold = engine_manifold
            self._preamble_manifold_dimension = int(manifold_dimension)
            self._preamble_manifold_name = str(manifold_name)
            self._preamble_manifold_structure = str(manifold_structure)
            self._preamble_differentiability_degree = differentiability_degree
            self._preamble_charts = {}
            self._preamble_transitions = {}
            super().__init__(**rest)

        def dimension(self):
            return self._preamble_manifold_dimension

        def manifold_name(self):
            return self._preamble_manifold_name

        def manifold_structure(self):
            return self._preamble_manifold_structure

        def regularity(self):
            degree = self._preamble_differentiability_degree
            if degree is None:
                return "topological"
            if degree == Infinity:
                return "smooth"
            return f"C^{degree}"

        def differentiability_degree(self):
            degree = self._preamble_differentiability_degree
            if degree is None:
                raise TypeError("a merely topological manifold has no differentiability degree")
            return degree

        def is_smooth(self) -> bool:
            return self._preamble_differentiability_degree == Infinity

        def _engine_manifold(self):
            return self._preamble_engine_manifold

        def chart(self, label, coordinates):
            if label in self._preamble_charts:
                raise ValueError(f"the chart label {label!r} is already used")
            engine_chart = self._engine_manifold().chart(coordinates)
            chart = ManifoldAtlasChart(self, label, engine_chart)
            self._preamble_charts[label] = chart
            return chart

        def chart_labels(self):
            return finite_ordered_set(tuple(self._preamble_charts))

        def atlas(self):
            labels = self.chart_labels()
            return finite_indexed_family(
                labels,
                lambda label: self._preamble_charts[label],
                name=f"Atlas charts of {self}",
            )

        def transition_map(
            self,
            source_label,
            target_label,
            forward_expressions,
            inverse_expressions,
        ):
            source = self.atlas()[source_label]
            target = self.atlas()[target_label]
            forward_expressions = tuple(forward_expressions)
            inverse_expressions = tuple(inverse_expressions)
            if len(forward_expressions) != self.dimension():
                raise ValueError("a coordinate change has one target expression per coordinate")
            if len(inverse_expressions) != self.dimension():
                raise ValueError("an inverse coordinate change has one source expression per coordinate")
            engine_transition = source._engine_chart().transition_map(
                target._engine_chart(),
                forward_expressions,
            )
            engine_transition.set_inverse(*inverse_expressions)
            transition = ManifoldAtlasTransition(
                source,
                target,
                engine_transition,
                forward_expressions,
                inverse_expressions,
            )
            reverse = transition.inverse()
            self._preamble_transitions[source_label, target_label] = transition
            self._preamble_transitions[target_label, source_label] = reverse
            return transition

        def transition(self, source_label, target_label):
            try:
                return self._preamble_transitions[source_label, target_label]
            except KeyError as error:
                raise ValueError("no represented atlas transition joins those labels") from error

        def transitions(self):
            index_set = finite_ordered_set(tuple(self._preamble_transitions))
            return finite_indexed_family(
                index_set,
                lambda pair: self._preamble_transitions[pair],
                name=f"Atlas transitions of {self}",
            )

        def _repr_(self):
            return (
                f"{self.dimension()}-dimensional {self.regularity()} manifold "
                f"{self.manifold_name()}"
            )


class DifferentiableManifolds(OwnedCategory):
    r"""Owned real differentiable manifolds.

    The direct constructor records a finite positive ``C^k`` degree.  Smooth
    manifolds form the represented subcategory below and therefore belong here
    as well.
    """

    def super_categories(self):
        return [TopologicalManifolds()]

    @classmethod
    def _repr_object_names(cls):
        return "differentiable manifolds"

    def an_object(self):
        return self(1, "M_C1", 1)

    def _call_(self, dimension, name, differentiability_degree):
        dimension = int(dimension)
        degree = int(differentiability_degree)
        if dimension <= 0:
            raise ValueError("a represented manifold here has positive dimension")
        if degree <= 0:
            raise ValueError("a finite differentiability degree is a positive integer")
        engine = _SageManifold(
            dimension,
            str(name),
            structure="differentiable",
            diff_degree=degree,
            unique_tag=object(),
        )
        return object_of(
            self,
            engine_manifold=engine,
            manifold_dimension=dimension,
            manifold_name=str(name),
            manifold_structure="differentiable",
            differentiability_degree=degree,
        )


class SmoothManifolds(OwnedCategory):
    r"""Owned smooth real manifolds."""

    def super_categories(self):
        return [DifferentiableManifolds()]

    @classmethod
    def _repr_object_names(cls):
        return "smooth manifolds"

    def an_object(self):
        return self(1, "M_smooth")

    def _call_(self, dimension, name):
        dimension = int(dimension)
        if dimension <= 0:
            raise ValueError("a represented manifold here has positive dimension")
        engine = _SageManifold(
            dimension,
            str(name),
            structure="smooth",
            unique_tag=object(),
        )
        return object_of(
            self,
            engine_manifold=engine,
            manifold_dimension=dimension,
            manifold_name=str(name),
            manifold_structure="smooth",
            differentiability_degree=Infinity,
        )


__all__ = [
    "DifferentiableManifolds",
    "ManifoldAtlasChart",
    "ManifoldAtlasTransition",
    "SmoothManifolds",
    "TopologicalManifolds",
]
