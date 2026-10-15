r"""Owned topological, finite-``C^k`` and smooth manifolds and atlas maps.

SageManifolds is the private chart/transition engine.  The public object keeps
the manifold's dimension and differentiability degree, an owned finite family
of labelled charts, and exact forward/inverse coordinate expressions for each
represented atlas transition.
"""

from sage.categories.category_with_axiom import all_axioms
from sage.combinat.root_system.coxeter_group import CoxeterGroup
from sage.combinat.root_system.coxeter_matrix import CoxeterMatrix
from sage.manifolds.manifold import Manifold as _SageManifold
from sage.matrix.constructor import matrix as _engine_matrix
from sage.matrix.special import identity_matrix as _engine_identity_matrix
from sage.misc.cachefunc import cached_function, cached_method
from sage.rings.infinity import Infinity
from sage.structure.element import Element
from sage.structure.element import parent as element_parent
from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject
from sage.symbolic.ring import SR

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _own_ring,
    _owned_complex_field,
    _owned_engine_element,
    _owned_integers,
)
from dzack_research.preamble.categories.sets.finite_families import finite_family
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
    indexed_family,
)
from dzack_research.preamble.categories.sets.set_categories import NN, Sets
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.logic import ask
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.rings.real import RR

for _manifold_axiom in ("GloballySymmetric", "BoundedSymmetric"):
    if _manifold_axiom not in all_axioms:
        all_axioms.add(_manifold_axiom)


class ManifoldAtlasChart(SageObject):
    r"""One labelled chart of an owned manifold."""

    def __init__(self, manifold, label, engine_chart) -> None:
        self._manifold = manifold
        self._label = label
        self._engine = engine_chart
        self._coordinates = _raise_manifold_expression_family(
            engine_chart[:],
            name=f"Coordinates of chart {label}",
        )

    def manifold(self):
        return self._manifold

    def label(self):
        return self._label

    def coordinates(self):
        return self._coordinates

    def coordinate(self, index):
        position = self.coordinates().index_set()[int(index)]
        return self.coordinates()[position]

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
        self._forward = _admit_manifold_expression_family(
            forward_expressions,
            name=f"Coordinate change {source.label()} to {target.label()}",
        )
        self._inverse_expressions = _admit_manifold_expression_family(
            inverse_expressions,
            name=f"Coordinate change {target.label()} to {source.label()}",
        )
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
        image = self._engine(
            *(_engine_manifold_expression(coordinate) for coordinate in coordinates)
        )
        return _raise_manifold_expression_family(
            image,
            name=f"Coordinates after {self.source().label()} to {self.target().label()}",
        )

    def _repr_(self):
        return (
            f"{self.regularity()} atlas transition "
            f"{self.source().label()} -> {self.target().label()}"
        )


def _engine_manifold(manifold):
    r"""Return a manifold's private Sage realization to this module's adapters.

    Protected manifold contract (\`OWN-05\`--\`OWN-07\`).  The
    implementation endpoint is
    \`TopologicalManifolds.ParentMethods._engine_manifold_realization\`.  Permitted
    callers are the point, chart, holomorphic-map, and analytic-open adapters
    in this module after the corresponding owned construction has been
    selected.  The Sage manifold remains private to those adapters.
    """
    return manifold._engine_manifold_realization()


def _engine_manifold_chart(chart):
    r"""Return a chart's private Sage realization to a manifold adapter.

    The implementation endpoint is :meth:\`ManifoldAtlasChart._engine_chart\`.
    Permitted callers are the point, transition, map, and open-submanifold
    adapters in this module.  The raw chart never becomes mathematical output.
    """
    return chart._engine_chart()


@cached_function
def _manifold_expression_ring():
    r"""Return the owned facade of Sage's exact symbolic-expression ring."""
    return _own_ring(SR)


def _raise_manifold_expression(value):
    r"""Raise one private symbolic engine expression into the owned expression ring."""
    return _owned_engine_element(_manifold_expression_ring(), value)


def _admit_manifold_expression(value):
    r"""Admit public literal/owned formula data, rejecting raw Sage expressions."""
    return _manifold_expression_ring()(value)


def _engine_manifold_expression(value):
    r"""Lower one owned chart/formula expression for a SageManifolds adapter.

    Protected manifold-expression contract under OWN-05--OWN-07.  Permitted
    callers are atlas/map/open-submanifold adapters in this module and the
    affine-analytification adapter, all of which consume the raw expression
    immediately and return owned manifold/formula data.
    """
    expression = _admit_manifold_expression(value)
    return _engine_element(_manifold_expression_ring(), expression)


def _upper_triangle(n):
    r"""The index pairs ``(i, j)``, ``i <= j < n``, of the entries of an ``n x n`` symmetric matrix."""
    return tuple((row, column) for row in range(int(n)) for column in range(row, int(n)))


def _symmetric_entry(coordinates, row, column):
    return coordinates[(min(row, column), max(row, column))]


def _skew_entry(coordinates, row, column):
    match row - column:
        case 0:
            return SR.zero()
        case difference if difference > 0:
            return -coordinates[(column, row)]
        case _:
            return coordinates[(row, column)]


def _engine_positive_definite(hermitian):
    r"""Sylvester's criterion: a Hermitian matrix is positive definite iff each leading principal minor is positive.

    The minors of a Hermitian matrix are real; the conditions compare their
    real parts with ``0`` so that the engine reads each as a real inequality.
    """
    return tuple(
        hermitian[:size, :size].det().real_part() > 0
        for size in range(1, hermitian.nrows() + 1)
    )


def _engine_positive_root_count(diagram, vertices):
    r"""``|Phi_X^+|`` for the subdiagram on ``vertices``: the length of the longest element of ``W_X``."""
    from dzack_research.preamble.categories.coxeter_diagrams import (
        _engine_coxeter_matrix_entry,
    )

    match len(vertices):
        case 0:
            return 0
        case _:
            group = CoxeterGroup(
                CoxeterMatrix(
                    [
                        [
                            _engine_coxeter_matrix_entry(diagram.coxeter_entry(left, right))
                            for right in vertices
                        ]
                        for left in vertices
                    ]
                ),
                implementation="reflection",
            )
            return group.long_element().length()


