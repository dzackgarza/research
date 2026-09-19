r"""Owned topological, finite-``C^k`` and smooth manifolds and atlas maps.

SageManifolds is the private chart/transition engine.  The public object keeps
the manifold's dimension and differentiability degree, an owned finite family
of labelled charts, and exact forward/inverse coordinate expressions for each
represented atlas transition.
"""

from sage.categories.morphism import Morphism
from sage.manifolds.manifold import Manifold as _SageManifold
from sage.misc.cachefunc import cached_method
from sage.rings.infinity import Infinity
from sage.structure.element import Element
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
)
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.owned_category import _object_of


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


class _ManifoldTopologyData(SageObject):
    r"""Private topology realization supplied by SageManifolds.

    The native manifold is the maintained representation of the complete
    topology.  The owned topology exposes its open-set object without
    pretending that arbitrary subsets of an infinite manifold are enumerable.
    Exact arbitrary-subset openness is assertion-gated until a represented
    subset is carried by a native open-submanifold construction.
    """

    def __init__(self, engine_manifold) -> None:
        self._engine_manifold = engine_manifold

    def engine_manifold(self):
        return self._engine_manifold

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
                    "openness of an arbitrary represented subset of a manifold "
                    "requires a selected native open-submanifold presentation"
                )


class TopologicalManifolds(OwnedCategory):
    r"""Owned finite-dimensional topological manifolds."""

    def super_categories(self):
        return [TopologicalSpaces()]

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
        return _object_of(
            self,
            topology_data=_ManifoldTopologyData(engine),
            engine_manifold=engine,
            manifold_dimension=dimension,
            manifold_name=str(name),
            manifold_structure="topological",
            differentiability_degree=None,
            manifold_field="real",
        )

    class ElementMethods(Element):
        r"""A point of a manifold, given by its coordinates in a labelled chart."""

        def __init__(self, parent: Parent, coordinates, chart_label) -> None:
            Element.__init__(self, parent)
            self._coordinates = tuple(coordinates)
            self._chart_label = chart_label
            self._engine_point = parent._engine_manifold()(
                self._coordinates,
                chart=parent.atlas()[chart_label]._engine_chart(),
            )

        def manifold(self):
            return self.parent()

        def coordinates(self):
            return self._coordinates

        def chart(self):
            return self.parent().atlas()[self._chart_label]

        def _engine_manifold_point(self):
            return self._engine_point

        def __eq__(self, other) -> bool:
            r"""Two points of one manifold are equal when they are the same point, in whichever charts they were given."""
            return (
                element_parent(other) is self.parent()
                and other._engine_manifold_point() == self._engine_manifold_point()
            )

        def __ne__(self, other) -> bool:
            return not self == other

        def __hash__(self) -> int:
            return hash(id(self.parent()))

        def _repr_(self):
            return f"Point {self.coordinates()} of {self.manifold()}"

    class ParentMethods:
        def __init__(
            self,
            engine_manifold,
            manifold_dimension,
            manifold_name,
            manifold_structure,
            differentiability_degree,
            manifold_field="real",
            **rest,
        ) -> None:
            self._preamble_engine_manifold = engine_manifold
            self._preamble_manifold_dimension = int(manifold_dimension)
            self._preamble_manifold_name = str(manifold_name)
            self._preamble_manifold_structure = str(manifold_structure)
            self._preamble_differentiability_degree = differentiability_degree
            self._preamble_manifold_field = str(manifold_field)
            self._preamble_charts = {}
            self._preamble_transitions = {}
            super().__init__(**rest)

        def dimension(self):
            return self._preamble_manifold_dimension

        def manifold_name(self):
            return self._preamble_manifold_name

        def manifold_structure(self):
            return self._preamble_manifold_structure

        def base_field_type(self):
            return self._preamble_manifold_field

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
            return self._register_chart(label, self._engine_manifold().chart(coordinates))

        def _register_chart(self, label, engine_chart):
            r"""Record the chart ``engine_chart`` of this manifold's engine under ``label``."""
            if label in self._preamble_charts:
                raise ValueError(f"the chart label {label!r} is already used")
            chart = ManifoldAtlasChart(self, label, engine_chart)
            self._preamble_charts[label] = chart
            return chart

        def __call__(self, *args, **kwargs):
            r"""Construct a point through the owned element construction directly."""
            return self._element_constructor_(*args, **kwargs)

        def _element_constructor_(self, datum, chart_label="standard"):
            r"""Return the point with coordinates ``datum`` in the chart ``chart_label``, or ``datum`` if it is a point of this manifold."""
            match datum:
                case _ if element_parent(datum) is self:
                    return datum
                case _:
                    coordinates = tuple(datum)
                    if len(coordinates) != self.dimension():
                        raise ValueError("a manifold point has one coordinate per dimension")
                    return self.element_class(self, coordinates, chart_label)

        def point(self, coordinates, chart_label="standard"):
            return self(coordinates, chart_label)

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
            assert (source_label, target_label) in self._preamble_transitions, (
                "no represented atlas transition joins those labels"
            )
            return self._preamble_transitions[source_label, target_label]

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
        return _object_of(
            self,
            topology_data=_ManifoldTopologyData(engine),
            engine_manifold=engine,
            manifold_dimension=dimension,
            manifold_name=str(name),
            manifold_structure="differentiable",
            differentiability_degree=degree,
            manifold_field="real",
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
        return _object_of(
            self,
            topology_data=_ManifoldTopologyData(engine),
            engine_manifold=engine,
            manifold_dimension=dimension,
            manifold_name=str(name),
            manifold_structure="smooth",
            differentiability_degree=Infinity,
            manifold_field="real",
        )


class HolomorphicMapPresentation:
    r"""The selected chart presentation defining one represented holomorphic map."""

    def __init__(self, engine_map, coordinate_expressions, source_label, target_label) -> None:
        self._engine_map = engine_map
        self._coordinate_expressions = tuple(coordinate_expressions)
        self._source_label = source_label
        self._target_label = target_label

    def engine_map(self):
        return self._engine_map

    def coordinate_expressions(self):
        return self._coordinate_expressions

    def source_chart_label(self):
        return self._source_label

    def target_chart_label(self):
        return self._target_label


class HolomorphicMap(Morphism):
    r"""A holomorphic map represented by polynomial formulas in selected complex charts."""

    def __init__(self, parent, presentation) -> None:
        Morphism.__init__(self, parent)
        self._presentation = presentation

    def presentation(self):
        return self._presentation

    def coordinate_expressions(self):
        return self.presentation().coordinate_expressions()

    def source_chart(self):
        return self.domain().atlas()[self.presentation().source_chart_label()]

    def target_chart(self):
        return self.codomain().atlas()[self.presentation().target_chart_label()]

    def _engine_holomorphic_map(self):
        return self.presentation().engine_map()

    def __mul__(self, other):
        if not isinstance(other, HolomorphicMap) or other.codomain() is not self.domain():
            return NotImplemented
        engine = self._engine_holomorphic_map() * other._engine_holomorphic_map()
        source = other.source_chart()
        target = self.target_chart()
        expressions = engine.expr(source._engine_chart(), target._engine_chart())
        # Native Sage charts can return the one coordinate either as a
        # scalar expression or as a tuple; normalize only the scalar case.
        if self.codomain().dimension() == 1 and not isinstance(expressions, tuple):
            expressions = (expressions,)
        return other.domain().Mor(self.codomain())._from_engine_polynomial_map(
            engine,
            tuple(expressions),
            source.label(),
            target.label(),
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, HolomorphicMap)
            and other.domain() is self.domain()
            and other.codomain() is self.codomain()
            and other.coordinate_expressions() == self.coordinate_expressions()
            and other.source_chart().label() == self.source_chart().label()
            and other.target_chart().label() == self.target_chart().label()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None

    def _repr_(self):
        return f"Holomorphic map {self.domain()} -> {self.codomain()}"


class ComplexManifoldHomset(CategoricalHomset):
    Element = HolomorphicMap

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    @staticmethod
    def _unique_chart(manifold):
        labels = tuple(manifold.chart_labels())
        assert len(labels) == 1, (
            "the represented polynomial holomorphic-map constructor requires one selected global chart"
        )
        return manifold.atlas()[labels[0]]

    def polynomial(self, coordinate_expressions):
        r"""Construct the holomorphic map defined by polynomial chart formulas."""
        source = self._unique_chart(self.domain())
        target = self._unique_chart(self.codomain())
        expressions = tuple(coordinate_expressions)
        if len(expressions) != self.codomain().dimension():
            raise ValueError("a holomorphic coordinate map has one expression per target coordinate")
        variables = tuple(source.coordinates())
        if any(not all(expression.is_polynomial(variable) for variable in variables) for expression in expressions):
            raise ValueError("this constructor certifies holomorphicity only for polynomial coordinate formulas")
        engine = self.domain()._engine_manifold().diff_map(
            self.codomain()._engine_manifold(),
            expressions if len(expressions) != 1 else expressions[0],
            chart1=source._engine_chart(),
            chart2=target._engine_chart(),
        )
        return self._from_engine_polynomial_map(
            engine, expressions, source.label(), target.label()
        )

    def _from_engine_polynomial_map(self, engine, expressions, source_label, target_label):
        presentation = HolomorphicMapPresentation(
            engine,
            tuple(expressions),
            source_label,
            target_label,
        )
        return self.element_class(
            self,
            presentation,
        )

    @cached_method
    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only for equal complex-manifold endpoints")
        chart = self._unique_chart(self.domain())
        return self.polynomial(tuple(chart.coordinates()))


class ComplexManifoldHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return ComplexManifoldHomset


class ComplexManifolds(OwnedCategory):
    r"""Finite-dimensional complex analytic manifolds with holomorphic atlases."""

    _HomCategory = ComplexManifoldHomCategoryConstruction

    def super_categories(self):
        return [TopologicalManifolds()]

    @classmethod
    def _repr_object_names(cls):
        return "complex analytic manifolds"

    def an_object(self):
        return self.affine_space(1, name="C")

    def _call_(self, dimension, name):
        dimension = int(dimension)
        if dimension <= 0:
            raise ValueError("a complex manifold has positive complex dimension")
        engine = _SageManifold(
            dimension,
            str(name),
            field="complex",
            structure="smooth",
            unique_tag=object(),
        )
        return _object_of(
            self,
            topology_data=_ManifoldTopologyData(engine),
            engine_manifold=engine,
            manifold_dimension=dimension,
            manifold_name=str(name),
            manifold_structure="complex analytic",
            differentiability_degree=Infinity,
            manifold_field="complex",
        )

    def affine_space(self, dimension, name=None, coordinate_names=None):
        dimension = int(dimension)
        if name is None:
            name = f"C^{dimension}"
        if coordinate_names is None:
            coordinate_names = tuple(f"z{index}" for index in range(dimension))
        coordinate_names = tuple(str(name) for name in coordinate_names)
        if len(coordinate_names) != dimension:
            raise ValueError("a complex affine chart has one coordinate name per dimension")
        manifold = self(dimension, name)
        manifold.chart("standard", " ".join(coordinate_names))
        return manifold

    def _open_submanifold_data(self, containing_manifold, name, restriction):
        r"""The construction data of the open subset ``{restriction}`` of ``containing_manifold``, cut out in its one chart."""
        assert containing_manifold in self, (
            "a complex analytic open submanifold is open in a complex manifold"
        )
        labels = tuple(containing_manifold.chart_labels())
        assert len(labels) == 1, (
            "represented analytic opens are cut out in the one selected global chart"
        )
        chart = containing_manifold.atlas()[labels[0]]
        engine_open = containing_manifold._engine_manifold().open_subset(
            str(name),
            coord_def={chart._engine_chart(): restriction},
        )
        return {
            "topology_data": _ManifoldTopologyData(engine_open),
            "engine_manifold": engine_open,
            "manifold_dimension": containing_manifold.dimension(),
            "manifold_name": str(name),
            "manifold_structure": "complex analytic",
            "differentiability_degree": Infinity,
            "manifold_field": "complex",
            "containing_manifold": containing_manifold,
            "open_restriction": restriction,
            "chart_label": labels[0],
        }

    def open_submanifold(self, containing_manifold, name, restriction):
        r"""Return the open subset of ``containing_manifold`` where ``restriction`` holds in its chart."""
        return _object_of(
            self,
            _engine=(self, _ComplexOpenEngine, None),
            **self._open_submanifold_data(containing_manifold, name, restriction),
        )

    def disc(self, radius=1, name="Delta", containing_manifold=None, *, punctured=False):
        r"""Return the disc ``{|z| < radius}``, or with ``punctured`` the disc ``{0 < |z| < radius}``.

        The disc is cut out in the chart of the one-dimensional
        ``containing_manifold``; omitted, that is a fresh complex line.
        """
        radius = float(radius)
        if radius <= 0:
            raise ValueError("an analytic disc has positive radius")
        if containing_manifold is None:
            containing_manifold = self.affine_space(
                1, name=f"{name}_line", coordinate_names=("z",)
            )
        assert containing_manifold.dimension() == 1, (
            "a disc is cut out in a one-dimensional complex chart"
        )
        z = containing_manifold.atlas()[
            tuple(containing_manifold.chart_labels())[0]
        ].coordinate(0)
        match punctured:
            case True:
                restriction = (abs(z) < radius, z != 0)
            case False:
                restriction = abs(z) < radius
        return _object_of(
            self,
            _engine=(self, _ComplexDiscEngine, None),
            disc_radius=radius,
            punctured=punctured,
            **self._open_submanifold_data(containing_manifold, name, restriction),
        )

    class ParentMethods:
        def complex_dimension(self):
            return self.dimension()

        def real_dimension(self):
            return 2 * int(self.dimension())

        def is_analytic(self) -> bool:
            return True

        def regularity(self):
            return "analytic"

        def holomorphic_polynomial_map(self, codomain, coordinate_expressions):
            return self.Mor(codomain).polynomial(coordinate_expressions)

        def open_inclusion(self):
            r"""The selected ambient open inclusion, absent for a standalone construction."""
            return None

        def is_open_submanifold(self) -> bool:
            r"""Whether this construction retains an ambient open inclusion."""
            return self.open_inclusion() is not None


class _ComplexOpenEngine:
    r"""Native chart-restriction realization at ComplexManifolds, not a category.

    The retained ambient manifold and restriction determine the inclusion;
    the cooperative constructor registers the restricted native chart.
    """

    def __init__(self, containing_manifold, open_restriction, chart_label, **rest) -> None:
        self._containing_manifold = containing_manifold
        self._open_restriction = open_restriction
        super().__init__(**rest)
        self._register_chart(
            chart_label,
            containing_manifold.atlas()[chart_label]._engine_chart().restrict(
                self._engine_manifold()
            ),
        )

    def open_restriction(self):
        return self._open_restriction

    @cached_method
    def open_inclusion(self):
        r"""Return the holomorphic inclusion of this open subset into the manifold it is open in."""
        label = tuple(self.chart_labels())[0]
        coordinates = tuple(self.atlas()[label].coordinates())
        return self.Mor(self._containing_manifold).polynomial(coordinates)


class _ComplexDiscEngine(_ComplexOpenEngine):
    r"""The disc parameters refine the chart-restriction engine, not the category."""

    def __init__(self, disc_radius, punctured, **rest) -> None:
        self._disc_radius = disc_radius
        self._punctured = punctured
        super().__init__(**rest)

    def disc_radius(self):
        return self._disc_radius

    def is_punctured(self) -> bool:
        return self._punctured


__all__ = [
    "ComplexManifoldHomset",
    "ComplexManifolds",
    "DifferentiableManifolds",
    "HolomorphicMap",
    "ManifoldAtlasChart",
    "ManifoldAtlasTransition",
    "SmoothManifolds",
    "TopologicalManifolds",
]