def _symmetric_space_rank_and_dimension(satake_diagram):
    r"""The real rank ``dim a_0`` and the dimension ``dim p_0`` of ``G/K`` for the real form of a Satake diagram.

    ``a_0`` is a maximal abelian subspace of ``p_0``; its dimension is the
    number of ``tau``-orbits of white nodes (Araki, 1962).  The roots
    vanishing on ``a_0`` are the roots ``Phi_X`` of the black subdiagram, so
    ``dim n_0 = |Phi^+| - |Phi_X^+|``, and the Iwasawa decomposition
    ``g_0 = k_0 + a_0 + n_0`` (Helgason, Ch. VI) gives
    ``dim G/K = dim p_0 = dim a_0 + dim n_0``.
    """
    diagram = satake_diagram.dynkin_diagram()
    tau = satake_diagram.involution()
    black = tuple(satake_diagram.black_nodes())
    vertices = tuple(diagram.index_set())
    white = tuple(vertex for vertex in vertices if vertex not in satake_diagram.black_nodes())
    rank = len({frozenset((vertex, tau(vertex))) for vertex in white})
    return rank, rank + _engine_positive_root_count(diagram, vertices) - _engine_positive_root_count(
        diagram, black
    )


def _admit_manifold_expression_family(values, *, name):
    return finite_family(
        tuple(_admit_manifold_expression(value) for value in values),
        name=name,
    )


def _raise_manifold_expression_family(values, *, name):
    return finite_family(
        tuple(_raise_manifold_expression(value) for value in values),
        name=name,
    )


def _engine_manifold_point(point):
    r"""Return a point's private Sage realization for same-manifold equality."""
    return point._engine_manifold_point()


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

    def _engine_manifold_realization(self):
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
                    f"cannot decide whether {selected} is open in the manifold {space}: "
                    f"openness is decided only for the empty set, the whole manifold, "
                    f"and open submanifolds constructed as such"
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
            raise ValueError(
                f"cannot construct a topological manifold {name} of dimension {dimension}: "
                f"the dimension must be positive"
            )
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
            self._coordinates = _admit_manifold_expression_family(
                coordinates,
                name=f"Coordinates of point of {parent}",
            )
            self._chart_label = chart_label
            self._engine_point = _engine_manifold(parent)(
                tuple(
                    _engine_manifold_expression(coordinate)
                    for coordinate in self._coordinates
                ),
                chart=_engine_manifold_chart(parent.atlas()[chart_label]),
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
                and _engine_manifold_point(other) == self._engine_manifold_point()
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
            chart_index_set=None,
            chart_provider=None,
            **rest,
        ) -> None:
            self._preamble_engine_manifold = engine_manifold
            self._preamble_manifold_dimension = NN(int(manifold_dimension))
            self._preamble_manifold_name = str(manifold_name)
            self._preamble_manifold_structure = str(manifold_structure)
            self._preamble_differentiability_degree = (
                differentiability_degree
                if differentiability_degree is None or differentiability_degree == Infinity
                else NN(int(differentiability_degree))
            )
            self._preamble_manifold_field = str(manifold_field)
            self._preamble_charts = {}
            self._preamble_chart_index_set = chart_index_set
            self._preamble_chart_provider = chart_provider
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
                raise TypeError(
                    f"{self} has no differentiability degree: it is a topological "
                    f"manifold with no differentiable structure"
                )
            return degree

        def is_smooth(self) -> bool:
            return self._preamble_differentiability_degree == Infinity

        def _engine_manifold_realization(self):
            return self._preamble_engine_manifold

        def chart(self, label, coordinates):
            return self._register_chart(label, self._engine_manifold_realization().chart(coordinates))

        def _register_chart(self, label, engine_chart):
            r"""Record the chart ``engine_chart`` of this manifold's engine under ``label``."""
            if label in self._preamble_charts:
                raise ValueError(
                    f"cannot add a chart labelled {label!r} to {self}: its atlas already "
                    f"has a chart with that label"
                )
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
                        raise ValueError(
                            f"{coordinates} are not the coordinates of a point of {self}: a "
                            f"point of a manifold of dimension {self.dimension()} has "
                            f"{self.dimension()} coordinates, not {len(coordinates)}"
                        )
                    return self.element_class(self, coordinates, chart_label)

        def point(self, coordinates, chart_label="standard"):
            return self(coordinates, chart_label)

        def chart_labels(self):
            if self._preamble_chart_index_set is not None:
                return self._preamble_chart_index_set
            return self.selected_finite_chart_labels()

        def selected_finite_chart_labels(self):
            r"""Labels in the currently registered finite chart realization."""
            return finite_ordered_set(tuple(self._preamble_charts))

        def atlas(self):
            labels = self.chart_labels()
            return indexed_family(
                labels,
                lambda label: (
                    self._preamble_charts[label]
                    if label in self._preamble_charts
                    else self._preamble_chart_provider(label)
                    if self._preamble_chart_provider is not None
                    else self._preamble_charts[label]
                ),
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
            forward_expressions = _admit_manifold_expression_family(
                forward_expressions,
                name=f"Coordinate change {source_label} to {target_label}",
            )
            inverse_expressions = _admit_manifold_expression_family(
                inverse_expressions,
                name=f"Coordinate change {target_label} to {source_label}",
            )
            if int(forward_expressions.cardinality()) != self.dimension():
                raise ValueError(
                    f"the coordinate change {source_label} -> {target_label} on {self} must "
                    f"give {self.dimension()} coordinate expressions, one per dimension, but "
                    f"{forward_expressions.cardinality()} were given"
                )
            if int(inverse_expressions.cardinality()) != self.dimension():
                raise ValueError(
                    f"the inverse coordinate change {target_label} -> {source_label} on "
                    f"{self} must give {self.dimension()} coordinate expressions, one per "
                    f"dimension, but {inverse_expressions.cardinality()} were given"
                )
            engine_transition = _engine_manifold_chart(source).transition_map(
                _engine_manifold_chart(target),
                tuple(
                    _engine_manifold_expression(expression)
                    for expression in forward_expressions
                ),
            )
            engine_transition.set_inverse(
                *(
                    _engine_manifold_expression(expression)
                    for expression in inverse_expressions
                )
            )
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
                f"{self} has no transition map from the chart {source_label!r} to the "
                f"chart {target_label!r}: none was defined with transition_map"
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
            raise ValueError(
                f"cannot construct a differentiable manifold {name} of dimension "
                f"{dimension}: the dimension must be positive"
            )
        if degree <= 0:
            raise ValueError(
                f"cannot construct a C^{degree} manifold {name}: a finite "
                f"differentiability degree must be a positive integer"
            )
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
            raise ValueError(
                f"cannot construct a smooth manifold {name} of dimension {dimension}: "
                f"the dimension must be positive"
            )
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


class RiemannianManifolds(OwnedCategory):
    r"""Smooth real manifolds ``(M, g)`` with a chosen Riemannian metric ``g``.

    The metric ``g`` is a smooth section of ``Sym^2 T^*M`` that is positive
    definite on every tangent space ``T_p M`` (Helgason, *Differential
    Geometry, Lie Groups, and Symmetric Spaces*, Ch. I, §9; Mathlib
    ``Mathlib/Topology/VectorBundle/Riemannian.lean``, ``RiemannianBundle``).
    A smooth manifold admits many metrics, so the metric is chosen data and
    this is a data subcategory of ``SmoothManifolds()``, its immediate
    supercategory: forgetting ``g`` returns the smooth manifold ``M``.

    A morphism ``(M, g) -> (N, h)`` is a smooth map ``f`` with ``f^* h = g``,
    a local isometry.  The Mor category with that condition is not presented
    yet; ``isometry_group()`` is the automorphism group of ``(M, g)`` in it.
    """

    def super_categories(self):
        return [SmoothManifolds()]

    @classmethod
    def _repr_object_names(cls):
        return "Riemannian manifolds"

    def an_object(self):
        r"""The Euclidean line ``(R, dx^2)``."""
        assert False, "an_object on RiemannianManifolds: not implemented"

    def _call_(self, manifold, metric):
        r"""Return ``(M, g)`` for a smooth manifold ``M`` and a Riemannian metric ``g`` on it.

        ``metric`` is a smooth positive definite section of ``Sym^2 T^*M``.
        The construction stores ``M`` and ``g`` and computes nothing.
        """
        assert manifold in SmoothManifolds(), (
            f"cannot equip {manifold} with the Riemannian metric {metric}: a Riemannian "
            f"metric is defined on a smooth manifold, and {manifold} is in "
            f"{manifold.category()}"
        )
        assert False, "construction of an object of RiemannianManifolds: not implemented"

    class SubcategoryMethods:
        def GloballySymmetric(self):
            r"""The axiom: every point is an isolated fixed point of an involutive isometry.

            ``(M, g)`` is a Riemannian globally symmetric space when it is a
            connected analytic Riemannian manifold and each ``p in M`` is an
            isolated fixed point of an involutive isometry ``s_p`` of ``(M, g)``
            (Helgason, Ch. IV, §3, Definition; a Riemannian manifold is
            connected by Helgason's Ch. I, §9 definition).
            """
            return self._with_axiom("GloballySymmetric")

    class ParentMethods:
        def riemannian_metric(self):
            r"""Return the chosen metric ``g``, a positive definite section of ``Sym^2 T^*M``."""
            assert False, "riemannian_metric on RiemannianManifolds: not implemented"

        def isometry_group(self):
            r"""Return ``I(M, g)``, the group of isometries ``f: M -> M`` with ``f^* g = g``.

            With the compact open topology it is a locally compact
            topological transformation group of ``M`` (Helgason, Ch. IV,
            Theorem 2.5(a)), an object of ``TopologicalGroups()``.  On a
            Riemannian globally symmetric space it is a Lie transformation
            group of ``M`` (Helgason, Ch. IV, Lemma 3.2), an object of
            ``LieGroups()``.
            """
            assert False, "isometry_group on RiemannianManifolds: not implemented"

    class GloballySymmetric(CategoryWithAxiom):
        r"""Riemannian globally symmetric spaces (Helgason, Ch. IV, §3).

        A connected analytic Riemannian manifold ``(M, g)`` in which each point ``p``
        is an isolated fixed point of an involutive isometry ``s_p``, the
        geodesic symmetry at ``p``.
        """

        def noncompact_type(self, satake_diagram):
            r"""Return the irreducible symmetric space ``G/K`` of noncompact type of a real form.

            ``satake_diagram`` is an object of ``SatakeDiagrams()`` with a
            connected Dynkin diagram, classifying a noncompact real form
            ``g_0`` of a complex simple Lie algebra.  ``G`` is a connected Lie
            group with Lie algebra ``g_0`` and finite centre, ``K`` a maximal
            compact subgroup, and ``(g_0, theta)`` with ``theta`` a Cartan
            involution is an orthogonal symmetric Lie algebra of the
            noncompact type (Helgason, Ch. V, §1, Definition; the
            irreducible spaces of this type are listed in Ch. X, §6,
            Table V).

            ``G/K`` is the orbit space of the right action of ``K`` on ``G``:
            the coequalizer in ``TopologicalSpaces()`` of the action and the
            projection ``K x G -> G``, returned by ``orbit_space()`` on the
            object of ``GObjects(K, SmoothManifolds())`` with ``k . g = g k^{-1}``;
            right translation is a diffeomorphism of ``G``, not a group morphism.
            The smooth structure and the ``G``-invariant metric induced by
            the Killing form of ``g_0`` restricted to ``p_0`` place it here.

            The construction is the smooth manifold on the one global chart
            ``Exp: p_0 -> G/K``, a diffeomorphism for noncompact type
            (Helgason, Ch. VI, Theorem 1.1), with coordinates ``x_0, ...``
            on ``p_0``.  ``dim p_0`` and the real rank are read from the
            Satake diagram by the Iwasawa decomposition.  The orbit-space
            route above and the metric are not constructed.
            """
            from dzack_research.preamble.categories.satake_diagrams import SatakeDiagrams

            assert satake_diagram in SatakeDiagrams(), (
                f"cannot construct the symmetric space of noncompact type of {satake_diagram}: "
                f"a noncompact real form of a simple Lie algebra is classified by an object "
                f"of SatakeDiagrams(), and {satake_diagram} is in {satake_diagram.category()}"
            )
            assert satake_diagram.dynkin_diagram().is_connected(), (
                f"cannot construct the irreducible symmetric space of {satake_diagram}: an "
                f"irreducible space comes from a simple Lie algebra, whose Dynkin diagram is "
                f"connected"
            )
            rank, dimension = _symmetric_space_rank_and_dimension(satake_diagram)
            assert rank >= 1, (
                f"{satake_diagram} has every node black, so it is the compact real form, and "
                f"its symmetric space G/K is a point, not of the noncompact type"
            )
            engine = _SageManifold(
                int(dimension), "G/K", structure="smooth", unique_tag=object()
            )
            space = _object_of(
                self,
                _engine=(SmoothManifolds(), _RealFormSymmetricSpace, None),
                topology_data=_ManifoldTopologyData(engine),
                engine_manifold=engine,
                manifold_dimension=int(dimension),
                manifold_name="G/K",
                manifold_structure="smooth",
                differentiability_degree=Infinity,
                manifold_field="real",
                satake_diagram=satake_diagram,
                real_rank=rank,
            )
            space.chart("p0", " ".join(f"x{index}" for index in range(int(dimension))))
            return space

        def hyperbolic_space(self, component):
            r"""Return the hyperbolic space ``HH(C^+)`` of a chosen positive-cone component.

            ``component`` is an object of ``PositiveConeComponents(L)`` for a
            lattice ``L`` of signature ``(1, n)``, the component ``C^+`` of
            ``{x in L_RR : q(x) > 0}``.  The result is the hyperboloid
            ``{x in C^+ : q(x) = 1}`` of dimension ``n``, with the metric
            ``-b`` on each tangent space ``x^perp``; it is
            ``SO_0(1, n)/SO(n)``, of Cartan type BDI with ``q = 1`` (Helgason,
            Ch. X, §6, Table V), placed in ``HyperbolicSpaces(n)``.
            """
            from dzack_research.preamble.categories.hyperbolic_geometry import (
                HyperbolicSpaces,
            )

            dimension = int(component.lattice().module_rank()) - 1
            engine = _SageManifold(
                dimension, "HH", structure="smooth", unique_tag=object()
            )
            return _object_of(
                HyperbolicSpaces(dimension),
                topology_data=_ManifoldTopologyData(engine),
                engine_manifold=engine,
                manifold_dimension=dimension,
                manifold_name="HH",
                manifold_structure="smooth",
                differentiability_degree=Infinity,
                manifold_field="real",
                component=component,
            )

        class ParentMethods:
            def geodesic_symmetry(self, point):
                r"""Return ``s_p``, the involutive isometry of ``M`` with isolated fixed point ``p``.

                Domain and codomain are ``M``; ``s_p`` reverses every geodesic
                through ``p`` and its differential at ``p`` is ``-1`` on
                ``T_p M``.
                """
                assert False, "geodesic_symmetry on RiemannianManifolds.GloballySymmetric: not implemented"


class HolomorphicMapPresentation:
    r"""The selected chart presentation defining one represented holomorphic map."""

    def __init__(self, engine_map, coordinate_expressions, source_label, target_label) -> None:
        self._engine_map = engine_map
        self._coordinate_expressions = _admit_manifold_expression_family(
            coordinate_expressions,
            name="Holomorphic-map coordinate expressions",
        )
        self._source_label = source_label
        self._target_label = target_label

    def _engine_map_crossing(self):
        return self._engine_map

    def coordinate_expressions(self):
        return self._coordinate_expressions

    def source_chart_label(self):
        return self._source_label

    def target_chart_label(self):
        return self._target_label


def _engine_holomorphic_map(morphism):
    r"""Return a holomorphic map's private Sage realization to its composition adapter.

    Protected holomorphic-map contract (\`OWN-05\`--\`OWN-07\`).  The
    implementation endpoint is :meth:\`HolomorphicMap._engine_holomorphic_map\`.
    Its sole external role is exact composition of represented holomorphic
    maps; the resulting Sage map is immediately raised by
    :func:\`_holomorphic_map_from_engine\`.
    """
    return morphism._engine_holomorphic_map()


def _holomorphic_map_from_engine(
    mor,
    engine,
    expressions,
    source_label,
    target_label,
):
    r"""Raise a private Sage map into the selected owned holomorphic Mor object."""
    return mor._from_engine_polynomial_map(
        engine,
        _raise_manifold_expression_family(
            expressions,
            name="Holomorphic-map coordinate expressions",
        ),
        source_label,
        target_label,
    )


class HolomorphicMap:
    r"""A holomorphic map represented by polynomial formulas in selected complex charts."""

    def __init__(self, parent, presentation) -> None:
        self._presentation = presentation
        set_map = Sets().Mor(parent.domain(), parent.codomain())(
            lambda point: self._evaluate_point(point)
        )
        super().__init__(parent, set_map)

    def presentation(self):
        return self._presentation

    def coordinate_expressions(self):
        return self.presentation().coordinate_expressions()

    def source_chart(self):
        return self.domain().atlas()[self.presentation().source_chart_label()]

    def target_chart(self):
        return self.codomain().atlas()[self.presentation().target_chart_label()]

    def _engine_holomorphic_map(self):
        return self.presentation()._engine_map_crossing()

    def _evaluate_point(self, point):
        r"""Evaluate the retained chart formulas on one owned source point."""
        source_point = self.domain()(point)
        source_chart = self.source_chart()
        assert source_point.chart().label() == source_chart.label(), (
            f"cannot evaluate {self} at {source_point}: its coordinates are in the chart "
            f"{source_point.chart().label()!r}, while this represented holomorphic map is written in "
            f"{source_chart.label()!r}"
        )
        substitutions = {
            _engine_manifold_expression(variable): _engine_manifold_expression(value)
            for variable, value in zip(
                source_chart.coordinates(),
                source_point.coordinates(),
                strict=True,
            )
        }
        values = tuple(
            _raise_manifold_expression(
                _engine_manifold_expression(expression).subs(substitutions)
            )
            for expression in self.coordinate_expressions()
        )
        return self.codomain().point(values, self.target_chart().label())

    def __mul__(self, other):
        r"""Return the composite ``self o other`` of holomorphic maps ``X -> Y -> Z``."""
        assert other.codomain() is self.domain(), (
            f"cannot compose {self} with {other}: the codomain {other.codomain()} of the "
            f"first map is not the domain {self.domain()} of the second"
        )
        engine = _engine_holomorphic_map(self) * _engine_holomorphic_map(other)
        source = other.source_chart()
        target = self.target_chart()
        # SageManifolds returns the coordinate expressions of a map as a tuple
        # in every dimension (``MultiCoordFunction.expr``).
        expressions = engine.expr(
            _engine_manifold_chart(source),
            _engine_manifold_chart(target),
        )
        return _holomorphic_map_from_engine(
            other.domain().Mor(self.codomain()),
            engine,
            expressions,
            source.label(),
            target.label(),
        )

    def __eq__(self, other) -> bool:
        return (
            element_parent(other) is self.parent()
            and other.coordinate_expressions() == self.coordinate_expressions()
            and other.source_chart().label() == self.source_chart().label()
            and other.target_chart().label() == self.target_chart().label()
        )

    def __ne__(self, other) -> bool:
        return not self == other

    __hash__ = None

    def _repr_(self):
        return f"Holomorphic map {self.domain()} -> {self.codomain()}"


class ComplexManifoldMor(CategoricalMor):
    ElementMethods = HolomorphicMap

    def __init__(self, mor_family, domain, codomain) -> None:
        CategoricalMor.__init__(self, mor_family, domain, codomain)

    @staticmethod
    def _unique_chart(manifold):
        labels = tuple(manifold.chart_labels())
        assert len(labels) == 1, (
            f"cannot write a holomorphic map on {manifold} by polynomial formulas: the "
            f"formulas are taken in a single global chart, but {manifold} has the charts "
            f"{labels}"
        )
        return manifold.atlas()[labels[0]]

    def polynomial(self, coordinate_expressions):
        r"""Construct the holomorphic map defined by polynomial chart formulas."""
        source = self._unique_chart(self.domain())
        target = self._unique_chart(self.codomain())
        expressions = _admit_manifold_expression_family(
            coordinate_expressions,
            name="Holomorphic-map coordinate expressions",
        )
        if int(expressions.cardinality()) != self.codomain().dimension():
            raise ValueError(
                f"{coordinate_expressions} do not define a holomorphic map {self.domain()} -> "
                f"{self.codomain()}: it needs one expression per coordinate of the codomain, "
                f"that is {self.codomain().dimension()}, but {expressions.cardinality()} "
                f"were given"
            )
        engine_variables = tuple(
            _engine_manifold_expression(variable)
            for variable in source.coordinates()
        )
        engine_expressions = tuple(
            _engine_manifold_expression(expression)
            for expression in expressions
        )
        if any(
            not all(expression.is_polynomial(variable) for variable in engine_variables)
            for expression in engine_expressions
        ):
            raise ValueError(
                f"cannot conclude that {coordinate_expressions} define a holomorphic map "
                f"{self.domain()} -> {self.codomain()}: holomorphicity is known here only "
                f"for formulas polynomial in the coordinates {source.coordinates()}, and "
                f"some formula is not"
            )
        engine = _engine_manifold(self.domain()).diff_map(
            _engine_manifold(self.codomain()),
            engine_expressions if len(engine_expressions) != 1 else engine_expressions[0],
            chart1=_engine_manifold_chart(source),
            chart2=_engine_manifold_chart(target),
        )
        return self._from_engine_polynomial_map(
            engine, expressions, source.label(), target.label()
        )

    def _from_engine_polynomial_map(self, engine, expressions, source_label, target_label):
        presentation = HolomorphicMapPresentation(
            engine,
            expressions,
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
            raise ValueError(
                f"there is no identity map from {self.domain()} to {self.codomain()}: an "
                f"identity needs its domain and codomain to be the same complex manifold"
            )
        chart = self._unique_chart(self.domain())
        return self.polynomial(chart.coordinates())


class ComplexManifoldMorCategoryConstruction(MorCategoryConstruction):
    def fixed_category_class(self):
        return ComplexManifoldMor


class ComplexManifolds(OwnedCategory):
    r"""Finite-dimensional complex analytic manifolds with holomorphic atlases.

    A holomorphic map between open subsets of ``C^n`` and ``C^m`` is real
    analytic, so in particular ``C^infinity``, as a map between open subsets of
    ``R^{2n}`` and ``R^{2m}``.  A holomorphic atlas is therefore a smooth atlas
    of the underlying real manifold, of real dimension twice the complex
    dimension, and a holomorphic map is smooth.  Forgetting the complex
    structure is the functor to ``SmoothManifolds()``, the immediate
    supercategory.
    """

    _MorCategory = ComplexManifoldMorCategoryConstruction

    def super_categories(self):
        return [SmoothManifolds()]

    @classmethod
    def _repr_object_names(cls):
        return "complex analytic manifolds"

    def an_object(self):
        return self.affine_space(1, name="C")

    def _call_(self, dimension, name):
        dimension = int(dimension)
        if dimension <= 0:
            raise ValueError(
                f"cannot construct a complex manifold {name} of complex dimension "
                f"{dimension}: the dimension must be positive"
            )
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
            raise ValueError(
                f"cannot construct complex affine space {name} of dimension {dimension} "
                f"with the coordinates {coordinate_names}: it needs {dimension} coordinate "
                f"names, one per dimension, but {len(coordinate_names)} were given"
            )
        manifold = self(dimension, name)
        manifold.chart("standard", " ".join(coordinate_names))
        return manifold

    def _open_submanifold_data(self, containing_manifold, name, restriction):
        r"""The construction data of the open subset ``{restriction}`` of ``containing_manifold``, cut out in its one chart."""
        assert containing_manifold in self, (
            f"cannot cut out the open submanifold {name} of {containing_manifold}: it "
            f"must be an open subset of a complex manifold, and {containing_manifold} is "
            f"in {containing_manifold.category()}"
        )
        labels = tuple(containing_manifold.chart_labels())
        assert len(labels) == 1, (
            f"cannot cut out the open submanifold {name} of {containing_manifold} by "
            f"{restriction}: the condition is read in a single global chart, but "
            f"{containing_manifold} has the charts {labels}"
        )
        chart = containing_manifold.atlas()[labels[0]]
        engine_open = _engine_manifold(containing_manifold).open_subset(
            str(name),
            coord_def={_engine_manifold_chart(chart): restriction},
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
        ``containing_manifold``; omitted, that is a fresh complex line.  The
        radius is an exact positive real number, an element of ``RR``.
        """
        radius = RR(radius)
        assert ask(radius > RR.zero()) is True, (
            f"cannot construct the disc {name} of radius {radius}: the radius must be "
            f"a positive real number"
        )
        if containing_manifold is None:
            containing_manifold = self.affine_space(
                1, name=f"{name}_line", coordinate_names=("z",)
            )
        assert containing_manifold.dimension() == 1, (
            f"cannot cut out the disc {name} in {containing_manifold}: a disc lies in a "
            f"complex manifold of dimension one, and {containing_manifold} has dimension "
            f"{containing_manifold.dimension()}"
        )
        z = containing_manifold.atlas()[
            tuple(containing_manifold.chart_labels())[0]
        ].coordinate(0)
        engine_z = _engine_manifold_expression(z)
        match punctured:
            case True:
                restriction = (abs(engine_z) < radius.expression(), engine_z != 0)
            case False:
                restriction = abs(engine_z) < radius.expression()
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

    class SubcategoryMethods:
        def BoundedSymmetric(self):
            r"""The axiom: biholomorphic to a bounded symmetric domain.

            A bounded domain ``D`` in ``C^N`` is symmetric when each
            ``p in D`` is an isolated fixed point of an involutive
            biholomorphism of ``D`` (Helgason, Ch. VIII, §7).  The property
            is invariant under biholomorphism, so it is a property of a
            complex manifold, stated by an axiom on ``ComplexManifolds()``.
            Its objects are the Hermitian symmetric spaces of the
            noncompact type with their complex structure (Helgason,
            Ch. VIII, §7, the Harish-Chandra realization).
            """
            return self._with_axiom("BoundedSymmetric")

    class BoundedSymmetric(CategoryWithAxiom):
        r"""Complex manifolds biholomorphic to a bounded symmetric domain (Helgason, Ch. VIII, §7).

        Each object is a product of irreducible ones, and an irreducible
        object is ``G/K`` for ``G`` the identity component of its
        biholomorphism group, a noncompact simple Lie group whose real form
        has a Satake diagram of Hermitian type (Helgason, Ch. X, §6,
        Table V).  The irreducible ones are the four classical families
        ``I_{p,q}``, ``II_n``, ``III_n``, ``IV_n`` and the two exceptional
        domains ``EIII`` and ``EVII``.  The Bergman metric is invariant
        under every biholomorphism and makes the domain a Riemannian
        globally symmetric space of noncompact type.
        """

        def type_I(self, p, q):
            r"""Return ``I_{p,q} = SU(p, q)/S(U(p) x U(q))``, Cartan type AIII.

            Bounded realization ``{Z in M_{p x q}(C) : 1_q - Z^* Z > 0}``,
            of complex dimension ``pq``, for positive integers ``p`` and
            ``q``.  ``I_{1,1}`` is the disc, biholomorphic to
            ``upper_half_plane()``.  The positivity of the Hermitian matrix
            ``1_q - Z^* Z`` is read by Sylvester's criterion: every leading
            principal minor is positive.
            """
            assert p >= 1 and q >= 1, (
                f"I_{{p,q}} is defined for positive integers p and q, not p = {p}, q = {q}"
            )
            index_pairs = tuple(
                (row, column) for row in range(int(p)) for column in range(int(q))
            )
            space, coordinates = self._matrix_coordinate_space(f"I_{p}_{q}", index_pairs)
            matrix = _engine_matrix(
                SR, int(p), int(q), lambda row, column: coordinates[(row, column)]
            )
            return self._bounded_open_domain(
                space,
                f"I_{p}_{q}",
                _engine_positive_definite(
                    _engine_identity_matrix(SR, int(q)) - matrix.conjugate_transpose() * matrix
                ),
            )

        def type_II(self, n):
            r"""Return ``II_n = SO^*(2n)/U(n)``, Cartan type DIII.

            Bounded realization ``{Z in M_n(C) : Z^t = -Z, 1_n - Z^* Z > 0}``,
            of complex dimension ``n(n - 1)/2``, for an integer ``n >= 2``;
            the coordinates are the entries ``z_{ij}``, ``i < j``.
            """
            assert n >= 2, f"II_n is defined for integers n >= 2, not n = {n}"
            index_pairs = tuple(
                (row, column) for row in range(int(n)) for column in range(row + 1, int(n))
            )
            space, coordinates = self._matrix_coordinate_space(f"II_{n}", index_pairs)
            matrix = _engine_matrix(
                SR, int(n), int(n), lambda row, column: _skew_entry(coordinates, row, column)
            )
            return self._bounded_open_domain(
                space,
                f"II_{n}",
                _engine_positive_definite(
                    _engine_identity_matrix(SR, int(n)) - matrix.conjugate_transpose() * matrix
                ),
            )

        def type_III(self, n):
            r"""Return ``III_n = Sp_{2n}(RR)/U(n)``, Cartan type CI.

            Bounded realization ``{Z in M_n(C) : Z^t = Z, 1_n - Z^* Z > 0}``,
            of complex dimension ``n(n + 1)/2``, for a positive integer
            ``n``; the coordinates are the entries ``z_{ij}``, ``i <= j``.
            The Cayley transform identifies it with
            ``siegel_upper_half_space(n)``; ``III_1 = I_{1,1}``.
            """
            assert n >= 1, f"III_n is defined for positive integers n, not n = {n}"
            space, coordinates = self._matrix_coordinate_space(
                f"III_{n}", _upper_triangle(n)
            )
            matrix = _engine_matrix(
                SR, int(n), int(n), lambda row, column: _symmetric_entry(coordinates, row, column)
            )
            return self._bounded_open_domain(
                space,
                f"III_{n}",
                _engine_positive_definite(
                    _engine_identity_matrix(SR, int(n)) - matrix.conjugate_transpose() * matrix
                ),
            )

        def type_IV(self, n):
            r"""Return ``IV_n = SO_0(2, n)/(SO(2) x SO(n))``, Cartan type BDI with ``q = 2``.

            For a real quadratic space ``V`` of signature ``(2, n)`` it is
            one connected component of
            ``{[omega] in P(V_C) : (omega, omega) = 0, (omega, bar omega) > 0}``,
            the space of oriented positive definite real ``2``-planes in
            ``V``, of complex dimension ``n``, for a positive integer ``n``
            (lean-categories FOUNDATIONS, Definition 61.3, which states the
            two components and that choosing one is additional data;
            ``LeanCategories/Lattices/Valued/PeriodDomainData.lean``,
            ``latticePeriodDomainData``).

            The construction is the tube domain
            ``{z in C^n : Im z in C^+}``, ``C^+ = {y : y_1 > 0, (y, y) > 0}``
            for ``(y, y) = y_1^2 - y_2^2 - ... - y_n^2``.  Write
            ``V = U + W`` with ``U`` a hyperbolic plane on ``e, f`` and ``W``
            of signature ``(1, n - 1)``.  A line with ``(omega, e) != 0`` has
            the unique representative ``omega = -(z, z)/2 e + f + z``,
            ``z in W_C``, which is isotropic, and
            ``(omega, bar omega) = 2 (Im z, Im z)``.  No line of the period
            domain has ``(omega, e) = 0``: then ``Re omega`` and
            ``Im omega`` would span a positive definite real ``2``-plane in
            ``e^perp/e = W``, which has one positive direction.  The two
            components of ``{(y, y) > 0}`` are the two components of the
            period domain, and ``y_1 > 0`` chooses one.
            """
            assert n >= 1, f"IV_n is defined for positive integers n, not n = {n}"
            space, coordinates = self._matrix_coordinate_space(
                f"IV_{n}", tuple((0, index) for index in range(int(n)))
            )
            imaginary = tuple(
                coordinates[(0, index)].imag_part() for index in range(int(n))
            )
            return self._bounded_open_domain(
                space,
                f"IV_{n}",
                (
                    imaginary[0] > 0,
                    imaginary[0] ** 2 - sum(y**2 for y in imaginary[1:]) > 0,
                ),
            )

        def type_EIII(self):
            r"""Return ``E_{6(-14)}/(Spin(10) x U(1))``, of complex dimension ``16``.

            Built on the Satake diagram of ``E_{6(-14)}`` (Araki, 1962): in
            Bourbaki's labels the black nodes are ``3, 4, 5`` and ``tau``
            swaps ``1 <-> 6`` and ``3 <-> 5``; real rank ``2``.  The vertices
            of the session's ``E6`` diagram are Bourbaki's labels minus one.
            The bounded realization is ``harish_chandra_realization()``.
            """
            return self._exceptional_domain("EIII", "E6", (2, 3, 4), (5, 1, 4, 3, 2, 0))

        def type_EVII(self):
            r"""Return ``E_{7(-25)}/(E_6 x U(1))``, of complex dimension ``27``.

            Built on the Satake diagram of ``E_{7(-25)}`` (Araki, 1962): in
            Bourbaki's labels the black nodes are ``2, 3, 4, 5`` and ``tau``
            is the identity; real rank ``3``.  The vertices of the session's
            ``E7`` diagram are Bourbaki's labels minus one.
            """
            return self._exceptional_domain("EVII", "E7", (1, 2, 3, 4), (0, 1, 2, 3, 4, 5, 6))

        def _exceptional_domain(self, name, cartan_name, black_nodes, involution_images):
            r"""The Hermitian symmetric domain ``G/K`` of the real form with the given Satake diagram.

            Its complex dimension is ``dim p_0 / 2``; the complex manifold has
            no chart until its Harish-Chandra realization is constructed.
            """
            from dzack_research.preamble.categories.lattices import Lattices
            from dzack_research.preamble.categories.satake_diagrams import SatakeDiagrams

            diagram = Lattices(_owned_integers())(cartan_name).dynkin_diagram()
            satake = SatakeDiagrams()(
                diagram, black_nodes, diagram.Mor(diagram)(involution_images)
            )
            rank, dimension = _symmetric_space_rank_and_dimension(satake)
            engine = _SageManifold(
                dimension // 2,
                name,
                field="complex",
                structure="smooth",
                unique_tag=object(),
            )
            return _object_of(
                self,
                _engine=(SmoothManifolds(), _RealFormSymmetricSpace, None),
                topology_data=_ManifoldTopologyData(engine),
                engine_manifold=engine,
                manifold_dimension=dimension // 2,
                manifold_name=name,
                manifold_structure="complex analytic",
                differentiability_degree=Infinity,
                manifold_field="complex",
                satake_diagram=satake,
                real_rank=rank,
            )

        def upper_half_plane(self, name="HH"):
            r"""Return the upper half-plane ``{tau in C : Im(tau) > 0}``.

            It is ``SL_2(RR)/SO(2)``, the domain ``I_{1,1} = III_1``, by the
            Cayley transform ``tau -> (tau - i)/(tau + i)`` onto the disc.
            The construction is the open subset of a fresh complex line
            cut out by ``Im(tau) > 0`` in its chart.
            """
            complex_manifolds = self.base_category()
            line = complex_manifolds.affine_space(
                1, name=f"{name}_line", coordinate_names=("tau",)
            )
            tau = _engine_manifold_expression(
                line.atlas()[tuple(line.chart_labels())[0]].coordinate(0)
            )
            return _object_of(
                self,
                _engine=(complex_manifolds, _ComplexOpenEngine, None),
                **complex_manifolds._open_submanifold_data(
                    line, name, tau.imag_part() > 0
                ),
            )

        def siegel_upper_half_space(self, g):
            r"""Return ``H_g = {Z in M_g(C) : Z^t = Z, Im(Z) > 0}``, the Siegel upper half-space.

            It is ``Sp_{2g}(RR)/U(g)``, the domain ``III_g``, of complex
            dimension ``g(g + 1)/2``, for a positive integer ``g``;
            ``H_1 = upper_half_plane()``.  The coordinates are the entries
            ``z_{ij}``, ``i <= j``, of ``Z``, and the positive definiteness
            of the real symmetric matrix ``Im(Z)`` is read by Sylvester's
            criterion: every leading principal minor is positive.
            """
            assert g >= 1, f"H_g is defined for positive integers g, not g = {g}"
            space, coordinates = self._matrix_coordinate_space(
                f"H_{g}", _upper_triangle(g)
            )
            imaginary = _engine_matrix(
                SR,
                int(g),
                int(g),
                lambda row, column: _symmetric_entry(coordinates, row, column).imag_part(),
            )
            return self._bounded_open_domain(
                space, f"H_{g}", _engine_positive_definite(imaginary)
            )

        def _matrix_coordinate_space(self, name, index_pairs):
            r"""The complex affine space with one coordinate ``z_i_j`` per index pair, and its engine coordinates."""
            space = self.base_category().affine_space(
                len(index_pairs),
                name=f"{name}_space",
                coordinate_names=tuple(f"z_{row}_{column}" for row, column in index_pairs),
            )
            chart = space.atlas()[tuple(space.chart_labels())[0]]
            return space, {
                pair: _engine_manifold_expression(chart.coordinate(index))
                for index, pair in enumerate(index_pairs)
            }

        def _bounded_open_domain(self, space, name, restriction):
            r"""The open subset of ``space`` cut out by ``restriction``, an object of this category."""
            complex_manifolds = self.base_category()
            return _object_of(
                self,
                _engine=(complex_manifolds, _ComplexOpenEngine, None),
                **complex_manifolds._open_submanifold_data(space, name, restriction),
            )

        class ParentMethods:
            def harish_chandra_realization(self):
                r"""Return the biholomorphism onto a bounded symmetric domain in ``C^N``.

                Domain ``D``; codomain the open subset of
                ``ComplexManifolds().affine_space(N)`` that it realizes,
                ``N`` the complex dimension of ``D`` (Helgason, Ch. VIII,
                §7).
                """
                assert False, "harish_chandra_realization on ComplexManifolds.BoundedSymmetric: not implemented"

            def bergman_metric_space(self):
                r"""Return ``(D, g_B)``, ``D`` with its Bergman metric.

                The result is an object of
                ``RiemannianManifolds().GloballySymmetric()`` of noncompact
                type; for irreducible ``D`` it is
                ``noncompact_type(satake_diagram)`` for the Satake diagram of
                the real form ``Lie(Aut(D)^0)``.
                """
                assert False, "bergman_metric_space on ComplexManifolds.BoundedSymmetric: not implemented"


class _RealFormSymmetricSpace:
    r"""The symmetric space ``G/K`` of a real form, built on its Satake diagram; a realization, not a category.

    The Satake diagram classifies the real form ``g_0 = Lie(G)`` (Araki,
    1962), so it is the datum the construction is on; the real rank
    ``dim a_0`` is read from it.
    """

    def __init__(self, satake_diagram, real_rank, **rest) -> None:
        self._satake_diagram = satake_diagram
        self._real_rank = real_rank
        super().__init__(**rest)

    def satake_diagram(self):
        r"""Return the Satake diagram of the real form ``g_0`` of which this is ``G/K``."""
        return self._satake_diagram

    def real_rank(self):
        r"""Return ``dim a_0``, the rank of the symmetric space: the number of ``tau``-orbits of white nodes."""
        return self._real_rank

    def _repr_(self):
        diagram = self._satake_diagram
        return (
            f"{self.dimension()}-dimensional {self.manifold_structure()} symmetric space "
            f"{self.manifold_name()} of real rank {self._real_rank}, of the real form of "
            f"{diagram.dynkin_diagram().scaled_cartan_type()} with black nodes "
            f"{tuple(diagram.black_nodes())} and involution "
            f"{tuple(diagram.involution()(vertex) for vertex in diagram.dynkin_diagram().index_set())}"
        )


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
            _engine_manifold_chart(containing_manifold.atlas()[chart_label]).restrict(
                self._engine_manifold_realization()
            ),
        )

    def _engine_open_restriction(self):
        return self._open_restriction

    @cached_method
    def open_inclusion(self):
        r"""Return the holomorphic inclusion of this open subset into the manifold it is open in."""
        label = tuple(self.chart_labels())[0]
        coordinates = self.atlas()[label].coordinates()
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

    def _element_constructor_(self, datum, chart_label="standard"):
        r"""Return the point ``z`` of the disc for a complex number ``z``, or the point with coordinates ``datum``.

        A point of the disc ``{|z| < r}`` is a complex number ``z`` with
        ``|z| < r``, and ``z != 0`` when the disc is punctured: its one
        coordinate in the chart cut out of the line.  The chart restriction
        decides membership.
        """
        match datum:
            case _ if element_parent(datum) is self:
                return datum
            case _ if datum in _owned_complex_field():
                return super()._element_constructor_((datum,), chart_label)
            case _:
                return super()._element_constructor_(datum, chart_label)


__all__ = [
    "ComplexManifoldMor",
    "ComplexManifolds",
    "DifferentiableManifolds",
    "HolomorphicMap",
    "ManifoldAtlasChart",
    "ManifoldAtlasTransition",
    "RiemannianManifolds",
    "SmoothManifolds",
    "TopologicalManifolds",
]
